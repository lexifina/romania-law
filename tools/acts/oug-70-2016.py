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
 'title': 'Ordonanța de urgență a Guvernului nr. 70/2016',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocument/183142',
 'in_force': '2016-10-31',
 'first_law': 'oug-70-2016',
 'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 866 of 31 October 2016; an '
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
    P.BASE_LAWS.setdefault(SLUG, {'label': 'OUG nr. 70/2016',
 'kind': 'decree',
 'title': 'Ordonanța de urgență a Guvernului nr. 70/2016, publicată în Monitorul Oficial al României, Partea '
          'I, nr. 866 din 31 octombrie 2016',
 'enacted': '2016-10-26',
 'published': '2016-10-31',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/183142'})
