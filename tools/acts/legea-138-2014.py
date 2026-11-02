"""Legea nr. 138/2014 pentru modificarea și completarea Legii nr. 134/2010 privind Codul de procedură civilă, precum
și pentru modificarea și completarea unor acte normative conexe (Lexifina, 2026-11-02).

Act page 162199, also its base text (DetaliiDocumentAfis/162199); 4 consolidated forms (24.12.2015 .. 12.04.2016), all
held (forms.d/legea-138-2014.json). An amending act: its own articles (Art. I, II, ...) are the text, and the
provisions it inserts into other acts are quoted text.
"""
SLUG = 'legea-138-2014'

TITLE = ('Legea nr. 138/2014 pentru modificarea și completarea Legii nr. 134/2010 privind Codul de procedură civilă, '
         'precum și pentru modificarea și completarea unor acte normative conexe')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-138-2014', 'short': 'Legea nr. 138/2014', 'pad': 4, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'roman_articles': True, 'quoted_roman': True, 'quoted_lines': True, 'point_tail': True,
        'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/162199',
        'in_force': '2014-10-19', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 753 of 16 October 2014; it sets no day of its '
                     'own, so in force 3 days after publication (Constituția art. 78): 19 October 2014.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 138/2014: the first version is the law as published in Monitorul Oficial nr. 753 of 16 '
            'October 2014 (DetaliiDocumentAfis/162199), dated 19 October 2014: it sets no day of its own, so in '
            'force 3 days after publication (Constituția art. 78). The portal holds no consolidated form before 24 '
            'December 2015, so the changes made up to then arrive together that day.',
            'Legea nr. 138/2014: the law numbers its own articles in Roman numerals (I, II, ...); each is kept under '
            'its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
            'articles of other acts it quotes stay in the text of the article that quotes them. The adoption '
            'formula and the signature block after the last article are not text.',
        ],
    }
    # dates read from the act as published (DetaliiDocumentAfis/162199: "LEGE nr. 138 din 15 octombrie 2014", MO nr.
    # 753 din 16 octombrie 2014)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 138/2014', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 753 din 16 octombrie 2014',
        'enacted': '2014-10-15', 'published': '2014-10-16', 'url': P.PORTAL + 'DetaliiDocumentAfis/162199',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
