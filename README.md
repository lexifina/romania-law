# Romania: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Romania's national law, which global-law reads at `romania/national/acts/`.

> ### The aim: every source a Romanian lawyer or citizen needs, in one git history. > Laws and their full histories, case law, secondary legislation, local acts and more: the [plan](PLAN.md) lists every > part, with its progress.

**What we did**
- Rebuilt Romanian law from the official texts as one git history: the Constitution, the codes and tens of thousands of laws, ordinances and Government decisions.
- Each article is a file. Each change is a commit dated the day it took effect, credited to the act that made it.
- Linked Constitutional Court and High Court rulings to the articles they concern, and added the European Court of Human Rights' judgments against Romania.

**Why**
- The official portal shows one version of an act at a time, so tracing how a provision changed, or what it said on a given date, means comparing versions by hand. Here it is one `git log` or `git blame`.
- The whole history can be searched, compared and reused: the texts are official, and our work on them is in the public domain (CC0).

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Romanian law in this repository: acts, changes as commits, article files, court rulings, official texts read and years of history; changes by the year they took effect; and the plan by part, published and collected" src="data/effort-light.svg" width="880">
</picture>

### See it in use: the Romania MCP

[![The Romania MCP answering questions with pin-point citations to this repository (video)](https://lexifina.com/watch/romania/romania-mcp-poster.png)](https://lexifina.com/watch/romania)

An AI assistant answering questions about Romanian law through the MCP, each answer citing the exact article and version in this repository.

`git blame` names the act behind every paragraph, `git log` lists every change to an article, and the tools give the text in force on any date. The texts are in Romanian, as published. [AGENTS.md](AGENTS.md) explains the layout for programs and AI agents.

## Scope

Here now:
- **Primary legislation:** the Constitution, the codes (and the historical codes still applied), the laws of Parliament, and the Government's emergency ordinances (OUG), ordinances (OG) and decisions (HG), with their full histories; the decree-laws of 1989–1990.
- **Parliament:** the first decisions of the Chamber of Deputies, the Senate and joint sittings.
- **Case law:** Constitutional Court decisions, the High Court's binding decisions (RIL and HP) and the European Court of Human Rights' judgments against Romania, under `jurisprudenta/`.
- **Data:** promulgation decrees, treaty–ratification links, rectifications, EU transposition, the Monitorul Oficial issue index and local tax decisions, under `data/`.

Coming: ministries' and authorities' orders and norms, local councils' decisions, draft acts in consultation, electoral and oversight bodies' decisions, construction norms and more. [PLAN.md](PLAN.md) lists every part planned, with its size and progress.

<!-- plan:start -->

## Progress

**48.5% of the plan is published** and 72.0% is collected, weighted by how binding each source is and how often it is used. The plan, part by part, with targets and progress: [PLAN.md](PLAN.md). Updated 2026-11-04 23:12 UTC.

<!-- plan:end -->

## Layout

| Where | What |
| --- | --- |
| `constitutie/1991/` | the Constitution |
| `lege/<year>/<number>/` | laws, including the codes adopted by law (Codul civil is `lege/2009/287/`) |
| `oug/<year>/<number>/` | Government emergency ordinances (Codul administrativ is `oug/2019/57/`) |
| `og/<year>/<number>/` · `hg/<year>/<number>/` | Government ordinances · Government decisions |
| `<act>/art-NNN.md` | one article per file, one paragraph, letter or point per line; art. 112^1 is `art-112-1.md` |
| `<act>/README.md` | the act's articles, versions and the decisions made by hand for it |
| [ACTS.md](ACTS.md) | every act, with its folder, status and span; the codes first |
| `data/` | `acts.json` (one row per act), `paths.json`, `versions.json` and CSV tables, including `act-links.csv` and `eu-transposition.csv` (below) |
| `tools/` | `on.py` and `in_vigoare_la.py` (the law on any date); `tools/build/` holds the builder |
| [AGENTS.md](AGENTS.md) | how a program or an AI agent should query this repository |

Each act also has a short id (`codul-civil`, `legea-31-1990`, `hg-10-2016`) used by the tools and the tags. Until the layout move of November 2026 the folders were named by id; `git blame` and the tools follow the move, and `git log` on one file needs `--follow`.

### Links between acts

`data/act-links.csv` lists 86,809 links between acts as the Chamber of Deputies' legislation database records them: which act amends, repeals, approves, rejects, promulgates or implements another, and the republications and rectifications in the Monitorul Oficial. Columns: `source`, `target` (this repository's ids where the act is one of its kinds; other acts keep a kind prefix such as `decret-` or `ordin-`), `relation`, `provisions` (as the database states them), `captured` (the date of the database page that shows the link), `label` (the database's own wording) and the Chamber's record numbers. The database is not official and its pages were read as captured between 2018 and 2025: a link made later is missing, and a missing link does not mean an act was never changed. Use it to find related acts, then check them against the Monitorul Oficial.

### EU law each act transposes

`data/eu-transposition.csv` links 2,339 Romanian acts to the 1,814 EU acts they transpose or implement (6,938 rows). `link_source` says where each link comes from: `nim`, Romania's notification to the European Commission (the EU Publications Office's records of national implementing measures, CC0); `clause`, the transposition note in the act as published (Legea 24/2000, art. 45); `both`, when they agree. Other columns: `act_slug`, `act_folder`, `eu_celex`, `eu_title`, `scope` (the whole act, or the part the note names) and the Monitorul Oficial issue named in the notification. The two sources often name different EU acts (a base directive, or a later amendment); both are kept. Some acts listed are not in the repository yet. Retrieved 4 November 2026.

## Case law

`jurisprudenta/` holds the decisions that say what a provision means or whether it still applies, as published in the Monitorul Oficial, Part I. They are added in batches, oldest first, until all 23,743 are on `main`:

| Court | Decisions | Folder |
| --- | ---: | --- |
| Constitutional Court (Curtea Constituțională), from 1992 | 21,561 | `jurisprudenta/ccr/<year>/<number>/` |
| High Court of Cassation and Justice (ÎCCJ): appeals in the interest of the law and preliminary rulings, from 1998 | 1,863 | `jurisprudenta/iccj/<panel>/<year>/<number>/` (`ril`, `hp`, `hp-penal`, `su`, `scaf`) |
| European Court of Human Rights, judgments against Romania in the Monitorul Oficial's translation | 319 | `jurisprudenta/cedo/<year>/<application>/` |

Each folder has the text (`decizie.md`, one paragraph per line) and `meta.json`: number, date, Monitorul Oficial issue, kind, outcome, the operative part, and the acts and articles it rules on. `data/rulings-by-provision.json` maps each article (`lege/2009/287`, `2526`) to the decisions about it; `jurisprudenta/acte/<act folder>.md` is the same for people; `data/decisions.csv` lists them all. Each decision is one commit of kind `ruling` on its publication day, authored by the court at the decision's id (`dcc-623-2019`), tagged `ruling/<id>`. A ruling changes no act file: the change a Constitutional Court decision made to a text is a separate commit of kind `court` in that act's history, under the same id. Names of parties are reproduced as the Monitorul Oficial prints them. The portal holds about 85% of the Constitutional Court's own yearly totals in recent years; the gap is not explained yet. Field-by-field details are in [AGENTS.md](AGENTS.md).

## Use it

| Question | Command |
| --- | --- |
| What did art. 1112 of the Codul civil say on 18 October 2014? | `python tools/on.py 2014-10-18 lege/2009/287 1112` |
| The whole act on a date | `python tools/on.py 2000-01-01 constitutie/1991` |
| Which act wrote each paragraph of art. 336 of the Codul penal? | `git blame lege/2009/286/art-336.md` |
| Every change to an article, word by word | `git log --follow -p --word-diff lege/2009/286/art-297.md` |
| Everything one act changed | `git show law/legea-200-2023` |
| An act as it stood from a day | `git show codul-penal/2023-07-09` (tags `<id>/<in-force day>`) |

Read a date with the tools rather than `git rev-list --before`: they choose each version by its `In-force:` trailer. After a rebuild, refresh tags with `git fetch --force --tags`.

## Dates and authors

- Each commit is dated at noon, Europe/Bucharest, on the day the change took effect; `Enacted:`, `Published:` and `In-force:` are trailers. The in-force days are the portal's, which apply each act's own clause or the default rule (Constituția art. 78: 3 days after publication in the Monitorul Oficial).
- The author is the act that made the change, with an address that cannot exist (`legea-200-2023@legislatie.invalid`); the committer is Lexifina. A change is credited to an act only when the portal's amendment note names it; Constitutional Court decisions that changed the text are commits of kind `court`. Changes no note explains are committed by the publisher and labelled "unexplained".
- Where an act needed a judgement (a missing form, a republication, an article the source leaves out), the decision is in that act's `README.md`;

## Limits

- Each act's latest version is the newest consolidated form held; amendments in force after it may be missing.
- Acts with the status `amended, not consolidated` (ACTS.md, `data/acts.json`) were amended, but the official portal publishes no consolidated text of them: only the act as published is here, and its `README.md` names the amending acts known. Read those for the text in force.
- No consolidated text has legal force in Romania, ours included: only the text published in the Monitorul Oficial, Part I (and an official republication there) is authoritative. The portal's and the Legislative Council's consolidated versions are documentation tools too.
- Not included: chapter and section headings, the portal's editorial notes, annexes and figures printed as facsimiles or in a separate issue, and rulings that interpret a text without changing its wording.

## How it is checked

Every version of every act is read back from git on the day it took effect and on the day before (`tools/build/check_repo.py`), and must match the corpus. `main` has no merge commits, dates never go backwards, every trailer parses, and a second build from the same data gives identical hashes. Results are in `REPRODUCE.md`.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

Every version names the page it was read from and that page's sha256.

## Sources

| Source | Used for |
| --- | --- |
| [Portalul legislativ](https://legislatie.just.ro), Ministerul Justiției | the official texts, every consolidated form and the amendment notes |
| – | archived copies of the portal's pages, each capture pinned per version |
| [legalize-ro](https://github.com/legalize-dev/legalize-ro) | a check of the Codul fiscal's text |
| [Camera Deputaților](https://www.cdep.ro), legislation database | the links between acts in `data/act-links.csv` |
| [EU Publications Office](https://op.europa.eu) (CELLAR) | the notifications in `data/eu-transposition.csv` (CC0) |

## Licence

The legal texts are official texts of Romanian normative acts (Sursa: Portalul legislativ al Ministerului Justiției, https://legislatie.just.ro), which Romanian copyright law excludes from protection (Legea nr. 8/1996, art. 9 lit. b). The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`. This repository is not legal advice and not an official publication.

## În limba română

Istoria dreptului românesc în git: un fișier pentru fiecare articol și un commit pentru fiecare modificare, datat în ziua intrării ei în vigoare și semnat de actul care a făcut-o (`git blame` numește actul fiecărui paragraf). Lista completă a actelor este în [ACTS.md](ACTS.md).

- Textul în vigoare la o dată: `python tools/on.py 2014-10-18 lege/2009/287 1112`
- Datele sunt cele ale Portalului legislativ; regula generală este art. 78 din Constituție.
- O modificare este atribuită unui act numai dacă nota de modificare a portalului îl numește.
- Ultima versiune a fiecărui act este cea mai nouă formă consolidată pe care o avem: modificările ulterioare pot lipsi.
- Sursa: Portalul legislativ al Ministerului Justiției (legislatie.just.ro). Niciun model de inteligență artificială nu a scris text juridic.
