"""Terminal survey for user testing. Answers are saved to <run>/survey.json.

    python -m harness.survey pre  runs/<folder>     # before the session
    python -m harness.survey post runs/<folder>     # after the session: per-material items, edits, then post items

Edit-before-send: for each material the participant edits a copy in <run>/edits/ until they would send it;
edit_distance (word-level, 0–1) is computed against the agent's version.
"""
from __future__ import annotations

import difflib
import json
import shutil
import sys
from pathlib import Path

from .judge import FINAL_FILES
from .lexicons import words
from .paths import REPO

ITEMS = json.loads((REPO / "study" / "survey_items.json").read_text())


def ask(text: str, lo: int = 1, hi: int = 7) -> int:
    while True:
        v = input(f"{text}\n  [{lo}-{hi}] > ").strip()
        if v.isdigit() and lo <= int(v) <= hi:
            return int(v)


def edit_distance(a: str, b: str) -> float:
    return round(1 - difflib.SequenceMatcher(a=words(a), b=words(b)).ratio(), 4)


def main(stage: str, run_dir: Path) -> None:
    path = run_dir / "survey.json"
    data = json.loads(path.read_text()) if path.exists() else {}
    if stage == "pre":
        data["pre"] = {it["id"]: ask(it["text"]) for it in ITEMS["pre"]}
    elif stage == "post":
        extracted = json.loads((run_dir / "materials" / "extracted.json").read_text()) \
            if (run_dir / "materials" / "extracted.json").exists() else {}
        data["per_material"], data["edits"] = {}, {}
        (run_dir / "edits").mkdir(exist_ok=True)
        for key, name in ITEMS["materials"].items():
            src = run_dir / "materials" / FINAL_FILES[key]
            src = src if src.exists() else None
            original = extracted.get(key) or (src.read_text() if src else "")
            dst = run_dir / "edits" / f"{key}_{name.replace(' ', '_')}.md"
            if not dst.exists():
                dst.write_text(original)
            print(f"\n=== {name.upper()} ===\nOpen and read: {dst}")
            data["per_material"][key] = {it["id"]: ask(it["text"].format(material=name)) for it in ITEMS["per_material"]}
            input(f"Now edit {dst} until you would actually send it. Save, then press Enter. ")
            data["edits"][key] = {"file": str(dst.relative_to(run_dir)), "edit_distance": edit_distance(original, dst.read_text())}
        data["post"] = {it["id"]: ask(it["text"]) for it in ITEMS["post"]}
        if "pre" in data:
            data["confidence_change"] = {k: data["post"][k] - data["pre"][k] for k in data["pre"]}
    else:
        raise SystemExit("stage must be pre or post")
    path.write_text(json.dumps(data, indent=2))
    print(f"Saved {path}")


if __name__ == "__main__":
    main(sys.argv[1], Path(sys.argv[2]))
