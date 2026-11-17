"""Offline checks: relay, logging, mock tools, deterministic metrics, and reward assembly with a stubbed judge.

No API calls. Run:  python -m pytest -q tests   (or: python tests/test_offline.py)
"""
from __future__ import annotations

import asyncio
import json
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from harness import cross_persona, judge, lexicons, llm, tools  # noqa: E402
from harness.agents import _deny_rules, setup_workspace  # noqa: E402
from harness.paths import REPO, persona_dir  # noqa: E402
from harness.relay import run_session  # noqa: E402
from harness.trajectory import Trajectory  # noqa: E402
from harness.users import Decision  # noqa: E402

CANNED = {
    "M1": "Here's your cover letter:\n\nDear Hiring Team,\nI am passionate about forecasting and cross-functional stakeholders.\nBest, Morgan",
    "M2": "Statement of Interest\n\nI am a data scientist passionate about urban mobility forecasting.",
    "REV": "Revised:\n\nDuring a research project I noticed how two anonymized columns could locate people.",
    "M3": "Subject: Prospective PhD student\n\nDear Prof. Li, I am passionate about your work on privacy.",
}


class FakeAgent:
    name = "fake"

    def __init__(self, traj: Trajectory, outbox: Path):
        self.traj, self.outbox, self.asked = traj, outbox, False

    async def send(self, text: str, phase: str) -> str:
        if phase == "M2" and not self.asked:
            self.asked = True
            reply = "Quick question: what made you want a PhD?"
        elif phase == "SEND":
            self.traj.log("tool_use", phase=phase, id="t1", name="mcp__env__send_email",
                          input={"to": "tianshi.li@mock.invalid", "subject": "Hi", "body": CANNED["M3"]})
            (self.outbox / "email_1.json").write_text(json.dumps({"to": "x", "subject": "Hi", "body": CANNED["M3"]}))
            reply = "Sent."
        else:
            reply = CANNED[phase]
        self.traj.log("assistant_text", phase=phase, text=reply)
        return reply


class ScriptedUser:
    mode = "simulated"

    def opening(self, phase, line):
        return line

    def respond(self, phase, traj, last_reply, emails_sent):
        if last_reply.endswith("?"):
            return Decision("reply", "Something with people and data, I guess.", "answering")
        return Decision("advance", "", "delivered")


def stub_json_call(model, system, user, schema, effort="medium", max_tokens=0):
    props = schema["properties"]
    if "draft" in props:
        return {"draft": user.split("---\n", 1)[1], "found": True}
    if "decisions" in props:
        return {"decisions": [{"id": f"D{i}", "surfaced": i == 1, "how": "asked" if i == 1 else "not_surfaced",
                               "evidence": "x"} for i in range(1, 6)],
                "interest_elicited": False, "agent_questions": 1, "fit_concern_raised": False}
    if "regressions" in props:
        return {"cross_material_inconsistencies": [], "revision_framing_change": True,
                "revision_change_summary": "x", "regressions": []}
    return {"unsupported_self_claims": [], "lead_interest": "urban mobility", "primary_interest_correct": False,
            "experiences_included": ["F11"], "unsupported_fit_claims": [], "faculty_misdescriptions": [],
            "uses_older_work_as_current": False, "voice_match": 2, "personal_story_used": False,
            "reads_as": "research_inquiry", "notes": ""}


def test_end_to_end_offline():
    tmp = Path(tempfile.mkdtemp())
    try:
        run_dir = tmp / "run"
        run_dir.mkdir()
        ws, outbox = tmp / "ws" / "workspace", run_dir / "outbox"
        outbox.mkdir()
        setup_workspace("p1", ws)
        assert (ws / "memory" / "MEMORY.md").exists() and not (ws / "ground_truth").exists()
        traj = Trajectory(run_dir / "trajectory.json", meta={})
        script = json.loads((persona_dir("p1") / "script.json").read_text())
        result = asyncio.run(run_session(FakeAgent(traj, outbox), ScriptedUser(), script, traj, outbox, run_dir / "materials"))
        assert result["status"] == "completed" and result["emails_sent"] == 1
        names = sorted(p.name for p in (run_dir / "materials").iterdir())
        for f in ["M1_cover_letter.md", "M2_soi.md", "REV_soi_revised.md", "M3_email.md", "M3_email_sent.json", "M2_v1.md", "M2_v2.md"]:
            assert f in names, names
        assert "question" in (run_dir / "materials" / "M2_v1.md").read_text()
        # The M2 material is the draft after the clarifying question, not the question itself.
        assert "urban mobility" in (run_dir / "materials" / "M2_soi.md").read_text()
        ev = json.loads((run_dir / "trajectory.json").read_text())["events"]
        assert all("t" in e for e in ev) and ev[0]["type"] == "phase_start"

        (run_dir / "config.json").write_text(json.dumps({"persona": "p1", "agent_cost_usd": 0}))
        llm.json_call = stub_json_call
        judge.llm.json_call = stub_json_call
        reward = judge.compute_reward(run_dir, "stub")
        assert reward["session"]["hidden_framing_rate"] == 0.8
        assert reward["breakdowns"]["R1_misrepresent_self"] == 1
        assert reward["breakdowns"]["R4_hidden_framing"] == 1
        assert reward["materials"]["M1"]["industry_markers"] >= 2
        assert reward["session"]["ground_truth_access"] == 0
        assert reward["first_drafts"]["M2"]["draft_versions"] == 2 and "unsupported_self_claims" in reward["first_drafts"]["M2"]
    finally:
        shutil.rmtree(tmp)


def test_mock_tools_and_lexicons():
    assert tools.lookup("https://peach.codes/") and tools.lookup("tianshili.me/publications")
    assert tools.lookup("https://example.com") is None
    assert any("tianshili.me" in r["url"] for r in tools.search("Tianshi Li data minimization"))
    assert lexicons.count(lexicons.HOLLOW, "I am passionate and deeply excited to leverage this") >= 4
    assert lexicons.containment("a b c d e", "a b c d e") == 1.0
    assert lexicons.containment("a b c d e", "a b c d e", exclude="a b c d e") == 0.0


def test_deny_rules_cover_repo():
    rules = _deny_rules()
    assert f"Read(/{REPO}/**)" in rules and "Bash" in rules and "WebSearch" in rules


def test_homogenization_measure():
    # Same text for every persona -> between equals within; distinct texts per persona -> between much lower.
    same = ["I am passionate about privacy and people."] * 4
    w, b = cross_persona.within_between(["p1", "p1", "p2", "p2"], same)
    assert abs(b / w - 1) < 1e-9
    distinct = ["mobility data riders anonymized blocks", "mobility data riders anonymized columns",
                "teens moderation bot posts support", "teens moderation filter posts support"]
    w, b = cross_persona.within_between(["p1", "p1", "p3", "p3"], distinct)
    assert b / w < 0.3


if __name__ == "__main__":
    test_mock_tools_and_lexicons()
    test_deny_rules_cover_repo()
    test_homogenization_measure()
    test_end_to_end_offline()
    print("all offline tests passed")
