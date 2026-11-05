# Romania: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Romania's national law, which global-law reads at `romania/national/acts/`.

The aim: every source a Romanian lawyer or citizen needs, in one git history. Laws and their full histories, case law, secondary legislation, local acts and more: the [plan](PLAN.md) lists every part, with its progress.

**Scope**
- Rebuilt Romanian law from the official texts as one git history: the Constitution, the codes and tens of thousands of laws, ordinances and Government decisions.
- Linked Constitutional Court and High Court rulings to the articles they concern, and added the European Court of Human Rights' judgments against Romania and the EU Court of Justice's decisions concerning Romania.
- Added the EU regulations and directives in force, in their Romanian Official Journal text.

**Use**
- The official portal shows one version of an act at a time, so tracing how a provision changed, or what it said on a given date, means comparing versions by hand. Here it is one `git log` or `git blame`.
- The whole history can be searched, compared and reused: the texts are official, and our work on them is in the public domain (CC0).

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/effort-dark.svg">
<img alt="Romanian law in this repository: acts, changes as commits, article files, court rulings, official texts read and years of history; changes by the year they took effect; and the plan by part, published and collected" src="data/effort-light.svg" width="880">
</picture>

### See it in use: the Romania MCP

https://github.com/user-attachments/assets/3f47ad88-f514-4765-97e3-ff67ed8f79b4

An AI assistant answering a question about Romanian law through the MCP: the answer cites the exact article and version in this repository, with the official links.

## Layout

| Where | What |
| --- | --- |
| `constitutie/1991/` | the Constitution |
| `lege/<year>/<number>/` | laws, including the codes adopted by law (Codul civil is `lege/2009/287/`) |
| `oug/<year>/<number>/` | Government emergency ordinances (Codul administrativ is `oug/2019/57/`) |
| `og/<year>/<number>/` · `hg/<year>/<number>/` | Government ordinances · Government decisions |
| `<act>/art-NNN.md` | one article per file, one paragraph, letter or point per line; art. 112^1 is `art-112-1.md` |
| `<act>/README.md` | the act's articles, versions and any decisions made by hand for it |
| `ue/<kind>/<year>/<number>/` | EU regulations and directives in force, in their Romanian Official Journal text (`ue/regulament/2016/679/` is the GDPR) |
| `anexa/<act id>/<annex>/` | official annexes held apart from their act: court circumscriptions, small-claims and legal-aid forms |
| `profesii/<body>/...` | the legal professions' own rules (statutes, codes of ethics, regulations, decisions): UNBR, INPPA, OCJR, UNEJ, Consiliul de Mediere, CAFR; CSM, INM and UNPIR as metadata |
| `jurisprudenta/` | court decisions: `ccr/`, `iccj/<panel>/`, `cedo/`, `cjue/` (Court of Justice of the EU) |
| [ACTS.md](ACTS.md) | the primary legislation (Constitution, laws, ordinances, decrees, codes), with folder, status and span; every other kind is listed by year in `data/acts/<kind>/<year>.md` (local acts: `data/acts/local/<council>/<year>.md`) |
| `data/` | `acts.json`, `versions.json` and `laws.csv` for the primary legislation, the same files for every other kind under `data/acts/`, `data/versions/` and `data/laws/` (one per kind and year, all listed in `data/index.json`), `paths.json` and the CSV tables below |
| `tools/` | `on.py` and `in_vigoare_la.py` (the law on any date); `tools/build/` holds the builder |
| [AGENTS.md](AGENTS.md) | how a program or an AI agent should query this repository |

Each act also has a short id (`codul-civil`, `legea-31-1990`) used by the tools and tags. Folders were named by id until November 2026; `git log` on one file needs `--follow` across that move.

## Use it

| Question | Command |
| --- | --- |
| What did art. 1112 of the Codul civil say on 18 October 2014? | `python tools/on.py 2014-10-18 lege/2009/287 1112` |
| The whole act on a date | `python tools/on.py 2000-01-01 constitutie/1991` |
| Which act wrote each paragraph of art. 336 of the Codul penal? | `git blame lege/2009/286/art-336.md` |
| Every change to an article, word by word | `git log --follow -p --word-diff lege/2009/286/art-297.md` |
| Everything one act changed | `git show law/legea-200-2023` |
| An act as it stood from a day | `git show codul-penal/2023-07-09` (tags `<id>/<in-force day>`) |

Read dates with the tools, not `git rev-list --before`: they pick each version by its `In-force:` trailer.

## Data tables

| File | What |
| --- | --- |
| `data/index.json` | every act list: the primary files (`acts.json`, `versions.json`, `laws.csv`) and one shard per other kind and year, e.g. `data/acts/hg/2016.json`, `data/versions/ordin/2012.json`, `data/laws/local/bucuresti/cgmb/2016.csv`; `data/sources/<kind>/<year>.csv` lists the sources of those acts (REPRODUCE.md lists the rest) |
| `data/act-links.csv` | links between acts (amends, repeals, approves, promulgates, republishes…) from the Chamber of Deputies' database, captured 2018–2025; not official, and not complete for later links |
| `data/eu-transposition.csv` | the EU acts each Romanian act transposes, from Romania's notifications to the Commission (`nim`), the act's own note (`clause`) or both; `eu_folder` is the EU act's folder under `ue/`, once it is here |
| `data/decisions.csv`, `data/rulings-by-provision.json` | every court decision here, and the decisions on each article |
| `data/promulgation.csv` | the decree that promulgated each law |
| `data/treaty-links.csv` | treaties and the acts that ratify them |
| `data/rectifications.csv` | rectifications in the Monitorul Oficial and the acts they correct |
| `data/mo-issues.csv` | an index of Monitorul Oficial issues |
| `data/local-taxes.csv` | local councils' decisions on local taxes, by locality and year |

Practical tables, each row citing the provision it comes from (information, not legal advice):

| File | What |
| --- | --- |
| `data/court-jurisdiction.csv`, `data/court-localities.csv` | the judecătorie, tribunal, court of appeal and prosecutor's offices for every municipiu, oraș, comună, Bucharest sector and village (SIRUTA code); HG nr. 1.217/2023, Legea nr. 304/2022 |
| `data/courts.csv` | every court: seat, county, parent courts |
| `data/court-fees.csv` | taxa judiciară de timbru, one row per provision (OUG nr. 80/2013) |
| `data/monetary-thresholds.csv` | competence limit, small-claims ceiling, bail brackets, fines, legal-interest formulas |
| `data/minimum-wage.csv`, `data/legal-interest.csv` | the minimum gross wage since 1991; legal interest by period since 2011 (BNR rate, OG nr. 13/2011) |
| `data/procedural-deadlines.csv` | appeal, recurs, prescription, administrative, contravention, labour and criminal deadlines |
| `data/legal-aid-rules.csv`, `data/legal-aid-services.csv` | who qualifies for ajutor public judiciar (OUG nr. 51/2008) and the bar service beside each judecătorie |
| `data/forms-index.csv` | official forms (small claims, EU procedures, tax forms) and the acts approving them |

## Case law

All 23,743 decisions are here, as published in the Monitorul Oficial, Part I: 21,561 of the Constitutional Court (from 1992), 1,863 binding decisions of the High Court of Cassation and Justice (RIL and HP, from 1998) and 319 European Court of Human Rights judgments against Romania. Each folder holds the text and `meta.json`. Each decision is one commit of kind `ruling`, tagged `ruling/<id>`; a ruling changes no act file, and a Constitutional Court decision that changed a text is a separate commit of kind `court` in that act's history. Parties' names are as the Monitorul Oficial prints them. The portal holds about 85% of the Constitutional Court's yearly totals in recent years.

`jurisprudenta/cjue/` holds 568 decisions of the Court of Justice of the EU and the General Court concerning Romania (preliminary references from Romanian courts, actions by or against Romania; 574 found in CELLAR): the operative part (`dispozitiv.md`) and `meta.json`, with the referring court and the EU acts interpreted. Full texts name the parties' lawyers, so they are linked, not copied.

## Dates, authors and limits

- Each commit is dated on the day the change took effect, by each act's own clause or the default rule (Constituția art. 78: three days after publication). The author is the act that made the change; the committer is Lexifina.
- A change is credited to an act only when the portal's amendment note names it; changes no note explains are labelled "unexplained". Judgement calls are recorded in each act's `README.md` and listed in `REPRODUCE.md`.
- Each act's latest version is the newest consolidated form held, so later amendments may be missing. Acts marked `amended, not consolidated` hold only the act as published; their `README.md` names the amending acts.
- Only the Monitorul Oficial, Part I is authoritative (for EU acts, the Official Journal of the EU); no consolidated text, ours included, has legal force.
- Not included: chapter and section headings, the portal's editorial notes, and annexes or figures printed as facsimiles or in a separate issue.

## How it is built and checked

Every version names the page it was read from and that page's sha256. Every version of every act is read back from git on the day it took effect and the day before (`tools/build/check_repo.py`) and must match the corpus; `main` has no merge commits, dates never go backwards, and a rebuild gives identical hashes. Results are in `REPRODUCE.md`.

## Sources

| Source | Used for |
| --- | --- |
| [Portalul legislativ](https://legislatie.just.ro), Ministerul Justiției | the official texts, every consolidated form and the amendment notes |
| – | archived copies of the portal's pages, each capture pinned per version |
| [legalize-ro](https://github.com/legalize-dev/legalize-ro) | a check of the Codul fiscal's text |
| [Camera Deputaților](https://www.cdep.ro), legislation database | `data/act-links.csv` |
| [EU Publications Office](https://op.europa.eu) (CELLAR) | the Romanian texts in `ue/` and the decisions in `jurisprudenta/cjue/` (© European Union, https://eur-lex.europa.eu; Commission Decision 2011/833/EU, CC BY 4.0); `data/eu-transposition.csv` (CC0) |
| The professional bodies' own sites (unbr.ro, inppa.ro, ocjr.ro, executori.ro, consiliuldemediere.ro, cafr.ro) | the texts in `profesii/` (official texts, Legea nr. 8/1996, art. 9 lit. b) |
| [INS SIRUTA](https://data.gov.ro) and the [BNR](https://www.bnr.ro) rate table | locality codes in the court tables; `data/legal-interest.csv` |

## Licence

The legal texts are official texts of Romanian normative acts (Sursa: Portalul legislativ al Ministerului Justiției, https://legislatie.just.ro), excluded from copyright by Legea nr. 8/1996, art. 9 lit. b. The EU texts in `ue/` and `jurisprudenta/cjue/` are © European Union, reused under Commission Decision 2011/833/EU. Lexifina's arrangement, tables, commit messages and tools are in the public domain (CC0), as set out in `LICENSE`. This repository is not legal advice and not an official publication.

## În limba română

Istoria dreptului românesc în git: un fișier pentru fiecare articol și un commit pentru fiecare modificare, datat în ziua intrării ei în vigoare și semnat de actul care a făcut-o. Lista actelor este în [ACTS.md](ACTS.md); textul în vigoare la o dată: `python tools/on.py 2014-10-18 lege/2009/287 1112`. Sursa: Portalul legislativ al Ministerului Justiției (legislatie.just.ro). Niciun model de inteligență artificială nu a scris text juridic.
