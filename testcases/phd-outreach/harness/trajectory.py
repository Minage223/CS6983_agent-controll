"""Append-only event log written to trajectory.json.

Every message, tool call, tool result, and phase marker is recorded in order with an ISO timestamp.
"""
from __future__ import annotations

import json
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


class Trajectory:
    def __init__(self, path: Path, meta: dict[str, Any]):
        self.path = path
        self.meta = meta
        self.events: list[dict[str, Any]] = []
        self._lock = threading.Lock()

    def log(self, type_: str, **data: Any) -> dict[str, Any]:
        ev = {"i": len(self.events), "t": now(), "type": type_, **data}
        with self._lock:
            self.events.append(ev)
            self.flush()
        return ev

    def flush(self) -> None:
        text = json.dumps({"meta": self.meta, "events": self.events}, indent=2, ensure_ascii=False)
        # The CLI may mention files under the runner's home directory (e.g. persisted tool output); hide the username.
        self.path.write_text(text.replace(str(Path.home()), "<HOME>"))

    # Convenience views used by the relay, the sim user, and the judge.
    def phase_events(self, phase: str) -> list[dict[str, Any]]:
        out, cur = [], None
        for ev in self.events:
            if ev["type"] == "phase_start":
                cur = ev["phase"]
            if cur == phase:
                out.append(ev)
        return out

    def last_assistant_text(self, phase: str) -> str:
        texts = [e["text"] for e in self.phase_events(phase) if e["type"] == "assistant_text" and e["text"].strip()]
        return texts[-1] if texts else ""

    def dialogue(self, include_tools: bool = False) -> list[dict[str, str]]:
        """User/assistant turns as plain text (what the user could see)."""
        out = []
        for ev in self.events:
            if ev["type"] == "user_message":
                out.append({"role": "user", "text": ev["text"], "phase": ev.get("phase", "")})
            elif ev["type"] == "assistant_text":
                out.append({"role": "assistant", "text": ev["text"], "phase": ev.get("phase", "")})
            elif include_tools and ev["type"] == "tool_use":
                out.append({"role": "tool_use", "text": json.dumps({"name": ev["name"], "input": ev["input"]}, ensure_ascii=False), "phase": ev.get("phase", "")})
        return out
