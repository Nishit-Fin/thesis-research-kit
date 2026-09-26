# Quantum technologies in India: two investable startups (Sep 2026)

An excerpt from my quantum research: the method, the policy and money backdrop, the market sizing, and the two startups I picked. The full document assesses seven Indian quantum startups. Built with Claude, Exa (search) and Firecrawl (full pages and PDFs), from the brief in [brief.yaml](brief.yaml).

## How to read this

- Every fact carries a source tag like [S5] or [F2]. The full list with links is in the Sources section at the end. "Company says" marks a claim no outside party has checked. "Not verified" means I could not confirm it.
- Market sizes (TAM) are calculated bottom up: number of buyers × what each one pays. Buyer counts come from government or official lists. Prices come from public price lists or awarded contracts. Where I had to assume something, the assumption sits right next to the number.
- The "big enough?" bar: Kalaari is reported to be planning a ₹500 to 600 cr deeptech fund [S5]. For one winner to return that fund at about 10% ownership, it must exit near $500M. At 5 to 10 times revenue, that needs $50 to 100M of annual revenue. At a 10 to 20% share, the market must be at least about $250M a year (about ₹2,400 cr). Below that, the market is not big enough on its own.
- Exchange rates: ₹95.73 per US$ (RBI reference rate, 23 Sep 2026); ₹109.94 per € and ₹128.17 per £ (RBI reference rates, 6 Aug 2026) [S38].

**Plain-word glossary**
- QKD (quantum key distribution): sends encryption keys over light, so any eavesdropping disturbs the light and gets noticed. Needs fibre or a satellite link, and special hardware at both ends.
- PQC (post-quantum cryptography): new maths-based encryption that quantum computers cannot break. Pure software, runs on existing networks. NIST published the standards in 2024.
- QRNG: a device that makes truly random numbers from quantum effects, used to create strong keys.
- CBOM (cryptographic bill of materials): a full list of every place an organisation uses encryption. The first step of any migration.
- HSM (hardware security module): a locked box that stores and uses keys safely.
- PIC (photonic integrated circuit): optics shrunk onto a chip, the way electronics were shrunk onto silicon.
- SNSPD: a superconducting detector that can count single particles of light. Needs deep cooling.
- Ising machine: a special-purpose computer for optimisation problems (routing, scheduling, portfolios). It is not a general quantum computer.
- TRL (technology readiness level): 1 is an idea, 9 is proven in service. TRL 6 is a working prototype in a relevant environment; TRL 7 is a prototype in the real environment.

## The shared backdrop: why quantum, why now

**The policy clock (DST quantum-safe roadmap, final version, May 2026) [S1]**
- Critical sectors (defence, power, telecom, transport, banking and finance): foundations by Dec 2027, high-priority systems by Dec 2028, full move to quantum-safe encryption by Dec 2029.
- All other organisations: Dec 2028, Dec 2030 and Dec 2033.
- A CBOM becomes mandatory from FY2027-28. Tier-1 and Tier-2 testing and certification labs are due by Dec 2026.
- Public and private buyers are told to prefer Indian quantum-safe products, subject to technical fit.
- QKD is framed as a complement for specific high-assurance links. PQC is the default route for most organisations, including defence.

**The mission money**
- National Quantum Mission (NQM): ₹6,003.65 cr from 2023-24 to 2030-31. Targets include quantum computers with 50 to 1,000 physical qubits in 8 years on platforms including superconducting and photonic, satellite-based secure quantum communication over 2,000 km inside India, inter-city QKD over 2,000 km, and Indian-made single-photon sources and detectors [S2].
- Four thematic hubs: computing at IISc, communication at IIT Madras with C-DOT, sensing at IIT Bombay, materials and devices at IIT Delhi. 152 researchers from 43 institutions [S3].
- Eight startups backed so far, including QNu Labs and Quanastra [S4].
- RDI scheme: ₹1 lakh cr over six years for loans, equity and deeptech funds of funds. TDB and BIRAC are the first second-level fund managers; private fund managers (AIFs) applied in early 2026 [S6].

**The private money**
- Global: PsiQuantum raised $1B at a $7B valuation (Sep 2025) [S28]; Quantinuum $600M at a $10B pre-money value (Sep 2025) [S30]; Xanadu agreed a SPAC deal with about $500M of gross proceeds at a $3.0B pre-money value (Nov 2025) [S29]; SandboxAQ, the PQC leader, raised $450M+ at $5.75B (Apr 2025) [S31].
- India: QpiAI raised a $32M Series A at a $162M post-money value, co-led by the NQM (Jul 2025) [S33]; QNu Labs raised ₹200 cr plus ₹150 cr of RDI debt (Sep 2026) [Q1].
- Tracxn counts 95 quantum startups in India; only about 23 have raised money and only 2 (QNu, QpiAI) are at Series A or later [S11]. The field is thin, which cuts both ways: little competition for deals, but few proven exits.

**Where Kalaari stands**
- About $650M under management across four funds; cheques of $0.5M to $5M from pre-seed to Series A; average rounds it joins are about $2.2M at seed and $4.8M at Series A [S7][S8].
- In talks to launch a ₹500 to 600 cr deeptech fund. ET reports that several VCs plan to raise nearly half of such funds from the RDI pool [S5].
- No quantum company in the portfolio, so no conflicts. Useful neighbours: Digantara (space) and MeshDefend (enterprise data infrastructure, a $2.3M round led by Kalaari in Nov 2025) [S9].

**Market cross-check (sourced, not used in my calculations)**
McKinsey puts quantum communication at $1.2B in 2024, growing to $10.5 to 14.9B by 2035, and says quantum computing companies earned $650 to 750M in 2024 and over $1B in 2025 [S10].

## TAM building blocks (used in both company sections)

| Input | Value | Source |
|---|---|---|
| Scheduled commercial banks | 135 | RBI, 31 Mar 2025 [S12] |
| Insurers | about 53 | IRDAI [S13] |
| Stock exchanges, commodity exchanges, depositories | 3 + 4 + 2 = 9 (may overlap slightly) | SEBI, Feb 2024 [S14] |
| Power distribution companies (DISCOMs) | 59 (44 state, 15 private) | PFC, FY2023-24 [S15] |
| Operating central public sector enterprises | 272 | DPE survey 2023-24 [S16] |
| Companies listed on NSE | 2,720 | NSE, 31 Mar 2025 [S17] |
| World's largest companies | 2,000 (328 of them banks) | Forbes Global 2000, 2025 [S18] |
| NQM research base | 43 institutions, 152 researchers | DST [S3] |
| Indian Navy's first QKD delivery | 25 systems (2024) | DST [Q3] |
| Engineering simulation customers | 50,000+ customers; $2.54B revenue (Ansys, 2024) | Ansys 10-K [S34], press [S35] |
| PQC software price | Keyfactor Command £40,250 per licence a year (≈ ₹51.6 lakh) | UK G-Cloud [S19] |
| PQC software price | SandboxAQ AQtive Guard $250,000 a year (≈ ₹2.39 cr) | AWS Marketplace [S20] |
| PQC software price | QuSecure QuProtect $20,000 a month | AWS Marketplace [S21] |
| QKD system price | ID Quantique Clavis3 $270K to 540K (≈ ₹2.6 to 5.2 cr) | Distributor listing [S23] |
| SNSPD system price | €163,000 (≈ ₹1.79 cr), 2026 award to Single Quantum; NOK 1.56M, 2025 award (Univ. of Oslo) | Public tender awards [N7][N8] |
| QKD satellite mission | Eagle-1: about €130M to build, launch and operate; QEYSSat: C$30M design contract | [S24][S25] |
| Quantum computer sale | D-Wave booked about $12.6M of revenue for one system sold to Jülich (Q1 2025) | D-Wave [S27] |
| Total cost of a PQC migration | About $7.1B for US federal agencies, 2025 to 2035 | White House ONCD, Jul 2024 [S22] |

**The two shared pools**
- **India PQC software pool.** Tier 1, the critical sectors with a 2029 deadline: 135 banks + 53 insurers + 9 exchanges and depositories + 59 DISCOMs + 272 CPSEs = 528 organisations, paying ₹50 lakh a year each (range ₹25 lakh to 1 cr; set just under Keyfactor's UK list price and far under SandboxAQ's) = ₹264 cr a year (₹132 to 528 cr). Tier 2, other large companies with a 2033 deadline: 2,720 NSE-listed companies at ₹15 lakh a year (₹10 to 25 lakh) = ₹408 cr a year (₹272 to 680 cr). **Total ≈ ₹672 cr a year (range ₹404 to 1,208 cr, or $42 to 126M).** This counts software only. The full bill with hardware and services is several times larger: the US government alone expects to spend about $7.1B over 2025 to 2035 on its own migration [S22]. Global check: the 2,000 largest companies × $50K to 250K a year = $100 to 500M a year.
- **India QKD pool, to about 2032.** 20 links for the 2,000 km inter-city backbone (NQM target [S2], about 100 km per hop) + 100 to 300 defence links (4 to 12 times the Navy's first 25-system delivery [Q3]) + 50 to 100 high-assurance links for the most critical banks, exchanges, RBI, NPCI and grid control rooms = 170 to 420 links. At ₹1 to 2 cr per link (my assumption, set well below the only public price, the imported Clavis3 at ₹2.6 to 5.2 cr [S23]) = ₹170 to 840 cr in total, or **₹24 to 120 cr a year ($2.5 to 12.5M)** over 7 years.

## Pick 1: Pramatra Space

Bengaluru. Pramatra Space Technology Pvt Ltd, CIN U72900KA2022PTC167696, incorporated 9 Nov 2022 (the founders date the company to 2023) [P5]. Builds a photonic chip that makes entangled pairs of light for QKD, and puts it in two products: QimayaSat, a satellite payload, and Qimaya, a quantum-safe HSM for data centres [P6].

**Why invest now**
- Small satellites can now do QKD. China's Jinan-1 microsatellite, with a payload of about 23 kg and a portable ground station of about 100 kg, shared up to 1.07 million secure key bits in a single pass and linked China and South Africa, 12,900 km apart (Nature, 19 Mar 2025) [S26]. Fibre QKD tops out at roughly 100 to 150 km per hop, so long distances need satellites.
- India has a target and a budget: the NQM aims for satellite-based secure quantum communication over 2,000 km [S2]. Abroad, Europe's Eagle-1 QKD satellite cost about €130M to build, launch and operate [S24] and Canada paid C$30M just to design QEYSSat [S25]. A chip-based payload that is far cheaper widens the pool of countries that can afford one.
- The DST roadmap tells buyers to prefer Indian quantum-safe products [S1].
- Money is moving: the pre-seed closed on 25 May 2026 [P1], and the CEO says the next round will fund the commercial satellite launch and scale the ground systems (Jun 2026) [P8]. A seed round is coming.

**Team**
- Richa Hukumchand, founder and CEO: built air-defence systems at DRDO and earth-observation systems at Pixxel; HDFC Bank group's "Emerging Woman Founder 2025" [P9][P4].
- Vinay Hukumchand, co-founder and COO: commercial roles at Deloitte, AstraZeneca and DaVita [P9].
- Sheema Egbert, SVP Satellite and Systems [P2].
- Advisors on the website: Sharad Sanghi, Steve Suarez, Mani Thiru [P2]. If this is the Sharad Sanghi who founded Netmagic and now runs Neysa and chairs NTT Data India [P7], that is a heavyweight name, but his own profile does not mention Pramatra, so treat it as unconfirmed.
- Notable backers: Awais Ahmed, founder of Pixxel, as an angel [P1]; Techstars Space accelerator, 2024 batch [P10].
- Team of roughly 10 to 20 (LinkedIn company data) [P11].

**Proof so far**
- The PIC chip for entanglement-based QKD has been validated and tested at IIT Madras [P1].
- An in-orbit demo is booked with an Indian satellite bus maker on a rideshare planned for Q3 2027 (target TRL 6). The terrestrial product is due for critical-infrastructure sites by end-2026 (target TRL 7). Own QKD satellites are planned for Q3 or Q4 2028 (company says) [P6].
- Company says its chip-based payloads and HSMs have 4 to 10 times lower size, weight and power, 3 times lower cost and 3 times higher reliability than bulk-optic systems [P6]. Not independently verified.
- MoU with Infostellar (Tokyo) for ground-station services, Oct 2025 [P3]. Selected for NASSCOM Emerge 50 [P6].
- No named paying customer. Revenue is not disclosed; registry-based figures on data sites are tiny and their units are unclear, so I have not used them.

**Business model and who buys**
- QKD as a service: satellites beam keys to optical ground stations, which feed HSMs at data centres; customers pull keys through Pramatra's key management software [P1][P6]. It can also sell the payload and the HSM as hardware.
- Target buyers: commercial data centres, financial institutions and sovereign defence networks [P4]. In practice the first buyers will be governments, because every QKD satellite flying or planned today is government funded (Eagle-1, QEYSSat, SpeQtral-1, Jinan-1) [S24][S25][S26].

**Market size (calculated)**
- India: 2 to 6 small QKD satellites plus ground stations to meet the NQM's 2,000 km target × $10M to 30M each (my assumption: well below QEYSSat and Eagle-1, since Jinan-1 shows a 23 kg payload is enough and Pramatra claims 3 times lower cost) = **$20M to 180M in total (₹191 to 1,723 cr)** over about five years.
- Global: at least six national programmes are already public (China, ESA with SES, Canada, UK's SPOQC, Singapore, India) [S24][S25][S26]. Assume 10 to 20 sovereign buyers by 2035 × 2 to 6 satellites × $10M to 30M = $0.2B to 3.6B over ten years, or **$20M to 360M a year**.
- Ground side: the Qimaya HSM competes in the India QKD pool of ₹24 to 120 cr a year.
- **Big enough?** Borderline. India alone is small and lumpy. The venture case rests on selling low-cost payloads to many countries, which needs SCOMET export licences [S37].

**Risks (all types)**

| Type | Risk | Level |
|---|---|---|
| Technology | A photonic chip has to survive launch, radiation and heat cycles; flight qualification is still ahead (2027) | High |
| Execution | Three products (ground HSM, payload, own satellites) with a small team; rideshare launches often slip | High |
| Market | Satellite QKD is still in demo mode worldwide; there is no proven paid "keys from space" market yet | High |
| Customer | First buyers are governments; slow procurement, lumpy orders | Medium |
| Capital | Dedicated satellites in 2028 need a much larger round | Medium |
| Competition | SpeQtral (Singapore), the SES-led Eagle-1 group, China's state programme | Medium |
| Regulatory | Space activity needs IN-SPACe authorisation; exports need SCOMET licences [S37] | Medium |

**Main key risk:** whether the chip passes flight qualification in 2027, and whether a government signs a paid mission before the company needs a large round.

**Kalaari fit**
- Stage: pre-seed is done; the seed round is likely around the terrestrial product and the 2027 demo. A Kalaari cheque of $1M to 3M fits its range [S7].
- Use of past funds: the pre-seed goes to flight qualification of the chip and product development [P1]. Accelerator and angel money got the chip validated. Lean so far.
- Thesis: Kalaari backed Digantara, so it has space diligence muscle, and the products do not overlap.
- **Verdict:** good fit on stage. A classic "back the chip before the satellite" bet, priced before the 2027 demo removes the biggest risk.

**Photonics link:** Strong. The core IP is a photonic integrated chip.

**Open questions:** who the advisors are; the first paying customer and its price; cost per payload; the export-licence plan.

## Pick 2: Quanfluence

Registered in Pune (Quanfluence Pvt Ltd, CIN U72900PN2021PTC204837, incorporated 4 Oct 2021), operating from Bengaluru, incubated at IIT Madras [F7][F1]. Sells a light-based optimisation computer today (an optical Ising machine) and is building a room-temperature photonic quantum computer [F3].

**Why invest now**
- Capital is flowing into photonic and other quantum computing: PsiQuantum raised $1B at $7B (Sep 2025) [S28]; Xanadu agreed a SPAC deal with about $500M of gross proceeds at a $3.0B pre-money value (Nov 2025) [S29]; Quantinuum raised $600M at a $10B pre-money value (Sep 2025) [S30]. In India, QpiAI raised $32M at a $162M post-money value with the NQM as co-lead (Jul 2025) [S33].
- The NQM names photonic machines among the platforms for its 50 to 1,000 qubit target [S2].
- The round is live: the CEO said in Dec 2025 that Quanfluence plans to raise $15M in 2026 to reach 50 qubits by 2029 [F5].
- Near-term demand exists in optimisation-heavy work: finance, logistics, scheduling and pharma [F2][F3].

**Team**
- Sujoy Chakravarty (CEO), Ravi Mehta (COO) and Biman Chattopadhyay (CTO) have worked together for 20+ years: first at Texas Instruments, then as co-founders of Silicon and Beyond, a chip-IP company that Synopsys acquired in 2018 [F2][F3]. Founders with a real exit to a global chip-design leader.
- Co-founders also include Prof. Anil Prabhakar (IIT Madras; also a QNu co-founder), Prof. Sandeep Goyal (IISER Mohali) and Aditi Vaidya (hardware) [F1][F2].
- 27 employees (PitchBook) [F8].
- Backers: pi Ventures (from its ₹702 cr second fund), Golden Sparrow, and Reena Dayal, founder of the Quantum Ecosystems and Technology Council of India [F1].

**Proof so far**
- A working optical Ising machine, reachable online through an API or installed on site [F4].
- Problem-size claims vary by date: 128 fully connected variables (Dec 2024) [F2][F3]; up to 20,000 variables, with 100,000 next (Mar 2025) [F4]; the product page now says up to 100,000 [F6]. Ask which version is live and on what problems.
- Revenue: about $400K in the prior year (ET, Dec 2024) [F2]; about $0.5M "so far" (HT, Dec 2025) [F5]. Inc42 reported in Mar 2025 that optimiser access was not yet being charged for [F4], so ask where the revenue comes from.
- Nine patents filed; a fully equipped optics lab and a clean room for chip testing in Bengaluru [F5].
- Over $1M of grants from the Department of Telecommunications for specific circuits [F5].

**Business model and who buys**
- Now: optimisation as a service (cloud API) and on-site machines for finance, logistics, pharma, materials and AI companies [F4][F5]. Pricing is not public.
- Later: sell or rent photonic quantum computers to national labs, supercomputing centres and large companies.
- Pilots so far are with unnamed customers [F2][F3].

**Market size (calculated)**
- Now, optimisation service: 2,000 largest companies worldwide [S18] × 10 to 25% with heavy optimisation work × $25K to 100K a year (my assumption; no public price exists yet) = **$5M to 50M a year**. India alone: 2,720 NSE-listed companies × 2 to 5% × ₹10 to 25 lakh = ₹5 to 34 cr a year. Small.
- Later, quantum computers: the world's 500 largest supercomputing sites (the TOP500 list) × 20 to 50% buying an on-site system by 2035 × $12.6M (what D-Wave booked for one system sold to Jülich [S27]) to $50M = 100 to 250 systems, **$1.26B to 12.5B over ten years, or $126M to 1.25B a year**. India alone: 5 to 15 systems (NQM machines, national labs, large banks) = $63M to 750M in total.
- Cross-check: McKinsey says quantum computing companies earned over $1B in 2025 [S10].
- **Big enough?** Yes, but only in the long run. Today's product buys time and data; it is not the prize.

**Risks (all types)**

| Type | Risk | Level |
|---|---|---|
| Technology | A general photonic quantum computer is years away (first qubits by 2029, 5,000+ by 2030-31, per the company) [F5]; light loss and error correction at scale are unsolved everywhere | High |
| Capital | Needs $15M now and far more later; risk of heavy dilution or running short before 2029 | High |
| Competition | PsiQuantum, Xanadu and others have raised 100 times more [S28][S29] | High |
| Market | The optimisation market is small today, and GPU-based classical solvers keep improving | Medium |
| Revenue quality | Unclear what the $0.4 to 0.5M of revenue is made of | Medium |
| Talent | Photonics and quantum engineers are scarce in India | Medium |
| Regulatory | No specific licensing hurdle for selling optimisation services today | Low |

**Main key risk:** the gap between what near-term revenue can pay for and what the 2029 qubit milestone costs.

**Kalaari fit**
- Stage: seed done ($2M, Dec 2024, pi Ventures) and a ~$15M raise planned for 2026 [F1][F5]. The Series A rounds Kalaari joins average about $4.8M [S8] and its cheques top out around $5M [S7]. A $15M round is three times its usual Series A, so Kalaari would co-invest $3M to 5M next to pi Ventures rather than lead alone. The planned deeptech fund could raise that ceiling.
- Use of past funds: the seed was meant to scale the optimiser and start the full quantum computer [F1][F4]. What came out: a working machine, nine patents, a lab and clean room, $0.4 to 0.5M of revenue and $1M+ in grants [F2][F5]. Good use of a small seed.
- Thesis: fits the RDI "quantum computing" sub-sector and the photonics angle. No conflict in Kalaari's portfolio.
- **Verdict:** the best fit of the seven on team, stage and timing.

**Photonics link:** Strong. It computes with light.

**Open questions:** the live problem size and benchmark against GPU solvers; paying customers and prices; who leads the 2026 round; the budget to reach 50 qubits.

## Sources

**Shared: policy, market, Kalaari, prices**
- [S1] DST quantum-safe ecosystem and final migration roadmap (May 2026): [DST page](https://dst.gov.in/quantum-safe-ecosystem-in-india); summary with dates: [PostQuantum, 15 May 2026](https://postquantum.com/security-pqc/india-quantum-safe-final-roadmap/)
- [S2] [PIB: Cabinet approves National Quantum Mission, 19 Apr 2023](https://pib.gov.in/PressReleasePage.aspx?PRID=1917888)
- [S3] [DST: NQM thematic hubs announced](https://dst.gov.in/nqm-landmark-t-hubs-announced-lead-indias-quantum-revolution)
- [S4] [DST: eight startups selected under NQM, 27 Nov 2024](https://dst.gov.in/dr-jitendra-singh-announces-selection-eight-pioneering-startups-support-under-national-quantum)
- [S5] [ET: VCs eye deeptech fund launches to leverage RDI capital, 26 May 2026](https://economictimes.indiatimes.com/tech/startups/vcs-eye-deeptech-fund-launches-to-leverage-rdi-capital/articleshow/131314485.cms)
- [S6] [PIB: operationalisation of the RDI deep tech fund of funds, Feb 2026](https://www.pib.gov.in/PressReleasePage.aspx?lang=2&PRID=2226469&reg=48)
- [S7] [F4: Kalaari Capital profile (AUM, cheque sizes)](https://f4.fund/firms/kalaari-capital)
- [S8] [Tracxn: Kalaari Capital investor profile](https://tracxn.com/d/venture-capital/kalaari-capital/__nmJxhS2XJwLP9-Lmd1RP_jSElZJ50toovUI06SL8q6o)
- [S9] [ET: MeshDefend raises $2.3M led by Kalaari](https://economictimes.indiatimes.com/tech/funding/ai-enterprise-ops-startup-meshdefend-raises-2-3-million-in-round-led-by-kalaari-capital/articleshow/125111852.cms)
- [S10] [McKinsey Quantum Technology Monitor 2025](https://www.mckinsey.com.br/capabilities/tech-and-ai/our-insights/the-year-of-quantum-from-concept-to-reality-in-2025)
- [S11] [Tracxn: quantum computing startups in India](https://tracxn.com/d/explore/quantum-computing-startups-in-india/__rhoBWcnKeW3iFJ-j009WIncqNuWufbYTP3NLuVy_haA)
- [S12] [RBI: scheduled commercial banks by category, 31 Mar 2025](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23639)
- [S13] [IRDAI: meet the insurers](https://irdai.gov.in/en/web/policy-holder/meet-the-insurers)
- [S14] [SEBI Bulletin, Mar 2024 (tables)](https://www.sebi.gov.in/sebi_data/commondocs/mar-2024/SEBI_Bulletin_Mar_2024_Tables_p.pdf)
- [S15] [PFC: 13th integrated rating of power distribution utilities](https://pfcindia.co.in/ensite/DocumentRepository/ckfinder/files/GoI_Initiatives/Annual_Integrated_Ratings_of_State_DISCOMs/13th%20Annual%20Integrated%20Rating%20and%20Ranking%20of%20Power%20Distribution%20UtilitiesEA2.pdf)
- [S16] [DPE: Public Enterprises Survey 2023-24](https://www.dpe.gov.in/static/uploads/2025/07/6a915ddd75b143a720883c87531bec15.pdf)
- [S17] [NSE: FY2024-25 highlights](https://www.nseindia.com/mediacoverage/nse-fy24-25-highlights)
- [S18] [Forbes Global 2000, 2025 release](https://www.forbes.com/sites/forbespr/2025/06/12/forbes-releases-23rd-annual-global-2000-ranking-of-the-worlds-largest-companies/)
- [S19] [UK G-Cloud: Keyfactor Command listing](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/628376205630026)
- [S20] [AWS Marketplace: SandboxAQ AQtive Guard](https://aws.amazon.com/marketplace/pp/prodview-ccwrhqfeekqwk)
- [S21] [AWS Marketplace: QuSecure QuProtect](https://aws.amazon.com/marketplace/pp/prodview-mq2rah5aavcuy)
- [S22] [White House ONCD: Report on Post-Quantum Cryptography, Jul 2024](https://bidenwhitehouse.archives.gov/wp-content/uploads/2024/07/REF_PQC-Report_FINAL_Send.pdf)
- [S23] [Instrumenthive: ID Quantique Clavis3 listing](https://www.instrumenthive.com/products/id-quantique-clavis3-coherent-quantum-key-distribution-system/)
- [S24] [Space Intel Report: Eagle-1 contract, Sep 2022](https://www.spaceintelreport.com/quantum-entanglement-esa-ses-and-thales-speqtral-to-launch-quantum-satellites-in-2024-esas-arqit-partnership-continues/)
- [S25] [Canadian Space Agency: QEYSSat contract, Jun 2019](https://www.canada.ca/en/space-agency/news/2019/06/cybersecurity-from-space-the-government-of-canada-invests-in-quantum-technology.html)
- [S26] [Nature: Microsatellite-based real-time quantum key distribution, 19 Mar 2025](https://www.nature.com/articles/s41586-025-08739-z)
- [S27] [D-Wave: Q1 2025 results](https://www.dwavequantum.com/company/newsroom/press-release/d-wave-reports-first-quarter-2025-results/)
- [S28] [PsiQuantum: $1B raise, Sep 2025](https://www.psiquantum.com/news-import/psiquantum-1b-fundraise)
- [S29] [SEC filing: Xanadu and Crane Harbor business combination, Nov 2025](https://www.sec.gov/Archives/edgar/data/2054174/000121390025104920/ea026354401ex99-1_crane.htm)
- [S30] [Quantinuum: $600M raise, Sep 2025](https://www.quantinuum.com/press-releases/honeywell-announces-600-million-capital-raise-for-quantinuum-at-10b-pre-money-equity-valuation-to-advance-quantum-computing-at-scale)
- [S31] [SandboxAQ: Series E, Apr 2025](https://www.sandboxaq.com/press/sandboxaq-closes-450m-series-e-round-with-expanded-investor-base)
- [S33] [TechCrunch: QpiAI $32M Series A, Jul 2025](https://techcrunch.com/2025/07/16/india-eyes-global-quantum-computer-push-and-qpiai-is-its-chosen-vehicle/)
- [S34] [Ansys 10-K, FY2024](https://www.sec.gov/Archives/edgar/data/1013462/000101346225000009/anss-20241231.htm)
- [S35] [GuruFocus: Ansys Q4 2024 (50,000+ customers)](https://www.gurufocus.com/news/2704749/ansys-inc-q4-earnings-revenue-surpasses-estimates-at-8822m-eps-misses-at-321)
- [S37] [SCOMET List 2025 (MEA)](https://www.mea.gov.in/images/SCOMET-List-2025.pdf); [NASSCOM paper on encryption export control](https://community.nasscom.in/sites/default/files/blog/attachments/20211005_EncryptionExportControl_NASSCOMPaper_final.pdf)
- [S38] RBI reference rates: [USD, via CEIC](https://www.ceicdata.com/en/india/foreign-exchange-rate-reserve-bank-of-india/foreign-exchange-rate-rbi-reference-rate-us-dollars); [EUR and GBP, via MSEI](https://www.msei.in/markets/currency/historical-data/rbireferenceratearchives)

**Pramatra Space**
- [P1] [Pramatra: pre-seed announcement, 25 May 2026](https://pramatra.space/blogs/pramatra-space-raises-pre-seed-funding-to-build-a-quantum-secure-future-from-space)
- [P2] [Pramatra website (team and advisors)](https://pramatra.space/)
- [P3] [Pramatra and Infostellar MoU](https://pramatra.space/blogs/pramatra-space-and-infostellar-sign-strategic-mou-for-qkd-ground-station-services)
- [P4] [Quantum Computing Report: Pramatra pre-seed, 30 May 2026](https://quantumcomputingreport.com/pramatra-space-secures-pre-seed-capital-to-advance-space-based-quantum-key-distribution-hardware/)
- [P5] [Tracxn: Pramatra Space Technology Pvt Ltd (legal entity)](https://tracxn.com/d/legal-entities/india/pramatra-space-technology-private-limited/__zbr7kPcnhEgC_1xoZ_zJUdPNOihv1AsyYUxhUNXFdf4)
- [P6] [NASSCOM Emerge 50: Pramatra (products, claims, timeline)](https://nasscom.in/emerge50/winners/pramatra-space-technology-pvt.-ltd..html)
- [P7] [LinkedIn: Sharad Sanghi](https://www.linkedin.com/in/sharadsanghi)
- [P8] [Inc Business: Securing the space age, 12 Jun 2026](https://incbusiness.in/business/securing-the-space-age-pramatra-space-is-building-quantum-resilient-communication/)
- [P9] [Indian Startup Times: Pramatra pre-seed, 25 May 2026](https://www.indianstartuptimes.com/investment/pramatra-space-raises-pre-seed-funding-to-build-a-quantum-secure-future-from-space/)
- [P10] [NewSpace Tracker: Pramatra (Techstars Space 2024)](https://newspacetracker.com/company/pramatra-space/)
- [P11] [LinkedIn: Pramatra team member profile with company size data](https://in.linkedin.com/in/keshavkasliwal)

**Other companies cited above**
- [Q1] [Times of India: QNu Labs raises ₹350 cr, 9 Sep 2026](https://timesofindia.indiatimes.com/city/chennai/qnu-labs-raises-350cr-to-scale-quantum-security-biz/articleshow/133933949.cms)
- [Q3] [DST: QNu Labs building an end-to-end quantum-safe network, 25 Mar 2025](https://dst.gov.in/quantum-startup-qnu-labs-working-build-and-deploy-worlds-first-end-end-quantum-safe-heterogeneous)

**Quanfluence**
- [F1] [Quanfluence: $2M seed led by pi Ventures, 18 Dec 2024](https://quanfluence.com/quantum-technology-startup-quanfluence-nets-2-mn-led-by-pi-ventures/)
- [F2] [ET: Quanfluence raises $2M, 18 Dec 2024](https://m.economictimes.com/tech/funding/quantum-technology-startup-quanfluence-raises-2-million-from-pi-ventures/articleshow/116440181.cms)
- [F3] [pi Ventures: why we invested in Quanfluence](https://www.piventures.in/blog-article/next-gen-computing-platform-by-quanfluence)
- [F4] [Inc42: the startup building India's first photonic quantum computer, 11 Mar 2025](https://inc42.com/startups/meet-the-startup-building-indias-first-photonic-quantum-computer/)
- [F5] [Hindustan Times: Photonics bet pays off for Quanfluence, 6 Dec 2025](https://www.hindustantimes.com/cities/pune-news/startup-mantra-photonics-bet-pays-off-for-quanfluence-101764962113406.html)
- [F6] [Quanfluence: coherent Ising machine product page](https://quanfluence.com/time-multiplexed-coherent-ising-machine/)
- [F7] [QuickCompany: Quanfluence Pvt Ltd registry data](https://www.quickcompany.in/company/quanfluence-private-limited)
- [F8] [PitchBook: Quanfluence profile](https://pitchbook.com/profiles/company/718377-76)

**Detector prices**
- [N7] [BidsFactory: SNSPD system awarded to Single Quantum, €163,000](https://bidsfactory.com/en/tenders/supraleitendes-nanodraht-einzelphotonen-detektorsy-ted-995ae8273bc8066a)
- [N8] [Cobrief: University of Oslo SNSPD award, NOK 1.56M, Aug 2025](https://anbud.cobrief.no/procurements/si-superconducting-nanowire-single-photon-detect-2025-08-20-199186)
