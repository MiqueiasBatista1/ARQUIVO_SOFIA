"""Local-only ingestion command: python -m pipeline.VIDEO_INGESTION.cli."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Sequence

from .adapters.ffmpeg import FFmpegAudioExtractor, FFmpegFrameExtractor, FFprobeMetadataExtractor
from .adapters.pyscenedetect import PySceneDetectAdapter
from .adapters.reference_analysis_bridge import to_reference_analysis_payload
from .adapters.groq_transcription import transcriber_from_environment
from .extractors.orchestrator import IngestionAdapters, VideoIngestionPipeline
from .schemas.contracts import VideoInput


def _safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._") or "video"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ingest a local video for reference analysis.")
    parser.add_argument("--input", required=True, type=Path, help="Path to a local video")
    parser.add_argument("--output", required=True, type=Path, help="Directory for generated artifacts")
    parser.add_argument("--language", help="Known source language code, if available")
    parser.add_argument("--platform", help="Reference platform label, if known")
    parser.add_argument("--ffmpeg", default="ffmpeg", help="FFmpeg executable name or path")
    parser.add_argument("--ffprobe", default="ffprobe", help="ffprobe executable name or path")
    parser.add_argument("--scene-threshold", type=float, default=27.0)
    args = parser.parse_args(argv)

    source_path = args.input.expanduser().resolve()
    source = VideoInput(
        source_type="local", source=str(source_path), filename=source_path.name,
        language=args.language, platform=args.platform,
    )
    artifact_dir = args.output.expanduser().resolve() / _safe_name(source_path.stem)
    adapters = IngestionAdapters(
        metadata_extractor=FFprobeMetadataExtractor(args.ffprobe),
        audio_extractor=FFmpegAudioExtractor(artifact_dir / "audio", args.ffmpeg),
        scene_detector=PySceneDetectAdapter(args.scene_threshold),
        frame_extractor=FFmpegFrameExtractor(artifact_dir / "frames", args.ffmpeg),
        transcriber=transcriber_from_environment(),
    )
    result = VideoIngestionPipeline(adapters).run(source)
    artifact_dir.mkdir(parents=True, exist_ok=True)
    ingestion_payload = result.to_dict()
    analysis_payload = to_reference_analysis_payload(result)
    (artifact_dir / "ingestion.json").write_text(
        json.dumps(ingestion_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (artifact_dir / "reference_analysis_seed.json").write_text(
        json.dumps(analysis_payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Status: {result.status}")
    print(f"Artifacts: {artifact_dir}")
    for warning in result.warnings:
        print(f"Warning: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
