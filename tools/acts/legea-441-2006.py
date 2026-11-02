"""Legea nr. 441/2006 pentru modificarea și completarea Legii nr. 31/1990 și a Legii nr. 26/1990 (Lexifina, 2026-11-02).

Act page 77185, also its base text (DetaliiDocumentAfis/77185); the portal lists no consolidated form of it
(forms.d/legea-441-2006.json). Its art. III alin. (4) puts most of it in force on 1 December 2006 and art. II pct. 4 and
11 on 1 January 2007.
"""
SLUG = 'legea-441-2006'
TITLE = ('Legea nr. 441/2006 pentru modificarea și completarea Legii nr. 31/1990 privind societățile comerciale, '
         'republicată, și a Legii nr. 26/1990 privind registrul comerțului, republicată')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-441-2006', 'short': 'Legea nr. 441/2006', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'quoted_heads': True, 'titles': False,
        'roman_articles': True, 'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/77185',
        'in_force': '2006-12-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 955 of 28 November 2006, in force on 1 December '
                     '2006 (its art. III alin. (4)), save art. II pct. 4 and 11, which take effect on 1 January 2007.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 441/2006: the first version is the law as published in Monitorul Oficial nr. 955 of 28 '
            'November 2006 (DetaliiDocumentAfis/77185), dated 1 December 2006: its art. III alin. (4) puts it in force '
            'on that day, save art. II pct. 4 and 11, in force on 1 January 2007. The portal lists no consolidated '
            'form of it, so the text as published is the only text.',
            'Legea nr. 441/2006: the law numbers its own articles in Roman numerals (I, II, ...); each is kept under '
            'its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
            'articles of other acts it quotes stay in the text of the article that quotes them.',
        ],
        # art. III alin. (4): art. II pct. 4 and pct. 11 (with the text each one quotes) in force on 1 January 2007
        'later_provisions': (
            {'day': '2007-01-01', 'law': SLUG, 'lines': (), 'keys': ('art-002',),
             'spans': (('4. La articolul 4, după alineatul (3)', '5. La articolul 10'),
                       ('11. La articolul 51 se introduc', None)),
             'note': 'Art. II pct. 4 and 11, which add alin. (4) and (5) to art. 4 and alin. (2)-(4) to art. 51 of '
                     'Legea nr. 26/1990, take effect on this day (art. III alin. (4)).'},
        ),
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 441/2006', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 955 din 28 noiembrie 2006',
        'enacted': '2006-11-27', 'published': '2006-11-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/77185',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
