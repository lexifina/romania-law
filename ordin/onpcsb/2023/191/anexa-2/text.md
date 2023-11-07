# Anexa nr. 2
FORMA ȘI CONȚINUTUL
Raportului de tranzacții cu numerar, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, inclusiv operațiunile care au o legătură între ele, pentru entități bancare și nonbancare
I.
Aspecte introductive Prezentele dispoziții se aplică entităților raportoare prevăzute la art. 5 coroborat cu art. 7 alin. (1) și (2) din Legea nr. 129/2019 pentru prevenirea și combaterea spălării banilor și finanțării terorismului, precum și pentru modificarea și completarea unor acte normative, cu modificările și completările ulterioare (lege).
Raportul de tranzacții cu numerar, în lei sau în valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, inclusiv operațiunile care au o legătură între ele (denumit în continuare RTN) este un fișier în format structurat (.xlsx/.csv), denumit RTN_zzllaaaa_cccccc.xlsx/.csv, unde: -
RTN reprezintă identificatorul tipului de raport;
- zzllaaaa reprezintă data la care se face raportarea - sub forma zi, lună, an;
- cccccc reprezintă codul entității raportoare, care este alocat fiecărei entități raportoare la înregistrarea în portal.
II.
Forma raportului de tranzacții cu numerar este ilustrată în tabelul următor:
Număr coloană Denumire coloană Tip Dimensiune Observații/Restricții 1 data_rap Dată 10 setată în forma zz/ll/aaaa, unde zz = ziua, ll = luna, aaaa = anul 2 cod _ent Numeric 6 3 cod_suc Numeric 6 cod din nomenclatorul de sedii secundare 4 tip_c Caracter 1 valori admisibile „F” sau „J” 5 pep_c Numeric 1 cod din nomenclatorul Pep 6 nume_c Caracter 50 7 pren_c Caracter 30 8 cet_c Numeric 3 cod din nomenclatorul Tari 9 cod_c Caracter 13 10 data_n_c Dată 10 setată în forma zz/ll/aaaa 11 act_id_c Caracter 15 12 f_jur Caracter 10 cod din nomenclatorul Forme_juridice_de_organizare 13 cod_Caen Numeric 4 cod din nomenclatorul Coduri_Caen 14 tara_c Numeric 3 cod din nomenclatorul Tari 15 judet_c Numeric 2 cod din nomenclatorul Judete 16 loca_c Numeric 6 cod din nomenclatorul Loca 17 str_c Caracter 50 18 nr_c Caracter 10 19 pep_i Numeric 1 cod din nomenclatorul Pep 20 nume_i Caracter 50 21 pren_i Caracter 30 22 cet_i Numeric 3 cod din nomenclatorul Tari 23 cod_i Caracter 13 24 data_n_i Dată 10 setată în forma zz/ll/aaaa 25 act_id_i Caracter 15 26 tara_i Numeric 3 cod din nomenclatorul Tari 27 judet_i Numeric 2 cod din nomenclatorul Judete 28 loca_i Numeric 6 cod din nomenclatorul Loca 29 str_i Caracter 50 30 nr_i Caracter 10 31 cont_tit Caracter 30 32 cod_tr Caracter 50 33 cod_tr_leg Caracter 50 34 data_op Dată 10 setată în forma zz/ll/aaaa 35 fel_op Caracter 1 valori admisibile „D” sau „R” 36 scop_op Caracter 6 cod din nomenclatorul Tip_oper 37 cod_valuta Caracter 3 cod din nomenclatorul Valute 38 suma_op Numeric 13 >= 1 39 euro Numeric 13 >= 1 40 observatii Caracter 200
III.
Conținutul raportului de tranzacții cu numerar RTN conține, conform prevederilor art. 7 alin. (1) din lege, tranzacțiile cu numerar, în lei sau valută, a căror limită minimă reprezintă echivalentul în lei a 10.000 euro, inclusiv operațiunile care au o legătură între ele. Toate tranzacțiile cu numerar din ziua/perioada pentru care se face raportarea sunt incluse într-un singur RTN.
RTN conține următoarele categorii de informații: - data raportării și identificarea entității raportoare (coloanele 1-3);
- date de identificare ale clientului entității raportoare (coloanele 4-18);
- date de identificare ale persoanei care a efectuat propriu-zis operațiunea raportată: împuternicit, delegat, reprezentant, mandatar al clientului (coloanele 19-30);
- date despre tranzacție (coloanele 31-40).
Conținutul RTN este prezentat în detaliu în cele ce urmează, precizându-se și unele aspecte referitoare la obligativitatea și modul de completare a coloanelor indicate în forma raportului (pct. II): 1.
Coloana 1: „data_rap” conține data la care este raportat RTN, în format ZZ/LL/AAAA - zi/lună/an.
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
Coloana 9: „cod_c” conține codul numeric personal, așa cum este înscris în documentul de identitate - pentru clienți persoane fizice, respectiv codul unic de înregistrare/codul de înregistrare fiscală, așa cum este înscris în certificatul de înregistrare - pentru clienți persoane juridice. În cazul în care clientul persoană fizică străină nu are cod numeric personal, această coloană nu se completează.
10.
Coloana 10: „data_n_c” conține, sub forma zi/lună/an, data nașterii clientului - persoană fizică străină, așa cum este înscrisă în documentul de identitate, respectiv data înregistrării/înmatriculării la autoritatea abilitată, așa cum este înscrisă în documentul de înregistrare - în cazul clientului persoană juridică. În cazul în care clientul este persoană fizică română al cărei cod numeric personal este completat în coloana anterioară, această coloană nu se completează. În caz contrar, completarea acestei coloane este obligatorie.
11.
Coloana 11: „act_id_c” conține seria și numărul actului de identitate pentru client persoană fizică, respectiv numărul de înregistrare/înmatriculare la autoritatea abilitată pentru client persoană juridică.
12.
Coloana 12: „f_jur” conține abrevierea formei de organizare a clientului - persoană juridică, așa cum este înscrisă în actul constitutiv (actualizat)/certificatul de înmatriculare. În cazul în care clientul este persoană fizică, această coloană nu se completează.
13.
Coloana 13: „cod_CAEN” conține codul CAEN al activității de bază a clientului - persoană juridică, așa cum este înscrisă în actul constitutiv (actualizat)/certificatul de înmatriculare. În cazul în care clientul este persoană fizică, această coloană nu se completează.
14.
Coloana 14: „tara_c” conține codul de identificare al țării de domiciliu/reședință a clientului - persoană fizică, respectiv al țării unde se află sediul clientului - persoană juridică.
15.
Coloana 15: „judet_c” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința clientului - persoană fizică, respectiv al județului unde se află sediul clientului - persoană juridică.
16.
Coloana 16: „loca_c” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința clientului - persoană fizică, respectiv al localității unde se află sediul clientului - persoană juridică.
17.
Coloana 17: „str_c” conține denumirea străzii unde este situat/situată domiciliul/reședința clientului - persoană fizică, respectiv a străzii unde se află sediul clientului - persoană juridică. În cazul în care domiciliul/sediul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzător/corespunzătoare.
18.
Coloana 18: „nr_c” conține numărul aferent străzii unde este situat/situată domiciliul/reședința clientului - persoană fizică, respectiv numărul străzii unde se află sediul clientului - persoană juridică.
19.
Coloana 19: „pep_i” conține un cod de identificare al categoriei în care se încadrează persoana care efectuează tranzacția, respectiv: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public.
20.
Coloana 20: „nume_i” conține numele persoanei care efectuează tranzacția, așa cum este înscris în documentul de identitate.
21.
Coloana 21: „pren_i” conține prenumele întreg al persoanei care efectuează tranzacția, așa cum este înscris în documentul de identitate.
22.
Coloana 22: „cet_i” conține codul de identificare al țării corespunzătoare cetățeniei persoanei care efectuează tranzacția.
23.
Coloana 23: „cod_i” conține codul numeric personal al persoanei care efectuează tranzacția, așa cum este înscris în documentul de identitate. În cazul în care persoana care efectuează tranzacția este străină și nu are cod numeric personal, această coloană nu se completează.
24.
Coloana 24: „data_n_i” conține, sub forma zi/lună/an, data nașterii persoanei care efectuează tranzacția, așa cum este înscrisă în documentul de identitate. În cazul în care persoana care efectuează tranzacția este cetățean român al cărei cod numeric personal este completat în coloana anterioară, această coloană nu se completează. În caz contrar, completarea acestei coloane este obligatorie.
25.
Coloana 25: „act_id_i” conține seria și numărul actului de identitate al persoanei care efectuează tranzacția.
26.
Coloana 26: „tara_i” conține codul de identificare al țării de domiciliu/reședință a persoanei care efectuează tranzacția.
27.
Coloana 27: „județ_i” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința persoanei care efectuează tranzacția.
28.
Coloana 28: „loca_i” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința persoanei care efectuează tranzacția.
29.
Coloana 29: „str_i” conține denumirea străzii unde este situat/situată domiciliul/reședința persoanei care efectuează tranzacția. În cazul în care domiciliul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzător/corespunzătoare.
30.
Coloana 30: „nr_i” conține numărul aferent străzii unde este situat/situată domiciliul/reședința persoanei care efectuează tranzacția.
31.
Coloana 31: „cont_tit” conține, în cazul în care operațiunea raportată implică mișcări într-un cont deschis pe numele clientului, numărul/codul (IBAN) sau simbolul acestui cont. În cazul în care operațiunea se desfășoară în baza unei relații contractuale, în această coloană se completează numărul de înregistrare și data contractului încheiat între entitatea raportoare și clientul respectiv.
În cazul în care entitatea raportoare autentifică un act prin care are loc operațiunea raportată, în această coloană se completează numărul și data cu care a fost autentificat actul respectiv.
În cazul în care operațiunea are loc prin casieria entității raportoare, în această coloană se completează simbolul contului contabil „Casa”.
32.
Coloana 32: „cod_tr” conține codul intern de identificare al tranzacției la entitatea raportoare Acest cod este stabilit de către entitatea raportoare și este unic pentru fiecare tranzacție. Dacă la nivelul entității raportoare nu există un cod unic de identificare al tranzacției, această coloană conține un cod agregat, format din codul entității raportoare însoțit de un număr secvențial (de la 1 la n) corespunzător fiecărei tranzacții, separate prin caracterul „_”.
33.
Coloana 33: „cod_tr_leg” conține, pentru operațiunile care au o legătură între ele [în sensul prevăzut la art. 2 lit. w) din lege] codul intern de identificare al tranzacției cu care a fost stabilită o legătură a tranzacției curente. Pentru completarea acestei coloane se au în vedere următoarele aspecte: - în situația în care se identifică două sau mai multe operațiuni care au o legătură între ele, se consideră operațiune de bază tranzacția cea mai veche din punct de vedere cronologic, ținând cont de data și, după caz, de ora, minutul etc. efectuării tranzacției respective;
- în mod convențional, pentru tranzacția de bază, în această coloană se preia din coloana 32 propriul cod intern de identificare;
- pentru toate celelalte operațiuni care au o legătură cu tranzacția de bază, această coloană conține codul intern de identificare al tranzacției de bază (valoarea coloanei 32 aferentă tranzacției de bază).
34.
Coloana 34: „data_op” conține data la care a fost făcută operațiunea, sub forma zi/lună/an.
35.
Coloana 35: „fel_op” conține felul operațiunii și are 2 valori admisibile și anume: „D” - pentru depunere de numerar/încasare de la client sau „R” - pentru retragere de numerar/plată către client. În mod convențional, în cazul operațiunilor de vânzare-cumpărare cu numerar, cumpărarea efectuată de către client este asimilată cu operațiunea de depunere (plată), respectiv vânzarea efectuată de către client este asimilată cu operațiunea de retragere (încasare).
36.
Coloana 36: „scop_op” conține codul de identificare al tipului de operațiune raportată.
37.
Coloana 37: „cod_valuta” conține codul de identificare al valutei corespunzătoare operațiunii raportate.
38.
Coloana 38: „suma_op” conține suma corespunzătoare operațiunii cu numerar, exprimată în valuta al cărei cod de identificare este completat în coloana 37. Dacă suma tranzacționată este un număr zecimal, aceasta se rotunjește la cel mai apropiat număr întreg. În cazul raportării operațiunilor care au o legătură între ele, dacă suma tranzacționată în una dintre operațiuni este subunitară, aceasta se rotunjește, în mod convențional, la valoarea 1.
39.
Coloana 39: „euro” conține echivalentul în euro al sumei completate în coloana 38, obținut folosind cursul de referință al Băncii Naționale a României din ziua în care s-a efectuat tranzacția. Dacă rezultatul aplicării cursului de referință este un număr zecimal, acesta se rotunjește la cel mai apropiat număr întreg. În cazul raportării operațiunilor care au o legătură între ele, dacă echivalentul euro aferent sumei tranzacționate în una dintre operațiuni este subunitar, acesta se rotunjește, în mod convențional, la valoarea 1.
40.
Coloana 40: „observatii” conține eventuale precizări suplimentare pe care le poate face entitatea raportoare în legătură cu tranzacția raportată. În cazul în care clientul sau persoana care efectuează operațiunea se încadrează în categoriile precizate în coloana 5 sau 19, în această coloană se completează datele și informațiile care au condus la încadrarea persoanei în respectiva categorie. Pentru operațiunile care au o legătură între ele, în această coloană se completează, în mod obligatoriu, elementele comune ale acestor operațiuni.
Completarea cu date a coloanelor 1-40 din RTN este obligatorie, cu următoarele excepții: 1)
În cazul în care clientul persoană fizică efectuează tranzacția în nume propriu, coloanele 19-30 nu se completează.
2)
În cazul în care clientul este persoană juridică sau este persoană fizică ce nu se încadrează în niciuna dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, coloana 5 nu se completează.
3)
În cazul în care persoana care efectuează tranzacția nu se încadrează în niciuna dintre categoriile: persoană expusă public, membru al familiei unei persoane expuse public sau persoană cunoscută ca asociat apropiat al unei persoane expuse public, coloana 19 nu se completează.
4)
Coloanele 15, 16, 27 și 28 nu se completează dacă valoarea aferentă coloanei 14, respectiv 26 corespunzătoare este alta decât 642 (România).
5)
Coloanele 15 și 27 nu se completează dacă valoarea aferentă coloanei 14, respectiv 26 corespunzătoare este 642 (România) și valoarea aferentă coloanei 16, respectiv 28 este 403 (București).
6)
La cele de mai sus se adaugă excepțiile prevăzute expres (în context), în paragraful privind conținutul RTN, pentru fiecare coloană.
Pentru completarea RTN se au în vedere următoarele reguli: 1)
Operațiunile de schimb valutar sunt incluse în RTN o singură dată, astfel: a) în coloana 35 „fel_op” se completează valoarea D;
b) în coloana 37 „cod valuta” se completează codul valutei sumei depuse de client în vederea efectuării schimbului;
c) în coloana 38 „suma_op” se completează suma de bani depusă de client în vederea efectuării schimbului;
d) în coloana 39 „euro” se completează echivalentul în euro, calculat la cursul Băncii Naționale a României, al sumei de bani depuse de client în vederea efectuării schimbului;
e) în coloana 40 „observatii” se completează obligatoriu suma primită de client din schimbul valutar, urmată de codul valutei corespunzătoare;
f) celelalte coloane se completează conform precizărilor din conținutul RTN.
2)
În cazul operațiunilor de vânzare-cumpărare cu numerar a unui bun deținut în comun de mai multe persoane - locuințe, terenuri etc., în fișier se completează, pentru fiecare persoană implicată în tranzacție, coloanele 1-37 conform precizărilor din conținutul RTN. Completarea celorlalte coloane se face după cum urmează: a) în coloana 38 „suma_op” se completează, pentru fiecare persoană, suma totală aferentă tranzacției;
b) în coloana 39 „euro” se completează, în mod convențional, valoarea obținută prin împărțirea echivalentului în euro, calculat la cursul Băncii Naționale a României, al sumei tranzacționate - coloana 38 - la numărul de persoane implicate de fiecare parte a tranzacției. Dacă rezultatul împărțirii este un număr zecimal, acesta se rotunjește la cel mai apropiat număr întreg;
c) în coloana 40 „observatii” se completează obligatoriu sintagma „efectuată în comun”.
3)
Pentru persoanele care au cetățenie dublă, în coloanele 8, respectiv 22 se completează cu prioritate cetățenia română. Celelalte informații despre cetățenia persoanei respective se completează în coloana 40.
4)
Pentru persoanele străine rezidente în România, în coloanele 14-18, respectiv 26-30 din fișier se completează cu prioritate adresa/sediul din România. Dacă aceste informații nu sunt disponibile, coloanele 14, 17 și 18, respectiv 26, 29 și 30 conțin adresa/sediul din străinătate a/al persoanei respective.
5)
La identificarea operațiunilor care au legătură între ele, pentru atingerea pragului de raportare (echivalentul în lei a 10.000 euro), se ține cont de felul operațiunii, respectiv depunere/retragere. Toate operațiunile care au legătură între ele sunt incluse într-un singur RTN, același cu fișierul care conține tranzacțiile a căror limită minimă reprezintă echivalentul în lei a 10.000 euro.
Fișierul denumit RTN_zzllaaaa_cccccc.xlsx/.csv, care este de fapt RTN, poate fi creat în 3 moduri, și anume: 1. prin completarea de către entitatea raportoare a coloanelor 1-40 în interfața portalului, caz în care fișierul este generat automat de către portal. La completarea RTN în interfața portalului, coloanele 1 și 2 din fișier se preiau automat, iar coloanele 4 și 35 se completează de către entitatea raportoare prin selecția din liste de valori predefinite.
Coloanele 3, 5, 8, 12-16, 19, 22, 26-28, 36 și 37 se preiau automat în portal prin alegerea de către entitatea raportoare, pentru fiecare coloană, a unei valori dintr-o listă bazată pe nomenclatoarele de sedii secundare, pep, țări, forme juridice de organizare, coduri CAEN, județe, localități, tipuri operațiuni, respectiv valute.
Coloanele 6, 7, 9-11, 17, 18, 20, 21, 23-25, 29-34 și 38-40 se completează propriu-zis de către entitatea raportoare în portal.
În portal, fiecărui raport RTN_zzllaaaa_cccccc.xlsx/.csv i se asociază automat un fișier de tip.pdf, cu caracter ilustrativ. În acest fișier, toate coloanele care conțin coduri în raport sunt înlocuite cu rubrici în care este explicitată semnificația (descrierea) fiecărui cod, conform nomenclatoarelor aferente;
2. prin generarea de către entitatea raportoare a unui fișier agregat denumit RTN_zzllaaaa_cccccc.xlsx /.csv, având forma și conținutul descrise în acest capitol, extras din baza de date proprie, folosind proceduri specifice. Pentru completarea unor coloane din acest fișier sunt folosite nomenclatoarele enumerate în anexa nr. 1 la ordin, după cum urmează: a) cccccc.xlsx - nomenclatorul conține valorile admisibile pentru coloana 3 din RTN;
b)
Pep.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 5 și 19 din RTN;
c)
Tari.xls - nomenclatorul conține valorile admisibile pentru coloanele 8, 14, 22 și 26 din RTN;
d)
Forme_jur.xlsx - nomenclatorul conține valorile admisibile pentru coloana 12 din RTN;
e)
Coduri_Caen.xlsx - nomenclatorul conține valorile admisibile pentru coloana 13 din RTN;
f)
Judete.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 15 și 27 din RTN;
g)
Loca.xlsx - nomenclatorul conține valorile admisibile pentru coloanele 16 și 28 din RTN. În acest nomenclator sunt cuprinse generic - ca denumire - toate localitățile din România, o singură dată. În cazul în care aceeași denumire corespunde în fapt mai multor localități, identificarea se face după codul județului completat în coloana de județ corespunzătoare;
h)
Valute.xlsx - nomenclatorul conține valorile admisibile pentru coloana 37 din RTN. În plus față de acestea, ONPCSB pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, nomenclatorul Tip_oper.xlsx, care conține valorile admisibile pentru coloana 36 din RTN;
3. prin colectarea de către entitatea raportoare a tranzacțiilor cu numerar care fac obiectul raportării din propriul sistem informatic, în forma și conținutul descrise în acest capitol, și folosirea unui serviciu web dedicat, pus la dispoziție de către ONPCSB pentru schimbul de date. De asemenea, ONPCSB pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, un format de RTN cu caracter ilustrativ: fișierul denumit RTN_zzllaaaa_cccccc.xlsx.
