"""Repository paths. Everything the agent must never see lives under PERSONAS/*/ground_truth and GROUND_TRUTH."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PERSONAS = REPO / "personas"
GROUND_TRUTH = REPO / "ground_truth"
SNAPSHOT = REPO / "environment" / "faculty_snapshot" / "tianshi-li"
PROMPTS = REPO / "prompts"
RUNS = REPO / "runs"


def persona_dir(persona_id: str) -> Path:
    d = PERSONAS / persona_id
    if not d.is_dir():
        raise FileNotFoundError(f"Unknown persona: {persona_id}")
    return d
