"""Legea nr. 303/2022 privind statutul judecătorilor și procurorilor (Lexifina, 2026-11-02).

Act page 261399, also its base text (DetaliiDocumentAfis/261399); 6 consolidated forms 01.01.2024 .. 02.03.2026, all
held (forms.d/legea-303-2022.json). Parsed as the Phase 6 acts.
It replaced Legea nr. 303/2004 (part 99v), which its art. 294 alin. (5) lit. a) repeals.
"""
SLUG = 'legea-303-2022'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-303-2022', 'short': 'Legea nr. 303/2022', 'pad': 3, 'cc_forms': True,
        'title': 'Legea nr. 303/2022 privind statutul judecătorilor și procurorilor',
        'url': P.PORTAL + 'DetaliiDocument/261399',
        'in_force': '2022-12-16', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 1102 of 16 November 2022, in force 30 days after '
                     'publication (its art. 294 alin. (1)): 16 December 2022.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 303/2022: the first version is the law as published in Monitorul Oficial nr. 1102 of 16 '
            'November 2022 (DetaliiDocumentAfis/261399), in force 30 days after publication (its art. 294 alin. '
            '(1)): 16 December 2022. The portal\'s first form is of 1 January 2024, so the changes made up to then '
            'arrive together that day.',
            'Legea nr. 303/2022: art. 294 alin. (2) puts off to a later day (1 January 2026 as published; 1 January '
            '2027 from 31 December 2025, as OUG nr. 93/2025 amended it) only the rule on counting service without '
            'the time spent as a trainee judge or prosecutor (auditor de justiție); it names no provision of its '
            'own, so no article is given a later day.',
            'Legea nr. 303/2022: the forms of 30 June and 14 August 2025 add the portal\'s note on Decizia Curții '
            'Constituționale nr. 203/2025 (Monitorul Oficial nr. 611 of 30 June 2025), which holds the phrase "care '
            'au făcut parte din serviciile de informații" in arts. 108 alin. (6), 142 alin. (4), 144 alin. (2) and '
            '150 alin. (4) constitutional only as far as it means the intelligence services before 1990; the note '
            'says that phrase ceased to have effect from 14 August 2025, but every later form prints the articles '
            'unchanged, so the text is kept as printed. Those forms, and the form of 1 January 2025, change no '
            'article and add no version.',
        ],
    }
    # as the portal's note links name it (the same entry part 99w carries for Legea nr. 304/2022); dates read from
    # the act as published (DetaliiDocumentAfis/261399)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 303/2022',
        'title': 'Legea nr. 303 din 15 noiembrie 2022, publicată în Monitorul Oficial al României, Partea I, nr. 1102 '
                 'din 16 noiembrie 2022',
        'kind': 'law', 'enacted': '2022-11-15', 'published': '2022-11-16', 'url': P.PORTAL + 'DetaliiDocument/261399',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
