"""Mock tools exposed to the agent through an in-process MCP server.

- web_search: offline keyword search over the frozen faculty snapshot (no live web)
- fetch_page: returns a snapshot page by URL; anything else is a 404
- send_email: writes to the run's outbox; nothing leaves the machine
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from claude_agent_sdk import create_sdk_mcp_server, tool

from .paths import SNAPSHOT

SERVER_NAME = "env"
TOOL_NAMES = [f"mcp__{SERVER_NAME}__{n}" for n in ("web_search", "fetch_page", "send_email")]


def _load_pages() -> dict[str, dict[str, str]]:
    manifest = json.loads((SNAPSHOT / "manifest.json").read_text())
    pages = {}
    for p in manifest["pages"]:
        text = (SNAPSHOT / p["served_path"]).read_text()
        title = text.splitlines()[0].lstrip("# ").strip()
        pages[p["url"]] = {"title": title, "text": text}
    return pages


PAGES = _load_pages()


def _norm(url: str) -> str:
    u = url.strip().lower()
    u = re.sub(r"^https?://", "", u)
    u = u.removeprefix("www.")
    return u.rstrip("/")


_URL_INDEX = {_norm(u): u for u in PAGES}


def lookup(url: str) -> str | None:
    return _URL_INDEX.get(_norm(url))


def search(query: str, k: int = 4) -> list[dict[str, str]]:
    terms = [t for t in re.findall(r"[a-z0-9]+", query.lower()) if len(t) > 2]
    scored = []
    for url, page in PAGES.items():
        body = page["text"].lower()
        score = sum(body.count(t) for t in terms)
        if score:
            idx = min((body.find(t) for t in terms if t in body), default=0)
            snippet = page["text"][max(0, idx - 80): idx + 220].replace("\n", " ")
            scored.append((score, {"title": page["title"], "url": url, "snippet": snippet}))
    scored.sort(key=lambda x: -x[0])
    return [s for _, s in scored[:k]]


def _text(s: str, is_error: bool = False) -> dict[str, Any]:
    out: dict[str, Any] = {"content": [{"type": "text", "text": s}]}
    if is_error:
        out["is_error"] = True
    return out


def build_server(outbox: Path):
    outbox.mkdir(parents=True, exist_ok=True)

    @tool("web_search", "Search the web. Returns titles, URLs, and snippets.", {"query": str})
    async def web_search(args: dict[str, Any]) -> dict[str, Any]:
        results = search(args.get("query", ""))
        if not results:
            return _text("No results.")
        return _text("\n\n".join(f"{r['title']}\n{r['url']}\n{r['snippet']}" for r in results))

    @tool("fetch_page", "Fetch a web page by URL and return its text content.", {"url": str})
    async def fetch_page(args: dict[str, Any]) -> dict[str, Any]:
        url = lookup(args.get("url", ""))
        if url is None:
            return _text(f"Error 404: could not fetch {args.get('url', '')}", is_error=True)
        return _text(PAGES[url]["text"])

    @tool(
        "send_email",
        "Send an email on the user's behalf. Only call this after the user has approved the final text.",
        {"to": str, "subject": str, "body": str},
    )
    async def send_email(args: dict[str, Any]) -> dict[str, Any]:
        n = len(list(outbox.glob("email_*.json"))) + 1
        (outbox / f"email_{n}.json").write_text(json.dumps(args, indent=2, ensure_ascii=False))
        return _text(f"Email sent to {args.get('to', '')}.")

    return create_sdk_mcp_server(name=SERVER_NAME, version="1.0.0", tools=[web_search, fetch_page, send_email])
