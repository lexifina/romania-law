"""Ordonanța de urgență a Guvernului nr. 84/2016 pentru modificarea și completarea unor acte normative din domeniul financiar-fiscal (Lexifina, 2026-11-02)."""
SLUG = 'oug-84-2016'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, **{'hg_notes': True,
 'trailing_notes': True,
 'sign_tail': True,
 'quoted_articles': True,
 'titles': False,
 'roman_articles': True,
 'part': '9z-oug-84-2016',
 'short': 'OUG nr. 84/2016',
 'pad': 3,
 'cc_forms': True,
 'root_word': 'act page',
 'title': 'Ordonanța de urgență a Guvernului nr. 84/2016 pentru modificarea și completarea unor acte normative '
          'din domeniul financiar-fiscal',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocument/184310',
 'in_force': '2016-12-06',
 'first_law': 'oug-84-2016',
 'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 977 of 6 December 2016; an '
              'emergency ordinance with no day of its own, in force on publication (Constituția art. 115 alin. '
              '(5); Legea nr. 24/2000 art. 12 alin. (2)).',
 'form_note': {},
 'republished': {},
 'decisions': [
     'OUG nr. 84/2016: the first version is the emergency ordinance as published in Monitorul Oficial nr. 977 of 6 '
     'December 2016 (DetaliiDocumentAfis/184310), dated 6 December 2016: an emergency ordinance with no day of its '
     'own, in force on publication (Constituția art. 115 alin. (5); Legea nr. 24/2000 art. 12 alin. (2)). The portal '
     'holds one consolidated form, of 5 May 2017, so the changes made up to then arrive together that day.',
     'OUG nr. 84/2016: the emergency ordinance numbers its own articles in Roman numerals (I, II, ...); each is kept '
     'under its Roman title and filed by its value (art-001 for Articolul I), so the files sort in order. The '
     'articles of other acts it quotes stay in the text of the article that quotes them.',
     'OUG nr. 84/2016: the form of 5 May 2017 (188272) changes art. II (art-002) in two places, each marked by a '
     'portal note that names Legea nr. 82/2017 (Monitorul Oficial nr. 313 of 2 May 2017, art. unic pct. 1 and 2): '
     'the new art. 229 of the Codul de procedură fiscală, with its added alin. (2) on bank garnishment, and alin. '
     '(4) of art. 236 ("la plătitorul venitului ... în condițiile Codului de procedură civilă"). Legea nr. 82/2017, '
     'read as published (DetaliiDocumentAfis/188706), gives that wording word for word; the change is credited to it.',
     'OUG nr. 84/2016: every other difference between the text as published and the form of 5 May 2017, in arts. I '
     'and II, is the publisher\'s typesetting and is credited to no law: the heading of a quoted article is run onto '
     'one line with its title ("Articolul 132 Obligații declarative ale ..." for "Articolul 132" and the title on '
     'separate lines), and the lines of dots the text as published prints as "(...)" are printed with a different '
     'number of dots. Nothing of the wording changes in those places.',
 ],
 'repeal_acts': {}},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {'label': 'OUG nr. 84/2016',
 'kind': 'decree',
 'title': 'Ordonanța de urgență a Guvernului nr. 84/2016 pentru modificarea și completarea unor acte normative '
          'din domeniul financiar-fiscal, publicată în Monitorul Oficial al României, Partea I, nr. 977 din 6 '
          'decembrie 2016',
 'enacted': '2016-11-16',
 'published': '2016-12-06',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/184310'})
