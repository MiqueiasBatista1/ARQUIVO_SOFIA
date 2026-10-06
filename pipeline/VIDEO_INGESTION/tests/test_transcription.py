import json
import os
import tempfile
import unittest
import wave
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from pipeline.VIDEO_INGESTION.adapters.groq_transcription import (
    GroqTranscriptionAdapter,
    transcriber_from_environment,
)
from pipeline.VIDEO_INGESTION.schemas.contracts import (
    TranscriptStatus,
    TranscriptionErrorCode,
)


def write_wav(path: Path, frames: bytes = b"\x00\x00" * 800) -> Path:
    with wave.open(str(path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(16000)
        wav_file.writeframes(frames)
    return path


class FakeRawResponse:
    def __init__(self, payload):
        self.http_response = SimpleNamespace(json=lambda: payload)


class FakeTranscriptions:
    def __init__(self, response=None, error=None):
        self.with_raw_response = self
        self.response = response
        self.error = error
        self.request = None

    def create(self, **kwargs):
        self.request = kwargs
        if self.error:
            raise self.error
        return FakeRawResponse(self.response)


class FakeClient:
    def __init__(self, api_key, transcriptions):
        self.api_key = api_key
        self.audio = SimpleNamespace(transcriptions=transcriptions)


class TranscriptionAdapterTests(unittest.TestCase):
    def make_adapter(self, transcriptions, **kwargs):
        def factory(api_key):
            return FakeClient(api_key, transcriptions)

        return GroqTranscriptionAdapter(
            model="whisper-large-v3",
            api_key="test-key-not-real",
            client_factory=factory,
            **kwargs,
        )

    def test_missing_audio_returns_typed_error(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.make_adapter(FakeTranscriptions()).transcribe(Path(directory) / "missing.wav")
        self.assertEqual(result.status, TranscriptStatus.ERROR)
        self.assertEqual(result.error.code, TranscriptionErrorCode.AUDIO_NOT_FOUND)

    def test_invalid_audio_returns_typed_error(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.wav"
            path.write_bytes(b"not a wave")
            result = self.make_adapter(FakeTranscriptions()).transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.ERROR)
        self.assertEqual(result.error.code, TranscriptionErrorCode.AUDIO_INVALID)

    def test_empty_wav_returns_typed_error(self):
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "empty.wav", frames=b"")
            result = self.make_adapter(FakeTranscriptions()).transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.ERROR)
        self.assertEqual(result.error.code, TranscriptionErrorCode.AUDIO_INVALID)

    def test_provider_not_configured_does_not_choose_a_model(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True):
            path = write_wav(Path(directory) / "audio.wav")
            adapter = GroqTranscriptionAdapter(model=None, api_key=None)
            result = adapter.transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.ERROR)
        self.assertEqual(result.error.code, TranscriptionErrorCode.PROVIDER_NOT_CONFIGURED)
        self.assertIsNone(result.model)

    def test_missing_provider_key_returns_provider_not_configured(self):
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True):
            path = write_wav(Path(directory) / "audio.wav")
            adapter = GroqTranscriptionAdapter(model="explicit-model", api_key=None)
            result = adapter.transcribe(path)
        self.assertEqual(result.error.code, TranscriptionErrorCode.PROVIDER_NOT_CONFIGURED)

    def test_environment_selects_only_configured_provider_and_model(self):
        self.assertIsNone(transcriber_from_environment({}))
        adapter = transcriber_from_environment({
            "SOFIA_TRANSCRIPTION_PROVIDER": "groq",
            "SOFIA_TRANSCRIPTION_MODEL": "explicit-model",
            "SOFIA_TRANSCRIPTION_LANGUAGE": "pt",
            "GROQ_API_KEY": "test-key-not-real",
        })
        self.assertEqual(adapter.model, "explicit-model")
        self.assertEqual(adapter.default_language, "pt")

    def test_success_preserves_provider_timestamps_and_optional_fields(self):
        transcriptions = FakeTranscriptions({
            "text": "recognized words",
            "language": "pt",
            "segments": [
                {"start": 1.25, "end": 2.5, "text": " recognized words "},
                {"start": 2.6, "end": 3.0, "text": "more words"},
            ],
        })
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.SUCCESS)
        self.assertEqual(result.language, "pt")
        self.assertEqual(result.model, "whisper-large-v3")
        self.assertEqual(result.segments[0].text, " recognized words ")
        self.assertEqual(result.text, "recognized words more words")
        self.assertEqual(result.to_dict()["text"], "recognized words more words")
        self.assertEqual(result.segments[0].start_seconds, 1.25)
        self.assertEqual(result.segments[0].end_seconds, 2.5)
        self.assertIsNone(result.segments[0].confidence)
        self.assertIsNone(result.segments[0].speaker)
        self.assertEqual(transcriptions.request["response_format"], "verbose_json")
        self.assertEqual(transcriptions.request["timestamp_granularities"], ["segment"])

    def test_requested_language_is_forwarded_without_rewriting_it(self):
        transcriptions = FakeTranscriptions({"text": "", "segments": []})
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path, language="pt")
        self.assertEqual(transcriptions.request["language"], "pt")
        self.assertIsNone(result.language)
        self.assertEqual(result.segments, ())
        self.assertEqual(result.text, "")

    def test_optional_provider_fields_are_preserved_only_when_returned(self):
        transcriptions = FakeTranscriptions({
            "language": "pt",
            "segments": [{
                "start": 0.2, "end": 0.9, "text": " fala ",
                "confidence": 0.87, "speaker": "speaker_1",
            }],
        })
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path)
        self.assertEqual(result.segments[0].confidence, 0.87)
        self.assertEqual(result.segments[0].speaker, "speaker_1")

    def test_partial_result_preserves_text_without_fabricating_timestamps(self):
        transcriptions = FakeTranscriptions({"text": "recognized words", "language": "pt"})
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.PARTIAL)
        self.assertEqual(result.segments[0].text, "recognized words")
        self.assertEqual(result.text, "recognized words")
        self.assertEqual(result.text, "recognized words")
        self.assertIsNone(result.segments[0].start_seconds)
        self.assertIsNone(result.segments[0].end_seconds)
        self.assertIsNotNone(result.error)

    def test_provider_error_keeps_cause_and_redacts_secret(self):
        class RateLimitError(Exception):
            pass

        error = RateLimitError("quota denied test-key-not-real")
        transcriptions = FakeTranscriptions(error=error)
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.ERROR)
        self.assertEqual(result.error.code, TranscriptionErrorCode.PROVIDER_RATE_LIMIT)
        self.assertEqual(result.error.cause_type, "RateLimitError")
        self.assertIn("quota denied", result.error.message)
        self.assertNotIn("test-key-not-real", json.dumps(result.to_dict()))

    def test_unsupported_language_response_has_its_own_typed_code(self):
        class BadRequestError(Exception):
            status_code = 400

        transcriptions = FakeTranscriptions(error=BadRequestError("unsupported language xx"))
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path, language="xx")
        self.assertEqual(result.error.code, TranscriptionErrorCode.UNSUPPORTED_LANGUAGE)

    def test_provider_authentication_and_availability_errors_are_typed(self):
        class AuthenticationError(Exception):
            pass

        class APIStatusError(Exception):
            status_code = 503

        for exception, expected in (
            (AuthenticationError("unauthorized"), TranscriptionErrorCode.PROVIDER_AUTH_ERROR),
            (APIStatusError("temporarily unavailable"), TranscriptionErrorCode.PROVIDER_UNAVAILABLE),
        ):
            with self.subTest(code=expected), tempfile.TemporaryDirectory() as directory:
                path = write_wav(Path(directory) / "audio.wav")
                result = self.make_adapter(FakeTranscriptions(error=exception)).transcribe(path)
            self.assertEqual(result.error.code, expected)

    def test_unclassified_provider_error_is_transcription_failed_and_preserves_message(self):
        error = RuntimeError("model request failed for configured model")
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(FakeTranscriptions(error=error)).transcribe(path)
        self.assertEqual(result.status, TranscriptStatus.ERROR)
        self.assertEqual(result.error.code, TranscriptionErrorCode.TRANSCRIPTION_FAILED)
        self.assertEqual(result.error.message, str(error))
        self.assertEqual(result.error.cause_type, "RuntimeError")

    def test_result_json_has_null_optional_metadata_when_provider_omits_it(self):
        transcriptions = FakeTranscriptions({
            "text": "",
            "segments": [{"start": 0.0, "end": 0.4, "text": " ok "}],
        })
        with tempfile.TemporaryDirectory() as directory:
            path = write_wav(Path(directory) / "audio.wav")
            result = self.make_adapter(transcriptions).transcribe(path)
        payload = result.to_dict()
        self.assertIsNone(payload["segments"][0]["speaker"])
        self.assertIsNone(payload["segments"][0]["confidence"])
        self.assertEqual(payload["segments"][0]["start"], 0.0)
        self.assertEqual(payload["segments"][0]["end"], 0.4)


if __name__ == "__main__":
    unittest.main()
