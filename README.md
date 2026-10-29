# Romania: law history in git

The law of Romania as a git history: one file per article, one commit per law on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ro/`. The texts are in Romanian, as published.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitutia/` | Constituția României | 2 | The 1991 text (in force on its approval by referendum, 8 December 1991) and the text revised by Legea nr. 429/2003 (in force 29 October 2003). It has not been amended since. |
| `codul-civil/` | Codul civil (Legea nr. 287/2009) | 13 | The 2009 text and, the same day, the republished text in force from 1 October 2011, then every consolidated form to 3 May 2026 |
| `codul-penal/` | Codul penal (Legea nr. 286/2009) | 45 | The 2009 text and, the same day, the text in force from 1 February 2014, then every consolidated form to 26 April 2026 |

Every version is one of the Portalul legislativ's own consolidated forms ("forme consolidate"). The per-act `README.md` in each folder lists every article, how often it changed and when.

**Not yet current to the day.** The portal could not be reached from our network, so it was read through Internet Archive captures, the newest from June and July 2026. On those captures the newest forms are those of 3 May 2026 (Codul civil) and 26 April 2026 (Codul penal). Amendments that took effect after the newest capture may be missing.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 1112 of the Codul civil say on 18 October 2014? | `python tools/in_vigoare_la.py 2014-10-18 codul-civil 1112` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2014-10-18T23:59:59Z" main -- codul-civil/art-1112.md):codul-civil/art-1112.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2014-10-18T23:59:59Z" main -- codul-civil/art-1112.md; git show "$($r):codul-civil/art-1112.md"` |
| Which act wrote each paragraph of art. 336 of the Codul penal? | `git blame codul-penal/art-336.md` |
| Every change to art. 297 of the Codul penal, word by word | `git log -p --word-diff codul-penal/art-297.md` |
| Every act in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one act changed | `git show law/legea-200-2023` (tags `law/<key>` mark each act's commit) |
| The whole act on a date | `python tools/in_vigoare_la.py 2000-01-01 constitutia` |
| The act as a consolidated form | `git show codul-penal/2023-07-09` (tags `<act>/<in-force day>`) |

Articles inserted later carry the portal's numbering: art. 112^1 is the file `art-112-1.md` (`in_vigoare_la.py` accepts `112^1`). After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Europe/Bucharest, on the day the change took effect**. Enactment and publication dates are trailers (`Enacted:`, `Published:`); the in-force day is in `In-force:`, which the tools read.
- **The in-force day is the portal's.** Every amended provision carries a note such as "(la 09-07-2023, Alineatul (1), Articolul 297 ... a fost modificat de Punctul 3., Articolul I din LEGEA nr. 200 din 5 iulie 2023 ...)", and each consolidated form is dated by the day its changes took effect. In every form we read, the dated notes on the changes the form adds carry the form's own date.
- **Default rule.** Constituția art. 78: a law is published in the Monitorul Oficial and takes effect 3 days after publication, or on a later date it sets. The portal's dates already apply it and each law's own date.
- **The Constitution** was adopted on 21 November 1991 and took effect on its approval by the national referendum of 8 December 1991. The revision (Legea nr. 429/2003) was approved by the referendum of 18-19 October 2003 and took effect on 29 October 2003; the Legislative Council republished the Constitution with renumbered articles on 31 October 2003 (art. 152 became art. 156). Files follow each text's own numbering, so on 29 October 2003 many articles change and some numbers hold different articles.
- **The codes before they took effect.** Both codes were enacted in 2009 and amended before they took effect (the Civil Code mainly by Legea nr. 71/2011, the Penal Code by Legea nr. 27/2012, 63/2012 and 187/2012). Each code's first commit is the 2009 text, dated the day the code took effect; the next commits, the same day, are the amendments, so the text at the end of that day is the text in force.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version of every act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match the corpus. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with git.
- Against the official text: the newest version of each act is the portal's newest consolidated form, parsed article by article. The Civil Code's form of 3 May 2026 was read from two separate captures (pages 109884 and 130143) and they agree in all 2,674 articles. Every version carries the capture URL and the sha256 of the page it was parsed from.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the act that made the change, with an e-mail address that cannot exist (`legea-200-2023@legislatie.invalid`), so `git blame` and `git log --author` name acts. The committer is always Lexifina.

- **Credits come only from the portal's amendment notes** on the changed article, which name the amending act (law, government emergency ordinance, Constitutional Court decision or rectification). Older forms print the same notes without a date; there a note counts when it is new on the article.
- **Constitutional Court decisions** are commits of kind "court": where the portal changed the text because a decision took effect (art. 147 of the Constitution: 45 days after publication unless Parliament acts), the change is credited to the decision, from the article's note. Decisions that left the words unchanged are not shown.
- **Whole-text changes.** The 2003 republication of the Constitution and the 2011 republication of the Civil Code are credited to the act that ordered them (Legea nr. 429/2003, Legea nr. 71/2011), as the portal's note on each republished text does, except where an article note names another act.
- **Unexplained changes** are committed by the publisher, the Portalul legislativ, and labelled "unexplained": ten diacritic corrections in the Codul penal on 20 May 2014 ("amendă" to "amenda" and the like), one in the Codul civil ("1)" to "(1)", art. 253, 3 October 2018), and two changes of paragraph breaks only (Codul penal arts. 194 and 378).
- Blame credits whole lines (one paragraph per line). In an article written by several acts, use `git log -p --word-diff` to see exactly which words each act changed.

## What it does not show

- **Amendments after mid-2026**, as above.
- **Editorial notes** (the portal's "Notă" boxes, which quote decisions of the Constitutional Court and the High Court and transitional provisions of amending laws) and the amendment notes themselves are not in the text. From its form of 3 February 2019 the portal prints two High Court holdings on art. 6 as paragraphs of Codul penal art. 183; they are left out.
- **Rulings that only interpret.** High Court rulings (HP, RIL) and Constitutional Court decisions that left the wording unchanged are not commits.
- **Chapter and section headings.** Only articles are files; the books, titles, chapters and sections are not.
- **The 2009 Civil Code text's glitches.** On the portal, arts. 1.251, 2.367, 2.374 and 2.655 of the 2009 text are printed outside their article markup; they are given their own files. Art. 2.448 is run into art. 2.447 and is left there.
- **Commencement and applicability conditions** in transitional provisions are in the text, not in the dates; no applicability data is recorded.

## How it is built

`tools/fetch.py` reads every page once through the shared Internet Archive client (one adaptive rate for the machine, every response cached by the sha256 of its URL), `tools/parse.py` turns the cache into the corpus, and the shared builder `tools/build.py` writes the history with `git fast-import`. The same corpus always gives the same hashes. `REPRODUCE.md` records every command, tool version, data hash and decision, and the result of a hash-for-hash rebuild.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions by date | Names the amending act | API or bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Portalul legislativ](https://legislatie.just.ro) · [Web service](https://legislatie.just.ro/ServiciulWebLegislatie.htm) | Official legislation, Ministry of Justice | yes, every consolidated form | yes, a note on each amended provision | SOAP web service | Used, through Internet Archive captures: the portal and its web service closed every connection from our network |
| [Internet Archive](https://web.archive.org) | Web archive | n/a | n/a | CDX API | `id_` raw captures of the portal's pages; capture timestamps pinned per version |
| [romanian-law-data](https://github.com/scriptogre/romanian-law-data) | Datasets | n/a | n/a | Parquet | Daily releases from legislatie.just.ro; not used |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of normative acts of Romania, as published by the Ministry of Justice on the Portalul legislativ. Sursa: Portalul legislativ al Ministerului Justiției, https://legislatie.just.ro. Romanian copyright law excludes official legislative texts from protection (Legea nr. 8/1996, art. 9 lit. b). The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## În limba română

Istoria dreptului românesc în git: un fișier pentru fiecare articol și un commit pentru fiecare act normativ, datat în ziua intrării sale în vigoare și semnat de actul care a făcut modificarea (`git blame` numește actul fiecărui paragraf). Conține Constituția României (textul din 1991 și textul revizuit prin Legea nr. 429/2003, în vigoare de la 29 octombrie 2003), Codul civil (de la 1 octombrie 2011 până la forma consolidată din 3 mai 2026) și Codul penal (de la 1 februarie 2014 până la forma consolidată din 26 aprilie 2026).

- Textul în vigoare la o dată: `python tools/in_vigoare_la.py 2014-10-18 codul-civil 1112`
- Datele: cele ale Portalului legislativ (nota „la ZZ-LL-AAAA” de la fiecare prevedere modificată și data fiecărei forme consolidate). Regula generală: art. 78 din Constituție (legea intră în vigoare la 3 zile de la publicarea în Monitorul Oficial sau la data prevăzută în textul ei).
- Autoria: o modificare este atribuită unui act numai dacă nota de modificare a portalului îl numește; ce nu explică nicio notă rămâne „unexplained”, în numele portalului.
- Capturile cele mai noi sunt din iunie și iulie 2026: modificările intrate în vigoare după aceea pot lipsi.
- Sursa: Portalul legislativ al Ministerului Justiției (legislatie.just.ro), citit prin capturile Internet Archive. Niciun model de inteligență artificială nu a scris text juridic.
