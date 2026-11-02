"""Ordonanța de urgență a Guvernului nr. 1/2016 pentru modificarea Legii nr. 134/2010 privind Codul de procedură civilă,
precum și a unor acte normative conexe (Lexifina, 2026-11-02).

Act page 175561, also its base text (DetaliiDocumentAfis/175561); one consolidated form, 24.03.2017 (187258), held
(forms.d/oug-1-2016.json). An amending act: its own articles (Art. I, II, ...) are the text, and the provisions it
inserts into other acts are quoted text.
"""
SLUG = 'oug-1-2016'

TITLE = ('Ordonanța de urgență a Guvernului nr. 1/2016 pentru modificarea Legii nr. 134/2010 privind Codul de '
         'procedură civilă, precum și a unor acte normative conexe')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-1-2016', 'short': 'OUG nr. 1/2016', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True,
        'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/175561',
        'in_force': '2016-02-04', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 85 of 4 February 2016; an '
                     'emergency ordinance with no day of its own, in force on publication (Constituția art. 115 '
                     'alin. (5); Legea nr. 24/2000 art. 12 alin. (2)).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 1/2016: the first version is the emergency ordinance as published in Monitorul Oficial nr. 85 '
            'of 4 February 2016 (DetaliiDocumentAfis/175561), dated 4 February 2016: an emergency ordinance with no '
            'day of its own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 '
            'alin. (2)). The portal holds no consolidated form before 24 March 2017, so the changes made up to then '
            'arrive together that day.',
            'OUG nr. 1/2016: the emergency ordinance numbers its own articles in Roman numerals (I, II, ...); each '
            'is kept under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in '
            'order. The articles of other acts it quotes stay in the text of the article that quotes them. The '
            'signature block after the last article is not text.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/175561: "ORDONANȚĂ DE URGENȚĂ nr. 1 din 3 februarie
    # 2016", MO nr. 85 din 4 februarie 2016)
    P.BASE_LAWS[SLUG] = {
        'label': 'OUG nr. 1/2016', 'kind': 'decree',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 85 din 4 februarie 2016',
        'enacted': '2016-02-03', 'published': '2016-02-04', 'url': P.PORTAL + 'DetaliiDocumentAfis/175561',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
