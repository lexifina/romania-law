"""Legea nr. 72/2013 (late payment of sums of money) (Lexifina, 2026-11-02).

Act page 146555 is also its base text (DetaliiDocumentAfis/146555); 2 consolidated forms (18.12.2015, 01.02.2016), all held from Common
Crawl (forms.d/legea-72-2013.json)."""

SLUG = 'legea-72-2013'
TITLE = ('Legea nr. 72/2013 privind măsurile pentru combaterea întârzierii în executarea obligațiilor de plată a unor sume de bani rezultând din contracte încheiate între profesioniști și între aceștia și autorități contractante')


def register(P):
    P.ACTS[SLUG] = {
        **P.P6, 'part': '9z-legea-72-2013', 'short': 'Legea nr. 72/2013', 'pad': 3, 'cc_forms': True, 'trailing_notes': True, 'sign_tail': True,
        'title': TITLE,
        'url': P.PORTAL + 'DetaliiDocument/146555',
        'in_force': '2013-04-05', 'first_law': SLUG,
        'base_note': 'The law as published in Monitorul Oficial nr. 182 of 2 April 2013; it sets no day of its own, so in force 3 days after publication (Constituția art. 78): 5 April 2013.',
        'form_note': {}, 'republished': {},
        'decisions': [
            'Legea nr. 72/2013: the first version is the law as published in Monitorul Oficial nr. 182 of 2 April 2013 '
            '(DetaliiDocumentAfis/146555), dated 5 April 2013: it sets no in-force day of its own, so 3 days after publication (Constituția art. 78). The portal's consolidated forms start on 18 December 2015, so '
            'the changes made before that day arrive together with that form.',
            'Legea nr. 72/2013: the portal prints repeal and change notes just after the article they concern; they are read as '
            'that article's notes. The signature block printed after the last article is not part of the article.',
        ],
        'repeal_acts': {},
    }
    P.BASE_LAWS[SLUG] = {  # read from the act as published (DetaliiDocumentAfis/146555)
        'label': 'Legea nr. 72/2013', 'kind': 'law',
        'title': TITLE + ', publicată în Monitorul Oficial al României, Partea I, nr. 182 din 2 aprilie 2013',
        'enacted': '2013-03-28', 'published': '2013-04-02', 'url': P.PORTAL + 'DetaliiDocumentAfis/146555',
    }
    P.PHASE11 += (SLUG,)
    P.PHASE6 += (SLUG,)
    P.PHASE2 += (SLUG,)
