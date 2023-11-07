# Anexa nr. 3
FORMA ȘI CONȚINUTUL
Raportului de transferuri externe, în și din conturi, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, indiferent dacă tranzacția se efectuează printr-o singură operațiune sau prin mai multe operațiuni care au o legătură între ele, pentru instituțiile de credit și instituțiile financiare
I.
Aspecte introductive Prezentele dispoziții se aplică instituțiilor de credit și instituțiilor financiare, conform prevederilor art. 7 alin. (3) din Legea nr. 129/2019 pentru prevenirea și combaterea spălării banilor și finanțării terorismului, precum și pentru modificarea și completarea unor acte normative, cu modificările și completările ulterioare (lege).
Raportul de transferuri externe, în și din conturi, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, indiferent dacă tranzacția se efectuează printr-o singură operațiune sau prin mai multe operațiuni care au o legătură între ele (denumit în continuare RTE) este un fișier în format structurat (.xlsx/.csv), denumit RTE_zzllaaaa_cccccc.xlsx/.csv, unde: -
RTE reprezintă identificatorul tipului de raport;
- zzllaaaa reprezintă data la care se face raportarea - sub forma zi, lună, an;
- cccccc reprezintă codul entității raportoare, care este alocat fiecărei entități raportoare la înregistrarea în portal.
II.
Forma raportului de transferuri externe este ilustrată în tabelul următor:
Nr. coloană
Denumire coloană
Tip
Dimensiune
Observații/Restricții 1 data_rap
Dată 10 setată în forma zz/ll/aaaa, unde zz = ziua, ll = luna, aaaa = anul 2 cod _ent
Numeric 6 3 cod_suc
Numeric 6 cod din nomenclatorul de sedii secundare 4 tip_c
Caracter 1 valori admisibile „F” sau „J” 5 pep_c
Numeric 1 cod din nomenclatorul Pep 6 nume_c
Caracter 50 7 pren_c
Caracter 30 8 cet_c
Numeric 3 cod din nomenclatorul Tari 9 cod_c
Caracter 13 10 data_n_c
Dată 10 setată în forma zz/ll/aaaa 11 act_id_c
Caracter 15 12 rez_c
Caracter 1 valori admisibile „R” sau „N” 13 f_jur
Caracter 10 cod din nomenclatorul Forme_juridice_de_organizare 14 cod_Caen
Numeric 4 cod din nomenclatorul Coduri_Caen 15 tara_c
Numeric 3 cod din nomenclatorul Tari 16 judet_c
Numeric 2 cod din nomenclatorul Judete 17 loca_c
Numeric 6 cod din nomenclatorul Loca 18 str_c
Caracter 50 19 nr_c
Caracter 10 20 pep_r
Numeric 1 cod din nomenclatorul Pep 21 nume_r
Caracter 50 22 pren_r
Caracter 30 23 cet_r
Numeric 3 cod din nomenclatorul Tari 24 cod_r
Caracter 13 25 data_n_r
Dată 10 setată în forma zz/ll/aaaa 26 pep_i
Numeric 1 cod din nomenclatorul Pep 27 nume_i
Caracter 50 28 pren_i
Caracter 30 29 cet_i
Numeric 3 cod din nomenclatorul Tari 30 cod_i
Caracter 13 31 data_n_i
Dată 10 setată în forma zz/ll/aaaa 32 act _id_i
Caracter 15 33 tara_i
Numeric 3 cod din nomenclatorul Tari 34 judet_i
Numeric 2 cod din nomenclatorul Judete 35 loca_i
Numeric 6 cod din nomenclatorul Loca 36 str_i
Caracter 50 37 nr_i
Caracter 10 38 fel_ct
Numeric 1 valori admisibile: 0, 1 și 2 39 cont_c
Caracter 30 40 tip_ct
Numeric 2 cod din nomenclatorul Tip_cont 41 tara_ext
Numeric 3 cod din nomenclatorul Tari 42 den_ext
Caracter 50 43 cont_ext
Caracter 30 44 tip_ext
Caracter 1 valori admisibile „F” sau „J” 45 pep_ext
Numeric 1 cod din nomenclatorul Pep 46 nume_ext
Caracter 50 47 pren_ext
Caracter 30 48 cod_tr
Caracter 50 49 cod_tr_leg
Caracter 50 50 data_op
Dată 10 setată în forma zz/ll/aaaa 51 suma_op
Numeric 13 >= 1 52 cod_valuta
Caracter 3 cod din nomenclatorul Valute 53 fel_op
Caracter 1 valori admisibile „D” sau „C” 54 euro
Numeric 13 >= 1 55 scop_op
Caracter 6 cod din nomenclatorul Tip_oper 56 observatii
Caracter 200
III.
Conținutul raportului de transferuri externe: RTE conține, conform prevederilor art. 7 alin. (3) din lege, date privind transferurile externe, în și din conturi, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, indiferent dacă tranzacția se efectuează printr-o singură operațiune sau prin mai multe operațiuni care au o legătură între ele. Toate transferurile externe din ziua/perioada pentru care se face raportarea sunt incluse într-un singur RTE.
RTE conține următoarele categorii de informații: - data raportării și identificarea entității raportoare (coloanele 1-3);
- date de identificare ale clientului entității raportoare (coloanele 4-19);
- date de identificare ale reprezentantului legal al clientului entității raportoare (coloanele 20-25);
- date de identificare ale persoanei care a efectuat propriu-zis operațiunea raportată: împuternicit, delegat, reprezentant, mandatar al clientului (coloanele 26-37);
- date despre contul clientului entității raportoare (coloanele 38-40);
- date despre entitatea externă și clientul acesteia (coloanele 41-47);
- date despre transfer/operațiune (coloanele 48-56).
Conținutul RTE este prezentat în detaliu în cele ce urmează, precizându-se și unele aspecte referitoare la obligativitatea și modul de completare a coloanelor indicate în forma raportului (pct. II): 1.
Coloana 1: „data_rap” conține data la care este raportat RTE, în format ZZ/LL/AAAA - zi/lună/an.
2.
Coloana 2: „cod_ent” conține codul de identificare al entității raportoare, care este un număr secvențial, alocat automat la înregistrarea în portal.
3.
Coloana 3: „cod_suc” conține codul intern de identificare al sediului secundar al entității raportoare - sucursală, agenție, punct de lucru, reprezentanță sau alte asemenea unități fără personalitate juridică - prin care s-a derulat operațiunea raportată. Acest cod este stabilit de către entitatea raportoare și este unic pentru fiecare sediu secundar al său. Dacă entitatea raportoare nu are sedii secundare, această coloană conține, în mod convențional, valoarea 0 - corespunzătoare sediului social.
4.
Coloana 4: „tip_c” conține tipul clientului entității raportoare și are una dintre cele 2 valori admisibile, și anume: „F” - pentru persoane fizice sau „J” - pentru persoane juridice.
5.
Coloana 5: „pep_c” conține un cod de identificare al categoriei în care se încadrează clientul entității raportoare - persoană fizică, respectiv: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public.
6.
Coloana 6: „nume_c” conține numele clientului - persoană fizică, așa cum este înscris în documentul de identitate, respectiv denumirea clientului - persoană juridică, așa cum este înscrisă în actul constitutiv (actualizat)/certificatul de înmatriculare.
7.
Coloana 7: „pren_c” conține prenumele întreg al clientului - persoană fizică, așa cum este înscris în documentul de identitate. În cazul în care clientul este persoană juridică, această coloană nu se completează.
8.
Coloana 8: „cet_c” conține codul de identificare al țării corespunzătoare cetățeniei clientului persoană fizică, respectiv codul țării unde a fost înregistrat clientul persoană juridică.
9.
Coloana 9: „cod_c” conține codul numeric personal, așa cum este înscris în documentul de identitate - pentru client persoană fizică, respectiv codul unic de înregistrare/codul de înregistrare fiscală, așa cum este înscris în certificatul de înregistrare - pentru client persoană juridică. În cazul în care clientul persoană fizică străină nu are cod numeric personal, această coloană nu se completează.
10.
Coloana 10: „data_n_c” conține, sub forma zi/lună/an, data nașterii clientului - persoană fizică străină, așa cum este înscrisă în documentul de identitate, respectiv data înregistrării/înmatriculării la autoritatea abilitată, așa cum este înscrisă în documentul de înregistrare - în cazul clientului persoană juridică. În cazul în care clientul este persoană fizică română al cărei cod numeric personal este completat în coloana anterioară, această coloană nu se completează. În caz contrar, completarea acestei coloane este obligatorie.
11.
Coloana 11: „act_id_c” conține seria și numărul actului de identitate al clientului - persoană fizică, respectiv numărul de înregistrare/înmatriculare la autoritatea abilitată - pentru client persoană juridică.
12.
Coloana 12: „rez_c” conține, pentru clientul entității raportoare - persoană fizică, una dintre cele două valori alternative, „R” pentru rezident sau „N” pentru nerezident. În cazul în care clientul este persoană juridică, această coloană nu se completează.
13.
Coloana 13: „f_jur” conține abrevierea formei de organizare a clientului - persoană juridică, așa cum este înscrisă în actul constitutiv (actualizat)/certificatul de înmatriculare. În cazul în care clientul este persoană fizică, această coloană nu se completează.
14.
Coloana 14: „cod_CAEN” conține codul CAEN al activității de bază a clientului - persoană juridică, așa cum este înscrisă în actul constitutiv (actualizat)/certificatul de înmatriculare. În cazul în care clientul este persoană fizică, această coloană nu se completează.
15.
Coloana 15: „tara_c” conține codul de identificare al țării de domiciliu/reședință a clientului - persoană fizică, respectiv al țării unde se află sediul clientului - persoană juridică.
16.
Coloana 16: „judet_c” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința clientului - persoană fizică, respectiv al județului unde se află sediul clientului - persoană juridică.
17.
Coloana 17: „loca_c” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința clientului - persoană fizică, respectiv al localității unde se află sediul clientului - persoană juridică.
18.
Coloana 18: „str_c” conține denumirea străzii unde este situat/situată domiciliul/reședința clientului - persoană fizică, respectiv a străzii unde se află sediul clientului - persoană juridică. În cazul în care domiciliul/sediul se află în străinătate, în această coloană se completează în plus denumirea orașului/localității corespunzător/corespunzătoare.
19.
Coloana 19: „nr_c” conține numărul aferent străzii unde este situat/situată domiciliul/reședința clientului - persoană fizică, respectiv numărul aferent străzii unde se află sediul clientului - persoană juridică.
20.
Coloana 20: „pep_r” conține un cod de identificare al categoriei în care se încadrează reprezentantul legal al clientului entității raportoare (persoană juridică), respectiv: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public.
21.
Coloana 21: „nume_r” conține numele reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, iar pentru clientul persoană fizică această coloană nu se completează.
22.
Coloana 22: „pren_r” conține prenumele întreg al reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, iar pentru clientul persoană fizică această coloană nu se completează.
23.
Coloana 23: „cet_r” conține codul de identificare al țării corespunzătoare cetățeniei reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, iar pentru clientul persoană fizică această coloană nu se completează.
24.
Coloana 24: „cod_r” conține codul numeric personal al reprezentantului legal al clientului (persoană juridică), așa cum este înscris în documentul de identitate. Pentru clientul persoană juridică completarea acestei coloane este obligatorie, cu excepția cazului în care reprezentantul legal al clientului este o persoană fizică străină și nu are cod numeric personal. Pentru clientul persoană fizică această coloană nu se completează.
25.
Coloana 25: „data_n_r” conține, sub forma zi/lună/an, data nașterii reprezentantului legal al clientului (persoană juridică), așa cum este înscrisă în documentul de identitate. În cazul în care reprezentantul legal al clientului (persoană juridică) este persoană fizică română al cărei cod numeric personal este completat în coloana anterioară, această coloană nu se completează. În caz contrar, completarea acestei coloane este obligatorie. Pentru clientul persoană fizică această coloană nu se completează.
26.
Coloana 26: „pep_i” conține un cod de identificare al categoriei în care se încadrează persoana care efectuează operațiunea, respectiv: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public.
27.
Coloana 27: „nume_i” conține numele persoanei care efectuează operațiunea, așa cum este înscris în documentul de identitate.
28.
Coloana 28: „pren_i” conține prenumele întreg al persoanei care efectuează operațiunea, așa cum este înscris în documentul de identitate.
29.
Coloana 29: „cet_i” conține codul de identificare al țării corespunzătoare cetățeniei persoanei care efectuează operațiunea, conform documentului de identitate.
30.
Coloana 30: „cod_i” conține codul numeric personal al persoanei care efectuează operațiunea, așa cum este înscris în documentul de identitate. În cazul în care persoana care efectuează operațiunea este persoană străină și nu are cod numeric personal, această coloană nu se completează.
31.
Coloana 31: „data_n_i” conține, sub forma zi/lună/an, data nașterii persoanei care efectuează operațiunea, așa cum este înscrisă în documentul de identitate. În cazul în care persoana care efectuează operațiunea este cetățean român al cărei cod numeric personal este completat în coloana anterioară, această coloană nu se completează. În caz contrar, completarea acestei coloane este obligatorie.
32.
Coloana 32: „act_id_i” conține seria și numărul actului de identitate al persoanei care efectuează operațiunea.
33.
Coloana 33: „tara_i” conține codul de identificare al țării de domiciliu/reședință a persoanei care efectuează operațiunea.
34.
Coloana 34: „judet_i” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința persoanei care efectuează operațiunea.
35.
Coloana 35: „loca_i” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința persoanei care efectuează operațiunea.
36.
Coloana 36: „str_i” conține denumirea străzii unde este situat/situată domiciliul/reședința persoanei care efectuează operațiunea. În cazul în care domiciliul se află în străinătate, în această coloană se completează în plus denumirea orașului/ localității corespunzător/corespunzătoare.
37.
Coloana 37: „nr_i” conține numărul aferent străzii unde este situat/situată domiciliul/reședința persoanei care efectuează operațiunea.
38.
Coloana 38: „fel_ct” conține codul de identificare al felului contului deschis de către client la entitatea raportoare, având una dintre următoarele valori admisibile: „0” pentru cont individual, „1” pentru contul deținut în comun de mai multe persoane sau „2” pentru contul unei persoane juridice.
39.
Coloana 39: „cont_c” conține numărul - codul, simbolul - contului prin care s-a efectuat transferul extern, cont deschis de către client la entitatea raportoare.
40.
Coloana 40: „tip_ct” conține codul de identificare al tipului de cont al clientului entității raportoare.
41.
Coloana 41: „tara_ext” conține codul de identificare al țării de proveniență sau, după caz, de destinație a sumei transferate. Acest cod nu se referă la țara unde este situat sediul social al entității externe.
42.
Coloana 42: „den_ext” conține denumirea băncii - entitate străină - de la care sau, după caz, către care se face transferul de bani.
43.
Coloana 43: „cont_ext” conține contul clientului entității externe din care/către care se face transferul de bani.
44.
Coloana 44: „tip_ext” conține tipul clientului entității externe și are una dintre cele 2 valori admisibile, și anume: „F” - pentru persoane fizice sau „J” - pentru persoane juridice.
45.
Coloana 45: „pep_ext” conține un cod de identificare al categoriei în care se încadrează clientul entității externe (persoană fizică), respectiv: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public.
46.
Coloana 46: „nume_ext” conține numele clientului entității externe - persoană fizică, așa cum este înscris în documentul de identitate, respectiv denumirea clientului entității externe - persoană juridică, așa cum este înscrisă în documentul de înregistrare.
47.
Coloana 47: „pren_ext” conține prenumele întreg al clientului entității externe - persoană fizică, așa cum este înscris în documentul de identitate. Pentru clienți ai entității externe persoane juridice, această coloană nu se completează.
48.
Coloana 48: „cod_tr” conține codul intern de identificare al tranzacției la entitatea raportoare. Acest cod este stabilit de către entitatea raportoare și este unic pentru fiecare tranzacție. Dacă la nivelul entității raportoare nu există un cod unic de identificare al tranzacției, această coloană conține un cod agregat, format din codul entității raportoare însoțit de un număr secvențial (de la 1 la n) corespunzător fiecărei tranzacții, separate prin caracterul „_”.
49.
Coloana 49: „cod_tr_leg” conține, pentru operațiunile care au o legătură între ele [în sensul prevăzut la art. 2 lit. w) din lege] codul intern de identificare al tranzacției cu care a fost stabilită o legătură a tranzacției curente. Pentru completarea acestei coloane se au în vedere următoarele aspecte: - în situația în care se identifică două sau mai multe operațiuni care au o legătură între ele, se consideră operațiune de bază tranzacția cea mai veche din punct de vedere cronologic, ținând cont de data și, după caz, de ora, minutul etc. efectuării tranzacției respective;
- în mod convențional, pentru tranzacția de bază, în această coloană se preia din coloana 48 propriul cod intern de identificare;
- pentru toate celelalte operațiuni care au o legătură cu tranzacția de bază, această coloană conține codul intern de identificare al tranzacției de bază (valoarea coloanei 48 aferentă tranzacției de bază).
50.
Coloana 50: „data_op” conține data la care a fost făcută operațiunea, sub forma zi/lună/an.
51.
Coloana 51: „suma_op” conține suma corespunzătoare transferului extern, exprimată în valuta al cărei cod de identificare este completat în coloana 52. Dacă suma operațiunii este un număr zecimal, aceasta se rotunjește la cel mai apropiat număr întreg. În cazul raportării transferurilor externe care se efectuează prin mai multe operațiuni care au o legătură între ele, dacă suma tranzacționată în una dintre operațiuni este subunitară, aceasta se rotunjește, în mod convențional, la valoarea 1.
52.
Coloana 52: „cod_valuta” conține codul de identificare al valutei corespunzătoare sumei înscrise în coloana 51.
53.
Coloana 53: „fel_op” conține una dintre cele două valori admisibile, și anume: „D” în cazul în care contul clientului entității raportoare se debitează, respectiv „C” atunci când contul se creditează. Felul operațiunii este definit în raport cu tranzacția efectuată pentru clientul entității raportoare.
54.
Coloana 54: „euro” conține echivalentul în euro al sumei completate în coloana 51, obținut folosind cursul de referință al Băncii Naționale a României din ziua în care s-a efectuat tranzacția. Dacă rezultatul aplicării cursului de referință este un număr zecimal, acesta se rotunjește la cel mai apropiat număr întreg. În cazul raportării transferurilor externe care se efectuează prin mai multe operațiuni care au o legătură între ele, dacă echivalentul euro aferent sumei tranzacționate în una dintre operațiuni este subunitar, acesta se rotunjește, în mod convențional, la valoarea 1.
55.
Coloana 55: „scop_op” conține codul de identificare al tipului de operațiune raportată.
56.
Coloana 56: „observatii” conține eventuale precizări suplimentare pe care le poate face entitatea raportoare în legătură cu transferul extern raportat. În cazul în care una dintre persoanele menționate în raport se încadrează în una dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, în această coloană se completează datele și informațiile care au condus la încadrarea persoanei în respectiva categorie.
Pentru operațiunile care au o legătură între ele, în această coloană se completează, în mod obligatoriu, elementele comune ale acestor operațiuni.
Completarea cu date a coloanelor 1-56 din RTE este obligatorie, cu următoarele excepții: 1)
În cazul în care clientul entității raportoare - persoană fizică efectuează tranzacția în nume propriu, coloanele 26-37 nu se completează.
2)
În cazul în care clientul entității raportoare este persoană juridică sau persoană fizică ce nu se încadrează în niciuna dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, coloana 5 nu se completează.
3)
În cazul în care reprezentantul legal al clientul entității raportoare (persoană juridică) nu se încadrează în niciuna dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, coloana 20 nu se completează.
4)
În cazul în care persoana care efectuează tranzacția nu se încadrează în niciuna dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, coloana 26 nu se completează.
5)
În cazul în care clientul entității externe este persoană juridică sau persoană fizică ce nu se încadrează în niciuna dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, coloana 45 nu se completează.
6)
Coloanele 16, 17, 34 și 35 nu se completează dacă valoarea aferentă coloanei 15, respectiv 33 corespunzătoare este alta decât 642 (România).
7)
Coloanele 16 și 34 nu se completează dacă valoarea aferentă coloanei 15, respectiv 33 corespunzătoare este 642 (România) și valoarea aferentă coloanei 17, respectiv 35 este 403 (București).
8)
La cele de mai sus se adaugă excepțiile prevăzute expres (în context) pentru fiecare coloană, în paragraful privind conținutul RTE.
Pentru completarea RTE se au în vedere următoarele reguli: 1)
Pentru persoanele care au cetățenie dublă, în coloanele 8, 23, respectiv 29 se completează cu prioritate cetățenia română. Celelalte informații despre cetățenia persoanei respective se completează în coloana 56.
2)
Pentru persoanele străine rezidente în România, în coloanele 15-19, respectiv 33-37 din fișier se completează cu prioritate adresa/sediul din România. Dacă aceste informații nu sunt disponibile, coloanele 15, 18 și 19, respectiv 30, 36 și 37 conțin adresa/sediul din străinătate a/al persoanei respective.
3)
La identificarea operațiunilor care au legătură între ele, pentru atingerea pragului de raportare (echivalentul în lei a 10.000 euro), se ține cont de felul operațiunii, respectiv debit/credit. Toate operațiunile care au legătură între ele sunt incluse într-un singur RTE, același cu fișierul care conține transferurile externe a căror limită minimă reprezintă echivalentul în lei a 10.000 euro.
Fișierul denumit RTE_zzllaaaa_cccccc.xlsx/.csv, care este de fapt RTE, poate fi creat în 3 moduri, și anume: 1. prin completarea de către entitatea raportoare a coloanelor 1-56 în interfața portalului, caz în care fișierul este generat automat de către portal. La completarea RTE în interfața portalului, coloanele 1 și 2 din fișier se preiau automat, iar coloanele 4, 12, 38, 44 și 53 se completează de către entitatea raportoare prin selecția din liste de valori predefinite.
Coloanele 3, 5, 8, 13-17, 20, 23, 26, 29, 33-35, 40, 41, 45, 52 și 55 se preiau automat în portal prin alegerea de către entitatea raportoare, pentru fiecare coloană, a unei valori dintr-o listă bazată pe nomenclatoarele de sedii secundare, pep, țări, forme juridice de organizare, coduri CAEN, județe, localități, tip cont, valute, respectiv tipuri operațiuni.
Coloanele 6, 7, 9-11, 18, 19, 21, 22, 24, 25, 27, 28, 30-32, 36, 37, 39, 42, 43, 46-51, 54 și 56 se completează propriu-zis de către entitatea raportoare în portal.
În portal, fiecărui raport RTE_zzllaaaa_cccccc.xlsx/.csv i se asociază automat un fișier de tip.pdf, cu caracter ilustrativ. În acest fișier, toate coloanele care conțin coduri în raport sunt înlocuite cu rubrici în care este explicitată semnificația (descrierea) fiecărui cod, conform nomenclatoarelor aferente;
2. prin generarea de către entitatea raportoare a unui fișier agregat denumit RTE_zzllaaaa_cccccc.xlsx/.csv, având forma și conținutul descrise în acest capitol, extras din baza de date proprie, folosind proceduri specifice. Pentru completarea unor coloane din acest fișier sunt folosite nomenclatoarele enumerate în anexele nr. 1 și 2 la ordin, după cum urmează: a) cccccc.xlsx - nomenclatorul conține valorile admisibile pentru coloana 3 din RTE;
b)
Pep.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 5, 20, 26 și 45 din RTE;
c)
Tari.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 8, 15, 23, 29, 33 și 41 din RTE;
d)
Forme_jur.xlsx - nomenclatorul conține valorile admisibile pentru coloana 13 din RTE;
e)
Coduri_Caen.xlsx - nomenclatorul conține valorile admisibile pentru coloana 14 din RTE;
f)
Judete.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 16 și 34 din RTE;
g)
Loca.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 17 și 35 din RTE.
h)
Valute.xlsx - nomenclatorul conține valorile admisibile pentru coloana 52 din RTE;
i)
Tip_oper.xlsx - nomenclatorul conține valorile admisibile pentru coloana 55 din RTE.
În plus față de acestea, ONPCSB pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, nomenclatorul Tip_cont.xls, care conține valorile admisibile pentru coloana 40 din RTE;
3. prin colectarea de către entitatea raportoare a transferurilor externe care fac obiectul raportării din propriul sistem informatic, în forma și conținutul descrise în acest capitol, și folosirea unui serviciu web dedicat, pus la dispoziție de către ONPCSB pentru schimbul de date. De asemenea, ONPCSB pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, un format de RTE cu caracter ilustrativ: fișierul RTE_zzllaaaa_cccccc.xlsx.
