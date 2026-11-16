"""Phrase lexicons and n-gram overlap. Deterministic, no API calls."""
from __future__ import annotations

import re

HOLLOW = [
    r"\bpassionate\b", r"\bdeeply\b", r"\bunique blend\b", r"\bat the intersection of\b", r"\bleverag(e|ing)\b",
    r"\bcutting[- ]edge\b", r"\balign(s|ed)? (closely|deeply|perfectly)\b", r"\bclosely aligned\b",
    r"\bexcited to\b", r"\bthrive\b", r"\bimmediate impact\b", r"\bdynamic\b", r"\binnovative\b",
    r"\binvaluable\b", r"\bresonates?\b", r"\bprofound(ly)?\b", r"\beager to contribute\b", r"\bperfect fit\b",
    r"\bstrong fit\b", r"\bi am confident that\b", r"\bholistic\b", r"\btransformative\b", r"\bseamless(ly)?\b",
    r"\bspark(ed)? my (interest|passion)\b", r"\bfuel(s|ed)? my\b", r"\bunwavering\b", r"\bgroundbreaking\b",
]

INDUSTRY = [
    r"\bstakeholders?\b", r"\bcross-functional\b", r"\bdeliverables?\b", r"\bactionable insights?\b",
    r"\bdrive (business|product) (decisions|outcomes)\b", r"\bROI\b", r"\bKPIs?\b", r"\bfast-paced\b",
    r"\bdata-driven (solutions|decisions|approach)\b", r"\bbusiness (value|impact|outcomes)\b",
    r"\bimmediate impact\b", r"\bresults-(oriented|driven)\b", r"\bhit the ground running\b",
    r"\bproduct (roadmap|strategy)\b", r"\bcustomer outcomes\b", r"\bin production\b", r"\bdeployed\b",
    r"\b(drove|driving) an? \d", r"\bcontribute to (your|the) (team|mission)\b",
]


def count(patterns: list[str], text: str) -> int:
    return sum(len(re.findall(p, text, flags=re.IGNORECASE)) for p in patterns)


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def rate_per_100(patterns: list[str], text: str) -> float:
    n = len(words(text))
    return round(100 * count(patterns, text) / n, 3) if n else 0.0


def ngrams(text: str, n: int = 4) -> set[tuple[str, ...]]:
    w = words(text)
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def containment(target: str, source: str, exclude: str = "", n: int = 4) -> float:
    """Share of target's n-grams that also appear in source, ignoring n-grams that come from `exclude` (e.g., the CV)."""
    t = ngrams(target, n) - ngrams(exclude, n)
    if not t:
        return 0.0
    return round(len(t & ngrams(source, n)) / len(t), 4)
