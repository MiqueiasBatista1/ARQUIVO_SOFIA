"""Groq transcription adapter using the installed Groq SDK lazily."""

from __future__ import annotations

import os
import wave
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from ..schemas.contracts import (
    TranscriptError,
    TranscriptResult,
    TranscriptSegment,
    TranscriptStatus,
    TranscriptionErrorCode,
)


class GroqTranscriptionAdapter:
    """Transcribe PCM WAV through Groq without leaking provider details upstream."""

    def __init__(
        self,
        model: str | None,
        api_key: str | None = None,
        default_language: str | None = None,
        client_factory: Callable[..., Any] | None = None,
    ) -> None:
        self.model = model.strip() if model and model.strip() else None
        self.api_key = api_key
        self.default_language = default_language
        self.client_factory = client_factory

    def transcribe(self, audio_path: Path, language: str | None = None) -> TranscriptResult:
        path = Path(audio_path).expanduser()
        source_audio = str(path.resolve())
        selected_language = language or self.default_language

        if not path.is_file():
            return self._error(
                source_audio, TranscriptionErrorCode.AUDIO_NOT_FOUND,
                f"Audio file does not exist: {source_audio}", "FileNotFoundError",
            )
        try:
            self._validate_wav(path)
        except (OSError, EOFError, ValueError, wave.Error) as exc:
            return self._error(
                source_audio, TranscriptionErrorCode.AUDIO_INVALID,
                f"Audio is not a readable, non-empty WAV: {exc}", type(exc).__name__,
            )

        if not self.model:
            return self._error(
                source_audio, TranscriptionErrorCode.PROVIDER_NOT_CONFIGURED,
                "SOFIA_TRANSCRIPTION_MODEL is required; no model was selected.",
                "ConfigurationError",
            )
        if not self.api_key and not os.environ.get("GROQ_API_KEY"):
            return self._error(
                source_audio, TranscriptionErrorCode.PROVIDER_NOT_CONFIGURED,
                "Groq requires GROQ_API_KEY in the process environment.",
                "ConfigurationError",
            )

        try:
            audio_file = path.open("rb")
        except OSError as exc:
            return self._error(
                source_audio, TranscriptionErrorCode.AUDIO_INVALID,
                f"Audio WAV could not be opened: {exc}", type(exc).__name__,
            )

        try:
            client = self._make_client()
            request: dict[str, Any] = {
                "model": self.model,
                "file": audio_file,
                "response_format": "verbose_json",
                "timestamp_granularities": ["segment"],
            }
            if selected_language:
                request["language"] = selected_language
            raw_response = client.audio.transcriptions.with_raw_response.create(**request)
            payload = self._response_json(raw_response)
        except Exception as exc:  # SDK and HTTP errors are normalized to a typed result.
            code = self._classify_provider_error(exc, selected_language)
            return self._error(
                source_audio, code, self._safe_message(exc), type(exc).__name__,
            )
        finally:
            audio_file.close()

        return self._result_from_payload(payload, source_audio)

    @staticmethod
    def _validate_wav(path: Path) -> None:
        with wave.open(str(path), "rb") as wav_file:
            if (
                wav_file.getnframes() <= 0
                or wav_file.getframerate() <= 0
                or wav_file.getnchannels() <= 0
                or wav_file.getsampwidth() <= 0
            ):
                raise ValueError("WAV contains no readable audio frames")
            # Read one frame to detect truncated/invalid PCM content.
            if not wav_file.readframes(1):
                raise ValueError("WAV contains no readable audio frames")

    def _make_client(self) -> Any:
        factory = self.client_factory
        if factory is None:
            try:
                from groq import Groq
            except ImportError as exc:
                raise RuntimeError("Groq SDK is unavailable; install the groq package") from exc
            factory = Groq
        return factory(api_key=self.api_key or os.environ.get("GROQ_API_KEY"))

    @staticmethod
    def _response_json(response: Any) -> Mapping[str, Any]:
        http_response = getattr(response, "http_response", None)
        payload = http_response.json() if http_response is not None else response
        if not isinstance(payload, Mapping):
            raise ValueError("Groq returned a non-object transcription response")
        return payload

    def _result_from_payload(
        self, payload: Mapping[str, Any], source_audio: str
    ) -> TranscriptResult:
        provider_language = payload.get("language")
        language = provider_language if isinstance(provider_language, str) and provider_language.strip() else None
        segments_payload = payload.get("segments")
        segments: list[TranscriptSegment] = []
        omitted_timestamps = False
        omitted_segments = False

        if isinstance(segments_payload, list):
            for item in segments_payload:
                if not isinstance(item, Mapping):
                    omitted_segments = True
                    continue
                text = item.get("text")
                if not isinstance(text, str) or not text.strip():
                    omitted_segments = True
                    continue
                start, end = item.get("start"), item.get("end")
                valid_times = (
                    isinstance(start, (int, float)) and not isinstance(start, bool)
                    and isinstance(end, (int, float)) and not isinstance(end, bool)
                )
                if not valid_times:
                    start = end = None
                    omitted_timestamps = True
                confidence = item.get("confidence")
                if (
                    not isinstance(confidence, (int, float))
                    or isinstance(confidence, bool)
                    or not 0 <= confidence <= 1
                ):
                    confidence = None
                speaker = item.get("speaker")
                if not isinstance(speaker, str) or not speaker.strip():
                    speaker = None
                segment_language = item.get("language")
                if not isinstance(segment_language, str) or not segment_language.strip():
                    segment_language = language
                try:
                    segments.append(TranscriptSegment(
                        float(start) if start is not None else None,
                        float(end) if end is not None else None,
                        text,
                        segment_language,
                        float(confidence) if confidence is not None else None,
                        speaker,
                    ))
                except (TypeError, ValueError, OverflowError):
                    # Keep recognized words without fabricated/invalid timing metadata.
                    segments.append(TranscriptSegment(
                        None, None, text, segment_language,
                        float(confidence) if confidence is not None else None,
                        speaker,
                    ))
                    omitted_timestamps = True

        if segments:
            if omitted_timestamps or omitted_segments:
                reason = "Groq returned incomplete segment data."
                if omitted_timestamps:
                    reason = "Groq returned text for some segments without usable timestamps."
                return TranscriptResult(
                    TranscriptStatus.PARTIAL, tuple(segments), language, "groq", self.model,
                    source_audio,
                    TranscriptError(
                        TranscriptionErrorCode.TRANSCRIPTION_FAILED,
                        reason,
                        "IncompleteProviderResponse",
                    ),
                )
            return TranscriptResult(
                TranscriptStatus.SUCCESS, tuple(segments), language, "groq", self.model, source_audio
            )

        full_text = payload.get("text")
        if isinstance(full_text, str) and full_text.strip():
            segment = TranscriptSegment(None, None, full_text, language)
            return TranscriptResult(
                TranscriptStatus.PARTIAL, (segment,), language, "groq", self.model, source_audio,
                TranscriptError(
                    TranscriptionErrorCode.TRANSCRIPTION_FAILED,
                    "Groq returned transcript text without segment timestamps.",
                    "IncompleteProviderResponse",
                ),
            )

        # An empty transcript is a valid provider response and may indicate no audible speech.
        return TranscriptResult(
            TranscriptStatus.SUCCESS, (), language, "groq", self.model, source_audio
        )

    @staticmethod
    def _classify_provider_error(
        exc: Exception, language: str | None
    ) -> TranscriptionErrorCode:
        name = type(exc).__name__.lower()
        status_code = getattr(exc, "status_code", None)
        message = str(exc).lower()
        if "authentication" in name or status_code in (401, 403):
            return TranscriptionErrorCode.PROVIDER_AUTH_ERROR
        if "ratelimit" in name or status_code == 429:
            return TranscriptionErrorCode.PROVIDER_RATE_LIMIT
        if "connection" in name or "timeout" in name or (
            isinstance(status_code, int) and status_code >= 500
        ):
            return TranscriptionErrorCode.PROVIDER_UNAVAILABLE
        if "sdk is unavailable" in message:
            return TranscriptionErrorCode.PROVIDER_NOT_CONFIGURED
        if language and status_code in (400, 422) and "language" in message and (
            "support" in message or "invalid" in message or "unsupported" in message
        ):
            return TranscriptionErrorCode.UNSUPPORTED_LANGUAGE
        return TranscriptionErrorCode.TRANSCRIPTION_FAILED

    def _safe_message(self, exc: Exception) -> str:
        message = str(exc).strip() or "The transcription provider returned an unspecified error."
        secret = self.api_key or os.environ.get("GROQ_API_KEY")
        if secret:
            message = message.replace(secret, "[REDACTED]")
        return message

    def _error(
        self, source_audio: str, code: TranscriptionErrorCode, message: str,
        cause_type: str,
    ) -> TranscriptResult:
        return TranscriptResult(
            status=TranscriptStatus.ERROR,
            provider="groq",
            model=self.model,
            source_audio=source_audio,
            error=TranscriptError(code, message, cause_type),
        )


class _UnconfiguredTranscriber:
    def __init__(self, provider: str) -> None:
        self.provider = provider

    def transcribe(self, audio_path: Path, language: str | None = None) -> TranscriptResult:
        path = Path(audio_path).expanduser().resolve()
        return TranscriptResult(
            TranscriptStatus.ERROR,
            language=language,
            provider=self.provider,
            source_audio=str(path),
            error=TranscriptError(
                TranscriptionErrorCode.PROVIDER_NOT_CONFIGURED,
                f"Unsupported transcription provider configuration: {self.provider!r}.",
                "ConfigurationError",
            ),
        )


def transcriber_from_environment(environ: Mapping[str, str] | None = None) -> Any | None:
    """Select a provider from environment without supplying an implicit model."""
    settings = os.environ if environ is None else environ
    provider = settings.get("SOFIA_TRANSCRIPTION_PROVIDER", "").strip().lower()
    if not provider or provider in {"none", "disabled"}:
        return None
    if provider == "groq":
        return GroqTranscriptionAdapter(
            model=settings.get("SOFIA_TRANSCRIPTION_MODEL"),
            api_key=settings.get("GROQ_API_KEY"),
            default_language=settings.get("SOFIA_TRANSCRIPTION_LANGUAGE"),
        )
    return _UnconfiguredTranscriber(provider)
