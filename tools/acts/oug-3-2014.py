"""Ordonanța de urgență a Guvernului nr. 3/2014 pentru luarea unor măsuri de implementare necesare aplicării Legii nr.
135/2010 privind Codul de procedură penală și pentru implementarea altor acte normative (Lexifina, 2026-11-02).

Act page and base text DetaliiDocumentAfis/155316 (the act page itself has no capture); one consolidated form is listed,
17.04.2016 (178364), held as its DetaliiDocumentAfis page (the DetaliiDocument page of the form has no capture; the
Afis page shows the same form, "actualizată până la data de 17 aprilie 2016", with its notes). An amending act: its own
articles (Art. I, II, ...) are the text, and the provisions it inserts into other acts are quoted text.
"""
SLUG = 'oug-3-2014'

TITLE = ('Ordonanța de urgență a Guvernului nr. 3/2014 pentru luarea unor măsuri de implementare necesare aplicării '
         'Legii nr. 135/2010 privind Codul de procedură penală și pentru implementarea altor acte normative')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-3-2014', 'short': 'OUG nr. 3/2014', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True,
        # the form's notes read "Art. 24 din LEGEA nr. 304/2004 ... a fost modificat de ... LEGEA nr. 58/2016": the
        # link before "a fost ... de" names the amended act, not the amending one
        'rect_after': True,
        'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/155316',
        'in_force': '2014-02-07', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 98 of 7 February 2014; an '
                     'emergency ordinance with no day of its own, in force on publication (Constituția art. 115 '
                     'alin. (5); Legea nr. 24/2000 art. 12 alin. (2)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 3/2014: the first version is the emergency ordinance as published in Monitorul Oficial nr. 98 '
            'of 7 February 2014 (DetaliiDocumentAfis/155316), dated 7 February 2014: an emergency ordinance with no '
            'day of its own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 '
            'alin. (2)). The portal holds no consolidated form before 17 April 2016, so the changes made up to then '
            'arrive together that day.',
            'OUG nr. 3/2014: the one consolidated form the portal lists, of 17 April 2016 (178364), has no captured '
            'DetaliiDocument page, so it is read from its DetaliiDocumentAfis page (capture 20251113001642), which '
            'is headed "actualizată până la data de 17 aprilie 2016" and prints the amendment notes of Legea nr. '
            '58/2016 that the form carries. It is the same text and notes as the form\'s own page would show.',
            'OUG nr. 3/2014: the emergency ordinance numbers its own articles in Roman numerals (I, II, ...); each '
            'is kept under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in '
            'order. The articles of other acts it quotes stay in the text of the article that quotes them. The '
            'signature block after the last article is not text.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/155316: "ORDONANȚĂ DE URGENȚĂ nr. 3 din 5 februarie
    # 2014", MO nr. 98 din 7 februarie 2014)
    P.BASE_LAWS[SLUG] = {
        'label': 'OUG nr. 3/2014', 'kind': 'decree',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 98 din 7 februarie 2014',
        'enacted': '2014-02-05', 'published': '2014-02-07', 'url': P.PORTAL + 'DetaliiDocumentAfis/155316',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
