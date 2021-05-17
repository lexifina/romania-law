# Anexa nr. 3
FORMA ȘI CONȚINUTUL rapoartelor de transferuri externe în și din conturi, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, indiferent dacă tranzacția se efectuează printr-o singură operațiune sau prin mai multe operațiuni care au o legătură între ele pentru entități bancare și nonbancare
I.
Aspecte introductive Prezentele dispoziții se aplică instituțiilor de credit și instituțiilor financiare, conform prevederilor art. 7 alin. (3) din Legea nr. 129/2019 pentru prevenirea și combaterea spălării banilor și finanțării terorismului, precum și pentru modificarea și completarea unor acte normative, cu modificările și completările ulterioare (denumită în continuare lege).
Raportul de transferuri externe în și din conturi, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, indiferent dacă tranzacția se efectuează printr-o singură operațiune sau prin mai multe operațiuni care au o legătură între ele (numit în continuare RTE) este un fișier în format structurat (.dbf), denumit cccccczzllaaaa_t.DBF, unde: - cccccc reprezintă codul entității raportoare, care este alocat fiecărei entități raportoare la înregistrarea în sistem;
- zzllaaaa reprezintă data la care se face raportarea - sub forma zi, lună, an;
- _t reprezintă identificatorul tipului de raport.
II.
Forma raportului de transferuri externe
Număr coloană
Denumire coloană
Tip
Dimensiune
Observații/Restricții 1 data_rap
Dată 10 setată în forma zz/ll/aaaa, unde zz = ziua, ll = luna, aaaa = anul - 4 poziții 2 cod_banca
Numeric 6 3 cod_suc
Numeric 6 cod din Nomenclatorul de subunități 4 tip_c
Caracter 1 valori admisibile „F” sau „J” 5 pep_c
Numeric 1 cod din nomenclatorul Pep 6 nume_c
Caracter 40 7 pren_c
Caracter 30 8 cod_c
Caracter 13 9 tip_id_c
Numeric 2 cod din nomenclatorul Act_id 10 seria_id_c
Caracter 3 11 nr_id_c
Caracter 14 12 data_id_c
Dată 10 setată în forma zz/ll/aaaa 13 autor_id_c
Caracter 20 14 tara_c
Numeric 3 cod din nomenclatorul Tari 15 judet_c
Numeric 2 cod din nomenclatorul Judete 16 loca_c
Numeric 6 cod din nomenclatorul Loca 17 str_c
Caracter 35 18 nr_c
Caracter 5 19 sector_c
Numeric 1 valori admisibile: 1 la 6 20 rez_c
Caracter 1 valori admisibile „R” sau „N” 21 cet_c
Numeric 3 cod din nomenclatorul Tari 22 loca_reg
Caracter 40 23 pep_rep
Numeric 1 cod din nomenclatorul Pep 24 nume_rep
Caracter 25 25 pren_rep
Caracter 30 26 cod_rep
Caracter 13 27 fel_ct
Numeric 1 valori admisibile: 0, 1 și 2 28 cont_c
Caracter 30 29 tip_ct
Numeric 2 cod din nomenclatorul Tip_cont 30 tara_ext
Numeric 3 cod din nomenclatorul Tari 31 den_ext
Caracter 50 32 cont_ext
Caracter 30 33 tip_ext
Caracter 1 valori admisibile „F” sau „J” 34 pep_ext
Numeric 1 cod din nomenclatorul Pep 35 nume_ext
Caracter 40 36 pren_ext
Caracter 30 37 pep_i
Numeric 1 cod din nomenclatorul Pep 38 nume_i
Caracter 25 39 pren_i
Caracter 30 40 cod_i
Caracter 13 41 tip_act_i
Caracter 15 42 nr_act_i
Caracter 15 43 tip_id_i
Numeric 2 cod din nomenclatorul Act_id 44 seria_id_i
Caracter 3 45 nr_id_i
Caracter 14 46 data_id_i
Dată 10 setată în forma zz/ll/aaaa 47 autor_id_i
Caracter 20 48 tara_i
Numeric 3 cod din nomenclatorul Tari 49 judet_i
Numeric 2 cod din nomenclatorul Judete 50 loca_i
Numeric 6 cod din nomenclatorul Loca 51 str_i
Caracter 35 52 nr_i
Caracter 5 53 sector_i
Numeric 1 valori admisibile: 1 la 6 54 data_op
Dată 10 setată în forma zz/ll/aaaa 55 suma_op
Numeric 13 >=1 56 cod_valuta
Caracter 3 cod din nomenclatorul Valute 57 fel_op
Caracter 1 2 valori admisibile „D” sau „C” 58 euro
Numeric 13 >=1 59 detalii
Caracter 6 cod din nomenclatorul Tip_oper 60 observatii
Caracter 200
III.
Conținutul raportului de transferuri externe RTE conține, conform prevederilor art. 7 alin. (3) din lege, date privind transferurile externe în și din conturi, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, indiferent dacă tranzacția se efectuează printr-o singură operațiune sau prin mai multe operațiuni care au o legătură între ele. Toate transferurile externe din ziua/perioada pentru care se face raportarea sunt incluse într-un singur RTE.
RTE conține următoarele categorii de informații: - data raportării și identificarea entității raportoare (coloanele 1 la 3);
- date de identificare și administrative ale clientului entității raportoare (coloanele 4 la 22);
- date de identificare ale reprezentantului legal al clientului entității raportoare (coloanele 23 la 26);
- date despre contul clientului entității raportoare (coloanele 27 la 29);
- date despre entitatea externă și clientul acesteia (coloanele 30 la 36);
- date de identificare și administrative ale persoanei care a efectuat propriu-zis operațiunea raportată: împuternicit, delegat, reprezentant, mandatar al clientului (coloanele 37 la 53);
- date despre transfer/operațiune (coloanele 54 la 60).
Conținutul RTE este prezentat în detaliu în cele ce urmează, precizându-se și unele aspecte referitoare la obligativitatea și modul de completare a coloanelor indicate în forma raportului (punctul II): 1.
Coloana 1: „data_rap” conține data la care este raportat RTE, în format ZZ/LL/AAAA - zi/lună/an.
2.
Coloana 2: „cod_banca” conține codul de identificare al entității raportoare, care este un număr secvențial, alocat automat la înregistrarea în sistem.
3.
Coloana 3: „cod_suc” conține codul intern de identificare al subunității entității raportoare - sucursală, agenție, punct de lucru etc. - prin care s-a derulat operațiunea raportată. Acest cod este stabilit de către entitatea raportoare și este unic pentru fiecare subunitate a sa. Dacă entitatea raportoare nu are subunități, în această coloană conține, în mod convențional, valoarea 0 - corespunzătoare sediului central.
4.
Coloana 4: „tip_c” conține tipul clientului entității raportoare și are una dintre cele 2 valori admisibile, și anume: „F” - pentru persoane fizice sau „J” - pentru persoane juridice.
5.
Coloana 5: „pep_c” se referă la statutul de „persoană expusă public” al clientului entității raportoare - persoană fizică, în sensul prevăzut de art. 3 alin. (1) din lege, și conține un cod de identificare al funcției publice importante pe care o ocupă clientul entității raportoare, conform art. 3 alin. (2) din lege.
6.
Coloana 6: „nume_c” conține numele de familie al clientului - persoană fizică, așa cum este înscris în documentul de identitate, respectiv denumirea clientului - persoană juridică, așa cum este înscrisă pe documentul de înregistrare.
7.
Coloana 7: „pren_c” conține prenumele întreg al clientului - persoană fizică, așa cum este înscris în documentul de identitate. În cazul în care clientul este persoană juridică, această coloană nu se completează.
8.
Coloana 8: „cod_c” conține codul numeric personal, așa cum este înscris în documentul de identitate - pentru client persoană fizică, respectiv codul unic de înregistrare, așa cum este înscris în certificatul de înregistrare - pentru client persoană juridică. În cazul în care clientul persoană fizică străină nu are cod numeric personal, în această coloană se completează, în mod convențional, numărul documentului de identitate.
9.
Coloana 9: „tip_id_c” conține codul de identificare al tipului de document de identitate al clientului entității raportoare - persoana fizică. Pentru persoane juridice această coloană nu se completează.
10.
Coloana 10: „seria_id_c” conține seria actului de identitate al clientului entității raportoare - persoană fizică. Pentru persoane juridice sau în cazul în care actul de identitate al clientului persoană fizică nu este prevăzut cu o serie, această coloană nu se completează.
11.
Coloana 11: „nr_id_c” conține numărul actului de identitate al clientului - persoană fizică, respectiv numărul de înmatriculare la Registrul comerțului al clientului - persoană juridică.
12.
Coloana 12: „data_id_c” conține, în forma zz/ll/aaaa (zi, lună, an) data eliberării actului de identitate al clientului entității raportoare - persoană fizică. Pentru persoane juridice această coloană nu se completează.
13.
Coloana 13: „autor_id_c” conține denumirea autorității care a emis actul de identitate al clientului entității raportoare - persoană fizică. Pentru persoane juridice această coloană nu se completează.
14.
Coloana 14: „tara_c” conține codul de identificare al țării de domiciliu/reședință a clientului - persoană fizică, respectiv al țării unde se află sediul clientului - persoană juridică.
15.
Coloana 15: „judet_c” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința clientului - persoană fizică, respectiv al județului unde se află sediul clientului - persoană juridică.
16.
Coloana 16: „loca_c” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința clientului - persoană fizică, respectiv al localității unde se află sediul clientului - persoană juridică.
17.
Coloana 17: „str_c” conține denumirea străzii unde este situat domiciliul/reședința clientului - persoană fizică, respectiv a străzii unde se află sediul clientului - persoană juridică. În cazul în care domiciliul/sediul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzătoare.
18.
Coloana 18: „nr_c” conține numărul aferent străzii unde este situat(ă) domiciliul/reședința clientului - persoană fizică, respectiv numărul aferent străzii unde se află sediul clientului - persoană juridică.
19.
Coloana 19: „sector_c” conține numărul sectorului unde este situat domiciliul/reședința clientului - persoană fizică, respectiv sectorul unde se află sediul clientului - persoană juridică. Coloana se completează numai în cazul în care domiciliul/sediul clientului este în București. Valorile admisibile pentru această coloană sunt numerele întregi de la 1 la 6.
20.
Coloana 20: „rez_c” conține, pentru clientul entității raportoare - persoană fizică, una dintre cele două valori alternative, „R” pentru rezident sau „N” pentru nerezident. În cazul în care clientul este persoană juridică, această coloană nu se completează.
21.
Coloana 21: „cet_c” conține codul de identificare al țării corespunzătoare cetățeniei clientului persoană fizică, respectiv codul țării unde a fost înregistrat clientul persoană juridică străină.
22.
Coloana 22: „loca_reg” conține, pentru persoanele juridice străine, denumirea orașului/localității unde au fost înregistrate acestea. Pentru persoanele fizice și pentru persoanele juridice române, această coloană nu se completează.
23.
Coloana 23: „pep_rep” se referă la statutul de „persoană expusă public” al reprezentantului legal al clientului entității raportoare (persoană juridică), în sensul prevăzut de art. 3 alin. (1) din lege, și conține un cod de identificare al funcției publice importante pe care o ocupă reprezentantul legal, conform art. 3 alin. (2) din lege. Dacă reprezentantul legal al clientului (persoană juridică) are statut de „persoană expusă public”, completarea acestei coloane este obligatorie. În caz contrar, precum și pentru clientul entității raportoare persoană fizică, această coloană că nu se completează.
24.
Coloana 24: „nume_rep” conține numele de familie al reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, iar pentru clientul persoană fizică această coloană nu se completează.
25.
Coloana 25: „pren_rep” conține prenumele întreg al reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, iar pentru clientul persoană fizică această coloană nu se completează.
26.
Coloana 26: „cod_rep” conține codul numeric personal al reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. În cazul în care reprezentantul legal al clientului este o persoană fizică străină și nu are cod numeric personal, în această coloană se completează, în mod convențional, numărul documentului de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, iar pentru clientul persoană fizică această coloană nu se completează.
27.
Coloana 27: „fel_ct” conține codul de identificare al felului contului deschis de către client la entitatea raportoare, având una dintre următoarele valori admisibile: „0” pentru cont individual, „1” pentru contul deținut în comun de mai multe persoane sau „2” pentru contul unei persoane juridice.
28.
Coloana 28: „cont_c” conține numărul - codul, simbolul - contului prin care s-a efectuat transferul extern, cont deschis de către client la entitatea raportoare.
29.
Coloana 29: „tip_ct” conține codul de identificare a tipului de cont al clientului entității raportoare.
30.
Coloana 30: „tara_ext” conține codul de identificare al țării de proveniență sau, după caz, de destinație a sumei transferate. Acest cod nu se referă la țara unde este situat sediul social central al entității externe.
31.
Coloana 31: „den_ext” conține denumirea băncii - entitate străină - de la care sau, după caz, către care se face transferul de bani.
32.
Coloana 32: „cont_ext” conține contul clientului entității externe din care/către care se face transferul de bani.
33.
Coloana 33: „tip_ext” conține tipul clientului entității externe și are una dintre cele 2 valori admisibile, și anume: „F” - pentru persoane fizice sau „J” - pentru persoane juridice.
34.
Coloana 34: „pep_ext” se referă la statutul de „persoană expusă public” al clientului entității externe (persoană fizică), în sensul prevăzut de art. 3 alin. (1) din lege, și conține un cod de identificare al funcției publice importante pe care o ocupă clientul entității externe, conform art. 3 alin. (2) din lege.
35.
Coloana 35: „nume_ext” conține numele de familie al clientului entității externe - persoană fizică, așa cum este înscris în documentul de identitate, respectiv denumirea clientului entității externe - persoană juridică, așa cum este înscrisă pe documentul de înregistrare.
36.
Coloana 36: „pren_ext” conține prenumele întreg al clientului entității externe - persoană fizică, așa cum este înscris în documentul de identitate. Pentru clienți ai entității externe - persoane juridice această coloană nu se completează.
37.
Coloana 37: „pep_i” se referă la statutul de „persoană expusă public” al persoanei care efectuează operațiunea, în sensul prevăzut de art. 3 alin. (1) din lege, și conține un cod de identificare al funcției publice importante pe care o ocupă persoana care efectuează operațiunea, conform art. 3 alin. (2) din lege.
38.
Coloana 38: „nume_i” conține numele de familie al persoanei care efectuează operațiunea, așa cum este înscris în documentul de identitate.
39.
Coloana 39: „pren_i” conține prenumele întreg al persoanei care efectuează operațiunea, așa cum este înscris în documentul de identitate.
40.
Coloana 40: „cod_i” conține codul numeric personal al persoanei care efectuează operațiunea, așa cum este înscris în documentul de identitate. În cazul în care persoana care efectuează operațiunea este persoană străină și nu are cod numeric personal, în această coloană se completează, în mod convențional, numărul documentului de identitate.
41.
Coloana 41: „tip_act_i” conține tipul actului în baza căruia persoana acționează ca împuternicit pe contul clientului, delegat, mandatar, reprezentant etc.
42.
Coloana 42: „nr_act_i” conține numărul și data înregistrării actului în baza căruia persoana acționează ca împuternicit pe contul clientului, delegat, mandatar, reprezentant etc.
43.
Coloana 43: „tip_id_i” conține codul de identificare al tipului de document de identitate al persoanei care efectuează operațiunea.
44.
Coloana 44: „seria_id_i” conține seria actului de identitate al persoanei care efectuează operațiunea. În cazul în care actul de identitate al persoanei care efectuează tranzacția nu este prevăzut cu o serie, această coloană nu se completează.
45.
Coloana 45: „nr_id_i” conține numărul actului de identitate al persoanei care efectuează operațiunea.
46.
Coloana 46: „data_id_i” conține, în forma zz/ll/aaaa (zi, lună, an), data eliberării actului de identitate al persoanei care efectuează tranzacția.
47.
Coloana 47: „autor_id_i” conține denumirea autorității care a emis actul de identitate al persoanei care efectuează operațiunea.
48.
Coloana 48: „tara_i” conține codul de identificare al țării de domiciliu/reședință a persoanei care efectuează operațiunea.
49.
Coloana 49: „județ_i” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința persoanei care efectuează operațiunea.
50.
Coloana 50: „loca_i” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința persoanei care efectuează operațiunea.
51.
Coloana 51: „str_i” conține denumirea străzii unde este situat domiciliul/reședința persoanei care efectuează operațiunea. În cazul în care domiciliul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzătoare.
52.
Coloana 52: „nr_i” conține numărul aferent străzii unde este situat(ă) domiciliul/reședința persoanei care efectuează operațiunea.
53.
Coloana 53: „sector_i” conține numărul sectorului unde este situat(ă) domiciliul/reședința persoanei care efectuează operațiunea. Coloana se completează numai în cazul în care domiciliul persoanei care efectuează tranzacția este în București. Valorile admisibile pentru această coloană sunt numerele întregi de la 1 la 6.
54.
Coloana 54: „data_op” conține data la care a fost făcută operațiunea, sub forma zi/lună/an.
55.
Coloana 55: „suma_op” conține suma corespunzătoare transferului extern, exprimată în valuta al cărei cod de identificare este completat în coloana 56. Dacă suma operațiunii este un număr zecimal, aceasta se rotunjește. În cazul raportării transferurilor externe care se efectuează prin mai multe operațiuni care au o legătură între ele, dacă suma tranzacționată în una dintre operațiuni este subunitară, aceasta se rotunjește, în mod convențional, la valoarea 1.
56.
Coloana 56: „cod_valuta” conține codul de identificare al valutei corespunzătoare sumei înscrise în coloana 55.
57.
Coloana 57: „fel_op” conține una dintre cele două valori admisibile, și anume: „D” în cazul în care contul clientului entității raportoare se debitează, respectiv „C” atunci când contul se creditează. Felul operațiunii este definit în raport cu tranzacția efectuată pentru clientul entității raportoare.
58.
Coloana 58: „euro” conține echivalentul în euro al sumei completate în coloana 55, obținut folosind cursul de referință al Băncii Naționale a României din ziua în care s-a efectuat tranzacția. Dacă rezultatul aplicării cursului de referință este un număr zecimal, acesta se rotunjește. În cazul raportării transferurilor externe care se efectuează prin mai multe operațiuni care au o legătură între ele, dacă echivalentul euro aferent sumei tranzacționate în una dintre operațiuni este subunitar, acesta se rotunjește, în mod convențional, la valoarea 1.
59.
Coloana 59: „detalii” conține codul de identificare al tipului de operațiune raportată.
60.
Coloana 60: „observatii” conține eventuale precizări suplimentare pe care le poate face entitatea raportoare în legătură cu transferul extern raportat. În cazul în care una dintre persoanele menționate în raport are statut de PEP, în această coloană se completează datele și informațiile care au condus la încadrarea persoanei în respectiva categorie.
Completarea cu date a coloanelor 1 la 60 din RTE este obligatorie, cu următoarele excepții:
1.
În cazul în care clientul entității raportoare - persoană fizică efectuează tranzacția în nume propriu, coloanele 37 la 53 nu se completează.
2.
În cazul în care clientul entității raportoare este persoană juridică sau persoană fizică fără statut de PEP, coloana 5 nu se completează.
3.
În cazul în care reprezentantul legal al clientul entității raportoare (persoană juridică) nu are statut de PEP, coloana 23 nu se completează.
4.
În cazul în care clientul entității externe este persoană juridică sau persoană fizică fără statut de PEP, coloana 34 nu se completează.
5.
În cazul în care persoana care efectuează tranzacția nu are statut de PEP, coloana 37 nu se completează.
6.
Coloanele 15, 16, 49 și 50 nu se completează dacă valoarea aferentă coloanei 14, respectiv 48 corespunzătoare este alta decât 642 (România).
7.
Coloanele 15 și 49 nu se completează dacă valoarea aferentă coloanei 14, respectiv 48 corespunzătoare este 642 (România) și valoarea aferentă coloanei 16, respectiv 50 este 403 (București).
8.
Coloanele 19 și 53 nu se completează dacă valoarea aferentă coloanei 16, respectiv 50 este alta decât 403 (București).
9.
Pentru persoanele străine rezidente în România, în coloanele 14 la 19, respectiv 48 la 53 din fișier se completează cu prioritate adresa/sediul din România. Dacă aceste informații nu sunt disponibile, coloanele 14, 17 și 18, respectiv 48, 51 și 52 conțin adresa/sediul din străinătate al persoanei respective.
10.
La cele de mai sus se adaugă excepțiile prevăzute expres (în context) pentru fiecare coloană în paragraful privind conținutul RTE.
Fișierul denumit cccccczzllaaaa_t.DBF, care este de fapt RTE, poate fi creat în 2 moduri: 1. prin completarea, de către entitatea raportoare, a coloanelor 1 la 60 în interfața sistemului, caz în care fișierul este generat automat de către sistem. La completarea RTE în interfața sistemului, coloanele 1 și 2 din fișier se preiau automat, iar coloanele 4, 19, 20, 27, 33, 53 și 57 se completează de către entitatea raportoare prin selecția din liste de valori predefinite.
Coloanele 3, 5, 9, 14 la 16, 21, 23, 29, 30, 34, 37, 43, 48 la 50, 56 și 59 se preiau automat în sistem prin alegerea, de către entitatea raportoare, pentru fiecare coloană, a unei valori dintro listă bazată pe nomenclatoarele de pep, țări, județe, localități, tip operațiuni, respectiv valute.
Coloanele 6 la 8, 10 la 13, 17, 18, 22, 24 la 26, 28, 31, 32, 35, 36, 38 la 42, 44 la 47, 51, 52, 54, 55, 58 și 60 se completează propriu-zis de către entitatea raportoare în sistem.
În sistem, fiecărui raport cccccczzllaaaa_t.DBF i se asociază automat un fișier de tip.pdf, cu caracter ilustrativ. În acest fișier, toate coloanele care conțin coduri în raport sunt înlocuite cu rubrici în care este explicitată semnificația (descrierea) fiecărui cod, conform nomenclatoarelor aferente.
2. prin încărcarea în sistem a unui fișier agregat cccccczzllaaaa_t.DBF, având forma și conținutul descrise în acest capitol, extras din baza de date a entității raportoare, folosind proceduri proprii. Pentru completarea unor coloane din acest fișier sunt folosite nomenclatoarele enumerate în anexa nr. 2 la ordin, după cum urmează:
a)
Tari.dbf - nomenclatorul conține valorile admisibile pentru coloanele 14, 21, 30 și 48 din RTE;
b)
Judete.dbf - nomenclatorul conține valorile admisibile pentru coloanele 15 și 49 din RTE;
c)
Loca.dbf - nomenclatorul conține valorile admisibile pentru coloanele 16 și 50 din RTE;
d)
Valute.dbf - nomenclatorul conține valorile admisibile pentru coloana 56 din RTE;
e)
Tip_oper.dbf - nomenclatorul conține valorile admisibile pentru coloana 59 din RTE;
f)
Pep.dbf - nomenclatorul conține valorile admisibile pentru coloanele 5, 23, 34 și 37 din RTE;
g) cccccc.dbf - nomenclatorul conține valorile admisibile pentru coloana 3 din RTE.
În plus față de acestea, Oficiul Național de Prevenire și Combatere a Spălării Banilor (ONPCSB) pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, următoarele nomenclatoare: a)
Act_id.dbf - nomenclatorul conține valorile admisibile pentru coloanele 9 și 43 din RTE;
b)
Tip_cont.dbf - nomenclatorul conține valorile admisibile pentru coloana 29 din RTE. De asemenea, ONPCSB pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, un format de RTE: fișierul cccccczzllaaaa_t.DBF.
