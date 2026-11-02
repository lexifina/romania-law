"""OUG nr. 111/2011 privind comunicațiile electronice (Lexifina, 2026-11-02).

Act page 134098, also its base text (DetaliiDocumentAfis/134098); 19 consolidated forms 26.07.2012 .. 31.12.2024
(forms.d/oug-111-2011.json). Parsed as the Phase 6 acts.
"""
SLUG = 'oug-111-2011'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-111-2011', 'short': 'OUG nr. 111/2011', 'pad': 3, 'cc_forms': True,
        'title': 'Ordonanța de urgență a Guvernului nr. 111/2011 privind comunicațiile electronice',
        'url': P.PORTAL + 'DetaliiDocument/134098',
        'in_force': '2011-12-27', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 925 of 27 December 2011; it sets '
                     'no day of its own for the whole, so in force on publication.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 111/2011: the first version is the emergency ordinance as published in Monitorul Oficial nr. 925 '
            'of 27 December 2011 (DetaliiDocumentAfis/134098), dated 27 December 2011: it sets no in-force day of its '
            'own for the whole, so in force on publication. Its art. 160 alin. (1) puts art. 50 alin. (1)-(3), art. 51 '
            'alin. (1)-(5), arts. 53-58 and art. 60 alin. (1)-(4) in force 60 days after publication; they are shown '
            'from the first day with the rest of the text.',
            'OUG nr. 111/2011: the portal\'s first consolidated form is of 26 July 2012, so the changes made up to then '
            'arrive together that day.',
            'OUG nr. 111/2011: its annexes (Anexele nr. 1 and 2, art. 157) are not articles and are not read.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/134098)
        'label': 'OUG nr. 111/2011', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 111/2011 privind comunicațiile electronice, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 925 din 27 decembrie 2011',
        'enacted': '2011-12-14', 'published': '2011-12-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/134098',
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
