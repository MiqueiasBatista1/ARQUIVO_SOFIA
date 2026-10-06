"""Injectable ingestion coordinator; actual media work belongs to adapters."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..adapters.interfaces import (
    AudioExtractor,
    Downloader,
    FrameExtractor,
    MetadataExtractor,
    OCRExtractor,
    SceneDetector,
    Transcriber,
    Translator,
)
from ..schemas.contracts import (
    IngestionOutput,
    Scene,
    TranscriptResult,
    TranscriptStatus,
    VideoInput,
    validate_local_file,
)


class AdapterConfigurationError(RuntimeError):
    """Raised when an input requires a capability that was not configured."""


@dataclass(frozen=True, slots=True)
class IngestionAdapters:
    downloader: Downloader | None = None
    metadata_extractor: MetadataExtractor | None = None
    audio_extractor: AudioExtractor | None = None
    frame_extractor: FrameExtractor | None = None
    scene_detector: SceneDetector | None = None
    ocr: OCRExtractor | None = None
    transcriber: Transcriber | None = None
    translator: Translator | None = None


class VideoIngestionPipeline:
    """Runs configured stages and returns a partial result when optional stages are absent."""

    def __init__(self, adapters: IngestionAdapters) -> None:
        self.adapters = adapters

    def run(self, source: VideoInput, target_language: str | None = None) -> IngestionOutput:
        warnings: list[str] = []
        if source.source_type == "local":
            media_path = validate_local_file(source)
        else:
            if self.adapters.downloader is None:
                raise AdapterConfigurationError("URL input requires a configured Downloader adapter")
            media_path = Path(self.adapters.downloader.download(source.source, source.filename)).resolve()
            if not media_path.is_file():
                raise FileNotFoundError("Downloader returned a path that does not exist")

        media_metadata = {}
        if self.adapters.metadata_extractor is None:
            warnings.append("metadata extractor adapter not configured")
        else:
            media_metadata = self.adapters.metadata_extractor.extract(media_path)

        audio_path: Path | None = None
        transcript = ()
        transcription_result: TranscriptResult | None = None
        translated = ()
        if self.adapters.audio_extractor is None:
            warnings.append("audio extraction adapter not configured")
        else:
            audio_path = Path(self.adapters.audio_extractor.extract(media_path)).resolve()
            if not audio_path.is_file():
                raise FileNotFoundError("AudioExtractor returned a path that does not exist")
            if self.adapters.transcriber is None:
                warnings.append("transcription adapter not configured")
            else:
                transcription_result = self.adapters.transcriber.transcribe(audio_path, source.language)
                if not isinstance(transcription_result, TranscriptResult):
                    raise TypeError("Transcriber must return a TranscriptResult")
                transcript = transcription_result.segments
                if transcription_result.status != TranscriptStatus.SUCCESS:
                    error = transcription_result.error
                    if error is not None:
                        warnings.append(
                            f"transcription {transcription_result.status.value.lower()} "
                            f"[{error.code.value}]: {error.message}"
                        )
                if target_language is not None:
                    if self.adapters.translator is None:
                        warnings.append("translation requested but Translator adapter not configured")
                    else:
                        translated = tuple(self.adapters.translator.translate(transcript, target_language))

        if self.adapters.scene_detector is None:
            warnings.append("scene detector adapter not configured")
            scenes: tuple[Scene, ...] = ()
        else:
            scenes = tuple(self.adapters.scene_detector.detect(media_path))

        frames = ()
        if self.adapters.frame_extractor is None:
            warnings.append("frame extractor adapter not configured")
        elif scenes:
            timestamps = tuple((scene.start_seconds + scene.end_seconds) / 2 for scene in scenes)
            frames = tuple(self.adapters.frame_extractor.extract(media_path, timestamps))

        if self.adapters.ocr is None:
            warnings.append("OCR adapter not configured")
            ocr_results = ()
        else:
            ocr_results = tuple(
                result
                for frame in frames
                for result in self.adapters.ocr.extract(frame)
            )

        return IngestionOutput(
            source=source,
            status="partial" if warnings else "complete",
            resolved_media_path=str(media_path),
            media_metadata=media_metadata,
            audio_path=str(audio_path) if audio_path else None,
            transcript=transcript,
            transcription_result=transcription_result,
            translated_transcript=translated,
            frames=frames,
            scenes=scenes,
            ocr=ocr_results,
            warnings=tuple(warnings),
        )
