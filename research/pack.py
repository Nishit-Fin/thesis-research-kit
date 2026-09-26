"""Turn saved search results and pages into a research pack.

Outputs (in runs/<name>/):
  evidence.md   every question, the pages that answer it, and the key excerpts
  numbers.csv   every figure found (money, %, GWh, km, qubits...), how many
                different websites state it, and whether those websites say it
                in similar words. One website = find a second source.
  sources.csv   every page used, with its date

No LLM here on purpose: the pack only shows what the pages say. The writing
and judgment happen after, with the pack open next to you.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Dict, List
from urllib.parse import urlparse

NUM = re.compile(
    r"(?P<cur>[₹$€£])?\s?(?P<num>\d{1,3}(?:,\d{2,3})+(?:\.\d+)?|\d+(?:\.\d+)?)\s?"
    r"(?P<unit>%|per ?cent\b|km\b|GWh\b|MWh\b|kWh\b|GW\b|MW\b|kW\b|qubits?\b|crore\b|cr\b|lakh\b|"
    r"million\b|billion\b|mn\b|bn\b|kg\b|tonnes?\b|[MBK]\b)?",
    re.IGNORECASE,
)
UNIT_ALIASES = {"percent": "%", "per cent": "%", "cr": "crore", "mn": "million", "bn": "billion", "qubit": "qubits",
                "m": "million", "b": "billion", "k": "thousand"}
SHORT_MONEY = {"m", "b", "k"}  # $2M, $1.5B, $250K: only counted after a currency sign
POWER_UNITS = {"gwh": "GWh", "mwh": "MWh", "kwh": "kWh", "gw": "GW", "mw": "MW", "kw": "kW"}


def norm_unit(unit: str) -> str:
    low = unit.lower()
    return UNIT_ALIASES.get(low) or POWER_UNITS.get(low) or low


def domain(url: str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")


def sentences(text: str) -> List[str]:
    text = re.sub(r"\s+", " ", text or "")
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z₹$])", text) if 20 < len(s.strip()) < 400]


def figures(sentence: str):
    for m in NUM.finditer(sentence):
        cur, unit = m.group("cur") or "", (m.group("unit") or "").strip()
        if not cur and not unit:
            continue  # a bare number (often a year or a page number) is not a figure
        if unit.lower() in SHORT_MONEY and not cur:
            continue  # "5 m" is more likely metres than millions
        unit = norm_unit(unit)
        value = m.group("num").replace(",", "")
        yield f"{cur}{value} {unit}".strip(), sentence


def build_pack(brief, results: Dict[str, List[dict]], pages: Dict[str, dict], out: Path) -> dict:
    """results: question id -> list of Exa results. pages: url -> scraped page."""
    out.mkdir(parents=True, exist_ok=True)
    fig_seen: Dict[str, dict] = defaultdict(lambda: {"domains": set(), "sentence": "", "url": "", "questions": set(),
                                                    "by_domain": {}})
    source_rows = []
    logged = set()

    for qid, rows in results.items():
        for r in rows:
            url = r["url"]
            text = " ".join(r.get("highlights") or [])
            if url in pages:
                text += " " + pages[url].get("markdown", "")
            for fig, sent in figures_in(text):
                f = fig_seen[fig]
                f["domains"].add(domain(url))
                f["by_domain"].setdefault(domain(url), sent)
                f["questions"].add(qid)
                if not f["sentence"]:
                    f["sentence"], f["url"] = sent, url
            if (qid, url) in logged:
                continue
            logged.add((qid, url))
            source_rows.append([qid, r.get("title", ""), url, domain(url), (r.get("publishedDate") or "")[:10],
                                "yes" if url in pages else "no"])

    with open(out / "sources.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["question", "title", "url", "website", "published", "full_page_read"])
        w.writerows(source_rows)

    fig_rows = sorted(fig_seen.items(), key=lambda kv: (-len(kv[1]["domains"]), kv[0]))
    with open(out / "numbers.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["figure", "websites_stating_it", "websites_in_similar_words", "status", "websites",
                    "questions", "example_sentence", "example_url"])
        for fig, f in fig_rows:
            n, similar = len(f["domains"]), agreeing_sites(f["by_domain"])
            w.writerow([fig, n, similar, status(n, similar), "; ".join(sorted(f["domains"])),
                        "; ".join(sorted(f["questions"])), f["sentence"], f["url"]])

    write_evidence(brief, results, pages, fig_rows, out / "evidence.md")
    return {"sources": len(source_rows), "figures": len(fig_rows),
            "confirmed": sum(1 for _, f in fig_rows if agreeing_sites(f["by_domain"]) >= 2)}


STOP = set("""the and for with that this from have has had was were are been its their than into over
under about after before also more most such which while when where what will would could should
said says per year years india indian company startup""".split())


def _words(sentence: str) -> set:
    return {w for w in re.findall(r"[a-z]{4,}", sentence.lower()) if w not in STOP}


def agreeing_sites(by_domain: Dict[str, str]) -> int:
    """How many websites state the figure in similar words (2+ shared content words with
    another website's sentence). The same number in unrelated sentences does not count:
    '10%' about tariffs and '10%' about efficiency are not the same fact."""
    items = list(by_domain.items())
    agree = set()
    for i, (d1, s1) in enumerate(items):
        for d2, s2 in items[i + 1:]:
            if len(_words(s1) & _words(s2)) >= 2:
                agree.update({d1, d2})
    return len(agree)


def status(n_sites: int, similar: int) -> str:
    if n_sites < 2:
        return "one site only: find a second source"
    if similar >= 2:
        return "2+ sites in similar words: likely the same fact"
    return "same number on 2+ sites, different context: check by hand"


def figures_in(text: str):
    for s in sentences(text):
        yield from figures(s)


def write_evidence(brief, results, pages, fig_rows, path: Path) -> None:
    asks = {q.id: q.ask for q in brief.questions}
    lines = [f"# Evidence pack: {brief.theme}", "",
             f"Built {date.today().isoformat()}. Geography: {brief.geography or 'any'}. "
             f"Pages published since: {brief.since or 'any date'}.", ""]

    thin = [qid for qid, rows in results.items() if len({domain(r['url']) for r in rows}) < 3]
    if thin:
        lines += ["## Check before you write", "",
                  "These questions have fewer than 3 different websites behind them. Search again or find a primary source:", ""]
        lines += [f"- {asks.get(q, q)}" for q in thin] + [""]

    for qid, rows in results.items():
        lines += [f"## {asks.get(qid, qid)}", ""]
        seen = set()
        for r in rows:
            if r["url"] in seen:
                continue
            seen.add(r["url"])
            date_s = (r.get("publishedDate") or "")[:10] or "no date"
            tag = " (full page read)" if r["url"] in pages else ""
            lines.append(f"- **{r.get('title') or domain(r['url'])}**, {domain(r['url'])}, {date_s}{tag}  ")
            lines.append(f"  {r['url']}")
            for h in (r.get("highlights") or [])[:2]:
                h = re.sub(r"\s+", " ", h).strip()
                lines.append(f"  > {h[:320]}{'...' if len(h) > 320 else ''}")
        q_figs = [(fig, f) for fig, f in fig_rows if qid in f["questions"]][:8]
        if q_figs:
            lines += ["", "Figures found for this question:", ""]
            lines += [f"- {fig}: {status(len(f['domains']), agreeing_sites(f['by_domain']))}" for fig, f in q_figs]
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
