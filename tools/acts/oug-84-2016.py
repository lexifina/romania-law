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
 'decisions': ['@@DECISIONS@@'],
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
