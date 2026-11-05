# For programs and AI agents

How to query this repository without reading it all. Everything here is plain git plus two standard-library Python tools; nothing needs network access.

## Find an act

- `data/acts.json`: one row per act of the primary legislation with `slug` (the act id), `path` (its folder), `kind` (`constitutie`, `lege`, `oug`, `og`, `decret`, `decret-lege`, `hotarare-parlament`, `cod`), `year`, `number`, `title`, `code` (the code's name, if it is one), `status` (`in force`, `repealed <day>`, `amending act`), `versions`, `from`, `latest` and `portal` (the source page).
- Every other kind (`hg`, the orders such as `ordin`, `local` and the rest) has the same rows in shards, one file per kind and year: `data/acts/hg/2016.json`, `data/acts/ordin/2012.json`; local acts per council and year, `data/acts/local/bucuresti/cgmb/2016.json`. `data/index.json` lists every shard (`shards[].acts`, `.versions`, `.laws`, `.list`); for the whole list read `data/acts.json` and every shard. `data/versions.json` and `data/laws.csv` are split the same way (`data/versions/<kind>/<year>.json`, `data/laws/<kind>/<year>.csv`), and the sources of a shard's acts are in `data/sources/<kind>/<year>.csv` (REPRODUCE.md lists the others).
- The folder is the official identifier: Legea nr. 31/1990 is `lege/1990/31/`, OUG nr. 195/2002 `oug/2002/195/`, HG nr. 10/2016 `hg/2016/10/`. A code lives under its own act: Codul civil `lege/2009/287/`, Codul administrativ `oug/2019/57/`, the Constitution `constitutie/1991/`.
- `data/paths.json` maps every act id to its folder, every kind included (it is not split).
- [ACTS.md](ACTS.md) is the same list for people; each shard's list is beside its JSON (`data/acts/hg/2016.md`).

## Read the law on a day

    python tools/in_vigoare_la.py 2014-10-18 codul-civil 1112   # one article, by act id and article number
    python tools/on.py 2014-10-18 lege/2009/287 1112            # the same, by folder
    python tools/on.py 2014-10-18 codul-civil                   # the whole act
    python tools/on.py --law 2014-10-18 codul-civil 1112        # and the act behind that wording

The tools choose each version by the commit's `In-force:` trailer, never by commit date. Use them rather than `git rev-list --before`: acts added after the first build carry their publish time as commit date, so a date query on commit dates misses them.

## Read history

- One article per file (`art-NNN.md`, an inserted article 112^1 is `art-112-1.md`), one paragraph, letter or point per line.
- `git blame <folder>/art-NNN.md` names, line by line, the act that wrote it (the commit author).
- `git log --follow -p --word-diff <folder>/art-NNN.md` gives every change, word by word.
- Tags: `<act id>/<in-force day>` is the act as it stood from that day; `law/<key>` is the commit of the act `<key>`; `ruling/<id>` is the commit that added the decision `<id>` (`ruling/dcc-623-2019`). A Constitutional Court decision that changed a text has both: `law/dcc-<n>-<year>` on the text change, `ruling/dcc-<n>-<year>` on the decision.
- Commit trailers (all ASCII, parse with `git interpret-trailers --parse`):
  - `In-force:`, the day the change took effect;
  - `Kind:`: `law` (a law), `decree` (an ordinance or Government decision), `court` (a change to an act's text made
    by a Constitutional Court decision: the article struck out or conditioned), `ruling` (a court decision itself,
    added under `jurisprudenta/`; it changes no act's text), `publisher` (a change no amendment note explains),
    `layout` (the folder move) or `correction` (see below);
  - `Corrects:` and `Re-asserts:`, on a correction, the earlier commit it replaces for its day;
  - `Law:`, the act's key, as in `law/<key>` tags;
  - `Enacted:` and `Published:`;
  - `Act:` and `Provisions:` (or `Affecting:`), the act and provisions changed;
  - `Words-changed:`;
  - `Consolidated:` and `Source:`, the source pages of that version.

## Find a court decision

- `jurisprudenta/ccr/<year>/<number>/` (Constitutional Court), `jurisprudenta/iccj/<panel>/<year>/<number>/` (High Court of Cassation and Justice; panels `ril`, `hp`, `hp-penal`, `su`, `scaf`), `jurisprudenta/cedo/<year>/<application>/` (European Court of Human Rights). Each holds the text as published (`decizie.md`, or `hotarare.md` for an ECHR judgment), one paragraph per line, and `meta.json`. A 1993–1995 plenary decision is `ccr/<year>/plen-<n>/`; ÎCCJ United Sections numbers printed in Roman numerals are given in digits (`su/2007/22/` is Decizia nr. XXII/2007).
- `meta.json`: `key` (the id: `dcc-623-2019`, `iccj-ril-13-2023`, `iccj-hp-penal-8-2015`, `cedo-3594-19-2020-05-05`), `number`, `date` (of the decision), `mo` (Monitorul Oficial number and date), `binding_from`, `kind` and `subkind` (CCR: `exceptie`, `a-priori`, `alta`; ÎCCJ: `RIL`, `HP`, `alta`), `panel`, `outcome` (`admitted`, `rejected`, `other`; ECHR: `violation`, `no-violation`, `inadmissible`, `struck-out`, `friendly-settlement`), `finds_unconstitutional`, `interpretive`, `rejected_as` (`neintemeiata`, `inadmisibila`, `devenita-inadmisibila`, `fara-obiect`), `operative` (the operative part, one item per paragraph), `subjects` (the acts and articles it rules on, read from its title and operative part, not its reasoning; the Constitution is the standard, not a subject), `cites` (every act its text cites, with counts), `source` (the page and the text's sha256) and `warnings` (where a rule could not read a field). These fields are read by rules, not by hand.
- A code is resolved by name and date: "Codul penal" in a decision of 2010 is `lege/1968/15`, in 2015 `lege/2009/286`.
- `data/decisions.json` (and `.csv`) has one row per decision on main. `data/rulings-by-provision.json` maps an act's folder (`lege/2009/287`) and article (`2526`, `112-1` for art. 112^1) to the ids of the decisions on it; `jurisprudenta/acte/<act folder>.md` is the same for people.
- Commits of kind `ruling` carry `Law:`, `Kind: ruling`, `Court:` (`ccr`, `iccj`, `cedo`), `Ruling-kind:`, `Panel:`, `Outcome:`, `Enacted:` (the day of the decision), `Published:` (the Monitorul Oficial day), `In-force:` (the day it binds: the publication day, or the day of the judgment for the ECHR), `Monitorul-Oficial:`, `Rules-on:` (one per act ruled on), `Ceases-unless-amended:` (a Constitutional Court finding on a law or ordinance in force: publication plus 45 days, Constituția art. 147(1)), `Application:` (ECHR), `Source:` and `Text-sha256:`. The author is the court, at the decision's id (`Curtea Constituțională <dcc-623-2019@legislatie.invalid>`), dated on the publication day.
- `tools/on.py` never reads a `ruling` commit: it takes an act's text only from commits that touch the act's folder. To see what a decision did to a text, follow its id: `git log --author=dcc-638-2018` lists the decision and the `court` commit that struck the words.

## The layout move (November 2026)

One commit labelled `Kind: layout` renamed every act folder from its id (`codul-civil/`) to its official identifier (`lege/2009/287/`). No text changed.
- Commits before it use the old folder names.
- `git blame` follows the move by itself.
- `git log` on a single file needs `--follow`, or both paths.
- `tools/on.py` and `tools/build/check_repo.py` read both folders.
- Tools outside this repository that take paths should map paths through `data/paths.json` for days before the move.

## Withdrawn acts and retired ids

An act that turns out not to belong here (for example, an act titled as a Government decision but issued by another body) is removed by a correction commit (`Kind: correction`, one `Withdraws: <id>` trailer per act). The commits that added it stay in the history, and so do its tags, which are never moved or deleted. ACTS.md and `data/acts.json` (or the kind's shard and its list) show it under "Withdrawn", with the reason and the removing commit. Its id is retired: a later act with the same official number gets the id with `-2` appended (`hg-10-2021-2`, tags `hg-10-2021-2/<day>`). Its folder is still the official identifier (`hg/2021/10/`).

## Corrected text

History is never rewritten. When a version was published with the wrong text (for example, a republished text dated as the act as enacted), the fix is appended as a block of `Kind: correction` commits for that act:
- The first carries the official text, with `In-force:` set to the day it took effect and `Corrects: <commit>` naming the commit that served the wrong text.
- Each later version follows again, oldest first. It is marked `Corrects: <commit>` if its text was wrong too, or `Re-asserts: <commit>` if it was right but must be restated.

The rule for reading a day stays the same: take the newest commit that touches the act's folder with `In-force:` on or before the day. Every day from the corrected one on then reads the corrected history, and earlier days read the original commits. `tools/on.py` and `tools/build/check_repo.py` follow this rule. The `<act id>/<day>` tags made before a correction are never moved, so they still show the text as first published.

When only the credit was wrong (the words are right, but a change was credited to the wrong law, or to none), nothing is restated. A `Kind: correction` commit with `Credits: <n>` and `Corrects: <commit>` trailers and no `In-force:` trailer (so no reader ever takes text from it) does two things:
- it adds one row per provision and day to `data/credits.csv` (`act,in_force,provision,law,was_law,was_commit`);
- it lists the corrected credits in the act's README.md, under "Credits corrected".

`git blame` still names the commit that wrote the words, and `tools/on.py --law` gives the corrected law. To credit a change, take the commit's author, unless `data/credits.csv` has a row for that act, day and provision; if it has several, the last one counts.

## What is not here

- Annexes, chapter and section headings.
- Figures, signs, pictograms and annexes that the Monitorul Oficial printed as facsimiles or in a separate issue; an article that refers to one keeps that reference.
- The portal's editorial notes.
- Court decisions other than the Constitutional Court's, the High Court of Cassation and Justice's binding decisions and the ECHR judgments published in the Monitorul Oficial. Those are in `jurisprudenta/` and change no act file.
- Forms newer than the newest archived capture.

Each act's README.md lists its articles and the decisions made by hand for that act. REPRODUCE.md says how the repository was built and checked.
