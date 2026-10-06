"""Map ingestion output into evidence candidates for 03_PROMPTS/REFERENCE_ANALYSIS."""

from __future__ import annotations

from typing import Any

from ..schemas.contracts import IngestionOutput


def to_reference_analysis_payload(
    output: IngestionOutput, reference_id: str | None = None
) -> dict[str, Any]:
    """Create a reviewable evidence seed, not a completed analysis or interpretation."""
    identifier = (
        reference_id
        or output.source.metadata.get("reference_id")
        or output.source.filename
        or output.source.source
    )
    context = {
        "source_type": output.source.source_type,
        "source": output.source.source,
        "filename": output.source.filename,
        "language": output.source.language,
        "duration_seconds": output.source.duration,
        "platform": output.source.platform,
        "metadata": dict(output.source.metadata),
        "media_metadata": dict(output.media_metadata),
        "ingestion_status": output.status,
        "warnings": list(output.warnings),
    }
    if output.transcription_result is not None:
        context["transcription"] = output.transcription_result.to_metadata_dict()
    observations: list[dict[str, Any]] = []
    interpretations: list[dict[str, Any]] = []
    seen: set[tuple[str, str, float | None, float | None]] = set()

    def add(
        field_name: str, content: str, start: float | None, end: float | None,
        source_name: str, *, language: str | None = None,
        confidence: float | None = None, speaker: str | None = None,
    ) -> None:
        key = (field_name, content, start, end)
        if key in seen:
            return
        seen.add(key)
        observation = {
            "field": field_name,
            "classification": "OBSERVADO",
            "content": content,
            "evidence_locator": {"start_seconds": start, "end_seconds": end},
            "evidence_source": source_name,
            "review_status": "PENDING_HUMAN_REVIEW",
        }
        if language is not None:
            observation["language"] = language
        if confidence is not None:
            observation["confidence"] = confidence
        if speaker is not None:
            observation["speaker"] = speaker
        observations.append(observation)

    for scene in output.scenes:
        start, end = scene.start_seconds, scene.end_seconds
        mappings = (
            ("OBSERVED_VISUAL_DESCRIPTION", scene.visual_description),
            ("OBSERVED_ACTION", scene.main_action),
            ("OBSERVED_PERSON_CHARACTER", scene.person_character),
            ("OBSERVED_PRODUCT_DEMO", scene.product),
            ("OBSERVED_ENVIRONMENT", scene.environment),
            ("OBSERVED_FRAMING", scene.framing),
            ("OBSERVED_CAMERA_MOVEMENT", scene.camera_movement),
            ("OBSERVED_DIALOGUE", scene.speech),
            ("OBSERVED_AUDIO_MUSIC", scene.audio_music),
            ("OBSERVED_CTA", scene.cta),
        )
        for field_name, content in mappings:
            if content:
                add(field_name, content, start, end, "scene_analysis_adapter")
        for text in scene.on_screen_text:
            add("OBSERVED_ON_SCREEN_TEXT", text, start, end, "scene_ocr_adapter")
        for note in scene.observations:
            add("OBSERVED_NOTE", note, start, end, "scene_analysis_adapter")
        if scene.perceived_emotion:
            interpretations.append({
                "field": "PERCEIVED_EMOTION",
                "classification": "INTERPRETADO",
                "content": scene.perceived_emotion,
                "evidence_locator": {"start_seconds": start, "end_seconds": end},
                "evidence_source": "scene_analysis_adapter",
                "review_status": "PENDING_HUMAN_REVIEW",
            })

    for segment in output.transcript:
        segment_language = segment.language
        if segment_language is None and output.transcription_result is not None:
            segment_language = output.transcription_result.language
        add(
            "OBSERVED_DIALOGUE", segment.text, segment.start_seconds, segment.end_seconds,
            "transcription_adapter", language=segment_language,
            confidence=segment.confidence, speaker=segment.speaker,
        )
    derived_translations: list[dict[str, Any]] = []
    for segment in output.translated_transcript:
        derived_translations.append({
            "field": "TRANSLATED_DIALOGUE",
            "content": segment.text,
            "evidence_locator": {
                "start_seconds": segment.start_seconds,
                "end_seconds": segment.end_seconds,
            },
            "evidence_source": "translation_adapter",
            "review_status": "PENDING_HUMAN_REVIEW",
            "language": segment.language,
        })
    for item in output.ocr:
        add("OBSERVED_ON_SCREEN_TEXT", item.text, item.timestamp_seconds, item.timestamp_seconds, "ocr_adapter")

    return {
        "reference_id": str(identifier),
        "source_context": context,
        "observations": observations,
        "interpretations": interpretations,
        "derived_translations": derived_translations,
        "reusable_patterns": [],
        "mechanisms": [],
        "non_copyable_elements": [],
        "remodeling_opportunities": [],
        "hypotheses_to_test": [],
    }
