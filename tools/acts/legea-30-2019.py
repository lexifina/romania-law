"""Legea nr. 30/2019 pentru aprobarea OUG nr. 25/2018 și a unor măsuri fiscal-bugetare (Lexifina, 2026-11-02).

Act page 210007, also its base text (DetaliiDocumentAfis/210007); the portal lists no consolidated form of it
(forms.d/legea-30-2019.json). Its art. VI puts art. I in force 3 days after publication, with exceptions that apply
from later days.
"""
SLUG = 'legea-30-2019'
TITLE = ('Legea nr. 30/2019 pentru aprobarea Ordonanței de urgență a Guvernului nr. 25/2018 privind modificarea și '
         'completarea unor acte normative, precum și pentru aprobarea unor măsuri fiscal-bugetare')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-30-2019', 'short': 'Legea nr. 30/2019', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'quoted_heads': True,
        'titles': False, 'roman_articles': True, 'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/210007',
        'in_force': '2019-01-20', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 44 of 17 January 2019, in force 3 days after '
                     'publication: 20 January 2019 (its art. VI for art. I; Constituția art. 78 for the rest), save '
                     'the provisions of art. I that apply from later days.',
        'form_note': {}, 'republished': {},
        # art. VI: art. I in force 3 days after publication (20 January 2019), save the points applied from 1 April
        # 2019: art. I pct. 1^2, 3, 5-16 (pct. 9 with 8^1 and 8^2, pct. 11 with 9^1, pct. 14 with 11^1, pct. 16 with
        # 12^1) and pct. 19 as to subpct. 18^1 and 18^2
        'later_provisions': (
            {'day': '2019-04-01', 'law': SLUG, 'lines': (), 'keys': ('art-001',),
             'spans': (('1^2. La articolul 25 alineatul (4), litera i)', '1^3. La articolul 25, după alineatul (4)'),
                       ('3. La articolul I punctul 5, la articolul 56, alineatul (1^1)',
                        '4. La articolul I punctul 5, la articolul 56, litera b)'),
                       ('5. La articolul I punctul 7, la articolul 68^1, alineatul (7)',
                        '17. La articolul I, după punctul 16'),
                       ('18^1. La articolul 123, alineatele (5) și (6) se abrogă',
                        '18^3. La articolul 130, după alineatul (6)')),
             'note': 'The points of art. I that art. VI applies from 1 April 2019 (pct. 1^2, 3, 5-16 and, of pct. 19, '
                     'subpct. 18^1 and 18^2) take effect on this day.'},
        ),
        'decisions': [
            'Legea nr. 30/2019: the first version is the law as published in Monitorul Oficial nr. 44 of 17 January '
            '2019 (DetaliiDocumentAfis/210007), dated 20 January 2019: its art. VI puts art. I in force 3 days after '
            'publication, and the other articles, which set no day, are in force then too (Constituția art. 78). The '
            'portal lists no consolidated form of it, so the text as published is the only text.',
            'Legea nr. 30/2019: art. VI lists exceptions that apply from a later day or an earlier one. Those that '
            'apply from 1 April 2019 (pct. 1^2, 3, 5-16, and pct. 19 as to subpct. 18^1 and 18^2, taking in the '
            'income of April 2019 and the rules that go with them) are left out of the first version, each point '
            'with the text it quotes (the heading of pct. 19, which names subpct. 18^1-18^3, stays), and a version of '
            '1 April 2019 adds them, credited to Legea nr. 30/2019. Those applied from 1 January 2019 (pct. 1^1, 1^4, 1^5, 20 and 21; for pct. 1^4 and 1^5 also from the first '
            'day of the fiscal year that begins after it) or to the income of the year 2019 (pct. 17, 18 and 19 as to '
            'subpct. 18^3) come before the day the law was published, which no version can precede, '
            'so they stand from 20 January 2019 with the rest.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 30/2019', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 44 din 17 ianuarie 2019',
        'enacted': '2019-01-10', 'published': '2019-01-17', 'url': P.PORTAL + 'DetaliiDocumentAfis/210007',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
