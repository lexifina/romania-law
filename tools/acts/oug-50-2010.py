"""OUG nr. 50/2010 (consumer credit agreements) (Lexifina, 2026-11-02).

Act page 119472 is also its base text (DetaliiDocumentAfis/119472); 8 consolidated forms (02.01.2011 .. 17.03.2024), all held from Common
Crawl (forms.d/oug-50-2010.json)."""

SLUG = 'oug-50-2010'
TITLE = ('Ordonanța de urgență a Guvernului nr. 50/2010 privind contractele de credit pentru consumatori')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-oug-50-2010', 'short': 'OUG nr. 50/2010', 'pad': 3, 'cc_forms': True, 'trailing_notes': True, 'sign_tail': True,
        # art. 92 amends Legea nr. 190/1999 and quotes the articles it rewrites (S_ART inside S_ART)
        'quoted_articles': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/119472',
        'in_force': '2010-06-21', 'first_law': SLUG,
        'base_note': 'The emergency ordinance as published in Monitorul Oficial nr. 389 of 11 June 2010, in force within 10 days of publication (its art. 94): 21 June 2010.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'OUG nr. 50/2010: the first version is the emergency ordinance as published in Monitorul Oficial nr. 389 of 11 June 2010 '
            '(DetaliiDocumentAfis/119472), dated 21 June 2010: in force within 10 days of publication (its art. 94). The portal\'s consolidated forms start on 2 January 2011, so '
            'the changes made before that day arrive together with that form.',
            'OUG nr. 50/2010: the portal prints repeal and change notes just after the article they concern; they are read as '
            'that article\'s notes. The signature block printed after the last article is not part of the article.',
            'OUG nr. 50/2010: art. 92 amends Legea nr. 190/1999 and quotes the articles it rewrites; the quoted articles '
            'are read as part of art. 92. The portal prints some of those quotations differently from one form to the '
            'next (with or without quotation marks, "Articolul 8" repeated as a heading), and the text of arts. 41, '
            '49, 53, 66, 70, 92, 95^1 and 96 differs between forms in typing corrections, a dropped transposition '
            'footnote (art. 96) and joined words ("art. 7pct. 5"): no note names a law for them, so they are committed '
            'as the publisher\'s. Its annexes (Anexele nr. 1-3, the information forms) are not articles and are not read.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/119472)
        'label': 'OUG nr. 50/2010', 'kind': 'decree',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 389 din 11 iunie 2010',
        'enacted': '2010-06-09', 'published': '2010-06-11', 'url': P.PORTAL + 'DetaliiDocumentAfis/119472',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
