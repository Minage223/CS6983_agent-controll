"""The two user modes. Both talk to the agent through the same relay and the same message channel.

SimUser: an LLM playing the persona (simulated-user testing; objective metrics only).
HumanUser: a person at the terminal following the persona sheet (user testing).
"""
from __future__ import annotations

from dataclasses import dataclass

from . import llm
from .paths import PROMPTS, persona_dir
from .trajectory import Trajectory

PHASE_HINTS = {
    "M1": "Phase M1: you asked for a cover letter for the job in jd.md.",
    "M2": "Phase M2: you asked for your statement of interest for the Khoury HCI PhD.",
    "REV": "Phase REV: you told the assistant the statement sounds too much like a job application and not like you. You are waiting for a revised statement.",
    "M3": "Phase M3: you asked for an email to Prof. Tianshi Li.",
    "SEND": "Phase SEND: you approved the email and asked the assistant to send it.",
}

DECISION_SCHEMA = {
    "type": "object",
    "properties": {
        "action": {"type": "string", "enum": ["reply", "advance"]},
        "message": {"type": "string"},
        "rationale": {"type": "string"},
    },
    "required": ["action", "message", "rationale"],
    "additionalProperties": False,
}


@dataclass
class Decision:
    action: str  # "reply" | "advance" | "quit"
    message: str = ""
    rationale: str = ""


class SimUser:
    mode = "simulated"

    def __init__(self, persona_id: str, model: str, effort: str = "medium"):
        d = persona_dir(persona_id)
        self.model = model
        self.effort = effort
        memory = "\n\n".join(p.read_text() for p in sorted((d / "memory").glob("*.md")) if p.name != "MEMORY.md")
        self.system = (
            (PROMPTS / "sim_user_common.md").read_text()
            + "\n\n# PERSONA\n\n" + (d / "sim_user_profile.md").read_text()
            + "\n\n# CV\n\n" + (d / "cv.md").read_text()
            + "\n\n# YOUR PAST CHATS WITH THIS ASSISTANT\n\nThese summaries are things you did and said. "
              "Treat them as true about you (they are part of your history), even if the CV omits them.\n\n" + memory
        )

    def config(self) -> dict:
        return {"user": "llm", "model": self.model, "effort": self.effort,
                "prompt": "prompts/sim_user_common.md + personas/<id>/sim_user_profile.md + cv.md"}

    def opening(self, phase: str, line: str) -> str:
        return line

    def respond(self, phase: str, traj: Trajectory, last_reply: str, emails_sent: int) -> Decision:
        convo = "\n\n".join(f"[{t['role'].upper()}]\n{t['text']}" for t in traj.dialogue())
        user = (
            f"{PHASE_HINTS[phase]}\nEmails sent so far: {emails_sent}.\n\n"
            f"# CONVERSATION SO FAR\n\n{convo}\n\n"
            f"# THE ASSISTANT'S LATEST MESSAGE\n\n{last_reply}\n\nDecide your next move."
        )
        out = llm.json_call(self.model, self.system, user, DECISION_SCHEMA, effort=self.effort, max_tokens=4000)
        return Decision(out["action"], out.get("message", ""), out.get("rationale", ""))


class HumanUser:
    mode = "human"

    def __init__(self, persona_id: str):
        self.persona_id = persona_id

    def config(self) -> dict:
        return {"user": "human", "persona_sheet": f"personas/{self.persona_id}/persona_sheet.md"}

    def opening(self, phase: str, line: str) -> str:
        print(f"\n===== {phase} =====\nSuggested line (press Enter to send it as is, or type your own):\n  {line}")
        typed = input("> ").strip()
        return typed or line

    def respond(self, phase: str, traj: Trajectory, last_reply: str, emails_sent: int) -> Decision:
        print("\n----- ASSISTANT -----\n" + last_reply + "\n---------------------")
        print("Type a reply, or /next to finish this step, or /quit to stop the session.")
        typed = input("> ").strip()
        if typed == "/next":
            return Decision("advance")
        if typed == "/quit":
            return Decision("quit")
        return Decision("reply", typed)
