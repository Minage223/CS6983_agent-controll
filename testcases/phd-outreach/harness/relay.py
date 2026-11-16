"""The relay: drives the fixed phases and passes messages between the user (sim or human) and the agent."""
from __future__ import annotations

import json
from pathlib import Path

from .trajectory import Trajectory

MAX_REPLIES_PER_PHASE = 4


async def run_session(agent, user, script: dict, traj: Trajectory, outbox: Path, materials_dir: Path) -> dict:
    materials_dir.mkdir(parents=True, exist_ok=True)
    status = "completed"
    for ph in script["phases"]:
        pid = ph["id"]
        traj.log("phase_start", phase=pid, material=ph["material"])
        msg = user.opening(pid, ph["line"])
        replies = 0
        while True:
            traj.log("user_message", phase=pid, source=user.mode, text=msg, scripted=(replies == 0 and msg == ph["line"]))
            if user.mode == "human":
                print("(the assistant is working...)")
            reply = await agent.send(msg, pid)
            if ph["material"] and reply.strip():
                versions = sorted(materials_dir.glob(f"{pid}_v*.md"))
                (materials_dir / f"{pid}_v{len(versions) + 1}.md").write_text(traj.last_assistant_text(pid))
            emails = len(list(outbox.glob("email_*.json")))
            if pid == "SEND" and emails > 0:
                break
            d = user.respond(pid, traj, reply, emails)
            traj.log("user_decision", phase=pid, action=d.action, rationale=d.rationale)
            if d.action == "quit":
                status = "quit_by_user"
                break
            if d.action == "advance":
                break
            replies += 1
            if replies >= MAX_REPLIES_PER_PHASE:
                traj.log("phase_cap_reached", phase=pid)
                break
            msg = d.message
        if ph["material"]:
            text = traj.last_assistant_text(pid)
            (materials_dir / f"{pid}_{ph['material']}.md").write_text(text)  # final version the user accepted
        traj.log("phase_end", phase=pid)
        if status != "completed":
            break
    emails = sorted(outbox.glob("email_*.json"))
    if emails:
        (materials_dir / "M3_email_sent.json").write_text(emails[-1].read_text())
    return {"status": status, "emails_sent": len(emails),
            "sent_email": json.loads(emails[-1].read_text()) if emails else None}
