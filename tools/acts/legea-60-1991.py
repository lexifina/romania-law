"""Legea nr. 60/1991 privind organizarea și desfășurarea adunărilor publice (Lexifina, 2026-11-02).

Act page 1532, also the text as published (DetaliiDocumentAfis/1532). Four forms 29.09.2004 .. 14.03.2014 are listed
(forms.d/legea-60-1991.json) and all are held; the act page shows the form of 11.10.2021. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-60-1991'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-60-1991', 'short': 'Legea nr. 60/1991', 'pad': 3, 'cc_forms': True,
        'hg_notes': True, 'trailing_notes': True, 'sign_tail': True, 'quoted_articles': True, 'titles': False,
        'root_word': 'act page',
        'title': 'Legea nr. 60/1991 privind organizarea și desfășurarea adunărilor publice',
        'url': P.PORTAL + 'DetaliiDocument/1532',
        'in_force': '1991-09-25', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 192 of 25 September 1991, in force on publication '
                     '(its art. 29).',
        'form_note': {'55480': 'The law as republished on 29 September 2004 under art. II of Legea nr. 31/2004.',
                      '156395': 'The law as republished on 14 March 2014 under art. 248 of Legea nr. 187/2012.'},
        'republished': {'55480': 'legea-31-2004', '156395': 'legea-187-2012'},
        'decisions': [
            'Legea nr. 60/1991: the first version is the law as published in Monitorul Oficial nr. 192 of 25 '
            'September 1991 (DetaliiDocumentAfis/1532), dated 25 September 1991: its art. 29 puts it in force on '
            'publication. The portal holds no consolidated form before 29 September 2004, so the changes made up to '
            'then arrive together that day.',
            'Legea nr. 60/1991: the republication of 29 September 2004 (55480) is credited, for the changes no note '
            'explains, to Legea nr. 31/2004, under whose art. II it was republished, as its own note says.',
            'Legea nr. 60/1991: the republication of 14 March 2014 (156395) is credited, for the changes no note '
            'explains, to Legea nr. 187/2012, under whose art. 248 it was republished, as its own note says.',
        ],
        'repeal_acts': {},
    }
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
    P.BASE_LAWS.setdefault('legea-31-2004', {  # named by the note of the republication of 2004 (form 55480)
        'label': 'Legea nr. 31/2004', 'kind': 'law',
        'title': 'Legea nr. 31/2004 pentru modificarea și completarea Legii nr. 60/1991 privind organizarea și '
                 'desfășurarea adunărilor publice, publicată în Monitorul Oficial al României, Partea I, nr. 223 din '
                 '15 martie 2004',
        'enacted': None, 'published': '2004-03-15', 'url': None,  # the cached pages give no date of adoption
    })
    P.BASE_LAWS.setdefault(SLUG, {  # from the text as published (DetaliiDocumentAfis/1532)
        'label': 'Legea nr. 60/1991', 'kind': 'law',
        'title': 'Legea nr. 60/1991, publicată în Monitorul Oficial al României, Partea I, nr. 192 din 25 septembrie '
                 '1991',
        'enacted': '1991-09-23', 'published': '1991-09-25', 'url': P.PORTAL + 'DetaliiDocumentAfis/1532',
    })
