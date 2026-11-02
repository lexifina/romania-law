"""Legea-cadru nr. 153/2017 privind salarizarea personalului plătit din fonduri publice (Lexifina, 2026-11-02).

Act page 190446, also its base text (DetaliiDocumentAfis/190446); 67 consolidated forms (08.12.2017 .. 01.01.2026),
55 held from Common Crawl and 12 from archive.org (forms.d/legea-153-2017.json, listed from the act page's capture
showing 01.01.2026). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-153-2017'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-153-2017', 'short': 'Legea-cadru nr. 153/2017', 'pad': 3, 'cc_forms': True,
        'root_word': 'act page',
        'title': 'Legea-cadru nr. 153/2017 privind salarizarea personalului plătit din fonduri publice',
        'url': P.PORTAL + 'DetaliiDocument/190446',
        'in_force': '2017-07-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 492 of 28 June 2017, in force on 1 July 2017 (its '
                     'art. 43).',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea-cadru nr. 153/2017: the first version is the law as published in Monitorul Oficial nr. 492 of 28 '
            'June 2017 (DetaliiDocumentAfis/190446), in force on 1 July 2017 (its art. 43).',
            'Legea-cadru nr. 153/2017: annexes I-IX (the pay families, grids and their own rules; art. 45) are not '
            'articles of the law and are not part of this record, as for the other acts; forms whose changes are all '
            'in the annexes change no article and give no version.',
            'Legea-cadru nr. 153/2017: the forms of 01.01.2025 to 07.03.2025 print, inside art. 16, the portal\'s '
            'quotation of art. I-IV and XV of OUG nr. 156/2024 ("Art. I-IV și XV din ORDONANȚA DE URGENȚĂ nr. 156 '
            '... prevăd:"), which the other forms print as a note; it is not the article\'s text, and is left out.',
            'Legea-cadru nr. 153/2017: the form of 24.05.2020 prints new ministry names in arts. 3, 16, 17, 23, 28 '
            'and 33 with no note naming an act; those changes are left uncredited (the publisher\'s).',
        ],
        'repeal_acts': {},
    }
    # the forms of 01.01.2025 to 07.03.2025 print the portal's quotation of art. I-IV and XV of OUG nr. 156/2024 as
    # paragraphs of art. 16 (its heading line names the gazette, so it is dropped as an editorial paragraph)
    P.EDITORIAL_LINES[SLUG] = {'art-016': (
        'Articolul I', 'Articolul II', 'Articolul III', 'Articolul IV', 'Articolul XV',
        '(1) Prin derogare de la prevederile art. 12 alin. (2) din Legea-cadru ',
        '(2) Prin derogare de la prevederile art. 13 alin. (1) din Legea-cadru ',
        '(3) Prin derogare de la prevederile art. 11 alin. (1) din Legea-cadru ',
        '(4) Ordonatorii de credite dispun măsurile necesare astfel încât cuant',
        '(1) În anul 2025, începând cu data de 1 ianuarie, cuantumul sporurilor',
        '(2) Prin derogare de la prevederile art. 18 alin. (1) din Legea-cadru ',
        '(1) Prin derogare de la prevederile art. 21 alin. (2)-(6) din Legea-ca',
        '(2) În anul 2025, munca suplimentară prestată în cadrul activităților ',
        '(3) Plata majorării prevăzute la alin. (2) se efectuează cu aprobarea ',
        '(4) Condițiile și procedurile specifice pentru stabilirea și plata maj',
        '(5) În anul 2025, pentru personalul din instituțiile și autoritățile p',
        '(1) În anul 2025, instituțiile și autoritățile publice, astfel cum sun',
        '(2) Prin excepție de la prevederile alin. (1), pentru personalul milit',
        '(3) În anul 2025, instituțiile și autoritățile publice, astfel cum sun',
        '(4) În anul 2025, serviciile publice autonome de interes național, cu ',
        '(5) Prin derogare de la prevederile art. 9 alin. (1) lit. a) pct. i) ș',
        '(6) În anul 2025, instituțiile și autoritățile publice, astfel cum sun',
        '(7) Instituțiile trimițătoare pot aproba cheltuielile reglementate la ',
        '(1) În anul 2025, personalul plătit din fonduri publice, salarizat pot',
        '(2) În anul 2025, judecătorii și procurorii care funcționează în insti',
    )}
    # dates read from the act as published (DetaliiDocumentAfis/190446: "LEGE-CADRU nr. 153 din 28 iunie 2017",
    # "București, 28 iunie 2017. Nr. 153.", MONITORUL OFICIAL nr. 492 din 28 iunie 2017)
    P.BASE_LAWS[SLUG] = {
        'label': 'Legea-cadru nr. 153/2017', 'kind': 'law',
        'title': 'Legea-cadru nr. 153 din 28 iunie 2017 privind salarizarea personalului plătit din fonduri publice, '
                 'publicată în Monitorul Oficial al României, Partea I, nr. 492 din 28 iunie 2017',
        'enacted': '2017-06-28', 'published': '2017-06-28', 'url': P.PORTAL + 'DetaliiDocument/190446',
    }
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
