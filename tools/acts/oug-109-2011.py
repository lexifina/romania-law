"""OUG nr. 109/2011 on the corporate governance of public enterprises: Lexifina, 2026-11-02.

The act page 304455 is the newest form (09.12.2025); the base text is DetaliiDocumentAfis/133685. 17 forms 04.06.2013 ..
09.12.2025, all held from Common Crawl (forms.d/oug-109-2011.json, forms listed by the capture of page 268345)."""

SLUG = 'oug-109-2011'
TITLE = 'Ordonanța de urgență a Guvernului nr. 109/2011 privind guvernanța corporativă a întreprinderilor publice'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-109-2011', 'short': 'OUG nr. 109/2011', 'pad': 3, 'cc_forms': True, 'trailing_notes': True,
        'sign_tail': True, 'selfclosed_body': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/304455',
        'in_force': '2011-12-14', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 883 of 14 December 2011; it sets no '
                     'day of its own, so in force on publication.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 109/2011: the first version is the emergency ordinance as published in Monitorul Oficial nr. 883 '
            'of 14 December 2011 (DetaliiDocumentAfis/133685), dated 14 December 2011: it sets no in-force day of its '
            'own, so in force on publication. The portal\'s first consolidated form is of 4 June 2013, so the changes '
            'made up to then arrive together that day.',
            'OUG nr. 109/2011: approved with amendments by Legea nr. 111/2016; the portal\'s notes date its changes '
            'with the form that carries them, and each change is credited to the act the note names.',
            'OUG nr. 109/2011: the form of 4 June 2013 prints art. 65 with an empty body element and its two '
            'paragraphs just after it, so the paragraphs are read as the article\'s text.',
            'OUG nr. 109/2011: the signature block printed after the last article ("PRIM-MINISTRU ...") is not part of '
            'the article.',
        ],
        'repeal_acts': {},
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'OUG nr. 109/2011', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 109/2011 privind guvernanța corporativă a întreprinderilor '
                 'publice, publicată în Monitorul Oficial al României, Partea I, nr. 883 din 14 decembrie 2011',
        'enacted': '2011-11-30', 'published': '2011-12-14', 'url': P.PORTAL + 'DetaliiDocumentAfis/133685',
    }
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
