"""Thesis Research Kit.

    python run.py --brief briefs/quantum-technologies.yaml

Reads a short brief (your theme and the questions the thesis must answer),
searches each question with Exa, reads the best pages in full with Firecrawl,
and writes a research pack to runs/<brief name>/.
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from dotenv import load_dotenv

from research.brief import load_brief
from research.pack import build_pack
from research.sources import exa_search, firecrawl_scrape


def main() -> int:
    load_dotenv()
    ap = argparse.ArgumentParser(description="Build a research pack for an investment thesis.")
    ap.add_argument("--brief", required=True, type=Path)
    ap.add_argument("--out", type=Path, help="run folder (default: runs/<brief name>)")
    ap.add_argument("--no-scrape", action="store_true", help="search only, skip reading full pages")
    args = ap.parse_args()

    brief = load_brief(args.brief)
    out = args.out or Path("runs") / args.brief.stem
    raw = out / "raw"

    # 1. Search: every query of every question, plus a lookalike search per seed company
    jobs = [(q.id, query, q.domains) for q in brief.questions for query in q.queries]
    for name in brief.seed_companies:
        jobs.append((f"seed:{name}", f"{name} startup {brief.geography}".strip(), []))
        jobs.append((f"seed:{name}", f"startups similar to {name} in {brief.geography}".strip(), []))
    print(f"Searching {len(jobs)} queries for '{brief.theme}'...")

    with ThreadPoolExecutor(max_workers=5) as pool:
        responses = list(pool.map(lambda j: exa_search(raw, j[1], brief.since, j[2]), jobs))

    results = {}
    for (qid, _, _), resp in zip(jobs, responses):
        results.setdefault(qid, []).extend(resp["response"].get("results", []))

    # 2. Read the top pages of each question in full
    pages = {}
    if not args.no_scrape:
        urls = []
        for qid, rows in results.items():
            if qid.startswith("seed:"):
                continue
            seen = []
            for r in rows:
                if r["url"] not in seen:
                    seen.append(r["url"])
            urls += seen[: brief.scrape_top]
        urls = list(dict.fromkeys(urls))
        print(f"Reading {len(urls)} pages in full...")
        with ThreadPoolExecutor(max_workers=4) as pool:
            for page in pool.map(lambda u: firecrawl_scrape(raw, u), urls):
                if page:
                    pages[page["url"]] = page

    # 3. Pack
    stats = build_pack(brief, results, pages, out)
    print(f"Done. {stats['sources']} sources, {stats['figures']} figures, "
          f"{stats['confirmed']} stated by 2+ websites in similar words.")
    print(f"Open {out / 'evidence.md'} and {out / 'numbers.csv'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
