"""Legea nr. 263/2010 privind sistemul unitar de pensii publice (Lexifina, 2026-11-02).

Act page 124530, also its base text (DetaliiDocumentAfis/124530); 73 consolidated forms 2010-12-30 .. 31.08.2023, all
held (forms.d/legea-263-2010.json, listed from the act page's capture showing 31.08.2023). Parsed as the Phase 6 acts.
Repealed in full by Legea nr. 360/2023 (acts/legea-360-2023.py) from 1 September 2024 (act_repeal).
"""
SLUG = 'legea-263-2010'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-263-2010', 'short': 'Legea nr. 263/2010', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 263/2010 privind sistemul unitar de pensii publice',
        'url': P.PORTAL + 'DetaliiDocument/124530',
        'in_force': '2011-01-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 852 of 20 December 2010, in force on 1 January '
                     '2011 (its art. 193 alin. (1)), save art. 70 alin. (1), art. 132, 135 and 194, which took effect '
                     'on 23 December 2010.',
        'form_note': {}, 'republished': {},
        # the portal lists this form under 01.10.2008; its text is the law updated to 24 June 2012
        'form_date': {'138601': '2012-06-24'},
        # the portal prints "la 12-07-2021" on the note of art. 149 alin. (2) (forms 2019-07-20 .. 2021); its sibling
        # note on alin. (1) and its editorial note give 12 July 2019, the day art. 183 alin. (1) of Legea nr. 127/2019
        # took effect
        'note_date_fix': [('2021-07-12', '2019-07-12', 'Articolul 183 din LEGEA nr. 127 din 8 iulie 2019')],
        'decisions': [],
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 263/2010', 'kind': 'law',
        'title': 'Legea nr. 263 din 16 decembrie 2010, publicată în Monitorul Oficial al României, Partea I, nr. 852 '
                 'din 20 decembrie 2010',
        'enacted': '2010-12-16', 'published': '2010-12-20', 'url': P.PORTAL + 'DetaliiDocument/124530',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
