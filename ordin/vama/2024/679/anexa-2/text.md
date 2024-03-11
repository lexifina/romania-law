# Anexa nr. 2 (Anexa la instrucțiuni)
Reguli de completare a rubricilor din e-DA/e-DAS
Pentru completarea unui e-DA/e-DAS, după autentificarea în sistem prin introducerea userului și parolei alocate, se accesează butonul „Creează Mișcare”, care deschide un ecran ce afișează secțiunea „Informații generale”.
În secțiunea „Informații generale” se completează rubricile 1-16 și 18. Accesând butonul „Încarcă xml” pot fi încărcate datele existente într-un fișier local, în format xml. Accesând butonul „Următor” se poate trece la secțiunea „Informații expediere produse”, în care se completează rubrica 17.
Trecerea de la o căsuță/rubrică la alta se poate face cu ajutorul tastei „tab” sau poziționând direct mouse-ul pe rubrica/ subrubrica care se dorește a fi completată.
A.
Câmpurile e-DA/e-DAS ce trebuie completate Rubrica „Tipul mesajului” permite selectarea unuia dintre următoarele coduri: - 1 - trimitere standard;
- 2 - (rezervat);
- 3 - prezentare pentru accize plătite (se utilizează pentru deplasarea produselor deja eliberate în consum).
Tipul de mesaj nu este vizibil într-un e-DA/e-DAS căruia i-a fost atribuit un ARC și nici în documentul pe suport hârtie utilizat în procedură de rezervă.
Rubrica „Indicator de prezentare amânată” - obligatoriu de completat la prezentarea unui e-DA/e-DAS pentru o deplasare începută în procedură de rezervă pe baza documentului pe suport hârtie. Acest element de date nu este vizibil într-un e-DA/e-DAS căruia i-a fost atribuit un ARC și nici în documentul pe suport hârtie utilizat în procedură de rezervă.
Rubrica „Codul tipului de origine”, explicată la subrubrica 9d), și rubrica „Codul tipului de destinație”, explicată la subrubrica 1a), sunt necesar a fi completate la începutul paginii „Informații generale”. În funcție de opțiuni, se modifică structura paginii ce urmează a fi completată.
1.
Deplasare de mărfuri accizabile a)
Codul tipului de destinație Rubrica permite selectarea destinației deplasării utilizând unul dintre următoarele coduri: - 1 - Antrepozit fiscal;
- 2 - Destinatar înregistrat;
- 3 - Destinatar înregistrat ocazional;
- 4 - Livrare directă;
- 5 - Destinatar scutit;
- 6 - Export;
- 8 - Destinație necunoscută;
- 9 - Destinație - Destinatar certificat;
- 10 - Destinație - Destinatar certificat ocazional;
- 11 - Destinație - Returnare la locul de expediție al expeditorului;
- 12 - Utilizator final.
În funcție de opțiunea selectată se modifică structura paginii ce urmează a fi completată.
b)
Durata călătoriei Ținând cont de mijlocul de transport și de distanță, se înscrie perioada de timp normală necesară călătoriei, exprimată în ore sau zile. Indicația pentru ore trebuie să fie un număr mai mic sau egal cu 24. Indicația pentru zile trebuie să fie un număr mai mic sau egal cu valorile posibile ale duratei maxime a călătoriei pentru fiecare cod al modului de transport, stipulate la pct. 26 din instrucțiuni.
c)
Organizarea transportului Rubrica permite selectarea persoanei responsabile cu organizarea primului transport, utilizând unul dintre următoarele coduri: - 1 - Expeditor;
- 2 - Destinatar;
- 3 - Proprietarul produselor;
- 4 - Alta.
d)
Cod de referință administrativ unic - ARC Este generat automat de aplicația autorității vamale de expediere la momentul validării proiectului de e-DA/e-DAS. Structura ARC este următoarea: - două caractere numerice care corespund anului acceptării formale a deplasării;
- două caractere alfanumerice care reprezintă identificatorul SM în care a fost prezentat inițial e-DA/e-DAS;
- 15 caractere alfanumerice (cifre și litere majuscule) reprezentând un cod unic pentru fiecare deplasare, atribuit la nivel național. Modul în care este completat acest câmp este în responsabilitatea autorității vamale, dar fiecare deplasare EMCS trebuie să aibă un număr unic;
- un caracter alfanumeric ce identifică tipul deplasării. Valoarea „P” corespunde unei deplasări de produse eliberate deja pentru consum și orice altă valoare pentru o deplasare de produse în regim suspensiv/de scutire/exceptare de accize;
- un caracter numeric ce reprezintă o cifră de control care ajută la detectarea unei erori în momentul introducerii ARC.
e)
Data și ora validării e-DA/e-DAS Se completează de către autoritatea vamală de expediere la momentul validării proiectului de e-DA/e-DAS. Ora indicată este ora locală.
f)
Număr secvențial Se completează de către autoritatea vamală de expediere la momentul validării proiectului de e-DA/e-DAS și pentru fiecare schimbare a destinației. Este fixat la 1 în momentul validării inițiale și mărit cu o unitate în fiecare e-DA/e-DAS generat în sistem de autoritatea vamală de expediție, la fiecare schimbare de destinație.
g)
Data și ora validării actualizării Se completează de către autoritatea vamală de expediere în cazul schimbării destinației și reprezintă data și ora validării mesajului de schimbare a destinației. Ora indicată este ora locală.
2.
Expeditor a)
Codul de acciză al operatorului - se înscrie codul de acciză din SEED valabil al antrepozitarului autorizat, al expeditorului înregistrat, al expeditorului certificat sau al expeditorului certificat ocazional, după caz;
b)
Denumirea operatorului;
c)
Strada;
d)
Numărul;
e)
Codul poștal;
f)
Orașul;
g)
Limbă - se specifică limba utilizată în acest set de date. Rubrica „Expeditor” va fi completată automat cu datele aferente antrepozitarului autorizat, respectiv ale expeditorului înregistrat, expeditorului certificat sau expeditorului certificat ocazional de care aparține utilizatorul care a accesat aplicația.
3.
Locul de expediere - rubrică obligatorie, dacă „Codul tipului de origine” este „Antrepozit fiscal” sau „Accize plătite” a)
Codul de acciză al antrepozitului fiscal - se înscrie numărul de înregistrare SEED valabil al antrepozitului fiscal autorizat, prin selectarea antrepozitului din care se face livrarea din lista antrepozitelor aparținând antrepozitarului selectat la rubrica 2a);
b)
Denumirea operatorului;
c)
Strada;
d)
Numărul;
e)
Codul poștal;
f)
Orașul;
g)
Limba - se specifică limba utilizată în acest set de date.
Subrubricile b)-g) se completează automat, după selectarea subrubricii a).
4.
Birou de expediere-import - rubrică obligatorie dacă „Codul tipului de origine” este „Import”, caz în care se selectează codul BV unde are loc punerea în liberă circulație a produselor accizabile 4.a.
Numărul de referință al biroului - se specifică codul biroului vamal unde are loc punerea în liberă circulație.
5.
Destinatar - rubrică obligatorie, cu excepția cazurilor în care: - la rubrica „Codul tipului de destinație” a fost selectat „Destinație necunoscută”.
a)
Identificarea operatorului - subrubrică obligatorie, când la rubrica „Codul tipului de destinație” a fost selectat „Antrepozit fiscal”, „Destinatar înregistrat”, „Destinatar înregistrat ocazional”, „Livrare directă”, „Destinație - Destinatar certificat”, „Destinație - Destinatar certificat ocazional”, „Destinație - Returnare la locul de expediție al expeditorului” sau „Utilizator final”, după caz. În cazul „Export”, completarea subrubricii este opțională. În cazul destinatarului scutit în sensul art. 395 din Codul fiscal, setul de date nu se aplică. Când subrubrica este obligatorie se completează prin înscrierea codului de acciză valabil, transmis în SEED, al operatorului economic autorizat să primească produse accizabile, cu excepția „Codului tipului de destinație - Returnare la locul de expediție al expeditorului”, când se specifică un număr de înregistrare SEED valabil al destinatarului, care este expeditorul certificat inițial sau expeditorul certificat ocazional al deplasării.
Când subrubrica este opțională se înscrie numărul de identificare TVA al persoanei care reprezintă expeditorul la BV de export;
b)
Denumirea operatorului;
c)
Strada;
d)
Numărul;
e)
Codul poștal;
f)
Orașul;
g)
Limba - se specifică limba utilizată în acest set de date;
h)
Număr EORI - se înscrie codul EORI al persoanei responsabile cu depunerea declarației vamale de export. Subrubricile b)-f) din rubrica „Destinatar” se vor completa automat cu datele aferente primitorului, după validarea codului de acciză introdus la subrubrica a).
Subrubrica h) din rubrica „Destinatar” este opțională când la rubrica „Codul tipului de destinație” a fost selectat „Export” și nu se aplică când la rubrica „Codul tipului de destinație” a fost selectat „Antrepozit fiscal”, „Destinatar înregistrat”, „Destinatar înregistrat ocazional”, „Livrare directă”, „Destinatar scutit”, „Destinație necunoscută”, „Destinație - Destinatar certificat”, „Destinație - Destinatar certificat ocazional”, „Destinație - Returnare la locul de expediție al expeditorului „sau „Utilizator final”.
6.
Date complementare destinatar - rubrică obligatorie când la rubrica „Codul tipului de destinație” a fost selectat „Destinatar scutit” în sensul art. 395 din Codul fiscal
a)
Codul statului membru - se înscrie codul statului membru de destinație.
b)
Numărul de serie al certificatului de scutire, dacă este menționat pe certificatul de scutire prevăzut în Regulamentul (UE) 2022/1.637.
7.
Locul livrării - rubrică obligatorie când la rubrica „Codul tipului de destinație” a fost selectat „Antrepozit fiscal”, „Livrare directă”, „Destinație - Destinatar certificat”, „Destinație - Destinatar certificat ocazional” sau „Utilizator final”. Rubrica este opțională când la rubrica „Codul tipului de destinație” a fost selectat „Destinatar înregistrat”, „Destinatar înregistrat ocazional” sau „Destinatar scutit” în sensul art. 395 din Codul fiscal. În cazul în care rubrica este opțională și la rubrica „Codul tipului de destinație” a fost selectat „Destinatar înregistrat”, rubrica nu se aplică pentru proiectul de e-DA, iar statul membru de expediție poate completa această rubrică numai cu adresa sediului social al destinatarului înregistrat, indicată în SEED. a)
Identificarea operatorului - subrubrică obligatorie când la rubrica „Codul tipului de destinație” a fost selectat „Antrepozit fiscal”, „Destinație - Destinatar certificat”, „Destinație - Destinatar certificat ocazional” sau „Utilizator final”. Completarea subrubricii este opțională când la rubrica „Codul tipului de destinație” a fost selectat „Destinatar înregistrat”, „Destinatar înregistrat ocazional” sau „Destinatar scutit” în sensul art. 395 din Codul fiscal. -
Când subrubrica este obligatorie se completează cu codul de acciză valabil, transmis în SEED, al antrepozitului fiscal primitor din lista antrepozitelor aparținând antrepozitarului primitor sau al utilizatorului final primitor din lista locațiilor autorizate aparținând utilizatorului final, după caz.
-
Când subrubrica este opțională se poate înscrie numărul de identificare TVA sau orice alt identificator.
b)
Denumirea operatorului - subrubrică obligatorie când la rubrica „Codul tipului de destinație” a fost selectat „Antrepozit fiscal”, „Destinatar înregistrat”, „Destinatar înregistrat ocazional”, „Destinatar scutit” în sensul art. 395 din Codul fiscal, „Destinație - Destinatar certificat”, „Destinație - Destinatar certificat ocazional” sau „Utilizator final”. Când la rubrica „Codul tipului de destinație” a fost selectat „Livrare directă”, în cazul livrărilor de produse accizabile în regim scutit destinate alimentării navelor, se vor înscrie numele operatorului și numele navei în care se descarcă produsele.
c)
Strada;
d)
Numărul;
e)
Codul poștal;
f)
Orașul;
g)
Limba - se specifică limba utilizată în acest set de date.
Subrubricile c), e) și f) sunt obligatorii când la rubrica „Codul tipului de destinație” a fost selectat „Destinatar înregistrat”, „Destinatar înregistrat ocazional”, „Livrare directă”, „Destinatar scutit” în sensul art. 395 din Codul fiscal, „Destinație - Destinatar certificat”, „Destinație - Destinatar certificat ocazional”. Subrubricile devin opționale când la rubrica „Codul tipului de destinație” este selectat „Antrepozit fiscal” sau „Utilizator final”.
8.
Birou Locul livrării - Birou vamal de export - rubrică obligatorie când la rubrica „Codul tipului de destinație” a fost selectat „Export”. 8.a.
- Numărul de referință al biroului - se completează codul BV de export la care va fi depusă declarația vamală de export.
9. e-DA/e-DAS a)
Numărul de referință local - subrubrică obligatorie, se completează prin înscrierea numărului de serie unic atribuit de către expeditor, care identifică lotul în evidența expeditorului.
b)
Numărul facturii/avizului - subrubrică obligatorie. Avizul de însoțire a mărfurilor se înscrie în cazul deplasării produselor accizabile de la antrepozitul fiscal către alte locuri proprii de depozitare și/sau comercializare sau în cazul deplasării produselor accizabile de la antrepozitul fiscal către clienți, dacă la momentul expedierii nu se emite factura sau dacă expedierea se face direct către clienții cumpărătorului revânzător;
c)
Data facturii/avizului - subrubrică obligatorie. Se selectează din calendarul afișat data documentului indicat la subrubrica b).
d)
Codul tipului de origine - subrubrică obligatorie. Se completează prin selectarea: - 1 - „Origine - Antrepozit fiscal”, dacă produsele sunt expediate dintr-un antrepozit fiscal; sau
- 2 - „Origine - Import”, dacă produsele au fost puse în liberă circulație la un BV; sau
- 3 - „Origine - Accize plătite”, dacă produsele sunt eliberate pentru consum.
e)
Data expedierii - subrubrică obligatorie. Se înscrie data la care începe deplasarea și nu poate depăși cu mai mult de 7 zile data prezentării proiectului de e-DA. Data expedierii poate fi o dată din trecut în cazul în care aplicația EMCS-RO-Mișcări a fost indisponibilă la momentul expedierii produselor, iar expeditorul a utilizat procedura de rezervă de transmitere a DA la autoritatea vamală de expediere.
f)
Ora expedierii - subrubrică obligatorie. Se înscrie ora locală la care începe deplasarea.
g)
ARC în amonte - se completează de către autoritatea de expediere la momentul validării unor noi e-DA în urma validării mesajului privind operațiunea de divizare. ARC-ul care trebuie specificat este cel al e-DA înlocuit.
9.1.
DAU Import - rubrică obligatorie, dacă la rubrica „Codul tipului de origine” se selectează „Import” 9.1.a.
Număr SAD Import - subrubrică obligatorie. Se înscrie/înscriu numărul/numerele documentului administrativ unic/documentelor administrative unice utilizat/utilizate pentru punerea în liberă circulație a produselor vizate. Se completează de către expeditor la momentul transmiterii proiectului de e-DA sau de către autoritățile competente ale statului membru de expediție la momentul validării proiectului de e-DA.
10.
Autoritatea competentă a locului de expediere - rubrică obligatorie 10.a.
Numărul de referință al biroului - se specifică codul biroului vamal competent al statului membru de expediție responsabil cu controlul accizelor la locul expediției.
11.
Garanția deplasării - rubrică obligatorie a)
Codul tipului de garant - se înscrie/înscriu persoana responsabilă/persoanele responsabile cu furnizarea garanției, selectând tipul garantului din listă: - 1 - expeditor;
- 2 - transportator;
- 3 - proprietarul produsului accizabil;
- 4 - destinatar;
- 5 - nu este furnizată nicio garanție, în conformitate cu art. 17 alin. (2) și cu art. 17 alin. (5) lit. b) din Directiva 2020/262/CE;
- 12 - garanție comună a expeditorului și a transportatorului;
- 13 - garanție comună a expeditorului și a proprietarului produselor accizabile;
- 14 - garanție comună a expeditorului și a destinatarului;
- 23 - garanție comună a transportatorului și a proprietarului produselor accizabile;
- 24 - garanție comună a transportatorului și a destinatarului;
- 34 - garanție comună a proprietarului produselor accizabile și a destinatarului;
- 123 - garanție comună a expeditorului, a transportatorului și a proprietarului produselor accizabile;
- 124 - garanție comună a expeditorului, a transportatorului și a destinatarului;
- 134 - garanție comună a expeditorului, a proprietarului produselor accizabile și a destinatarului;
- 234 - garanție comună a transportatorului, a proprietarului produselor accizabile și a destinatarului;
- 1234 - garanție comună a expeditorului, a transportatorului, a proprietarului produselor accizabile și a destinatarului. Tipul garantului va fi selectat potrivit legislației în vigoare.
12.
Operator garant - rubrică obligatorie dacă garantul este altul decât expeditorul și/sau destinatarul ori garanție comună a celor doi sau nu este furnizată nicio garanție. Se înscriu datele de identificare ale transportatorului și/sau proprietarului produselor dacă acesta/aceștia furnizează garanția.
a)
Codul de acciză al operatorului;
b)
Numărul TVA;
c)
Denumirea operatorului;
d)
Strada;
e)
Numărul;
f)
Codul poștal;
g)
Orașul;
h)
Limba - se specifică limba utilizată în acest set de date. Subrubricile a) și b) se completează cu codul de acciză valabil înscris în SEED sau un cod de identificare în scopuri de TVA valabil al transportatorului sau al proprietarului produselor accizabile, după caz.
Subrubricile c), d), f) și g) sunt opționale dacă este completată subrubrica a); în caz contrar devin obligatorii.
13.
Transport - rubrică obligatorie a)
Codul modului de transport - subrubrică obligatorie; se înscrie modul de transport la momentul începerii deplasării, selectând, după caz, din listă: - 0 - altul;
- 1 - transport pe mare;
- 2 - transport feroviar;
- 3 - transport rutier;
- 4 - transport aerian;
- 5 - trimitere poștală;
- 7 - instalație de transport fixă;
- 8 - transport pe căi navigabile interioare. Atunci când „Codul tipului de garant” este „5 - Nu se furnizează garanții în conformitate cu art. 17 alin. (2) și cu art. 17 alin. (5) lit. (b) din Directiva (UE) 2020/262”, codul modului de transport trebuie să fie „Transport pe mare” sau „Instalație de transport fixă”.
b)
Informații complementare - subrubrică obligatorie dacă codul modului de transport este „Altul”. Se va înscrie o descriere textuală a modului de transport;
c)
Limbă informații complementare - se specifică limba utilizată în acest set de date;
14.
Organizatorul transportului - rubrică obligatorie pentru identificarea persoanei responsabile cu primul transport, dacă la subrubrica 1c) a fost selectat „Proprietarul produselor” sau „Altul”. a)
Numărul TVA;
b)
Denumirea operatorului;
c)
Strada;
d)
Numărul;
e)
Codul poștal;
f)
Orașul;
g)
Limba - se specifică limba utilizată în acest set de date. Subrubricile b), c), e), f) și g) sunt obligatorii dacă se completează rubrica 14.
15.
Primul transportator - rubrică obligatorie, pentru identificarea persoanei responsabile cu efectuarea primului transport a)
Numărul TVA;
b)
Denumirea operatorului;
c)
Strada;
d)
Numărul;
e)
Codul poștal;
f)
Orașul;
g)
Limba - se specifică limba utilizată în acest set de date.
16.
Detalii privind transportul - rubrică obligatorie a)
Codul unității de transport - subrubrică obligatorie. Se selectează unitatea de transport în funcție de modul de transport indicat la subrubrica 13 a), care poate fi: - 1 - container;
- 2 - vehicul;
- 3 - remorcă;
- 4 - cap tractor;
- 5 - instalație de transport fixă.
b)
Identitatea unităților de transport - subrubrică obligatorie. Se înscrie numărul de înregistrare al unității/unităților de transport, cu excepția cazului în care la codul unității de transport este 5 - instalație de transport fixă.
c)
Identitatea sigiliului comercial - subrubrică obligatorie, dacă sunt utilizate sigilii comerciale. Se înscriu datele de identificare ale sigiliilor comerciale utilizate la sigilarea unității de transport.
d)
Informații privind sigiliul - subrubrică opțională. Se pot înscrie orice informații suplimentare privind sigiliile comerciale (de exemplu, tipul de sigiliu utilizat).
e)
Limbă informații sigiliu - subrubrică obligatorie, dacă se completează subrubrica 16d). Se specifică limba utilizată în acest set de date.
f)
Informații complementare - subrubrică opțională. Se pot înscrie orice informații suplimentare referitoare la transport, de exemplu, identitatea oricărui transportator ulterior, informații referitoare la unități de transport ulterioare.
g)
Limbă informații complementare - subrubrică obligatorie dacă se completează subrubrica f). Se specifică limba utilizată în acest set de date.
17.
Corpul e-DA/e-DAS - rubrică obligatorie. Se completează câte un set de date separat pentru fiecare produs care face parte din lot. a)
Număr unic de referință al corpului de date - subrubrică obligatorie. Se înscrie un număr secvențial unic care începe cu 1.
b)
Codul produsului accizabil - subrubrică obligatorie. Se înscrie codul produsului accizabil, potrivit OMFP nr. 221/2016. Atunci când codul tipului de garant este „5 - Nu se furnizează garanții în conformitate cu art. 17 alin. (2) și cu art. 17 alin. (5) lit. (b) din Directiva (UE) 2020/262”, codul produsului accizabil trebuie să fie cel al unui produs energetic.
c)
Codul NC - subrubrică obligatorie. Se selectează din lista aferentă codul NC aplicabil la data expedierii. Valoarea acestui element de date trebuie să fie mai mare ca zero.
d)
Cantitatea - subrubrică obligatorie. Se înscrie cantitatea, exprimată în unitatea de măsură asociată codului produsului. În cazul unei deplasări către un destinatar înregistrat ocazional, destinatar certificat ocazional sau utilizator final, cantitatea nu trebuie să o depășească pe cea pe care primitorul este autorizat să o primească, după caz. În cazul unei deplasări către un destinatar scutit în sensul art. 395 din Codul fiscal, cantitatea nu trebuie să o depășească pe cea înregistrată în certificatul de scutire de accize. Valoarea acestui element de date trebuie să fie mai mare ca zero.
e)
Masa brută - subrubrică obligatorie. Se înscrie masa brută a lotului (produse accizabile cu ambalaj). Valoarea acestui element de date trebuie să fie mai mare ca zero. Masa brută trebuie să fie cel puțin egală cu Masa netă.
f)
Masa netă - subrubrică obligatorie. Se înscrie masa produselor accizabile fără ambalaj (pentru alcool și băuturile alcoolice, produse energetice și pentru toate produsele din tutun, cu excepția țigărilor). Valoarea acestui element de date trebuie să fie mai mare ca zero.
g)
Tăria alcoolică în volume, exprimată în procente - subrubrică obligatorie dacă este aplicabil produselor accizabile respective. Se înscrie Tăria alcoolică (procent per volum la 20°C dacă produsele sunt încadrate în categoria B, W, I sau S, potrivit OMFP nr. 221/2016). Valoarea acestui element de date trebuie să fie mai mare ca zero. Valoarea acestui element de date trebuie să fie mai mare ca 0,5 și mai mică sau egală cu 100.
h)
Gradul Plato - subrubrică obligatorie dacă nivelul accizei pentru bere este stabilit pe baza gradului Plato în statul membru de expediție și/sau statul membru de destinație. Valoarea acestui element de date trebuie să fie mai mare ca zero.
i)
Marcajul fiscal - subrubrică opțională. Se înscriu orice informații suplimentare referitoare la marcajele fiscale impuse de autoritatea competentă de destinație.
j)
Limbă marcaj fiscal - subrubrică obligatorie dacă se completează subrubrica i). Se specifică limba utilizată în acest set de date.
k)
Indicatorul marcajului fiscal utilizat - rubrică obligatorie dacă sunt utilizate marcaje fiscale. Se bifează corespunzător („1” - dacă produsele poartă sau conțin marcaje fiscale sau „0” - dacă produsele nu poartă sau nu conțin marcaje fiscale).
l)
Denumirea de origine - rubrică opțională. Pot fi înscrise certificări: 1. în cazul anumitor vinuri, cu privire la denumirea de origine protejată (DOP) sau la indicația geografică protejată (IGP) și la anul de recoltă sau la soiul de struguri de vinificație, în conformitate cu art. 24 și 31 din Regulamentul delegat (UE) nr. 273/2018; certificarea se redactează în următorii termeni: „Prin prezenta se certifică faptul că produsul descris a fost fabricat în conformitate cu regulile prevăzute în Regulamentul delegat (UE) nr. 273/2018. Dacă produsul este un produs DOP sau IGP, această frază este urmată de denumirea sau denumirile DOP sau IGP și de numărul sau numerele sale din registru, așa cum prevede la art. 119 alin. (1) lit. (b) din Regulamentul (UE) nr. 1.308/2013;
2. în cazul anumitor băuturi spirtoase, pentru care comercializarea este legată de categoria sau categoriile, indicația geografică (IG) și/sau perioada de maturare/vechimea băuturii spirtoase, în conformitate cu legislația Uniunii în materie de băuturi spirtoase [în speță, art. 10 și art. 13 alin. (6) cap. III și anexa I la Regulamentul (UE) 2019/787], certificarea se redactează în următorii termeni: „Se certifică prin prezenta că produsul descris este comercializat și etichetat în conformitate cu Regulamentul (UE) 2019/787.”
m)
Limbă denumire origine - subrubrică obligatorie dacă se completează subrubrica l). Se specifică limba utilizată în acest set de date.
n)
Dimensiunea producătorului - subrubrică opțională. Pentru băuturile alcoolice produse de micii producători independenți autocertificați, cantitatea anuală produsă în conformitate cu art. 5 alin. (3) din Regulamentul (UE) 2021/2.266, în cazul în care se dorește solicitarea unui nivel de accizare mai scăzut în statul membru de destinație. Valoarea acestui element trebuie să fie mai mare ca zero.
o)
Densitate - subrubrică obligatorie pentru produsele accizabile încadrate în categoria E200, E300, E410, E420, E430, E440, E450, E460, E480, E490, E700, E800, E910, E920 potrivit OMFP nr. 221/2016. Pentru aceste produse se înscrie densitatea la 15°C. Valoarea acestui element de date trebuie să fie mai mare ca zero.
p)
Descrierea comercială - subrubrică opțională. Se înscrie descrierea comercială a produselor în scopul identificării produselor transportate. Pentru transportul în vrac al vinurilor menționate la punctele 1-9, 15 și 16 din partea II a anexei VII la Regulamentul (UE) nr. 1.308/2013, descrierea produsului include informațiile opționale prevăzute la art. 120 din regulamentul respectiv, cu condiția ca acestea să fie indicate în etichetare sau să se aibă în vedere indicarea lor în etichetare. Pentru orice băutură spirtoasă, descrierea comercială trebuie să includă denumirea sa legală în conformitate cu art. 10 din Regulamentul (UE) 2019/787.
q)
Limbă descriere comercială - subrubrică obligatorie dacă se completează subrubrica p). Se specifică limba utilizată în acest set de date.
r)
Marca comercială a produselor - subrubrică obligatorie dacă produsele accizabile au o marcă comercială. Autoritatea vamală de expediere poate decide că nu este necesară specificarea mărcii comerciale a produselor transportate dacă aceasta este precizată pe factură sau pe alt document comercial menționat la subrubrica 9b).
s)
Limbă marca comercială a produselor - subrubrică obligatorie dacă se completează subrubrica r). Se specifică limba utilizată în acest set de date.
t)
Perioada de maturare sau vechimea produselor - subrubrică opțională. Pentru băuturile spirtoase, perioada de maturare sau vechimea trebuie să corespundă cu cea indicată în descrierea, prezentarea și eticheta acestora, astfel cum se menționează la art. 13 alin. (6) din Regulamentul (UE) 2019/787.
u)
Limbă perioada de maturare sau vechimea produselor - subrubrică obligatorie
v)
Declarația pentru micii producători independenți Pentru băuturile alcoolice produse de micii producători independenți certificați trebuie adăugată declarația privind tipul de băutură alcoolică autorizată în certificat în conformitate cu art. 2 din Regulamentul (UE) 2021/2.266, atunci când se dorește solicitarea unui nivel mai scăzut al accizei în statul membru de destinație.
Pentru băuturile alcoolice produse de micii producători independenți autocertificați trebuie adăugată declarația privind statutul producătorului în conformitate cu art. 4, art. 5 alin. (1) și art. 5 alin. (2) din Regulamentul (UE) 2021/2.266, atunci când se dorește solicitarea unui nivel mai scăzut al accizei în statul membru de destinație.
w)
Limbă declarația pentru micii producători independenți - subrubrică obligatorie dacă se completează subrubrica v). Se specifică limba utilizată în acest set de date.
17.1.
Ambalaj - rubrică obligatorie a)
Codul Tipului de ambalaje - subrubrică obligatorie. Se selectează unul dintre codurile prevăzute din anexa VI la Recomandarea nr. 21, adoptată de Centrul Organizației Națiunilor Unite pentru facilitarea comerțului și a tranzacțiilor electronice.
b)
Numărul de ambalaje - subrubrică obligatorie, dacă sunt numărabile. În cazul în care „Numărul de ambalaje” este 0, atunci trebuie să existe cel puțin un ambalaj cu aceleași „Mărci de expediție” și „Număr de ambalaje” cu o valoare mai mare ca 0.
c)
Identitatea sigiliului comercial - subrubrică obligatorie, dacă sunt utilizate sigilii comerciale. Se înscriu datele de identificare ale sigiliilor comerciale.
d)
Informații privind sigiliul - subrubrică opțională. Se înscriu orice informații suplimentare privind sigiliile comerciale (de exemplu, tipul de sigiliu utilizat).
e)
Limbă informații sigiliul - subrubrică obligatorie, dacă se completează subrubrica d). Se specifică limba utilizată în acest set de date.
f)
Mărci de expediție - subrubrică obligatorie, dacă numărul de ambalaje este zero și opțională în celelalte cazuri.
17.2.
Produse vitivinicole - rubrică obligatorie pentru produsele vitivinicole incluse în partea XII din anexa I la Regulamentul (UE) nr. 1.308/2013 a)
Categoria de produs vitivinicol - subrubrică obligatorie pentru produsele vitivinicole incluse în partea XII din anexa I la Regulamentul (UE) nr. 1.308/2013. Se selectează una dintre următoarele categorii: - 1 - Vin fără DOP/IGP;
- 2 - Vin din soiuri fără DOP/IGP;
- 3 - Vin cu DOP sau IGP;
- 4 - Vin importat;
- 5 - Altele.
b)
Codul zonei vitivinicole - subrubrică obligatorie pentru produsele vitivinicole în vrac (volum nominal de peste 60 de litri). Se înscrie zona vitivinicolă din care provine produsul transportat, în conformitate cu apendicele 1 la anexa VII la Regulamentul (UE) nr. 1.308/2013.
c)
Țara terță de origine - subrubrică obligatorie în cazul în care categoria de produse vitivinicole de la subrubrica a) este „Vin importat”. Se selectează codul de țară.
d)
Alte informații - subrubrică opțională;
e)
Limbă alte informații - subrubrică obligatorie dacă se completează subrubrica d). Se specifică limba utilizată în acest set de date.
17.2.1.
Codul operațiunii cu vinuri - rubrică obligatorie pentru produse vitivinicole în vrac (volum nominal de peste 60 de litri) -
Codul operațiunii cu vinuri - se înscrie unul sau mai multe coduri ale operațiunii cu vinuri, în conformitate cu lista de la pct. 2.1 lit. (e) subpct. (ii) din partea B a anexei V la Regulamentul delegat (UE) nr. 273/2018.
18.
Document certificat - rubrică opțională a)
Scurtă descriere a documentului - subrubrică obligatorie, cu excepția cazului în care se completează subrubrica c) sau e). Se înscrie o descriere a oricărui certificat legat de produsele transportate, de exemplu, certificate referitoare la denumirea de origine menționată la rubrica 17.I.
b)
Limbă scurtă descriere a documentului - subrubrică obligatorie dacă se completează subrubrica a). Se specifică limba utilizată în acest set de date.
c)
Referința documentului - subrubrică obligatorie, cu excepția cazului în care se completează subrubrica a) sau e). Se înscriu referințe pentru orice certificat referitor la produsele transportate.
d)
Limbă referința documentului - se specifică limba utilizată în acest set de date.
e)
Tipul documentului - subrubrică obligatorie, cu excepția cazului în care se completează subrubrica a) sau c). Se înscrie codul tipului documentului prezentat în lista de coduri 15 din anexa II la Regulamentul de punere în aplicare (UE) 2016/323 al Comisiei de stabilire a unor norme detaliate referitoare la cooperarea și schimbul de informații între statele membre în ceea ce privește mărfurile aflate în regim suspensiv de accize în conformitate cu Regulamentul (UE) nr. 389/2012 al Consiliului.
f)
Referința documentului - subrubrică obligatorie dacă este completată subrubrica e).
B.
Completarea opțiunii de anulare 1.
Din meniul principal se accesează „Mișcare” > „Rezultate mișcări identificate local” și se selectează o mișcare accesând ARC-ul acesteia.
2.
Se accesează butonul „Anulare”.
3.
a)
Se selectează motivul anulării: - 0 - Altul;
- 1 - Eroare de redactare;
- 2 - Tranzacție comercială întreruptă;
- 3 - E-DA duplicat;
- 4 - Deplasarea nu a început la data expedierii.
b)
Informații complementare - subrubrică obligatorie dacă motivul anulării este „altul”.
c)
Limbă referință document - se specifică limba utilizată în acest set de date.
4.
Pentru a transmite o anulare se accesează butonul „Transmitere”.
C.
Completarea opțiunii de schimbare a destinației 1.
Din meniul principal se accesează „Mișcare” > „Rezultate mișcări identificate local” și se selectează o mișcare accesând ARC-ul acesteia.
2.
Se accesează butonul „Schimbare destinație”.
3.
Pot fi actualizate date cuprinse în rubricile: „Durata călătoriei”, „Organizarea transportului”, „Numărul facturii”, „Data facturii”, „Codul modului de transport”, „Informații complementare”, „Limbă informații complementare”, „Codul tipului de destinație”, „Destinatar”, „Locul livrării”, „Birou vamal de export”, „Garanția deplasării”, „Garant”, „Organizatorul transportului”, „Transportator”, „Detalii privind transportul”.
4.
Dacă „Codul tipului de destinație” are valoarea: „Antrepozit fiscal”, „Destinatar înregistrat”, „Destinatar înregistrat ocazional”, „Livrare directă” sau „Utilizator final”, un buton „Validare” apare în apropierea câmpului „Identificarea comerciantului”, la secțiunea „Comerciant destinatar nou”. După completarea acestui câmp se selectează butonul „Validare”, astfel încât toate câmpurile din secțiunea „Nou Destinatar Comerciant” să fie validate și recuperate din baza de date locală. În secțiunea „Loc Livrare Comerciant”, o casetă combo se referă la câmpul „Identificare Comerciant”. Se selectează o valoare și câmpurile conexe vor fi completate în mod automat.
5.
Prin accesarea butonului „+ Comerciant destinatar nou” se poate adăuga o nouă secțiune pentru acest set de date. Nu poate exista decât un singur element „Comerciant destinatar nou” pentru fiecare schimbare de destinație. Elementele create „Comerciant destinatar nou” pot fi eliminate prin accesarea butonului „Ștergere opțiune”. Ștergerea se realizează printr-un mesaj de confirmare.
6.
Prin accesarea butonului „+ Locul comercial de livrare” se poate adăuga o secțiune pentru locul de livrare. Nu poate exista decât un singur element „Loc Livrare Comerciant”, pentru fiecare schimbare de destinație. Elementele create „Loc Livrare Comerciant” pot fi eliminate accesând butonul „Ștergere opțiune”. Ștergerea se realizează printr-un mesaj de confirmare.
7.
Dacă „Codul tipului de destinație” are valoarea: „Export”, butonul „Validare” lipsește și toate câmpurile vor fi completate de către utilizator.
8.
Dacă „Codul tipului de destinație” are valoarea: „Destinatar certificat” sau „Destinatar certificat ocazional”, codul de acciză se selectează automat, urmând a se accesa butonul „Validare”. În continuare se poate înregistra numai noul loc de livrare aparținând aceluiași destinatar certificat sau destinatar certificat ocazional, după caz.
9.
Dacă „Codul tipului de destinație” are valoarea: „Returnare la locul de expediție al expeditorului”, codul de acciză al expeditorului inițial, certificat sau certificat ocazional, se selectează automat, urmând a se accesa butonul „Validare”.
10.
Pentru a previzualiza proiectul de schimbare a destinației se accesează butonul „Vizualizare proiect”.
11.
Pentru a transmite proiectul revizuit se accesează butonul „Transmitere”. Se afișează un mesaj de confirmare a transmiterii cu succes a documentelor. Odată ce pagina este reinițiată, datele transmise trebuie să fie disponibile în mod needitabil.
12.
Accesând butonul „Vizualizare proiect schimbare destinație” sau „Vizualizare schimbare destinație remisă”, poate fi afișată o listă a datelor în format imprimabil prin accesarea butonului „Vizualizare la imprimare”.
13.
Dacă se dorește vizualizarea istoricului mișcării, operațiunea este posibilă dacă mișcarea este creată și cel puțin un document de schimbare de destinație a fost transmis cu succes. În tabul „Mișcări” se selectează ARC-ul aferent unei mișcări pentru care este generată o schimbare de destinație. Accesând butonul „Schimbare destinație” pot fi vizualizate datele. Se accesează butonul „Istoric”.
14.
Butonul „Schimbare destinație” este întotdeauna afișat expeditorului unei mișcări specifice. În cazul în care nu a fost remisă o schimbare de destinație, se afișează ecranul „Schimbare destinație nouă”. Dacă a fost remisă cel puțin o schimbare de destinație pentru mișcarea afișată, se afișează ecranul „Vizualizare Schimbare destinație”. În cel de-al doilea caz, datele din ultima schimbare de destinație remisă sunt disponibile pe ecran.
D.
Completarea opțiunii de divizare 1.
Din meniul principal se accesează „Mișcări” > „Rezultate mișcări identificate local” și se selectează o mișcare accesând ARC-ul acesteia.
2.
Se accesează butonul „Divizare”, apoi „e-DA Nou” pentru introducerea informațiilor despre noile e-DA-uri în legătură cu mișcarea respectivă.
3.
Pot fi actualizate date cuprinse în rubricile: „Codul statului membru (de divizare)”, „Număr de referință local”, „Durata călătoriei”, „Organizarea transportului”, „Codul tipului de destinație”, „Destinatar”, „Locul livrării”, „Birou vamal de export”, „Organizatorul transportului”, „Transportator”, „Detalii privind transportul”, „Corpul e-DA”, „Ambalaj”.
4.
Pentru a previzualiza proiectul de divizare a mișcării se accesează butonul „Vizualizare proiect”.
5.
Proiectele revizuite pot fi transmise prin accesarea butonului „Trimitere”.
E.
Completarea opțiunii de atenționare/respingere 1.
După inițierea unei mișcări, dar înaintea sosirii mărfurilor la destinație, primitorul are posibilitatea de a emite o atenționare sau de a respinge mișcarea.
2.
Din meniul principal, primitorul accesează „Mișcări” > „Rezultate mișcări identificate local” și selectează o mișcare accesând ARC-ul acesteia.
3.
Se accesează butonul „Atenționare/Respingere”.
4.
După accesarea butonului „Creează”, dacă primitorul nu bifează opțiunea „Indicator de respingere e-DA/e-DAS”, mesajul este considerat o atenționare. Dacă primitorul bifează opțiunea "Indicator de respingere e-DA/e-DAS", mesajul este considerat o respingere a produselor, iar după validare se așteaptă schimbarea de destinație de către primitor. În ambele situații este necesară completarea câmpului „Motiv Atenționare/Respingere”.
5.
Pentru a efectua operația se accesează butonul „Transmite”.
F.
Raport de primire/Raport de export 1.
Din meniul principal se accesează „Mișcări” > „Rezultate mișcări identificate local” și se selectează o mișcare accesând ARC-ul e-DA/e-DAS pentru care se dorește transmiterea raportului de primire.
2.
Se accesează butonul „Raport de primire”.
3.
Dacă un raport de primire a fost deja transmis, poate fi vizualizat în mod needitabil.
4.
În cazul în care niciun raport de primire nu a fost remis încă, pagina afișează două subfile: -
„Detalii raport de primire” - indică informații de bază privind mișcarea în format needitabil. Datele generale din e-DA/ e-DAS sunt completate automat. Secțiunea permite completarea datelor în raportul de primire și încheierea generală a primirii, prin completarea rubricilor: a)
Data primirii produselor - rubrică obligatorie. Se înscrie data primirii produselor.
b)
Concluzia generală a primirii - rubrică obligatorie. Se poate selecta, după caz: - 1 - Primire acceptată și satisfăcătoare;
- 2 - Primire acceptată, deși nesatisfăcătoare;
- 3 - Primire refuzată;
- 4 - Primire refuzată parțial;
- 21 - Ieșire acceptată și satisfăcătoare;
- 22 - Ieșire acceptată cu neconcordanțe minore detectate;
- 23 - Ieșire refuzată.
c)
Informații complementare - rubrică opțională. Se pot înscrie orice informații suplimentare referitoare la primirea produselor accizabile.
d)
Limbă informații complementare - rubrică obligatorie, dacă se completează rubrica „Informații complementare”. Se specifică limba utilizată în acest set de date.
-
„Listă articole Raport de primire/Raport de export” - secțiune obligatorie, dacă concluzia generală a primirii nu este „Primire acceptată și satisfăcătoare” sau „Ieșire acceptată și satisfăcătoare”. Rubrica 7: Corpul raportului de primire/export a)
Număr unic de referință al corpului de date - subrubrică obligatorie. Se înscrie numărul unic de referință al corpului de date al e-DA/e-DAS asociat (rubrica 17a din e-DA/e-DAS) privind același produs accizabil din e-DA/e-DAS asociat căruia i se aplică unul dintre codurile pentru care se completează lista.
b)
Indicator de lipsă sau excedent - subrubrică obligatorie, când se constată o lipsă sau un excedent în cazul corpului de date respectiv. Se poate selecta, după caz, „Lipsă” sau „Excedent”.
c)
Lipsa sau excedentul constatate - subrubrică obligatorie, dacă este specificat indicatorul din rubrica „Indicator de lipsă sau excedent”. Se înscrie cantitatea (exprimată în unitatea de măsură asociată codului produsului accizabil). Valoarea acestui element de date trebuie să fie mai mare ca zero.
d)
Codul produsului accizabil - subrubrică obligatorie completată automat cu datele existente.
e)
Cantitatea refuzată - subrubrică obligatorie, dacă pentru concluzia generală de primire codul este „Primire refuzată parțial”.
Rubrica 7.1: Motivul insatisfacției - rubrică obligatorie pentru fiecare articol căruia nu îi este aplicat codul concluziei generale de primire „Primire acceptată și satisfăcătoare” sau „Ieșire acceptată și satisfăcătoare”. a)
Motivul insatisfacției - subrubrică obligatorie. Se selectează unul dintre motivele: - 0 - Altul;
- 1 - Excedent;
- 2 - Lipsă;
- 3 - Produse deteriorate;
- 4 - Sigiliu rupt;
- 5 - Raportat de AES-RO;
- 7 - Cantitate mai mare decât cea din autorizația ocazională.
b)
Informații complementare - subrubrică obligatorie, dacă motivul insatisfacției este „Altul”. În cazul în care codul motivului insatisfacției este „Excedent”, „Lipsă”, Produse deteriorate”, „Sigiliu rupt”, „Raportat de AES-RO” sau „Cantitate mai mare decât cea menționată în autorizația ocazională”, subrubrica este opțională.
c)
Limbă informații complementare - rubrică obligatorie, dacă se completează rubrica „Informații complementare”. Se specifică limba utilizată în acest set de date.
G.
Completarea explicației privind lipsuri/excedent 1.
Din meniul principal, expeditorul sau primitorul accesează „Mișcări” > „Rezultate mișcări identificate local” și selectează o mișcare făcând clic pe ARC-ul acesteia.
2.
Se accesează butonul „Explicații Lipsă/Excedent”.
3.
După accesarea butonului „Creează” se introduc informații în legătură cu data analizei și se completează subrubrica „Explicația globală” cu orice alte informații suplimentare relevante pentru cazul respectiv.
4.
Pentru a transmite explicația se accesează butonul „Transmitere”.
H.
Completarea explicației privind întârzierea 1.
Din meniul principal, expeditorul accesează „Mișcări” > „Rezultate mișcări identificate local” și selectează o mișcare făcând clic pe ARC-ul acesteia.
2.
Se accesează butonul „Notificări/Explicații Întârzieri”, apoi „Creează explicație”.
3.
Expeditorul poate introduce explicații privind motivul întârzierii și informații complementare relevante pentru cazul respectiv. Explicațiile posibile sunt: a) accident;
b) altele;
c) condiții meteorologice nefavorabile;
d) grevă;
e) investigație în curs, efectuată de funcționari;
f) tranzacție comercială anulată;
g) tranzacție comercială în așteptare.
4.
Pentru a transmite explicația se accesează butonul „Transmitere”.
I.
Completarea opțiunii de transbordare 1.
Din meniul principal, expeditorul accesează „Mișcări” > „Rezultate mișcări identificate local” și selectează o mișcare făcând clic pe ARC-ul acesteia.
2.
Se accesează butonul „Transbordare”, apoi „Creează”.
3.
Se completează informații în legătură cu codul modului de transport, noul transportator și alte detalii privind transportul, după caz.
4.
Pentru a transmite mesajul se accesează butonul „Transmitere”.
