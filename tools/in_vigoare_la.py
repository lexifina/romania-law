"""Prints the law of Romania as it stood on a given day, read from this repository's history.

    python tools/in_vigoare_la.py 2014-10-18 codul-civil 1112      # art. 1112 the day before Legea nr. 138/2014
    python tools/in_vigoare_la.py 2016-01-01 codul-penal 112^1     # art. 112^1 (the file art-112-1.md)
    python tools/in_vigoare_la.py 2000-01-01 constitutia           # the whole Constitution on 1 January 2000
    python tools/in_vigoare_la.py --law 2024-01-01 codul-penal 336 # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date. An article number may be written as the portal writes it (`112^1`); it is read as the file `art-112-1`.
Standard library only.
"""
import re
import runpy
import sys
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.argv = [str(Path(__file__).with_name('on.py'))] + [re.sub(r'^(\d+)\^(\d+)$', r'\1-\2', a) for a in sys.argv[1:]]
    runpy.run_path(sys.argv[0], run_name='__main__')
