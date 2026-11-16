"""Thin wrapper over the Anthropic Messages API for the simulated user and the judge.

Structured output via output_config.format (JSON schema). Server-side refusal fallback is enabled
(fallbacks="default"); a refusal that survives the fallback chain raises.
"""
from __future__ import annotations

import json
from typing import Any

import anthropic

_client: anthropic.Anthropic | None = None


def client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


class Refused(RuntimeError):
    pass


def json_call(model: str, system: str, user: str, schema: dict[str, Any], effort: str = "medium",
              max_tokens: int = 16000) -> dict[str, Any]:
    resp = client().beta.messages.create(
        model=model,
        max_tokens=max_tokens,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        system=system,
        messages=[{"role": "user", "content": user}],
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
    )
    if resp.stop_reason == "refusal":
        raise Refused(str(getattr(resp, "stop_details", "")))
    if resp.stop_reason == "max_tokens":
        raise RuntimeError("Response hit max_tokens before the JSON finished")
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text)
