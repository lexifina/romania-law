# Data, freshness and sources

The tables, files and sources behind this repository. The [README](README.md) has the short version.

## Act lists and indexes

| File | What |
| --- | --- |
| `data/index.json` | every act list: the primary files (`acts.json`, `versions.json`, `laws.csv`) and one shard per other kind and year, e.g. `data/acts/hg/2016.json`, `data/versions/ordin/2012.json`, `data/laws/local/bucuresti/cgmb/2016.csv`; `data/sources/<kind>/<year>.csv` lists the sources of those acts (REPRODUCE.md lists the rest) |
| `data/paths.json` | every act id mapped to its folder |
| [ACTS.md](ACTS.md) | the primary legislation, with folder, status and span; every other kind is listed by year in `data/acts/<kind>/<year>.md` |

## Links between acts and legislative history

| File | What |
| --- | --- |
| `data/act-links-<year>.csv` | links between acts (amends, repeals, approves, promulgates, republishes…), one file per year of the act that acts; `evidence` says where each link is stated: the Chamber of Deputies' sheets, the act's own official title, the bill file or the promulgation record. Not official, and a missing link does not mean no change |
| `data/bills-<year>.csv` | the bill behind each law since 1996 and the bills still in Parliament: chamber numbers, initiator, adoption dates, votes, Constitutional Court referral, promulgation decree, and links to the opinions and texts; not official |
| `data/bill-initiators-<year>.csv` | the members of Parliament who initiated each bill |
| `data/bill-documents.csv` | the documents linked from each bill file: opinions, explanatory memorandum, the text sent for promulgation |
| `data/promulgation.csv` | the decree that promulgated each law |
| `data/eu-transposition.csv` | the EU acts each Romanian act transposes (`nim`: Romania's notifications; `clause`: the act's own note); `eu_folder` is the EU act's folder under `ue/` |
| `data/treaty-links.csv` | treaties and the acts that ratify them |
| `data/rectifications.csv` | rectifications in the Monitorul Oficial and the acts they correct |
| `data/mo-issues.csv` | an index of Monitorul Oficial issues |
| `data/local-taxes.csv` | local councils' decisions on local taxes, by locality and year |

## Court decisions

| File | What |
| --- | --- |
| `data/decisions.csv`, `data/rulings-by-provision.json` | every court decision here, and the decisions on each article |
| `data/court-notes.csv` | Constitutional Court findings noted on an act but not applied to its text (only some words, a reading, or a decision before the 2003 revision) |
| `data/echr-romania.csv` | ECHR judgments and decisions against Romania transmitted for execution, with HUDOC and HUDOC-EXEC links |

## Practical tables

Each row cites the provision it comes from. Information, not legal advice.

| File | What |
| --- | --- |
| `data/court-jurisdiction.csv`, `data/court-localities.csv` | the judecătorie, tribunal, court of appeal and prosecutor's offices for every municipiu, oraș, comună, Bucharest sector and village (SIRUTA code) |
| `data/courts.csv` | every court: seat, county, parent courts |
| `data/court-fees.csv` | taxa judiciară de timbru (OUG nr. 80/2013) |
| `data/monetary-thresholds.csv` | competence limit, small-claims ceiling, bail brackets, fines, legal-interest formulas |
| `data/minimum-wage.csv`, `data/legal-interest.csv` | the minimum gross wage since 1991; legal interest since 2011 |
| `data/procedural-deadlines.csv` | appeal, recurs, prescription, administrative, contravention, labour and criminal deadlines |
| `data/legal-aid-rules.csv`, `data/legal-aid-services.csv` | who qualifies for ajutor public judiciar, and the bar service beside each judecătorie |
| `data/forms-index.csv` | official forms and the acts approving them |

## Freshness

`data/freshness.json` (the summary) and `data/freshness/` (one row per act, sharded like the act lists; `data/freshness/index.json` lists the files) record, for each act, the last day a check of the official source confirmed that the version here is still the newest, how it was checked, and any change the source reports that is not here yet.

| Status | Meaning |
| --- | --- |
| `current` | checked within its threshold, and no known change is missing |
| `pending-change` | the official source reports a change not here yet: an amendment, a repeal, a newer EU consolidated version or an end of validity |
| `stale` | last checked longer ago than its threshold |
| `unverified` | never checked for later changes |
| `source-unavailable` | due for a check, but the official source is not answering |

The threshold is 7 days for the Constitution, codes, laws, ordinances, decrees and Government decisions, and 30 days for everything else. A repealed act has none; court decisions do not change once published and have no rows. `tools/freshness.py` works offline from these files: to be certain, open the official link it prints.

## Update status

`data/status.json` is refreshed every hour:

| Field | Meaning |
| --- | --- |
| `updates` | `running` while new versions are being published |
| `last_published` | when the newest commit reached this repository |
| `published_last_24h` | commits and new acts published in the last 24 hours |
| `official_sources` | each official source's state (`available`, `unavailable`), since when, and the last successful contact |

Source states are as seen from the pipeline: a source marked unavailable did not answer it, and may still be up for you.

## Sources

| Source | Used for |
| --- | --- |
| [Portalul legislativ](https://legislatie.just.ro), Ministerul Justiției | the official texts, every consolidated form and the amendment notes |
| – | archived copies of the portal's pages, each capture pinned per version |
| [legalize-ro](https://github.com/legalize-dev/legalize-ro) | a check of the Codul fiscal's text |
| [Camera Deputaților](https://www.cdep.ro) and the [Senate](https://www.senat.ro) | act links, bill files and initiators |
| [EU Publications Office](https://op.europa.eu) (CELLAR) | the texts in `ue/` and the decisions in `jurisprudenta/cjue/` (© European Union, https://eur-lex.europa.eu; Commission Decision 2011/833/EU, CC BY 4.0); `data/eu-transposition.csv` (CC0) |
| The professional bodies' own sites | the texts in `profesii/` |
| The authorities' own sites (BNR, ASF, ANRE, ANCOM, CNA and others) | regulator acts, checked against the official texts |
| [INS SIRUTA](https://data.gov.ro) and the [BNR](https://www.bnr.ro) rate table | locality codes in the court tables; `data/legal-interest.csv` |
| [HUDOC-EXEC](https://hudoc.exec.coe.int), Council of Europe | `data/echr-romania.csv` and the metadata-only ECHR entries |
