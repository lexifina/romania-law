"""OUG nr. 65/2005: read from the portal's forms with the standing rules (Lexifina, 2026-11-02).

Parse rules and decisions only; its forms manifest is forms.d/oug-65-2005.json.
"""
SLUG = 'oug-65-2005'


def register(P):
    P.ACTS[SLUG] = {**P.P6, **{'hg_notes': True,
         'trailing_notes': True,
         'sign_tail': True,
         'quoted_articles': True,
         'quoted_heads': True,
         'titles': False,
         'roman_articles': True,
         'part': '9z-oug-65-2005',
         'short': 'OUG nr. 65/2005',
         'pad': 3,
         'cc_forms': True,
         'root_word': 'act page',
         'title': 'Ordonanța de urgență a Guvernului nr. 65/2005',
         'url': 'https://legislatie.just.ro/Public/DetaliiDocument/62888',
         'in_force': '2005-07-05',
         'first_law': 'oug-65-2005',
         'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 576 of 5 July 2005; an emergency '
                      'ordinance with no day of its own, in force on publication (Constituția art. 115 alin. (5); '
                      'Legea nr. 24/2000 art. 12 alin. (2)).',
         'form_note': {},
         'republished': {},
         'decisions': ['OUG nr. 65/2005: built by hand by Lexifina with the standing reading rules, with no ruling of '
                       'its own for this act: the forms are those the portal lists, each version is dated by its form '
                       'or by the notes it prints. The text of the articles was checked word by word against the page, '
                       'and none of it is lost.',
                       'OUG nr. 65/2005: the first version is the emergency ordinance as published in Monitorul '
                       'Oficial nr. 576 of 5 July 2005 (DetaliiDocumentAfis/62888), dated 5 July 2005: an emergency '
                       'ordinance with no day of its own, in force on publication (Constituția art. 115 alin. (5); '
                       'Legea nr. 24/2000 art. 12 alin. (2)). The portal holds no consolidated form before 22 December '
                       '2005, so the changes made up to then arrive together that day.',
                       'OUG nr. 65/2005: the emergency ordinance numbers its own articles in Roman numerals (I, II, '
                       '...); each is kept under its Roman title and filed by its value (art-001 for Articolul I), so '
                       'the files sort in order. The articles of other acts it quotes stay in the text of the article '
                       'that quotes them.'],
         'repeal_acts': {},
         'quoted_roman': True,
         'quoted_lines': True,
         'point_tail': True}}
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {'label': 'OUG nr. 65/2005',
         'kind': 'decree',
         'title': 'Ordonanța de urgență a Guvernului nr. 65/2005, publicată în Monitorul Oficial al României, Partea '
                  'I, nr. 576 din 5 iulie 2005',
         'enacted': '2005-06-29',
         'published': '2005-07-05',
         'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/62888'})
