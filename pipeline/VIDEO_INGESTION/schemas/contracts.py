"""Validated, provider-neutral contracts for video ingestion."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from math import isfinite
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


def _non_empty(value: Any, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")


def _time_range(start: float, end: float) -> None:
    if (
        isinstance(start, bool)
        or isinstance(end, bool)
        or not isinstance(start, (int, float))
        or not isinstance(end, (int, float))
        or not isfinite(start)
        or not isfinite(end)
    ):
        raise ValueError("timestamps must be numbers")
    if start < 0 or end <= start:
        raise ValueError("timestamps must satisfy 0 <= start_seconds < end_seconds")


@dataclass(frozen=True, slots=True)
class VideoInput:
    source_type: str
    source: str
    filename: str | None = None
    language: str | None = None
    duration: float | None = None
    platform: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.source_type, str) or self.source_type not in {"local", "url"}:
            raise ValueError("source_type must be 'local' or 'url'")
        _non_empty(self.source, "source")
        if self.source_type == "url":
            parsed = urlparse(self.source)
            if parsed.scheme not in {"http", "https"} or not parsed.hostname:
                raise ValueError("URL source must be an absolute http(s) URL")
        for name in ("filename", "language", "platform"):
            value = getattr(self, name)
            if value is not None:
                _non_empty(value, name)
        if self.duration is not None and (
            isinstance(self.duration, bool)
            or not isinstance(self.duration, (int, float))
            or not isfinite(self.duration)
            or self.duration <= 0
        ):
            raise ValueError("duration must be a positive number or null")
        if not isinstance(self.metadata, dict):
            raise ValueError("metadata must be an object")

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> VideoInput:
        allowed = {"source_type", "source", "filename", "language", "duration", "platform", "metadata"}
        if not isinstance(payload, dict):
            raise ValueError("video input must be an object")
        extras = set(payload) - allowed
        if extras:
            raise ValueError(f"unknown video input fields: {', '.join(sorted(extras))}")
        if "source_type" not in payload or "source" not in payload:
            raise ValueError("source_type and source are required")
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class TranscriptSegment:
    start_seconds: float | None
    end_seconds: float | None
    text: str
    language: str | None = None
    confidence: float | None = None
    speaker: str | None = None

    def __post_init__(self) -> None:
        if self.start_seconds is None and self.end_seconds is None:
            pass
        elif self.start_seconds is None or self.end_seconds is None:
            raise ValueError("transcript timestamps must both be present or both be null")
        else:
            _time_range(self.start_seconds, self.end_seconds)
        _non_empty(self.text, "text")
        for name in ("language", "speaker"):
            value = getattr(self, name)
            if value is not None:
                _non_empty(value, name)
        if self.confidence is not None and (
            isinstance(self.confidence, bool)
            or not isinstance(self.confidence, (int, float))
            or not isfinite(self.confidence)
            or not 0 <= self.confidence <= 1
        ):
            raise ValueError("confidence must be a number between 0 and 1")


class TranscriptStatus(str, Enum):
    SUCCESS = "SUCCESS"
    PARTIAL = "PARTIAL"
    ERROR = "ERROR"


class TranscriptionErrorCode(str, Enum):
    AUDIO_NOT_FOUND = "AUDIO_NOT_FOUND"
    AUDIO_INVALID = "AUDIO_INVALID"
    UNSUPPORTED_LANGUAGE = "UNSUPPORTED_LANGUAGE"
    PROVIDER_NOT_CONFIGURED = "PROVIDER_NOT_CONFIGURED"
    PROVIDER_AUTH_ERROR = "PROVIDER_AUTH_ERROR"
    PROVIDER_RATE_LIMIT = "PROVIDER_RATE_LIMIT"
    PROVIDER_UNAVAILABLE = "PROVIDER_UNAVAILABLE"
    TRANSCRIPTION_FAILED = "TRANSCRIPTION_FAILED"


@dataclass(frozen=True, slots=True)
class TranscriptError:
    code: TranscriptionErrorCode
    message: str
    cause_type: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.code, TranscriptionErrorCode):
            raise ValueError("code must be a TranscriptionErrorCode")
        _non_empty(self.message, "message")
        if self.cause_type is not None:
            _non_empty(self.cause_type, "cause_type")


@dataclass(frozen=True, slots=True)
class TranscriptResult:
    status: TranscriptStatus
    segments: tuple[TranscriptSegment, ...] = ()
    language: str | None = None
    provider: str | None = None
    model: str | None = None
    source_audio: str | None = None
    error: TranscriptError | None = None
    text: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.status, TranscriptStatus):
            raise ValueError("status must be a TranscriptStatus")
        if self.status == TranscriptStatus.ERROR and self.error is None:
            raise ValueError("ERROR transcription results require error details")
        if self.status == TranscriptStatus.SUCCESS and self.error is not None:
            raise ValueError("SUCCESS transcription results cannot contain an error")
        if self.status == TranscriptStatus.PARTIAL and self.error is None:
            raise ValueError("PARTIAL transcription results require a reason")
        if not isinstance(self.text, str):
            raise ValueError("text must be a string")
        if any(not isinstance(segment, TranscriptSegment) for segment in self.segments):
            raise ValueError("segments must contain TranscriptSegment values")
        if self.segments:
            object.__setattr__(self, "text", " ".join(segment.text.strip() for segment in self.segments))
        if self.language is not None:
            _non_empty(self.language, "language")
        for name in ("provider", "model", "source_audio"):
            value = getattr(self, name)
            if value is not None:
                _non_empty(value, name)

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.value,
            "text": self.text,
            "language": self.language,
            "segments": [
                {
                    "start": segment.start_seconds,
                    "end": segment.end_seconds,
                    "text": segment.text,
                    "language": segment.language,
                    "confidence": segment.confidence,
                    "speaker": segment.speaker,
                }
                for segment in self.segments
            ],
            "provider": self.provider,
            "model": self.model,
            "source_audio": self.source_audio,
            "error": asdict(self.error) if self.error else None,
        }

    def to_metadata_dict(self) -> dict[str, Any]:
        """Metadata for the evidence bridge; segment text is emitted separately."""
        payload = self.to_dict()
        payload.pop("segments")
        return payload


@dataclass(frozen=True, slots=True)
class ExtractedFrame:
    timestamp_seconds: float
    path: str

    def __post_init__(self) -> None:
        if (
            isinstance(self.timestamp_seconds, bool)
            or not isinstance(self.timestamp_seconds, (int, float))
            or not isfinite(self.timestamp_seconds)
            or self.timestamp_seconds < 0
        ):
            raise ValueError("timestamp_seconds must be zero or greater")
        _non_empty(self.path, "path")


@dataclass(frozen=True, slots=True)
class OCRResult:
    timestamp_seconds: float
    text: str
    confidence: float | None = None

    def __post_init__(self) -> None:
        if (
            isinstance(self.timestamp_seconds, bool)
            or not isinstance(self.timestamp_seconds, (int, float))
            or not isfinite(self.timestamp_seconds)
            or self.timestamp_seconds < 0
        ):
            raise ValueError("timestamp_seconds must be zero or greater")
        _non_empty(self.text, "text")
        if self.confidence is not None and (
            isinstance(self.confidence, bool)
            or not isinstance(self.confidence, (int, float))
            or not isfinite(self.confidence)
            or not 0 <= self.confidence <= 1
        ):
            raise ValueError("confidence must be a number between 0 and 1")


@dataclass(frozen=True, slots=True)
class Scene:
    start_seconds: float
    end_seconds: float
    visual_description: str | None = None
    main_action: str | None = None
    person_character: str | None = None
    product: str | None = None
    environment: str | None = None
    framing: str | None = None
    camera_movement: str | None = None
    on_screen_text: tuple[str, ...] = ()
    speech: str | None = None
    audio_music: str | None = None
    cta: str | None = None
    perceived_emotion: str | None = None
    observations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _time_range(self.start_seconds, self.end_seconds)
        for name in (
            "visual_description", "main_action", "person_character", "product", "environment",
            "framing", "camera_movement", "speech", "audio_music", "cta", "perceived_emotion",
        ):
            value = getattr(self, name)
            if value is not None:
                _non_empty(value, name)
        for name in ("on_screen_text", "observations"):
            value = getattr(self, name)
            if not isinstance(value, (tuple, list)) or any(not isinstance(item, str) for item in value):
                raise ValueError(f"{name} must be a list of strings")

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> Scene:
        if not isinstance(payload, dict):
            raise ValueError("scene must be an object")
        allowed = set(cls.__dataclass_fields__)
        extras = set(payload) - allowed
        if extras:
            raise ValueError(f"unknown scene fields: {', '.join(sorted(extras))}")
        if "start_seconds" not in payload or "end_seconds" not in payload:
            raise ValueError("scene requires start_seconds and end_seconds")
        for key in ("on_screen_text", "observations"):
            if key in payload:
                if not isinstance(payload[key], (list, tuple)):
                    raise ValueError(f"{key} must be a list of strings")
                payload = {**payload, key: tuple(payload[key])}
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class IngestionOutput:
    source: VideoInput
    status: str
    resolved_media_path: str | None = None
    media_metadata: dict[str, Any] = field(default_factory=dict)
    audio_path: str | None = None
    transcript: tuple[TranscriptSegment, ...] = ()
    transcription_result: TranscriptResult | None = None
    translated_transcript: tuple[TranscriptSegment, ...] = ()
    frames: tuple[ExtractedFrame, ...] = ()
    scenes: tuple[Scene, ...] = ()
    ocr: tuple[OCRResult, ...] = ()
    warnings: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in {"complete", "partial"}:
            raise ValueError("status must be 'complete' or 'partial'")

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source.to_dict(),
            "status": self.status,
            "resolved_media_path": self.resolved_media_path,
            "media_metadata": self.media_metadata,
            "audio_path": self.audio_path,
            "transcript": [asdict(item) for item in self.transcript],
            "transcription_result": self.transcription_result.to_dict() if self.transcription_result else None,
            "translated_transcript": [asdict(item) for item in self.translated_transcript],
            "frames": [asdict(item) for item in self.frames],
            "scenes": [item.to_dict() for item in self.scenes],
            "ocr": [asdict(item) for item in self.ocr],
            "warnings": list(self.warnings),
        }


def validate_local_file(source: VideoInput) -> Path:
    """Resolve a local input and require an existing file; never downloads URLs."""
    if source.source_type != "local":
        raise ValueError("validate_local_file accepts only local inputs")
    path = Path(source.source).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"local video file not found: {path}")
    return path.resolve()
