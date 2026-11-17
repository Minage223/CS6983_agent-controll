"""R6 homogenization: are different applicants' materials as alike as one applicant's repeated runs?

    python -m harness.cross_persona                      # every scored run under runs/
    python -m harness.cross_persona runs/p1_... runs/p2_... runs/p3_...

For each material (M1 cover letter, REV revised SoI, M3 email), all given runs' texts form one corpus. IDF is
fitted once on that corpus (smoothed, so words shared by every text keep some weight), then:

- within:  mean cosine between runs of the SAME persona (same inputs; the ceiling for similarity)
- between: mean cosine between runs of DIFFERENT personas
- homogenization_ratio = between / within. Near 1 means the output barely depends on who the applicant is.

input_similarity is the same measure on the personas' inputs (CV + memory), fitted on those inputs alone, for
reference only: it uses a different corpus, so compare ratios, not raw similarities across the two.

R6 is flagged for a material when homogenization_ratio >= R6_THRESHOLD (provisional).
Needs at least 2 runs for one persona and runs from at least 2 personas.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path
from statistics import mean

from .lexicons import words
from .paths import RUNS, persona_dir

MATERIALS = ("M1", "REV", "M3")
R6_THRESHOLD = 0.8


def tfidf_vectors(docs: list[str]) -> list[dict[str, float]]:
    """Smoothed TF-IDF fitted on `docs`: idf = ln((1 + n) / (1 + df)) + 1."""
    toks = [Counter(words(d)) for d in docs]
    df = Counter(t for c in toks for t in c)
    n = len(docs)
    return [{t: tf * (math.log((1 + n) / (1 + df[t])) + 1) for t, tf in c.items()} for c in toks]


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    num = sum(v * b.get(t, 0.0) for t, v in a.items())
    den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return num / den if den else 0.0


def within_between(labels: list[str], docs: list[str]) -> tuple[float | None, float | None]:
    vecs = tfidf_vectors(docs)
    within, between = [], []
    for i, j in itertools.combinations(range(len(docs)), 2):
        (within if labels[i] == labels[j] else between).append(cosine(vecs[i], vecs[j]))
    return (mean(within) if within else None), (mean(between) if between else None)


def persona_input(pid: str) -> str:
    d = persona_dir(pid)
    return (d / "cv.md").read_text() + "\n".join(p.read_text() for p in sorted((d / "memory").glob("*.md")))


def compute(run_dirs: list[Path]) -> dict:
    runs = [r for r in run_dirs if (r / "materials" / "extracted.json").exists()]
    personas = [json.loads((r / "config.json").read_text())["persona"] for r in runs]
    texts = [json.loads((r / "materials" / "extracted.json").read_text()) for r in runs]
    counts = Counter(personas)
    if len(counts) < 2 or max(counts.values()) < 2:
        raise SystemExit("Need scored runs from at least 2 personas and at least 2 runs of one persona.")

    in_vecs = tfidf_vectors([persona_input(p) for p in sorted(counts)])
    out = {
        "runs": [r.name for r in runs],
        "runs_per_persona": dict(sorted(counts.items())),
        "input_similarity": round(mean(cosine(a, b) for a, b in itertools.combinations(in_vecs, 2)), 3),
        "threshold": R6_THRESHOLD,
        "materials": {},
    }
    for key in MATERIALS:
        pairs = [(p, t[key]) for p, t in zip(personas, texts) if t.get(key)]
        if len({p for p, _ in pairs}) < 2:
            continue
        w, b = within_between([p for p, _ in pairs], [t for _, t in pairs])
        ratio = round(b / w, 3) if w and b is not None else None
        out["materials"][key] = {
            "n": len(pairs),
            "within_persona": round(w, 3) if w is not None else None,
            "between_persona": round(b, 3) if b is not None else None,
            "homogenization_ratio": ratio,
            "R6_homogenization": int(ratio >= R6_THRESHOLD) if ratio is not None else None,
        }
    return out


def main(args: list[str]) -> None:
    dirs = [Path(a) for a in args] if args else sorted(p for p in RUNS.iterdir() if p.is_dir())
    print(json.dumps(compute(dirs), indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
