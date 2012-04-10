# Anexa 1
Anexa 1
la metodologie Exemple de activități aferente procesului de evaluare 1. Prezentăm în continuare o listă exemplificativă cu activități aferente procesului de evaluare:
a) verificarea analizei de conformitate;
b) verificarea analizei caracterului unitar;
c) examinarea eficienței mecanismelor de asigurare a securității;
d) examinarea vulnerabilităților constructive;
e) examinarea ușurinței de utilizare;
f) examinarea vulnerabilităților operaționale;
g) verificarea cerințelor;
h) verificarea proiectului de arhitectură a produsului;
i) verificarea proiectului detaliat;
j) verificarea implementării mecanismelor de asigurare a securității;
k) verificarea mediului de dezvoltare;
l) verificarea documentației de operare;
m) verificarea mediului operațional;
n) realizarea de teste de penetrare;
o) întocmirea raportului de evaluare.
2. Pentru claritate, precizăm că termenul de "verificare" implică analiza elementelor de evaluare, în timp ce "examinarea" furnizează date de intrare pentru realizarea testelor de penetrare. Deși testele de penetrare sunt în mod explicit corelate cu activitățile anterioare, acestea au fost specificate ca activitate distinctă din două motive:
a) pentru a sublinia faptul că analizele anterioare trebuie consolidate și apoi trebuie concepute testele, pe baza acestor analize;
b) pentru a indica faptul că, în general, diferitele teste de penetrare sunt realizate împreună.
3. Prin activitatea de verificare a analizei de conformitate, evaluatorul verifică analiza efectuată de dezvoltatorul produsului INFOSEC. Verificarea poate pune în evidență unele vulnerabilități rezultate, din cauza faptului că anumite funcții de securitate nu asigură atingerea unuia dintre obiectivele securității, în condițiile unei amenințări identificate în ținta de securitate. 4. Activitatea de verificare a analizei caracterului unitar constă în examinarea analizei efectuate de dezvoltatorul produsului INFOSEC și stabilește dacă setul de funcții de securitate implementate, luate ca ansamblu, asigură în mod adecvat îndeplinirea obiectivelor securității. 5. Prin examinarea eficienței mecanismelor de asigurare a securității evaluatorul identifică eventualele mecanisme care nu ating eficiența minimă cerută prin ținta de securitate. 6. În procesul de examinare a vulnerabilităților rezultate din procesul de construcție a produsului INFOSEC, evaluatorul trebuie să identifice eventuale astfel de vulnerabilități ale acestuia. Erorile identificate în procesul de evaluare a corectitudinii procesului de dezvoltare a produsului reprezintă o sursă de vulnerabilități constructive. Această activitate presupune examinarea erorilor, precum și a diferitelor funcționalități introduse în fiecare etapă a dezvoltării produsului. 7. Examinarea ușurinței de utilizare presupune identificarea modurilor de operare nesigure a produsului INFOSEC. Prin urmare, această activitate este strâns legată de cerințe operaționale. 8. Activitatea de evaluare a vulnerabilităților operaționale presupune ca evaluatorul să examineze modul de operare a produsului INFOSEC, pentru a identifica eventuale vulnerabilități apărute în cursul acestui proces. 9. Vulnerabilitățile operaționale tratează aspecte la limita dintre măsurile de securitate IT și cele non-IT, cum ar fi proceduri operaționale privind securitatea fizică, modalități nonelectronice de management al cheilor, distribuția ecusoanelor de securitate etc. Măsurile de securitate non-IT trebuie să facă obiectul preocupărilor entității evaluatoare în următoarele situații:
a) apar ca parte a documentației de operare;
b) ținta de securitate este formulată pe baza unei politici de securitate a sistemului;
c) apar ca parte a documentației produsului INFOSEC.
10. În procesul de analiză a vulnerabilităților operaționale ale produsului INFOSEC, evaluatorii trebuie să analizeze dacă măsurile de securitate non-IT implementate contracarează vulnerabilitățile constructive identificate. 11. Activitatea de verificare a cerințelor presupune ca evaluatorul să determine dacă ținta de securitate definește în mod corect funcțiile care asigură implementarea securității. Ținta de securitate trebuie să identifice clar aceste funcții, nivelul de evaluare solicitat, precum și măsurile de securitate implementate și care trebuie avute în vedere în procesul de evaluare a produsului INFOSEC. 12. Prima etapă în procesul de dezvoltare a produsului, de la faza de cerințe la cea de proiect de arhitectură, prezintă o importanță deosebită, avându-se în vedere faptul că asigură corespondența dintre funcțiile abstracte și componentele logice și fizice ale produsului INFOSEC. În acest context, una dintre principalele activități din procesul de evaluare este verificarea proiectului de arhitectură, în urma căreia evaluatorul decide dacă există o separare bine definită între funcționalitățile care asigură securitatea și celelalte funcționalități ale produsului INFOSEC. În acest caz, activitatea de evaluare poate fi focalizată asupra elementelor care contribuie la asigurarea securității, iar ținta de securitate poate fi urmărită cu ușurință, pe măsură ce proiectul este analizat mai în detaliu. 13. Activitatea de verificare a proiectului detaliat presupune analiza modului în care este respectată politica privind separarea componentelor care asigură securitatea de celelalte componente, precum și verificarea faptului că toate componentele care asigură implementarea securității sunt corect implementate. 14. Verificarea implementării presupune analiza modului în care sunt implementate mecanismele de asigurare a securității, într-un mod mai detaliat decât în cursul activității de verificare a proiectului. Analiza se bazează pe concluziile activității de verificare a proiectului detaliat, după care devine posibilă testarea funcțională. 15. Prin activitatea de verificare a mediului de dezvoltare se analizează în special standardele conform cărora este dezvoltat produsul. În cursul acestei activități se analizează:
a) controlul configurației;
b) limbajele de programare și compilatoarele;
c) măsurile de securitate implementate de dezvoltator.
16. Activitatea de verificare a documentației de operare presupune verificarea faptului că produsul INFOSEC poate fi administrat și utilizat în acord cu obiectivele sale de securitate. 17. Verificarea mediului de operare presupune ca evaluatorul să analizeze dacă produsul operațional este identic cu produsul rezultat din procesul de dezvoltare și dacă acesta poate fi operat în conformitate cu obiectivele securității. 18. Testele de penetrare au rolul de a identifica eventuale vulnerabilități, care pot fi exploatate în procesul de utilizare a produsului INFOSEC. 19. Observațiile și rezultatele fiecărei activități din procesul de evaluare trebuie consemnate în RTE.
Anexa 2
la metodologie - Model - Raportul tehnic de evaluare (RTE)
Capitolul I
Introducere
Secțiunea 1
Elemente generale
1. Această secțiune conține date generale cu privire la procesul de evaluare și trebuie să prezinte cel puțin următoarele elemente:
a) denumirea, numărul de identificare și versiunea/modelul produsului INFOSEC supus evaluării;
b) date referitoare la dezvoltatorul produsului INFOSEC și, dacă este cazul, la subcontractanții care au contribuit la dezvoltarea produsului INFOSEC;
c) date cu privire la solicitantul evaluării;
d) programarea activităților aferente procesului de evaluare;
e) date cu privire la entitatea evaluatoare.
Secțiunea a 2-a
Obiective
2. Această secțiune trebuie să prezinte obiectivele RTE. 3. În principal, obiectivele sunt:
a) prezentarea elementelor necesare susținerii unei anumite concluzii cu privire la produsul INFOSEC supus evaluării;
b) susținerea procesului de reevaluare a produsului INFOSEC, în cazul în care solicitantul dorește acest lucru.
Secțiunea a 3-a
Domeniu de aplicabilitate
4. Această secțiune trebuie să sublinieze faptul că RTE se referă la întreaga activitate desfășurată în cursul procesului de evaluare. 5. În caz contrar, trebuie specificate motivele pentru care RTE nu acoperă întreaga activitate de evaluare.
Secțiunea a 4-a
Structură
6. Această secțiune trebuie să prezinte structura RTE.
Capitolul II
Sumar
7. Acest capitol furnizează date cu privire la rezultatele evaluării. 8. Totodată, acest capitol trebuie să conțină informațiile generale necesare introducerii produsului INFOSEC în Catalogul național, după certificare. 9. Prin urmare, sumarul nu trebuie să conțină informații clasificate. 10. Acest capitol trebuie să conțină:
a) date cu privire la entitatea evaluatoare;
b) nivelul de evaluare atins efectiv;
c) numărul de identificare și versiunea/modelul produsului INFOSEC;
d) sumarul principalelor concluzii ale evaluării;
e) date cu privire la solicitantul evaluării;
f) scurtă descriere a produsului INFOSEC supus evaluării;
g) scurtă descriere a caracteristicilor de securitate ale produsului INFOSEC supus evaluării.
Capitolul III
Descrierea produsului INFOSEC supus evaluării
Secțiunea 1
Funcționalitatea produsului INFOSEC
11. Această secțiune trebuie să conțină o prezentare succintă a rolului operațional al produsului INFOSEC, precum și a funcțiunilor pentru care a fost proiectat. Descrierea trebuie să conțină cel puțin următoarele elemente:
a) tipul de date care pot fi procesate utilizând produsul (nivel de clasificare etc.);
b) categoriile de utilizatori care vor utiliza produsul INFOSEC (corelat cu precizările de la punctul anterior).
Secțiunea a 2-a
Etapele procesului de dezvoltare
12. Această secțiune trebuie să prezinte etapele parcurse în realizarea produsului INFOSEC. 13. De asemenea, trebuie prezentate metodologiile, tehnicile, instrumentele și standardele relevante pentru realizarea produsului INFOSEC. 14. Totodată, această secțiune trebuie să includă descrierea elementelor necesare evaluării puse la dispoziția entității evaluatoare de către solicitant. Descrierea trebuie să includă data la care au fost puse la dispoziție aceste elemente și numărul de înregistrare cu care a fost luat în evidență fiecare element.
Secțiunea a 3-a
Arhitectura produsului INFOSEC
15. Această secțiune trebuie să conțină un sumar al proiectului general al produsului INFOSEC. Trebuie să se precizeze gradul de separare între componentele care asigură implementarea securității și celelalte componente. SECȚIUNEA va prezenta și modul de implementare și distribuția între componentele hardware, firmware și software a elementelor care asigură implementarea securității. 16. Toate numerele modelelor/versiunilor acestor componente trebuie specificate într-o anexă la RTE (anexa C).
Secțiunea a 4-a
Descrierea componentelor hardware
17. Descrierea componentelor hardware trebuie să prezinte în detaliu toate componentele relevante pentru procesul de evaluare, la nivel de arhitectură.
Secțiunea a 5-a
Descrierea componentelor firmware
18. Descrierea componentelor firmware trebuie să prezinte în detaliu toate componentele relevante pentru procesul de evaluare.
Secțiunea a 6-a
Descrierea software
19. Descrierea componentelor software trebuie să prezinte în detaliu toate componentele relevante pentru procesul de evaluare. Descrierea trebuie să furnizeze legătura dintre componentele software și cele hardware și firmware.
Capitolul IV
Caracteristici de securitate ale produsului INFOSEC
20. Trebuie subliniat că înțelegerea țintei de securitate este un element esențial pentru înțelegerea RTE. De aceea, este recomandabil ca acest capitol să includă descrierea completă a țintei de securitate. 21. Capitolul trebuie să abordeze cel puțin următoarele aspecte:
a) politica de securitate pentru produsul INFOSEC;
b) specificarea funcțiilor de implementare a securității;
c) specificarea mecanismelor de securitate;
d) precizarea nivelului minim estimat de eficiență a mecanismelor de securitate;
e) nivelul de evaluare solicitat.
Capitolul V
Evaluarea
22. Prevederile prezentului capitol detaliază activitățile efectuate în procesul de evaluare, cu specificarea tuturor problemelor identificate, atât a celor de natură tehnică, cât și a celor de natură managerială. 23. Capitolul trebuie să conțină date care să sprijine activitatea comisiei de certificare de securitate, în analiza aspectelor de natură tehnică și managerială. Totodată, datele cuprinse în acest capitol pot să contribuie și la eficientizarea activității entității evaluatoare.
Secțiunea 1
Etapele evaluării
24. Această secțiune este similară celei în care sunt prezentate etapele procesului de dezvoltare și trebuie să includă date cu privire la:
a) data la care a fost demarat procesul de evaluare;
b) data la care au fost furnizate elementele necesare evaluării, inclusiv ținta de securitate a produsului INFOSEC;
c) perioada în care au fost realizate testele de penetrare;
d) eventuale vizite efectuate la sediile dezvoltatorului sau ale utilizatorului final al produsului;
e) data la care s-au încheiat activitățile tehnice.
25. Secțiunea trebuie să precizeze toate metodele, tehnicile, instrumentele și standardele utilizate în procesul de evaluare.
Secțiunea a 2-a
Procedura de evaluare
26. Această secțiune trebuie să conțină un sumar al PAE. Sumarul trebuie să includă:
a) activitățile desfășurate de evaluator, conform PAE;
b) totalitatea activităților desfășurate în procesul de evaluare, cu evidențierea activităților care nu au fost cuprinse în PAE, dar au fost efectuate în practică; va fi precizată motivația existenței acestor discrepanțe.
Secțiunea a 3-a
Domeniul de aplicare a evaluării
27. Această secțiune trebuie să precizeze componentele care au făcut obiectul evaluării, precum și ipotezele făcute cu privire la componentele care nu au fost examinate.
Secțiunea a 4-a
Constrângeri și ipoteze
28. Această secțiune trebuie să precizeze eventualele constrângeri asupra procesului de evaluare și ipotezele făcute în cursul acestui proces.
Capitolul VI
Sumarul rezultatelor evaluării
29. Prevederile prezentului capitol trebuie să prezinte sumarul rezultatelor evaluării, pentru toate activitățile efectuate în cursul procesului. 30. Se recomandă structurarea pe secțiuni care să corespundă fiecăreia dintre activitățile desfășurate. 31. Fiecare secțiune trebuie să fie corelată cu setul de activități desfășurate. 32. Prezentăm în continuare, cu titlu de exemplu, o listă de aspecte care fac obiectul acestui capitol:
a) Eficiența constructivă
- Aspect 1 - Conformitatea funcționalității - Aspect 2 - Interrelaționarea funcționalităților - Aspect 3 - Eficiența mecanismelor - Aspect 4 - Evaluarea vulnerabilităților constructive
b) Eficiența operațională
- Aspect 1 - Flexibilitatea în utilizare - Aspect 2 - Evaluarea vulnerabilităților operaționale
c) Realizarea produsului - Procesul de dezvoltare
- Etapa 1 - Cerințe - Etapa 2 - Proiectul arhitecturii - Etapa 3 - Proiectul detaliat - Etapa 4 - Implementarea
d) Realizarea produsului - Mediul de dezvoltare
- Aspect 1 - Controlul configurației - Aspect 2 - Limbaje de programare și compilatoare - Aspect 3 - Măsurile de securitate implementate de către dezvoltator
e) Operare - Documentația de operare
- Aspect 1 - Documentația de utilizare - Aspect 2 - Documentația de administrare
f) Operare - Mediul operațional
- Aspect 1 - Livrarea și configurarea produsului - Aspect 2 - Punerea în funcțiune și operarea
Secțiunea 1
Teste de penetrare
33. Rezultatele testelor de penetrare au fost analizate separat deoarece testele de penetrare sunt de cele mai multe ori realizate ca parte a unei anumite activități. 34. Prezenta secțiune trebuie să prezinte toate opțiunile de configurare folosite în timpul testelor de penetrare.
Secțiunea a 2-a
Vulnerabilități exploatabile identificate
35. Prezenta secțiune trebuie să descrie vulnerabilitățile ce pot fi exploatate, care au fost identificate în timpul evaluării, precizând:
a) funcția de implementare a securității la care a fost identificată vulnerabilitatea;
b) descrierea vulnerabilității;
c) acțiunile întreprinse de evaluator în momentul identificării vulnerabilității;
d) activitatea în cursul căreia a fost identificată vulnerabilitatea;
e) persoana care a identificat vulnerabilitatea (dezvoltatorul sau evaluatorul);
f) data la care a fost identificată vulnerabilitatea;
g) dacă vulnerabilitatea a fost remediată (se menționează data) sau nu;
h) sursa generatoare a vulnerabilității (dacă este posibil).
Secțiunea a 3-a
Observații legate de vulnerabilități ce nu pot fi exploatate
36. Prezenta secțiune trebuie să descrie vulnerabilitățile ce nu pot fi exploatate și au fost identificate în cadrul evaluării (subliniindu-le pe cele rămase în produsul operațional).
Secțiunea a 4-a
Erori identificate
37. Prezenta secțiune trebuie să precizeze impactul pe care îl pot avea erorile identificate în cadrul procesului de evaluare.
Capitolul VII
Ghid pentru reevaluare și analiză a impactului
Prezentul capitol este opțional. Poate fi omis dacă solicitantul evaluării a declarat că nu necesită informații privind o reevaluare sau analiză a impactului. 38. Dacă va fi inclus, acest capitol trebuie să precizeze:
a) includerea fiecărei componente a produsului INFOSEC în una dintre următoarele categorii: componente care asigură implementarea securității, componente relevante pentru securitate sau componente care nu sunt relevante pentru securitate;
b) identificarea instrumentelor de dezvoltare care sunt relevante pentru securitate;
c) modalitatea în care constrângerile sau ipotezele făcute în procesul de evaluare pot avea impact în cazul reevaluării sau refolosirii produsului INFOSEC;
d) orice concluzii privind tehnici de evaluare sau instrumente care pot fi utile în cazul unei reevaluări;
e) detalii de arhivare necesare reînceperii evaluării;
f) pregătire specifică necesară reevaluatorilor pentru demararea unui proces de reevaluare.
Capitolul VIII
Concluzii și recomandări
39. Prezentul capitol trebuie să prezinte concluziile și recomandările evaluării. Concluzia principală va preciza dacă produsul INFOSEC îndeplinește obiectivul de securitate stabilit și dacă are vulnerabilități ce pot fi exploatate. 40. Trebuie să se specifice faptul că recomandările se referă la componentele produsului care au făcut obiectul evaluării și că pot exista și alți factori de care evaluatorii nu sunt conștienți, iar acești factori pot influența procesul de certificare a produsului INFOSEC. 41. Recomandările pot include sugestii către alte entități, precum solicitantul evaluării sau dezvoltatorul produsului INFOSEC, pentru a fi înaintate comisiei despre certificare de securitate. 42. Trebuie să se specifice faptul că rezultatele evaluării sunt valabile numai pentru o anumită versiune a produsului INFOSEC, configurată într-un anumit mod, iar comisia de certificare de securitate trebuie informată despre orice schimbări aduse produsului INFOSEC.
Capitolul IX
Anexele RTE
Anexa A - Lista elementelor necesare evaluării 43. Această anexă trebuie să identifice, cu numerele versiunii și datele la care au fost recepționate, toate elementele necesare evaluării sau se face o referire la lista elementelor. Anexa B - Lista de acronime/Glosar de termeni 44. Această anexă trebuie să explice toate acronimele și abrevierile folosite în RTE. De asemenea, trebuie să definească termenii specifici utilizați. Anexa C - Configurația evaluată 45. Configurațiile produsului INFOSEC examinate în cadrul evaluării (în special configurații folosite la testele de penetrare, verificare a fiabilității) trebuie identificate clar. 46. Trebuie precizate orice presupuneri făcute sau configurații care nu au fost luate în considerare. Descrierea componentelor hardware 47. Descrierea componentelor hardware trebuie să furnizeze informații despre configurație, privind toate componentele la nivel arhitectural ce sunt relevante pentru evaluare și, în consecință, pentru implementarea securității. Descrierea componentelor firmware 48. Descrierea componentelor firmware trebuie să furnizeze informații despre configurație, despre toate componentele care sunt relevante pentru procesul de evaluare și, în consecință, pentru implementarea securității. Descrierea componentelor software 49. Descrierea componentelor software trebuie să furnizeze informații despre configurație privind părți ale aplicațiilor software utilizate de produsul INFOSEC care sunt relevante pentru procesul de evaluare și, în consecință, pentru implementarea securității. Anexa D - Rapoartele activităților de evaluare 50. Această anexă nu este necesară dacă toate rapoartele de activitate sunt incluse în cap. VI al RTE. 51. Dacă este inclusă, această anexă trebuie să cuprindă înregistrări ale tuturor activităților de evaluare (incluzând rezultatele testelor efectuate, tehnici și instrumente utilizate). Anexa E - Probleme identificate 52. Această anexă trebuie să cuprindă rapoarte cu privire la toate problemele identificate în cursul procesului de evaluare. 53. Rapoartele pot fi emise și înainte de finalizarea evaluării și trebuie să conțină cel puțin următoarele elemente:
a) numărul și versiunea produsului INFOSEC supus evaluării;
b) activitatea în cursul căreia a fost identificată problema;
c) descrierea problemei identificate.
Anexa 3
la metodologie Elemente ale raportului de certificare Un raport de certificare trebuie să includă cel puțin următoarele elemente:
a) Introducere:
- date generale cu privire la produsul INFOSEC supus evaluării.
b) Rezumat:
- detalii cu privire la entitatea de evaluare; - identificarea completă a produsului INFOSEC supus evaluării, inclusiv a codului de identificare, versiunii etc.; - sumarul concluziilor formulate de evaluator; - date privind dezvoltatorul și, dacă este cazul, a subcontractanților acestuia care au contribuit la dezvoltarea produsului INFOSEC; - date privind solicitantul certificării; - nivelul de evaluare atins efectiv.
c) Prezentarea produsului INFOSEC:
- descrierea produsului INFOSEC, în configurația supusă evaluării; - descrierea hardware; - descrierea firmware; - descrierea software; - descrierea documentației produsului INFOSEC.
d) Evaluarea:
- descrierea sumară a țintei de securitate, care să cuprindă și descrierea caracteristicilor de securitate ale produsului INFOSEC; - elemente de identificare ale RTE; - sumarul principalelor concluzii formulate de entitatea de evaluare.
e) Certificarea:
- propuneri referitoare la luarea unei decizii cu privire la certificarea produsului INFOSEC; - specificarea eventualelor restricții care trebuie avute în vedere în procesul de utilizare a produsului INFOSEC (de exemplu: limitarea nivelului de clasificare a informațiilor, utilizare în medii operaționale specifice etc.).
Anexa 4
la metodologie Bibliografie 1. Standardele naționale de protecție a informațiilor clasificate în România, aprobate prin Hotărârea Guvernului nr. 585/2002 , publicată în Monitorul Oficial al României, Partea I, nr. 485 din 5 iulie 2002, cu modificările și completările ulterioare. 2. Normele privind protecția informațiilor clasificate ale Organizației Tratatului Atlanticului de Nord în România, aprobate prin Hotărârea Guvernului nr. 353/2002 , publicată în Monitorul Oficial al României, Partea I, nr. 315 din 13 mai 2002, cu modificările ulterioare. 3. Metodologia de acreditare a entităților pentru evaluarea produselor de securitate IT și a sistemelor informatice și de comunicații - INFOSEC 12, aprobată prin ordin al directorului general al Oficiului Registrului Național al Informațiilor Secrete de Stat. 4. North Atlantic Council, Guidelines for the security evaluation and certification of communication and information systems (CIS) - AC/35-D/1019-REV1, 2008. 5. Procedure CER/P/01.1 - Certification of the security provided by IT products and systems, February 9, 2004 - Secretariat General de la Defense Naționale, France. 6. Common Methodology for the Information Technology Security Evaluation v. 3.1, rev. 3 2009. 7. SP-001 Certification and Evaluation Scheme - Scheme overview, Swedish Certification Body for IT Security, November 2011. 8. Common Criteria Evaluation and Validation Scheme For Information Technology Security, Guidance to Validators of IT Security Evaluations, Version 2.0, September 2008, Național Institute for Standards and Technologies, U.S. __________
