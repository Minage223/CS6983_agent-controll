"""Run the test case.

Simulated user, 5 baseline runs for P1:
    python -m harness.run --persona p1 --mode sim --runs 5

Human user (role-play or own CV), one session:
    python -m harness.run --persona p1 --mode human

Re-score an existing run folder:
    python -m harness.run --rejudge runs/<folder>
"""
from __future__ import annotations

import argparse
import asyncio
import json
import platform
import shutil
import tempfile
from datetime import datetime
from pathlib import Path

from .agents import AGENTS, setup_workspace
from .judge import compute_reward
from .paths import RUNS, persona_dir
from .relay import run_session
from .trajectory import Trajectory
from .users import HumanUser, SimUser

DEFAULT_MODEL = "claude-opus-5-5"


def _versions() -> dict[str, str]:
    out = {"python": platform.python_version()}
    for pkg in ("claude_agent_sdk", "anthropic"):
        try:
            mod = __import__(pkg)
            out[pkg] = getattr(mod, "__version__", "unknown")
        except Exception:  # pragma: no cover
            out[pkg] = "missing"
    return out


async def one_run(args, k: int) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS / f"{args.persona}_{args.condition}_{args.agent}_{args.mode}_{stamp}_{k}"
    run_dir.mkdir(parents=True)
    # Workspace lives outside the repo (fresh temp dir) so the agent cannot see ground truth or other runs.
    workspace = Path(tempfile.mkdtemp(prefix=f"testcase_{args.persona}_")) / "workspace"
    outbox = run_dir / "outbox"
    setup_workspace(args.persona, workspace)
    script = json.loads((persona_dir(args.persona) / "script.json").read_text())

    if args.mode == "human":
        from .survey import main as survey
        print("Pre-task survey (participant answers):")
        survey("pre", run_dir)
    user = SimUser(args.persona, args.sim_model) if args.mode == "sim" else HumanUser(args.persona)
    config = {
        "mode": "simulated" if args.mode == "sim" else "human",
        "persona": args.persona,
        "condition": args.condition,
        "condition_flags": {"interest": "vague", "target_professor": "given", "delegation": "full",
                            "order": "M1-M2-REV-M3", "cover_letter": "in_session"},
        "run_index": k,
        "started_at": stamp,
        "user": user.config(),
        "judge_model": args.judge_model,
        "versions": _versions(),
    }
    traj = Trajectory(run_dir / "trajectory.json", meta={"run": run_dir.name})
    agent_cls = AGENTS[args.agent]
    async with agent_cls(workspace, outbox, traj, args.agent_model) as agent:
        config["agent"] = agent.config()
        (run_dir / "config.json").write_text(json.dumps(config, indent=2))
        result = await run_session(agent, user, script, traj, outbox, run_dir / "materials")
        config.update({"status": result["status"], "agent_cost_usd": round(agent.cost_usd, 4)})
    (run_dir / "config.json").write_text(json.dumps(config, indent=2))
    # Keep a record of the final workspace (files the agent wrote, if any), minus the copied inputs.
    shutil.copytree(workspace, run_dir / "workspace_final", ignore=shutil.ignore_patterns("memory", "cv.md", "jd.md"))
    shutil.rmtree(workspace.parent, ignore_errors=True)

    if args.mode == "human":
        (run_dir / "edits").mkdir(exist_ok=True)
        (run_dir / "interview.md").write_text((Path(__file__).parent.parent / "study" / "interview_template.md").read_text())
    if not args.no_judge:
        compute_reward(run_dir, args.judge_model)
    print(f"Run saved: {run_dir}")
    return run_dir


PLACEHOLDER_KEY = "YOUR_ANTHROPIC_API_KEY"


def _check_key() -> None:
    """The key comes only from the user's own environment; the repo holds a placeholder."""
    import os
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key or key == PLACEHOLDER_KEY or key == "...":
        raise SystemExit("ANTHROPIC_API_KEY is not set. Run `export ANTHROPIC_API_KEY=<your key>` in your own shell first.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--persona", choices=["p1", "p2", "p3"])
    ap.add_argument("--mode", choices=["sim", "human"], default="sim")
    ap.add_argument("--agent", choices=list(AGENTS), default="baseline")
    ap.add_argument("--condition", default="main")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--agent-model", default=DEFAULT_MODEL)
    ap.add_argument("--sim-model", default=DEFAULT_MODEL)
    ap.add_argument("--judge-model", default=DEFAULT_MODEL)
    ap.add_argument("--no-judge", action="store_true")
    ap.add_argument("--rejudge", type=Path)
    args = ap.parse_args()

    _check_key()  # every mode calls the API (the agent itself, plus the sim user and judge)
    if args.rejudge:
        print(json.dumps(compute_reward(args.rejudge, args.judge_model)["breakdowns"], indent=2))
        return
    if not args.persona:
        ap.error("--persona is required")
    if args.condition != "main":
        ap.error("Only the main condition is wired up so far.")
    if args.mode == "human" and args.runs != 1:
        ap.error("Human mode runs one session at a time.")
    for k in range(1, args.runs + 1):
        asyncio.run(one_run(args, k))


if __name__ == "__main__":
    main()
