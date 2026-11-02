"""OUG nr. 109/2009 pentru modificarea și completarea Legii nr. 571/2003 privind Codul fiscal: Lexifina, 2026-11-02.

Act page 112207, also its base text (DetaliiDocumentAfis/112207). The portal lists no consolidated form of it: the text
as published is its only version. An amending act: its own articles (Art. I, II, ...) are the text, and the provisions
it inserts into other acts are quoted text."""
SLUG = 'oug-109-2009'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-109-2009', 'short': 'OUG nr. 109/2009', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True, 'quoted_heads': True,
        'root_word': 'act page',
        'title': 'Ordonanța de urgență a Guvernului nr. 109/2009 pentru modificarea și completarea Legii nr. '
                 '571/2003 privind Codul fiscal',
        'url': P.PORTAL + 'DetaliiDocument/112207',
        'in_force': '2009-10-13', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 689 of 13 October 2009; an '
                     'emergency ordinance with no day of its own, in force on publication (Constituția art. 115 '
                     'alin. (5); Legea nr. 24/2000 art. 12 alin. (2)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 109/2009: the first version is the emergency ordinance as published in Monitorul Oficial nr. '
            '689 of 13 October 2009 (DetaliiDocumentAfis/112207), dated 13 October 2009: an emergency ordinance with '
            'no day of its own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 '
            'alin. (2)). The portal lists no consolidated form of it, so the text as published is its only version.',
            'OUG nr. 109/2009: the ordinance numbers its own articles in Roman numerals (I, II, ...); each is kept '
            'under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
            'provisions it inserts into Legea nr. 571/2003 and the other acts it amends are quoted text and stay in '
            'the article that quotes them. The signature block printed after the last article is not text.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/112207)
        'label': 'OUG nr. 109/2009', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 109/2009 pentru modificarea și completarea Legii nr. '
                 '571/2003 privind Codul fiscal, publicată în Monitorul Oficial al României, Partea I, nr. 689 din '
                 '13 octombrie 2009',
        'enacted': '2009-10-07', 'published': '2009-10-13', 'url': P.PORTAL + 'DetaliiDocumentAfis/112207',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
