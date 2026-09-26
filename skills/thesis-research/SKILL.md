---
name: thesis-research
description: This skill should be used when the user asks to "research a thesis", "build an investment thesis", "size a market bottom up", "find startups in <sector>", or check whether a sector or startup is investable. Uses Exa and Firecrawl and writes a sourced, checkable document.
---

# Thesis research

The workflow I use with Claude, with Exa and Firecrawl connected as MCP tools.
`run.py` in this repo does steps 1 and 2 on its own. The rest happens in the
conversation, with the pack open.

## 0. Brief first, search second

Write down the questions the thesis has to answer before any search. Every
thesis I write answers the same six:

1. **Why now?** A dated event that changed demand: a rule, a deadline, a price drop, a tender.
2. **How big?** Market size counted bottom up (buyers x price), never a report's headline number.
3. **Who pays, and why would they switch?**
4. **What is the hard part?** The technical problem that stopped earlier companies.
5. **Who is building it?** Startups that pass the filters (HQ country, stage, last round).
6. **What kills it?** Risks by type: team, technology, market, regulation, money.

Ask the user for the fund's filters (geography, stage, cheque size) if they
are not given. They decide which companies count.

## 1. Find with Exa

- One search per question, phrased the way the answer would be written.
- For companies: search the category, then "startups similar to <best one>".
- Keep the date window tight when the question is about "now".

## 2. Read in full with Firecrawl

Exa excerpts are for finding. Anything that becomes a number in the document
comes from a page read in full: the government PDF, the tender, the funding
announcement, the company's own site. Firecrawl reads PDFs too.

## 3. Check every number

- Every figure gets a source tag like [S4] that points to a link in the Sources list.
- A number needs two independent sources, or one primary source (the regulator, the company, the paper).
- Claims only the company makes are marked "company says".
- When two sources disagree, show both. (Example from the quantum run: one page said 5 patents, another said 14. Both went in, flagged.)
- Check headquarters in a company registry or funding release. One company in the quantum run looked Indian but was headquartered in New York.

`numbers.csv` from `run.py` does the first pass: it counts how many different
websites state each figure and marks the single-source ones.

## 4. Size the market bottom up

Buyers x price, with each input from an official list or a public price, and
the assumption written next to the number. Then test it against the fund:
for one winner to return the fund, what exit does it need, and can this
market support that?

## 5. Due diligence and live signals

- For every shortlisted company, run the `due-diligence` skill: registry, founders, patents, research papers, tenders and government orders, funding history, financials, traction, courts, licences, competition, adverse media.
- For the sector, run the `funding-radar` skill to see who raised in the last weeks, and offer to make it a weekly alert.

## 6. Write each company the same way

What it does (in plain words) / why now / team / proof so far / business
model and buyers / market size / risks table / main risk / fund fit / verdict /
due-diligence findings / open questions.

The open questions become the founder question bank for the first call.

## Style

- Explain every technical term the first time, in one plain line. Keep a glossary at the top.
- Everyday words. No em dashes.
- Lead with the answer: a bottom-line table before the detail.
