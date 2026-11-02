"""Legea nr. 216/2022: read from the portal's forms with the standing rules (Lexifina, 2026-11-02).

Parse rules and decisions only; its forms manifest is forms.d/legea-216-2022.json.
"""
SLUG = 'legea-216-2022'


def register(P):
    P.ACTS[SLUG] = {**P.P6, **{'hg_notes': True,
         'trailing_notes': True,
         'sign_tail': True,
         'quoted_articles': True,
         'quoted_heads': True,
         'titles': False,
         'roman_articles': True,
         'part': '9z-legea-216-2022',
         'short': 'Legea nr. 216/2022',
         'pad': 3,
         'cc_forms': True,
         'root_word': 'act page',
         'title': 'Legea nr. 216/2022 pentru modificarea și completarea Legii nr. 85/2014 privind procedurile de '
                  'prevenire a insolvenței și de insolvență și a altor acte normative',
         'url': 'https://legislatie.just.ro/Public/DetaliiDocument/257536',
         'in_force': '2022-07-17',
         'first_law': 'legea-216-2022',
         'base_note': 'The law as published in Monitorul Oficial nr. 709 of 14 July 2022; it sets no day of its own, '
                      'so in force 3 days after publication (Constituția art. 78): 17 July 2022.',
         'form_note': {},
         'republished': {},
         'decisions': ['Legea nr. 216/2022: built by hand by Lexifina with the standing reading rules, with no ruling '
                       'of its own for this act: the forms are those the portal lists, each version is dated by its '
                       'form or by the notes it prints. The text of the articles was checked word by word against the '
                       'page, and none of it is lost.',
                       'Legea nr. 216/2022: the first version is the law as published in Monitorul Oficial nr. 709 of '
                       '14 July 2022 (DetaliiDocumentAfis/257536), dated 17 July 2022: it sets no day of its own, so '
                       'in force 3 days after publication (Constituția art. 78). The portal lists no consolidated form '
                       'of it, so the text as published is its only version; the act page (DetaliiDocument/257536) '
                       'prints the same text.',
                       'Legea nr. 216/2022: the law numbers its own articles in Roman numerals (I, II, ...); each is '
                       'kept under its Roman title and filed by its value (art-001 for Articolul I), so the files sort '
                       'in order. The articles of other acts it quotes stay in the text of the article that quotes '
                       'them.'],
         'repeal_acts': {},
         'quoted_roman': True,
         'quoted_lines': True,
         'point_tail': True}}
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {'label': 'Legea nr. 216/2022',
         'kind': 'law',
         'title': 'Legea nr. 216/2022 pentru modificarea și completarea Legii nr. 85/2014 privind procedurile de '
                  'prevenire a insolvenței și de insolvență și a altor acte normative, publicată în Monitorul Oficial '
                  'al României, Partea I, nr. 709 din 14 iulie 2022',
         'enacted': '2022-07-14',
         'published': '2022-07-14',
         'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/257536'})
