"""Legea nr. 86/2006 privind Codul vamal al României (Lexifina, 2026-11-02).

The code's page 70955 (COD VAMAL) lists its 13 consolidated forms, 07.04.2009 .. 18.12.2025; the law's own pages
(70964, and its form pages 104495 ... 304528) only frame the code's forms. Base text: the law as published,
DetaliiDocumentAfis/70964. All forms held (forms.d/legea-86-2006.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-86-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-86-2006', 'short': 'Codul vamal (Legea nr. 86/2006)', 'pad': 3,
        'cc_forms': True,
        'trailing_notes': True,  # the repeal notes of OUG nr. 96/2020 are printed after each "Abrogat." article
        'title': 'Legea nr. 86/2006 privind Codul vamal al României',
        'url': P.PORTAL + 'DetaliiDocument/70955',
        'in_force': '2006-06-18', 'first_law': SLUG,
        'base_note': 'The code as published in Monitorul Oficial nr. 350 of 19 April 2006, in force 60 days after '
                     'publication (its art. 288 alin. (1)): 18 June 2006.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Codul vamal (Legea nr. 86/2006): the first version is the law as published in Monitorul Oficial nr. 350 '
            'of 19 April 2006 (DetaliiDocumentAfis/70964), in force 60 days after publication (its art. 288 alin. '
            '(1)): 18 June 2006. Art. 288 alin. (4) puts art. 245 alin. (2) and (3), art. 247, art. 252 and art. 255 '
            'alin. (2) and (3) in force on Romania\'s accession to the European Union (1 January 2007); they are '
            'shown from 18 June 2006, as the law prints them. The portal\'s first form is of 7 April 2009, so the '
            'changes made up to then arrive together that day.',
            'Codul vamal (Legea nr. 86/2006): the portal keeps the code as its own document (DetaliiDocument/70955, '
            '"CODUL VAMAL"); the pages of the law (DetaliiDocument/70964 and its form pages) only frame the code\'s '
            'forms, so the forms are read from the code\'s pages. The form of 18 December 2025 (304529) is read '
            'from its DetaliiDocumentAfis page as captured on 10 February 2026 (Internet Archive 20260210135951), '
            'which shows that form as the newest and lists every earlier one.',
            'Codul vamal (Legea nr. 86/2006): the law as published and the forms to 29 June 2013 print, after art. 288 '
            'alin. (4), the note "* Prezenta lege asigură aplicarea Regulamentului Consiliului (CEE) nr. 2.913/92 de '
            'instituire a Codului vamal comunitar ..."; it says which EU act the law implements and is not an '
            'article\'s text, so it is left out.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/70964, Common Crawl 20260123204237)
        'label': 'Legea nr. 86/2006', 'kind': 'law',
        'title': 'Legea nr. 86/2006 privind Codul vamal al României, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 350 din 19 aprilie 2006',
        'enacted': '2006-04-10', 'published': '2006-04-19', 'url': P.PORTAL + 'DetaliiDocumentAfis/70964',
    }
    # the law's note that it implements Regulation (EEC) nr. 2913/92, printed after art. 288 alin. (4) by the base text
    # and the forms to 29.06.2013 (left out from 01.02.2014): not the code's text
    P.EDITORIAL_LINES[SLUG] = {'art-288': ('*', 'Prezenta lege asigură aplicarea Regulamentului Consiliului (CEE) nr. '
                                                '2.913/92')}
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
