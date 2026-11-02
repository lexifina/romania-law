"""Legea nr. 241/2005 pentru prevenirea și combaterea evaziunii fiscale (Lexifina, 2026-11-02).

Act page 63590, also its base text (DetaliiDocumentAfis/63590); 9 consolidated forms 23.06.2010 .. 16.05.2024, all held
(forms.d/legea-241-2005.json). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-241-2005'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-241-2005', 'short': 'Legea nr. 241/2005', 'pad': 3,
        'cc_forms': True,
        'reprint_notes': True,  # the 2014 form reprints OUG nr. 54/2010's note on art. 2 as "Lit. g)" for "Litera g)"
        'title': 'Legea nr. 241/2005 pentru prevenirea și combaterea evaziunii fiscale',
        'url': P.PORTAL + 'DetaliiDocument/63590',
        'in_force': '2005-08-26', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 672 of 27 July 2005, in force 30 days after '
                     'publication (its art. 15): 26 August 2005.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 241/2005: the first version is the law as published in Monitorul Oficial nr. 672 of 27 July '
            '2005 (DetaliiDocumentAfis/63590), in force 30 days after publication (its art. 15): 26 August 2005. The '
            'portal\'s first form is of 23 June 2010, so the changes made up to then arrive together that day.',
            'Legea nr. 241/2005: the act page as captured on 30 June 2026 (Internet Archive 20260630175020) still '
            'shows the form of 16 May 2024 as the newest.',
            'Legea nr. 241/2005: Decizia Curții Constituționale nr. 363/2015 (Monitorul Oficial nr. 495 of 6 July '
            '2015) found art. 6 unconstitutional; under Constituția art. 147 alin. (1) it ceased to have effect 45 '
            'days after publication, on 20 August 2015. The portal\'s next form, of 21 August 2015, prints art. 6 as '
            '"Încetat efectele juridice." with a note naming the decision; the change is dated by that form and '
            'credited to the decision.',
            'Legea nr. 241/2005: the changes no note explains (art. 9 on 23 June 2010; arts. 2, 8, 9, 13, 14 and 16 '
            'on 1 February 2014) differ from the text before only in diacritics and spelling, the publisher\'s '
            'typesetting. The form of 1 February 2014 reprints the note on art. 2 (OUG nr. 54/2010) as "Lit. g) a '
            'art. 2 ..." where earlier forms print "Litera g) a art. 2 ..."; it is the same note, so that change is '
            'not credited to the ordinance.',
        ],
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/63590, Common Crawl 20260115080825)
        'label': 'Legea nr. 241/2005', 'kind': 'law',
        'title': 'Legea nr. 241/2005 pentru prevenirea și combaterea evaziunii fiscale, publicată în Monitorul '
                 'Oficial al României, Partea I, nr. 672 din 27 iulie 2005',
        'enacted': '2005-07-15', 'published': '2005-07-27', 'url': P.PORTAL + 'DetaliiDocumentAfis/63590',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
