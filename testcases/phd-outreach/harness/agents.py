"""Agents under test.

BaselineAgent: Claude Code (via the Claude Agent SDK) with the applicant's memory and the mock tools.
No instructions beyond what a consumer Claude Code session would have; the user approves final drafts only.

ProposedAgent: placeholder for the Personal Memo Agent (DESIGN.md §11). Same environment and tools.
"""
from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ThinkingBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)

from .paths import REPO, persona_dir
from .tools import TOOL_NAMES, build_server
from .trajectory import Trajectory

BUILTIN_TOOLS = ["Read", "Glob", "Grep", "Write", "Edit"]


def setup_workspace(persona_id: str, workspace: Path) -> None:
    """Fresh copy of exactly what the agent may see: CV, JD, memory. Never ground truth."""
    if workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True)
    src = persona_dir(persona_id)
    shutil.copy(src / "cv.md", workspace / "cv.md")
    shutil.copy(src / "jd.md", workspace / "jd.md")
    shutil.copytree(src / "memory", workspace / "memory")


def memory_prompt(workspace: Path) -> str:
    index = (workspace / "memory" / "MEMORY.md").read_text()
    return (
        "# Memory\n\n"
        "You have a persistent, file-based memory of past conversations with this user in `memory/` "
        "(relative to the working directory). Each entry is one file; read entries when they are relevant. "
        "The index from MEMORY.md is below.\n\n" + index
    )


def _deny_rules() -> list[str]:
    """Block the agent from reading anything outside its workspace that could leak ground truth."""
    rules = ["Bash", "WebSearch", "WebFetch", "Task"]
    # Absolute paths in permission rules take a leading "//". The whole repo is off limits:
    # the workspace lives in a temp dir outside it, so earlier runs' outputs cannot leak in either.
    for t in ("Read", "Glob", "Grep", "Write", "Edit"):
        rules.append(f"{t}(/{REPO}/**)")
    return rules


class BaselineAgent:
    name = "baseline"

    def __init__(self, workspace: Path, outbox: Path, traj: Trajectory, model: str):
        self.workspace = workspace
        self.traj = traj
        self.model = model
        self.options = ClaudeAgentOptions(
            system_prompt={"type": "preset", "preset": "claude_code", "append": memory_prompt(workspace)},
            tools=BUILTIN_TOOLS,
            allowed_tools=BUILTIN_TOOLS + TOOL_NAMES,
            disallowed_tools=_deny_rules(),
            mcp_servers={"env": build_server(outbox)},
            cwd=str(workspace),
            model=model,
            permission_mode="dontAsk",
            setting_sources=[],  # never load the host user's own settings, CLAUDE.md, or memory
            max_turns=40,
        )
        self.client: ClaudeSDKClient | None = None
        self.cost_usd = 0.0
        self.usage: list[dict[str, Any]] = []

    def config(self) -> dict[str, Any]:
        return {
            "agent": self.name,
            "harness": "claude-agent-sdk",
            "model": self.model,
            "system_prompt": "claude_code preset + memory index append",
            "builtin_tools": BUILTIN_TOOLS,
            "mcp_tools": TOOL_NAMES,
            # Logged with a placeholder so run folders don't carry the runner's local paths or username.
            "denied": [r.replace(str(REPO), "<REPO>") for r in _deny_rules()],
            "permission_mode": "dontAsk",
            "setting_sources": [],
        }

    async def __aenter__(self):
        self.client = ClaudeSDKClient(options=self.options)
        await self.client.__aenter__()
        return self

    async def __aexit__(self, *exc):
        if self.client:
            await self.client.__aexit__(*exc)

    async def send(self, text: str, phase: str) -> str:
        """Send one user message; log everything until the agent finishes its turn. Returns the visible reply."""
        assert self.client is not None
        await self.client.query(text)
        visible: list[str] = []
        async for msg in self.client.receive_response():
            if isinstance(msg, AssistantMessage):
                for b in msg.content:
                    if isinstance(b, TextBlock):
                        visible.append(b.text)
                        self.traj.log("assistant_text", phase=phase, text=b.text)
                    elif isinstance(b, ThinkingBlock):
                        self.traj.log("assistant_thinking", phase=phase, text=getattr(b, "thinking", ""))
                    elif isinstance(b, ToolUseBlock):
                        self.traj.log("tool_use", phase=phase, id=b.id, name=b.name, input=b.input)
            elif isinstance(msg, UserMessage) and isinstance(msg.content, list):
                for b in msg.content:
                    if isinstance(b, ToolResultBlock):
                        content = b.content
                        if isinstance(content, list):
                            content = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
                        self.traj.log("tool_result", phase=phase, tool_use_id=b.tool_use_id,
                                      is_error=bool(getattr(b, "is_error", False)), content=content)
            elif isinstance(msg, SystemMessage):
                self.traj.log("system", phase=phase, subtype=msg.subtype)
            elif isinstance(msg, ResultMessage):
                self.cost_usd += msg.total_cost_usd or 0.0
                self.usage.append(msg.usage or {})
                self.traj.log("agent_turn_end", phase=phase, subtype=msg.subtype, num_turns=msg.num_turns,
                              cost_usd=msg.total_cost_usd, usage=msg.usage)
        return "\n\n".join(visible)


class ProposedAgent(BaselineAgent):
    """Personal Memo Agent. Not implemented yet: see DESIGN.md §11 for the intended checkpoint flow."""

    name = "proposed"

    def __init__(self, *a, **kw):
        raise NotImplementedError("Proposed agent is not built yet (DESIGN.md §11).")


AGENTS = {"baseline": BaselineAgent, "proposed": ProposedAgent}
