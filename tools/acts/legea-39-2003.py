"""Legea nr. 39/2003 privind prevenirea și combaterea criminalității organizate (Lexifina, 2026-11-02).

Act page 41478, also its base text (DetaliiDocumentAfis/41478); 3 consolidated forms 27.07.2006 .. 01.02.2014, all held
(forms.d/legea-39-2003.json, listed from DetaliiDocumentAfis/41478: no capture of the act page itself). Parsed as the
Phase 6 acts. Legea nr. 187/2012 (the law putting the 2009 Penal Code into force, 01.02.2014) is credited under its
existing law key, legea-187-2012, from the portal's notes.
"""
SLUG = 'legea-39-2003'
TITLE = 'Legea nr. 39/2003 privind prevenirea și combaterea criminalității organizate'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-39-2003', 'short': 'Legea nr. 39/2003', 'pad': 3,
        'cc_forms': True, 'root_word': 'act page',
        # arts. 27-30 amend other acts; the form of 01.02.2014 prints each article they quote as an article nested
        # inside the amending one
        'quoted_articles': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/41478',
        'in_force': '2003-02-28', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 50 of 29 January 2003, in force 30 days after '
                     'publication (its art. 33): 28 February 2003.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 39/2003: the first version is the law as published in Monitorul Oficial nr. 50 of 29 January '
            '2003 (DetaliiDocumentAfis/41478), in force 30 days after publication (its art. 33): 28 February 2003. '
            'The portal\'s first form is of 27 July 2006, so the changes made up to then arrive together that day.',
            'Legea nr. 39/2003: no capture of the act page itself (DetaliiDocument/41478) is held; its forms are those '
            'listed by its base text\'s page (DetaliiDocumentAfis/41478), each read from its own page.',
            'Legea nr. 39/2003: the form of 27 July 2006 prints no amendment note; its changes (arts. 6, 18, 19, 20, 23, '
            '24) are diacritics and spelling only, the publisher\'s.',
            'Legea nr. 39/2003: the changes of 1 February 2014, the day the 2009 Penal Code and Code of Criminal '
            'Procedure took effect, are credited as the portal\'s notes name them: Legea nr. 187/2012, art. 126 (art. 2 '
            'lit. a) and b); arts. 7-10 and 13 repealed), and Legea nr. 255/2013, art. 60 (arts. 11, 14-19 and 23 '
            'repealed).',
            'Legea nr. 39/2003: arts. 27-30 amend other acts. The form of 1 February 2014 prints each article they '
            'quote as an article nested in the amending one ("Articolul 17" for "Art. 17. -"), without the quotation '
            'marks; the quoted article is kept as the amending article\'s text, on its own lines. That change of '
            'layout is the publisher\'s.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/41478, Common Crawl 20251205142622)
        'label': 'Legea nr. 39/2003', 'kind': 'law',
        'title': 'Legea nr. 39/2003 privind prevenirea și combaterea criminalității organizate, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 50 din 29 ianuarie 2003',
        'enacted': '2003-01-21', 'published': '2003-01-29', 'url': P.PORTAL + 'DetaliiDocumentAfis/41478',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
