"""Grow a published git-for-law history append-only: new acts and newer versions go on top; nothing is rewritten.

    python -X utf8 append.py <scripts/<slug>-law> --repo <clone of the published repo> --docs-date YYYY-MM-DD

The clone's main must equal origin/main. What main already holds is read from git itself: for each act, the newest
In-force day it carries, and that the text in force on that day equals the corpus version. Then:

- an act main does not hold yet is appended as one block: its first version, then one commit per law per in-force day,
  in in-force order;
- a version of an act main already holds, in force after the newest one there, is appended as a change, as the full
  build would make it;
- a version in force on or before the newest one there that main lacks (a back-filled form), or a version whose text
  differs from main (a correction), stops the run: those need a labelled correction commit, decided by hand;
- versions in force after --docs-date are left for a later run (they are appended when their day comes).

Author date: noon local time on the in-force day, as in the full build. Committer date: the published head's committer
time plus one second per appended commit, so committer dates never go backwards and the same head and corpus always
give the same hashes. Tags that already exist are never moved; new ones are added. A documentation commit is appended
last (README, REPRODUCE.md, data/), never replacing the earlier one. The result is pushed with a plain `git push`.

Readers choose versions by the In-force trailer (tools/on.py, tools/check_repo.py), so an appended block reads the same
as a full build does.
"""
import argparse
import csv
import hashlib
import io
import json
import marshal
import re
import os
import subprocess
import sys
import tempfile
import time
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build as B  # noqa: E402
import check_repo as K  # noqa: E402
import layout as L  # noqa: E402


def git(repo: Path, *args: str) -> str:
    return B.git(repo, *args)


# ---------------------------------------------------------------- reading the corpus in little memory (2026-11-05)
# At ~100,000 acts, build.load() held every part three times over (the part cache, the joined corpus bytes and every
# provision's text) and an append peaked at ~7 GB. Most acts are trusted (their part is unchanged since the last
# verified publish, GITLAW_TRUSTED_ACTS), and for them an append only writes tables. So load_corpus() reads the same
# parts as build.load(), merged the same way, but keeps a trusted act's provisions without their words: each text
# becomes its git blob id (LeanText), which compares equal exactly when the words do, and is all the tables use. A
# trusted act that turns out to need its words (a version that came due) has its part read again in full
# (reload_parts). The corpus bytes are hashed while they are read, never joined.


class LeanText(str):
    """A provision's text kept only as its git blob id (plus the final newline the schema asks of every text): equal
    to another exactly when the words are equal. Writing it anywhere fails loudly instead of publishing a hash."""
    __slots__ = ()

    def encode(self, *a, **k):
        raise B.CorpusError('internal: a provision read without its words (LeanText) was about to be written')


class RawCorpus:
    """Stands in for build.load()'s corpus bytes, which the documentation only hashes (sha256) and counts: the same
    digest and length, taken while the parts are read."""

    def __init__(self):
        self.sha = hashlib.sha256()
        self.size = 0

    def add(self, b: bytes):
        self.sha.update(b)
        self.size += len(b)

    def __len__(self):
        return self.size


class _Hashlib:
    """build.py's `hashlib`, answering sha256(<RawCorpus>) from the digest taken while reading."""

    def __getattr__(self, name):
        return getattr(hashlib, name)

    def sha256(self, data=b'', **kw):
        return data.sha.copy() if isinstance(data, RawCorpus) else hashlib.sha256(data, **kw)


B.hashlib = _Hashlib()


class PartChanged(Exception):
    """A part read again in full no longer has the bytes read at the start: the run starts over."""


def cache_prefix(folder: Path) -> str | None:
    """build.PartCache's file prefix (GITLAW_PART_CACHE, default in the temp folder), or None when it is off ('0')."""
    env = os.environ.get('GITLAW_PART_CACHE')
    if env == '0':
        return None
    key = str(folder.resolve())
    return env or str(Path(tempfile.gettempdir()) / f'lawrepo-cache-{hashlib.sha1(key.encode()).hexdigest()[:12]}')


class PartStore:
    """Every part's bytes in one file, <prefix>-parts.pack, indexed by <prefix>-parts.idx ({name: (size, mtime, offset,
    crc32)}): a run reads it with one seek per part instead of opening ~100,000 files, and holds one part at a time
    (build.PartCache holds them all, ~2 GB). An entry is used only while the part's size and modification time are as
    recorded and its bytes match their CRC; otherwise the part file is read and appended to the pack. One writer at a
    time (<prefix>-parts.lock); the index is replaced only after the pack is on disk, so a power cut leaves the old
    index, and a bad entry is only a re-read. Nothing in it is published."""

    def __init__(self, prefix: str | None):
        self.idx: dict[str, tuple[int, int, int, int]] = {}
        self.end = 0
        self.rf = self.wf = None
        self.locked = self.dirty = False
        self.listed: set[str] | None = None  # the folder's parts, as load_corpus listed them
        if prefix is None:
            return
        self.pack, self.idx_path, self.lock = (Path(f'{prefix}-parts.{x}') for x in ('pack', 'idx', 'lock'))
        try:
            if self.lock.exists() and time.time() - self.lock.stat().st_mtime > 3600:  # left by a run that died
                self.lock.unlink()
            os.close(os.open(self.lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
            self.locked = True
        except OSError:
            pass  # another run writes it: read what is there, write nothing
        try:
            d = marshal.loads(self.idx_path.read_bytes())
            if isinstance(d, dict) and d.get('v') == 1 and self.pack.stat().st_size >= d['end']:
                self.idx, self.end = d['parts'], d['end']
                self.rf = open(self.pack, 'rb')
        except (OSError, ValueError, EOFError, TypeError, KeyError):
            self.idx, self.end = {}, 0

    def has(self, name: str, st: tuple[int, int]) -> bool:
        e = self.idx.get(name)
        return bool(e) and (e[0], e[1]) == st

    def get(self, name: str, st: tuple[int, int]) -> bytes | None:
        if not self.has(name, st):
            return None
        e = self.idx[name]
        self.rf.seek(e[2])
        b = self.rf.read(e[0])
        return b if len(b) == e[0] and zlib.crc32(b) == e[3] else None

    def put(self, name: str, st: tuple[int, int], b: bytes):
        if not self.locked or len(b) != st[0]:  # rewritten between the listing and the read: not kept
            return
        if self.wf is None:
            self.wf = open(self.pack, 'r+b' if self.end and self.pack.exists() else 'wb')
            self.wf.seek(self.end)
        self.wf.write(b)
        self.idx[name] = (st[0], st[1], self.end, zlib.crc32(b))
        self.end += len(b)
        self.dirty = True

    def close(self):
        """Write the index (entries for parts still in the folder), compacting the pack once over half of it is dead."""
        if self.rf:
            self.rf.close()
        if not self.locked:
            return
        try:
            if self.wf:  # the pack's new bytes reach the disk before an index names them
                self.wf.flush()
                os.fsync(self.wf.fileno())
                self.wf.close()
            gone = set(self.idx) - self.listed if self.listed is not None else set()
            for n in gone:
                del self.idx[n]
            if not (self.dirty or gone):
                return
            live = sum(e[0] for e in self.idx.values())
            if self.end - live > max(live // 2, 256_000_000):
                new, idx, off = Path(f'{self.pack}.new'), {}, 0
                with open(self.pack, 'rb') as src, open(new, 'wb') as dst:
                    for n, e in sorted(self.idx.items()):
                        src.seek(e[2])
                        b = src.read(e[0])
                        if len(b) == e[0] and zlib.crc32(b) == e[3]:
                            dst.write(b)
                            idx[n] = (e[0], e[1], off, e[3])
                            off += e[0]
                    dst.flush()
                    os.fsync(dst.fileno())
                os.replace(new, self.pack)
                self.idx, self.end = idx, off
            tmp = Path(f'{self.idx_path}.{os.getpid()}.tmp')
            with open(tmp, 'wb') as f:
                f.write(marshal.dumps({'v': 1, 'end': self.end, 'parts': self.idx}))
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, self.idx_path)
        except OSError:
            pass  # only a cache: the next run reads the files again
        finally:
            if self.wf:
                self.wf.close()
            self.rf = self.wf = None
            self.lock.unlink(missing_ok=True)
            self.locked = False


def _read_part(p: Path) -> bytes:
    try:
        return p.read_bytes()
    except FileNotFoundError:  # renamed or removed since the listing: list the folder again
        raise PartChanged(p.stem) from None


def _part_bytes(parts: list[Path], stat: dict[str, tuple[int, int]], store: PartStore):
    """(path, bytes) for each part in order: from the store when it holds the part as listed (or its entry is damaged),
    else from the file, then kept in the store."""
    for p in parts:
        b = store.get(p.name, stat[p.name])
        if b is None:
            b = _read_part(p)
            store.put(p.name, stat[p.name], b)
        yield p, b


def _expand(acts: list[dict]) -> None:
    """build.load(): a version given as `changes` (or with no `units`) gets the full units of the version before it."""
    for act in acts:
        for prev, v in zip(act.get('versions', []), act.get('versions', [])[1:]):
            if 'units' in v:
                continue
            units = dict(prev['units'])
            for k, u in (v.get('changes') or {}).items():
                if u is None:
                    units.pop(k, None)
                else:
                    units[k] = u
            v['units'] = units


def _lean(act: dict) -> None:
    """Replace every provision's text in the act's versions (and their `changes`) by its LeanText. A text the schema
    would refuse (no final newline, a \\r, not a string) is kept, so validate() reports it exactly as before. One lean
    unit per unit object, so versions keep sharing them as build.load() made them."""
    memo: dict[int, dict] = {}

    def lu(u):
        if not isinstance(u, dict):
            return u
        r = memo.get(id(u))
        if r is None:
            t = u.get('text')
            r = {**u, 'text': LeanText(K.blob_oid(t) + '\n')} if (
                type(t) is str and t.endswith('\n') and '\r' not in t) else u
            memo[id(u)] = r
        return r
    for v in act.get('versions', []):
        for field in ('units', 'changes'):
            if isinstance(v.get(field), dict):
                v[field] = {k: lu(u) for k, u in v[field].items()}


def _shared(o, strs: dict, done: dict):
    """o rebuilt with one copy of each string value and key (json.loads makes new ones for every part: ~8 million
    strings for ~1.7 million values at 100,000 parts). An object met twice (a unit shared by versions) stays shared."""
    t = type(o)
    if t is str:
        return strs.setdefault(o, o)
    if t is dict or t is list:
        r = done.get(id(o))
        if r is None:
            if t is dict:
                r = {strs.setdefault(k, k) if type(k) is str else k: _shared(v, strs, done) for k, v in o.items()}
            else:
                r = [_shared(v, strs, done) for v in o]
            done[id(o)] = r
        return r
    return o


def _merge_part(c: dict, name: str, stem: str, part: dict) -> None:
    """build.load()'s merge of one part into the corpus."""
    if not c.get('country') and part.get('country'):
        c['country'] = part['country']
    for key, law in part.get('laws', {}).items():
        have = c.setdefault('laws', {}).get(key)
        if have and have.get('label') != law.get('label'):
            raise B.CorpusError(f'{name}: law {key!r} is {law.get("label")!r} here but {have.get("label")!r} elsewhere')
        c['laws'].setdefault(key, law)
    for a in part.get('acts', []):
        a['_decisions'] = list(part.get('decisions', []))
        a['_part'] = stem
    for s in part.get('sources', []):
        s['_acts'] = [a['slug'] for a in part.get('acts', [])]
    for field in ('acts', 'sources', 'applies', 'decisions', 'ai_use'):
        c.setdefault(field, []).extend(part.get(field, []))


def load_corpus(folder: Path, lean: set[str], store: PartStore | None = None
                ) -> tuple[dict, RawCorpus, dict[str, tuple[str, bytes]]]:
    """build.load() (the same parts, in the same order, merged the same way, the same corpus digest), with the acts in
    `lean` kept without their words. Also {part stem: (path, sha1 of the bytes read)}, for reload_parts()."""
    store = store or PartStore(None)
    main_path = folder / 'corpus.json'
    stat: dict[str, tuple[int, int]] = {}
    names: set[str] = set()
    if (folder / 'corpus.d').exists():
        for e in os.scandir(folder / 'corpus.d'):
            names.add(e.name)
            if e.name.endswith('.json') and e.is_file():
                st = e.stat()
                stat[e.name] = (st.st_size, st.st_mtime_ns)
    parts = [folder / 'corpus.d' / n for n in sorted(stat)]
    if os.environ.get('GITLAW_VERIFIED_PARTS_ONLY') == '1':
        parts = [p for p in parts if f'{p.stem}.PUBLISH' in names]
    held = {s.strip() for s in os.environ.get('GITLAW_EXCLUDE_PARTS', '').split(',') if s.strip()}
    parts = [p for p in parts if p.stem not in held]
    only = os.environ.get('GITLAW_ONLY_PARTS')
    if only:
        keep = set(Path(only).read_text(encoding='utf-8').split())
        parts = [p for p in parts if p.stem in keep]
    if not main_path.exists() and not parts:
        raise B.CorpusError(f'{folder} has no corpus.json')
    head = main_path.read_bytes() if main_path.exists() else b''
    c = json.loads(head.decode('utf-8')) if head else {}
    raw = RawCorpus()
    raw.add(head)
    court_acts = B.court_effect_acts(folder)  # always read with their words: court-effects.json edits their text
    _expand(c.get('acts', []))
    for a in c.get('acts', []):
        if a.get('slug') in lean and a.get('slug') not in court_acts:
            _lean(a)
    strs: dict[str, str] = {}
    c = _shared(c, strs, {})
    read: dict[str, tuple[str, bytes]] = {}
    store.listed = set(stat)  # what close() keeps entries for
    for p, b in _part_bytes(parts, stat, store):
        raw.add(b'\n' + p.name.encode() + b'\n')
        raw.add(b)
        read[p.stem] = (str(p), hashlib.sha1(b).digest())
        part = json.loads(b.decode('utf-8'))
        del b
        _expand(part.get('acts', []))
        for a in part.get('acts', []):
            if a.get('slug') in lean and a.get('slug') not in court_acts:
                _lean(a)
        _merge_part(c, p.name, p.stem, _shared(part, strs, {}))
    B.apply_court_effects(c, folder)
    return c, raw, read


def reload_parts(c: dict, slugs: set[str], read: dict[str, tuple[str, bytes]]) -> None:
    """Give the acts in `slugs` (read without their words) their full versions, from their parts read again; a part
    whose bytes changed since load_corpus() read it raises PartChanged."""
    stems = sorted({a['_part'] for a in c['acts'] if a['slug'] in slugs})
    full: dict[str, list] = {}
    for stem in stems:
        p, digest = read[stem]
        b = _read_part(Path(p))
        if hashlib.sha1(b).digest() != digest:
            raise PartChanged(stem)
        acts = json.loads(b.decode('utf-8')).get('acts', [])
        _expand(acts)
        full.update({a['slug']: a['versions'] for a in acts if a.get('slug') in slugs})
    for a in c['acts']:
        if a['slug'] in slugs:
            a['versions'] = full[a['slug']]  # the same part bytes: every other field is as loaded


def needs_words(act: dict, last: str | None, docs_date: str) -> bool:
    """Whether to_append() takes any version of the act: new on main, or a version after its newest one there."""
    vs = [v for v in act['versions'] if v['from'] <= docs_date]
    return bool(vs) if last is None else any(v['from'] > last for v in vs)


def commits_by_act(repo: Path, branch: str, dirs: dict[str, list[str]]) -> dict[str, list[tuple[str, str]]]:
    """check_repo.all_commits_by_act(), reading git's output as it comes instead of holding all of it (the whole
    history's file names, hundreds of MB) at once. Same records, parsed the same way."""
    want = {d: a for a, ds in dirs.items() for d in ds}
    rows: dict[str, list[tuple[str, str]]] = {a: [] for a in dirs}

    def take(rec: str):
        head, _, names = rec.partition('\n')
        h, _, d = head.partition('\t')
        d = d.strip()
        if not d:
            return
        hit = set()
        for name in names.splitlines():
            parts = name.split('/')
            for i in range(1, len(parts) + 1):
                p = '/'.join(parts[:i])
                if p in want:
                    hit.add(want[p])
        for a in hit:
            rows[a].append((h, d))
    p = subprocess.Popen(['git', 'log', '--no-merges', '--no-renames', '--name-only',
                          '--format=%x00%H%x09%(trailers:key=In-force,valueonly,separator=)', branch], cwd=repo,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    buf: list[str] = []
    started = False
    for line in p.stdout:
        while '\x00' in line:  # a record starts after each NUL
            before, _, line = line.partition('\x00')
            buf.append(before)
            if started:
                take(''.join(buf))
            started, buf = True, []
        buf.append(line)
    if started:
        take(''.join(buf))
    err = p.stderr.read()
    if p.wait():
        raise subprocess.CalledProcessError(p.returncode, p.args, None, err)
    return rows


class NotesCache:
    """build.public_note()'s cache (build.PartCache.current answers it), kept small in a file of its own,
    <prefix>-notes.marshal: build.PartCache keeps every note and its result beside every part's bytes (~2 GB, which
    append no longer reads), ~0.7 GB in memory at ~700,000 notes. Here a note is known by a 16-byte digest of its key;
    most notes publish unchanged and keep only that digest, the rest their published text. Reused only by the same
    build.py (build.CODE), like build.PartCache's notes."""

    def __init__(self, path: Path | None):
        self.path = path
        self.same: set[bytes] = set()
        self.changed: dict[bytes, str] = {}
        self.used: set[bytes] = set()
        self.dirty = False
        try:
            d = marshal.loads(path.read_bytes()) if path else None
            if isinstance(d, dict) and d.get('v') == 2 and d.get('code') == B.CODE:
                self.same, self.changed = set(d['same']), dict(d['changed'])
        except (OSError, ValueError, EOFError, TypeError, KeyError):
            pass

    @staticmethod
    def digest(key) -> bytes:
        s, keep = key
        h = hashlib.blake2b(s.encode('utf-8', 'surrogatepass'), digest_size=16)
        for k in sorted(keep):
            h.update(b'\0' + k.encode('utf-8', 'surrogatepass'))
        return h.digest()

    def note(self, key, make):
        d = self.digest(key)
        self.used.add(d)
        if d in self.same:
            return key[0]
        r = self.changed.get(d)
        if r is None:
            r = make()
            if r == key[0]:
                self.same.add(d)
            else:
                self.changed[d] = r
            self.dirty = True
        return r

    def save(self):
        """Write the cache when it gained notes: those used, when the documentation was made (it uses every note still
        current), else all. Atomic; a failure only costs recomputing them later."""
        if not self.path or not self.dirty:
            return
        same, changed = self.same, self.changed
        if self.used:
            same = same & self.used
            changed = {d: r for d, r in changed.items() if d in self.used}
        tmp = self.path.with_name(f'{self.path.name}.{os.getpid()}.tmp')
        try:
            tmp.write_bytes(marshal.dumps({'v': 2, 'code': B.CODE, 'same': same, 'changed': changed}))
            os.replace(tmp, self.path)
        except OSError:
            pass
        self.dirty = False


def open_notes_cache(folder: Path) -> NotesCache:
    prefix = cache_prefix(folder)
    nc = NotesCache(Path(f'{prefix}-notes.marshal') if prefix else None)
    B.PartCache.current = nc  # build.public_note() asks PartCache.current.note()
    return nc


def published_state(repo: Path, c: dict, trusted: set[str] | None = None) -> tuple[dict[str, str], dict[str, tuple[str, list[str]]], dict, dict]:
    """{act slug: newest In-force day on main} for every act main holds, and the acts whose published text differs
    from the corpus on some day main covers: {slug: (first such day, messages)}. Also the per-act commit rows and
    folders, for a correction."""
    # Each act's folder now (assigned from data/paths.json or its official identifier, so an act missing from
    # paths.json is still found), then its folder before the layout move.
    dirs = {a['slug']: list(dict.fromkeys([a.get('path') or a['slug'], a['slug']])) for a in c['acts']}
    rows = commits_by_act(repo, 'main', dirs)
    cat = K.Cat(repo)
    trees: dict = {}
    state = {}
    problems: dict[str, tuple[str, list[str]]] = {}
    for act in c['acts']:
        # No history found, yet files in its folder: appending it as new would write its first version over a later
        # text. Never; hold it (or refuse) for a look by hand.
        # (A folder holding only a README.md, which a documentation commit wrote, has no text: it doesn't count.)
        if not rows[act['slug']] and act.get('path') and act['versions'] and K.tree_oids(cat, 'main', act['path'], {}):
            problems[act['slug']] = (act['versions'][0]['from'], [
                f'{act["slug"]}: its folder {act["path"]} is on main but no commit with In-force touches it '
                '(an index lost the act?); not appended as new'])
    trusted = trusted_acts() if trusted is None else trusted
    try:
        for act in c['acts']:
            r = rows[act['slug']]
            if not r:
                continue
            last = max(d for _, d in r)
            state[act['slug']] = last
            if act['slug'] in trusted:
                continue
            # On every day that starts a version, in the corpus or on main, up to `last`, main must serve the corpus's
            # text (else: correction or back-fill). Main's own days matter too: a repeal main dates too early is a day
            # only main has, on which the corpus still has the earlier text in force.
            for day in version_days(act, r, last):
                v = in_force_on(act, day)
                h = K.state_on(r, day)
                files = K.tree_oids(cat, h, dirs[act['slug']], trees) if h else {}
                want = {f'{k}.md': K.blob_oid(u['text']) for k, u in v['units'].items()} if v else {}
                # a commit leaving the folder with no provision file serves nothing (an order re-dated later)
                if files != want or (v is None and h is not None and files) or (v is not None and h is None):
                    bad = sorted(f for f in set(files) | set(want) if files.get(f) != want.get(f))
                    first, msgs = problems.get(act['slug'], (day, []))
                    problems[act['slug']] = (min(first, day), msgs)
                    msgs.append(f'{act["slug"]} {day}: main differs from the corpus in {len(bad)} file(s), '
                                f'e.g. {bad[:3]} (a correction or a back-filled form: decide by hand)')
    finally:
        cat.close()
    return state, problems, rows, dirs


def trusted_acts() -> set[str]:
    """Acts whose part file is unchanged since the last verified publish (listed by the caller) need no re-reading:
    main only grows, so their published text can't have moved. Everything else is read back in full. An act listed for
    correction is always read back: trust from a stale record would skip the very difference the correction is for
    (codul-procedura-civila-1865, 2026-11-02)."""
    trusted_path = os.environ.get('GITLAW_TRUSTED_ACTS')
    trusted = set(Path(trusted_path).read_text(encoding='utf-8').split()) if trusted_path and Path(trusted_path).exists() else set()
    return trusted - set(approved_corrections())


def in_force_on(act: dict, day: str) -> dict | None:
    """The corpus version in force on `day` (the last one of the latest day on or before it), or None before the first."""
    hit = None
    for v in act['versions']:
        if v['from'] > day:
            break
        hit = v
    return hit


def version_days(act: dict, rows: list, last: str) -> list[str]:
    """Every day on or before `last` that starts a version in the corpus or on main (main's In-force days)."""
    return sorted({v['from'] for v in act['versions'] if v['from'] <= last} | {d for _, d in rows if d <= last})


def absent_acts(repo: Path, head: str, listed: set[str], known_paths: dict[str, str], c: dict):
    """Acts main holds that this publish's corpus does not: withdrawn ones (a "Withdraws: <id>" trailer) and ones whose
    part is held back this cycle. Returns (index entries, their versions.json rows, recovered {id: folder})."""
    def versions_at(ref: str) -> dict[str, dict]:
        # data/versions.json and, since 2026-11-05, its shards (listed in data/index.json)
        try:
            return {a['slug']: a for a in B.index_rows(repo, ref, 'versions') or []}
        except (ValueError, subprocess.CalledProcessError):
            return {}
    rows_for = {s: a for s, a in versions_at(head).items() if s not in listed}
    # Withdrawn: the trailer names the act; the "- <id>: <reason>" lines of the same commit give the reason.
    withdrawn: dict[str, tuple[str, str]] = {}
    for rec in git(repo, 'log', '--format=%x1e%h%x1f%B', '--grep=^Withdraws:', head).split('\x1e')[1:]:
        h, _, body = rec.partition('\x1f')
        lines = [ln.strip() for ln in body.splitlines()]
        reasons = {m.group(1): m.group(2) for m in (re.match(r'^- ([a-z0-9-]+): (.+)$', ln) for ln in lines) if m}
        for m in (re.match(r'^Withdraws:\s*([a-z0-9-]+)\s*$', ln) for ln in lines):
            if m and m.group(1) not in withdrawn:
                withdrawn[m.group(1)] = (h.strip(), reasons.get(m.group(1), ''))
                if m.group(1) not in rows_for and m.group(1) not in listed:  # its row from just before the withdrawal
                    row = versions_at(f'{h.strip()}^').get(m.group(1))
                    if row:
                        rows_for[m.group(1)] = row
    # Folders on main that no index names (an earlier publish dropped them): the act is recovered from the last
    # paths.json that had the folder, and its row from the versions.json of the same commit.
    path_for: dict[str, str] = {}
    have = set(known_paths.values()) | {a['path'] for a in c['acts'] if a.get('path')}
    folders = {f[:-len('/README.md')] for f in git(repo, 'ls-tree', '-r', '--name-only', head).splitlines()
               if f.endswith('/README.md') and f.split('/')[0] not in ('tools', 'data')}
    # An order's annex folder (ordin/<issuer>/<year>/<nr>/anexa-<n>/README.md) is part of its act's folder, not an act:
    # a README under a known act folder is never looked up as a lost act (2026-11-04).
    folders = {f for f in folders if not any('/'.join(f.split('/')[:i]) in have for i in range(1, f.count('/') + 1))}
    for f in sorted(folders - have):
        if '/' not in f and f in rows_for:  # a folder still named by its id (an act from before the layout move)
            continue
        hits = git(repo, 'log', '--format=%H', f'-S"{f}"', head, '--', 'data/paths.json').split()
        for h in hits:  # newest first: the commit that dropped it; its parent still names it
            old = L.paths_at(repo, f'{h}^')
            s = next((k for k, v in old.items() if v == f), None)
            if s:
                path_for[s] = f
                if s not in listed and s not in rows_for:
                    row = versions_at(f'{h}^').get(s)
                    if row:
                        rows_for[s] = row
                break
        else:
            print(f'append: folder {f} on main is in no index, and no paths.json ever named it', file=sys.stderr)
    extra = []
    for s, a in sorted(rows_for.items()):
        if s in withdrawn:
            extra.append({**a, '_withdrawn': True, 'path': None, '_withdrawn_by': withdrawn[s][0],
                          '_reason': withdrawn[s][1] or 'not in the current record'})
        else:  # held back from this publish: listed as it stands on main
            p = known_paths.get(s) or path_for.get(s) or a.get('path')
            extra.append({**a, 'path': p})
            rows_for[s] = {**a, 'path': p}
    return extra, rows_for, path_for


CREDIT_COLUMNS = ['act', 'in_force', 'provision', 'law', 'was_law', 'was_commit']


def credit_ledger(repo: Path, ref: str) -> list[dict]:
    """data/credits.csv on ref: every credit corrected so far, oldest first ([] before the first)."""
    out = subprocess.run(['git', 'show', f'{ref}:data/credits.csv'], cwd=repo, capture_output=True, text=True,
                         encoding='utf-8')
    return list(csv.DictReader(io.StringIO(out.stdout))) if not out.returncode and out.stdout else []


def main_credits(repo: Path, c: dict, acts: list[dict]) -> dict[str, dict[tuple[str, str], tuple[str, str]]]:
    """{act: {(in-force day, provision): (law key or '', commit)}} as main credits each change, for several acts from
    one history walk. A law commit is authored at the law's own address (<key>@<publisher domain>, build.law_email);
    a publisher or correction commit credits no law."""
    if not acts:
        return {}
    key_of = {B.law_email(c, k).lower(): k for k in c['laws']}
    owner = {f: a['slug'] for a in acts for f in dict.fromkeys([a.get('path') or a['slug'], a['slug']])}
    out = git(repo, 'log', '--no-merges', '--reverse', '--name-only',
              '--format=%x00%H%x09%(trailers:key=In-force,valueonly,separator=)%x09%(trailers:key=Kind,valueonly,'
              'separator=)%x09%ae', 'main', '--', *owner)
    have: dict[str, dict] = {a['slug']: {} for a in acts}
    for rec in out.split('\x00')[1:]:
        head, _, names = rec.partition('\n')
        h, d, kind, email = (head.split('\t') + ['', '', ''])[:4]
        d, kind, law = d.strip(), kind.strip(), key_of.get(email.strip().lower(), '')
        if not d or kind == 'layout':
            continue
        for name in names.splitlines():
            if not name.endswith('.md') or name.endswith('/README.md'):
                continue
            folder = name.rsplit('/', 1)[0]
            while folder and folder not in owner:  # a provision in a sub-folder of its act
                folder = folder.rsplit('/', 1)[0] if '/' in folder else ''
            if folder:
                have[owner[folder]][(d, name[len(folder) + 1:-3])] = ('' if kind == 'correction' else law, h)
    return have


def credit_fixes(repo: Path, c: dict, act: dict, last: str, ledger: list[dict],
                 have: dict[tuple[str, str], tuple[str, str]] | None = None) -> list[dict]:
    """Provisions whose change on a published day main credits to a different law (or to none) than the corpus now
    does, when the words are the same. Main's credit for (day, provision) is the Law trailer of the last commit with
    that In-force day that wrote the provision (none for a publisher commit or a text correction), overridden by the
    ledger; the corpus's is what build.plan would credit (the latest law named for it). Versions after `last` are
    appended as usual and need no correction."""
    have = dict(have if have is not None else main_credits(repo, c, [act])[act['slug']])
    for r in ledger:
        if r['act'] == act['slug']:
            have[(r['in_force'], r['provision'])] = (r['law'], have.get((r['in_force'], r['provision']), ('', ''))[1])
    want: dict[tuple[str, str], str] = {}
    for prev, cur in zip(act['versions'], act['versions'][1:]):
        if cur['from'] > last:
            break
        credits = cur.get('credits', {})
        for k in set(prev['units']) | set(cur['units']):
            if prev['units'].get(k, {}).get('text') != cur['units'].get(k, {}).get('text'):
                ls = sorted(set(credits.get(k, [])), key=lambda l: B.law_order(c['laws'], l))
                want[(cur['from'], k)] = ls[-1] if ls else ''
    return [{'act': act['slug'], 'in_force': d, 'provision': k, 'law': law, 'was_law': have[(d, k)][0],
             'was_commit': have[(d, k)][1]}
            for (d, k), law in sorted(want.items()) if (d, k) in have and have[(d, k)][0] != law]


def approved_corrections() -> dict[str, str]:
    """{act slug: public reason} from the file GITLAW_CORRECTIONS names (JSON). Only these acts are corrected; a
    listed act whose published text already matches the corpus needs nothing, so the list can stay in place."""
    p = os.environ.get('GITLAW_CORRECTIONS')
    if not p or not Path(p).exists():
        return {}
    return {k: str(v) for k, v in json.loads(Path(p).read_text(encoding='utf-8')).items()}


def correction_block(repo: Path, c: dict, act: dict, first_day: str, last: str, rows: list, reason: str) -> list[dict]:
    """The commits that correct one act append-only, from `first_day` (the first day main's text differs) to `last`
    (main's newest day for the act). Readers take the newest commit, in log order, that touches the act's folder with
    In-force on or before their day. So the block restates every version from `first_day` on, oldest first: the
    corrected one, then each later one again, so every day from `first_day` reads the corrected history; days before
    it still read the original commits. Nothing published is rewritten."""
    vs = act['versions']
    # (In-force day, the corpus text in force from it): the first wrong day with whatever version is in force then
    # (it may have started earlier: a repeal main dated too early leaves the earlier text in force on main's day),
    # then each later version day up to `last`, a day's last version being its text.
    start = in_force_on(act, first_day)
    if start is None and vs and vs[0]['from'] > first_day and L.issuer_of(act.get('path') or ''):
        return not_yet_block(repo, act, first_day, rows, reason)
    if start is None:
        raise B.CorpusError(f'correction of {act["slug"]}: main has the act in force on {first_day}, before its first '
                            'version in the corpus; a correction can only restate text, so decide by hand')
    days = [(first_day, start)] + [(v['from'], v) for i, v in enumerate(vs) if first_day < v['from'] <= last
                                   and not (i + 1 < len(vs) and vs[i + 1]['from'] == v['from'])]
    path = act.get('path') or act['slug']
    cat = K.Cat(repo)
    try:
        head = git(repo, 'rev-parse', 'main').strip()
        have = K.tree_oids(cat, head, path, {})  # the act's files on main now: {name: blob}
        served = []
        trees: dict = {}
        for day, v in days:
            h = K.state_on(rows, day)
            want = {f'{k}.md': K.blob_oid(u['text']) for k, u in v['units'].items()}
            served.append((h, bool(h) and K.tree_oids(cat, h, [path, act['slug']], trees) == want))
    finally:
        cat.close()
    first = start
    pre = []
    if {f'{k}.md': K.blob_oid(u['text']) for k, u in first['units'].items()} == have and L.issuer_of(path):
        # An order dated too late on main (2026-11-05): its text is right, only its day is not. A commit with no
        # In-force trailer (no reader takes text from it) removes its files, so the next one, In-force: first_day,
        # touches the folder when it writes them back.
        label = act.get('short') or act.get('title') or act['slug']
        pre = [{'day': first_day, 'act': act, 'files': {f'{path}/{n}': None for n in have},
                'message': [f'Correction: {label}, files cleared before it is restated from {first_day}', '',
                            'No reader takes text from this commit (it has no In-force trailer); the next commit '
                            f'writes the same text back with In-force: {first_day}, the day the act came into force.'],
                'trailers': ['Kind: correction', f'Act: {act["slug"]}']}]
        have = {}
    if {f'{k}.md': K.blob_oid(u['text']) for k, u in first['units'].items()} == have:
        # A commit that changes no file under the folder is invisible to the reader rule: the original commits would
        # still be served for the days it should correct.
        raise B.CorpusError(f'correction of {act["slug"]}: the text in force from {first_day} equals the text on main '
                            'now, so no commit can correct it by touching the folder; decide by hand')
    out, prev = [], None
    for (day, v), (h, same) in zip(days, served):
        if prev is None:
            files = {f'{path}/{k}.md': u['text'] for k, u in v['units'].items()}
            files.update({f'{path}/{n}': None for n in have if n[:-3] not in v['units']})
        else:
            files = B.act_files(act, v['units'], prev['units'])
        label = act.get('short') or act.get('title') or act['slug']
        if prev is None:
            since = '' if v['from'] == day else f' (the text in force since {v["from"]}, still in force on this day)'
            msg = [f'Correction: {label} as in force on {day}', '',
                   f'{reason}'.rstrip() + (' ' if reason else '') +
                   f'The text served for this day {"was" if h else "was missing"} '
                   f'{"in commit " + h[:12] if h else "from main"}; this commit carries the official text{since}.']
        else:
            msg = [f'Correction: {label} as in force from {day}, restated', '',
                   f'Restates the text in force from {day} after the correction of {first_day}, so that every '
                   'later day reads the corrected history.' + ('' if same else ' The text served for this day '
                                                                  'differed from the official one as well.')]
        trailers = ['Kind: correction', f'Act: {act["slug"]}', f'In-force: {day}']
        if h:
            trailers.append(f'{"Re-asserts" if same and prev is not None else "Corrects"}: {h}')
        entry = {'day': day, 'act': act, 'files': files, 'message': msg, 'trailers': trailers}
        if v.get('_court') and v['from'] == day:
            # A Constitutional Court finding applied (build.apply_court_effects, 2026-11-06): the first commit is the
            # decision's own (Kind: court, authored by it, tag law/<key>), carrying the act as in force that day; the
            # commits after it restate the later versions with the provision still struck.
            i = act['versions'].index(v)
            x = {'day': day, 'kind': 'law', 'law': v['_court'],
                 'parts': [{'act': act, 'prev': act['versions'][i - 1], 'cur': v, 'keys': sorted(v['credits']),
                            'also': {}, 'named': []}]}
            author, cmsg, ctr = B.change_message(c, x)
            while cmsg and cmsg[-1] == '':
                cmsg.pop()
            cmsg += ['', *B.wrap((
                'Added after the later versions: this commit carries the whole act as in force on this day, and the '
                'commits after it restate each later version with the provision still struck.' if prev is None else
                'Added in order among the restated versions that follow an earlier court ruling on this act.'))]
            entry.update(message=cmsg, trailers=ctr, law=v['_court'], author=author)
        out.append(entry)
        prev = v
    return pre + out



def not_yet_block(repo: Path, act: dict, first_day: str, rows: list, reason: str) -> list[dict]:
    """An order main serves from `first_day`, before the day it comes into force (its in-force clause was first read
    wrongly): one commit removes its provision files with In-force: first_day (so those days read nothing in force),
    then its first version is restated from its own day (2026-11-05)."""
    vs = act['versions']
    path = act.get('path') or act['slug']
    label = act.get('short') or act.get('title') or act['slug']
    cat = K.Cat(repo)
    try:
        have = K.tree_oids(cat, git(repo, 'rev-parse', 'main').strip(), path, {})
    finally:
        cat.close()
    h = K.state_on(rows, first_day)
    v = vs[0]
    out = [{'day': first_day, 'act': act, 'files': {f'{path}/{n}': None for n in have},
            'message': [f'Correction: {label} not yet in force on {first_day}', '',
                        f'{reason}'.rstrip() + (' ' if reason else '') +
                        f'The text served from this day was in commit {(h or "")[:12]}; the act comes into force on '
                        f'{v["from"]}, so its provisions are removed for the days before, and the next commit restates '
                        'them from that day.'],
            'trailers': ['Kind: correction', f'Act: {act["slug"]}', f'In-force: {first_day}'] +
                        ([f'Corrects: {h}'] if h else [])}]
    out.append({'day': v['from'], 'act': act, 'files': {f'{path}/{k}.md': u['text'] for k, u in v['units'].items()},
                'message': [f'Correction: {label} as in force from {v["from"]}', '',
                            f'Restates the text from {v["from"]}, the day it comes into force, after the correction of '
                            f'{first_day}.'],
                'trailers': ['Kind: correction', f'Act: {act["slug"]}', f'In-force: {v["from"]}'] +
                            ([f'Re-asserts: {h}'] if h else [])})
    return out


def to_append(c: dict, state: dict[str, str], docs_date: str) -> tuple[dict, set[str]]:
    """A corpus of only what is new. A held act keeps its newest held version as the base, so the first new version
    is planned as a change from it; that base's own 'start' commit is dropped (main has it)."""
    out = dict(c)
    acts, based = [], set()
    for act in c['acts']:
        vs = [v for v in act['versions'] if v['from'] <= docs_date]
        last = state.get(act['slug'])
        if last is None:
            if vs:
                acts.append({**act, 'versions': vs})
            continue
        held = [v for v in vs if v['from'] <= last]
        new = [v for v in vs if v['from'] > last]
        if new:
            acts.append({**act, 'versions': [held[-1]] + new})
            based.add(act['slug'])
    out['acts'] = acts
    return out, based


def published_log(repo: Path) -> list[dict]:
    text = git(repo, 'show', 'main:data/commits.csv')
    log = []
    for r in csv.DictReader(io.StringIO(text)):
        log.append({'day': r['day'], 'kind': r['kind'], 'law': r['law'] or None, 'acts': r['acts'].split(),
                    'units': int(r['files'] or 0), 'branch': r['branch'], 'clamped': r['day'] < '1970-01-01'})
    return log


def acts_index(c: dict) -> str:
    """ACTS.md: every act in the corpus, grouped by kind, with its version count and span (generated each publish)."""
    groups = [('Codes and the Constitution', lambda s: s.startswith(('codul-', 'constitutia'))),
              ('Laws (legi)', lambda s: s.startswith('legea-')),
              ('Emergency ordinances (OUG)', lambda s: s.startswith('oug-')),
              ('Ordinances (OG)', lambda s: s.startswith('og-')),
              ('Government decisions (HG)', lambda s: s.startswith('hg-'))]
    acts = sorted(c['acts'], key=lambda a: a['slug'])
    seen: set[str] = set()
    out = ['# Every act in this repository', '',
           f'{len(acts)} acts, {sum(len(a["versions"]) for a in acts):,} versions. Generated on every publish from the '
           'corpus; each folder\'s README.md lists its articles. Dates are in-force days.', '']
    for name, test in groups + [('Other acts', lambda s: True)]:
        rows = [a for a in acts if a['slug'] not in seen and test(a['slug'])]
        if not rows:
            continue
        seen |= {a['slug'] for a in rows}
        out += [f'## {name} ({len(rows)})', '', '| Folder | Act | Versions | From | Latest |', '| --- | --- | ---: | --- | --- |']
        for a in rows:
            vs = a['versions']
            title = a.get('title', a['slug']).replace('|', '/')
            out.append(f'| [`{a["slug"]}/`]({a["slug"]}/) | {title} | {len(vs)} | {vs[0]["from"]} | {vs[-1]["from"]} |')
        out.append('')
    return '\n'.join(out)


class Stored:
    """A file whose content Appender.blob() already sent: the commit names it by mark."""
    __slots__ = ('mark',)

    def __init__(self, mark: int):
        self.mark = mark


class Counted:
    """A version's provisions after the documentation tables are made: only how many there are (layout.status asks
    whether there are any). Reading a provision from it fails loudly."""
    __slots__ = ('n',)

    def __init__(self, n: int):
        self.n = n

    def __len__(self):
        return self.n


def drop_words(acts: list[dict]) -> None:
    """Once the documentation tables are made: every version reduced to its day and its number of provisions
    (Counted), all the indexes read of it."""
    for a in acts:
        if 'versions' in a:
            a['versions'] = [{'from': v['from'], **({'units': Counted(len(v['units']))} if 'units' in v else {})}
                             for v in a['versions']]
        a.pop('_decisions', None)  # shown only in the README


# Documentation files written later (split_docs, the batch log) or read again (split_indexes): kept as text.
REWRITTEN = ('ACTS.md', 'REPRODUCE.md', 'data/acts.json', 'data/versions.json', 'data/laws.csv', 'data/paths.json',
             'data/index.json', 'data/appends.csv')


def stream_docs(w: 'Appender', docs: dict) -> None:
    """Send every settled documentation file to fast-import now (Appender.blob), keeping its mark in its place."""
    for p, text in list(docs.items()):
        if isinstance(text, str) and p not in REWRITTEN and not p.startswith(B.SHARD_DIRS):
            docs[p] = w.blob(text)


class Appender:
    """`git fast-import` onto an existing main; separate author and committer dates."""

    def __init__(self, repo: Path, head: str, head_ct: int, head_tz: str, cap: int | None = None):
        self.p = subprocess.Popen(['git', 'fast-import', '--quiet', '--done', '--date-format=raw'], cwd=repo,
                                  stdin=subprocess.PIPE)
        self.mark, self.parent, self.ct, self.tz = 0, head, head_ct, head_tz
        # Never date a commit after `cap` (the publish time): once the batch reaches it, commits share that second
        # (git and check_repo allow equal times; only a time going backwards or into the future is an error).
        self.cap = cap

    def _w(self, b: bytes):
        self.p.stdin.write(b)

    def _data(self, s: str):
        b = s.encode('utf-8')
        self._w(f'data {len(b)}\n'.encode() + b + b'\n')

    def commit(self, author: tuple[str, str], when: str, committer: tuple[str, str], message: str,
               files: dict[str, str | None]) -> int:
        self.mark += 1
        self.ct = self.ct + 1 if self.cap is None else max(self.ct, min(self.ct + 1, self.cap))
        self._w(f'commit refs/heads/main\nmark :{self.mark}\n'.encode())
        self._w(f'author {author[0]} <{author[1]}> {when}\n'.encode('utf-8'))
        self._w(f'committer {committer[0]} <{committer[1]}> {self.ct} {self.tz}\n'.encode('utf-8'))
        self._data(message)
        self._w((f'from {self.parent}\n' if isinstance(self.parent, str) else f'from :{self.parent}\n').encode())
        for path in sorted(files):
            if files[path] is None:
                self._w(f'D {path}\n'.encode('utf-8'))
            elif isinstance(files[path], Stored):
                self._w(f'M 100644 :{files[path].mark} {path}\n'.encode('utf-8'))
            else:
                self._w(f'M 100644 inline {path}\n'.encode('utf-8'))
                self._data(files[path])
        self.parent = self.mark
        return self.mark

    def blob(self, text: str) -> 'Stored':
        """A file's content sent ahead of its commit (fast-import `blob`), so the caller can let the text go."""
        self.mark += 1
        self._w(f'blob\nmark :{self.mark}\n'.encode())
        self._data(text)
        return Stored(self.mark)

    def tag(self, name: str, mark: int):
        self._w(f'reset refs/tags/{name}\nfrom :{mark}\n\n'.encode('utf-8'))

    def finish(self):
        self._w(b'done\n')
        self.p.stdin.close()
        if self.p.wait():
            raise B.CorpusError('git fast-import failed')


def append(folder: Path, repo: Path, docs_date: str, dry_run: bool = False, committer_time: int | None = None,
           refresh_docs: bool = False) -> dict:
    nc = open_notes_cache(folder)
    store = PartStore(cache_prefix(folder))
    try:
        for attempt in range(3):
            try:
                return _append(folder, repo, docs_date, dry_run, committer_time, refresh_docs, store)
            except PartChanged:
                # A trusted part was rewritten while this run read it: read everything again, as one read would have.
                # The part is not named (the caller sets aside a part an error names).
                if attempt == 2:
                    raise B.CorpusError('corpus parts kept changing while append read them; try again') from None
    finally:
        store.close()
        nc.save()


def _append(folder: Path, repo: Path, docs_date: str, dry_run: bool, committer_time: int | None,
            refresh_docs: bool, store: PartStore) -> dict:
    # Trusted acts are read without their words (load_corpus); published_state skips them by the same set.
    trusted = trusted_acts()
    c, raw, part_read = load_corpus(folder, trusted, store)
    errs = B.validate(c)
    if errs:
        raise B.CorpusError('corpus has problems:\n  ' + '\n  '.join(errs[:60]))
    c['_docs_date'] = docs_date
    # After the layout move (data/paths.json on main), every act lives in its official-identifier folder; new acts
    # get theirs from the same rule. Before it, folders are slugs (act['path'] unset).
    known_paths = L.paths_at(repo, 'main')
    if known_paths:
        L.assign(c, known_paths)
    if git(repo, 'rev-parse', '--is-bare-repository').strip() != 'true' and \
            git(repo, 'status', '--porcelain', '--untracked-files=no').strip():
        raise B.CorpusError(f'{repo} has uncommitted changes; refusing')
    head = git(repo, 'rev-parse', 'main').strip()
    origin = subprocess.run(['git', 'rev-parse', '--verify', '-q', 'origin/main'], cwd=repo, capture_output=True,
                            text=True).stdout.strip()
    if origin and origin != head:
        # Only the layout cutover appends onto its own unpushed layout commit (GITLAW_ALLOW_AHEAD=1), and only when
        # main is origin/main plus commits of its own.
        ahead_ok = os.environ.get('GITLAW_ALLOW_AHEAD') == '1' and subprocess.run(
            ['git', 'merge-base', '--is-ancestor', origin, head], cwd=repo).returncode == 0
        if not ahead_ok:
            raise B.CorpusError(f'main {head[:12]} is not origin/main {origin[:12]}: fetch and reset to the published head first')
    head_ct, head_tz = git(repo, 'log', '-1', '--format=%ct %ci', 'main').split()[0::3]
    head_ct = int(head_ct)
    state, problems, rows, dirs = published_state(repo, c, trusted)
    # An act whose published text differs from the corpus is corrected only when listed in GITLAW_CORRECTIONS. Any
    # other stops the run as before, or with GITLAW_HOLD_MISMATCHED=1 is left out of this append (its part is
    # reported in held_parts, for the caller to leave out of its check too) so one act can't stop every publish.
    approved = approved_corrections()
    # A correction needs the act's published history; an act with none (its folder found without it) is never one.
    unapproved = {s: p for s, p in problems.items() if s not in approved or s not in state}
    if unapproved and os.environ.get('GITLAW_HOLD_MISMATCHED') != '1':
        msgs = [m for _, ms in unapproved.values() for m in ms]
        raise B.CorpusError('main does not match the corpus for versions it already holds:\n  ' + '\n  '.join(msgs[:40]))
    by_slug = {a['slug']: a for a in c['acts']}
    corrections = []
    for s in sorted(set(problems) - set(unapproved)):
        corrections += correction_block(repo, c, by_slug[s], problems[s][0], state[s], rows[s],
                                        B.public_note(approved[s]) or '')
    # a day a correction restates is published: an order re-dated later must not be appended again from its new day
    for x in corrections:
        s = x['act']['slug']
        state[s] = max(state.get(s, ''), x['day'])
    # Credits: a listed act whose words already match main may still credit a change to the wrong law. Text first:
    # an act corrected for its text this publish gets its credits checked on the next.
    ledger = credit_ledger(repo, head)
    credit_rows: dict[str, list[dict]] = {}
    listed = sorted(set(approved) & set(state) - set(problems))
    credited = main_credits(repo, c, [by_slug[s] for s in listed])  # one history walk for all of them
    for s in listed:
        rows_s = credit_fixes(repo, c, by_slug[s], state[s], ledger, credited[s])
        if rows_s:
            credit_rows[s] = rows_s
    fixes_by_act: dict[str, list[dict]] = {}
    for r in ledger + [r for rs in credit_rows.values() for r in rs]:
        fixes_by_act.setdefault(r['act'], []).append(r)
    for a in c['acts']:
        a['_credit_fixes'] = fixes_by_act.get(a['slug'], [])  # shown in the act's README
    # A trusted act read without its words that this append adds or extends (a version that came due) is read in full.
    wordless = {a['slug'] for a in c['acts'] if a['slug'] in trusted and a['slug'] not in unapproved
                and needs_words(a, state.get(a['slug']), docs_date)}
    if wordless:
        reload_parts(c, wordless, part_read)
    del part_read, trusted, rows, dirs  # not read below
    sub, based = to_append({**c, 'acts': [a for a in c['acts'] if a['slug'] not in unapproved]}, state, docs_date)
    commits = B.plan(sub) if sub['acts'] else []
    commits = [x for x in commits if not (x['kind'] == 'start' and x['act']['slug'] in based)]
    existing_tags = set(git(repo, 'tag', '--list').split())
    co = c['country']
    committer = ('Lexifina', f'{co["slug"]}-law@lexifina.com')
    clock = B.Clock(co['tz'])
    summary = {'head': head, 'new_acts': sorted(a['slug'] for a in sub['acts'] if a['slug'] not in based),
               'extended_acts': sorted(based), 'commits': len(commits) + len(corrections),
               'corrected_acts': sorted({x['act']['slug'] for x in corrections}),
               'credit_corrections': {s: len(rs) for s, rs in credit_rows.items()},
               'held_acts': sorted(unapproved),
               'held_parts': sorted({by_slug[s].get('_part') for s in unapproved} - {None})}
    if dry_run or (not commits and not corrections and not credit_rows and not refresh_docs):
        summary['main'] = head
        return summary
    # Committer time: the publish time when given (so the host shows when the law was added), never earlier than the
    # published head; each appended commit one second after the last. The batch log (data/appends.csv) records it, so
    # a rebuild replays the same times and the same hashes.
    # The batch ends at the publish time, not after it: check_repo rejects commits dated in the future.
    start_ct = max(head_ct, (committer_time - len(commits) - len(corrections) - len(credit_rows) - 2)
                   if committer_time else 0)
    w = Appender(repo, head, start_ct, '+0000' if committer_time else head_tz, cap=committer_time)
    tags: dict[str, int] = {}
    log = []
    # Corrections go first, so the extensions planned from the corrected text follow them.
    fixed_when = f'{committer_time} +0000' if committer_time else clock.stamp(docs_date)
    for x in corrections:
        B.check_trailers(x['trailers'])
        text = '\n'.join(x['message']).rstrip('\n') + '\n\n' + '\n'.join(x['trailers']) + '\n'
        if x.get('law'):  # a court ruling applied: the decision's own commit, dated on the day it took effect
            mark = w.commit(x['author'], clock.stamp(x['day']), committer, text, x['files'])
            tags.setdefault(f'law/{x["law"]}', mark)
            tags.setdefault(f'{x["act"]["slug"]}/{x["day"]}', mark)
            log.append({'day': x['day'], 'kind': 'law', 'law': x['law'], 'acts': [x['act']['slug']],
                        'units': len(x['files']), 'branch': 'main', 'clamped': x['day'] < '1970-01-01'})
            continue
        w.commit(committer, fixed_when, committer, text, x['files'])
        log.append({'day': x['day'], 'kind': 'correction', 'law': None, 'acts': [x['act']['slug']],
                    'units': len(x['files']), 'branch': 'main', 'clamped': x['day'] < '1970-01-01'})
    # Credit corrections: one commit per act, with no In-force trailer, so no reader ever takes text from it. It adds
    # the rows to data/credits.csv and rewrites the act's README, so `git log` on the act's folder shows it too.
    ledger_rows = list(ledger)
    names = {k: l.get('label', k) for k, l in c['laws'].items()}
    def law_name(k: str) -> str:
        return names.get(k, k) if k else "no law (a change the publisher's record leaves unexplained)"
    for s, rows_s in credit_rows.items():
        act = by_slug[s]
        ledger_rows += rows_s
        buf = io.StringIO()
        wr = csv.DictWriter(buf, fieldnames=CREDIT_COLUMNS, lineterminator='\n')
        wr.writeheader()
        wr.writerows(ledger_rows)
        readme = f'{act.get("path") or s}/README.md'
        files = {'data/credits.csv': buf.getvalue(), readme: B.tables({**c, 'acts': [act]}, [])[readme]}
        lines = [f'- In force {r["in_force"]}, {r["provision"]}: {law_name(r["law"])} (was {law_name(r["was_law"])}).'
                 for r in rows_s]
        reason = B.public_note(approved[s]) or ''
        msg = [f'Credit correction: {act.get("short") or s}', ''] + ([reason, ''] if reason else []) + \
              ['The words are unchanged; only the law each change is credited to. git blame still names the commit that '
               'wrote the words; data/credits.csv records the corrected credit.', ''] + \
              lines[:60] + ([f'- and {len(lines) - 60} more (data/credits.csv)'] if len(lines) > 60 else [])
        trailers = ['Kind: correction', f'Act: {s}', f'Credits: {len(rows_s)}'] + \
                   [f'Corrects: {h}' for h in dict.fromkeys(r['was_commit'] for r in rows_s) if h]
        B.check_trailers(trailers)
        w.commit(committer, fixed_when, committer, '\n'.join(msg).rstrip('\n') + '\n\n' + '\n'.join(trailers) + '\n',
                 files)
        log.append({'day': docs_date, 'kind': 'correction', 'law': None, 'acts': [s], 'units': len(rows_s),
                    'branch': 'main', 'clamped': False})
    for x in commits:
        if x['kind'] == 'start':
            author, msg, trailers = B.start_message(c, x)
            files = B.act_files(x['act'], x['version']['units'], None)
            touched = [x['act']['slug']]
        else:
            author, msg, trailers = B.change_message(c, x)
            files = {}
            for p in x['parts']:
                files.update(B.act_files(p['act'], p['cur']['units'], p['prev']['units'], p['keys']))
            touched = [p['act']['slug'] for p in x['parts']]
        B.check_trailers(trailers)
        text = '\n'.join(msg).rstrip('\n') + '\n\n' + '\n'.join(trailers) + '\n'
        mark = w.commit(author, clock.stamp(x['day']), committer, text, files)
        for s in touched:
            tags.setdefault(f'{s}/{x["day"]}', mark)
        if x['kind'] == 'law':
            tags.setdefault(f'law/{x["law"]}', mark)
        elif x['kind'] == 'start' and x['act'].get('first_law'):
            tags.setdefault(f'law/{x["act"]["first_law"]}', mark)
        log.append({'day': x['day'], 'kind': x['kind'],
                    'law': x.get('law') or (x['act'].get('first_law') if x['kind'] == 'start' else None),
                    'acts': touched, 'units': len(files), 'branch': 'main', 'clamped': x['day'] < '1970-01-01'})
    full_log = published_log(repo) + log
    all_tags = {t: 0 for t in existing_tags} | {t: m for t, m in tags.items()}
    # Documentation covers acts with text history on main after this append: those main held before it and those it
    # appends. An act in the corpus that is not appended (it takes effect later, or is held back) gets no README and
    # no index row yet; a README-only folder would otherwise read as a published act with no text.
    on_main = set(state) | {a['slug'] for a in sub['acts']}
    tagged = {t.split('/', 1)[0] for t in existing_tags if '/' in t and not t.startswith('law/')}  # <id>/<day> tags
    c_pub = {**c, 'acts': [a for a in c['acts'] if a['slug'] in on_main]}
    docs = B.docs_files(c_pub, folder, raw, full_log, all_tags, docs_date)
    # Ship this script beside build.py, so the repository says how its appended commits were made.
    for name in ('append.py', 'layout.py'):
        docs[f'tools/build/{name}'] = (HERE / name).read_text(encoding='utf-8').replace('\r\n', '\n')
    B.check_published_tools(docs)  # every published .py compiles, no tool lost its line breaks
    # Memory (2026-11-05): the files made so far that nothing below reads or rewrites (the acts' READMEs, ~100,000 files
    # and ~0.5 GB as text, the static docs and data, the tools) go to fast-import now, as blobs the commit names by
    # mark. Of the corpus, the indexes below read only each act's own fields, its versions' days and how many
    # provisions each has, how many laws there are, and the sources; of the log, only REPRODUCE.md's counts. The rest
    # is let go before the indexes are split, the run's peak.
    stream_docs(w, docs)
    drop_words(c['acts'])
    for k in c.get('laws', {}):
        c['laws'][k] = None  # only their number is read below (REPRODUCE.md)
    counts: dict = {}
    full_log = [counts.setdefault((e['kind'], e['branch'], e['clamped']),
                                  {'kind': e['kind'], 'branch': e['branch'], 'clamped': e['clamped']}) for e in full_log]
    # The indexes (ACTS.md, data/acts.json, data/versions.json, data/paths.json) list every act main holds, not only the
    # acts in this publish's corpus: a part held back for a cycle must not drop its acts from them, and only a
    # correction commit's "Withdraws: <id>" trailer marks an act withdrawn. Rows for acts not in this corpus come from
    # main: head's versions.json, else the last one that had them.
    listed = {a['slug'] for a in c['acts']}
    extra, rows_for, path_for = absent_acts(repo, head, listed, known_paths, c)
    # Of the acts this corpus doesn't have, keep the withdrawn and those with history (held back this cycle).
    no_text = [a for a in extra if not a.get('_withdrawn') and a['slug'] not in tagged]
    no_text_ids = {id(a) for a in no_text}  # by identity: list membership compared whole dicts, O(n^2)
    extra = [a for a in extra if id(a) not in no_text_ids]
    index = {**c, 'acts': c_pub['acts'] + extra}
    # READMEs that earlier documentation commits wrote into folders with no text are removed (documentation, not
    # history: each documentation commit regenerates it).
    readmes = {f for f in git(repo, 'ls-tree', '-r', '--name-only', 'main').splitlines() if f.endswith('/README.md')}
    for a in [a for a in c['acts'] if a['slug'] not in on_main and a['slug'] not in tagged] + no_text:
        p = f'{a.get("path") or known_paths.get(a["slug"]) or a["slug"]}/README.md'
        if p in readmes:
            docs[p] = None
    if not known_paths:  # after the layout move, split_docs writes ACTS.md
        docs['ACTS.md'] = acts_index(c_pub)
    docs['data/acts.json'] = L.acts_json(index)
    vj = json.loads(docs['data/versions.json'])
    vj['acts'] += [rows_for[a['slug']] for a in extra]  # kept, so the next publish still knows them
    docs['data/versions.json'] = json.dumps(vj, ensure_ascii=False, indent=1) + '\n'
    del vj
    if known_paths:
        since = json.loads(git(repo, 'show', 'main:data/paths.json')).get('since', docs_date)
        pj = json.loads(L.paths_json(index, since))
        # paths.json never drops a folder: an entry main has stays, whatever this corpus holds.
        withdrawn = {a['slug'] for a in extra if a.get('_withdrawn')}  # a set: extra can hold every act (a trial corpus)
        for s, p in {**known_paths, **path_for}.items():
            if (s in on_main or s in tagged) and s not in withdrawn:
                pj['paths'].setdefault(s, p)
        pj['paths'] = dict(sorted(pj['paths'].items()))
        docs['data/paths.json'] = json.dumps(pj, ensure_ascii=False, indent=0) + '\n'
        del pj
        # data/index.json: primary files plus per-kind-and-year shards (2026-11-05)
        split_docs(docs, index, repo, c_pub.get('sources', []),
                   lambda kept: B.reproduce({**c_pub, 'sources': kept}, folder, raw, full_log, all_tags, docs_date))
    # Tools that moved or are no longer shipped (the old flat tools/ layout, tools/acts/) are removed, not left stale.
    shipped_tools = {p for p in git(repo, 'ls-tree', '-r', '--name-only', 'main', 'tools/').splitlines() if p}
    for p in shipped_tools - set(docs):
        docs[p] = None
    # One row per append batch: which head it started from, its first committer time, its commit count and its acts.
    prev_log = subprocess.run(['git', 'show', f'{head}:data/appends.csv'], cwd=repo, capture_output=True,
                              text=True, encoding='utf-8').stdout or 'batch,base,committer_start,commits,acts\n'
    n_batch = max(len(prev_log.strip().splitlines()) - 1, 0) + 1
    new_acts = ' '.join(sorted({a['slug'] for a in sub['acts']}))
    docs['data/appends.csv'] = prev_log + f'{n_batch},{head},{start_ct + 1}{f'..{committer_time}' if committer_time else ''},{len(log) + 1},{new_acts}\n'
    # The documentation commit is ours, made at publish time: its author date is the publish time too (the host shows
    # the head commit's author date as "updated N minutes ago"). Law commits keep their in-force day as author date.
    docs_when = f'{max(w.ct, min(w.ct + 1, committer_time))} +0000' if committer_time else clock.stamp(docs_date)
    w.commit(committer, docs_when, committer,
             f'Documentation, tables, tools and REPRODUCE.md\n\nAppended {len(log)} commits to {head[:12]}; corpus '
             f'sha256 {B.hashlib.sha256(raw).hexdigest()}, data retrieved {docs_date}.\n', docs)
    for name, mark in sorted(tags.items()):
        if name not in existing_tags:
            w.tag(name, mark)
    w.finish()
    if git(repo, 'rev-parse', '--is-bare-repository').strip() != 'true':  # a bare trial clone has no working tree
        git(repo, '-c', 'checkout.workers=0', 'checkout', '-q', '-f', 'main')
    # fast-import writes each new tag as a loose file; tens of thousands of them made every `git tag --list` take
    # seconds. Packing the new ones each run keeps it cheap (local refs only; nothing published changes).
    git(repo, 'pack-refs', '--all')
    new_head = git(repo, 'rev-parse', 'main').strip()
    if subprocess.run(['git', 'merge-base', '--is-ancestor', head, new_head], cwd=repo).returncode:
        raise B.CorpusError('internal: the published head is not an ancestor of the new main')
    summary.update({'main': new_head, 'tags_added': sum(1 for t in tags if t not in existing_tags)})
    return summary


def split_docs(docs: dict, index: dict, repo: Path, sources: list, reproduce) -> None:
    """The indexes split into the primary files and per-kind-and-year shards (build.split_indexes, data/index.json).
    ACTS.md keeps the primary legislation and links the other kinds' lists, data/acts/<shard>.md; REPRODUCE.md keeps
    the sources of the primary legislation (and every shared one), the rest go to data/sources/<shard>.csv."""
    where, kept = B.split_indexes(docs, sources)
    if len(kept) != len(sources):
        text = reproduce(kept)
        text = text.replace('Every word of law in this repository comes from these sources.',
                            'Every word of law in this repository comes from these sources and, for the acts of the '
                            'other kinds, from the sources listed beside them in `data/sources/<kind>/<year>.csv` '
                            '(local acts: `data/sources/local/<council>/<year>.csv`; all in `data/index.json`).', 1)
        docs['REPRODUCE.md'] = text.replace('is listed in [ACTS.md](ACTS.md)', 'is listed in [ACTS.md](ACTS.md) '
                                            'and the lists it links', 1)
    groups: dict = {}
    for a in index['acts']:  # index order, as ACTS.md had it
        groups.setdefault(where.get(a['slug']), []).append(a)
    link = re.compile(r'\]\(([^)#:]+/[^)]*)\)')
    for s, acts in groups.items():
        if s is None:
            continue
        base = s.rsplit('/', 1)[-1]
        kind, sub = s.split('/', 1)
        name = L.KIND_NAMES.get(kind) or L.ORDER_KINDS.get(kind) or kind
        text = L.acts_md({**index, 'acts': acts}).replace('[data/acts.json](data/acts.json)', f'[{base}.json]({base}.json)')
        up = '../' * (2 + s.count('/'))  # links in data/acts/<shard>.md are relative to it
        text = link.sub(lambda m: f'](<{up}{m.group(1)}>)' if ' ' in m.group(1) else f']({up}{m.group(1)})', text)
        head = f'# {name}: ' + (f'`local/{sub.rsplit("/", 1)[0]}/`, {base}' if kind == 'local' else sub)
        docs[f'data/acts/{s}.md'] = text.replace('# Every act in this repository', head, 1)
    md = L.acts_md({**index, 'acts': groups.get(None, [])})
    md = md.replace('the same list is in [data/acts.json](data/acts.json).',
                    'the same list is in [data/acts.json](data/acts.json). This page lists the primary legislation; every '
                    'other kind is listed by year (local acts: by council and year) under [data/acts/](data/acts/) (see '
                    '[Other kinds](#other-kinds)), and [data/index.json](data/index.json) names every file.', 1)
    kinds: dict = {}
    for s, acts in groups.items():
        if s is not None:
            kinds[s.split('/', 1)[0]] = kinds.get(s.split('/', 1)[0], 0) + len(acts)
    if kinds:
        order = {k: i for i, k in enumerate(L.KIND_ORDER)}
        md = md.rstrip('\n') + '\n\n## Other kinds\n\n| Kind | Acts | Lists, by year (local acts: by council and year) |\n' \
                               '| --- | ---: | --- |\n'
        md += ''.join(f'| {L.KIND_NAMES.get(k) or L.ORDER_KINDS.get(k) or k} | {n} | [`data/acts/{k}/`](data/acts/{k}/) |\n'
                      for k, n in sorted(kinds.items(), key=lambda x: (order.get(x[0], 99), x[0])))
    docs['ACTS.md'] = md
    existing = set(git(repo, 'ls-tree', '-r', '--name-only', 'main', '--', *B.SHARD_DIRS).splitlines())
    B.drop_stale_shards(docs, existing)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('folder')
    ap.add_argument('--repo', required=True)
    ap.add_argument('--docs-date', required=True)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--refresh-docs', action='store_true', help='append a documentation commit even with no new law commit')
    ap.add_argument('--committer-time', type=int, help='epoch seconds to date the appended commits from (the publish time)')
    a = ap.parse_args()
    print(append(Path(a.folder), Path(a.repo), a.docs_date, a.dry_run, a.committer_time, a.refresh_docs))


if __name__ == '__main__':
    main()
