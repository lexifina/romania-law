"""OG nr. 13/2011 (legal interest): Lexifina, 2026-11-02.

Act page 131085 is also its base text (DetaliiDocumentAfis/131085); 18 forms 30.09.2011 .. 07.08.2024, all held from
Common Crawl (forms.d/og-13-2011.json)."""

SLUG = 'og-13-2011'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-og-13-2011', 'short': 'OG nr. 13/2011', 'pad': 3, 'cc_forms': True,
        'quoted_articles': True, 'cte_notes': True, 'angle_quotes': True, 'sign_tail': True,
        'title': 'Ordonanța Guvernului nr. 13/2011 privind dobânda legală remuneratorie și penalizatoare pentru '
                 'obligații bănești, precum și pentru reglementarea unor măsuri financiar-fiscale în domeniul bancar',
        'url': P.PORTAL + 'DetaliiDocument/131085',
        'in_force': '2011-09-01', 'first_law': SLUG,
        'base_note': 'The ordinance as published in Monitorul Oficial nr. 607 of 29 August 2011, in force 3 days after '
                     'publication (its art. 19): 1 September 2011.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OG nr. 13/2011: the first version is the ordinance as published in Monitorul Oficial nr. 607 of 29 August '
            '2011 (DetaliiDocumentAfis/131085), dated 1 September 2011: its art. 19 puts it in force 3 days after '
            'publication. The provisions that article puts in force later (art. 8 alin. (3) and art. 10 on 1 October '
            '2011; art. 15 pct. 1-29 on 31 December 2011), and art. 8 alin. (2), which art. 18 alin. (4) applies only '
            'until 1 October 2011, are shown as published from 1 September 2011; no version is made for those days.',
            'OG nr. 13/2011: approved by Legea nr. 43/2012, as the portal\'s forms say ("aprobată prin Legea nr. '
            '43/2012"); no note names a change made by it, so it is credited with none.',
            'OG nr. 13/2011: the ordinance as published ends art. 19 with its note on the EU directives it transposes '
            '("* Prezenta ordonanță asigură transpunerea ..."); it is kept as printed. The rectification published in '
            'Monitorul Oficial nr. 694 of 30 September 2011 changes that note ("la cap. III-V" -> "la cap. II") and is '
            'credited from the portal\'s note. The signature block printed after it ("PRIM-MINISTRU ...") is not part '
            'of the article.',
            'OG nr. 13/2011: the forms of 30 September 2011 and 5 April 2013 print the quotation marks of terms quoted '
            'in art. 17 as "<<instituţie de credit>>", and the ordinance as published as "lt; lt;instituţie de credit '
            'gt; gt;"; both are read as quoted terms („instituție de credit”), as the later forms print them, so that '
            'no words are lost.',
            'OG nr. 13/2011: from the form of 25 October 2013 the portal prints the articles that arts. 12-17 put into '
            'other acts as articles of their own inside them ("Articolul 3", "Articolul 16^1"); they are kept as the '
            'amending article\'s text, so the layout of those articles changes that day (the publisher\'s, unexplained).',
        ],
    }
    P.BASE_LAWS[SLUG] = {
        'label': 'OG nr. 13/2011', 'kind': 'decree',
        'title': 'Ordonanța Guvernului nr. 13/2011 privind dobânda legală remuneratorie și penalizatoare pentru '
                 'obligații bănești, precum și pentru reglementarea unor măsuri financiar-fiscale în domeniul bancar, '
                 'publicată în Monitorul Oficial al României, Partea I, nr. 607 din 29 august 2011',
        'enacted': '2011-08-24', 'published': '2011-08-29', 'url': P.PORTAL + 'DetaliiDocumentAfis/131085',
    }
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
