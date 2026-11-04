# Romania: law history in git

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/coverage-dark.svg">
<img alt="How much of Romanian law is here: acts on main against every numbered law, ordinance and government decision the official service publishes, by kind; the Constitution and the main codes with their histories" src="data/coverage-light.svg" width="880">
</picture>

The law of Romania as a git history: one file per article, one commit per change on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every paragraph, `git log` lists every change to an article, and the tools give the text in force on any date. The texts are in Romanian, as published.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `romania/national/acts/`.

## Scope

This repository holds Romania's **primary legislation**: the Constitution, the laws of Parliament (the codes among them), and the Government's emergency ordinances (OUG), ordinances (OG) and decisions (HG). The card above counts them against every such act we have found in the official service; that list is still growing, so the real total is higher.

The repository will grow well beyond that: case law, the orders and norms of ministries and authorities, local councils' decisions, treaties, EU links and legislative history. The next section lists every part planned, with its size and progress.

<!-- plan:start -->

## What will be here

The aim is every source a Romanian lawyer or citizen needs. This table is the plan, bin by bin, with what is published so far; it is regenerated with each documentation commit, so the gap can be followed over time.

**40.8%** of the plan is published, weighted by how binding each source is and how often it is used. **71.7%** counting sources already collected but not yet published. 1.7% of the weight is in bins that need the publisher's permission first. Updated 2026-11-04 17:41 UTC.

| Bin | Will be in | Weight | Progress | How | Status |
| --- | --- | ---: | --- | --- | --- |
| **Primary legislation** | | | | | |
| Constitution and codes | constitutie/1991/; the codes in lege/ and oug/ (Codul civil is lege/2009/287/) | 11.7% | 19 of 20 acts · 95.0% | built by hand with every version, checked against the text as published | collecting |
| Laws, OUG, OG and HG (consolidated) | lege/, oug/, og/, hg/ | 25.3% | 35,334 of 55,923 acts · 67.8% | automatic: the official text as published plus every consolidated form | collecting |
| Amended, not consolidated | lege/, oug/, og/, hg/ with status "amended, not consolidated" | in the laws bin | 5,876 of 8,321 acts · 70.6% | the official text as published, labelled, with the amending acts named | collecting |
| Third-party-only acts | lege/, oug/, og/, hg/ once found in the official service | 1.9% | 445 of 5,166 acts · 8.6% | searched for one by one in the official service; only its text is used | collecting |
| **Case law** | | | | | |
| CCR decisions | jurisprudenta/ccr/ | 9.7% | 11,614 of 25,153 decisions; 0 of 937 rulings applied · 36.9% | official texts as published; unconstitutionality rulings dated on the articles they suspend | collecting |
| ICCJ RIL and HP | jurisprudenta/iccj/ | 4.9% | 229 of 2,102 decisions · 10.9% | official texts as published, linked to the articles they interpret | collecting |
| ICCJ other judgments (links) | data/iccj-links.csv | 1.0% | target unknown | links and metadata only | no publication channel found yet |
| Lower courts (ReJust links; MO annulments) | data/rejust-links.csv; annulments as effects on acts | 1.5% | 0 of 26,000,000 judgments; 0 of 229 annulments · 0.0% | links and metadata only; annulments of acts as dated effects | planned |
| ECHR judgments against Romania | jurisprudenta/cedo/ | 1.5% | 157 of 1,942 judgments · 8.1% | Romanian translations published in the Monitorul Oficial; HUDOC links for the rest | collecting |
| CJEU references | data/cjeu-links.csv | 0.5% | 0 of 397 cases · 0.0% | links by ECLI and CELEX to the EU publications | planned |
| CNSC and other bodies | jurisprudenta/cnsc/ (links for the rest) | 0.5% | target unknown | official bulletins, where reuse is allowed | needs the publisher's permission |
| **Secondary legislation** | | | | | |
| Ministerial and authority orders | ordin/<issuer>/ | 10.7% | 0 of 62,513 orders · 0.0% | official texts as published, with the documents that amend them | collecting |
| Norms and regulations (BNR, ASF, ANRE, ANCOM and others) | norme/<issuer>/ | 11.2% | 0 of 38,525 acts · 0.0% | official texts as published | planned |
| Standards (ASRO) | none: standard numbers cited only | – | out of scope | standard numbers cited only (the texts are copyright) | not planned: Copyright held by ASRO |
| **Local acts** | | | | | |
| Local acts: Bucharest (CGMB) | local/bucuresti/cgmb/ | 1.2% | 0 of 12,236 records · index pages 1,224/1,224 · listed 12,236/12,236 · texts 1 · 0.0% | the council's own register of decisions (PDF and text) | collecting |
| Local acts: Bucharest sectors 1-6 | local/bucuresti/sector-1/ ... sector-6/ | 0.6% | 0 of 6 sectors · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: county councils (41) | local/judet/<county>/ | 1.0% | 0 of 41 councils · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: municipalities and towns | local/<county>/<municipality or town>/ | 0.7% | 0 of 320 councils · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: communes | local/<county>/<commune>/ | 0.3% | 0 of 2,861 councils · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: other local authorities (prefects' orders) | local/prefect/<county>/ | 0.2% | 0 of 42 prefects · 0.0% | each prefecture, where it publishes | no publication channel found yet |
| **EU and international** | | | | | |
| Treaties | tratat/ (texts), linked from the ratifying acts | 2.0% | 0 of 2,648 treaty texts; 1,664 of 3,500 acts · 18.1% | official texts, linked from the ratifying acts | collecting |
| EU transposition links | data/eu-transposition.csv | 2.9% | 6,938 of 5,834 notification records · 100.0% | EU notification records and the transposition clauses in the acts | done |
| EU law in Romanian (links) | data/eu-links.csv (texts, if kept, in eu/) | 0.5% | 0 of 37,112 EU acts · 0.0% | links to the Romanian text on EUR-Lex | planned |
| **Parliament and President** | | | | | |
| Presidential decrees | promulgation data on each law; normative decrees in decret/ | 0.3% | 0 of 9,678 decrees · 0.0% | promulgation data on each law; normative decrees as acts | planned |
| Parliament decisions | hotarare-parlament/ | 0.4% | 0 of 7,050 decisions · 0.0% | official texts as published | planned |
| **Legislative history and publications** | | | | | |
| Legislative history (amendment links, bills, Council opinions) | data/act-links.csv, data/bills.csv | 5.6% | 53,706 of 36,045 acts; 0 of 7,467 laws (+2 more) · 61.4% | the Chamber of Deputies' act sheets and bill files | collecting |
| Monitorul Oficial parts | MO reference in each version; data/mo-links.csv | 1.3% | 36,045 of 36,045 acts · 38.5% | the Monitorul Oficial reference of every version | planned |
| Collective labour agreements (MO Part V) | cct/ | 0.3% | 0 of 57 agreements · 0.0% | official texts as published | planned |
| **Historical law** | | | | | |
| Historical law | cod/ (old codes), decret-lege/, pre-1990 lege/ and decret/ | 2.4% | 9 of 10 codes and statutes; 2 of 200 decree-laws (+1 more) · 36.5% | built by hand from the official texts | collecting |
| **Out of scope** | | | | | |
| Doctrine, forms, arbitral awards | none | – | out of scope | not planned (not law, or not public) | not planned: Copyrighted per publisher |

Progress counts what is on `main`; targets are the official counts where they exist (the portal's own listing, the courts' totals), otherwise the best public estimate. Folders not on `main` yet will appear as the bins are published.

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
