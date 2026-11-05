# The plan: every source a Romanian lawyer or citizen needs

This is the plan for this repository, part by part, with what is published so far. It is regenerated with each documentation commit, so the gap can be followed over time.

**55.3%** of the plan is published, weighted by how binding each source is and how often it is used. **71.4%** counting sources already collected but not yet published. 1.1% of the weight is in parts that need the publisher's permission first. Updated 2026-11-05 04:40 UTC.

| Part | Will be in | Weight | Progress | How | Status |
| --- | --- | ---: | --- | --- | --- |
| **Primary legislation** | | | | | |
| Constitution and codes | constitutie/1991/; the codes in lege/ and oug/ (Codul civil is lege/2009/287/) | 11.4% | 19 of 20 acts · 95.0% | built by hand with every version, checked against the text as published | collecting |
| Laws, OUG, OG and HG (consolidated) | lege/, oug/, og/, hg/ | 24.6% | 40,016 of 55,923 acts · 74.2% | automatic: the official text as published plus every consolidated form | collecting |
| Amended, not consolidated | lege/, oug/, og/, hg/ with status "amended, not consolidated" | in the laws bin | 7,252 of 8,321 acts · 87.2% | the official text as published, labelled, with the amending acts named | collecting |
| Third-party-only acts | lege/, oug/, og/, hg/ once found in the official service | 1.9% | 450 of 5,166 acts · 8.7% | searched for one by one in the official service; only its text is used | collecting |
| **Case law** | | | | | |
| CCR decisions | jurisprudenta/ccr/ | 9.5% | 22,178 of 25,303 decisions; 0 of 937 rulings applied · 70.1% | official texts as published; unconstitutionality rulings dated on the articles they suspend | collecting |
| ICCJ RIL and HP | jurisprudenta/iccj/ | 4.7% | 1,867 of 2,113 decisions · 88.4% | official texts as published, linked to the articles they interpret | collecting |
| ICCJ other judgments (links) | data/iccj-links.csv | 0.9% | target unknown | links and metadata only | no publication channel found yet |
| Lower courts (ReJust links; MO annulments) | data/rejust-links.csv; annulments as effects on acts | 1.4% | 0 of 26,000,000 judgments; 0 of 229 annulments · 0.0% | links and metadata only; annulments of acts as dated effects | planned |
| ECHR judgments against Romania | jurisprudenta/cedo/ | 1.4% | 320 of 1,942 judgments · 16.5% | Romanian translations published in the Monitorul Oficial; HUDOC links for the rest | collecting |
| CJEU references | data/cjeu-links.csv | 0.5% | 0 of 397 cases · 0.0% | links by ECLI and CELEX to the EU publications | planned |
| CNSC and other bodies | jurisprudenta/cnsc/ (links for the rest) | 0.6% | target unknown | official texts where public; decisions naming private persons as metadata only | collecting |
| **Secondary legislation** | | | | | |
| Ministerial and authority orders | ordin/<issuer>/ | 10.4% | 26,153 of 62,513 orders · 50.3% | official texts as published, with the documents that amend them | planned |
| Norms and regulations (BNR, ASF, ANRE, ANCOM and others) | norme/<issuer>/ | 11.2% | 5,742 of 38,892 acts · 18.8% | official texts as published | collecting |
| Standards (ASRO) | none: standard numbers cited only | – | out of scope | standard numbers cited only (the texts are copyright) | not planned: Copyright held by ASRO |
| **Local acts** | | | | | |
| Local acts: Bucharest (CGMB) | local/bucuresti/cgmb/ | 1.1% | 0 of 12,236 records · index pages 1,224/1,224 · listed 12,236/12,236 · texts 1 · 0.0% | the council's own register of decisions (PDF and text) | planned |
| Local acts: Bucharest sectors 1-6 | local/bucuresti/sector-1/ ... sector-6/ | 0.6% | 0 of 6 sectors · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: county councils (41) | local/judet/<county>/ | 0.9% | 0 of 41 councils · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: municipalities and towns | local/<county>/<municipality or town>/ | 0.7% | 0 of 320 councils · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: communes | local/<county>/<commune>/ | 0.3% | 0 of 2,861 councils · 0.0% | each council's Monitorul Oficial Local | planned |
| Local acts: other local authorities (prefects' orders) | local/prefect/<county>/ | 0.2% | 0 of 42 prefects · 0.0% | each prefecture, where it publishes | no publication channel found yet |
| Local taxes per locality | data/local-taxes.csv | 0.6% | 0 of 3,181 localities · 0.0% | each council's yearly decision on local taxes, indexed by locality and year | collecting |
| **Oversight and elections** | | | | | |
| Electoral rulings (BEC, AEP) | decizie-bec/, hotarare-aep/, norma-aep/ | 0.4% | 720 of 720 decisions · 100.0% | official texts; decisions about individual persons as metadata only | done |
| Court of Accounts | curtea-de-conturi/ | 0.3% | target unknown | official texts as published | collecting |
| Ombudsman (Avocatul Poporului) | avocatul-poporului/ | 0.2% | 2 of 1,807 documents · 0.1% | the Ombudsman's own publications | collecting |
| **EU and international** | | | | | |
| Treaties | tratat/ (texts), linked from the ratifying acts | 2.0% | 13 of 2,648 treaty texts; 2,086 of 3,500 acts · 22.9% | official texts, linked from the ratifying acts | collecting |
| EU transposition links | data/eu-transposition.csv | 2.8% | 6,938 of 5,834 notification records · 100.0% | EU notification records and the transposition clauses in the acts | done |
| EU law in Romanian (links) | data/eu-links.csv (texts, if kept, in eu/) | 0.5% | 0 of 37,112 EU acts · 0.0% | links to the Romanian text on EUR-Lex | planned |
| **Parliament and President** | | | | | |
| Presidential decrees | promulgation data on each law; normative decrees in decret/ | 0.3% | 7,490 of 9,678 decrees · 77.4% | promulgation data on each law; normative decrees as acts | collecting |
| Parliament decisions | hotarare-parlament/ | 0.4% | 368 of 7,050 decisions · 5.2% | official texts as published | planned |
| **Legislative history and publications** | | | | | |
| Legislative history (amendment links, bills, Council opinions) | data/act-links.csv, data/bills.csv | 5.4% | 53,706 of 107,448 acts; 0 of 8,056 laws (+2 more) · 41.6% | the Chamber of Deputies' act sheets and bill files | collecting |
| Draft acts in public consultation | proiect/<initiator>/<year>/ | 0.9% | target unknown | official drafts and explanatory notes as published, each stage appended | collecting |
| Monitorul Oficial parts | MO reference in each version; data/mo-links.csv | 1.2% | 107,448 of 107,448 acts · 38.5% | the Monitorul Oficial reference of every version | planned |
| Collective labour agreements (MO Part V) | cct/ | 0.3% | 0 of 57 agreements · 0.0% | official texts as published | planned |
| **Historical law** | | | | | |
| Historical law | cod/ (old codes), decret-lege/, pre-1990 lege/ and decret/ | 2.4% | 9 of 10 codes and statutes; 26 of 200 decree-laws (+1 more) · 40.3% | built by hand from the official texts | collecting |
| **Out of scope** | | | | | |
| Doctrine, forms, arbitral awards | none | – | out of scope | not planned (not law, or not public) | not planned: Copyrighted per publisher |

Progress counts what is on `main`; targets are the official counts where they exist (the portal's own listing, the courts' totals), otherwise the best public estimate. Folders not on `main` yet will appear as the parts are published.
