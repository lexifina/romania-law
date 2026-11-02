"""Legea nr. 237/2015 privind autorizarea și supravegherea activității de asigurare și reasigurare (Lexifina,
2026-11-02).

Act page 172402, also its base text (DetaliiDocumentAfis/172402); no republication; 11 consolidated forms 19.09.2016 ..
19.12.2025 (forms.d/legea-237-2015.json, listed from DetaliiDocumentAfis/305297). Parsed as the Phase 6 acts.
"""
SLUG = 'legea-237-2015'
TITLE = 'Legea nr. 237/2015 privind autorizarea și supravegherea activității de asigurare și reasigurare'


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-237-2015', 'short': 'Legea nr. 237/2015', 'pad': 3, 'cc_forms': True,
        # art. 180 amends Legea nr. 32/2000 and quotes the articles it rewrites (S_ART inside S_ART)
        'quoted_articles': True, 'root_word': 'act page',
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/172402',
        'in_force': '2016-01-01', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 800 of 28 October 2015, in force on 1 January 2016 '
                     '(its art. 182); art. 166 alin. (1)-(3) took effect 3 days after publication.',
        'form_note': {}, 'republished': {},
        # the form of 19.01.2024 prints art. 110^1, inserted by Legea nr. 17/2024 art. I pct. 16, which its own note
        # in that form puts in force on 15.02.2024 (art. V alin. (1) of that law); the form of 15.02.2024 prints it
        # with its note
        'early_text': {'269869': {'absent': ('art-110-1',), 'placeholder': ()}},
        'decisions': [
            'Legea nr. 237/2015: the first version is the law as published in Monitorul Oficial nr. 800 of 28 October '
            '2015 (DetaliiDocumentAfis/172402), dated 1 January 2016, when it takes effect (its art. 182). Art. 166 '
            'alin. (1)-(3) took effect 3 days after publication (31 October 2015); it is shown from 1 January 2016 '
            'with the rest of the law. Its annexes are not articles and are not read.',
            'Legea nr. 237/2015: the law as published prints its EU-transposition note ("*", "Prezenta lege transpune: '
            '1. ... 3. ...") as the last lines of art. 182; it is not an article\'s text and is left out, as in the '
            'portal\'s forms.',
            'Legea nr. 237/2015: art. 180 quotes the articles of Legea nr. 32/2000 it rewrites; the quoted articles are '
            'kept as art. 180\'s text.',
            'Legea nr. 237/2015: the portal\'s form of 19 January 2024 (269869) prints art. 110^1, inserted by Legea '
            'nr. 17/2024 art. I pct. 16, as an article, though its own note in that form says the insertion applies '
            'from 15 February 2024 (art. V alin. (1) of that law). Under the rule for text printed before its law, '
            'art. 110^1 is left out of that form; it arrives with the form of 15 February 2024, credited to Legea nr. '
            '17/2024 by that form\'s note.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/172402, Common Crawl 20251111162613)
        'label': 'Legea nr. 237/2015', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 800 din 28 octombrie 2015',
        'enacted': '2015-10-19', 'published': '2015-10-28', 'url': P.PORTAL + 'DetaliiDocumentAfis/172402',
    }
    # the law's EU-transposition note, printed by the text as published as the last lines of art. 182
    P.EDITORIAL_LINES[SLUG] = {'art-182': (
        '*', 'Prezenta lege transpune:', '1. dispozițiile Directivei 2009/138/CE',
        '2. dispozițiile art. 4 din Directiva 2011/89/UE', '3. Dispozițiile art. 2 din Directiva 2014/51/UE')}
    # parsed as the Phase 6 acts (repeal rule, sources and decisions)
    P.PHASE11 = P.PHASE11 + (SLUG,)
    P.PHASE6 = P.PHASE6 + (SLUG,)
    P.PHASE2 = P.PHASE2 + (SLUG,)
