# Anexa nr. 2
FORMA ȘI CONȚINUTUL rapoartelor de tranzacții cu numerar, în lei sau valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, inclusiv operațiunile care au o legătură între ele pentru entități bancare și nonbancare
I.
Aspecte introductive Prezentele dispoziții se aplică entităților raportoare prevăzute la art. 5 coroborat cu art. 7 alin. (2) din Legea nr. 129/2019 pentru prevenirea și combaterea spălării banilor și finanțării terorismului, precum și pentru modificarea și completarea unor acte normative, cu modificările și completările ulterioare (denumită în continuare lege).
Raportul de tranzacții cu numerar, în lei sau valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, inclusiv operațiunile care au o legătură între ele (denumit în continuare RTN) este un fișier în format structurat (.dbf), denumit cccccczzllaaaa_n.DBF, unde: - cccccc reprezintă codul entității raportoare, care este alocat fiecărei entități raportoare la înregistrarea în sistem;
- zzllaaaa reprezintă data la care se face raportarea - sub forma zi, lună, an;
- n reprezintă identificatorul tipului de raport.
II.
Forma raportului de tranzacții cu numerar
Număr coloană Denumire coloană Tip Dimensiune Observații/Restricții 1 data_rap Dată 10 setată în forma zz/ll/aaaa, unde zz = ziua, ll = luna, aaaa = anul 2 cod_banca Numeric 6 3 cod_suc Numeric 6 cod din nomenclatorul de subunități 4 tip_c Caracter 1 valori admisibile „F” sau „J” 5 pep_c Numeric 1 cod din nomenclatorul Pep 6 nume_c Caracter 40 7 pren_c Caracter 30 8 tara_c Numeric 3 cod din nomenclatorul Tari 9 judet_c Numeric 2 cod din nomenclatorul Judete 10 loca_c Numeric 6 cod din nomenclatorul Loca 11 str_c Caracter 35 12 nr_c Caracter 5 13 sector_c Numeric 1 valori admisibile: 1 la 6 14 act_id_c Caracter 15 15 cod_c Caracter 13 16 data_nasc Dată 10 setată în forma zz/ll/aaaa 17 tara_nasc Numeric 3 cod din nomenclatorul Tari 18 loca_nasc Numeric 6 cod din nomenclatorul Loca 19 pep_i Numeric 1 cod din nomenclatorul Pep 20 nume_i Caracter 25 21 pren_i Caracter 30 22 tara_i Numeric 3 cod din nomenclatorul Tari 23 judet_i Numeric 2 cod din nomenclatorul Judete 24 loca_i Numeric 6 cod din nomenclatorul Loca 25 str_i Caracter 35 26 nr_i Caracter 5 27 sector_i Numeric 1 valori admisibile: 1 la 6 28 act_id_i Caracter 15 29 cod_i Caracter 13 30 cont_tit Caracter 30 31 data_op Dată 10 setată în forma zz/ll/aaaa 32 fel_op Caracter 1 valori admisibile „D” sau „R” 33 scop_op Caracter 6 cod din nomenclatorul Tip_oper 34 cod_valuta Caracter 3 cod din nomenclatorul Valute 35 suma_op Numeric 13 >=1 36 euro Numeric 13 >=1 37 observații Caracter 200
III.
Conținutul raportului de tranzacții cu numerar RTN conține, conform prevederilor art. 7 alin. (1) din lege, tranzacțiile cu numerar, în lei sau valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, inclusiv operațiunile care au o legătură între ele. Toate tranzacțiile cu numerar din ziua/perioada pentru care se face raportarea sunt incluse într-un singur RTN.
RTN conține următoarele categorii de informații: - data raportării și identificarea entității raportoare (coloanele 1 la 3);
- date de identificare și administrative ale clientului entității raportoare (coloanele 4 la 18);
- date de identificare și administrative ale persoanei care a efectuat propriu-zis operațiunea raportată: împuternicit, delegat, reprezentant, mandatar al clientului (coloanele 19 la 29);
- date despre tranzacție (coloanele 30 la 37).
Conținutul RTN este prezentat în detaliu în cele ce urmează, precizându-se și unele aspecte referitoare la obligativitatea și modul de completare a coloanelor indicate în forma raportului (punctul II): 1.
Coloana 1: „data_rap” conține data la care este raportat RTN, în format ZZ/LL/AAAA - zi/lună/an.
2.
Coloana 2: „cod_banca” conține codul de identificare al entității raportoare, care este un număr secvențial, alocat automat la înregistrarea în sistem.
3.
Coloana 3: „cod_suc” conține codul intern de identificare al subunității entității raportoare - sucursală, agenție, punct de lucru etc. - prin care s-a derulat operațiunea raportată. Acest cod este stabilit de către entitatea raportoare și este unic pentru fiecare subunitate a sa. Dacă entitatea raportoare nu are subunități, această coloană conține, în mod convențional, valoarea 0 - corespunzătoare sediului central.
4.
Coloana 4: „tip_c” conține tipul clientului entității raportoare și are una dintre cele 2 valori admisibile, și anume: „F” - pentru persoane fizice sau „J” - pentru persoane juridice.
5.
Coloana 5: „pep_c” se referă la statutul de „persoană expusă public” al clientului - persoană fizică, în sensul prevăzut de art. 3 alin. (1) din lege, și conține un cod de identificare al funcției publice importante pe care o ocupă clientul, conform art. 3 alin. (2) din lege.
6.
Coloana 6: „nume_c” conține numele de familie al clientului - persoană fizică, așa cum este înscris în documentul de identitate, respectiv denumirea clientului - persoană juridică, așa cum este înscrisă pe documentul de înregistrare.
7.
Coloana 7: „pren_c” conține prenumele întreg al clientului - persoană fizică, așa cum este înscris în documentul de identitate. În cazul în care clientul este persoană juridică, această coloană nu se completează.
8.
Coloana 8: „tara_c” conține codul de identificare al țării de domiciliu/reședință a clientului - persoană fizică, respectiv al țării unde se află sediul clientului - persoană juridică.
9.
Coloana 9: „judet_c” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința clientului - persoană fizică, respectiv al județului unde se află sediul clientului - persoană juridică.
10.
Coloana 10: „loca_c” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința clientului - persoană fizică, respectiv al localității unde se află sediul clientului - persoană juridică.
11.
Coloana 11: „str_c” conține denumirea străzii unde este situat domiciliul/reședința clientului - persoană fizică, respectiv a străzii unde se află sediul clientului - persoană juridică. În cazul în care domiciliul/sediul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzătoare.
12.
Coloana 12: „nr_c” conține numărul aferent străzii unde este situat domiciliul/reședința clientului - persoană fizică, respectiv numărul străzii unde se află sediul clientului - persoană juridică.
13.
Coloana 13: „sector_c” conține numărul sectorului unde este situat domiciliul/reședința clientului - persoană fizică, respectiv sectorul unde se află sediul clientului - persoană juridică. Coloana se completează numai în cazul în care domiciliul/sediul clientului este în București. Valorile admisibile pentru această coloană sunt numerele întregi de la 1 la 6.
14.
Coloana 14: „act_id_c” conține seria și numărul actului de identitate pentru client persoană fizică, respectiv numărul de înmatriculare de la registrul comerțului - pentru client persoană juridică.
15.
Coloana 15: „cod_c” conține codul numeric personal, așa cum este înscris în documentul de identitate, pentru clienți persoane fizice, respectiv codul unic de înregistrare, așa cum este înscris în certificatul de înregistrare, pentru clienți persoane juridice. În cazul în care clientul persoană fizică străină nu are cod numeric personal, în această coloană se completează, în mod convențional, numărul documentului de identitate.
16.
Coloana 16: „data_nasc” conține, sub forma zi/lună/an, data nașterii clientului persoană fizică, așa cum este înscrisă în documentul de identitate, respectiv data înmatriculării, așa cum este înscrisă în documentul de înregistrare - în cazul clientului persoană juridică.
17.
Coloana 17: „tara_nasc” conține codul de identificare al țării nașterii clientului - persoană fizică, respectiv al țării unde a fost înmatriculată persoana juridică.
18.
Coloana 18: „loca_nasc” conține, dacă este cazul, codul de identificare al localității nașterii clientului persoană fizică, respectiv al localității unde a fost înmatriculat clientul - persoană juridică
19.
Coloana 19: „pep_i” se referă la statutul de „persoană expusă public” al persoanei care efectuează tranzacția, în sensul prevăzut în sensul prevăzut de art. 3 alin. (1) din lege, și conține un cod de identificare al funcției publice importante pe care o ocupă persoana care efectuează tranzacția, conform art. 3 alin. (2) din lege.
20.
Coloana 20: „nume_i” conține numele de familie al persoanei care efectuează tranzacția, așa cum este înscris în documentul de identitate.
21.
Coloana 21: „pren_i” conține prenumele întreg al persoanei care efectuează tranzacția, așa cum este înscris în documentul de identitate.
22.
Coloana 22: „tara_i” conține codul de identificare al țării de domiciliu/reședință a persoanei care efectuează tranzacția.
23.
Coloana 23: „județ_i” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința persoanei care efectuează tranzacția.
24.
Coloana 24: „loca_i” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința persoanei care efectuează tranzacția.
25.
Coloana 25: „str_i” conține denumirea străzii unde este situat domiciliul/reședința persoanei care efectuează tranzacția. În cazul în care domiciliul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzătoare.
26.
Coloana 26: „nr_i” conține numărul aferent străzii unde este situat domiciliul/reședința persoanei care efectuează tranzacția.
27.
Coloana 27: „sector_i” conține numărul sectorului unde este situat domiciliul/reședința persoanei care efectuează tranzacția. Coloana se completează numai în cazul în care domiciliul persoanei care efectuează tranzacția este în București. Valorile admisibile pentru această coloană sunt numerele întregi de la 1 la 6.
28.
Coloana 28: „act_id_i” conține seria și numărul actului de identitate al persoanei care efectuează tranzacția.
29.
Coloana 29: „cod_i” conține codul numeric personal al persoanei care efectuează tranzacția, așa cum este înscris în documentul de identitate. În cazul în care persoana care efectuează tranzacția este persoană străină și nu are cod numeric personal, în această coloană se completează, în mod convențional, numărul documentului de identitate.
30.
Coloana 30: „cont_tit” conține, în cazul în care operațiunea raportată implică mișcări într-un cont deschis pe numele clientului, numărul - codul, simbolul - acestui cont. În cazul în care operațiunea se desfășoară în baza unei relații contractuale, în această coloană se completează numărul de înregistrare și data contractului încheiat între entitatea raportoare și clientul respectiv.
În cazul în care entitatea raportoare autentifică un act prin care are loc operațiunea raportată, în această coloană se completează numărul și data cu care a fost autentificat actul respectiv.
În cazul în care operațiunea are loc prin casieria entității raportoare, în această coloană se completează simbolul contului contabil „Casa”.
31.
Coloana 31: „data_op” conține data la care a fost făcută operațiunea, sub forma zi/lună/an.
32.
Coloana 32: „fel_op” conține felul operațiunii și are 2 valori admisibile, și anume: „D” - pentru depunere de numerar/ încasare de la client sau „R” - pentru retragere de numerar/plată către client. În mod convențional, în cazul operațiunilor de vânzare-cumpărare cu numerar, cumpărarea efectuată de către client este asimilată cu operațiunea de depunere, respectiv vânzarea efectuată de către client este asimilată cu operațiunea de retragere.
33.
Coloana 33: „scop_op” conține codul de identificare al tipului de operațiune raportată.
34.
Coloana 34: „cod_valuta” conține codul de identificare al valutei corespunzătoare operațiunii raportate.
35.
Coloana 35: „suma_op” conține suma corespunzătoare operațiunii cu numerar, exprimată în valuta al cărei cod de identificare este completat în coloana 34. Dacă suma tranzacționată este un număr zecimal, aceasta se rotunjește. În cazul raportării operațiunilor care au o legătură între ele, dacă suma tranzacționată într-una dintre operațiuni este subunitară, aceasta se rotunjește, în mod convențional, la valoarea 1.
36.
Coloana 36: „euro” conține echivalentul în euro al sumei completate în coloana 35, obținut folosind cursul de referință al Băncii Naționale a României din ziua în care s-a efectuat tranzacția. Dacă rezultatul aplicării cursului de referință este un număr zecimal, acesta se rotunjește. În cazul raportării operațiunilor care au o legătură între ele, dacă echivalentul euro aferent sumei tranzacționate într-una dintre operațiuni este subunitar, acesta se rotunjește, în mod convențional, la valoarea 1.
37.
Coloana 37: „observatii” conține eventuale precizări suplimentare pe care le poate face entitatea raportoare în legătură cu tranzacția raportată. În cazul în care clientul sau persoana care efectuează operațiunea are statut de PEP, în această coloană se completează datele și informațiile care au condus la încadrarea persoanei în respectiva categorie.
Completarea cu date a coloanelor 1 la 36 din RTN este obligatorie, cu următoarele excepții:
1.
În cazul în care clientul persoană fizică efectuează tranzacția în nume propriu, coloanele 19 la 29 nu se completează.
2.
În cazul în care clientul este persoană juridică sau este persoană fizică fără statut de PEP, coloana 5 nu se completează.
3.
În cazul în care persoana care efectuează tranzacția nu are statut de PEP, coloana 19 nu se completează.
4.
Coloanele 9 și 23 nu se completează dacă valoarea aferentă coloanei 8, respectiv 22 corespunzătoare este alta decât 642 (România).
5.
Coloanele 9 și 23 nu se completează dacă valoarea aferentă coloanei 8, respectiv 22 corespunzătoare este 642 (România) și valoarea aferentă coloanei 10, respectiv 24 este 403 (București).
6.
Coloanele 10, 18 și 24 nu se completează în cazul în care valoarea aferentă coloanei 8, 17, respectiv 22 este alta decât 642 (România).
7.
Coloanele 13 și 27 nu se completează dacă valoarea aferentă coloanei 10, respectiv 24 este alta decât 403 (București).
8.
La cele de mai sus se adaugă excepțiile prevăzute expres (în context), în paragraful privind conținutul RTN, pentru fiecare coloană.
Pentru completarea RTN se au în vedere următoarele reguli: 1.
Operațiunile de schimb valutar sunt incluse în RTN o singură dată, astfel: a) în coloana 32 „fel_op” - se completează valoarea D;
b) în coloana 34 - „cod valuta” - se completează codul valutei sumei depuse de client în vederea efectuării schimbului;
c) în coloana 35 - „suma_op” - se completează suma de bani depusă de client în vederea efectuării schimbului;
d) în coloana 36 - „euro” - se completează echivalentul în euro, calculat la cursul Băncii Naționale a României, al sumei de bani depuse de client în vederea efectuării schimbului;
e) în coloana 37 - „observatii” - se completează obligatoriu suma primită de client în urma schimbului valutar, urmată de codul valutei corespunzătoare;
f)
Celelalte coloane se completează conform precizărilor din conținutul RTN.
2.
În cazul operațiunilor de vânzare-cumpărare cu numerar a unui bun deținut în comun de mai multe persoane - locuințe, terenuri etc., în fișier se completează, pentru fiecare persoană implicată în tranzacție, coloanele 1 la 34 conform precizărilor din conținutul RTN. Completarea celorlalte coloane se face după cum urmează: a) în coloana 35 - „suma_op” - se completează, pentru fiecare persoană, suma totală aferentă tranzacției;
b) în coloana 36 - „euro” - se completează, în mod convențional, valoarea obținută prin împărțirea echivalentului în euro, calculat la cursul Băncii Naționale a României, al sumei tranzacționate - coloana 35 - la numărul de persoane implicate de fiecare parte a tranzacției. Dacă rezultatul împărțirii este un număr zecimal, acesta se rotunjește;
c) în coloana 37 - „observatii” - se completează obligatoriu sintagma „efectuată în comun”.
3.
Pentru persoanele străine rezidente în România, în coloanele 8 la 13, respectiv 22 la 27 din fișier se completează cu prioritate adresa/sediul din România. Dacă aceste informații nu sunt disponibile, coloanele 8, 11 și 12, respectiv 22, 25 și 26 conțin adresa/sediul din străinătate al persoanei respective. Fișierul denumit cccccczzllaaaa_n.DBF, care este de fapt RTN, poate fi creat în 2 moduri: 1. prin completarea, de către entitatea raportoare, a coloanelor 1 la 37 în interfața sistemului, caz în care fișierul este generat automat de către sistem. La completarea RTN în interfața sistemului, coloanele 1 și 2 din fișier se preiau automat, iar coloanele 4, 13, 27 și 32 se completează de către entitatea raportoare prin selecția din liste de valori predefinite.
Coloanele 3, 5, 8 la 10, 17 la 19, 22 la 24, 33 și 34 se preiau automat în sistem prin alegerea, de către entitatea raportoare, pentru fiecare coloană, a unei valori dintr-o listă bazată pe nomenclatoarele de pep, țări, județe, localități, tip operațiuni, respectiv valute.
Coloanele 6, 7, 11, 12, 14 la 16, 20, 21, 25, 26, 28 la 31 și 35 la 37 se completează propriu-zis de către entitatea raportoare în sistem.
În sistem, fiecărui raport cccccczzllaaaa_n.DBF i se asociază automat un fișier de tip.pdf, cu caracter ilustrativ. În acest fișier toate coloanele care conțin coduri în raport sunt înlocuite cu rubrici în care este explicitată semnificația (descrierea) fiecărui cod, conform nomenclatoarelor aferente.
2. prin încărcarea în sistem a unui fișier agregat cccccczzllaaaa_n.DBF, având forma și conținutul descrise în acest capitol, extras din baza de date a entității raportoare, folosind proceduri proprii. Pentru completarea unor coloane din acest fișier, Oficiul Național de Prevenire și Combatere a Spălării Banilor (ONPCSB) pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, următoarele nomenclatoare: a)
Tari.dbf - nomenclatorul conține valorile admisibile pentru coloanele 8, 17 și 22 din RTN;
b)
Judete.dbf - nomenclatorul conține valorile admisibile pentru coloanele 9 și 23 din RTN;
c)
Loca.dbf - nomenclatorul conține valorile admisibile pentru coloanele 10, 18 și 24 din RTN. În acest nomenclator sunt cuprinse generic - ca denumire - toate localitățile din România, o singură dată. În cazul în care aceeași denumire corespunde în fapt mai multor localități, identificarea se face după codul județului completat în coloana de județ corespunzătoare.
d)
Valute.dbf - nomenclatorul conține valorile admisibile pentru coloana 34 din RTN;
e)
Tip_oper.dbf - nomenclatorul conține valorile admisibile pentru coloana 33 din RTN;
f)
Pep.dbf - nomenclatorul conține valorile admisibile pentru coloanele 5 și 19 din RTN;
g) cccccc.dbf (unde cccccc reprezintă codul entității raportoare) - formatul nomenclatorului de subunități, cu următoarea structură:
Nr. coloană Denumire coloană Tip Dimensiune Observații/Restricții 1 cod_s Numeric 6 codul sucursalei, agenției, punctului de lucru etc. 2 den_s Caracter 100 denumirea subunității 3 tip_s Caracter 1 tipul subunității, valori admisibile: „C” - sediul central, „S” - sucursală, „A” - agenție, „P” - punct de lucru 4 cod_j Numeric 2 codul județului unde este situată subunitatea, conform nomenclatorului Judete
Acest nomenclator poate fi completat de către entitatea raportoare în interfața sistemului sau poate fi obținut din sistemul informatic al acesteia și apoi încărcat în sistem. Nomenclatorul de subunități conține valorile admisibile pentru completarea coloanei 3 din RTN.
De asemenea, ONPCSB pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, un format de RTN: fișierul cccccczzllaaaa_n.DBF.
