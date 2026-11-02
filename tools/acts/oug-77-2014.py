"""OUG nr. 77/2014 privind procedurile naționale în domeniul ajutorului de stat (state aid procedures): Lexifina,
2026-11-02.

Act page 163659, also its base text (DetaliiDocumentAfis/163659). 7 forms 29.12.2014 .. 29.07.2024, all held
(forms.d/oug-77-2014.json, listed from DetaliiDocumentAfis/163659)."""
SLUG = 'oug-77-2014'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-77-2014', 'short': 'OUG nr. 77/2014', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'root_word': 'act page',
        'title': 'Ordonanța de urgență a Guvernului nr. 77/2014 privind procedurile naționale în domeniul ajutorului '
                 'de stat, precum și pentru modificarea și completarea Legii concurenței nr. 21/1996',
        'url': P.PORTAL + 'DetaliiDocument/163659',
        'in_force': '2015-01-01', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 893 of 9 December 2014; its arts. '
                     '1-49 take effect on 1 January 2015 (its art. 51 alin. (1)), arts. 50 and 51 on publication.',
        # the portal's form of 29.12.2014 is the text as rectified in Monitorul Oficial nr. 954 of 29 December 2014,
        # before arts. 1-49 took effect: read as of 1 January 2015, after the text as published
        'read_on': {'164327': '2015-01-01'},
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 77/2014: the first version is the emergency ordinance as published in Monitorul Oficial nr. 893 '
            'of 9 December 2014 (DetaliiDocumentAfis/163659), dated 1 January 2015, when its arts. 1-49 take effect '
            '(its art. 51 alin. (1)). Arts. 50 (which amends Legea concurenței nr. 21/1996) and 51 took effect on '
            'publication, 9 December 2014; they are shown from 1 January 2015 with the rest.',
            'OUG nr. 77/2014: the portal\'s form of 29 December 2014 is the text as rectified in Monitorul Oficial nr. '
            '954 of 29 December 2014, published before arts. 1-49 took effect. It is read as of 1 January 2015, the '
            'same day as the text as published and after it, so the rectified text is the one in force from that '
            'day; its changes are credited to the rectification, as the portal\'s notes say.',
            'OUG nr. 77/2014: art. 50 quotes the articles of Legea nr. 21/1996 it rewrites; the quoted articles are '
            'kept as art. 50\'s text.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/163659)
        'label': 'OUG nr. 77/2014', 'kind': 'decree',
        'title': 'Ordonanța de urgență a Guvernului nr. 77/2014 privind procedurile naționale în domeniul ajutorului '
                 'de stat, precum și pentru modificarea și completarea Legii concurenței nr. 21/1996, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 893 din 9 decembrie 2014',
        'enacted': '2014-12-03', 'published': '2014-12-09', 'url': P.PORTAL + 'DetaliiDocumentAfis/163659',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
