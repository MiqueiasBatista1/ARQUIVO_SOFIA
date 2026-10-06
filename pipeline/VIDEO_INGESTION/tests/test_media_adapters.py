import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline.VIDEO_INGESTION.adapters.ffmpeg import (
    ExternalToolMissing,
    FFmpegAudioExtractor,
    FFmpegFrameExtractor,
    FFprobeMetadataExtractor,
)
from pipeline.VIDEO_INGESTION.adapters.pyscenedetect import PySceneDetectAdapter


class FFprobeTests(unittest.TestCase):
    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.shutil.which", return_value="/tools/ffprobe")
    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.subprocess.run")
    def test_metadata_extractor_normalizes_media_streams(self, run, _which):
        run.return_value = subprocess.CompletedProcess(
            args=[], returncode=0,
            stdout=json.dumps({
                "format": {"format_name": "mov,mp4", "duration": "12.5", "size": "999"},
                "streams": [
                    {"codec_type": "video", "codec_name": "h264", "width": 720, "height": 1280},
                    {"codec_type": "audio", "codec_name": "aac", "sample_rate": "44100", "channels": 2},
                ],
            }), stderr="",
        )
        data = FFprobeMetadataExtractor().extract(Path("clip.mp4"))
        self.assertEqual(data["duration_seconds"], 12.5)
        self.assertEqual(data["video"]["width"], 720)
        self.assertEqual(data["audio"]["sample_rate"], 44100)

    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.shutil.which", return_value=None)
    def test_missing_ffprobe_is_explained_without_installing(self, _which):
        with self.assertRaisesRegex(ExternalToolMissing, "ffprobe.*not found"):
            FFprobeMetadataExtractor().extract(Path("clip.mp4"))


class FFmpegExtractionTests(unittest.TestCase):
    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.shutil.which", return_value="/tools/ffmpeg")
    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.subprocess.run")
    def test_audio_extractor_runs_ffmpeg_and_returns_created_wav(self, run, _which):
        def create_output(args, **kwargs):
            Path(args[-1]).write_bytes(b"wav")
            return subprocess.CompletedProcess(args=args, returncode=0, stdout="", stderr="")

        run.side_effect = create_output
        with tempfile.TemporaryDirectory() as directory:
            clip = Path(directory) / "sample.mp4"
            clip.write_bytes(b"video")
            audio = FFmpegAudioExtractor(Path(directory) / "audio").extract(clip)
            self.assertTrue(audio.is_file())
            self.assertIn("16000", run.call_args.args[0])

    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.shutil.which", return_value="/tools/ffmpeg")
    @patch("pipeline.VIDEO_INGESTION.adapters.ffmpeg.subprocess.run")
    def test_frame_extractor_uses_requested_timestamps(self, run, _which):
        def create_output(args, **kwargs):
            Path(args[-1]).write_bytes(b"jpeg")
            return subprocess.CompletedProcess(args=args, returncode=0, stdout="", stderr="")

        run.side_effect = create_output
        with tempfile.TemporaryDirectory() as directory:
            clip = Path(directory) / "sample.mp4"
            clip.write_bytes(b"video")
            frames = FFmpegFrameExtractor(Path(directory) / "frames").extract(clip, [1.25, 3.5])
        self.assertEqual([item.timestamp_seconds for item in frames], [1.25, 3.5])
        self.assertEqual(run.call_count, 2)


class SceneDetectionTests(unittest.TestCase):
    def test_missing_pyscenedetect_is_explained(self):
        with patch.dict("sys.modules", {"scenedetect": None}):
            with self.assertRaisesRegex(ExternalToolMissing, "PySceneDetect is not installed"):
                PySceneDetectAdapter().detect(Path("clip.mp4"))


if __name__ == "__main__":
    unittest.main()
