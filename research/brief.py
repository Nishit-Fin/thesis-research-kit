"""Load and check a research brief (a small YAML file you write before any search)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

import yaml


@dataclass
class Question:
    id: str
    ask: str
    queries: List[str]
    domains: List[str] = field(default_factory=list)  # optional hard allowlist, only if you chose it


@dataclass
class Brief:
    theme: str
    geography: str
    since: Optional[str]
    questions: List[Question]
    seed_companies: List[str]
    scrape_top: int = 3


def load_brief(path: Path) -> Brief:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    qs = [
        Question(
            id=q["id"],
            ask=q["ask"],
            queries=list(q.get("queries") or [q["ask"]]),
            domains=list(q.get("domains") or []),
        )
        for q in raw.get("questions", [])
    ]
    brief = Brief(
        theme=raw["theme"],
        geography=raw.get("geography", ""),
        since=raw.get("since"),
        questions=qs,
        seed_companies=list(raw.get("seed_companies") or []),
        scrape_top=int(raw.get("scrape_top", 3)),
    )
    problems = check_brief(brief)
    if problems:
        raise ValueError("Brief has problems:\n  " + "\n  ".join(problems))
    return brief


def check_brief(brief: Brief) -> List[str]:
    problems = []
    if not brief.questions:
        problems.append("add at least one question")
    ids = [q.id for q in brief.questions]
    if len(ids) != len(set(ids)):
        problems.append("question ids must be unique")
    for q in brief.questions:
        if len(q.queries) > 6:
            problems.append(f"'{q.id}' has {len(q.queries)} queries; keep it to 6 or fewer so the question stays narrow")
    return problems
