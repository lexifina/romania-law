"""Legea nr. 343/2006 pentru modificarea și completarea Legii nr. 571/2003 privind Codul fiscal (Lexifina, 2026-11-02).

The portal lists no consolidated form of it: the text as published (DetaliiDocumentAfis/73981) is its only version.
Parsed as the Phase 6 acts, with the flags of the automatic entries.
"""
SLUG = 'legea-343-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'star_footnotes': True,
        'part': '9z-legea-343-2006', 'short': 'Legea nr. 343/2006', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Legea nr. 343/2006 pentru modificarea și completarea Legii nr. 571/2003 privind Codul fiscal',
        'url': P.PORTAL + 'DetaliiDocument/73981',
        'in_force': '2006-08-04', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 662 of 1 August 2006; it sets no day of its own, '
                     'so in force 3 days after publication (Constituția art. 78): 4 August 2006.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 343/2006: the first version is the law as published in Monitorul Oficial nr. 662 of 1 August '
            '2006 (DetaliiDocumentAfis/73981), dated 4 August 2006: it sets no day of its own for the whole law, so it '
            'is in force 3 days after publication (Constituția art. 78). Its art. V puts art. I in force on 1 January '
            '2007 (unless a provision says otherwise) and art. II 3 days after publication; the provisions are shown '
            'as published from 4 August 2006, and no version is made for 1 January 2007. The portal lists no '
            'consolidated form of it, so the text as published is its only version.',
            'Legea nr. 343/2006: the law numbers its own articles in Roman numerals (I, II, ...); each is kept under '
            'its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
            'articles of other acts it quotes stay in the text of the article that quotes them.',
            'Legea nr. 343/2006: the tables of art. I are printed as the portal prints them, and the notes under '
            'them ("*) Nivelul accizelor va fi menținut ...", "**) Structura accizei totale ... va fi stabilită prin '
            'Hotărâre de Guvern", "1) Gradul Plato ...") are the law\'s own footnotes and are kept as text; the '
            'portal\'s editorial notes, which open with "* " in other acts, are not dropped here.',
        ],
        'repeal_acts': {},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {  # from the text as published (DetaliiDocumentAfis/73981)
        'label': 'Legea nr. 343/2006', 'kind': 'law',
        'title': 'Legea nr. 343/2006 pentru modificarea și completarea Legii nr. 571/2003 privind Codul fiscal, '
                 'publicată în Monitorul Oficial al României, Partea I, nr. 662 din 1 august 2006',
        'enacted': '2006-07-17', 'published': '2006-08-01', 'url': P.PORTAL + 'DetaliiDocumentAfis/73981',
    })
