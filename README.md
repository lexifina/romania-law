# Romania: law history in git

The law of Romania as a git history: one file per article, one commit per law on the day it took effect, and the act that made each change as the commit's author. `git blame` names the act behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ro/`. The texts are in Romanian, as published.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitutia/` | Constituția României | 2 | The 1991 text (in force on its approval by referendum, 8 December 1991) and the text revised by Legea nr. 429/2003 (in force 29 October 2003). It has not been amended since. |
| `codul-civil/` | Codul civil (Legea nr. 287/2009) | 13 | The 2009 text and, the same day, the republished text in force from 1 October 2011, then every consolidated form to 3 May 2026 |
| `codul-penal/` | Codul penal (Legea nr. 286/2009) | 45 | The 2009 text and, the same day, the text in force from 1 February 2014, then every consolidated form to 26 April 2026 |
| `codul-procedura-civila/` | Codul de procedură civilă (Legea nr. 134/2010) | 28 | The 2010 text and, the same day, the republished text in force from 15 February 2013, then every consolidated form to 14 December 2025, including the 2015 republication |
| `codul-procedura-penala/` | Codul de procedură penală (Legea nr. 135/2010) | 61 | The 2010 text and, the same day, the text in force from 1 February 2014, then every consolidated form to 13 June 2026 (one form, 2 March 2017, has no text on the portal) |
| `codul-muncii/` | Codul muncii (Legea nr. 53/2003) | 61 | The 2003 text in force from 1 March 2003, then every consolidated form to 18 December 2025, including the 2011 republication with renumbered articles |
| `legea-190-2018/` | Legea nr. 190/2018 (GDPR implementation) | 2 | The 2018 text in force from 31 July 2018 and its only consolidated form, 1 December 2019 (Legea nr. 233/2019) |
| `legea-31-1990/` | Legea societăților nr. 31/1990 (company law) | 43 | The 1990 text in force from 17 December 1990, then every consolidated form to 18 December 2025, including the republications of 1998 and 2004 with renumbered articles. The portal has no form between 4 June 1991 and the 1998 republication. |
| `codul-fiscal/` | Codul fiscal (Legea nr. 227/2015) | 149 | The 2015 text in force from 1 January 2016, then every consolidated form to 8 August 2026; four forms of 2026 have no text we could read, so their changes appear with the next form |
| `codul-administrativ/` | Codul administrativ (OUG nr. 57/2019) | 46 | The 2019 text in force from 5 July 2019 (without its annexes), then every consolidated form to 30 March 2026 |
| `legea-554-2004/` | Legea contenciosului administrativ nr. 554/2004 | 20 | The 2004 text in force from 6 January 2005, then every consolidated form to 10 July 2025, including the changes made by Constitutional Court decisions |

Every version is one of the Portalul legislativ's own consolidated forms ("forme consolidate"). The per-act `README.md` in each folder lists every article, how often it changed and when.

**Not yet current to the day.** The newest forms held are those of 3 May 2026 (Codul civil), 26 April 2026 (Codul penal), 14 December 2025 (Codul de procedură civilă), 13 June 2026 (Codul de procedură penală), 18 December 2025 (Codul muncii and Legea nr. 31/1990), 1 December 2019 (Legea nr. 190/2018), 8 August 2026 (Codul fiscal), 30 March 2026 (Codul administrativ) and 10 July 2025 (Legea nr. 554/2004). Each act's latest version is the newest form we hold; amendments that took effect after it may be missing.

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
- **The procedure codes** were enacted in 2010 and amended before they took effect: the Codul de procedură civilă by Legea nr. 76/2012, which ordered its republication and set 15 February 2013 as its first day; the Codul de procedură penală mainly by Legea nr. 255/2013, from 1 February 2014. As with the 2009 codes, the first commit is the 2010 text, dated the day the code took effect, and the amendments follow the same day.
- **The Codul muncii** took effect on 1 March 2003 (its art. 298 alin. (1)). **Legea nr. 190/2018** took effect on 31 July 2018, 5 days after publication (its art. 16). **Legea nr. 31/1990** took effect on 17 December 1990, 30 days after publication (its art. 221). **The Codul fiscal** took effect on 1 January 2016 (its art. 501), save where it provides otherwise. **Legea nr. 554/2004** took effect on 6 January 2005, 30 days after publication (its art. 31). **The Codul administrativ** took effect on publication, 5 July 2019 (its art. 597 alin. (1)); the provisions it starts later are shown from that day too, and its annexes are not included.
- **Changes printed early.** The Codul administrativ's form of 30 October 2023 already prints changes to arts. 63 and 390 whose notes put them in force on 1 November 2023; they are dated 1 November 2023.
- **Changes between two forms.** Where a Codul fiscal note dates a change to a day for which the portal has no form of its own (for example 1 April 2019, carried by the form of 20 April 2019), the change is dated by the note, with the later form's text for the articles it names.
- **Republications** without a form of their own: the Codul de procedură civilă republished on 10 April 2015 (under art. XIV of Legea nr. 138/2014) and the Codul muncii republished on 18 May 2011 (under art. V of Legea nr. 40/2011, renumbering its articles) are read from the republished text as printed (the portal's DetaliiDocumentAfis page), since their own pages show the newest form. Their changes are credited to the act that ordered the republication, except where an article note names another act.
- **Gaps.** The Codul de procedură penală's form of 2 March 2017 has no text on the portal, so its changes appear with the form of 3 March 2017. Legea nr. 31/1990 has no form between 4 June 1991 and its republication of 29 January 1998, so the changes of those years appear together that day, uncredited (several acts made them). The Codul fiscal's forms of 25 February, 16 April, 8 May and 1 July 2026 are missing, so their changes appear with the next form held.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version of every act is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match the corpus. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with git.
- Against the official text: the newest version of each act is the portal's newest consolidated form, parsed article by article. The Civil Code's form of 3 May 2026 was read from two separate captures (pages 109884 and 130143) and they agree in all 2,674 articles. The newest form of each of the four later acts was also read from a second, separate capture of the act's page, and agrees article by article (1,143, 641, 297 and 16 articles), as do Legea nr. 31/1990 (467 articles) and Legea nr. 554/2004 (32 articles). For the Codul administrativ the newest form that has a second capture is that of 28 July 2025, and it agrees with the corpus on that day in all 674 articles. The Codul fiscal's newest form was held in one capture only; instead its version in force on 1 March 2026 was compared with that form as reproduced in legalize-ro (github.com/legalize-dev/legalize-ro, public domain), and 632 of 636 articles agree line for line; the other four differ only in how numbered points and tables are laid out there. Every version carries the capture URL and the sha256 of the page it was parsed from.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the act that made the change, with an e-mail address that cannot exist (`legea-200-2023@legislatie.invalid`), so `git blame` and `git log --author` name acts. The committer is always Lexifina.

- **Credits come only from the portal's amendment notes** on the changed article, which name the amending act (law, government emergency ordinance, Constitutional Court decision or rectification). Older forms print the same notes without a date; there a note counts when it is new on the article.
- **Constitutional Court decisions** are commits of kind "court": where the portal changed the text because a decision took effect (art. 147 of the Constitution: 45 days after publication unless Parliament acts), the change is credited to the decision, from the article's note. Decisions that left the words unchanged are not shown.
- **Whole-text changes.** The 2003 republication of the Constitution and the 2011 republication of the Civil Code are credited to the act that ordered them (Legea nr. 429/2003, Legea nr. 71/2011), as the portal's note on each republished text does, except where an article note names another act; so is the 2004 republication of Legea nr. 31/1990 (Legea nr. 161/2003).
- **Unexplained changes** are committed by the publisher, the Portalul legislativ, and labelled "unexplained": ten diacritic corrections in the Codul penal on 20 May 2014 ("amendă" to "amenda" and the like), one in the Codul civil ("1)" to "(1)", art. 253, 3 October 2018), and two changes of paragraph breaks only (Codul penal arts. 194 and 378). In the later acts most are the portal's own typesetting, made and undone between forms: the Codul muncii's form of 22 April 2007 drops every diacritic (271 articles) until the 2011 republication restores them, and the Codul de procedură civilă's forms of 2013-2014 change words such as "străinătate"/"străînătate" and "comunică"/"comunica" back and forth. Legea nr. 31/1990's forms of 2001-2005 drop and restore diacritics in most articles, and the Codul fiscal's tables are typeset differently from form to form. The portal's own editorial paragraphs inside an article (on Constitutional Court rulings or rectifications) are left out of the later acts' text. Articles that disappear with no note (repealed provisions the portal stopped printing) are unexplained too. REPRODUCE.md lists every one.
- Blame credits whole lines (one paragraph per line). In an article written by several acts, use `git log -p --word-diff` to see exactly which words each act changed.

## What it does not show

- **Amendments after mid-2026**, as above.
- **Editorial notes** (the portal's "Notă" boxes, which quote decisions of the Constitutional Court and the High Court and transitional provisions of amending laws) and the amendment notes themselves are not in the text. From its form of 3 February 2019 the portal prints two High Court holdings on art. 6 as paragraphs of Codul penal art. 183; they are left out.
- **Rulings that only interpret.** High Court rulings (HP, RIL) and Constitutional Court decisions that left the wording unchanged are not commits.
- **Chapter and section headings.** Only articles are files; the books, titles, chapters and sections are not.
- **Portal notes printed as text.** Some forms print an editorial note as a black paragraph inside an article ("Conform art. XII ... din LEGEA nr. 2 ... publicată în MONITORUL OFICIAL ...", or a note that a Constitutional Court decision ended a provision's effects). In the four later acts these paragraphs are left out (the gazette in capitals marks them; the acts' own text writes "Monitorul Oficial"), and an article that a publisher's note quotes from another act ("Articolul XVII") is not a file.
- **The 2009 Civil Code text's glitches.** On the portal, arts. 1.251, 2.367, 2.374 and 2.655 of the 2009 text are printed outside their article markup; they are given their own files. Art. 2.448 is run into art. 2.447 and is left there.
- **Commencement and applicability conditions** in transitional provisions are in the text, not in the dates; no applicability data is recorded.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions by date | Names the amending act | API or bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Portalul legislativ](https://legislatie.just.ro) · [Web service](https://legislatie.just.ro/ServiciulWebLegislatie.htm) | Official legislation, Ministry of Justice | yes, every consolidated form | yes, a note on each amended provision | SOAP web service | Used, through Internet Archive captures: the portal and its web service closed every connection from our network |
| [Internet Archive](https://web.archive.org) | Web archive | n/a | n/a | – | – |
| – | Web archive | n/a | n/a | index files, WARC byte ranges | Captures of the portal's pages from 40 crawls (2022-2026), used first for the four later acts; WARC file, offset and length pinned per version. |
| [legalize-ro](https://github.com/legalize-dev/legalize-ro) | Reconstructed history (public-domain data) | yes | yes | git | Checked: it holds none of the acts here beyond the Constitution, so not used |
| [romanian-law-data](https://github.com/scriptogre/romanian-law-data) | Datasets | n/a | n/a | Parquet | Daily releases from legislatie.just.ro; not used |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of normative acts of Romania, as published by the Ministry of Justice on the Portalul legislativ. Sursa: Portalul legislativ al Ministerului Justiției, https://legislatie.just.ro. Romanian copyright law excludes official legislative texts from protection (Legea nr. 8/1996, art. 9 lit. b). The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## În limba română

Istoria dreptului românesc în git: un fișier pentru fiecare articol și un commit pentru fiecare act normativ, datat în ziua intrării sale în vigoare și semnat de actul care a făcut modificarea (`git blame` numește actul fiecărui paragraf). Conține Constituția României (textul din 1991 și textul revizuit prin Legea nr. 429/2003, în vigoare de la 29 octombrie 2003), Codul civil (de la 1 octombrie 2011 până la forma consolidată din 3 mai 2026), Codul penal (de la 1 februarie 2014 până la forma consolidată din 26 aprilie 2026), Codul de procedură civilă (de la 15 februarie 2013 până la forma din 14 decembrie 2025), Codul de procedură penală (de la 1 februarie 2014 până la forma din 13 iunie 2026), Codul muncii (de la 1 martie 2003 până la forma din 18 decembrie 2025), Legea nr. 190/2018 (de la 31 iulie 2018; forma din 1 decembrie 2019), Legea societăților nr. 31/1990 (de la 17 decembrie 1990 până la forma din 18 decembrie 2025), Codul fiscal (de la 1 ianuarie 2016 până la forma din 8 august 2026) Codul administrativ (de la 5 iulie 2019 până la forma din 30 martie 2026, fără anexe) și Legea contenciosului administrativ nr. 554/2004 (de la 6 ianuarie 2005 până la forma din 10 iulie 2025).

- Textul în vigoare la o dată: `python tools/in_vigoare_la.py 2014-10-18 codul-civil 1112`
- Datele: cele ale Portalului legislativ (nota „la ZZ-LL-AAAA” de la fiecare prevedere modificată și data fiecărei forme consolidate). Regula generală: art. 78 din Constituție (legea intră în vigoare la 3 zile de la publicarea în Monitorul Oficial sau la data prevăzută în textul ei).
- Autoria: o modificare este atribuită unui act numai dacă nota de modificare a portalului îl numește; ce nu explică nicio notă rămâne „unexplained”, în numele portalului.
- Ultima versiune a fiecărui act este cea mai nouă formă consolidată pe care o avem: modificările intrate în vigoare după aceea pot lipsi.
- Sursa: Portalul legislativ al Ministerului Justiției (legislatie.just.ro). Niciun model de inteligență artificială nu a scris text juridic.
