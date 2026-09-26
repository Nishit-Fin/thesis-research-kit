"""Offline checks for the research pack. No API keys needed: python -m pytest -q"""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from research.brief import Brief, Question  # noqa: E402
from research.pack import agreeing_sites, build_pack, figures_in  # noqa: E402


def test_figures_are_read_with_units():
    found = {fig for fig, _ in figures_in(
        "The payload shared keys across 12,900 km in one pass. Pramatra raised $2M in its pre-seed round. "
        "India tendered 102 GWh of storage in 2025. The mission has a budget of ₹6,003.65 crore.")}
    assert {"12900 km", "$2 million", "102 GWh", "₹6003.65 crore"} <= found
    assert not any(f.startswith("2025") for f in found)  # a year alone is not a figure


def test_same_number_needs_similar_words_to_count():
    same_fact = {
        "nature.com": "A 23 kg payload shared keys between China and South Africa, 12,900 km apart.",
        "thehindu.com": "The satellite shared keys between China and South Africa over 12,900 km.",
    }
    unrelated = {
        "a.com": "Bids fell 10% in the latest storage auction.",
        "b.com": "Round-trip efficiency improved by 10% this quarter.",
    }
    assert agreeing_sites(same_fact) == 2
    assert agreeing_sites(unrelated) == 0


def test_pack_marks_single_source_figures(tmp_path):
    brief = Brief(theme="Test", geography="India", since=None, scrape_top=1,
                  questions=[Question(id="why-now", ask="Why now?", queries=["q"])], seed_companies=[])
    results = {"why-now": [
        {"url": "https://dst.gov.in/roadmap", "title": "DST roadmap", "publishedDate": "2026-05-10",
         "highlights": ["Critical sectors must be quantum-safe by December 2029, and 5 sectors are named."]},
        {"url": "https://example-news.com/story", "title": "News", "publishedDate": "2026-05-11",
         "highlights": ["India tendered 102 GWh of battery storage in 2025, the ministry said."]},
    ]}
    stats = build_pack(brief, results, {}, tmp_path)
    rows = list(csv.DictReader(open(tmp_path / "numbers.csv", encoding="utf-8")))
    gwh = next(r for r in rows if r["figure"] == "102 GWh")
    assert gwh["status"].startswith("one site only")
    assert stats["sources"] == 2
    assert (tmp_path / "evidence.md").read_text(encoding="utf-8").startswith("# Evidence pack: Test")
