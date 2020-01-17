# Anexa 1
ANEXA nr. 2 la procedură
Secțiunea 1. Documentația tehnică a MGCCC
Documentația conține:
copia ATR;
autorizația de înființare acordată de ANRE, sau după caz licența de exploatare comercială;
datele de contact ale gestionarului;
punctul de racordare;
data preconizată pentru punerea sub tensiune pentru perioada de probe;
certificatele de conformitate pentru echipamentele utilizate de MGCCC, însoțite de rezultatele testelor, în cazul în care acestea sunt invocate de OTS sau ORR, după caz, ca parte a dovezilor de conformitate. Acestea cuprind:
verificarea curbei de capabilitate P - Q;
trecerea peste defect;
funcționarea MGCCC în plaja de frecvență, la o viteză de variație a frecvenței de 2 Hz/sec pentru o fereastră de timp de 500 ms, de 1,5 Hz/s pentru o fereastră de timp de 1s și de 1,25 Hz/s pentru o fereastră de timp de 2s, reducerea de putere activă față de puterea activă maximă produsă în cazul scăderii frecvenței sub valoarea de 49,5 Hz, capabilitatea asigurării răspunsului limitat la creșterile de frecvență peste valoarea nominală de 50 Hz, capabilitatea asigurării răspunsului limitat la scăderile de frecvență sub valoarea nominală de 50 Hz, capabilitatea menținerii constante a puterii active mobilizate indiferent de variațiile de frecvență, în limita puterii oferite de către sursa primară, capabilitatea de reconectare automată a MGCCC la variațiile de tensiune de (0,85 -- 1,1) Un;
perturbațiile electrice, conform EN 50160 ediția în vigoare, comunicate de fabricant prin buletine emise de laboratoare atestate la nivel european sau măsurate, în punctul de racordare, în c.a., de un operator economic atestat de ANRE. Măsurătorile de calitate a energiei electrice se finalizează prin raport de măsurare, având anexate datele extrase din analizorul de calitate de clasă A;
modul de răspuns la variații ale consemnelor de putere activă și putere reactivă.
în ceea ce privește echipamentele utilizate pentru care nu a fost primit un certificat, trebuie furnizate informații (teste și rezultatele acestora etc.) în conformitate cu instrucțiunile date de către ORR și/sau OTS, după caz, relevante pentru cerințele tehnice aplicabile, specifice MGCCC;
datele tehnice detaliate ale MGCCC, conform Tabelului nr. 1-MGCCC, precum și proiectul tehnic din care să rezulte: lungimile și caracteristicile tehnice ale cablurilor și ale racordului la stația/celula aparținând ORR, modul de conectare al MGCCC și al instalațiilor auxiliare, precum și schema electrică monofilară.
modelele matematice utilizate în simulare sau informații echivalente, prevăzute în Norma Tehnică și solicitate de ORR și OTS, după caz, care să simuleze complet comportamentul MGCCC, în punctul de interfață HVDC, în regim staționar și dinamic, inclusiv pentru fenomene electromagnetice tranzitorii, schimbul de putere activă și reactivă în punctul de racordare, calitatea energiei electrice asigurată în punctul de racordare. Formatul și programul de calcul în care se furnizează modelele de mai sus utilizate în simulare, este specificat de ORR și OTS, după caz, de regulă Eurostag sau PSS-E. Conținutul modelelor matematice include condițiile/setările pentru regimurile permanente și dinamice, topologia rețelei și schema electrică monofilară. Modelele matematice se transmit cu cel puțin o lună înainte de data prognozată de solicitant pentru de punerea sub tensiune. Cerințele de modelare pentru studiile de sistem de regim permanent și de regim dinamic, respectiv modelele matematice ale MGCCC, se realizează după cum urmează:
pentru calculul regimului staționar și al curenților de scurtcircuit, sunt necesare:
schema electrică și a stației de racord la sistem;
lungimea tuturor LEA sau LES dintre MGCCC și stația de racordare la sistem;
parametrii electrici specifici tuturor cablurilor și liniilor: tipul (material), R+ [Q/km], R0 [Q/km], Rm0 [Q/km], X+ [Q/km], X0 [Q/km], Xm0 [Q/km], C+ [µFarad/km], C0 [µFarad/km], S [mm], Un [kV] etc.
pentru unitățile de transformare: puterea nominală a înfășurărilor, tensiunile nominale, pierderile în gol, pierderile în cupru, tensiunea de scurtcircuit, curentul de mers în gol, grupa de conexiuni, reglajul tensiunii (tipul de reglaj, domeniul de reglaj, inclusiv numărul plotului nominal, numărul maxim al ploturilor), tratarea neutrului;
date privind sistemul de compensare a puterii reactive și indicarea pe schema electrică solicitată a locului de instalare a sistemului de compensare;
date referitoare la MGCCC: puterea activă nominală, diagrama P-Q, viteza de variație a puterii active;
pentru calculul regimului dinamic sunt necesare:
schema logică de funcționare a MGCCC;
modelul matematic al modulelor MGCCC și al centralei în totalitate, inclusiv stația de conversie HVDC, precum și parametrii acestuia/acesteia;
sistemul de reglaj electric: scheme de reglaj și parametri pentru reglajul de putere activă și reglajul de putere reactivă și, după caz, al tensiunii la borne sau în punctul de racordare;
modelul matematic al sistemelor de reglaj putere activă, reactivă și tensiune, în formă de diagrame (incluzând funcțiile matematice), precum și setul de parametri corespunzător. Ca alternativă se poate specifica asimilarea cu un model generic din una din aplicațiile PSSE v32 (se vor furniza obligatoriu și fisierele tip ,,.dll&quot;) sau Eurostag v4.5 pentru care se furnizează parametrii. În cazul în care modelul include funcții suplimentare de reglaj sau caracteristici specifice, acestea se vor menționa și se vor adăuga scheme grafice;
protecțiile la variații de tensiune: ,,trecerea peste defect - tensiune scăzută&quot; (LVRT, ZVRT);
alte funcții speciale: ,,logica de putere la tensiune scăzută&quot;, participare la reglajul de frecvență etc;
echivalentul dinamic al MGCCC.
studii efectuate de către gestionarul MGCCC inclusiv simulări pe model, pentru a demonstra performanțele în regim permanent și dinamic, inclusiv utilizarea valorilor măsurate a testelor de fabrică la nivelul de detaliu solicitat de ORR și OTS, după caz.
schemele de reglare a puterii active, a puterii reactive, în detaliu, la nivelul MGCCC, în scopul evidențierii modului în care:
sunt preluate și modificate consemnele de putere activă și putere reactivă;
este preluată măsura de putere reactivă la nivel de MGCCC;
studiul de rețea pentru calculul necesarului de putere reactivă în punctul de racordare, pentru îndeplinirea cerințelor privind puterea reactivă în punctul de racordare (0,9 inductiv -- 0,9 capacitiv) pe toată plaja de putere activă, cu asigurarea schimbului de reactiv nul cu sistemul în situația în care puterea activă produsă este nulă. Se atașează diagrama P - Q a MGCCC în punctul de racordare (inclusiv contribuția tuturor modulelor și a mijloacelor auxiliare) și diagrama U-Q/Pmax;
studiul de regim dinamic al MGCCC și al zonei electrice în care se racordează și care poate fi luată în calcul pentru determinarea măsurilor de evitare a funcționării insularizate al acestuia;
datele necesare calculelor aferente reglajelor protecțiilor, care se trimit la ORR și/sau OTS, după caz, cu cel puțin o lună înainte de data la care se solicită punerea sub tensiune pentru perioada de probe: proiectul tehnic complet, protecțiile proprii pentru defecte interne și externe, reglajele și timpii de acționare, caracteristicile electrice ale MGCCC și ale transformatoarelor aferente, caracteristicile electrice, protecțiile proprii cu reglajele aferente și automatizările de conectare/deconectare ale elementelor de compensare a puterii reactive;
caracteristicile tehnice ale analizorului de calitate a energiei electrice, care se montează în punctul de racordare, în circuitul de c.a.. Analizorul trebuie să fie de clasă A, certificat PSL și să fie capabil să transmită fișiere de tip ,,SQL&quot;, ,,PQDIF&quot;, ,,.txt&quot; sau ,,.xls&quot; în structura impusă de sistemul de monitorizare a calității energiei electrice al OTS. Acesta se integrează în sistemul de monitorizare a calității energiei electrice al OTS;
documente privind caracteristicile tehnice ale căii de comunicație și a echipamentelor de integrare în DMS-SCADA și/sau EMS-SCADA, după caz, precum și contracte de realizare și mentenanță a căii de comunicație;
rezultatele testelor de verificare a funcționării căii de comunicație și a integrării noii instalații în DMS-SCADA și/sau EMS-SCADA;
studii de stabilitate statică și dinamică sau de integrare în sistem, dacă e cazul și dacă acestea nu au fost realizate la etapa de stabilire a soluției de racordare la rețeaua electrică.
Tabelul nr. 1-MGCCC: Date pentru MGCCC
Descrierea datelor
Unitatea de măsură
Categoria datelor
Punctul de racordare/delimitare, după caz
Text, schemă
S, D, R
Condițiile standard de determinate datele tehnice
mediu
pentru
care
au
fost
Text
D, R
Tensiunea nominală în punctul de racordare/delimitare, după caz
kV
S, D, R
Valoarea curentului maxim de scurtcircuit în punctul de racordare/delimitare, după caz, furnizat de MGCCC (înainte de echipamentul de electronică de putere/ după echipamentul de electronică de putere) la un defect:
- Simetric (trifazat)
kA
D, R
- Nesimetric (bifazat, bifazat cu pământul și monofazat)
kA
D, R
Valoarea curentului minim de scurtcircuit în punctul de racordare/delimitare, după caz, furnizat de MGCCC (înainte de echipamentul de electronică de putere/ după echipamentul de electronică de putere) la un defect:
- Simetric (trifazat)
kA
D, R
- Nesimetric (bifazat, bifazat cu pământul și monofazat)
kA
D, R
Puterea nominală aparentă
MVA
S, D, R
Factor de putere nominal (cos q n )
-
S, D, R
Putere netă
MW
S, D, R
Puterea activă nominală produsă la borne
MW
S, D, R
Puterea activă maximă produsă la borne
MW
S, D, R
Putere activă minimă produsă
MW
S, D, R
Tensiunea nominală
kV
S, D, R
Frecvența maximă/minimă de funcționare la parametrii nominali
Hz
S, D, R
Consumul serviciilor proprii la puterea maximă produsă la borne (după caz)
MW
S, D,R
Puterea reactivă maximă la borne
MVAr
S, D, R
Putere reactivă minimă la borne
MVAr
S, D, R
Capabilitatea de trecere peste defect LVRT
Diagramă
S, D,R
Funcțiile de protecție interne conținute
Text
D
Diagrame
Diagrama de capabilitate P-Q
Date grafice
S, D, R
Diagrama de variație a datelor tehnice în funcție de abaterile față de condițiile standard de mediu
R
Răspunsul la scăderea de frecvență
Diagramă
R
Răspunsul la creșterea de frecvență
Diagramă
R
Domeniul de setare al statismului
%
R
Valoarea statismului s 1
%
R
Banda moartă de frecvență
mHz
R
Timpul de întârziere (timpul mort t 1 )
s
R
Timpul de răspuns (t 2 )
s
R
Zona de insensibilitate
mHz
R
Capabilitatea de insularizare
Da/NU
S, D, R
Detalii asupra reglajului de viteză prezentat în schema bloc referitoare la funcțiile de transfer asociate elementelor individuale și unitățile de măsură
Schemă
R
Funcția de transfer echivalentă, eventual standardizată a reglajului de tensiune, valori și unități de măsură
Text
S
Unități de transformare:
Număr de înfășurări
Text
S, D, R
Puterea nominală pe fiecare înfășurare
MVA
S, D, R
Raportul nominal de transformare
kV/kV
S, D, R
Tensiune de scurtcircuit pe fiecare pereche de înfășurări (u 12 pentru transformator cu două înfășurări, u 12 , u 13 , u 23 pentru transformator cu trei înfășurări)
% din U nom, la S nom
S, D, R
Pierderi în gol
kW
S, D, R
Pierderi în sarcină
kW
S, D, R
Curentul de magnetizare
%
S, D, R
Grupa de conexiuni
Text
S, D, R
Domeniul de reglaj
kV-kV
S, D, R
Schema de reglaj (longitudinal sau longo-transversal)
Text, diagramă
D, R
Mărimea treptei de reglaj și numărul de prize
%
S, D, R
Reglaj sub sarcină
Da/Nu
D, R
Tratarea neutrului
Text,
S, D, R
diagramă
Curba de saturație
Diagramă
R
Date pentru module generatoare de tip eolian (după caz)
Tipul unității eoliene (cu ax orizontal/vertical)
Descriere
S, R
Diametrul rotorului
m
S, R
Înălțimea axului rotorului
m
S, R
Sistemul de comandă a palelor (pitch/stall)
Text
S, R
Sistemul de comandă a vitezei (fix/cu două viteze/variabil)
Text
S, R
Tipul de generator
Descriere
S, R
Certificate de tip, însoțite de rezultatele testelor efectuate de laboratoare recunoscute pe plan european pentru variații de frecvență, de tensiune și trecere peste defect
Certificate
D
Tipul de convertor de frecvență și parametrii nominali
kW
S,R
Viteza de variație a puterii active
MW/min
S, R
Curentul nominal
A
S, R
Tensiunea nominală
V
S, R
Viteza vântului de pornire
m/s
S, R
Viteza vântului (corespunzătoare puterii nominale
m/s
S, R
Viteza vântului de deconectare
m/s
S, R
Variația puterii generate cu viteza vântului
Tabel
S, R
Parametrii de calitate ai energiei
Coeficient de flicker la funcționare continuă
S
Factorul treaptă de flicker pentru operații de comutare
S
Factor de variație a tensiunii
S
Număr maxim de operații de comutare la interval de 10 minute
Număr
S
Număr maxim de operații de comutare la interval de 2 ore
Număr
S
Date pentru module generatoare de tip fotovoltaic
Numărul de panouri fotovoltaice
Număr
S
Tipul panourilor fotovoltaice
Descriere
D
Puterea nominală a panoului fotovoltaic (c.c.)
kW
S
Puterea maximă a panoului fotovoltaic (c.c.)
kW
S
Date pentru invertoarele utilizate
Numărul de invertoare
Număr
S
Tipul invertorului
Descriere
S
Certificate de tip pentru invertoare, însoțite de rezultatele testelor efectuate de laboratoare recunoscute pe plan european pentru variații de frecvență, de tensiune și trecere peste defect
Certificate
D
Puterea nominală de intrare (c.c.)
kW
S
Puterea maximă de intrare recomandată (c.c.)
kW
S
Domeniul de tensiune de intrare (c.c.)
V
S
Tensiunea maximă de intrare (c.c.)
V
S
Curentul maxim de intrare (c.c.)
A
S
Puterea activă nominală de ieșire (c.a.)
kW
S
Puterea activă maximă de ieșire (c.a.)
kW
S
Puterea reactivă nominală de ieșire (c.a.)
kVAr
S
Tensiunea nominală de ieșire (c.a.)
V, kV
S
Curentul nominal de ieșire (c.a.)
A
S
Domeniul de frecvență
Hz
S
Domeniul de reglaj al factorului de putere
Text
D
Consumul propriu maxim (c.a.)
W
D
Consumul pe timp de noapte (c.a.)
W
D
Parametrii de calitate ai energiei electrice
Număr maxim de variații ale puterii (�S/S sc ) pe minut
Număr/min
S
Valoarea maximă pentru variațiile rapide de tensiune
V, kV
S
Factor total de distorsiune de curent electric
Text
S
Armonice de curent electric (până la armonica 50)
S
Factor total de distorsiune de tensiune
S
Armonice de tensiune (până la armonica 50)
S
Factor de nesimetrie de secvență negativă de tensiune
S
Gestionarul MGCCC are obligația de a transmite la ORR datele tehnice prevăzute în tabelul nr. 1- MGCCC, în conformitate cu prevederile Procedurii de notificare pentru racordarea la rețelele electrice de interes public a sistemelor de înaltă tensiune în curent continuu și a centralelor electrice foarmate din module generatoare, care se racordează la rețelele electrice de interes public prin intermediul sistemelor de înaltă tensiune în curent continuu, și de verificare a conformității acestora, aprobată prin Ordin al președintelui Autorității Naționale de Reglementare în Domeniul Energiei .
În cadrul Procedurii prevăzute la pct. 1, ORR și OTS, după caz, pot solicita date suplimentare pentru fiecare etapă a procesului de notificare și de verificare a conformității.
Datele standard de planificare (S), comunicate prin cererea de racordare și utilizate în studiile de soluție, reprezintă totalitatea datelor tehnice generale care caracterizează MGCCC.
Datele detaliate pentru planificare (D), sunt date tehnice care permit analize speciale de stabilitate statică și tranzitorie, dimensionarea instalațiilor de automatizare și reglajul protecțiilor, precum și alte date necesare în programare operativă; datele detaliate pentru planificare (D) se transmit la ORR și OTS, după caz, cu minimum 6 luni înainte de PIF.
Datele, validate și completate la punerea sub tensiune a instalației pentru începerea perioadei de probe, sunt confirmate în procesul de verificare a conformității cu cerințele tehnice privind racordarea la rețelele electrice de interes public (R).
Secțiunea a 2-a Documentația care atestă realizarea lucrărilor premergătoare punerii sub tensiune pentru începerea perioadei de probă pentru MGCCC Documentația conține:
dovada unui acord privind schemele de protecții aplicabile în punctul de racordare;
documentele care atestă realizarea căilor de comunicație cu DMS-SCADA și/sau EMS- SCADA (o cale de comunicație), după caz;
documentele care atestă realizarea implementării soluției de agregare și integrare în DMS- SCADA și/sau EMS-SCADA convenită cu ORR și/sau OTS, după caz. Integrarea se referă cel puțin la integrarea măsurilor P (putere activă), Q (putere reactivă), U (tensiune) și frecvență precum și a consemnelor P, Q, U;
programul de punere sub tensiune pentru perioada de probe a MGCCC și data la care se preconizează punerea sub tensiune pentru perioada de probe până la puterea aprobată prin ATR corespunzătoare etapei specificate în ATR/ etapizat, pentru MGCCC; Programul se detaliază pe paliere de putere instalată; (dacă este cazul) ORR și OTS, după caz, are obligația de a publica pe pagina proprie de internet acest program;
convenția de exploatare între ORR și OTS, după caz, și gestionarul MGCCC, dosarul instalației de utilizare și procesele-verbale care confirmă recepția la terminarea lucrărilor aferente instalației de racordare;
documentul prin care se dovedește existența și montarea mijloacelor de compensare a puterii reactive în punctul de racordare, dacă acest lucru reiese din studiul de putere reactivă;
dovada înființării unui centru de dispecer local sau a integrării MGCCC într-un centru de dispecer local existent;
dovada obținerii ordinului de investire;
dovada înscrierii la piața de energie.
Secțiunea a 3-a Model de solicitare pentru punerea sub tensiune pentru perioada de probe a MGCCC
ANTET
Către,
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; (*)
Societatea (denumirea firmei, adresa, număr de înregistrare, reprezentantul legal, telefon, fax, e-mail).............................................. înregistrată la Registrul Comerțului din
cu
numărul ....................., solicită punerea sub tensiune pentru perioada de probe a MGCCC.
aflat(e) în gestiunea sa.
În susținerea acestei cereri, se anexează documentele prevăzute în Procedura de notificare pentru racordarea la rețelele electrice de interes public a sistemelor de înaltă tensiune în curent continuu și a centralelor electrice formate din module generatoare, care se racordează la rețelele electrice de interes public prin intermediul sistemelor de înaltă tensiune în curent continuu, și de verificare a conformității acestora, aprobată prin Ordinul președintelui Autorității Naționale de Reglementare în Domeniul Energiei nr. &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; .
Director/Reprezentant
legal
Data: &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;
(*) ORR
