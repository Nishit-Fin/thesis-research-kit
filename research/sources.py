"""Talk to Exa (search) and Firecrawl (full page as markdown).

Every raw response is saved under runs/<name>/raw/, and a saved response is
reused on the next run. That keeps runs cheap and lets you rebuild the pack
without searching again.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import List, Optional

import requests

EXA_SEARCH = "https://api.exa.ai/search"
FIRECRAWL_SCRAPE = "https://api.firecrawl.dev/v2/scrape"


def _key(*parts: str) -> str:
    return hashlib.sha1("|".join(parts).encode()).hexdigest()[:16]


def _cached(path: Path, fetch):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    data = fetch()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return data


def exa_search(raw_dir: Path, query: str, since: Optional[str] = None, domains: Optional[List[str]] = None) -> dict:
    """One Exa search with highlights (short, relevant excerpts from each page)."""
    body = {"query": query, "type": "auto", "contents": {"highlights": True}}
    if since:
        body["startPublishedDate"] = since
    if domains:
        body["includeDomains"] = domains

    def fetch():
        key = os.environ.get("EXA_API_KEY")
        if not key:
            raise RuntimeError("EXA_API_KEY is missing. Add it to .env (see .env.example).")
        r = requests.post(EXA_SEARCH, headers={"x-api-key": key}, json=body, timeout=120)
        if r.status_code != 200:
            raise RuntimeError(f"Exa returned {r.status_code} for '{query}': {r.text[:300]}")
        return {"query": query, "response": r.json()}

    return _cached(raw_dir / "exa" / f"{_key(json.dumps(body, sort_keys=True))}.json", fetch)


def firecrawl_scrape(raw_dir: Path, url: str) -> Optional[dict]:
    """Full page as clean markdown. Works on PDFs too (policy papers, tenders)."""

    def fetch():
        key = os.environ.get("FIRECRAWL_API_KEY")
        if not key:
            raise RuntimeError("FIRECRAWL_API_KEY is missing. Add it to .env (see .env.example).")
        r = requests.post(
            FIRECRAWL_SCRAPE,
            headers={"Authorization": f"Bearer {key}"},
            json={"url": url, "formats": ["markdown"], "onlyMainContent": True},
            timeout=180,
        )
        if r.status_code != 200:
            return {"url": url, "error": f"{r.status_code}: {r.text[:200]}"}
        data = r.json().get("data", {})
        return {"url": url, "markdown": data.get("markdown", ""), "metadata": data.get("metadata", {})}

    page = _cached(raw_dir / "pages" / f"{_key(url)}.json", fetch)
    return None if page.get("error") else page
