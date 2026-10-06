"""Contracts and validation for reference analysis and remodeled UGC output."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from math import isfinite
from typing import Any


ANALYSIS_LIST_FIELDS = (
    "observations",
    "interpretations",
    "derived_translations",
    "reusable_patterns",
    "mechanisms",
    "non_copyable_elements",
    "remodeling_opportunities",
    "hypotheses_to_test",
)
OUTPUT_FIELDS = (
    "reference_id",
    "content_type",
    "ugc_template",
    "hook",
    "problem",
    "mechanism",
    "product",
    "core_benefit",
    "scene_structure",
    "dialogue",
    "actions",
    "camera",
    "lighting",
    "location",
    "emotion",
    "retention_devices",
    "cta",
    "duration_seconds",
    "adaptation_notes",
    "originality_notes",
)
NULLABLE_OUTPUT_FIELDS = {"product", "core_benefit", "dialogue", "camera", "lighting", "location", "emotion"}


def _text(value: Any, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")


@dataclass(frozen=True, slots=True)
class ReferenceAnalysisPayload:
    reference_id: str
    source_context: dict[str, Any]
    observations: tuple[dict[str, Any], ...]
    interpretations: tuple[dict[str, Any], ...]
    derived_translations: tuple[dict[str, Any], ...]
    reusable_patterns: tuple[dict[str, Any], ...]
    mechanisms: tuple[dict[str, Any], ...]
    non_copyable_elements: tuple[dict[str, Any], ...]
    remodeling_opportunities: tuple[dict[str, Any], ...]
    hypotheses_to_test: tuple[dict[str, Any], ...]

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> ReferenceAnalysisPayload:
        if not isinstance(payload, dict):
            raise ValueError("reference analysis must be an object")
        required = {"reference_id", "source_context", *ANALYSIS_LIST_FIELDS}
        missing = required - set(payload)
        extra = set(payload) - required
        if missing:
            raise ValueError(f"reference analysis missing fields: {', '.join(sorted(missing))}")
        if extra:
            raise ValueError(f"unknown reference analysis fields: {', '.join(sorted(extra))}")
        _text(payload["reference_id"], "reference_id")
        if not isinstance(payload["source_context"], dict):
            raise ValueError("source_context must be an object")
        normalized: dict[str, Any] = dict(payload)
        for name in ANALYSIS_LIST_FIELDS:
            values = payload[name]
            if not isinstance(values, list):
                raise ValueError(f"{name} must be a list")
            if any(not isinstance(item, dict) for item in values):
                raise ValueError(f"{name} entries must be objects")
            normalized[name] = tuple(values)
        return cls(**normalized)

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        for name in ANALYSIS_LIST_FIELDS:
            result[name] = list(result[name])
        return result


@dataclass(frozen=True, slots=True)
class UGCOutput:
    reference_id: str
    content_type: str
    ugc_template: str
    hook: str
    problem: str
    mechanism: str
    product: str | None
    core_benefit: str | None
    scene_structure: tuple[dict[str, Any], ...]
    dialogue: str | None
    actions: tuple[str, ...]
    camera: str | None
    lighting: str | None
    location: str | None
    emotion: str | None
    retention_devices: tuple[str, ...]
    cta: str
    duration_seconds: float
    adaptation_notes: tuple[str, ...]
    originality_notes: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        for key in (
            "scene_structure", "actions", "retention_devices", "adaptation_notes", "originality_notes"
        ):
            result[key] = list(result[key])
        return result


def validate_ugc_output(payload: dict[str, Any]) -> UGCOutput:
    if not isinstance(payload, dict):
        raise ValueError("UGC output must be an object")
    missing = set(OUTPUT_FIELDS) - set(payload)
    extra = set(payload) - set(OUTPUT_FIELDS)
    if missing:
        raise ValueError(f"UGC output missing fields: {', '.join(sorted(missing))}")
    if extra:
        raise ValueError(f"unknown UGC output fields: {', '.join(sorted(extra))}")

    for name in OUTPUT_FIELDS:
        value = payload[name]
        if name in NULLABLE_OUTPUT_FIELDS and value is None:
            continue
        if name in {"scene_structure", "actions", "retention_devices", "adaptation_notes", "originality_notes"}:
            if not isinstance(value, list) or not value:
                raise ValueError(f"{name} must be a non-empty list")
        elif name == "duration_seconds":
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not isfinite(value)
                or value <= 0
            ):
                raise ValueError("duration_seconds must be a positive number")
        else:
            _text(value, name)

    for index, scene in enumerate(payload["scene_structure"]):
        if not isinstance(scene, dict):
            raise ValueError("scene_structure entries must be objects")
        for field_name in ("beat", "purpose", "action"):
            _text(scene.get(field_name), f"scene_structure[{index}].{field_name}")
        scene_duration = scene.get("duration_seconds")
        if scene_duration is not None and (
            isinstance(scene_duration, bool)
            or not isinstance(scene_duration, (int, float))
            or not isfinite(scene_duration)
            or scene_duration <= 0
        ):
            raise ValueError(f"scene_structure[{index}].duration_seconds must be positive or null")
    for list_name in ("actions", "retention_devices", "adaptation_notes", "originality_notes"):
        for index, item in enumerate(payload[list_name]):
            _text(item, f"{list_name}[{index}]")

    return UGCOutput(
        **{
            key: tuple(value) if key in {
                "scene_structure", "actions", "retention_devices", "adaptation_notes", "originality_notes"
            } else value
            for key, value in payload.items()
        }
    )


def transform_reference_to_ugc(
    analysis_payload: dict[str, Any], concept_draft: dict[str, Any]
) -> UGCOutput:
    """Bind an original concept draft to its source analysis without copying source content."""
    analysis = ReferenceAnalysisPayload.from_dict(analysis_payload)
    if not analysis.reusable_patterns:
        raise ValueError("at least one reusable pattern is required before remodeling")
    if not analysis.remodeling_opportunities:
        raise ValueError("at least one remodeling opportunity is required")
    if not isinstance(concept_draft, dict):
        raise ValueError("concept_draft must be an object")

    draft = dict(concept_draft)
    supplied_reference_id = draft.pop("reference_id", analysis.reference_id)
    if supplied_reference_id != analysis.reference_id:
        raise ValueError("concept reference_id must match the analyzed reference")
    if set(draft) != set(OUTPUT_FIELDS) - {"reference_id"}:
        missing = (set(OUTPUT_FIELDS) - {"reference_id"}) - set(draft)
        extra = set(draft) - (set(OUTPUT_FIELDS) - {"reference_id"})
        details = []
        if missing:
            details.append(f"missing: {', '.join(sorted(missing))}")
        if extra:
            details.append(f"unknown: {', '.join(sorted(extra))}")
        raise ValueError("invalid concept draft fields (" + "; ".join(details) + ")")
    return validate_ugc_output({"reference_id": analysis.reference_id, **draft})
