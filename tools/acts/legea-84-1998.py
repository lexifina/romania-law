"""Legea nr. 84/1998 privind mărcile și indicațiile geografice (Lexifina, 2026-11-02).

Act page 119052 (also the republication of 2010). 12 forms 28.12.2005 .. 07.03.2024 listed by DetaliiDocumentAfis/119052
as captured on 2026-01-18, all held (forms.d/legea-84-1998.json). The portal holds no text as first published, so the
record starts at its oldest form (no_base).
"""
SLUG = 'legea-84-1998'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-84-1998', 'short': 'Legea nr. 84/1998', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 84/1998 privind mărcile și indicațiile geografice',
        'url': P.PORTAL + 'DetaliiDocument/119052',
        'no_base': True, 'in_force': '2005-12-28', 'first_law': None, 'revert_credit': True,
        'earlier_laws': [SLUG],
        'base_note': 'Oldest version available: the portal\'s consolidated form of 28 December 2005. The law was '
                     'enacted on 15 April 1998 and first published in Monitorul Oficial nr. 161 of 23 April 1998; that '
                     'text is not held.',
        'form_note': {'119052': 'The law as republished in Monitorul Oficial nr. 350 of 27 May 2010 under art. V of '
                                'Legea nr. 66/2010, with renumbered articles.',
                      '158000': 'The law as republished in Monitorul Oficial nr. 337 of 8 May 2014 under art. 248 of '
                                'Legea nr. 187/2012, with renumbered articles.',
                      '230312': 'The law as republished in Monitorul Oficial nr. 856 of 18 September 2020 under art. IV '
                                'of Legea nr. 112/2020, with renumbered articles.'},
        'republished': {'119052': 'legea-66-2010', '158000': 'legea-187-2012', '230312': 'legea-112-2020'},
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS.setdefault(SLUG, {  # from the heading of the republication of 2010 (DetaliiDocumentAfis/119052)
        'label': 'Legea nr. 84/1998', 'kind': 'law',
        'title': 'Legea nr. 84/1998 privind mărcile și indicațiile geografice, publicată în Monitorul Oficial al '
                 'României, Partea I, nr. 161 din 23 aprilie 1998',
        'enacted': '1998-04-15', 'published': '1998-04-23', 'url': None,
    })
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
