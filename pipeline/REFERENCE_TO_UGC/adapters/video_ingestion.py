"""Bridge that adapts VIDEO_INGESTION evidence into the analysis payload contract."""

from __future__ import annotations

from typing import Any

from pipeline.VIDEO_INGESTION.schemas.contracts import IngestionOutput
from pipeline.VIDEO_INGESTION.adapters.reference_analysis_bridge import to_reference_analysis_payload
from ..schemas.contracts import ReferenceAnalysisPayload


def ingestion_to_analysis_seed(
    output: IngestionOutput, reference_id: str | None = None
) -> ReferenceAnalysisPayload:
    payload: dict[str, Any] = to_reference_analysis_payload(output, reference_id)
    return ReferenceAnalysisPayload.from_dict(payload)
