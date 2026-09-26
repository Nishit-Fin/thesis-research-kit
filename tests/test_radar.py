"""Offline checks for the funding radar: python -m pytest -q"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research.radar import build_queries, merge_hits, stage_in, write_digest  # noqa: E402


def test_every_stage_from_pre_seed_to_series_c_is_searched():
    qs = build_queries("India", ["quantum"])
    stages = {q["stage"] for q in qs}
    assert stages == {"pre-seed", "seed", "pre-Series A", "Series A", "Series B", "Series C"}
    assert len(qs) == 12  # one broad and one sector query per stage


def test_stage_labels_are_not_confused():
    assert stage_in("Startup raises pre-Series A round") == "pre-Series A"
    assert stage_in("Startup raises $12M Series A") == "Series A"
    assert stage_in("Pre-seed round led by Seafund") == "pre-seed"
    assert stage_in("Seed funding for storage startup") == "seed"


def test_old_articles_drop_and_duplicates_merge(tmp_path):
    hits = [
        {"url": "https://inc42.com/a", "title": "X raises Series A", "publishedDate": "2026-09-25", "sector": "quantum"},
        {"url": "https://inc42.com/a", "title": "X raises Series A", "publishedDate": "2026-09-25", "sector": ""},
        {"url": "https://entrackr.com/old", "title": "Y raises seed", "publishedDate": "2026-08-01", "sector": ""},
    ]
    rows = merge_hits(hits, since="2026-09-20")
    assert [r["url"] for r in rows] == ["https://inc42.com/a"]
    assert rows[0]["stage"] == "Series A" and rows[0]["sectors"] == {"quantum"}
    write_digest(rows, {}, "India", "2026-09-20", tmp_path / "digest.md")
    text = (tmp_path / "digest.md").read_text(encoding="utf-8")
    assert "undisclosed" in text and "inc42.com" in text
