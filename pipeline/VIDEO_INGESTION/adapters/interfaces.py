"""Provider-neutral protocols. No provider implementations are bundled."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol, Sequence

from ..schemas.contracts import ExtractedFrame, OCRResult, Scene, TranscriptResult, TranscriptSegment


class Downloader(Protocol):
    def download(self, url: str, filename: str | None = None) -> Path: ...


class MetadataExtractor(Protocol):
    def extract(self, video_path: Path) -> dict[str, Any]: ...


class AudioExtractor(Protocol):
    def extract(self, video_path: Path) -> Path: ...


class FrameExtractor(Protocol):
    def extract(self, video_path: Path, timestamps: Sequence[float]) -> Sequence[ExtractedFrame]: ...


class SceneDetector(Protocol):
    def detect(self, video_path: Path) -> Sequence[Scene]: ...


class OCRExtractor(Protocol):
    def extract(self, frame: ExtractedFrame) -> Sequence[OCRResult]: ...


class Transcriber(Protocol):
    def transcribe(self, audio_path: Path, language: str | None = None) -> TranscriptResult: ...


class Translator(Protocol):
    def translate(
        self, segments: Sequence[TranscriptSegment], target_language: str
    ) -> Sequence[TranscriptSegment]: ...
