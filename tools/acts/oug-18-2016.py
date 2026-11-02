"""OUG nr. 18/2016 pentru modificarea și completarea Legii nr. 286/2009 privind Codul penal, a Legii nr. 135/2010
privind Codul de procedură penală și pentru completarea art. 31 alin. (1) din Legea nr. 304/2004: Lexifina, 2026-11-02.

Act page 178639, also its base text (DetaliiDocumentAfis/178639). One consolidated form listed, 10.05.2024
(DetaliiDocument/282154). An amending act: its own articles (Art. I, II, ...) are the text, and the provisions it
inserts into the codes are quoted text."""
SLUG = 'oug-18-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-18-2016', 'short': 'OUG nr. 18/2016', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True,
        'root_word': 'act page',
        'title': 'Ordonanța de urgență a Guvernului nr. 18/2016 pentru modificarea și completarea Legii nr. 286/2009 '
                 'privind Codul penal, Legii nr. 135/2010 privind Codul de procedură penală, precum și pentru '
                 'completarea art. 31 alin. (1) din Legea nr. 304/2004 privind organizarea judiciară',
        'url': P.PORTAL + 'DetaliiDocument/178639',
        'in_force': '2016-05-23', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 389 of 23 May 2016; an emergency '
                     'ordinance with no day of its own, in force on publication (Constituția art. 115 alin. (5); '
                     'Legea nr. 24/2000 art. 12 alin. (2)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 18/2016: the first version is the emergency ordinance as published in Monitorul Oficial nr. 389 '
            'of 23 May 2016 (DetaliiDocumentAfis/178639), dated 23 May 2016: an emergency ordinance with no day of '
            'its own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 alin. (2)). '
            'The portal holds no consolidated form before 10 May 2024, so the changes made up to then arrive '
            'together that day.',
            'OUG nr. 18/2016: the ordinance numbers its own articles in Roman numerals (I, II, ...); each is kept '
            'under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
            'provisions it inserts into the Codul penal, the Codul de procedură penală and Legea nr. 304/2004 are '
            'quoted text and stay in the article that quotes them. The signature block printed after the last '
            'article is not text.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178639)
        'label': 'OUG nr. 18/2016', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 18/2016 pentru modificarea și completarea Legii nr. 286/2009 '
                 'privind Codul penal, Legii nr. 135/2010 privind Codul de procedură penală, precum și pentru '
                 'completarea art. 31 alin. (1) din Legea nr. 304/2004 privind organizarea judiciară, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 389 din 23 mai 2016',
        'enacted': '2016-05-18', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178639',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
