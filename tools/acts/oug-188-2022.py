"""OUG nr. 188/2022 pentru modificarea și completarea Legii nr. 207/2015 privind Codul de procedură fiscală (Lexifina,
2026-11-02).

Act page 263291, also its base text (DetaliiDocumentAfis/263291); one consolidated form, of 16 December 2023, held from
Common Crawl (forms.d/oug-188-2022.json). Its art. III alin. (1) puts it in force on publication, save art. I pct. 43
(10 days after publication) and pct. 4, 12, 13 (as to art. 118 alin. (2)), 14-17 and 32 (1 January 2026).
"""
SLUG = 'oug-188-2022'
TITLE = ('Ordonanța de urgență a Guvernului nr. 188/2022 pentru modificarea și completarea Legii nr. 207/2015 privind '
         'Codul de procedură fiscală și pentru modificarea Ordonanței de urgență a Guvernului nr. 74/2013 privind '
         'unele măsuri pentru îmbunătățirea și reorganizarea activității Agenției Naționale de Administrare Fiscală, '
         'precum și pentru modificarea și completarea unor acte normative')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-188-2022', 'short': 'OUG nr. 188/2022', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/263291',
        'in_force': '2022-12-29', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 1272 of 29 December 2022, in force '
                     'on publication (its art. III alin. (1)), save the provisions that take effect on later days.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 188/2022: the first version is the emergency ordinance as published in Monitorul Oficial nr. 1272 '
            'of 29 December 2022 (DetaliiDocumentAfis/263291), dated 29 December 2022: its art. III alin. (1) puts it '
            'in force on publication, save art. I pct. 43 (10 days after publication) and art. I pct. 4, 12, 13 as to '
            'art. 118 alin. (2), 14-17 and 32 (1 January 2026). The portal holds no consolidated form before 16 '
            'December 2023, so the changes made up to then arrive together that day.',
            'OUG nr. 188/2022: each provision takes effect on its own day. The first version holds the law without '
            'art. I pct. 43, which is added on 8 January 2023 (10 days after publication) and without pct. 4, 12, '
            '13 as to art. 118 alin. (2), 14-17 and 32, which are added on 1 January 2026; each point is taken out '
            'with the text it quotes (the quoted alin. (2) of pct. 13 is taken out, its alin. (4) stays). A version '
            'on each of those days adds the provisions as the newest form held prints them, credited to the '
            'emergency ordinance. The portal prints all of them from its form of 16 December 2023; no form of 2026 is '
            'held, so the version of 1 January 2026 carries the text as that form prints it.',
            'OUG nr. 188/2022: the emergency ordinance numbers its own articles in Roman numerals (I, II, ...); each '
            'is kept under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in '
            'order. The articles of other acts it quotes stay in the text of the article that quotes them.',
        ],
        # art. III alin. (1): art. I pct. 43 10 days after publication (8 January 2023); pct. 4, 12, 13 as to art. 118
        # alin. (2), 14-17 and 32 on 1 January 2026
        'later_provisions': (
            {'day': '2023-01-08', 'law': SLUG, 'lines': (), 'keys': ('art-001',),
             'spans': (('43. La articolul 336 alineatul (1)', None),),
             'note': 'Art. I pct. 43, which rewrites art. 336 alin. (1) lit. g) of Legea nr. 207/2015, takes effect on '
                     'this day, 10 days after publication (art. III alin. (1) lit. b)).'},
            {'day': '2026-01-01', 'law': SLUG, 'lines': (), 'keys': ('art-001',),
             'spans': (('4. La articolul 7, alineatul (10)', '5. La articolul 55'),
                       ('12. La articolul 118, după alineatul (1)', '13. La articolul 118'),
                       ('(2) Inspecția fiscală se exercită, în cazul organului fiscal local',
                        '(4) La începerea inspecției fiscale, organul de inspecție fiscală trebuie'),
                       ('14. Articolul 119', '18. După articolul 121'),
                       ('32. La articolul 138, după alineatul (2)', '33. După articolul 140')),
             'note': 'Art. I pct. 4, 12, 13 (as to art. 118 alin. (2)), 14-17 and 32 take effect on this day (art. '
                     'III alin. (1) lit. a)).'},
        ),
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'OUG nr. 188/2022', 'kind': 'decree',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 1272 din 29 decembrie 2022',
        'enacted': '2022-12-28', 'published': '2022-12-29', 'url': P.PORTAL + 'DetaliiDocumentAfis/263291',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
