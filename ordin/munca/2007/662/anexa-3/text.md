# Anexa 3
------- (Anexa nr. 3 la procedura) -------------------------- Fișierul Cap 1. DBF sau Cap 1. TXT conține câte o înregistrare pentru fiecare asigurat*1) și are urmatoarea structură: ----------- *1) Pentru persoanele care au mai multe contracte individuale de muncă la același angajator, declarația se va completa cu câte o înregistrare pentru fiecare contract în parte.
Denumirea câmpului Tipul câmpului Lungimea câmpului Semnificație
1 2 3 4 5
Luna declarației LD N 2 Se completează cu luna anului pentru care se întocmește declarația
Anul declarației AD N 4 Se completează cu anul pentru care se întocmește declarația
Codul unic de înregistrare (CUI)/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/codului fiscal atribuit angajatorilor - persoane juridice
Codul unic de înregistrare (CUI)/CNP al angajatorului persoană fizică CNPA N 13 Conține codul unic de înregistrare atribuit prin certificatul de înregistrare angajatorilor persoane fizice (codul numeric personal al angajatorului)
Numele și prenumele asiguratului NUME C 30 Conține numele și prenumele asiguratului
Codul numeric personal CNP N 13 Conține codul numeric personal al asiguratului
Codul numeric personal anterior CNPANT N 13 Se completează numai în cazul declarațiilor rectificative (REC = "C") și conține codul numeric personal al asiguratului din declarația inițială, care trebuie schimbat
Tipul contractului TC C 2 Se completează cu:
"1" - pentru toate raporturile de muncă/serviciu cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 8 ore;
"10" - pentru toate raporturile de muncă/serviciu cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 7 ore;
"11" - pentru toate raporturile de muncă/serviciu cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 6 ore;
"2" - pentru contractul individual de muncă cu timp parțial de lucru, unde timpul normal de lucru este de 8 ore;
"3" - pentru contractul individual de muncă cu timp parțial de lucru, unde timpul normal de lucru este de 7 ore;
"4" - pentru contractul individual de muncă cu timp parțial de lucru, unde timpul normal de lucru este de 6 ore;
"5" - pentru contractul de muncă temporară cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 8 ore;
"50" - pentru contractul de muncă temporară cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 7 ore;
"51" - pentru contractul de muncă temporară cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 6 ore;
"6" - pentru contractul de muncă temporară cu timp parțial de lucru, unde timpul normal de lucru este de 8 ore;
"7" - pentru contractul de muncă temporară cu timp parțial de lucru, unde timpul normal de lucru este de 7 ore;
"8" - pentru contractul de muncă temporară cu timp parțial de lucru, unde timpul normal de lucru este de 6 ore;
"9" - pentru toate raporturile de muncă/serviciu ale angajaților militari cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 8 ore;
"90" - pentru toate raporturile de muncă/serviciu ale angajaților militari cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 7 ore;
"91" - pentru toate raporturile de muncă/serviciu ale angajaților militari cu durata normală a timpului de muncă/lucru cu normă întreagă, unde timpul normal de lucru este de 6 ore.
Număr de ore normate în lună NOL N 3 Se completează cu numărul de ore de lucru normate în lună. Exemplu nr. 1:
- timpul de muncă/lucru cu normă întreagă: 8 ore/zi; zile lucrătoare în lună: 21 de zile; NOL= 8 ore/zi X 21 de zile = 168 de ore normate în lună. Exemplu nr. 2:
- timpul de muncă/lucru, timp parțial: 1 oră/zi; zile lucrătoare în lună: 22 de zile; NOL= 1 oră/zi X 22 de zile = 22 de ore normate în lună. Exemplu nr. 3:
- în situația unui program de lucru inegal format din două zile lucrătoare în care timpul de muncă/lucru este de 3 ore/zi și două zile lucrătoare în care timpul de muncă/lucru este de 7 ore/zi; total zile lucrate în cursul lunii: 4 zile; NOL= 3+3+7+7=20 de ore normate în lună.
Numărul de ore lucrate efectiv în lună NOEL N 3 Se completează cu numărul de ore efectiv lucrate în lună. Pentru persoana care are raporturile de muncă sau de serviciu suspendate pentru incapacitate temporară de muncă de cel mult 30 de zile, rubrica se va completa în același mod în care se completează pentru persoanele care au lucrat toată luna (orele din programul de lucru în care raporturile de muncă sau de serviciu sunt suspendate pentru incapacitate temporară de muncă de cel mult 30 de zile sunt considerate ore efectiv lucrate).
Numărul de ore suspendate în lună NOS N 3 Se completează cu numărul de ore din programul de lucru în care raporturile de muncă sau de serviciu sunt suspendate, conform legii, cu excepția suspendării pentru incapacitate temporară de muncă de cel mult 30 de zile (orele din programul de lucru în care raporturile de muncă sau de serviciu sunt suspendate pentru incapacitate temporară de muncă de cel mult 30 de zile sunt considerate ore efectiv lucrate).
Baza de calcul BC N 10 Se completează cu drepturile bănești determinate în conformitate cu prevederile art. 14 din Normelemetodologice de aplicare a Legii nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, aprobate prin Hotărârea Guvernului nr. 174/2002, cu modificările și completările ulterioare, pentru asigurații prevăzuți la art. 19 din Legea nr. 76/2002, cu modificările și completările ulterioare. În lunile în care raporturile de muncă sau de serviciu se stabilesc, încetează, se suspendă, respectiv se reiau, cu excepția suspendării pentru incapacitate temporară de muncă, dacă aceasta nu depășește 30 de zile, baza de calcul se consideră în funcție de numărul de ore efectiv lucrate în luna respectivă. Pentru persoana care are raporturile de muncă sau de serviciu suspendate pentru incapacitate temporară de muncă de cel mult 30 de zile, rubrica se va completa în același mod ca și pentru persoanele care au lucrat toată luna.
Contribuția individuală datorată CID N 8 Conține contribuția datorată de asigurat și reținută de angajator (1% din BC - cu rotunjire potrivit prevederilor legale).
Tipul asiguratului TA N 1 Se completează cu: "1" - dacă pentru asiguratul obligatoriu, prin efectul legii, în sistemul asigurărilor pentru șomaj, angajatorul are obligația, conform Legii nr. 200/2006 privind constituirea și utilizarea Fondului de garantare pentru plata creanțelor salariale, de a plăti lunar contribuția la Fondul de garantare pentru plata creanțelor salariale;
"2" - dacă pentru asiguratul obligatoriu, prin efectul legii, în sistemul asigurărilor pentru șomaj, angajatorul nu are obligația, conform Legii nr. 200/2006 privind constituirea și utilizarea Fondului de garantare pentru plata creanțelor salariale, de a plăti lunar contribuția la Fondul de garantare pentru plata creanțelor salariale.
Rectificativă REC C 1 - spațiu dacă declarația nu este rectificativă;
- "M", dacă se dorește modificarea înregistrării inițiale;
- "A", dacă se dorește adăugarea unei înregistrări noi;
- "S", dacă se dorește ștergerea înregistrării inițiale;
- "C", dacă se dorește modificarea CNP-ului din declarația inițială.
Fișierul cap. 2. DBF sau cap. 2. TXT conține o singură înregistrare și are următoarea structură:
Denumirea câmpului Tipul câmpului Lungimea câmpului Semnificație
1 2 3 4 5
Luna declarației LD N 2 Se completează cu luna anului pentru care se întocmește declarația
Anul declarației AD N 4 Se completează cu anul pentru care se întocmește declarația
Denumirea angajatorului DEN C 30 Conține denumirea angajatorului
Codul unic de înregistrare (CUI)/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/codului fiscal atribuit angajatorilor - persoane juridice.
Codul unic de înregistrare anterior (CUI)/CF pentru angajatori persoane juridice CFANT N 10 Se completează numai în cazul declarațiilor rectificative (REC= "C") și conține codul fiscal al angajatorului din declarația inițială, care trebuie schimbat (a fost introdus eronat în declarația inițială).
Codul unic de înregistrare (CUI)/CNP pentru angajatori persoane fizice CNPA N 13 Conține codul unic de înregistrare atribuit prin certificatul de înregistrare angajatorilor persoane fizice (codul numeric personal al angajatorului).
Codul unic de înregistrare (CUI)/CNP pentru angajatori persoane fizice CNPAANT N 13 Se completează numai în cazul declarațiilor rectificative (REC= "C") și conține codul numeric personal al angajatorului persoană fizică din declarația inițială, care trebuie schimbat (a fost introdus eronat în declarația inițială).
Codul CAEN CAEN C 4 Codul CAEN al angajatorului pentru activitatea de bază
Localitatea (oraș, comună) LOC C 30 Adresa, sediul angajatorului - localitatea (orașul sau comuna)
Strada (strada, satul) STR C 30 Adresa, sediul angajatorului - strada sau satul - dacă localitatea este oraș, se completează în mod obligatoriu și strada
Număr NRA C 10 Adresa, sediul angajatorului - numărul
Bloc BL C 10 Adresa, sediul angajatorului - blocul
Scara SC C 4 Adresa, sediul angajatorului - scara
Etaj ET C 2 Adresa, sediul angajatorului - etajul
Apartament AP C 4 Adresa, sediul angajatorului - apartamentul
Sector SECT N 1 Adresa, sediul angajatorului - sectorul (numai pentru București); câmp obligatoriu pentru angajatorii cu sediul în municipiul București
Județ JUD C 15 Adresa, sediul angajatorului - județul
Telefon TEL N 9 Numărul de telefon pentru contactare al angajatorului
Fax FAX N 9 Numărul de fax al angajatorului
E-mail MAIL C 30 Adresa de e-mail a angajatorului de la care se trimite declarația, respectiv cea comunicată în scris în condițiile art. 5 alin. (2) din procedură.
Cod poștal CPOST C 6 Codul poștal
Cod IBAN IBAN C 24 Codul IBAN
Banca BANCA C 30 Banca la care angajatorul are deschis contul
Fondul de salarii brute realizate de personalul contractual FS1 N 15 Conține total fond de salarii brute realizate de asigurații menționați la art. 19 lit. a) din Legea nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, cu modificările și completările ulterioare, (salariații încadrați în temeiul unui contract individual de muncă încheiat pentru normă întreagă sau cu timp parțial ori a unui contract de muncă la domiciliu, de muncă temporară sau de ucenicie la locul de muncă, indiferent de durata acestora, cu excepția persoanelor care au calitatea de pensionar), determinat în conformitate cu prevederile art. 13 din Normele metodologice de aplicare a Legii nr. 76/2002, aprobate prin Hotărârea Guvernului nr. 174/2002, cu modificările și completările ulterioare.
Fondul de salarii brute realizate de personal necontractual FS2 N 15 Conține total fond de salarii brute realizate de asigurații menționați la art. 19 lit. b) - f) din Legea nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, cu modificările și completările ulterioare, determinat în conformitate cu prevederile art. 13 dinNormele metodologice de aplicare a Legii nr. 76/2002, aprobate prin Hotărârea Guvernului nr. 174/2002, cu modificările și completările ulterioare.
Contribuția angajatorului diminuată CAD1 N 10 Contribuția datorată de angajator la bugetul asigurărilor pentru șomaj, cu rotunjire potrivit prevederilor legale. [CAD1 = FS1 x cota contribuției datorate de angajatori la bugetul asigurărilor pentru șomaj, diminuată conform art. 7 alin. (2) din Legea nr. 200/2006 privind constituirea și utilizarea Fondului de garantare pentru plata creanțelor salariale].
Contribuția angajatorului nediminuată CAD2 N 10 Contribuția datorată de angajator la bugetul asigurărilor pentru somaj, cu rotunjire potrivit prevederilor legale [CAD2 = FS2 x cota contribuției datorate de angajatori la bugetul asigurărilor pentru șomaj, prevăzută de art. 26 din Legea nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, cu modificările și completările ulterioare (cota de contribuție nediminuată conform art. 7 alin. (2) din Legea nr. 200/2006 privind constituirea și utilizarea Fondului de garantare pentru plata creanțelor salariale)].
Total contribuție datorată de angajator TCAD N 10 Contribuția totală datorată de angajator la bugetul asigurărilor pentru șomaj (este egală cu suma dintre CAD1 și CAD2).
Total contribuții individuale datorate de asigurați și colectate de angajator TCID N 10 Suma contribuțiilor individuale datorate la bugetul asigurărilor pentru șomaj declarate de angajator în cap. 1.
Subvenții, scutiri și reduceri recuperate SSRR N 10 Suma subvențiilor, scutirilor și reducerilor recuperate din contribuția datorată de angajator (nu poate fi mai mare decât această contribuție).
Rest de plată RP N 10 Se completează cu suma pe care angajatorul o virează la bugetul asigurărilor pentru șomaj, în cazul în care TCAD>SSRR. (RP = TCAD - SSRR), după efectuarea, în condițiile legii, a deducerilor din contribuția datorată de angajator.
Rest de încasat RI N 10 Se completează cu suma pe care angajatorul o are de încasat de la bugetul asigurărilor pentru șomaj, în cazul în care TCAD = SSRR [reprezintă suma subvențiilor, scutirilor și reducerilor de restituit de către AJOFM/AMOFM (SUB80RES, SC80144RES, SUB85RES, SC85144RES, SUB58RES, SUB116RES, RED9394RES, SUB17ARES, SUB17BRES, SUB172RES), după efectuarea, în condițiile legii, a deducerilor din contribuția datorată de angajator].
Numărul de asigurați din cap. 1 NA N 6 Numărul de asigurați (CNP-uri unice) din cap. 1.
Numărul de înregistrări din cap. 1 NI N 6 Numărul de înregistrări din cap. 1; poate fi mai mare decât numărul de asigurați (NA), în cazul în care cel puțin un asigurat are mai mult de un contract individual de muncă cu respectivul angajator.
Numărul de asigurați de tip asigurat = 2 NTA N 6 Numărul de asigurați care în cap. 1 sunt de tip asigurat 2 (TA = 2).
Subvenții conform art. 80 din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperate din CAD SUB80REC N 10 Sumele cuvenite pentru timpul efectiv lucrat, conform art. 80 din Legea nr. 76/2002, cu modificările si completările ulterioare, recuperate prin deducere din TCAD.
Subvenții conform art. 80 din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit SUB80RES N 10 Sumele cuvenite pentru timpul efectiv lucrat, conform art. 80 din Legea nr. 76/2002, cu modificările si completările ulterioare, de restituit de către AJOFM/AMOFM.
Scutire de la plata contribuției datorate de angajator, conform art. 80 din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperată din CAD SC80144REC N 10 Scutire de la plata contribuției datorate de angajator, aferentă absolvenților încadrați, conform art. 80 din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperată prin deducere din TCAD.
Scutire de la plata contribuției datorate de angajator, conform art. 80 din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit SC80144RES N 10 Scutire de la plata contribuției datorate de angajator, aferentă absolvenților încadrați, conform art. 80 din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit de către AJOFM/AMOFM.
Subvenții conform art. 85 din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperate din CAD SUB85REC N 10 Sumele cuvenite pentru timpul efectiv lucrat, conform art. 85 din Legea nr. 76/2002, cu modificările si completările ulterioare, recuperate prin deducere din TCAD.
Subvenții conform art. 85 din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit SUB85RES N 10 Sumele cuvenite pentru timpul efectiv lucrat, conform art. 85 din Legea nr. 76/2002, cu modificările si completările ulterioare, de restituit de către AJOFM/AMOFM.
Scutire de la plata contribuției datorate de angajator, conform art. 85 alin. (1) din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperată din CAD SC85144REC N 10 Scutire de la plata contribuției datorate de angajator, aferentă persoanelor încadrate din categoriile prevăzute de lege, conform art. 85 alin. (1) din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperată prin deducere din TCAD.
Scutire de la plata contribuției datorate de angajator, conform art. 85 alin. (1) din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit SC85144RES N 10 Scutire de la plata contribuției datorate de angajator, aferentă persoanelor încadrate din categoriile prevăzute de lege, conform art. 85 alin. (1) din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit de către AJOFM/AMOFM.
Subvenții conform art. 7 alin. (3) din Ordonanța de urgență a Guvernului nr. 58/2001, cu modificările și completările ulterioare, recuperată din CAD SUB58REC N 10 Subvenții conform art. 7 alin. (3) din Ordonanța de urgență a Guvernului nr. 58/2001, recuperate prin deducere din TCAD.
Subvenții conform art. 7 alin. (3) din Ordonanța de urgență a Guvernului nr. 58/2001, cu modificările și completările ulterioare, de restituit SUB58RES N 10 Subvenții conform art. 7 alin. (3) din Ordonanța de urgență a Guvernului nr. 58/2001, de restituit de către AJOFM/AMOFM.
Subvenții în baza Legii nr. 116/2002 și a Nomelor metodologice aprobate prin Hotărârea Guvernului nr. 1.149/2002, recuperate din CAD SUB116REC N 10 Subvenții în baza Legii nr. 116/2002 și a Normelormetodologice aprobate prin Hotărârea Guvernului nr. 1.149/2002, recuperate prin deducere din TCAD.
Subvenții în baza Legii nr. 116/2002 și a Normelor metodologice aprobate prin Hotărârea Guvernului nr. 1.149/2002, de restituit SUB116RES N 10 Subvenții în baza Legii nr. 116/2002 și a Normelor metodologice aprobate prin Hotărârea Guvernului nr. 1.149/2002, de restituit de către AJOFM/AMOFM.
Reduceri ale contribuției datorate de angajator, conform art. 93 și 94 din Legea nr. 76/2002, cu modificările și completările ulterioare, recuperate din CAD RED9394REC N 10 Reduceri ale contribuției datorate de angajator, conform art. 93 și 94 din Legea nr. 76/2002, recuperate prin deducere din TCAD.
Reduceri ale contribuției datorate de angajator, conform art. 93 și 94 din Legea nr. 76/2002, cu modificările și completările ulterioare, de restituit. RED9394RES N 10 Reduceri ale contribuției datorate de angajator, conform art. 93 și 94 din Legea nr. 76/2002, de restituit de către AJOFM/AMOFM.
Subvenții conform art. 17 alin. (1) lit. a) din Legea nr. 279/2005, recuperate din CAD SUB17AREC N 10 Sume cuvenite pentru timpul efectiv lucrat, conform art. 17 alin. (1) lit. a) din Legea nr. 279/2005, recuperate prin deducere din TCAD.
Subvenții conform art. 17 alin. (1) lit. a) din Legea nr. 279/2005, de restituit SUB17ARES N 10 Sume cuvenite pentru timpul efectiv lucrat, conform art. 17 alin. (1) lit. a) din Legea nr. 279/2005, de restituit de către AJOFM/AMOFM.
Subvenții, conform art. 17 alin. (1) lit. b) din Legea nr. 279/2005, recuperate din CAD SUB17BREC N 10 Contravaloarea lunară a servicilor de instruire teoretică a ucenicilor, conform art. 17 alin. (1) lit. b) din Legea nr. 279/2005, recuperată prin deducere din TCAD.
Subvenții conform art. 17 alin. (1) lit. b) din Legea nr. 279/2005, de restituit SUB17BRES N 10 Contravaloarea lunară a serviciilor de instruire teoretică a ucenicilor, conform art. 17 alin. (1) lit. b) din Legea nr. 279/2005, de restituit de către AJOFM/AMOFM.
Subvenții, conform art. 1 din Legea nr. 72/2007, recuperate din CAD SUB172REC N 10 Sumele cuvenite pentru timpul efectiv lucrat, conform art. 1 din Legea nr. 72/2007, recuperate prin deducere din TCAD
Subvenții, conform art. 1 din Legea nr. 72/2007, de restituit SUB172RES N 10 Sumele cuvenite pentru timpul efectiv lucrat, conform art. 1 din Legea nr. 72/2007, de restituit de către AJOFM/AMOFM
Numele persoanei autorizate NUMEA C 15 Numele persoanei autorizate să depună declarația
Prenumele persoanei autorizate PREA C 15 Prenumele persoanei autorizate să depună declarația
Funcția persoanei autorizate FUNCTA C 15 Funcția persoanei autorizate să depună declarația
Rectificativă REC C 1 - spațiu, dacă declarația nu este rectificativă
- "M", dacă se dorește modificarea înregistrării inițiale
- "C", dacă se dorește modificarea CF/CNP-ului din declarația inițială
------------
