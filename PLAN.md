# The plan: every source a Romanian lawyer or citizen needs

This is the plan for this repository, part by part, with what is published so far. It is regenerated with each documentation commit, so the gap can be followed over time.

**80.4%** of the plan is published, weighted by how binding each source is and how often it is used. **82.6%** counting sources already collected but not yet published. 1.1% of the weight is in parts that need the publisher's permission first. Updated 2026-11-07 09:43 UTC.

| Part | Will be in | Weight | Progress | How | Status |
| --- | --- | ---: | --- | --- | --- |
| **Primary legislation** | | | | | |
| Constitution and codes | constitutie/1991/; the codes in lege/ and oug/ (Codul civil is lege/2009/287/) | 11.4% | 19 of 20 acts · 95.0% | built by hand with every version, checked against the text as published | collecting |
| Laws, OUG, OG and HG (consolidated) | lege/, oug/, og/, hg/ | 24.6% | 57,437 of 55,923 acts · 99.0% | automatic: the official text as published plus every consolidated form | collecting |
| Amended, not consolidated | lege/, oug/, og/, hg/ with status "amended, not consolidated" | in the laws bin | 13,607 of 8,321 acts · 100.0% | the official text as published, labelled, with the amending acts named | done |
| Third-party-only acts | lege/, oug/, og/, hg/ once found in the official service | 1.9% | 3,822 of 5,166 acts · 74.0% | searched for one by one in the official service; only its text is used | collecting |
| **Case law** | | | | | |
| CCR decisions | jurisprudenta/ccr/ | 9.5% | 26,774 of 25,199 decisions; 603 of 1,035 rulings handled (103 applied; 500 noted) · 91.7% | official texts as published; unconstitutionality rulings dated on the articles they suspend | collecting |
| ICCJ RIL and HP | jurisprudenta/iccj/ | 4.7% | 2,219 of 2,119 decisions · 100.0% | official texts as published, linked to the articles they interpret | done |
| ICCJ other judgments (links) | data/iccj-links.csv | 0.9% | target unknown | links and metadata only | no publication channel found yet |
| Lower courts (MO decisions, ROLII archive; annulments) | instante/<court>/; data/court-annulments.csv | 1.4% | 530 of 26,000,000 judgments; 89 of 229 annulments · 13.0% | texts where no private person is named, else metadata and a link; annulments noted on the acts | collecting |
| ECHR judgments against Romania | jurisprudenta/cedo/ | 1.4% | 1,652 of 1,942 judgments · 85.1% | Romanian translations published in the Monitorul Oficial; HUDOC links for the rest | collecting |
| CJEU references | jurisprudenta/cjue/ | 0.5% | 568 of 574 cases · 99.0% | the operative part and metadata of each decision concerning Romania; full texts linked | collecting |
| CNSC and other bodies | cnsc/decizie/ (links for the rest) | 0.6% | 2,717 of 32,482 decisions · 4.2% | decisions as issued and as reasoned, identifiers removed; other bodies as metadata where they name private persons | collecting |
| **Secondary legislation** | | | | | |
| Ministerial and authority orders | ordin/<issuer>/ | 10.4% | 39,160 of 62,513 orders · 75.6% | official texts as published, with the documents that amend them | planned |
| Norms and regulations (BNR, ASF, ANRE, ANCOM and others) | norme/<issuer>/ | 11.2% | 22,958 of 38,987 acts · 64.4% | official texts as published | collecting |
| Standards (ASRO) | none: standard numbers cited only | – | out of scope | standard numbers cited only (the texts are copyright) | not planned: Copyright held by ASRO |
| **Local acts** | | | | | |
| Local acts: Bucharest (CGMB) | local/bucuresti/cgmb/ | 1.1% | 12,536 of 12,536 records · index pages 1,224/1,224 · listed 12,236/12,536 · texts 1 · 100.0% | the council's own register of decisions (PDF and text) | done |
| Local acts: Bucharest sectors 1-6 | local/bucuresti/sector-1/ ... sector-6/ | 0.6% | 6 of 6 sectors · 100.0% | each council's Monitorul Oficial Local | done |
| Local acts: county councils (41) | local/judet/<county>/ | 0.9% | 35 of 41 councils · 85.4% | each council's Monitorul Oficial Local | collecting |
| Local acts: municipalities and towns | local/<county>/<municipality or town>/ | 0.7% | 184 of 320 councils · 57.5% | each council's Monitorul Oficial Local | collecting |
| Local acts: communes | local/<county>/<commune>/ | 0.3% | 926 of 2,861 councils · 32.4% | each council's Monitorul Oficial Local | collecting |
| Local acts: other local authorities (prefects' orders) | local/prefect/<county>/ | 0.2% | 0 of 42 prefects · 0.0% | each prefecture, where it publishes | no publication channel found yet |
| Local taxes per locality | data/local-taxes.csv | 0.6% | 64 of 3,181 localities · 2.0% | each council's yearly decision on local taxes, indexed by locality and year | collecting |
| **Oversight and elections** | | | | | |
| Electoral rulings (BEC, AEP) | decizie-bec/, hotarare-aep/, norma-aep/ | 0.4% | 720 of 720 decisions · 100.0% | official texts; decisions about individual persons as metadata only | done |
| Court of Accounts | curtea-de-conturi/ | 0.3% | target unknown | official texts as published | collecting |
| Ombudsman (Avocatul Poporului) | avocatul-poporului/ | 0.2% | 1,776 of 1,807 documents · 98.3% | the Ombudsman's own publications | collecting |
| **EU and international** | | | | | |
| Treaties | tratat/ (texts), linked from the ratifying acts | 2.0% | 2,594 of 2,648 treaty texts; 3,649 of 3,500 acts · 84.7% | official texts, linked from the ratifying acts | planned |
| EU transposition links | data/eu-transposition.csv | 2.8% | 6,938 of 5,834 notification records · 100.0% | EU notification records and the transposition clauses in the acts | done |
| EU law in Romanian | ue/<kind>/<year>/<number>/ | 0.5% | 16,409 of 16,415 EU acts · 100.0% | the Romanian Official Journal text of each regulation and directive in force | done |
| **Parliament and President** | | | | | |
| Presidential decrees | promulgation data on each law; normative decrees in decret/ | 0.3% | 9,090 of 9,678 decrees · 93.9% | promulgation data on each law; normative decrees as acts | collecting |
| Parliament decisions | hotarare-parlament/ | 0.4% | 5,633 of 7,050 decisions · 79.9% | official texts as published | planned |
| **Legislative history and publications** | | | | | |
| Legislative history (amendment links, bills, Council opinions) | data/act-links-<year>.csv, data/bills-<year>.csv | 5.4% | 58,168 of 322,751 acts; 10,032 of 10,124 laws (+2 more) · 41.1% | the Chamber of Deputies' act sheets and bill files | collecting |
| Draft acts in public consultation | proiect/<initiator>/<year>/ | 0.9% | target unknown | official drafts and explanatory notes as published, each stage appended | collecting |
| Monitorul Oficial parts | MO reference in each version; data/mo-links.csv | 1.2% | 322,751 of 322,751 acts · 38.5% | the Monitorul Oficial reference of every version | planned |
| Collective labour agreements (MO Part V) | cct/ | 0.3% | 0 of 57 agreements · 0.0% | official texts as published | planned |
| **Historical law** | | | | | |
| Historical law | cod/ (old codes), decret-lege/, pre-1990 lege/ and decret/ | 2.4% | 9 of 10 codes and statutes; 111 of 200 decree-laws (+1 more) · 67.3% | built by hand from the official texts | collecting |
| **Out of scope** | | | | | |
| Doctrine, forms, arbitral awards | none | – | out of scope | not planned (not law, or not public) | not planned: Copyrighted per publisher |

Progress counts what is on `main`; targets are the official counts where they exist (the portal's own listing, the courts' totals), otherwise the best public estimate. Folders not on `main` yet will appear as the parts are published.
