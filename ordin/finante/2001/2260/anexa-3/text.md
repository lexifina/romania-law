# Anexa 4
CONDIȚII pentru transmiterea fișelor fiscale pe cale electronică 1. Condiții generale Fișele fiscale în format electronic se depun la aceleași termene ca și formularele de fise fiscale tipărite (FF1 și FF2) la unitatea fiscală în a carei raza teritorială își are sediul angajatorul. Fișele fiscale în format electronic vor fi transmise pe dischete 3 1/2 inch, 1.440 MB, compatibile MS-DOS. Dischetele vor fi însoțite de un borderou privind conținutul acestora și de fișele fiscale listate pe hârtie, pentru funcția de baza (FF1), pentru angajații cărora nu li s-au efectuat operațiunile de regularizare, precum și de fișele fiscale 2 (FF2). De asemenea, angajatorii vor lista pe hârtie, la sfârșitul anului sau la încetarea activității angajaților, fișele fiscale ce vor fi înmânate acestora. 2. Condiții tehnice standard pentru formatul electronic al fisei fiscale Informațiile din fișele fiscale (FF1 și FF2) pot fi transmise fie:
a) în fisiere format text ASCII, în care fiecare înregistrare (linie) se termina cu "carriage return" și "linefeed". Nu se admit în cadrul înregistrărilor (liniilor) diacritice (caractere românești) și caractere de control, cu excepția celor menționate anterior. Separatorul dintre câmpuri va fi virgula, iar delimitatorul campurilor de tip caracter (alfanumeric) va fi #;
b) în fisiere format DBF - DataBaseFile (dbase, Fox, Visual Fox etc.).
Ordinea campurilor din structura fisierelor este obligatorie, indiferent dacă acestea se completează sau nu. În descrierea de mai jos "Tip camp" are următoarea semnificație: N = numeric; C = caracter (alfanumeric); D = data. Fișierele (text sau DBF) vor avea în mod obligatoriu următoarele denumiri și vor conține:
REP_aaaa TXT sau
REP_aaaa DBF
date de identificare angajator
FF1_aaaa TXT sau
FF1_aaaa DBF
(funcția de baza)
date de identificare angajați, total coeficienți de deduce-
re, coeficienți de deducere pentru situația proprie a
angajatului, venit net, impozit reținut, impozit pe venitu-
rile din salarii cu impunere finala, venit scutit, infor-
matii privind operațiunile de regularizare efectuate
DEB_aaaa TXT sau
DEB_aaaa DBF
date de identificare persoana în întreținere, coeficienți
de deducere suplimentară sau pentru persoanele aflate în
întreținerea angajaților
FF2_aaaa TXT sau
FF2_aaaa DBF
date de identificare angajați, tip venit, venit baza de
calcul, impozit reținut
Unde "aaaa" reprezintă anul fiscal de referința (de ex. REP_2002.TXT,
REP_2002.DBF, FF1_2002.TXT, FF1_2002.DBF, DED_2002.TXT, DED_2002.DBF,
FF2_2002.TXT, FF2_2002.DBF,
REP_aaaa.TXT, REP_aaaa.DBF va conține o singura înregistrare (linie) cu datele de identificare ale angajatorului în următoarea structura:
Denumire
camp
Descriere
camp
Tip
camp
Lungimea
maxima
Explicații
Cod_ang
Cod angajator
N
13
- se completează codul de
înregistrare fiscală sau codul
unic de înregistrare al anga-
jatorului, dacă angajatorul
este persoana juridică
- se completează codul
numeric personal sau numărul
de înregistrare fiscală al
angajatorului, dacă angajato-
rul este persoana fizica
Tip_ang
Tip angajator
N
1
- se completează cu 1, dacă
angajatorul este persoana
juridică
- se completează cu 2, dacă
angajatorul este persoana
fizica
Denumire
Denumire
C
160
- se completează denumirea
angajatorului persoana
juridică
Nume
Nume
C
40
- se completează numele
angajatorului persoana fizica
Prenume
Prenume
C
40
- se completează prenumele
angajatorului persoana fizica
Localitate
Localitate
C
50
Județ
Județ
C
20
Strada
Strada
C
50
Nr
Număr
C
10
Cod_poștal
Cod poștal
N
6
Bloc
Bloc
C
10
Scara
Scara
C
10
Etaj
Etaj
C
10
Ap
Ap
C
10
Sector
Sector
N
1
Telefon
Telefon
C
10
Email
E-mail
C
50
FF1_aaaa.TXT, FF1_aaaa.DBF va conține câte o înregistrare (linie) pentru fiecare angajat care a obținut venituri din salarii la funcția de baza, în următoarea structura:
Denumire
camp
Descriere
camp
Tip
camp
Lungimea
maxima
Explicații
Cnd_ang
Cod angajat
N
13
- se completează codul
numeric personal sau numărul
de identificare fiscală al
angajatului
Nume
Nume
C
40
Prenume
Prenume
C
40
Localitate
Localitate
C
50
Județ
Județ
C
20
Strada
Strada
C
50
Nr
Număr
C
10
Cod_poștal
Cod poștal
N
6
Bloc
Bloc
C
10
Scara
Scara
C
10
Etaj
Etaj
C
10
Ap
Ap
C
10
Sector
Sector
N
1
Rectific
Fișa fiscală
rectificativa
C
1
- se completează cu X,
dacă este fișa fiscală
rectificativa
Regulariz
Fișa fiscală
regularizata
C
1
- se completează cu X,
dacă s-a efectuat regulariza-
rea impozitului
Fără_dom
Persoane fizice
române fără domici-
liu în România
C
1
- se completează cu X,
pentru angajații persoane
fizice române fără domiciliu
în România
Alte_surse
Alte surse supuse
impozitului pe veni-
tul anual global
C
1
- se completează cu X,
dacă angajatul are alte surse
supuse impozitului pe venitul
anual global
Invalid_I
Invalid gr. I,
handicap grav
C
1
- se completează cu X, în
funcție de situația
angajatului
Invalid_II
Invalid gr. II,
handicap accentuat
C
1
- se completează cu X, în
funcție de situația
angajatului
Alte_sit.
Alte situații de
invaliditate
C
1
- se completează cu X, în
funcție de situația
angajatului
Data_angaj
Data angajării
D
10
- se completează, dacă
angajarea a avut loc în timpul
anului fiscal de referința,
în formatul ZZ/LL/AAAA
Data_incet
Data încetării
activității
D
10
- se completează, dacă
încetarea activității a avut
loc în timpul anului fiscal
de referința, în formatul
ZZ/LL/AAAA
Coef_T_01
Total coeficient de
deducere pentru
luna Ianuarie
N
4.2
- se completează în
formatul 9.99
Coef_T_02
Total coeficient de
deducere pentru
luna Februarie
N
4.2
- se completează în
formatul 9.99
Coef_T_03
Total coeficient de
deducere pentru
luna Martie
N
4.2
- se completează în
formatul 9.99
Coef_T_04
Total coeficient de
deducere pentru
luna Aprilie
N
4.2
- se completează în
formatul 9.99
Coef_T_05
Total coeficient de
deducere pentru
luna Mai
N
4.2
- se completează în
formatul 9.99
Coef_T_06
Total coeficient de
deducere pentru
luna Iunie
N
4.2
- se completează în
formatul 9.99
Coef_T_07
Total coeficient de
deducere pentru
luna Iulie
N
4.2
- se completează în
formatul 9.99
Coef_T_08
Total coeficient de
deducere pentru
luna August
N
4.2
- se completează în
formatul 9.99
Coef_T_09
Total coeficient de
deducere pentru
luna Septembrie
N
4.2
- se completează în
formatul 9.99
Coef_T_10
Total coeficient de
deducere pentru
luna Octombrie
N
4.2
- se completează în
formatul 9.99
Coef_T_11
Total coeficient de
deducere pentru
luna Noiembrie
N
4.2
- se completează în
formatul 9.99
Coef_T_12
Total coeficient de
deducere pentru
luna Decembrie
N
4.2
- se completează în
formatul 9.99
Coef_P_01
Coeficient de dedu-
cere personală
pentru luna
Ianuarie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_02
Coeficient de dedu-
cere personală
pentru luna
Februarie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_03
Coeficient de dedu-
cere personală
pentru luna
Martie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_04
Coeficient de dedu-
cere personală
pentru luna
Aprilie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_05
Coeficient de dedu-
cere personală
pentru luna
Mai
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_06
Coeficient de dedu-
cere personală
pentru luna
Iunie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_07
Coeficient de dedu-
cere personală
pentru luna
Iulie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_08
Coeficient de dedu-
cere personală
pentru luna
August
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_09
Coeficient de dedu-
cere personală
pentru luna
Septembrie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_10
Coeficient de dedu-
cere personală
pentru luna
Octombrie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_11
Coeficient de dedu-
cere personală
pentru luna
Noiembrie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Coef_P_12
Coeficient de dedu-
cere personală
pentru luna
Decembrie
N
4.2
- se completează în funcție de
dreptul de deducere și de
situația angajatului, în
formatul 9.99
Venit_01
Venit net pentru
luna Ianuarie
N
12
- se completează conform
statului de salarii
Impozit_01
Impozit reținut
pentru luna
Ianuarie
N
12
- se completează conform
statului de salarii
Venit_02
Venit net pentru
luna Februarie
N
12
- se completează conform
statului de salarii
Impozit_02
Impozit reținut
pentru luna
Februarie
N
12
- se completează conform
statului de salarii
Venit_03
Venit net pentru
luna Martie
N
12
- se completează conform
statului de salarii
Impozit_03
Impozit reținut
pentru luna
Martie
N
12
- se completează conform
statului de salarii
Venit_04
Venit net pentru
luna Aprilie
N
12
- se completează conform
statului de salarii
Impozit_04
Impozit reținut
pentru luna
Aprilie
N
12
- se completează conform
statului de salarii
Venit_05
Venit net pentru
luna Mai
N
12
- se completează conform
statului de salarii
Impozit_05
Impozit reținut
pentru luna
Mai
N
12
- se completează conform
statului de salarii
Venit_06
Venit net pentru
luna Iunie
N
12
- se completează conform
statului de salarii
Impozit_06
Impozit reținut
pentru luna
Iunie
N
12
- se completează conform
statului de salarii
Venit_07
Venit net pentru
luna Iulie
N
12
- se completează conform
statului de salarii
Impozit_07
Impozit reținut
pentru luna
Iulie
N
12
- se completează conform
statului de salarii
Venit_08
Venit net pentru
luna August
N
12
- se completează conform
statului de salarii
Impozit_08
Impozit reținut
pentru luna
August
N
12
- se completează conform
statului de salarii
Venit_09
Venit net pentru
luna Septembrie
N
12
- se completează conform
statului de salarii
Impozit_09
Impozit reținut
pentru luna
Septembrie
N
12
- se completează conform
statului de salarii
Venit_10
Venit net pentru
luna Octombrie
N
12
- se completează conform
statului de salarii
Impozit_10
Impozit reținut
pentru luna
Octombrie
N
12
- se completează conform
statului de salarii
Venit_11
Venit net pentru
luna Noiembrie
N
12
- se completează conform
statului de salarii
Impozit_11
Impozit reținut
pentru luna
Noiembrie
N
12
- se completează conform
statului de salarii
Venit_12
Venit net pentru
luna Decembrie
N
12
- se completează conform
statului de salarii
Impozit_12
Impozit reținut
pentru luna
Decembrie
N
12
- se completează conform
statului de salarii
Venit_13
Prima de vacanta
N
12
Impozit_13
Impozit aferent
primei de vacanta
N
12
Venit_14
Total venit net
N
12
Impozit_14
Total impozit
reținut
N
12
Nr_luni
Număr luni pentru
care s-au acordat
cheltuieli profe-
sionale
N
12
Ch_ acord
Cheltuieli
profesionale
acordate
N
12
Ch_ cuven
Cheltuieli
profesionale
cuvenite
N
12
Venit_rec
Venit net
recalculat
N
12
Deduceri
Deduceri
personale
cuvenite
N
12
- se completează numai pentru
angajații cărora li s-au
efectuat operațiunile de
regularizare
Venit_baza
Venit anual baza
de calcul
N
12
- se completează numai pentru
angajații cărora li s-au
efectuat operațiunile de
regularizare
Imp_anual
Impozit anual
N
12
- se completează numai pentru
angajații cărora li s-au
efectuat operațiunile de
regularizare
Dif_plata
Diferența impozit
rămas de achitat
de către angajat
N
12
- se completează numai pentru
angajații cărora li s-au
efectuat operațiunile de
regularizare
Dif_restit
Diferența impozit
de restituit
angajatului
N
12
- se completează numai pentru
angajații cărora li s-au
efectuat operațiunile de
regularizare
Venit_fin
Venit din salarii
cu impunere finala
N
12
- se completează numai pentru
veniturile din salarii stabi-
lite prin hotărâri
judecătorești
Imp_fin
Impozit pe venitul
din salarii cu
impunere finala
N
12
- se completează numai pentru
veniturile din salarii stabi-
lite prin hotărâri
judecătorești
Venit_scut
Venit net scutit
de impozit pe venit
N
12
- se completează numai pentru
veniturile scutite de impozit
pe venit
DED_aaaa.TXT sau DED_aaaa.DBF va conține câte o înregistrare (linie) pentru fiecare persoana aflată în întreținere a unui angajat
Denumire
camp
Descriere
camp
Tip
camp
Lungimea
maxima
Explicații
Cnp_ang
Cod angajat
N
13
- se completează codul numeric
personal sau numărul de iden-
tificare fiscală al
angajatului
Cnp_pers
Cod persoana în
întreținere
N
13
- se completează codul numeric
personal sau numărul de iden-
tificare fiscală al persoanei
în întreținere
Nume
Nume
C
40
Prenume
Prenume
C
40
Soț
Soț/sotie
C
1
- se completează cu X, în
funcție de calitatea persoa-
nei aflate în întreținere
Copil
Copil
C
1
- se completează cu X, în
funcție de calitatea persoa-
nei aflate în întreținere
Alta
Alta
C
1
- se completează cu X, în
funcție de calitatea persoa-
nei aflate în întreținere
Invalid_I
Invalid gr. I,
handicap grav
C
1
- se completează cu X, în
funcție de situația persoanei
aflate în întreținere
Invalid_II
Invalid gr. II,
handicap accentuat
C
1
- se completează cu X, în
funcție de situația persoanei
aflate în întreținere
Alte_sit
Alte situații de
invaliditate
C
1
- se completează cu X, în
funcție de situația persoanei
aflate în întreținere
Coef_01
Coeficient de dedu-
cere pentru luna
Ianuarie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_02
Coeficient de dedu-
cere pentru luna
Februarie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_03
Coeficient de dedu-
cere pentru luna
Martie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_04
Coeficient de dedu-
cere pentru luna
Aprilie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_05
Coeficient de dedu-
cere pentru luna
Mai
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_06
Coeficient de dedu-
cere pentru luna
Iunie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_07
Coeficient de dedu-
cere pentru luna
Iulie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_08
Coeficient de dedu-
cere pentru luna
August
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_09
Coeficient de dedu-
cere pentru luna
Septembrie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_10
Coeficient de dedu-
cere pentru luna
Octombrie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_11
Coeficient de dedu-
cere pentru luna
Noiembrie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
Coef_12
Coeficient de dedu-
cere pentru luna
Decembrie
N
4.2
- se completează în funcție
de calitatea și situația per-
soanei aflate în întreținere,
în formatul 9.99
FF2_aaaa.TXT, FF2_aaaa.DBF va conține câte o înregistrare (linie) pentru fiecare angajat care obține venituri din salarii, altele decât cele de la funcția de baza, în următoarea structura:
Denumire
camp
Descriere
camp
Tip
camp
Lungimea
maxima
Explicații
Cnd_ang
Cod angajat
N
13
- se completează codul
numeric personal sau numărul
de identificare fiscală al
angajatului
Nume
Nume
C
40
Prenume
Prenume
C
40
Localitate
Localitate
C
50
Județ
Județ
C
20
Strada
Strada
C
50
Nr
Număr
C
10
Cod_poștal
Cod poștal
N
6
Bloc
Bloc
C
10
Scara
Scara
C
10
Etaj
Etaj
C
10
Ap
Ap
C
10
Sector
Sector
N
1
Rectific
Fișa fiscală
rectificativa
C
1
- se completează cu X,
dacă este fișa fiscală
rectificativa
AS1
AS1
C
1
- se completează cu X, în
funcție de tipul venitului
AS2
AS2
C
1
- se completează cu X, în
funcție de tipul venitului
AS3
AS3
C
1
- se completează cu X, în
funcție de tipul venitului
AS4
AS4
C
1
- se completează cu X, în
funcție de tipul venitului
AS5
AS5
C
1
- se completează cu X, în
funcție de tipul venitului
AS6
AS6
C
1
- se completează cu X, în
funcție de tipul venitului
AS7
AS7
C
1
- se completează cu X, în
funcție de tipul venitului
AS8
AS8
C
1
- se completează cu X, în
funcție de tipul venitului
Venit_01
Venit baza de calcul
pentru luna
Ianuarie
N
12
- se completează conform
statului de salarii
Impozit_01
Impozit reținut
pentru luna
Ianuarie
N
12
- se completează conform
statului de salarii
Venit_02
Venit baza de calcul
pentru luna
Februarie
N
12
- se completează conform
statului de salarii
Impozit_02
Impozit reținut
pentru luna
Februarie
N
12
- se completează conform
statului de salarii
Venit_03
Venit baza de calcul
pentru luna
Martie
N
12
- se completează conform
statului de salarii
Impozit_03
Impozit reținut
pentru luna
Martie
N
12
- se completează conform
statului de salarii
Venit_04
Venit baza de calcul
pentru luna
Aprilie
N
12
- se completează conform
statului de salarii
Impozit_04
Impozit reținut
pentru luna
Aprilie
N
12
- se completează conform
statului de salarii
Venit_05
Venit baza de calcul
pentru luna
Mai
N
12
- se completează conform
statului de salarii
Impozit_05
Impozit reținut
pentru luna
Mai
N
12
- se completează conform
statului de salarii
Venit_06
Venit baza de calcul
pentru luna
Iunie
N
12
- se completează conform
statului de salarii
Impozit_06
Impozit reținut
pentru luna
Iunie
N
12
- se completează conform
statului de salarii
Venit_07
Venit baza de calcul
pentru luna
Iulie
N
12
- se completează conform
statului de salarii
Impozit_07
Impozit reținut
pentru luna
Iulie
N
12
- se completează conform
statului de salarii
Venit_08
Venit baza de calcul
pentru luna
August
N
12
- se completează conform
statului de salarii
Impozit_08
Impozit reținut
pentru luna
August
N
12
- se completează conform
statului de salarii
Venit_09
Venit baza de calcul
pentru luna
Septembrie
N
12
- se completează conform
statului de salarii
Impozit_09
Impozit reținut
pentru luna
Septembrie
N
12
- se completează conform
statului de salarii
Venit_10
Venit baza de calcul
pentru luna
Octombrie
N
12
- se completează conform
statului de salarii
Impozit_10
Impozit reținut
pentru luna
Octombrie
N
12
- se completează conform
statului de salarii
Venit_11
Venit baza de calcul
pentru luna
Noiembrie
N
12
- se completează conform
statului de salarii
Impozit_11
Impozit reținut
pentru luna
Noiembrie
N
12
- se completează conform
statului de salarii
Venit_12
Venit baza de calcul
pentru luna
Decembrie
N
12
- se completează conform
statului de salarii
Impozit_12
Impozit reținut
pentru luna
Decembrie
N
12
- se completează conform
statului de salarii
Venit_13
Total venit baza
de calcul
N
12
Impozit_13
Total impozit
reținut
N
12
Modelele fișelor fiscale pe care angajatorii le vor lista, atât pentru unitatea fiscală cat și pentru angajați, precum și modelul borderoului de însoțire a dischetei trebuie să respecte următoarea structura:
FIȘA FISCALĂ 1 (pentru venituri din salarii la funcția de bază) pentru anul: 9999.................................................................................
Fișa fiscală rectificativă Nu/Da
Fișa fiscală regularizată Nu/Da ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ I Date de identificare angajator ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ Cod angajator 9999999999999 Denumire/Nume xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Prenume xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Adresa xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Telefon xxxxxxxxx E-mail xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ II Date de identificare angajat ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ Cod angajat 9999999999999 Nume xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Prenume xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Domiciliu xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx Persoană fizică română fără domiciliu în România Nu/Da ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ III Date privind îndeplinirea condițiilor ptr. calculul impozitului anual și regularizarea acestuia ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
Alte surse supuse impozitului pe venitul anual global Nu/Da
ZZ/LL/AAAA Data angajării ZZ/LL/AAAA Data încetării activității ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ IV Deduceri personale ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ A. Total coeficient
Ian Feb Mar Apr Mai Iun Iul Aug Sept Oct Nov Dec deducere 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ B. Situația proprie pentru deducere
Invalid I/Invalid Ian Feb Mar Apr Mai Iun Iul Aug Sept Oct Nov Dec
II/Alte situații 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ C. Date referitoare la persoanele aflate în întreținere
Cod 9999999999999 Nume, prenume xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Calitatea soț(soție)/copil/alta Invalid I/Invalid II/Alte situații
Coeficienți
Ian Feb Mar Apr Mai Iun Iul Aug Sept Oct Nov Dec de deducere 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 9.99 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
V. Calculul impozitului pe veniturile din salarii
Luna
Venit net
Impozit calculat și
reținut
Ianuarie
1
999.999.999.999
999.999.999.999
Februarie
2
999.999.999.999
999.999.999.999
Martie
3
999.999.999.999
999.999.999.999
Aprilie
4
999.999.999.999
999.999.999.999
Mai
5
999.999.999.999
999.999.999.999
Iunie
6
999.999.999.999
999.999.999.999
Iulie
7
999.999.999.999
999.999.999.999
August
8
999.999.999.999
999.999.999.999
Septembrie
9
999.999.999.999
999.999.999.999
Octombrie
10
999.999.999.999
999.999.999.999
Noiembrie
11
999.999.999.999
999.999.999.999
Decembrie
12
999.999.999.999
999.999.999.999
Prima de vacanta
13
999.999.999.999
999.999.999.999
Total
14
999.999.999.999
999.999.999.999
Tip venit: AS1/AS2/AS3/AS4/AS5/AS6/AS7/AS8
Luna
Venit baza de calcul
Impozit calculat și
reținut
Ianuarie
1
999.999.999.999
999.999.999.999
Februarie
2
999.999.999.999
999.999.999.999
Martie
3
999.999.999.999
999.999.999.999
Aprilie
4
999.999.999.999
999.999.999.999
Mai
5
999.999.999.999
999.999.999.999
Iunie
6
999.999.999.999
999.999.999.999
Iulie
7
999.999.999.999
999.999.999.999
August
8
999.999.999.999
999.999.999.999
Septembrie
9
999.999.999.999
999.999.999.999
Octombrie
10
999.999.999.999
999.999.999.999
Noiembrie
11
999.999.999.999
999.999.999.999
Decembrie
12
999.999.999.999
999.999.999.999
Total
13
999.999.999.999
999.999.999.999
Borderou de însoțire a dischetei cu fișe fiscale pentru anul 9999 Borderou de însoțire a dischetei cu fișe fiscale pentru anul 9999 ---------------
