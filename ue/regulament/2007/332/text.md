REGULAMENTUL (CE) NR. 332/2007 AL COMISIEI
din 27 martie 2007
privind modalitățile tehnice de transmitere a statisticilor cu privire la transportul feroviar
(Text cu relevanță pentru SEE)
COMISIA COMUNITĂȚILOR EUROPENE,
având în vedere Tratatul de instituire a Comunității Europene,
având în vedere Regulamentul (CE) nr. 91/2003 al Parlamentului European și al Consiliului din 16 decembrie 2002 privind statisticile din transportul feroviar (1), în special articolul 6 alineatul (2),
întrucât:
(1) Este necesar să se specifice detaliat formatul în care trebuie transmise Comisiei (Eurostatului) datele privind transportul feroviar pentru a se asigura faptul că informațiile pot fi procesate rapid și într-o manieră profitabilă.
(2) Măsurile prevăzute în prezentul regulament sunt conforme cu avizul Comitetului pentru programe statistice, constituit prin Decizia 89/382/CEE, Euratom a Consiliului (2),
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Formatul tehnic pentru transmiterea de date Comisiei (Eurostatului) este cel prezentat în anexă.
Statele membre folosesc acest format pentru datele privind anul de referință 2007 și anii următori.
Articolul 2
Datele și metadatele furnizate în conformitate cu Regulamentul (CE) nr. 91/2003 sunt transmise în format electronic de către orice organizație desemnată de autoritățile naționale către singurul punct de intrare pentru date al Comisiei (Eurostatului). Transferul este conform cu un standard de schimb adecvat specificat de Eurostat.
Articolul 3
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 27 martie 2007.
Pentru Comisie
Joaquín ALMUNIA
Membru al Comisiei
(1) JO L 14, 21.1.2003, p. 1. Regulament, astfel cum a fost modificat prin Regulamentul (CE) nr. 1192/2003 al Comisiei (JO L 167, 4.7.2003, p. 13).
(2) JO L 181, 28.6.1989, p. 47.
ANEXĂ
FORMAT TEHNIC PENTRU TRANSMITEREA DATELOR
1. STRUCTURA DATELOR
Înregistrările de date individuale care trebuie trimise Eurostatului la fiecare trimestru, an sau perioadă de cinci ani cuprind 9 seturi de date, fiecare corespunzând unei anexe la Regulamentul (CE) nr. 91/2003. Aceste seturi de date cuprind următoarele date:
— statistici anuale privind transportul de mărfuri – raportare detaliată (anexa A);
— statistici anuale privind transportul de mărfuri – raportare simplificată (anexa B);
— statistici anuale privind transportul de călători – raportare detaliată (anexa C);
— statistici anuale privind transportul de călători – raportare simplificată (anexa D);
— statistici trimestriale privind transportul de mărfuri și de călători (anexa E);
— statistici regionale cincinale privind transportul de mărfuri și de călători (anexa F);
— statistici cincinale privind fluxurile de trafic pe rețeaua feroviară (anexa G);
— statistici privind accidentele (anexa H);
— lista întreprinderilor feroviare pentru care sunt furnizate statistici (anexa I).
Anexele B și D stabilesc condiții de raportare simplificate, care pot fi folosite de către statele membre ca alternativă la raportarea normală detaliată stabilită în anexele A și C, pentru întreprinderi care se situează sub pragurile precizate la articolul 4 alineatul (2) din Regulamentul (CE) nr. 91/2003.
2. LISTĂ DE CÂMPURI
În conformitate cu Regulamentul (CE) nr. 91/2003, în fiecare anexă trebuie prevăzut câte un set de date sub forma unui fișier plat care folosește punct și virgulă „;” ca separator de câmpuri. Fiecare set de date, cu excepția setului de date C, trebuie să conțină informații pentru toate tabelele cerute în mod obligatoriu în anexă. Pentru fiecare set de date, numărul de câmpuri din fiecare raportare este fix. Așadar, toate câmpurile trebuie să figureze, chiar dacă sunt lipsite de informații (două separatoare de câmpuri notate succesiv indică un câmp lipsit de conținut).
Câmpurile individuale sunt descrise mai jos după cum urmează:
— „Numărul câmpului”: acesta indică poziția câmpului în raportare;
— „Numele câmpului”: acesta fie se referă la o variabilă din Regulamentul (CE) nr. 91/2003, fie la un identificator intern folosit pentru identificarea raportului;
— „Descriere”: scurtă descriere a conținutului câmpului;
— „Codificare”: în tabelele A2 și A4, anumite câmpuri trebuie codificate conform anexelor J și K la Regulamentul (CE) nr. 91/2003. Regulile de codificare suplimentare sunt definite aici. Mai multe explicații și recomandări privind codificarea sunt prevăzute de Eurostat în liniile directoare privind punerea în aplicare a Regulamentului (CE) nr. 91/2003;
— „Tipul câmpului”: indică existența în cadrul câmpului a unor informații numerice sau a unui text; toate informațiile numerice trebuie furnizate sub forma unui număr întreg;
— „Lungimea maximă”: lungimea maximă prevăzută a datelor pentru un anumit câmp. Datele prea lungi nu pot fi încărcate;
— „Indicator de confidențialitate” (FlagC) indică dacă raportarea este considerată confidențială de către statele membre [Regulamentul (CE) nr. 322/97 al Consiliului (1), articolul 13 alineatul (1) și Regulamentul (Euratom; CEE) nr. 1588/90 al Consiliului (2), articolul 2];
— „Indicator de autorizare a difuzării” de date confidențiale (FlagD) indică dacă informațiile confidențiale furnizate de către statele membre pot fi difuzate [Regulamentul (CE) nr. 322/97, articolul 13 alineatul (2) și Regulamentul (Euratom, CEE) nr. 1588/90, articolul 5 alineatul (4)]. Prin urmare, Comisia este autorizată prin lege să schimbe hotărârea statelor membre în cazuri bine definite. Aceasta se face prin schimbarea FlagD=1 cu FlagD=0 când FlagC=1.
Setul de date pentru anexa A: Statistici anuale privind transportul de mărfuri – raportare detaliată
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator set de date | A1 la A9 | Text | 2 |
3 | Year | Anul setului de date | 4 cifre | Text | 4 |
4 | Period | Perioada de referință | A0 | Text | 2 |
5 | TransID | Tipul de transport | 0 | : | transport total 1 | : | transport național 2 | : | transport internațional – total 3 | : | transport internațional – ieșiri 4 | : | transport internațional – intrări 5 | : | transport de tranzit | Text | 1 |
6 | Goods | Tipul de mărfuri | anexa J la regulament | Text | 2 |
7 | DGoods | Tipul de mărfuri periculoase | anexa K la regulament | Text | 3 |
8 | LDG | Țara de încărcare | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 | XX
9 | UNL | Țara de descărcare | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 | XX
10 | Consgmt | Tipul de modalitate de expediție | 1 | : | trenuri încărcate complet 2 | : | vagoane încărcate complet 3 | : | altele 9 | : | necunoscut | Text | 1 |
11 | TTU | Tipul unității de transport | 1 | : | containere și containere mobile 2 | : | semiremorci (neînsoțite) 3 | : | autovehicule (însoțite) 9 | : | necunoscut | Text | 1 |
12 | Tonnes | Transport total de mărfuri | Tone | Numeric | 10 |
13 | Tkm | Transport total de mărfuri în tone pe 1 000 km | Tone/1 000 km | Numeric | 10 |
14 | NbrITU | Număr de unități de transport intermodal | Număr de UTI | Numeric | 8 |
15 | TeuITU | Unități de transport intermodal efectuate în TEU | TEU | Numeric | 8 |
16 | TrainKM | Mișcări de trenuri de marfă pe 1 000 km | Tren/1 000 km | Numeric | 8 |
17 | FlagC | Indicator de confidențialitate | 1 | : | confidențial 0 | : | neconfidențial | Text | 1 |
18 | FlagD | Indicator de autorizare a difuzării | 1 | : | difuzare neautorizată 0 | : | difuzare autorizată | Text | 1 |
În fișierul plat care conține datele pentru anexa A, fiecare raportare cuprinde 18 câmpuri. Următorul tabel prezintă cu gri câmpurile care trebuie furnizate pentru diversele tabele ale anexei A. Căsuțele albe corespund câmpurilor fără conținut din raportare. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să constituie o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
Dset ID
Număr câmp | Nume câmp | A1 | A2 | A3 | A4 | A5(3) | A6 | A7 | A8 | A9
1 | RCount | * | * | * | * | * | * | * | * | *
2 | DsetID | * | * | * | * | * | * | * | * | *
3 | Year | * | * | * | * | * | * | * | * | *
4 | Period | * | * | * | * | * | * | * | * | *
5 | TransID | * | | * | | | * | * | * |
6 | Goods | | * | | | | | | |
7 | DGoods | | | | * | | | | |
8 | LDG | | | * | | | | | |
9 | UNL | | | * | | | | | |
10 | Consgmt | | | | | * | | | |
11 | TTU | | | | | | | | |
12 | Tonnes | | | | | | | | |
13 | Tkm | | | | | | | | |
14 | NbrITU | | | | | | | | |
15 | TeuITU | | | | | | | | |
16 | TrainKM | | | | | | | | |
17 | FlagC | | | | | | | | |
18 | FlagD | | | | | | | | |
Setul de date pentru anexa B: Statistici anuale privind transportul de mărfuri – raportare simplificată
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator set de date | B1 la B2 | Text | 2 |
3 | Year | Anul setului de date | 4 cifre | Text | 4 |
4 | Period | Perioada de referință | A0 | Text | 2 |
5 | TransID | Tipul de transport | 0 | : | transport total 1 | : | transport național 2 | : | transport internațional – total 3 | : | transport internațional – ieșiri 4 | : | transport internațional – intrări 5 | : | transport de tranzit | Text | 1 |
6 | Tonnes | Transport total de mărfuri | Tone | Numeric | 10 |
7 | Tkm | Transport total de mărfuri în tone pe 1 000 km | Tone/1 000 km | Numeric | 10 |
8 | TrainKm | Mișcări de trenuri de marfă pe 1 000 km | Tren/1 000 km | Numeric | 8 |
9 | FlagC | Indicator de confidențialitate | 1 | : | confidențial 0 | : | neconfidențial | Text | 1 |
10 | FlagD | Indicator de autorizare a difuzării | 1 | : | difuzare neautorizată 0 | : | difuzare autorizată | Text | 1 |
În fișierul plat care conține datele pentru anexa B, fiecare raportare cuprinde 10 câmpuri. Următorul tabel prezintă cu gri câmpurile care trebuie furnizate pentru fiecare dintre cele două tabele ale anexei B. Căsuțele albe corespund câmpurilor lipsite de conținut din raportare. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să constituie o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
Dset ID
Număr câmp | Nume câmp | B1 | B2
1 | RCount | * | *
2 | DsetID | * | *
3 | Year | * | *
4 | Period | * | *
5 | TransID | * |
6 | Tonnes | |
7 | Tkm | |
8 | TrainKM | |
9 | FlagC | |
10 | FlagD | |
Setul de date pentru anexa C: Statistici anuale privind transportul de călători – raportare detaliată
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator set de date | C1 la C5 | Text | 2 |
3 | Year | Anul setului de date | 4 cifre | Text | 4 |
4 | Period | Perioada de referință | A0 | Text | 2 |
5 | TransID | Tipul de transport | 1 | : | transport național 2 | : | transport internațional – total 3 | : | transport internațional – ieșiri 4 | : | transport internațional – intrări | Text | 1 |
6 | LDG | Țara de încărcare | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 | XX
7 | UNL | Țara de descărcare | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 | XX
8 | Pass | Transport total de călători | Călători | Numeric | 10 |
9 | Passkm | Transport total de călători pe 1 000 km | p/1 000 km | Numeric | 10 |
10 | TrainKm | Mișcări de trenuri de călători pe 1 000 km | Tren/1 000 km | Numeric | 8 |
11 | FlagC | Indicator de confidențialitate | 1 | : | confidențial 0 | : | neconfidențial | Text | 1 |
12 | FlagD | Indicator de autorizare a difuzării | 1 | : | difuzare neautorizată 0 | : | difuzare autorizată | Text | 1 |
În fișierul plat care conține datele pentru anexa C, fiecare raportare cuprinde 12 câmpuri. Următorul tabel prezintă cu gri câmpurile care trebuie furnizate pentru diversele tabele ale anexei C. Căsuțele albe corespund câmpurilor lipsite de conținut din raportare. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să reprezinte o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
Informații provizorii (tabelele C1 și C2), finale și consolidate (tabelele C3 și C4) urmează a fi trimise la date diferite și după aceeași structură.
Dset ID
Număr câmp | Nume câmp | C1(4) | C2(4) | C3(5) | C4(5) | C5
1 | RCount | * | * | * | * | *
2 | DsetID | * | * | * | * | *
3 | Year | * | * | * | * | *
4 | Period | * | * | * | * | *
5 | TransID | * 1 & 2 | * 3 & 4 | * 1 & 2 | * 3 & 4 |
6 | LDG | | * | | * |
7 | UNL | | * | | * |
8 | Pass | | | | |
9 | Passkm | | | | |
10 | TrainKM | | | | |
11 | FlagC | | | | |
12 | FlagD | | | | |
Setul de date pentru anexa D: Statistici anuale privind transportul de călători – raportare simplificată
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator set de date | D1 la D2 | Text | 2 |
3 | Year | Anul setului de date | 4 cifre | Text | 4 |
4 | Period | Perioada de referință | A0 | Text | 2 |
5 | Pass | Transport total de călători | Călători | Numeric | 10 |
6 | Passkm | Total de persoane transportate pe 1 000 km | p/1 000 km | Numeric | 10 |
7 | TrainKm | Transport total de călători pe 1 000 km | Tren/1 000 km | Numeric | 8 |
8 | FlagC | Indicator de confidențialitate | 1 | : | confidențial 0 | : | neconfidențial | Text | 1 |
9 | FlagD | Indicator de autorizare a difuzării | 1 | : | difuzare neautorizată 0 | : | difuzare autorizată | Text | 1 |
În fișierul plat care conține datele pentru anexa D, fiecare raportare cuprinde 9 câmpuri. Următorul tabel prezintă cu gri câmpurile care trebuie furnizate pentru fiecare dintre cele două tabele ale anexei D. Căsuțele albe corespund câmpurilor lipsite de conținut din raportare. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să reprezinte o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
DsetID
Număr câmp | Nume câmp | D1 | D2
1 | RCount | * | *
2 | DsetID | * | *
3 | Year | * | *
4 | Period | * | *
5 | Pass | |
6 | Passkm | |
7 | TrainKM | |
8 | FlagC | |
9 | FlagD | |
Setul de date pentru anexa E: Statistici trimestriale privind transportul de mărfuri și de călători
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator bază date | E1 la E2 | Text | 2 |
3 | Year | Anul bazei de date | 4 cifre | Text | 4 |
4 | Period | Perioada de referință | Q1 la Q4 | Text | 2 |
5 | Tonnes | Transport total de mărfuri | Tone | Numeric | 10 |
6 | Tkm | Transport total de mărfuri în tone pe 1 000 km | Tone/1 000 km | Numeric | 10 |
7 | Pass | Transport total de călători | Călători | Numeric | 10 |
8 | Passkm | Transport total de călători pe 1 000 km | p/1 000 km | Numeric | 10 |
9 | FlagC | Indicator de confidențialitate | 1 | : | confidențial 0 | : | neconfidențial | Text | 1 |
10 | FlagD | Indicator de autorizare a difuzării | 1 | : | difuzare neautorizată 0 | : | difuzare autorizată | Text | 1 |
În fișierul plat care conține datele pentru anexa E, fiecare raportare cuprinde 10 câmpuri. Următorul tabel prezintă cu gri câmpurile care trebuie furnizate pentru fiecare dintre cele două tabele ale anexei E. Căsuțele albe corespund câmpurilor lipsite de conținut din raportare. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să reprezinte o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
DsetID
Număr câmp | Nume câmp | E1 | E2
1 | RCount | * | *
2 | DsetID | * | *
3 | Year | * | *
4 | Period | * | *
5 | Tonnes | |
6 | Tkm | |
7 | Pass | |
8 | Passkm | |
9 | FlagC | |
10 | FlagD | |
Setul de date pentru anexa H: Statistici privind accidentele
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator set de date | H1 la H4 | Text | 2 |
3 | Year | Anul setului de date | 4 cifre | Text | 4 |
4 | Period | Perioada de referință | A0 | Text | 2 |
5 | AccID | Tipul de accident | 1 | : | Coliziuni 2 | : | Deraieri 3 | : | Accidente implicând treceri la nivel 4 | : | Accidente suferite de persoane datorită materialului rulant în mișcare 5 | : | Incendieri ale materialului rulant 6 | : | Altele 7 | : | Total 9 | : | Necunoscut | Text | 1 |
6 | PersID | Categorii de persoane | 1 | : | Călători 2 | : | Angajați 3 | : | Altele 4 | : | Total [5: Utilizatori ai trecerii la nivel] [6: | Persoane neautorizate în preajma căilor ferate] 9 | : | Necunoscut | Text | 1 |
7 | NbAccSign | Numărul de accidente importante | Număr | Numeric | 8 |
8 | NbAccInj | Numărul de accidente cu răni grave | Număr | Numeric | 8 |
9 | NbAccDGIn | Numărul de accidente care implică transportul de mărfuri periculoase | Număr | Numeric | 8 |
10 | NbAccDGRe | Numărul de accidente care implică dispersarea de mărfuri periculoase | Număr | Numeric | 8 |
11 | NbPersK | Numărul de persoane ucise | Număr | Numeric | 8 |
12 | NbPersI | Numărul de persoane cu răni grave | Număr | Numeric | 8 |
În fișierul plat care conține datele pentru anexa H, fiecare raportare cuprinde 12 câmpuri. Următorul tabel prezintă cu gri câmpurile care trebuie furnizate pentru fiecare dintre tabelele anexei H. Căsuțele albe corespund câmpurilor lipsite de conținut din raportare. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să reprezinte o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
Tabelul cuprinde alte două categorii de persoane care ar putea fi solicitate pe viitor: „5: Utilizatori ai trecerii la nivel” și „6: Persoane neautorizate în preajma căilor ferate”.
DsetID
Număr câmp | Nume câmp | H1 | H2 | H3 | H4
1 | RCount | * | * | * | *
2 | DsetID | * | * | * | *
3 | Year | * | * | * | *
4 | Period | * | * | * | *
5 | AccID | * | | * | *
6 | PersID | | | * | *
7 | NbAccSign | | | |
8 | NbAccInj(6) | | | |
9 | NbAccDGIn | | | |
10 | NbAccDGRe | | | |
11 | NbPersK | | | |
12 | NbPersI | | | |
Set de date pentru anexa I
Număr câmp | Nume câmp | Descriere | Codificare | Tip câmp | Lungime maximă | Coduri specifice pentru valorile lipsă
1 | RCount | Țara declarantă | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 |
2 | DsetID | Identificator set de date | I1 | Text | 2 |
3 | Year | Anul setului de date | 4 cifre | Text | 4 |
4 | UCode | Codul întreprinderii (constant) | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit + număr de 3 cifre | Text | 5 | XX
5 | UName | Denumirea întreprinderii | | Text | 100 |
6 | CountID | Țara în care își are sediul întreprinderea | nomenclatura ISO-3166-alpha2, cu excepția „UK” pentru Regatul Unit | Text | 2 | XX
7 | IntFret | Activitatea de transport de marfă: internațional | 1 | : | DA 0 | : | NU | Text | 1 |
8 | Natfret | Activitatea de transport de marfă: național | 1 | : | DA 0 | : | NU | Text | 1 |
9 | Intpass | Activitatea de transport de călători: internațional | 1 | : | DA 0 | : | NU | Text | 1 |
10 | Natpass | Activitatea de transport de călători: național | 1 | : | DA 0 | : | NU | Text | 1 |
11 | DsetA | Date incluse în anexa A | 1 | : | DA 0 | : | NU | Text | 1 |
12 | DsetB | Date incluse în anex B | 1 | : | DA 0 | : | NU | Text | 1 |
13 | DsetC | Date incluse în anexa C | 1 | : | DA 0 | : | NU | Text | 1 |
14 | DsetD | Date incluse în anexa D | 1 | : | DA 0 | : | NU | Text | 1 |
15 | DsetE | Date incluse în anexa E | 1 | : | DA 0 | : | NU | Text | 1 |
16 | DsetF | Date incluse în anexa F | 1 | : | DA 0 | : | NU | Text | 1 |
17 | DsetG | Date incluse în anexa G | 1 | : | DA 0 | : | NU | Text | 1 |
18 | DsetH | Date incluse în anexa H | 1 | : | DA 0 | : | NU | Text | 1 |
19 | Tons | Transport total de marfă (în tone) | Tone | Numeric | 10 |
20 | Tkm | Transport total de marfă (t/1 000 km) | Tone/1 000 kilometri | Numeric | 10 |
21 | Pass | Transport total de călători (în călători) | Număr de călători | Numeric | 10 |
22 | Passkm | Transport total de călători (călători/1 000 km) | Călători/1 000 km | Numeric | 10 |
În fișierul plat care conține datele pentru anexa I, fiecare raportare cuprinde 22 câmpuri. Următorul tabel prezintă toate câmpurile cu gri deoarece anexa I conține doar un tabel. Câmpurile opționale pot fi lăsate libere. Un câmp-cheie este notat cu un asterisc. Combinația valorilor câmpurilor-cheie dintr-o raportare trebuie să reprezinte o valoare-cheie unică în cadrul fișierului. Dacă există duplicate de valori-cheie, fișierul nu se va încărca corect.
Număr câmp | Nume câmp | DsetIDI1
1 | RCount | *
2 | DsetID | *
3 | Year | *
4 | UCode | *
5 | UName(7) |
6 | CountID |
7 | IntFret |
8 | Natfret |
9 | Intpass |
10 | Natpass |
11 | DsetA |
12 | DsetB |
13 | DsetC |
14 | DsetD |
15 | DsetE |
16 | DsetF |
17 | DsetG |
18 | DsetH |
19 | Tons(8) |
20 | Tkm(9) |
21 | Pass(10) |
22 | Passkm(11) |
3. VALORI LIPSĂ
Eurostat poate recomanda, pentru valorile lipsă sau alte valori speciale din anumite câmpuri, utilizarea unor coduri specifice (a se vedea coloana „coduri specifice pentru valorile lipsă”).
Informațiile suplimentare sunt prevăzute în liniile directoare privind punerea în aplicare a Regulamentului (CE) nr. 91/2003.
4. ALTERNATIVE LA FORMATELE STANDARD
Statele membre pot folosi alte formate standard care să mențină structurile de date menționate anterior, acolo unde acestea sunt propuse de Eurostat.
5. VALIDAREA DATELOR DE CĂTRE EUROSTAT
Înainte ca datele să fie încărcate în baza de date de producție, Eurostat supune unor controale de validare informațiile transmise de către statele membre. În cazul în care un număr important de înregistrări sunt invalide, Eurostat înștiințează statele membre cu privire la aceasta și aduce motivații pentru neacceptare. Statelor membre li se cere îndreptarea erorilor identificate și apoi repunerea la dispoziție a setului de date complet (nu doar a înregistrărilor invalide). Această procedură este necesară pentru garantarea corectitudinii informațiilor din și dintre diferite seturi de date.
6. DENUMIREA FIȘIERULUI SETULUI DE DATE
Trebuie utilizată următoarea convenție de denumire a fișierelor:
„ RAIL_annex_frequency_CC_YYYY_period[_OptionalField].format ”, unde:
RAIL | Pentru date privind transportul feroviar
Annex | Identificarea setului de date (de exemplu, anexă a regulamentului): A | : | Statistici anuale privind transportul de mărfuri – raportare detaliată B | : | Statistici anuale privind transportul de mărfuri – raportare simplificată C | : | Statistici anuale privind transportul de călători – raportare detaliată D | : | Statistici anuale privind transportul de călători – raportare simplificată E | : | Statistici trimestriale privind transportul de mărfuri și de călători F | : | Statistici regionale privind transportul de mărfuri și de călători G | : | Statistici privind fluxul de trafic pe rețeaua feroviară H | : | Statistici privind accidentele I | : | Lista întreprinderilor feroviare
Frequency | A pentru Anual Q pentru Trimestrial 5 pentru fiecare cinci ani
CC | Țara declarantă: a se utiliza ISO3166-alpha2, cu excepția „UK” pentru Regatul Unit
YYYY | An de referință (de exemplu, 2004)
Period | „0000” pentru anual „0001” pentru primul trimestru „0002” pentru cel de-al doilea trimestru „0003” pentru cel de-al treilea trimestru „0004” pentru cel de-al patrulea trimestru „0005” pentru cincinal
[_CâmpOpțional] | Poate conține orice înșiruire de caractere în număr de la 1 la 220 (sunt acceptate doar cele de la „A” la „Z”, „0” la „9” sau „_”). Acest câmp nu se interpretează prin instrumentele Eurostat.
.format | Formatul fișierului: (ex. „CSV” pentru „Comma Separated Value”, „GES” pentru GESMES)
Pentru fiecare anexă la regulament și pentru fiecare perioadă trebuie trimis un fișier separat.
Exemplu:
Fișierul „RAIL_E_Q_FR_2004_0002.csv” este fișierul de date care conține informațiile din Franța pentru anexa E la regulament, acoperind cel de-al doilea trimestru al anului 2004.
7. METODĂ DE TRANSMITERE
Datele sunt transmise sau transferate în format electronic către singurul punct de intrare pentru date al Eurostatului. Această metodă asigură transmiterea în siguranță a datelor confidențiale.
(1) JO L 52, 22.2.1997, p. 1.
(2) JO L 151, 15.6.1990, p. 1.
(3) Tabelul A5 este un tabel opțional.
(4) Informații provizorii.
(5) Informații finale consolidate.
(6) Numărul de accidente cu răni grave (NbAccInj) este o variabilă opțională în tabelul H1.
(7) Denumirea întreprinderii (UName) este o variabilă opțională.
(8) Transport total de marfă (în tone) este o variabilă opțională.
(9) Transport total de marfă (în t/1 000 km) (Tkm) este o variabilă opțională.
(10) Transport total de călători (în persoane) (Pass) este o variabilă opțională.
(11) Transport total de călători (în p/1 000 km) (Passkm) este o variabilă opțională.
