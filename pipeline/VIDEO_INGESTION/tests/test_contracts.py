import json
import tempfile
import unittest
from pathlib import Path

from pipeline.VIDEO_INGESTION.adapters.reference_analysis_bridge import to_reference_analysis_payload
from pipeline.VIDEO_INGESTION.extractors.orchestrator import (
    AdapterConfigurationError,
    IngestionAdapters,
    VideoIngestionPipeline,
)
from pipeline.VIDEO_INGESTION.schemas.contracts import (
    ExtractedFrame,
    IngestionOutput,
    OCRResult,
    Scene,
    TranscriptResult,
    TranscriptSegment,
    TranscriptStatus,
    VideoInput,
)


class VideoInputTests(unittest.TestCase):
    def test_valid_local_input(self):
        item = VideoInput.from_dict({"source_type": "local", "source": "clip.mp4"})
        self.assertEqual(item.source_type, "local")
        self.assertIsNone(item.duration)

    def test_valid_url_input(self):
        item = VideoInput.from_dict({"source_type": "url", "source": "https://example.test/video"})
        self.assertEqual(item.source_type, "url")

    def test_invalid_url_is_rejected(self):
        with self.assertRaises(ValueError):
            VideoInput(source_type="url", source="file:///clip.mp4")

    def test_missing_required_input_is_rejected(self):
        with self.assertRaises(ValueError):
            VideoInput.from_dict({"source_type": "local"})

    def test_invalid_duration_is_rejected(self):
        with self.assertRaises(ValueError):
            VideoInput(source_type="local", source="clip.mp4", duration=0)

    def test_input_schema_json_is_parseable(self):
        schema_path = Path(__file__).parents[1] / "schemas" / "video_input.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertIn("source_type", schema["required"])


class SceneSchemaTests(unittest.TestCase):
    def test_scene_round_trip_contains_requested_fields(self):
        scene = Scene.from_dict({
            "start_seconds": 1.0,
            "end_seconds": 3.5,
            "visual_description": "A surface and several objects are visible.",
            "main_action": "Objects are arranged.",
            "person_character": "presenter",
            "product": "not specified",
            "environment": "indoor",
            "framing": "medium",
            "camera_movement": "static",
            "on_screen_text": ["Step one"],
            "speech": "Example speech.",
            "audio_music": "background audio",
            "cta": None,
            "perceived_emotion": "uncertain",
            "observations": ["Needs review"],
        })
        self.assertEqual(scene.to_dict()["start_seconds"], 1.0)
        self.assertEqual(scene.to_dict()["on_screen_text"], ("Step one",))

    def test_scene_rejects_invalid_timestamp_order(self):
        with self.assertRaises(ValueError):
            Scene.from_dict({"start_seconds": 4, "end_seconds": 2})


class PipelineInputTests(unittest.TestCase):
    def test_local_file_is_resolved_and_pipeline_is_partial_without_adapters(self):
        with tempfile.TemporaryDirectory() as directory:
            clip = Path(directory) / "clip.mp4"
            clip.write_bytes(b"placeholder")
            result = VideoIngestionPipeline(IngestionAdapters()).run(
                VideoInput(source_type="local", source=str(clip))
            )
        self.assertEqual(result.status, "partial")
        self.assertTrue(result.resolved_media_path)
        self.assertTrue(result.warnings)

    def test_configured_pipeline_runs_injected_stages(self):
        class FakeAudio:
            def __init__(self, path):
                self.path = path

            def extract(self, video_path):
                return self.path

        class FakeMetadata:
            def extract(self, video_path):
                return {"duration_seconds": 2.0, "video": {"width": 640, "height": 360}}

        class FakeTranscriber:
            def transcribe(self, audio_path, language=None):
                segment = TranscriptSegment(0, 1, "Source words.", language)
                return TranscriptResult(
                    TranscriptStatus.SUCCESS, (segment,), language, "fake", "fake-model", str(audio_path)
                )

        class FakeTranslator:
            def translate(self, segments, target_language):
                return [TranscriptSegment(0, 1, "Palavras traduzidas.", target_language)]

        class FakeScenes:
            def detect(self, video_path):
                return [Scene(0, 2, main_action="A generic action.")]

        class FakeFrames:
            def __init__(self, path):
                self.path = path

            def extract(self, video_path, timestamps):
                return [ExtractedFrame(timestamps[0], str(self.path))]

        class FakeOCR:
            def extract(self, frame):
                return [OCRResult(frame.timestamp_seconds, "On-screen text.")]

        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            clip = base / "clip.mp4"
            audio = base / "audio.wav"
            frame = base / "frame.jpg"
            for path in (clip, audio, frame):
                path.write_bytes(b"placeholder")
            adapters = IngestionAdapters(
                metadata_extractor=FakeMetadata(),
                audio_extractor=FakeAudio(audio),
                transcriber=FakeTranscriber(),
                translator=FakeTranslator(),
                scene_detector=FakeScenes(),
                frame_extractor=FakeFrames(frame),
                ocr=FakeOCR(),
            )
            result = VideoIngestionPipeline(adapters).run(
                VideoInput(source_type="local", source=str(clip), language="en"),
                target_language="pt",
            )
        self.assertEqual(result.status, "complete")
        self.assertEqual(result.transcript[0].text, "Source words.")
        self.assertEqual(result.transcription_result.status, TranscriptStatus.SUCCESS)
        serialized_result = result.to_dict()["transcription_result"]
        self.assertEqual(serialized_result["segments"][0]["start"], 0)
        self.assertIsNone(serialized_result["segments"][0]["speaker"])
        seed = to_reference_analysis_payload(result)
        dialogue = next(item for item in seed["observations"] if item["field"] == "OBSERVED_DIALOGUE")
        self.assertEqual(dialogue["classification"], "OBSERVADO")
        self.assertEqual(dialogue["content"], "Source words.")
        self.assertEqual(dialogue["evidence_source"], "transcription_adapter")
        self.assertEqual(seed["source_context"]["transcription"]["status"], "SUCCESS")
        self.assertNotIn("segments", seed["source_context"]["transcription"])
        self.assertEqual(seed["interpretations"], [])
        self.assertEqual(result.translated_transcript[0].language, "pt")
        self.assertEqual(result.ocr[0].text, "On-screen text.")
        self.assertEqual(result.media_metadata["duration_seconds"], 2.0)

    def test_url_requires_explicit_downloader(self):
        with self.assertRaises(AdapterConfigurationError):
            VideoIngestionPipeline(IngestionAdapters()).run(
                VideoInput(source_type="url", source="https://example.test/video")
            )

    def test_url_can_use_an_injected_downloader_without_network(self):
        class FakeDownloader:
            def __init__(self, path):
                self.path = path

            def download(self, url, filename=None):
                self.asserted_url = url
                return self.path

        with tempfile.TemporaryDirectory() as directory:
            clip = Path(directory) / "downloaded.mp4"
            clip.write_bytes(b"placeholder")
            downloader = FakeDownloader(clip)
            result = VideoIngestionPipeline(
                IngestionAdapters(downloader=downloader)
            ).run(VideoInput(source_type="url", source="https://example.test/clip"))
        self.assertEqual(downloader.asserted_url, "https://example.test/clip")
        self.assertEqual(result.status, "partial")

    def test_scene_schema_json_is_parseable(self):
        schema_path = Path(__file__).parents[1] / "schemas" / "scene.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertIn("start_seconds", schema["required"])

    def test_output_schema_json_is_parseable(self):
        schema_path = Path(__file__).parents[1] / "schemas" / "ingestion_output.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertIn("scenes", schema["required"])
        self.assertIn("transcription_result", schema["properties"])

    def test_ingestion_seed_marks_items_for_review(self):
        scene = Scene(0, 2, main_action="A generic action occurs.")
        output = IngestionOutput(
            source=VideoInput(source_type="local", source="clip.mp4"),
            status="partial",
            scenes=(scene,),
        )
        payload = to_reference_analysis_payload(output, "ref-1")
        self.assertEqual(payload["reference_id"], "ref-1")
        self.assertEqual(payload["observations"][0]["review_status"], "PENDING_HUMAN_REVIEW")


if __name__ == "__main__":
    unittest.main()
