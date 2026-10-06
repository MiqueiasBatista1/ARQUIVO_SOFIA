import json
import unittest
from pathlib import Path

from pipeline.REFERENCE_TO_UGC.adapters.video_ingestion import ingestion_to_analysis_seed
from pipeline.REFERENCE_TO_UGC.schemas.contracts import (
    ReferenceAnalysisPayload,
    transform_reference_to_ugc,
    validate_ugc_output,
)
from pipeline.VIDEO_INGESTION.schemas.contracts import IngestionOutput, Scene, VideoInput


def analysis_payload():
    return {
        "reference_id": "reference-42",
        "source_context": {"source_type": "local"},
        "observations": [{"field": "OBSERVED_ACTION", "content": "A sequence is visible."}],
        "interpretations": [],
        "derived_translations": [],
        "reusable_patterns": [{"content": "Show context before steps."}],
        "mechanisms": [{"content": "Progressive explanation may support comprehension."}],
        "non_copyable_elements": [{"content": "Replace original language and assets."}],
        "remodeling_opportunities": [{"content": "Use a different scenario and actions."}],
        "hypotheses_to_test": [],
    }


def concept_draft():
    return {
        "content_type": "short-form UGC",
        "ugc_template": "demonstration",
        "hook": "Introduce a generic question about the process.",
        "problem": "A neutral context for explaining a process.",
        "mechanism": "Context followed by clear steps.",
        "product": None,
        "core_benefit": None,
        "scene_structure": [
            {"beat": "context", "purpose": "orient", "action": "show a generic workspace"}
        ],
        "dialogue": None,
        "actions": ["Present the steps in a new sequence."],
        "camera": None,
        "lighting": None,
        "location": None,
        "emotion": None,
        "retention_devices": ["Progressive explanation"],
        "cta": "Invite viewers to review the information provided.",
        "duration_seconds": 20,
        "adaptation_notes": ["Confirm target model controls before use."],
        "originality_notes": ["New scenario and wording; reference assets excluded."],
    }


class AnalysisContractTests(unittest.TestCase):
    def test_analysis_payload_accepts_complete_contract(self):
        parsed = ReferenceAnalysisPayload.from_dict(analysis_payload())
        self.assertEqual(parsed.reference_id, "reference-42")

    def test_analysis_payload_rejects_missing_sections(self):
        payload = analysis_payload()
        del payload["observations"]
        with self.assertRaises(ValueError):
            ReferenceAnalysisPayload.from_dict(payload)

    def test_analysis_schema_json_is_parseable(self):
        schema_path = Path(__file__).parents[1] / "schemas" / "reference_analysis_input.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertIn("reusable_patterns", schema["required"])

    def test_ingestion_bridge_creates_analysis_seed(self):
        output = IngestionOutput(
            source=VideoInput(source_type="local", source="clip.mp4"),
            status="partial",
            scenes=(Scene(0, 3, main_action="A generic action."),),
        )
        seed = ingestion_to_analysis_seed(output, "r-1")
        self.assertEqual(seed.reference_id, "r-1")
        self.assertEqual(len(seed.observations), 1)


class RemodelingTests(unittest.TestCase):
    def test_reference_transforms_to_complete_ugc_concept(self):
        result = transform_reference_to_ugc(analysis_payload(), concept_draft())
        self.assertEqual(result.reference_id, "reference-42")
        self.assertIsNone(result.product)
        self.assertEqual(result.to_dict()["hook"], concept_draft()["hook"])

    def test_reference_id_is_preserved_and_mismatch_rejected(self):
        draft = concept_draft()
        result = transform_reference_to_ugc(analysis_payload(), draft)
        self.assertEqual(result.to_dict()["reference_id"], analysis_payload()["reference_id"])
        draft["reference_id"] = "another-reference"
        with self.assertRaises(ValueError):
            transform_reference_to_ugc(analysis_payload(), draft)

    def test_incomplete_ugc_output_is_rejected(self):
        draft = concept_draft()
        del draft["cta"]
        with self.assertRaises(ValueError):
            transform_reference_to_ugc(analysis_payload(), draft)

    def test_empty_scene_structure_is_rejected(self):
        draft = concept_draft()
        draft["scene_structure"] = []
        with self.assertRaises(ValueError):
            validate_ugc_output({"reference_id": "reference-42", **draft})

    def test_analysis_without_patterns_cannot_be_remodeled(self):
        analysis = analysis_payload()
        analysis["reusable_patterns"] = []
        with self.assertRaises(ValueError):
            transform_reference_to_ugc(analysis, concept_draft())

    def test_ugc_output_schema_json_is_parseable(self):
        schema_path = Path(__file__).parents[1] / "schemas" / "ugc_output.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        self.assertIn("originality_notes", schema["required"])


if __name__ == "__main__":
    unittest.main()
