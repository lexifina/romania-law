# Romania: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Romania's national law, which global-law reads at `romania/national/acts/`.

The aim: every source a Romanian lawyer or citizen needs, in one git history. Laws and their full histories, case law, secondary legislation, local acts and more: the [plan](PLAN.md) lists every part, with its progress.

**Scope**
- Rebuilt Romanian law from the official texts as one git history: the Constitution, the codes and tens of thousands of laws, ordinances and Government decisions, with secondary legislation, local acts, treaties and EU law.
- Linked Constitutional Court and High Court rulings to the articles they concern, with the ECHR's judgments against Romania and the EU Court of Justice's decisions concerning Romania.

**Use**
- The official portal shows one version of an act at a time. Here, how a provision changed, or what it said on a given date, is one `git log` or `git blame`.
- Everything can be searched, compared and reused: the texts are official, and our work is public domain (CC0).

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Romanian law in this repository: acts, changes as commits, article files, court rulings, official texts read and years of history; changes by the year they took effect; and the plan by part, published and collected" src="data/effort-light.svg" width="880">
</picture>

### See it in use: the Romania MCP

https://github.com/user-attachments/assets/3f47ad88-f514-4765-97e3-ff67ed8f79b4

An AI assistant answering a question about Romanian law through the MCP: the answer cites the exact article and version in this repository, with the official links.

### Romanian law, drawn

![The government writes four acts for every law Parliament passes](https://raw.githubusercontent.com/lexifina/global-law/main/visualisations/stills/romanian-law-drawn-01-the-government-writes-four-acts-for-every-law-parl.png)

One of thirty charts drawn from this repository; see [visualisations/](visualisations/) for the rest.

## Layout

| Where | What |
| --- | --- |
| `constitutie/1991/`, `lege/`, `oug/`, `og/`, `hg/` | the Constitution, laws (with the codes: Codul civil is `lege/2009/287/`), ordinances and Government decisions, by year and number |
| `ordin/`, `norma/`, `regulament/`… | ministerial orders and authority norms |
| `local/` | local council decisions, by council and year |
| `ue/`, `tratat/`, `anexa/`, `profesii/` | EU law in Romanian, treaties, official annexes, the legal professions' rules |
| `jurisprudenta/` | court decisions: `ccr/`, `iccj/`, `cedo/`, `cjue/` |
| `<act>/art-NNN.md` · `<act>/README.md` | one article per file (one paragraph per line) · the act's versions and notes |
| [ACTS.md](ACTS.md) · `data/` · `tools/` | the act list · tables and indexes ([DATA.md](DATA.md)) · the tools below |

[AGENTS.md](AGENTS.md) explains how a program or an AI agent should query the repository.

## Use it

| Question | Command |
| --- | --- |
| What did art. 1112 of the Codul civil say on 18 October 2014? | `python tools/on.py 2014-10-18 lege/2009/287 1112` |
| Which act wrote each paragraph of art. 336 of the Codul penal? | `git blame lege/2009/286/art-336.md` |
| Every change to an article, word by word | `git log --follow -p --word-diff lege/2009/286/art-297.md` |
| Everything one act changed | `git show law/legea-200-2023` |
| Is the Codul civil here current? | `python tools/freshness.py codul-civil` |

Read dates with the tools, not `git rev-list --before`: they pick each version by its `In-force:` trailer.

## Data, case law and sources

- **Tables:** act lists and indexes, links between acts, the bills behind each law, EU transposition, and practical tables (which court covers each locality, court fees, deadlines, legal aid, minimum wage, legal interest). All are listed in [DATA.md](DATA.md).
- **Case law:** Constitutional Court and High Court (RIL and HP) decisions as published in the Monitorul Oficial, ECHR judgments against Romania, and EU Court of Justice decisions concerning Romania (operative part). Each decision is one commit; a Constitutional Court finding that struck a text is a separate commit in that act's history.
- **Sources:** the Ministry of Justice's legislative portal, archived copies of it, Parliament, the EU Publications Office and the issuing authorities ([DATA.md](DATA.md#sources)).

## How current is it

Every version names the official page it was read from, so every act can be checked against its source.

<!-- freshness-summary -->
Checked against the official sources: 2026-11-07; 82% of acts verified in the last 7 days, 82% in the last 30 ([data/freshness.json](data/freshness.json)).
<!-- /freshness-summary -->

`python tools/freshness.py <act>` gives an act's status, its last check and the official link. The pipeline is monitored around the clock, and [data/status.json](data/status.json) (hourly) says whether updates are running and which official sources are answering. Statuses and fields: [DATA.md](DATA.md#freshness).

## Dates, authors and limits

- Each commit is dated on the day the change took effect; the author is the act that made it, the committer Lexifina.
- An act's latest version is the newest consolidated form held, so later amendments may be missing; acts marked `amended, not consolidated` hold the act as published and name the amending acts.
- Only the Monitorul Oficial, Part I is authoritative (for EU acts, the Official Journal of the EU).
- Not included: chapter and section headings, the portal's editorial notes, and annexes printed as facsimiles.
- Every version is read back from git on its in-force day and must match the source; results are in `REPRODUCE.md`.

## Personal data

Official acts are republished as the Monitorul Oficial printed them, including the names of the persons they concern. CNPs, home addresses and dates of birth are removed, and decisions about criminal matters are metadata only. Anyone named can ask for a correction or removal via [lexifina.com](https://lexifina.com).

## Licence

The legal texts are official texts of Romanian normative acts (Sursa: Portalul legislativ al Ministerului Justiției, https://legislatie.just.ro), excluded from copyright by Legea nr. 8/1996, art. 9 lit. b. The EU texts are © European Union, reused under Commission Decision 2011/833/EU. Lexifina's arrangement, tables, commit messages and tools are in the public domain (CC0), as set out in `LICENSE`. This repository is not legal advice and not an official publication.

## În limba română

Istoria dreptului românesc în git: un fișier pentru fiecare articol și un commit pentru fiecare modificare, datat în ziua intrării ei în vigoare și semnat de actul care a făcut-o. Lista actelor este în [ACTS.md](ACTS.md); textul în vigoare la o dată: `python tools/on.py 2014-10-18 lege/2009/287 1112`. Sursa: Portalul legislativ al Ministerului Justiției (legislatie.just.ro). Niciun model de inteligență artificială nu a scris text juridic.
