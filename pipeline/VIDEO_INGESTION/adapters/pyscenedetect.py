"""Optional PySceneDetect adapter with a lazy, actionable dependency check."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from ..schemas.contracts import Scene
from .ffmpeg import ExternalToolMissing


class PySceneDetectAdapter:
    def __init__(self, threshold: float = 27.0) -> None:
        if threshold <= 0:
            raise ValueError("threshold must be positive")
        self.threshold = threshold

    def detect(self, video_path: Path) -> list[Scene]:
        try:
            from scenedetect import ContentDetector, SceneManager, open_video
        except ImportError as exc:
            raise ExternalToolMissing(
                "PySceneDetect is not installed; install the documented optional package"
            ) from exc
        video = open_video(str(video_path))
        manager = SceneManager()
        manager.add_detector(ContentDetector(threshold=self.threshold))
        manager.detect_scenes(video=video)
        detected = manager.get_scene_list(start_in_scene=True)
        return [
            Scene(
                start_seconds=float(start.get_seconds()),
                end_seconds=float(end.get_seconds()),
                observations=("Scene boundary detected by PySceneDetect; review visual content manually.",),
            )
            for start, end in detected
            if end.get_seconds() > start.get_seconds()
        ]
