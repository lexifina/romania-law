"""Legea nr. 192/2006 privind medierea și organizarea profesiei de mediator (Lexifina, 2026-11-02).

Act page 71928, also its base text (DetaliiDocumentAfis/71928); 15 forms 06.12.2009 .. 29.07.2019, all held from Common
Crawl (forms.d/legea-192-2006.json; the newest is read from the act page, which shows it). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-192-2006'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-192-2006', 'short': 'Legea nr. 192/2006', 'pad': 3, 'cc_forms': True, 'cte_notes': True,
        # the notes the forms of 2013 print as paragraphs ("Alin. (1^3) al art. 2 a fost introdus de pct. 4 al art. unic
        # din LEGEA nr. 214 ...") name the act that made the change
        'mod_lines': True,
        # art. 60^1 (Legea nr. 115/2012 art. I pct. 13): put off to 1.2.2013 by OUG nr. 90/2012 art. II, then, by OUG
        # nr. 4/2013 art. VIII (31.01.2013), lit. a)-f) to the Code of Civil Procedure's day (15.02.2013) and lit. g) to
        # the Code of Criminal Procedure's (1.2.2014); the forms of 21.12.2012 and 31.01.2013 print it before its day
        'early_text': {'139562': {'absent': ('art-060-1',), 'placeholder': ()},
                       '139563': {'absent': ('art-060-1',), 'placeholder': ()}},
        'later_provisions': (
            # art. 2 alin. (1^2) (OUG nr. 90/2012, in force on publication 21.12.2012): OUG nr. 4/2013 art. VI (in force
            # on publication 31.01.2013) puts it in force on 1.8.2013; the forms print it throughout
            {'day': '2013-08-01', 'since': '2013-01-31', 'law': 'oug-4-2013', 'keys': ('art-002',),
             'lines': ('(1^2) ',),
             'since_note': 'OUG nr. 4/2013 art. VI (Monitorul Oficial nr. 68 of 31 January 2013, in force on '
                           'publication) puts art. 2 alin. (1^2) in force on 1 August 2013; it is left out until then. '
                           'The portal holds no form of this day without it: the text is read from the form before.',
             'note': 'Art. 2 alin. (1^2) takes effect on this day (OUG nr. 4/2013 art. VI); the portal already prints '
                     'it in its earlier forms.'},
            # art. 60^1 alin. (1) lit. g): in force on 1.2.2014 by OUG nr. 4/2013 art. VIII lit. b), repealed that day
            # (the form of 01.02.2014: "g) abrogată;"), so never in force; the form of 01.07.2013 prints it early
            {'day': '2014-02-01', 'law': 'oug-4-2013', 'keys': ('art-060-1',),
             'lines': ('g) în cazul infracțiunilor',), 'no_add': True, 'note': ''},
        ),
        # Decizia CCR nr. 266/2014 (Monitorul Oficial nr. 464 of 25.06.2014) finds art. 2 alin. (1) and (1^2)
        # unconstitutional: the form of that day marks both "(Alineat suspendat)" (Constituția art. 147 alin. (1)); they
        # ceased to have effect 45 days after publication, 9.8.2014 (the form of 15.07.2016 prints "Încetat efecte
        # juridice.")
        'form_credits': {'159679': {'art-002': 'dcc-266-2014'}},
        'editorial_days': {'180124': {'art-002': '2014-08-09'}},
        'title': 'Legea nr. 192/2006 privind medierea și organizarea profesiei de mediator',
        'url': P.PORTAL + 'DetaliiDocument/71928',
        'in_force': '2006-05-25', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 441 of 22 May 2006, with no day of its own, so in '
                     'force 3 days after publication (Constituția, art. 78): 25 May 2006.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 192/2006: the first version is the law as published in Monitorul Oficial nr. 441 of 22 May '
            '2006 (DetaliiDocumentAfis/71928). It sets no in-force day of its own, so it took effect 3 days after '
            'publication (Constituția of 1991 as republished, art. 78): 25 May 2006. Its art. 74 alin. (2) makes the '
            'opinion of art. 9 applicable from the publication of the training standards; no article is given a '
            'later day. The portal\'s first form is of 6 December 2009, so the changes made up to then arrive '
            'together that day.',
            'Legea nr. 192/2006: art. 60^1 was inserted by Legea nr. 115/2012 (art. I pct. 13), whose art. II put it in '
            'force 6 months after publication; OUG nr. 90/2012 art. II put that off to 1 February 2013, and OUG nr. '
            '4/2013 art. VIII (Monitorul Oficial nr. 68 of 31 January 2013, in force on publication) put lit. a)-f) '
            'off to the day the Code of Civil Procedure took effect (15 February 2013, by art. I of the same OUG) and '
            'lit. g) to the day the Code of Criminal Procedure took effect (1 February 2014). Each act was read as published (DetaliiDocumentAfis/'
            '139488, 144035, 145075). The portal\'s forms of 21 December 2012 and 31 January 2013 print art. 60^1 '
            'before its day; under the rule for text printed before its law it is left out of both, and arrives with '
            'the form of 15 February 2013 (lit. a)-f)). Lit. g), printed by the form of 1 July 2013, was due to take '
            'effect on 1 February 2014, the day the form of that day prints it repealed ("g) abrogată;", Legea nr. '
            '255/2013): it never took effect and no version shows it.',
            'Legea nr. 192/2006: art. 2 alin. (1^2), inserted by OUG nr. 90/2012 art. I pct. 2 (in force on '
            'publication, 21 December 2012), is put in force on 1 August 2013 by OUG nr. 4/2013 art. VI, in force on '
            'publication on 31 January 2013; the portal\'s forms print it throughout. It is shown from 21 December '
            '2012, left out from 31 January 2013 by a version credited to OUG nr. 4/2013 (the text otherwise that of '
            'the form before), and shown again from 1 August 2013. No wording is changed.',
            'Legea nr. 192/2006: Decizia Curții Constituționale nr. 266/2014 (Monitorul Oficial nr. 464 of 25 June '
            '2014, read as published, DetaliiDocumentAfis/159260) finds art. 2 alin. (1) and (1^2) unconstitutional. '
            'The portal\'s form of 25 June 2014 marks both "(Alineat suspendat)"; that print is kept as the portal '
            'gives it and credited to the decision. Under Constituția art. 147 alin. (1) the two provisions ceased to '
            'have effect 45 days after publication, on 9 August 2014; the change to "Încetat efecte juridice.", first '
            'printed by the form of 15 July 2016, is dated that day, credited to the decision.',
        ],
        'root_word': 'act page',
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/71928)
        'label': 'Legea nr. 192/2006', 'kind': 'law',
        'title': 'Legea nr. 192 din 16 mai 2006 privind medierea și organizarea profesiei de mediator, publicată în '
                 'Monitorul Oficial al României, Partea I, nr. 441 din 22 mai 2006',
        'enacted': '2006-05-16', 'published': '2006-05-22', 'url': P.PORTAL + 'DetaliiDocumentAfis/71928',
    }
    # read as published (DetaliiDocumentAfis/159260); the same entry the Court-decision credit rule makes
    P.BASE_LAWS.setdefault('dcc-266-2014', {
        'label': 'Decizia CCR nr. 266/2014', 'kind': 'court',
        'title': 'Decizia Curții Constituționale nr. 266 din 7 mai 2014, publicată în Monitorul Oficial al României, '
                 'Partea I, nr. 464 din 25 iunie 2014',
        'enacted': '2014-05-07', 'published': '2014-06-25', 'url': None,
    })
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
