"""Legea nr. 176/2010 privind integritatea în exercitarea funcțiilor și demnităților publice (Lexifina, 2026-11-02).

Act page 303284 (forms 03.05.2013 .. 22.11.2025, all held in forms.d/legea-176-2010.json); base text
DetaliiDocumentAfis/121924. Parsed as the Phase 6 acts.
"""
SLUG = 'legea-176-2010'
TITLE = ('Legea nr. 176/2010 privind integritatea în exercitarea funcțiilor și demnităților publice, pentru '
         'modificarea și completarea Legii nr. 144/2007 privind înființarea, organizarea și funcționarea Agenției '
         'Naționale de Integritate, precum și pentru modificarea și completarea altor acte normative')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-176-2010', 'short': 'Legea nr. 176/2010', 'pad': 3, 'cc_forms': True,
        # titles II and III rewrite articles of Legea nr. 144/2007 and Legea nr. 115/1996 and quote them
        'quoted_articles': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/303284',
        'in_force': '2010-09-05', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 621 of 2 September 2010; it sets no day of its '
                     'own, so in force 3 days after publication (Constituția art. 78): 5 September 2010.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 176/2010: the first version is the law as published in Monitorul Oficial nr. 621 of 2 '
            'September 2010 (DetaliiDocumentAfis/121924), dated 5 September 2010: it sets no day of its own, so 3 '
            'days after publication (Constituția art. 78). The portal\'s first form is of 3 May 2013, so the '
            'changes made up to then arrive together that day.',
            'Legea nr. 176/2010: the articles of other acts that the amending provisions quote (S_ART inside the '
            'amending article) are kept as part of the amending article\'s text, as printed.',
            'Legea nr. 176/2010: the portal prints the quoted provisions of arts. 33 and 35 (title III) now between '
            'quotation marks as "Art. N. - ..." and now as nested articles titled "Articolul N"; the changes between '
            'those two printings (2013, 2014, 2018, 2019) alter no provision and are committed as the publisher\'s, '
            'uncredited.',
        ],
        'repeal_acts': {},
        'root_word': 'act page',
    }
    # dates read from the act as published (DetaliiDocumentAfis/121924: "București, 1 septembrie 2010. Nr. 176.",
    # Monitorul Oficial nr. 621 din 2 septembrie 2010)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea nr. 176/2010', 'kind': 'law',
        'title': 'Legea nr. 176 din 1 septembrie 2010, publicată în Monitorul Oficial al României, Partea I, nr. 621 '
                 'din 2 septembrie 2010',
        'enacted': '2010-09-01', 'published': '2010-09-02', 'url': P.PORTAL + 'DetaliiDocumentAfis/121924',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
