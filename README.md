# Thesis Research Kit

Write down the questions an investment thesis has to answer. Get back the pages that answer them,
the key lines from each, and every number found, marked by how many different websites back it up.

I use this before writing any thesis. My quantum technologies research was built this way.

## Result

| Theme | Brief | Output |
|---|---|---|
| Quantum technologies in India | [brief.yaml](examples/quantum-technologies/brief.yaml) | [research-excerpt.md](examples/quantum-technologies/research-excerpt.md): the policy and money backdrop, market sizes counted bottom up, and the two startups I picked, with 59 linked sources |

The excerpt covers the method and my two picks. The full document assesses seven startups and stays private.

## How it works

```
brief.yaml  ->  1. search (Exa)  ->  2. read in full (Firecrawl)  ->  3. pack
(the questions      every query,          the top pages for each           evidence.md
 the thesis         plus startups         question, PDFs and               numbers.csv
 must answer)       similar to the        tenders included                 sources.csv
                    ones I name
```

1. **Brief first.** I write the questions before any search: why now, how big, who pays, what is hard,
   who is building it, what kills it. Writing them down first keeps the research from drifting.
2. **Search.** Exa runs every query and also looks for startups similar to the ones I name.
3. **Read.** Firecrawl reads the best pages in full, including government PDFs and tenders.
4. **Pack.** `evidence.md` groups the pages under each question. `numbers.csv` lists every figure
   (money, %, GWh, km, qubits) with the number of websites that state it, and whether they state it
   in similar words. The same number in unrelated sentences does not count as a second source.
   Anything on one website only gets checked again before I use it.

The script has no AI model in it on purpose: the pack only shows what the pages say. The judgment,
the market sizing and the writing come after, in Claude, following
[the research skill](thesis-research/SKILL.md). That is also how the quantum research
above was written, with Exa and Firecrawl connected to Claude.

## Tools

| Tool | Used for |
|---|---|
| [Claude](https://claude.ai) | Building this kit, then the analysis and writing on top of the pack |
| [Exa](https://exa.ai) | Search, including "find startups like this one" |
| [Firecrawl](https://firecrawl.dev) | Reading full pages and PDFs as clean text |

## Run it

```
pip install -r requirements.txt
cp .env.example .env        # add EXA_API_KEY and FIRECRAWL_API_KEY
python run.py --brief briefs/quantum-technologies.yaml
python -m pytest -q         # offline checks, no keys needed
```

Raw responses are saved in `runs/<name>/raw/`, so a second run costs nothing.

## Code

```
run.py               one command: brief in, pack out
research/brief.py    loads and checks the brief (unique ids, 6 queries or fewer per question)
research/sources.py  Exa search and Firecrawl scrape, with every response cached
research/pack.py     evidence.md, numbers.csv (with the cross-check), sources.csv
```

## Next

- Tenders and government orders (GeM, CPPP, SECI) as their own source, since a tender is the clearest sign a buyer is ready.
- Research papers through Firecrawl's paper search, to judge how ready a technology really is.
- Patent and company registry lookups, to check patent counts and headquarters automatically.
- Weekly alerts on a live thesis (new rounds, new tenders) with Exa Monitors.
