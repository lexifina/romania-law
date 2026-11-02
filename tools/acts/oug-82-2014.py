"""OUG nr. 82/2014 pentru modificarea și completarea Legii nr. 135/2010 privind Codul de procedură penală: Lexifina,
2026-11-02.

Act page 163828, also its base text (DetaliiDocumentAfis/163828). One consolidated form listed, 02.05.2016
(DetaliiDocument/178093). An amending act: its own articles (Art. I, II, ...) are the text, and the provisions it
inserts into other acts are quoted text."""
SLUG = 'oug-82-2014'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-82-2014', 'short': 'OUG nr. 82/2014', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True, 'quoted_heads': True,
        'root_word': 'act page',
        'title': 'Ordonanța de urgență a Guvernului nr. 82/2014 pentru modificarea și completarea Legii nr. 135/2010 '
                 'privind Codul de procedură penală',
        'url': P.PORTAL + 'DetaliiDocument/163828',
        'in_force': '2014-12-15', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 911 of 15 December 2014; an '
                     'emergency ordinance with no day of its own, in force on publication (Constituția art. 115 '
                     'alin. (5); Legea nr. 24/2000 art. 12 alin. (2)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 82/2014: the first version is the emergency ordinance as published in Monitorul Oficial nr. 911 '
            'of 15 December 2014 (DetaliiDocumentAfis/163828), dated 15 December 2014: an emergency ordinance with '
            'no day of its own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 '
            'alin. (2)). The portal holds no consolidated form before 2 May 2016, so the changes made up to then '
            'arrive together that day.',
            'OUG nr. 82/2014: the ordinance numbers its own articles in Roman numerals (I, II, ...); each is kept '
            'under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
            'provisions it inserts into Legea nr. 135/2010 and the other acts it amends are quoted text and stay in '
            'the article that quotes them. The signature block printed after the last article is not text.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/163828)
        'label': 'OUG nr. 82/2014', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 82/2014 pentru modificarea și completarea Legii nr. 135/2010 '
                 'privind Codul de procedură penală, publicată în Monitorul Oficial al României, Partea I, nr. 911 '
                 'din 15 decembrie 2014',
        'enacted': '2014-12-10', 'published': '2014-12-15', 'url': P.PORTAL + 'DetaliiDocumentAfis/163828',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
