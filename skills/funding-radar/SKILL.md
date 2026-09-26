---
name: funding-radar
description: This skill should be used when the user asks for "funding news", "who raised this week", "weekly funding alerts", "funding radar", "latest rounds in <sector>", or wants to set up a weekly digest of startup funding rounds from pre-seed to Series C. Uses Exa to find announcements and Firecrawl to read them.
---

# Funding Radar

A weekly digest of startup funding rounds from pre-seed to Series C, filtered to
the user's geography and sectors, with every round traced to its announcement.

## Settings (ask once, then reuse)

Ask only for what is missing, in one message:

1. **Geography.** Default: India-headquartered startups.
2. **Sectors.** The user's thesis areas (for example: energy storage, quantum, photonics). "All sectors" is allowed.
3. **Window.** Default: the last 7 days.
4. **Stages.** Default: pre-seed, seed, pre-Series A, Series A, Series B, Series C.

If a weekly scheduled task is being created, put these settings into its prompt so every run uses them.

## Steps

1. **Search with Exa.** For every stage x sector pair, run one search phrased the way an announcement is written, for example `India <sector> startup raises seed round`. Keep the publication window to the chosen dates. Add one broad search per stage without a sector, to catch rounds outside the watchlist. Delegate the sweep to the `funding-scout` agent when many searches are needed.
2. **Keep only announcements.** Drop opinion pieces, listicles and rounds older than the window.
3. **Read each announcement with Firecrawl** and pull: company, city, stage, amount (in the original currency, plus USD), lead investor, other investors, date announced, what the company makes (one plain line), and use of funds if stated.
4. **Merge duplicates.** The same round reported by several outlets is one row, with every source kept.
5. **Check the stage label.** Outlets mislabel stages. If the amount looks wrong for the label (for example a "seed" above $10M), keep the reported label and add "check stage".
6. **Flag thesis fits.** Mark rounds in the user's sectors, and rounds led by investors the user tracks.

## Output

A short digest, newest first:

| Date | Company | What it makes | Stage | Amount | Lead | Thesis fit | Sources |

Then three lines at most: patterns worth noting (a busy sector, a repeat investor, an unusual round size). Offer to run `due-diligence` on any company in the table.

## Weekly alerts

When the user wants this every week, create a scheduled task (for example Monday 9:00 local time) whose prompt runs this skill with the saved settings and sends the digest. Say in one line which day and time it runs.

## Rules

- Every row links to at least one announcement. No source, no row.
- Amounts are as reported. Never estimate a missing amount; write "undisclosed".
- Plain words. No em dashes.

For query patterns and trusted sources, see `references/queries.md`.
