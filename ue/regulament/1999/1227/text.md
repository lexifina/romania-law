06/Volumul 03 | RO | Jurnalul Ofícial al Uniunii Europene | 165
31999R1227
L 154/75 | JURNALUL OFÍCIAL AL UNIUNII EUROPENE |
REGULAMENTUL (CE) NR. 1227/1999 AL COMISIEI
din 28 mai 1999
privind formatul tehnic de transmitere a statisticilor serviciilor de asigurare
(Text cu relevanță SEE)
COMISIA COMUNITĂȚILOR EUROPENE,
având în vedere Tratatul de instituire a Comunității Europene,
având în vedere Regulamentul (CE, Euratom) nr. 58/97 al Consiliului din 20 decembrie 1996 privind statistica structurală de întreprindere(1), modificat ultima dată de Regulamentul (CE, Euratom) nr. 410/98(2), în special articolul 12 punctul (viii),
(1) întrucât Regulamentul (CE, Euratom) al Consiliului nr. 58/97 a stabilit un cadru comun pentru elaborarea statisticilor comunitare privind structura, activitatea, performanța și competitivitatea sectorului de asigurări în Comunitate;
(2) întrucât este necesar să se specifice formatul tehnic pentru transmiterea statisticilor privind serviciile de asigurare;
(3) întrucât măsurile prevăzute de prezentul regulament sunt în conformitate cu avizul Comitetului pentru programul statistic,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Formatul tehnic prevăzut la articolul 9 din Regulamentul (CE, Euratom) nr. 58/97 este definit de anexa la prezent regulament.
Articolul 2
Statele membre aplică acest format pentru datele referitoare la anul de referință 1996 și anii următori.
Articolul 3
Prezentul regulament intră în vigoare în a douăzecea zi de la publicarea în Jurnalul Oficial al Comunităților Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 28 mai 1999.
Pentru Comisie
Yves-Thibault de SILGUY
Membru al Comisiei
(1) JO L 14, 17.1.1997, p. 1.
(2) JO L 52, 21.2.1998, p. 1.
ANEXĂ
FORMAT TEHNIC
1. Formatul datelor
Datele sunt transmise sub forma unui set de înregistrări, din care o mare parte descriu caracteristicile datelor (țara, anul, activitatea economică etc.). Datele în sine sunt niște numere ce pot fi asociate cu simboluri și note de subsol explicative folosite ca exemplu pentru a descrie agregate ale codului NACE. Datele confidențiale trebuie transmise cu valoarea reală înregistrată în câmpul valoric și cu un simbol care să indice natura confidențială a datelor.
Pentru a preciza natura datelor, este necesar să se facă distincție între următoarele cazuri speciale:
- date egale cu zero (cod „0”): numai valori egale cu zero;
- date confidențiale (cod „x”): indică datele pe care statele membre nu le transmit la Eurostat, deoarece acestea sunt confidențiale;
- date lipsă (cod „m”): acestea sunt date care lipsesc pentru moment, dar pe care statele membre intenționează să le furnizeze atunci când vor fi disponibile;
- date nedisponibile: acestea sunt date care nu se colectează într-un stat membru. În acest caz înregistrarea respectivă nu se transmite.
În mod prestabilit, dacă o întreagă dimensiune (o variabilă, un cod NUTS, un cod NACE etc.) nu se colectează, atunci înregistrările respective nu vor exista, cu excepția acelora care lipsesc datorită faptului că ele fac parte dintr-o regrupare a codurilor NACE. De aceea este important să se distingă clar care sunt datele care lipsesc într-adevăr atunci când se transmite o înregistrare (una per element lipsă), unde valoarea datelor este marcată cu un „m”, și datele care sunt egale cu zero când se transmit înregistrările respective, unde valoarea datelor este fixată la „0”.
2. Structura înregistrărilor
Înregistrările sunt alcătuite din câmpuri de lungimi variabile separate prin punct și virgulă (;). Pentru informare, tabelul de mai jos arată o dimensiune maximală a câmpurilor. În ordine, de la stânga la dreapta (de la 1 la 17), câmpurile sunt:
| Câmp | Tip | Lungimea maximă | Valori
1 | Serii | A | 2 | 5A, 5B, 5C etc. Codul alfanumeric al seriilor (vezi lista de mai jos)
2 | Anul | A | 4 | Anul cu patru caractere, de ex. 1996
3 | Unitatea teritorială | A | 2 | Corespunde codului de țară. NUTS 95 este noul nomenclator intrat în vigoare în iunie 1995
4 | Activitatea economică | A | 4 | Cod NACE Rev.1
5 | Măsura | A | 3 | Variabila – tipul de măsură
6 | Unitate | A | 4 | Unitate
7 | Variabila | A | 5 | Codul variabilei. Codurile definite în anexa 5 a regulamentului anchetei structurale de întreprindere au 5 cifre (vezi lista de mai jos)
8 | Tipul întreprinderii/activității de asigurare | A | 1 | Codul pentru tipul de întreprindere de asigurare sau activitate de asigurare (vezi lista de mai jos)
9 | Clasa de mărime | A | 4 | Codul clasei de mărime (vezi lista de mai jos)
Țara de reședință a întreprinderii-mamă | A | 4 | Codul țării de reședință a întreprinderii-mamă (vezi lista de mai jos)
10 | Defalcarea produselor | A | 6 | Corespunde clasificării produselor pe tipuri de activitate (vezi lista de mai jos)
11 | Forma juridică a întreprinderii | A | 4 | Codul pentru forma juridică a întreprinderii (vezi lista de mai jos)
Defalcarea geografică | A | 4 | Codul pentru defalcarea geografică a țărilor partenere (vezi lista de mai jos)
12 | Valoarea datelor | A | 12 | Valoarea numerică a datelor (valorile negative sunt precedate de semnul minus) exprimate în numere întregi, fără zecimale. Dacă datele nu se transmit la Eurostat, trebuie folosit un „x”, în cazul datelor confidențiale, și un „m”, în cazul datelor inexistente.
13 | Simbol de calitate | A | 1 | R: date revizuite M: date actualizate P: date provizorii
14 | Simbol pentru confidențialitate | A | 1 | A, B, C, D: indică faptul că datele sunt confidențiale și motivul confidențialității lor (vezi lista de mai jos). Un spațiu liber indică datele neconfidențiale.
15 | Dominantă | N | 3 | O valoare numerică mai mică sau egală cu 100. Aceasta indică procentajul dominant al uneia sau a două întreprinderi care domină datele și le determină confidențialitatea. Valoarea este rotunjită la numărul întreg cel mai apropiat: de ex. 90,3 devine 90; 94,50 devine 95. Acest câmp rămâne necompletat pentru date neconfidențiale. Acest câmp se utilizează numai când simbolurile de confidențialitate B sau C sunt folosite în câmpul precedent.
16 | Lista | A | 1 | Codul corespunzător listei de care aparține variabila – caracteristică
17 | Notă | A | 250 | Toate notele referitoare la date
NB: A = Alfanumeric; N = Numeric.
Acest format poate fi convertit într-un format fix utilizând lungimea maximă a fiecărui câmp și aliniind la dreapta conținutul fiecărui câmp precedat de spații goale.
3. Descrierea câmpurilor
3.1. Serii
Tipul seriei | Cod
Statistici anuale ale întreprinderilor | 5A
Statistici anuale ale întreprinderilor defalcate după forma juridică a întreprinderii | 5B
Statistici anuale ale întreprinderilor defalcate după țara de reședință a întreprinderii mamă | 5C
Statistici anuale ale întreprinderilor defalcate după clasa de mărime | 5D
Statistici anuale ale întreprinderilor defalcate după produse | 5E
Statistici anuale ale întreprinderilor după defalcarea geografică | 5F
3.2. Anul
3.3. Unitatea teritorială
Acest cod corespunde țărilor pentru seriile naționale
Țara | Cod
Belgia | BE
Danemarca | DK
Germania | DE
Grecia | GR
Spania | ES
Franța | FR
Irlanda | IE
Italia | IT
Luxemburg | LU
Țările de Jos | NL
Austria | AT
Portugalia | PT
Finlanda | FI
Suedia | SE
Regatul Unit | UK
Islanda | IS
Liechtenstein | LI
Norvegia | NO
Elveția | CH
3.4. Activitatea economică
Titlul activității economice – NACE Rev.1 | Cod
Asigurare de viață | 66.01
Asigurare generală | 66.03
Reasigurare | 66.04
3.5. Măsura
Măsura | Cod
Moneda națională | NC
Euro | EUR
Număr | NBR
3.6. Unitatea
Unitatea | Cod
Unități | UNIT
Mii | 1 000
Milioane | MIO
Miliarde | BIO
3.7. Variabila
Titlul variabilei | Cod
Număr de întreprinderi | 11 11 0
Număr de întreprinderi defalcat după forma juridică a întreprinderii | 11 11 1
Număr de întreprinderi defalcat după clasele de mărime ale primelor brute emise | 11 11 2
Număr de întreprinderi defalcat după clasele de mărime ale provizioanelor tehnice brute | 11 11 3
Număr de întreprinderi defalcat după țara de reședință a întreprinderii-mamă | 11 11 5
Numărul total și localizarea sucursalelor din alte țări | 11 41 0
Partea tehnică a contului de profit și pierdere
Prime brute emise | 12 11 0
Prime brute emise în asigurare directă | 12 11 1
Prime brute emise în reasigurare acceptată | 12 11 2
Prime brute emise în asigurare directă, prime individuale | 12 11 3
Prime brute emise în asigurare directă, prime din contracte de grup | 12 11 4
Prime brute emise în asigurare directă, prime periodice | 12 11 5
Prime brute emise în asigurare directă, prime unice | 12 11 6
Prime brute emise în asigurare directă, prime din contracte fără participare la profit | 12 11 7
Prime brute emise în asigurare directă, prime din contracte cu participare la profit | 12 11 8
Prime brute emise în asigurare directă, prime din contracte în care riscul investiției este suportat de persoana asigurată | 12 11 9
Venituri din investiții | 32 22 0
Profit nerealizat din investiții | 32 23 0
Variația brută a provizioanelor asigurării de viață | 32 25 0
Cheltuieli cu investițiile | 32 27 0
Pierderi nerealizate din investiții | 32 28 0
Venituri din investiții acordate, transferate în contul netehnic | 32 29 0
Variația brută a provizioanelor pentru prime neemise | 32 11 2
Prime brute emise, defalcate după forma juridică a întreprinderii | 32 11 4
Prime brute emise în asigurare directă, defalcate după țara de reședință a întreprinderii-mamă | 32 11 5
Prime brute emise în reasigurare acceptată, defalcate după țara de reședință a întreprinderii-mamă | 32 11 6
Venituri din investiții alocate, transferate din contul netehnic | 32 12 0
Sume brute plătite pentru daune | 32 13 1
Sume brute plătite pentru daune survenite în timpul exercițiului în curs | 32 13 2
Variația brută în provizioanele pentru daune datorate | 32 13 4
Cheltuieli brute de exploatare | 32 14 0
Variația provizioanelor pentru egalizare | 32 15 0
Alte posturi ale contului tehnic, sume brute | 32 16 0
Alte venituri tehnice, sume nete | 32 16 1
Modificări nete ale altor provizioane tehnice, nespecificate anterior | 32 16 2
Participații la profit și rabaturi, sume nete | 32 16 3
Alte cheltuieli tehnice, sume nete | 32 16 4
Subtotal I (Rezultatul brut al contului tehnic) | 32 17 0
Sold de reasigurare | 32 18 0
Partea reasigurătorilor în primele brute emise | 32 18 1
Partea reasigurătorilor în primele brute emise defalcate după țara de reședință a întreprinderii-mamă | 32 18 2
Partea reasigurătorilor în variația brută a provizioanelor pentru prime neachitate | 32 18 3
Partea reasigurătorilor în sumele brute plătite pentru daune | 32 18 5
Partea reasigurătorilor în variația brută a provizioanelor pentru prime neachitate | 32 18 6
Comisioane primite de reasigurători și participări la profit | 32 18 7
Partea reasigurătorilor în valoarea brută a posturilor contului tehnic nespecificate anterior | 32 18 8
Partea reasigurătorilor în variația brută a provizioanelor pentru asigurări de viață | 32 33 4
Subtotal II (rezultatul net al contului tehnic) | 32 19 0
Partea netehnică a contului de profit și pierdere
Venituri din investiții | 32 42 0
Venituri din investiții alocate, transferate din contul tehnic asigurări de viață | 32 43 0
Cheltuieli cu investițiile | 32 44 0
Venituri din investiții alocate, transferate din contul netehnic | 32 45 0
Alte venituri | 32 46 0
Alte cheltuieli, inclusiv actualizări valorice | 32 47 0
Profit sau pierderi din activități curente | 32 48 0
Profituri sau pierderi excepționale | 32 49 0
Toate impozitele (impozite pe profit sau pierderi din activități curente, impozite excepționale pe profit sau pierderi, alte impozite) | 32 50 0
Profit sau pierderi pentru anul financiar | 32 51 0
Variabile suplimentare în contul de profit și pierdere
Comisioane | 32 61 1
Comisioane aferente asigurărilor directe | 32 61 2
Cheltuieli externe pentru achiziționarea de bunuri și servicii | 32 61 4
Costuri cu personalul | 13 31 0
Cheltuieli externe și interne pentru gestionarea daunelor | 32 61 5
Cheltuieli de achiziție | 32 61 6
Cheltuieli de administrare | 32 61 7
Alte cheltuieli tehnice brute | 32 61 8
Cheltuieli de gestionare a investițiilor | 32 61 9
Venituri din interese de participare | 32 71 1
Venituri din terenuri și construcții | 32 71 3
Venituri din alte investiții | 32 71 4
Reevaluări și corecții la valoarea investițiilor | 32 71 5
Profit provenit din realizarea investițiilor | 32 71 6
Cheltuieli de gestionare a investițiilor, inclusiv cheltuieli pentru dobânzi | 32 72 1
Corecții la valoarea investițiilor | 32 72 2
Pierderi provenite din realizarea investițiilor | 32 72 3
Prime brute emise în asigurare directă, pe (sub)categorii CPA (la nivel de 5 cifre și subcategoriile 66.03.21, 66.03.22) | 33 11 1
Partea reasigurătorilor în primele brute emise în asigurare directă, pe (sub)categorii CPA (la nivel de 5 cifre și subcategoriile 66.03.21, 66.03.22) | 33 12 1
Sume brute plătite pentru daune, în asigurare directă, pe (sub)categorii CPA (la nivel de 5 cifre și subcategoriile 66.03.21, 66.03.22) | 33 13 1
Cheltuieli brute de exploatare, în asigurare directă, pe (sub)categorii CPA (la nivel de 5 cifre și subcategoriile 66.03.21, 66.03.22) | 33 14 1
Soldul de reasigurare, în asigurare directă, pe (sub)categorii CPA (la nivel de 5 cifre și subcategoriile 66.03.21, 66.03.22) | 33 15 1
Defalcarea geografică, în general, a primelor brute emise în asigurare directă | 34 11 0
Defalcarea geografică, în general, a primelor brute emise în reasigurare acceptată | 34 12 0
Defalcarea geografică, în general, a părților reasigurătorilor în primele brute emise | 34 13 0
Prime brute emise în asigurare directă pe categorii CPA (nivel de 5 cifre) și pe state membre, defalcarea geografică a operațiunilor realizate în temeiul dreptului de stabilire | 34 31 1
Prime brute emise în asigurare directă pe categorii CPA (nivel de 5 cifre) și pe state membre, defalcarea geografică a operațiunilor realizate în temeiul dreptului de prestare liberă a serviciilor | 34 32 1
Număr de persoane angajate | 16 11 0
Terenuri și construcții | 36 11 0
Terenuri și construcții utilizate de întreprinderea de asigurări pentru activități proprii | 36 11 1
Terenuri și construcții (valoare actuală) | 36 11 2
Investiții la întreprinderile din cadrul grupului și interese de participare | 36 12 0
Titluri de participare la întreprinderile din cadrul grupului și interese de participare | 36 12 1
Titluri de valoare emise de, precum și împrumuturi acordate către întreprinderile din cadrul grupului și întreprinderile cu care o întreprindere de asigurări este legată în temeiul unui interes de participare | 36 12 2
Investiții în întreprinderile din cadrul grupului și interese de participare (valoare actuală) | 36 12 3
Alte investiții financiare | 36 13 0
Acțiuni, alte titluri cu venit variabil și părți în fonduri comune de investiții | 36 13 1
Obligațiuni și alte titluri cu venit fix | 36 13 2
Participări la fonduri comune de investiții | 36 13 3
Împrumuturi ipotecare | 36 13 4
Alte împrumuturi | 36 13 5
Altele (inclusiv depozite la instituții de credit) | 36 13 6
Alte investiții financiare (valoare actuală) | 36 13 8
Depozite la întreprinderile cedente | 36 14 0
Investiții în beneficiul deținătorilor de polițe de asigurare de viață ale căror riscuri sunt suportate de ei | 36 20 0
Investiții în beneficiul deținătorilor de polițe de asigurare de viață care suportă riscul de investiție – terenuri și construcții | 36 21 0
Investiții în beneficiul deținătorilor de polițe de asigurare de viață care suportă riscul de investiție – alte investiții financiare | 36 22 0
Totalul bilanțului | 36 30 0
Capital și rezerve | 37 10 0
Capital și rezerve, defalcat după forma juridică a întreprinderii | 37 10 1
Capital subscris sau fonduri echivalente | 37 11 0
Prime de capital, rezerve de reevaluare, rezerve | 37 12 0
Pasive subordonate | 37 20 0
Total provizioane tehnice nete | 37 30 1
Provizioane brute pentru prime neachitate | 37 31 0
Provizioane brute pentru asigurările de viață | 37 32 0
Provizioane brute pentru daune | 37 33 0
Provizioane brute pentru daune, cu titlu de asigurări directe | 37 33 1
Provizioane brute pentru daune, cu titlu de asigurări directe, pe subcategorii ale CPA (la nivel de 5 cifre) și subcategoriile 66.03.21, 66.03.22 | 37 33 3
Provizioane brute pentru participarea la profit și rabaturi | 37 34 0
Provizioane pentru egalizare | 37 35 0
Alte provizioane tehnice brute | 37 36 0
Provizioane tehnice brute aferente asigurării de viață pentru care riscul investiției este suportat de persoanele asigurate | 37 37 0
Împrumuturi la termen | 37 41 0
Sume datorate instituțiilor de credit | 37 42 0
Numărul contractelor existente la sfârșitul exercițiului contabil, cu titlu de asigurări directe pentru toate contractele de asigurare de viață individuale și pentru următoarele subcategorii ale CPA: 66.01.1, 66.03.1, 66.03.4, 66.03.5 | 39 10 0
Numărul de persoane asigurate la sfârșitul exercițiului contabil, cu titlu de asigurări directe, pentru toate contractele de asigurare de viață individuale și pentru următoarea subcategorie a CPA: 66.03.1 | 39 20 0
Numărul de vehicule asigurate la sfârșitul exercițiului contabil, cu titlu de asigurări directe, pentru următoarea subcategorie a CPA: 66.03.2 | 39 30 0
Sume brute asigurate la sfârșitul exercițiului contabil, cu titlu de asigurări directe, pentru următoarele subcategorii ale CPA: 66.01.1 și 66.01.4 | 39 40 0
Numărul de daune survenite în cursul exercițiului contabil, cu titlu de asigurări directe, pentru următoarea subcategorie a CPA: 66.03.2 | 39 50 0
3.8. Tipuri de întreprinderi sau activități de asigurare
Tipuri de întreprinderi sau activități de asigurări | Cod
Întreprinderi de asigurare de viață | 1
Întreprinderi de asigurare generală | 2
Întreprinderi de asigurare mixte | 3
Întreprinderi de reasigurare specializată | 4
Activități de asigurări de viață ale întreprinderilor mixte | 5
Activități de asigurări generale ale întreprinderilor mixte (inclusiv reasigurarea acceptată) | 6
3.9. Clasele de mărime/locul de reședință a întreprinderii-mamă
Clasele de mărime după primele brute emise (milioane EUR) | Cod
< 5 | SC11
5-50 | SC12
51-250 | SC13
251-500 | SC14
501-1 000 | SC15
1 000 + | SC16
Clasele de mărime după provizioanele tehnice emise (milioane EUR) | Cod
< 50 | SC21
50-500 | SC22
501-2 500 | SC23
2 501-5 000 | SC24
5 001-10 000 | SC25
10 000 + | SC26
Țara de reședință a întreprinderii-mamă | Cod
Întreprindere-mamă situată în statul membru gazdă | RE01
Întreprindere-mamă situată în alte țări | RE02
3.10. Defalcarea produselor
Produse | Cod
Servicii de asigurare de viață nelegate de fondul de investiții | 66.01.1
Servicii de asigurare de viață legate de fondul de investiții | 66.01.2
Servicii de asigurare de tip tontină | 66.01.3
Operațiuni de capitalizare | 66.01.4
Alte servicii de asigurare de viață | 66.01.5
Servicii de pensionare colective | 66.02.1
Servicii de asigurare accidente și boală | 66.03.1
Servicii de asigurare autovehicule terestre | 66.03.2
Servicii de asigurare autovehicule terestre, răspunderea unei terțe părți | 66.03.21
Servicii de asigurare autovehicule terestre, alte clase | 66.03.22
Servicii de asigurare transport, maritim și aerian | 66.03.3
Servicii de asigurare a bunurilor împotriva incendiilor și a altor daune | 66.03.4
Servicii generale de asigurare cu răspunderea unor terțe părți | 66.03.5
Servicii de asigurare credite și asigurare garanții | 66.03.6
Servicii de asigurare asistență, de asistență juridică și alte asigurări de pierderi pecuniare diverse | 66.03.7
Alte servicii de asigurări generale | 66.03.8
3.11. Forma juridică a întreprinderii/Defalcare geografică
Forma juridică a întreprinderii | Cod
Întreprinderi pe acțiuni | LS01
Întreprinderi mutuale | LS02
Sucursale ale întreprinderilor ne-membre SEE | LS03
Altele | LS04
Țări și grupe de țări | Cod
BelgiqueBelgië | BEL
Danmark | DNK
Deutschland | DEU
Ελλάδα | GRC
España | ESP
France | FRA
Ireland | IRL
Italia | ITA
Luxembourg | LUX
Nederland | NLD
Österreich | AUT
Portugal | PRT
SuomiFinland | FIN
Sverige | SWE
United Kingdom | GBR
Island | ISL
Liechtenstein | LI
Norge | NOR
SchweizSuisseSvizzera | CHE
SUA | USA
Japonia | JPN
Statul membru al sediului social | MSHO
Alte state membre UE | OMS
Alte țări SEE | OEEA
Alte țări terțe (restul lumii) | THCO
3.12. Valoarea datelor
Datele monetare sunt exprimate în milioane în unitățile monetare naționale, cu excepția:
- Italiei: datele sunt exprimate în miliarde de unități monetare naționale
Pentru a avea o mai mare precizie în legătură cu natura datelor, este necesar să se facă o distincție în următoarele cazuri:
- date egale cu zero (cod „0”): numai valorile reale egale cu zero;
- date confidențiale (cod „x”): indică datele pe care statele membre nu le transmit la Eurostat, datorită confidențialității lor. Un simbol trebuie folosit, de asemenea, pentru a indica faptul că datele lipsesc datorită confidențialității (vezi punctul 3.14 de mai jos);
- datele lipsă (cod „m”): acestea sunt date care lipsesc pentru moment, dar pe care statele membre intenționează să le furnizeze atunci când vor fi disponibile;
- date nedisponibile: acestea sunt date care nu se colectează într-un stat membru. În acest caz, înregistrarea respectivă nu se transmite.
În lipsă, dacă o întreagă dimensiune (o variabilă, un cod NUTS, un cod NACE etc.) nu se colectează, atunci înregistrările respective nu vor exista, cu excepția acelora care lipsesc datorită faptului că fac parte dintr-o regrupare a codurilor NACE. De aceea, este important să se distingă clar care sunt datele care lipsesc într-adevăr atunci când se transmite o înregistrare (una per element lipsă) unde valoarea datelor este marcată cu un „m”.
3.13. Simbolul de calitate
Tipul datelor | Cod
Date revizuite | R
Date actualizate | M
Date provizorii | P
„Datele revizuite” se referă la datele care sunt transmise pentru a doua oară (sau mai mult) și reprezintă corecții la datele transmise anterior.
„Datele actualizate” se referă la datele care nu au fost disponibile anterior și au fost codificate ca lipsă în câmpul valoric al datelor (vezi punctul 3.12 de mai sus), dar care, de atunci, au devenit disponibile.
Simbolul care indică „datele provizorii” trebuie folosit pentru a indica faptul că este probabil ca datele care au fost transmise să fie corectate.
3.14. Confidențialitatea
Statele membre sunt invitate să indice clar datele confidențiale utilizând simbolurile din lista de mai jos.
Țările care nu pot transmite date confidențiale sunt rugate să lase valoarea la „x” (vezi punctul 3.12 de mai sus) și să indice printr-un simbol că datele lipsesc datorită confidențialității.
Motivul confidențialității | Simbol
Prea puține întreprinderi | A
Una din întreprinderi domină datele/piața | B
Două întreprinderi domină datele/piața | C
Date confidențiale din motive de confidențialitate secundară | D
3.15. Dominanța
O valoare numerică mai mică sau egală cu 100. Aceasta indică procentajul dominant al uneia sau a doua întreprinderi care domină datele și le determină confidențialitatea. Valoarea este rotunjită la numărul întreg cel mai apropiat: de ex. 90,3 devine 90; 94,50 devine 95. Acest câmp rămâne necompletat pentru date neconfidențiale. Acest câmp se utilizează numai când simbolurile de confidențialitate B sau C sunt folosite în câmpul precedent.
3.16. Lista
Variabilele – caracteristicile – sunt prezentate în Regulamentul (CE) nr. 410/98 al Consiliului în două liste diferite: A și B. Distincția se referă la primul an de referință pentru care ele sunt furnizate. Există trei variabile opționale.
Lista | Simbol
Lista A | A
Lista B | B
Opțional | O
4. Exemple de înregistrări
Exemplul 1
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Țara de reședință | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista
5A | 1996 | BE | 6 603 | NBR | UNIT | 11 110 | 2 | | | | 95 | | | | A
Belgia declară, în seria 5A (statistici anuale în întreprinderi) pentru anul de referință 1996, în NACE Rev.1, clasa 66.03: 95 de întreprinderi de asigurări generale. Datele nu sunt confidențiale și figurează în lista A.
5A;1996; BE; 6603; NBR; UNIT; 11110; 2;;;; 95;;;; A
Exemplul 2
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Țara de reședință | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista
5B | 1996 | DK | 6 601 | NBR | UNIT | 11 111 | 1 | | | LS01 | 49 | | | | A
Danemarca declară, în seria 5B (statistici anuale în întreprinderi defalcate după forma juridică a întreprinderii) pentru anul de referință 1996, în NACE Rev.1 clasa 66.01: 49 de întreprinderi de asigurări de viață care sunt întreprinderi pe acțiuni. Datele nu sunt confidențiale și figurează în lista A.
5B; 1996; DK; 6601; NBR; UNIT; 11111; 1;;; LS01; 49;;;; A
Exemplul 3
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Țara de reședință | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista
5C | 1996 | PT | 6 601 | NBR | UNIT | 11 115 | 1 | RE02 | | | 47 | | | | A
Portugalia declară, în seria 5C (statistici anuale în întreprinderi defalcate după țara de reședință a întreprinderii-mamă) pentru anul de referință 1996, în NACE Rev.1 clasa 66.01: 47 de întreprinderi de asigurări de viață ale căror întreprinderi-mamă sunt situate în alte țări. Datele nu sunt confidențiale și figurează în lista A.
5C; 1996; PT; 6601; NBR; UNIT; 11115; 1; RE02;;; 47;;;; A
Exemplul 4
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Țara de reședință | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista
5D | 1996 | FI | 6 603 | NBR | UNIT | 11 112 | 2 | SC14 | | | 7 | | | | A
Finlanda declară, în seria 5D (statistici anuale în întreprinderi defalcate după clasa de mărime) pentru anul de referință 1996, în NACE Rev.1 clasa 66.03: 7 de întreprinderi de asigurări generale a căror cifră de afaceri se află între 251 și 500 milioane EUR. Datele nu sunt confidențiale și figurează în lista A.
5D; 1996; FI; 6603; NBR; UNIT; 11112; 2; SC14;;; 7;;;; A
Exemplul 5
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Țara de reședință | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista | Notă
5E | 1996 | ES | 6 601 | NC | MIO | 33 111 | 1 | | 66 011 | | 1 410 692 | | | | A | Inclusiv activitățile de asigurări de viață în întreprinderile mixte
Spania declară, în seria 5E (statistici anuale în întreprinderi defalcate după produse) pentru anul de referință 1996, în NACE Rev.1 clasa 66.01:1 410 692 milioane pesetas spaniole prime brute emise în asigurare directă în serviciul de asigurare nelegat de întreprinderile de asigurări de viață. Datele nu sunt confidențiale și figurează în lista A.
5E; 1996; ES; 6601; NC; MIO; 33111; 1;; 66011;; 1410692;;;; A
Exemplul 6
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Rezidența | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista
5F | 1996 | CH | 6 601 | NC | MIO | 34 311 | 1 | | 66 021 | NLD | 302 | | | | A
Elveția declară, în seria 5F (defalcarea geografică a statisticilor anuale de întreprindere) pentru anul de referință 1996, în NACE Rev.1 clasa 66.01: 302 milioane de franci elvețieni de prime brute emise în asigurare directă prin sucursalele din Țările de Jos de către întreprinderile de asigurări de viață în grupa de produse servicii de pensionare colective. Datele nu sunt confidențiale și figurează în lista A.
5F; 1996; CH; 6601; NC; MIO; 34311; 1;; 66021; NLD; 302;;;; A
Exemplul 7
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16
Serii | Anul | Unitatea teritorială | Activitatea economică | Măsura | Unitatea | Variabila | Tipul întreprinderii | Clasa de mărime/Țara de reședință | Produse | Forma juridică a întreprinderii, defalcare geografică | Valoare | Calitate | Confidențialitate | Dominanța | Lista
5F | 2000 | ES | 6 604 | NC | MIO | 34 120 | 4 | | | OMS | M | | | | B
Spania declară, în seria 5F (defalcarea geografică a statisticilor anuale în întreprinderi) pentru anul de referință 2000, în NACE Rev.1 clasa 66.04: date lipsă milioane de pesetas spaniole de prime brute emise în reasigurare acceptată, emise de întreprinderi de reasigurare specializate din alte state membre. Datele nu sunt confidențiale și figurează în lista B.
5F; 2000; ES; 6604; NC; MIO; 34120; 4;;; OMS; M;;;; A
5. Tipul de suport magnetic
Pentru a facilita citirea datelor, acestea trebuie transmise pe o dischetă de 3,5.
6. Alte metode
Statele membre sunt invitate să transmită seturile de date prin Gesmes.
În urma unei cereri scrise, Eurostat poate furniza statelor membre chestionarele electronice în format Microsoft Excel. Cererea trebuie să fie făcută cu un avans considerabil față de data planificată pentru transmiterea datelor.
