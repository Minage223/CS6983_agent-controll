"""R6 homogenization: compare outputs across personas against how similar their inputs are.

    python -m harness.cross_persona runs/p1_... runs/p2_... runs/p3_...

Uses TF-IDF cosine similarity (pure Python) on the extracted REV statements and M3 emails, and on the inputs
(CV + memory). homogenization_ratio > 1 means outputs are more alike than inputs.
"""
from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

from .lexicons import words
from .paths import persona_dir


def tfidf_cos(docs: list[str]) -> float:
    toks = [Counter(words(d)) for d in docs]
    df = Counter(t for c in toks for t in c)
    n = len(docs)
    vecs = [{t: tf * math.log((1 + n) / (1 + df[t])) + tf * 1e-6 for t, tf in c.items()} for c in toks]

    def cos(a, b):
        num = sum(a[t] * b.get(t, 0.0) for t in a)
        den = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
        return num / den if den else 0.0

    pairs = list(itertools.combinations(range(n), 2))
    return round(sum(cos(vecs[i], vecs[j]) for i, j in pairs) / len(pairs), 4)


def persona_input(pid: str) -> str:
    d = persona_dir(pid)
    return (d / "cv.md").read_text() + "\n".join(p.read_text() for p in sorted((d / "memory").glob("*.md")))


def main(run_dirs: list[str]) -> None:
    runs = [Path(r) for r in run_dirs]
    cfgs = [json.loads((r / "config.json").read_text()) for r in runs]
    ext = [json.loads((r / "materials" / "extracted.json").read_text()) for r in runs]
    inputs = tfidf_cos([persona_input(c["persona"]) for c in cfgs])
    out = {"runs": [r.name for r in runs], "input_similarity": inputs}
    for key in ("REV", "M3"):
        s = tfidf_cos([e.get(key, "") for e in ext])
        out[f"output_similarity_{key}"] = s
        out[f"homogenization_ratio_{key}"] = round(s / inputs, 3) if inputs else None
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
