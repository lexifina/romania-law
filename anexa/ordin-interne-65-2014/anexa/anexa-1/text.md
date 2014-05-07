# Anexa 1
Anexa 1
la procedură FIȘA UTILIZATORULUI ....................................................................................................... (acest câmp se completează de către Direcția Regim Permise de Conducere și Înmatriculare a Vehiculelor) Unitatea ................................................................. Serviciul ................................................................ Gradul, numele și prenumele .............................................. Telefon serviciu (oraș/interior) ......................................... Telefon mobil (*) ........................................................ ------- (*) Câmpuri opționale. Aceste informații nu vor fi făcute publice și au ca scop doar înlesnirea comunicării între utilizator și personalul Direcției Regim Permise de Conducere și Înmatriculare a Vehiculelor, în probleme strict legate de aplicație. Din această cauză se recomandă completarea lor. Adresa e-mail serviciu ................................................... Adresa e-mail personală (*) .............................................. ------- (*) Câmpuri opționale. Aceste informații nu vor fi făcute publice și au ca scop doar înlesnirea comunicării între utilizator și personalul Direcției Regim Permise de Conducere și Înmatriculare a Vehiculelor, în probleme strict legate de aplicație. Din această cauză se recomandă completarea lor.
Data .................
Semnătura ...............
Anexa 2
la procedură ANGAJAMENT Subsemnatul, ............................................................. Sunt de acord cu următoarele cerințe de securitate și de operare: - voi efectua căutări individuale, potrivit Legii nr. 5/2014 privind unele măsuri pentru facilitarea schimbului transfrontalier de informații referitoare la încălcările normelor de circulație care afectează siguranța rutieră și pentru facilitarea executării sancțiunilor aplicate acestor încălcări, doar în interes de serviciu și cu respectarea legislației privind prelucrarea datelor cu caracter personal și libera circulație a acestora; - pentru fiecare căutare voi scrie în clar numărul de înregistrare al dosarului sau al lucrării penale; - nu voi divulga nimănui numele și parola contului meu și nici nu voi permite efectuarea de interogări în lipsa mea, prin folosirea contului meu; - în cazul în care voi pleca din fața calculatorului, îl voi închide (dacă e cazul) sau voi bloca accesul la acesta prin folosirea opțiunii "Blocare computer", disponibilă după apăsarea simultană a tastelor "Ctrl", "Alt" și "Del" sau prin alte metode cel puțin la fel de sigure ca precedenta (exemplu, un "Screen Saver" cu parolă, parola fiind cunoscută doar de mine); - sunt de acord cu faptul că orice căutare efectuată cu numele meu de utilizator și parola mea, logate ca atare, îmi aparțin; - am luat la cunoștință și voi respecta prevederile Procedurii .............; - orice modificare referitoare la informațiile proprii din fișa utilizatorului le voi comunica de îndată ............ și personalului Direcției Regim Permise de Conducere și Înmatriculare a Vehiculelor.
Data ..............
Semnătura ..............
Anexa 3
la procedură FORMATUL DE INTEROGARE a datelor de către personalul poliției rutiere din cadrul Poliției Române și al Poliției de Frontieră Române
*Font 9*
Elementul interogării
O/F
Tip/Număr
de
caractere
Descriere/Observații
Date privind vehiculul
O
AN 1-50
Se completează automat de către aplicația
informatică.
Statul membru de
înmatriculare
O
Enum
Selectabil dintr-o listă, care conține codul de
stat și denumirea în clar
Identificator unic al
căutării
O
AN 1-36
Editabil sau generat de sistem prin bifarea în
ecran a căsuței "Generare identificator căutare"
Numărul de înmatriculare
O
AN 1-15
Cod (A), potrivit abrevierii prevăzute de
Directiva 1999/37/CEa Consiliului din 29 aprilie
1999 privind documentele de înmatriculare pentru
vehicule
Numărul de înmatriculare,
partea a doua
F
AN 1-15
Aplicabil doar când statul selectat este Germania,
caz în care completarea este obligatorie
Date privind încălcarea
O
AN 1-50
Se completează automat de către aplicația
informatică.
Statul membru în care s-a
săvârșit încălcarea
O
Enum
Se completează automat de către aplicația
informatică.
Data de referință a
încălcării
O
Dată
Format "AAAA-LL-ZZ" sau dată cu denominarea
fusului orar, de exemplu, UTC "CCYY-MM-DDZ", sau
data locală la care se adaugă diferența orară față
de UTC: "CCYY-MM-DD±nn.nn"
Ora de referință a
încălcării
O
Timp
Format UTC "hh:mm:ssZ" sau "hh:mm:ss±00.00"
Scopul căutării
O
Enum
Codul încălcării selectabil dintr-o listă, în
funcție de tipul acesteia
Valorile permise sunt:
1 = exces de viteză;
2 = conducerea sub influența alcoolului;
3 = nefolosirea centurii de siguranță;
4 = nerespectarea semnificației culorii roșii a
semaforului;
5 = utilizarea unei benzi interzise;
10 = conducerea sub influența stupefiantelor;
11 = nefolosirea căștii de protecție;
12 = utilizarea ilegală a unui telefon mobil sau a
altui dispozitiv de comunicare în timpul
conducerii.
Denumirea autorității
competente
O
AN 1-50
Se completează automat în funcție de setările
utilizatorului. În caz contrar se introduce din
tastatură.
Abrevieri: O = obligatoriu, în cazul în care informația este disponibilă în sistemul de evidență aparținând statului membru, altul decât România; F = facultativ; AN = alfanumeric; Enum = listă de valori selectabile.
Anexa 4
la procedură SETUL MAXIM DE DATE ce poate fi obținut de poliția rutieră din cadrul Poliției Române și de Poliția de Frontieră Română în urma căutării automatizate în sistemele de evidență aparținând statelor membre, altele decât România
Cod corespunzător, potrivit abrevierilor prevăzute în Directiva 1999/37/CE a Consiliului din 29 aprilie 1999 privind documentele de înmatriculare pentru vehicule Denumire O/F Tip Observații
0 1 2 3 4
Partea I. Date privind vehiculele
Cod de stat O Enum
Numele statului de înmatriculare O AN
Rezultat căutare O Enum "Găsit", "Nu a fost găsit" sau "Eroare"
Număr rezultate O Int Afișat doar dacă rezultatul căutării este "Găsit"
Identificator unic O Text
Data de referință O DT
(E) Numărul de șasiu/Numărul de identificare al vehiculului O AN
(A) Numărul de înmatriculare O AN
(D.1) Marca O AN
(D.3) Modelul vehiculului O AN
(J) Codul categoriei UE a vehiculului O Enum
Limba în care este redactat certificatul de înmatriculare F Enum
Partea a II-a. Date privind deținătorii sau proprietarii vehiculelor
(C.1) Date privind deținătorul vehiculului
Informațiile se referă la deținătorul certificatului de înmatriculare
Data de referință a încălcării F DT Afișată cu marcaj distinct dacă este diferită de data de referință introdusă la căutare
Tipologia entității juridice F Enum
(C1.1) Numele de familie al deținătorului certificatului de înmatriculare/denumirea societății O AN Se obține în format imprimabil.
(C.1.2) Prenumele O AN Se obține în format imprimabil.
(C.1.2) Inițiala/inițialele, acolo unde este cazul O AN Se obține în format imprimabil.
(C1.2) Prenumele sau inițiala (inițialele) (acolo unde este cazul) F AN
Sexul F Enum Masculin, feminin
Data nașterii O Date
Entitate juridică O
Persoană fizică, asociație, întreprindere, societate etc.
Locul nașterii F AN
Număr de identificare F AN/Enum Se obține un element de identificare care identifică doar persoana sau societatea respectivă.
Cod unic de înregistrare societate F AN
Adresa
(C.1.3) Strada O AN Se obține în format imprimabil.
(C.1.3) Câmp suplimentar pentru stradă O AN Se obține în format imprimabil.
(C.1.3) Număr și anexe O Int/AN Se obține în format imprimabil.
(C.1.3) Cod poștal O AN Se obține în format imprimabil.
(C.1.3) Locul de reședință/rezidență O AN Se obține în format imprimabil.
(C.1.3) Statul membru O Enum Se obține în format imprimabil.
Nume tipăribil F AN Concatenat
Adresa tipăribilă F AN Concatenată
(C.2) Date privind proprietarul vehiculului
Informațiile se referă la proprietarul vehiculului.
Data de referință F DT Afișată cu marcaj distinct dacă este diferită de data de referință introdusă la căutare
Tipologia entității juridice F Enum
(C.2.1) Numele de familie al proprietarului sau denumirea societății O AN
(C.2.2) Prenumele O AN
(C.2.2) Inițiala/Inițialele, acolo unde este cazul O AN
(C.2.2) Prenumele sau inițiala (inițialele) (acolo unde este cazul) F AN
Sexul F Enum Masculin, feminin
Data nașterii O Date
Entitate juridică O
Persoană fizică, asociație, întreprindere, societate etc.
Locul nașterii F AN
Număr de identificare F AN/Enum Se obține un element de identificare care identifică doar persoana sau societatea respectivă.
(C2.1) Cod unic de înregistrare firmă F AN
Adresa
(C.2.3) Strada O AN
(C.2.3) Câmp suplimentar pentru stradă O AN
(C.2.3) Număr și anexe O Int/AN
(C.2.3) Cod poștal O AN
(C.2.3) Locul de reședință/rezidență O AN
(C.2.3) Stat membru O Enum
(C.2.3) Nume tipăribil F AN
Adresa tipăribilă F AN
Mesaje privind calitatea unor date F
Mesaje generale O AN
Abrevieri: O = obligatoriu, în cazul în care informația este disponibilă în sistemul de evidență aparținând statului membru, altul decât România; F = facultativ; AN = alfanumeric; N = numeric; Date = date; DT = dată și timp; Enum = listă de valori selectabile.
Anexa 5
la procedură DATELE furnizate de Direcția Regim Permise de Conducere și Înmatriculare a Vehiculelor din Registrul național de evidență a permiselor de conducere și a vehiculelor înmatriculate punctelor naționale de contact ale statelor membre Partea I. Date privind vehiculele
Intrare
Cod corespunzător,
potrivit abrevierilor
prevăzute în Directiva
1999/37/CEa Consiliului
din 29 aprilie 1999
privind documentele de
înmatriculare pentru
vehicule
Observații
Numărul de înmatriculare
Statul de înmatriculare
Numărul de șasiu/Numărul de
identificare al vehiculului
Marca
(D.1)
Modelul vehiculului
(D.3)
Codul categoriei UE a vehiculului
(J)
Partea a II-a. Date privind deținătorii sau proprietarii vehiculelor
*Font 7*
Intrare
Cod
corespunzător,
potrivit
abrevierilor
prevăzute în
Directiva
1999/37/CEa
Consiliului
din 29 aprilie
1999 privind
documentele de
înmatriculare
pentru vehicule
Observații
Date privind deținătorul vehiculului
(C.1)
Datele se referă la deținătorul certificatului de înmatriculare.
Numele de familie al deținătorului
certificatului de înmatriculare/Denumirea
societății
(C.1.1)
Se folosesc câmpuri separate pentru nume, infixe, titluri etc.
Se comunică în format imprimabil.
Prenume
(C.1.2)
Se folosesc câmpuri separate pentru prenume și inițiale. Se
comunică în format imprimabil.
Adresă
(C.1.3)
Se folosesc câmpuri separate pentru stradă, număr și anexe, cod
poștal, locul de reședință, statul de reședință etc. și se
comunică adresa în format imprimabil.
Entitate juridică
Persoană fizică, asociație, întreprindere, societate etc.
Date privind proprietarul vehiculului
(C.2)
Datele se referă la proprietarul vehiculului.
Numele proprietarului (denumirea
societății)
(C.2.1)
Prenume
(C.2.2)
Adresă
(C.2.3)
Entitate juridică
Persoană fizică, asociație, întreprindere, societate etc.
-------
