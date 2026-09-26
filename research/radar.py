"""Funding radar: this week's rounds from pre-seed to Series C, one row per round."""

from __future__ import annotations

import re
from datetime import date
from typing import Dict, List
from urllib.parse import urlparse

STAGES = ["pre-seed", "seed", "pre-Series A", "Series A", "Series B", "Series C"]

_STAGE_PATTERNS = [  # most specific first, so "pre-Series A" is not read as "Series A"
    ("pre-Series A", r"pre[- ]?series[- ]?a\b"),
    ("pre-seed", r"pre[- ]?seed"),
    ("Series C", r"series[- ]?c\b"),
    ("Series B", r"series[- ]?b\b"),
    ("Series A", r"series[- ]?a\b"),
    ("seed", r"\bseed\b"),
]


def build_queries(geography: str, sectors: List[str], stages: List[str] = STAGES) -> List[dict]:
    queries = []
    for stage in stages:
        queries.append({"stage": stage, "sector": "", "query": f"{geography} startup raises {stage} funding round"})
        for sector in sectors:
            queries.append({"stage": stage, "sector": sector,
                            "query": f"{geography} {sector} startup raises {stage} funding round"})
    return queries


def stage_in(text: str) -> str:
    low = (text or "").lower()
    for label, pattern in _STAGE_PATTERNS:
        if re.search(pattern, low):
            return label
    return ""


def merge_hits(hits: List[dict], since: str) -> List[dict]:
    """One row per article URL inside the window, tagged with the stage the text names."""
    rows: Dict[str, dict] = {}
    for h in hits:
        published = (h.get("publishedDate") or "")[:10]
        if published and published < since:
            continue
        url = h["url"]
        row = rows.setdefault(url, {"url": url, "title": h.get("title", ""), "published": published,
                                    "site": urlparse(url).netloc.removeprefix("www."),
                                    "sectors": set(), "stage": ""})
        if h.get("sector"):
            row["sectors"].add(h["sector"])
        row["stage"] = row["stage"] or stage_in(row["title"] + " " + " ".join(h.get("highlights") or []))
    return sorted(rows.values(), key=lambda r: r["published"], reverse=True)


def write_digest(rows: List[dict], rounds: Dict[str, dict], geography: str, since: str, path) -> None:
    lines = [f"# Funding radar: {geography}, since {since}", "",
             f"Built {date.today().isoformat()}. Amounts as reported; 'undisclosed' when the page does not say.", "",
             "| Published | Company | Stage | Amount | Lead | Sectors | Source |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        d = rounds.get(r["url"], {})
        company = d.get("company") or r["title"][:60]
        stage = d.get("stage") or r["stage"] or "unclear"
        amount = d.get("amount") or "undisclosed"
        lead = ", ".join(d.get("lead_investors") or []) or "not stated"
        sectors = ", ".join(sorted(r["sectors"])) or "other"
        lines.append(f"| {r['published'] or 'no date'} | {company} | {stage} | {amount} | {lead} | {sectors} | "
                     f"[{r['site']}]({r['url']}) |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
