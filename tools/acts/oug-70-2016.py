"""Ordonanța de urgență a Guvernului nr. 70/2016 (Lexifina, 2026-11-02)."""
SLUG = 'oug-70-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, **{'hg_notes': True,
 'trailing_notes': True,
 'sign_tail': True,
 'quoted_articles': True,
 'titles': False,
 'roman_articles': True,
 'part': '9z-oug-70-2016',
 'short': 'OUG nr. 70/2016',
 'pad': 3,
 'cc_forms': True,
 'root_word': 'act page',
 'title': 'Ordonanța de urgență a Guvernului nr. 70/2016 pentru modificarea și completarea Codului de procedură '
          'penală și a Legii nr. 304/2004 privind organizarea judiciară',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocument/183142',
 'in_force': '2016-10-31',
 'first_law': 'oug-70-2016',
 'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 866 of 31 October 2016; an '
              'emergency ordinance with no day of its own, in force on publication (Constituția art. 115 alin. '
              '(5); Legea nr. 24/2000 art. 12 alin. (2)).',
 'form_note': {},
 'republished': {},
 'decisions': [
     'OUG nr. 70/2016: the first version is the emergency ordinance as published in Monitorul Oficial nr. 866 of 31 '
     'October 2016 (DetaliiDocumentAfis/183142), dated 31 October 2016: an emergency ordinance with no day of its '
     'own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 alin. (2)). The portal '
     'holds no consolidated form before 29 May 2019, so what the forms print differently arrives together that day.',
     'OUG nr. 70/2016: the emergency ordinance numbers its own articles in Roman numerals (I, II, ...); each is kept '
     'under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
     'articles of other acts it quotes stay in the text of the article that quotes them.',
     'OUG nr. 70/2016: the form of 29 May 2019 (214247) prints no note, and it differs from the text as published in '
     'arts. I and II only in how the quoted articles of the Codul de procedură penală and of Legea nr. 304/2004 are '
     'typeset: the text as published opens each with its number and a dash inside quotation marks ("Art. 434. - (1) '
     '...") and closes it with a quotation mark, and the form prints "Articolul 434" and the provisions without the '
     'quotation marks; the lines of dots that stand for omitted text are printed with a different number of dots. '
     'The wording is the same word for word. The change is the publisher\'s and credited to no law. The form of 13 '
     'July 2019 (216989) prints the same text and is unchanged.',
 ],
 'repeal_acts': {}},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {'label': 'OUG nr. 70/2016',
 'kind': 'decree',
 'title': 'Ordonanța de urgență a Guvernului nr. 70/2016 pentru modificarea și completarea Codului de procedură '
          'penală și a Legii nr. 304/2004 privind organizarea judiciară, publicată în Monitorul Oficial al '
          'României, Partea I, nr. 866 din 31 octombrie 2016',
 'enacted': '2016-10-26',
 'published': '2016-10-31',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/183142'})
