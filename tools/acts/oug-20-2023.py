"""OUG nr. 20/2023: read from the portal's forms with the standing rules (Lexifina, 2026-11-02).

Parse rules and decisions only; its forms manifest is forms.d/oug-20-2023.json.
"""
SLUG = 'oug-20-2023'


def register(P):
    P.ACTS[SLUG] = {**P.P6, **{'hg_notes': True,
         'trailing_notes': True,
         'sign_tail': True,
         'quoted_articles': True,
         'quoted_heads': True,
         'titles': False,
         'roman_articles': True,
         'part': '9z-oug-20-2023',
         'short': 'OUG nr. 20/2023',
         'pad': 3,
         'cc_forms': True,
         'root_word': 'act page',
         'title': 'Ordonanța de urgență a Guvernului nr. 20/2023 pentru modificarea și completarea Legii nr. 207/2015 '
                  'privind Codul de procedură fiscală , precum și pentru modificarea Ordonanței Guvernului nr. 6/2019 '
                  'privind instituirea unor facilități fiscale',
         'url': 'https://legislatie.just.ro/Public/DetaliiDocument/266651',
         'in_force': '2023-04-06',
         'first_law': 'oug-20-2023',
         'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 290 of 6 April 2023; an emergency '
                      'ordinance with no day of its own, in force on publication (Constituția art. 115 alin. (5); '
                      'Legea nr. 24/2000 art. 12 alin. (2)).',
         'form_note': {},
         'republished': {},
         'decisions': ['OUG nr. 20/2023: built by hand by Lexifina with the standing reading rules, with no ruling of '
                       'its own for this act: the forms are those the portal lists, each version is dated by its form '
                       'or by the notes it prints. The text of the articles was checked word by word against the page, '
                       'and none of it is lost.',
                       'OUG nr. 20/2023: the first version is the emergency ordinance as published in Monitorul '
                       'Oficial nr. 290 of 6 April 2023 (DetaliiDocumentAfis/266651), dated 6 April 2023: an emergency '
                       'ordinance with no day of its own, in force on publication (Constituția art. 115 alin. (5); '
                       'Legea nr. 24/2000 art. 12 alin. (2)). The portal lists no consolidated form of it, so the text '
                       'as published is its only version; the act page (DetaliiDocument/266651) prints the same text.',
                       'OUG nr. 20/2023: the emergency ordinance numbers its own articles in Roman numerals (I, II, '
                       '...); each is kept under its Roman title and filed by its value (art-001 for Articolul I), so '
                       'the files sort in order. The articles of other acts it quotes stay in the text of the article '
                       'that quotes them.'],
         'repeal_acts': {},
         'quoted_roman': True,
         'quoted_lines': True,
         'point_tail': True}}
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {'label': 'OUG nr. 20/2023',
         'kind': 'decree',
         'title': 'Ordonanța de urgență a Guvernului nr. 20/2023 pentru modificarea și completarea Legii nr. 207/2015 '
                  'privind Codul de procedură fiscală , precum și pentru modificarea Ordonanței Guvernului nr. 6/2019 '
                  'privind instituirea unor facilități fiscale, publicată în Monitorul Oficial al României, Partea I, '
                  'nr. 290 din 6 aprilie 2023',
         'enacted': '2023-04-05',
         'published': '2023-04-06',
         'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/266651'})
