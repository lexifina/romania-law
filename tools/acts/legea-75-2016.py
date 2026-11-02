"""Legea nr. 75/2016 privind aprobarea Ordonanței de urgență a Guvernului nr. 82/2014 (Lexifina, 2026-11-02).

Act page 178058, also its base text (DetaliiDocumentAfis/178058); the portal lists no consolidated form of it. One
article ("Articolul UNIC"), which quotes the text of the articles of the ordinance it changes.
"""
SLUG = 'legea-75-2016'

TITLE = ('Legea nr. 75/2016 privind aprobarea Ordonanței de urgență a Guvernului nr. 82/2014 pentru modificarea și '
         'completarea Legii nr. 135/2010 privind Codul de procedură penală')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-75-2016', 'short': 'Legea nr. 75/2016', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'unic_article': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True,
        'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/178058',
        'in_force': '2016-05-02', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 334 of 29 April 2016; it sets no day of its own, '
                     'so in force 3 days after publication (Constituția art. 78): 2 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 75/2016: the first version is the law as published in Monitorul Oficial nr. 334 of 29 April '
            '2016 (DetaliiDocumentAfis/178058), dated 2 May 2016: it sets no day of its own, so in force 3 days after '
            'publication (Constituția art. 78). The portal lists no consolidated form of it, so the text as '
            'published is its only version.',
            'Legea nr. 75/2016: the law has a single article ("Articolul UNIC"), filed as art-001. The text it '
            'quotes from the ordinance it approves is part of that article. The signature block after it is not '
            'text.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/178058: "LEGE nr. 75 din 28 aprilie 2016", MO nr. 334
    # din 29 aprilie 2016)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 75/2016', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 334 din 29 aprilie 2016',
        'enacted': '2016-04-28', 'published': '2016-04-29', 'url': P.PORTAL + 'DetaliiDocumentAfis/178058',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
