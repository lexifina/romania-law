"""Legea nr. 343/2006 (Lexifina, 2026-11-02)."""
SLUG = 'legea-343-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, **{'hg_notes': True,
 'trailing_notes': True,
 'sign_tail': True,
 'quoted_articles': True,
 'titles': False,
 'roman_articles': True,
 'part': '9z-legea-343-2006',
 'short': 'Legea nr. 343/2006',
 'pad': 3,
 'cc_forms': True,
 'root_word': 'act page',
 'title': 'Legea nr. 343/2006',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocument/73981',
 'in_force': '2006-08-04',
 'first_law': 'legea-343-2006',
 'base_note': 'The law as published in Monitorul Oficial nr. 662 of 1 August 2006; it sets no day of its own, '
              'so in force 3 days after publication (Constituția art. 78): 4 August 2006.',
 'form_note': {},
 'republished': {},
 'decisions': ['@@DECISIONS@@'],
 'repeal_acts': {}},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault(SLUG, {'label': 'Legea nr. 343/2006',
 'kind': 'law',
 'title': 'Legea nr. 343/2006, publicată în Monitorul Oficial al României, Partea I, nr. 662 din 1 august 2006',
 'enacted': '2006-07-17',
 'published': '2006-08-01',
 'url': 'https://legislatie.just.ro/Public/DetaliiDocumentAfis/73981'})
