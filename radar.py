"""Weekly funding radar.

    python radar.py --geography India --sectors "energy storage" quantum photonics
    python radar.py --days 14 --no-read      # search only, skip reading each article

Searches Exa for rounds from pre-seed to Series C in the window, reads each
announcement with Firecrawl for the round details, and writes
runs/radar-<date>/digest.md. Schedule it weekly (cron, Task Scheduler, or a
Claude scheduled task that runs the funding-radar skill).
"""

from __future__ import annotations

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from pathlib import Path

from dotenv import load_dotenv

from research.radar import build_queries, merge_hits, write_digest
from research.sources import exa_search, firecrawl_round


def main() -> int:
    load_dotenv()
    ap = argparse.ArgumentParser(description="This week's startup funding rounds, pre-seed to Series C.")
    ap.add_argument("--geography", default="India")
    ap.add_argument("--sectors", nargs="*", default=[])
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--no-read", action="store_true", help="skip reading each announcement with Firecrawl")
    args = ap.parse_args()

    since = (date.today() - timedelta(days=args.days)).isoformat()
    out = Path("runs") / f"radar-{date.today().isoformat()}"
    raw = out / "raw"
    queries = build_queries(args.geography, args.sectors)
    print(f"Searching {len(queries)} queries since {since}...")
    with ThreadPoolExecutor(max_workers=5) as pool:
        responses = list(pool.map(lambda q: exa_search(raw, q["query"], since), queries))

    hits = []
    for q, resp in zip(queries, responses):
        for h in resp["response"].get("results", []):
            hits.append({**h, "sector": q["sector"]})
    rows = merge_hits(hits, since)

    rounds = {}
    if not args.no_read and rows:
        print(f"Reading {len(rows)} announcements...")
        with ThreadPoolExecutor(max_workers=4) as pool:
            for page in pool.map(lambda r: firecrawl_round(raw, r["url"]), rows):
                if page:
                    rounds[page["url"]] = page["round"]

    out.mkdir(parents=True, exist_ok=True)
    write_digest(rows, rounds, args.geography, since, out / "digest.md")
    print(f"{len(rows)} articles. Open {out / 'digest.md'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
