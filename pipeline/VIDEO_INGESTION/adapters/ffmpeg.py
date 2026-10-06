"""FFmpeg/ffprobe adapters. Executables are checked only when an adapter runs."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any, Sequence

from ..schemas.contracts import ExtractedFrame


class ExternalToolMissing(RuntimeError):
    """An optional external media executable is unavailable."""


def _require_executable(configured: str, tool_label: str) -> str:
    executable = shutil.which(configured)
    if executable is None:
        raise ExternalToolMissing(
            f"{tool_label} executable '{configured}' was not found on PATH; "
            "install the documented system dependency and retry"
        )
    return executable


def _run(args: list[str]) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise RuntimeError(f"media command failed: {detail}") from exc
    return result


class FFprobeMetadataExtractor:
    """Extract normalized container and stream metadata as JSON-compatible data."""

    def __init__(self, executable: str = "ffprobe") -> None:
        self.executable = executable

    def extract(self, video_path: Path) -> dict[str, Any]:
        executable = _require_executable(self.executable, "ffprobe")
        result = _run([
            executable, "-v", "error", "-show_format", "-show_streams",
            "-of", "json", str(video_path),
        ])
        payload = json.loads(result.stdout)
        streams = payload.get("streams", [])
        video = next((item for item in streams if item.get("codec_type") == "video"), {})
        audio = next((item for item in streams if item.get("codec_type") == "audio"), {})
        format_data = payload.get("format", {})
        duration_value = format_data.get("duration") or video.get("duration")
        try:
            duration = float(duration_value) if duration_value is not None else None
        except (TypeError, ValueError):
            duration = None
        return {
            "container": format_data.get("format_name"),
            "duration_seconds": duration,
            "size_bytes": _as_int(format_data.get("size")),
            "bit_rate": _as_int(format_data.get("bit_rate")),
            "video": {
                "codec": video.get("codec_name"),
                "width": video.get("width"),
                "height": video.get("height"),
                "frame_rate": video.get("avg_frame_rate") or video.get("r_frame_rate"),
                "pixel_format": video.get("pix_fmt"),
            } if video else None,
            "audio": {
                "codec": audio.get("codec_name"),
                "sample_rate": _as_int(audio.get("sample_rate")),
                "channels": audio.get("channels"),
            } if audio else None,
        }


def _as_int(value: Any) -> int | None:
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


class FFmpegAudioExtractor:
    """Extract mono 16 kHz PCM WAV suitable for local transcription adapters."""

    def __init__(self, output_dir: Path, executable: str = "ffmpeg") -> None:
        self.output_dir = Path(output_dir)
        self.executable = executable

    def extract(self, video_path: Path) -> Path:
        executable = _require_executable(self.executable, "FFmpeg")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        output_path = self.output_dir / f"{video_path.stem}.wav"
        _run([
            executable, "-y", "-i", str(video_path), "-vn", "-ac", "1",
            "-ar", "16000", "-c:a", "pcm_s16le", str(output_path),
        ])
        if not output_path.is_file():
            raise RuntimeError(f"FFmpeg completed without creating audio output: {output_path}")
        return output_path


class FFmpegFrameExtractor:
    """Extract one JPEG at each requested timestamp, with stable output names."""

    def __init__(self, output_dir: Path, executable: str = "ffmpeg") -> None:
        self.output_dir = Path(output_dir)
        self.executable = executable

    def extract(self, video_path: Path, timestamps: Sequence[float]) -> Sequence[ExtractedFrame]:
        executable = _require_executable(self.executable, "FFmpeg")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        frames: list[ExtractedFrame] = []
        for index, timestamp in enumerate(timestamps, start=1):
            if timestamp < 0:
                raise ValueError("frame timestamps cannot be negative")
            output_path = self.output_dir / f"frame_{index:04d}_{timestamp:.3f}s.jpg"
            _run([
                executable, "-y", "-ss", f"{timestamp:.3f}", "-i", str(video_path),
                "-frames:v", "1", "-q:v", "2", str(output_path),
            ])
            if not output_path.is_file():
                raise RuntimeError(f"FFmpeg completed without creating frame: {output_path}")
            frames.append(ExtractedFrame(float(timestamp), str(output_path.resolve())))
        return frames
