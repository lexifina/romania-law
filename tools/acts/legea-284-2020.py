"""Legea nr. 284/2020 pentru modificarea și completarea Legii nr. 135/2010 privind Codul de procedură penală
(Lexifina, 2026-11-02).

Act page 234457, also its base text (DetaliiDocumentAfis/234457); the portal lists no consolidated form of it. One
article ("ARTICOL UNIC") holding the provisions it inserts into the Codul de procedură penală as quoted text.
"""
SLUG = 'legea-284-2020'

TITLE = ('Legea nr. 284/2020 pentru modificarea și completarea Legii nr. 135/2010 privind Codul de procedură penală')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-284-2020', 'short': 'Legea nr. 284/2020', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'unic_article': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True,
        'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/234457',
        'in_force': '2020-12-12', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1201 of 9 December 2020; it sets no day of its '
                     'own, so in force 3 days after publication (Constituția art. 78): 12 December 2020.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 284/2020: the first version is the law as published in Monitorul Oficial nr. 1201 of 9 '
            'December 2020 (DetaliiDocumentAfis/234457), dated 12 December 2020: it sets no day of its own, so in '
            'force 3 days after publication (Constituția art. 78). The portal lists no consolidated form of it, so '
            'the text as published is its only version.',
            'Legea nr. 284/2020: the law has a single article ("ARTICOL UNIC"), filed as art-001. The provisions it '
            'inserts into the Codul de procedură penală are quoted text and stay in that article. The signature '
            'block after it is not text.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/234457: "LEGE nr. 284 din 8 decembrie 2020", MO nr.
    # 1201 din 9 decembrie 2020)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 284/2020', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 1201 din 9 decembrie 2020',
        'enacted': '2020-12-08', 'published': '2020-12-09', 'url': P.PORTAL + 'DetaliiDocumentAfis/234457',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
