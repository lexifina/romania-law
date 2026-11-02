"""Legea nr. 64/1991 privind brevetele de invenție (Lexifina, 2026-11-02).

Act page 38939 (also the republication of 2002). 14 forms 15.01.2003 .. 27.06.2024 listed by DetaliiDocumentAfis/38939
as captured on 2026-01-14, all held (forms.d/legea-64-1991.json). The portal holds no text as first published, so the
record starts at its oldest form, the republication of 2002 (no_base).
"""
SLUG = 'legea-64-1991'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-64-1991', 'short': 'Legea nr. 64/1991', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 64/1991 privind brevetele de invenție',
        'url': P.PORTAL + 'DetaliiDocument/38939',
        'no_base': True, 'in_force': '2003-01-15', 'first_law': None, 'revert_credit': True,
        'earlier_laws': [SLUG, 'legea-203-2002'],
        'base_note': 'Oldest version available: the law as republished in Monitorul Oficial nr. 752 of 15 October 2002 '
                     'under art. III of Legea nr. 203/2002, with renumbered articles, as the portal dates it (15 '
                     'January 2003). The law was enacted on 11 October 1991 and first published in Monitorul Oficial '
                     'nr. 212 of 21 October 1991; that text is not held.',
        'form_note': {'84262': 'The law as republished in Monitorul Oficial nr. 541 of 8 August 2007 under art. IV of '
                               'Legea nr. 28/2007, with renumbered articles.',
                      '160717': 'The law as republished in Monitorul Oficial nr. 613 of 19 August 2014 under art. 18 of '
                                'Legea nr. 83/2014, with renumbered articles.',
                      '284606': 'The law as republished in Monitorul Oficial nr. 600 of 27 June 2024 under art. VI '
                                'alin. (3) of Legea nr. 30/2024, with renumbered articles.'},
        'republished': {'84262': 'legea-28-2007', '160717': 'legea-83-2014', '284606': 'legea-30-2024'},
        'decisions': [],
        'root_word': 'act page',
    }
    P.BASE_LAWS.setdefault(SLUG, {  # from the heading of the republication of 2002 (DetaliiDocumentAfis/38939)
        'label': 'Legea nr. 64/1991', 'kind': 'law',
        'title': 'Legea nr. 64/1991 privind brevetele de invenție, publicată în Monitorul Oficial al României, Partea '
                 'I, nr. 212 din 21 octombrie 1991',
        'enacted': '1991-10-11', 'published': '1991-10-21', 'url': None,
    })
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
