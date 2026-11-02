"""Legea nr. 101/2016 privind remediile și căile de atac în materie de achiziții publice și CNSC (Lexifina,
2026-11-02).

Act page 178680 is also its base text (DetaliiDocumentAfis/178680); no republication; 10 forms, all held from Common
Crawl. forms.d/legea-101-2016.json.
"""
SLUG = 'legea-101-2016'
TITLE = ('Legea nr. 101/2016 privind remediile și căile de atac în materie de atribuire a contractelor de achiziție '
         'publică, a contractelor sectoriale și a contractelor de concesiune de lucrări și concesiune de servicii, '
         'precum și pentru organizarea și funcționarea Consiliului Național de Soluționare a Contestațiilor')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-101-2016', 'short': 'Legea nr. 101/2016', 'pad': 3, 'titles': False,
        'trailing_notes': True, 'cc_forms': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/178680',
        'in_force': '2016-05-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 393 of 23 May 2016; it sets no day of its own, so '
                     'in force 3 days after publication (Constituția art. 78): 26 May 2016.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 101/2016: the first version is the law as published in Monitorul Oficial nr. 393 of 23 May 2016 '
            '(DetaliiDocumentAfis/178680), dated 26 May 2016: it sets no in-force day of its own, so 3 days after '
            'publication (Constituția art. 78). The portal holds no consolidated form before 22 December 2017, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 101/2016: the portal prints some repeal notes just after the article they concern ("Articolul '
            '61^2 ... a fost abrogat de Punctul 25, Articolul IV din ORDONANȚA DE URGENȚĂ nr. 23 ..."); they are read '
            'as that article\'s notes.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/178680, Common Crawl 20251116033705)
        'label': 'Legea nr. 101/2016', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 393 din 23 mai 2016',
        'enacted': '2016-05-19', 'published': '2016-05-23', 'url': P.PORTAL + 'DetaliiDocumentAfis/178680',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
