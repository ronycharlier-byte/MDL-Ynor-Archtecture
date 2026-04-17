from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional


class EventTracker:
    """
    Record maintenance events as JSONL entries.
    """

    def __init__(self, sink_path: Optional[str] = None):
        self.events: List[Dict[str, Any]] = []
        self.sink_path = Path(sink_path) if sink_path else None
        if self.sink_path:
            self.sink_path.parent.mkdir(parents=True, exist_ok=True)

    def log_event(self, level: str, data: Dict[str, Any], kind: str = "event") -> Dict[str, Any]:
        event = {
            "timestamp": time.time(),
            "level": str(level).upper(),
            "kind": kind,
            "data": data,
        }
        self.events.append(event)
        if self.sink_path:
            with self.sink_path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event

    def latest(self) -> Optional[Dict[str, Any]]:
        return self.events[-1] if self.events else None

    def count_by_level(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for event in self.events:
            level = str(event.get("level", "UNKNOWN"))
            counts[level] = counts.get(level, 0) + 1
        return counts
