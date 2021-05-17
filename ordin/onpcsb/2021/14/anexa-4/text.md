# Anexa nr. 4
FORMA ȘI CONȚINUTUL rapoartelor privind transferurile de fonduri pentru activitatea de remitere de bani a căror limită minimă reprezintă echivalentul în lei a 2.000 euro
I.
Aspecte introductive Prezentele dispoziții se aplică exclusiv instituțiilor emitente de monedă electronică și instituțiilor de plată persoane juridice române, precum și punctelor unice de contact stabilite pe teritoriul României pentru instituțiile emitente de monedă electronică și instituțiile de plată persoane juridice străine, conform prevederilor art. 8 alin. (11^1) din Legea nr. 129/2019 pentru prevenirea și combaterea spălării banilor și finanțării terorismului, precum și pentru modificarea și completarea unor acte normative, cu modificările și completările ulterioare (denumită în continuare lege).
Raportul privind transferurile de fonduri pentru activitatea de remitere de bani a căror limită minimă reprezintă echivalentul în lei a 2.000 euro (denumit în continuare RTF) este un fișier în format structurat (.dbf), denumit cccccczzllaaaa_f.DBF, unde: - cccccc reprezintă codul entității raportoare, care este alocat fiecărei entități raportoare la înregistrarea în sistem;
- zzllaaaa reprezintă data la care se face raportarea - sub forma zi, lună, an;
- _f reprezintă identificatorul tipului de raport.
II.
Forma raportului privind transferurile de fonduri pentru activitatea de remitere de bani
Număr coloană Denumire coloană Tip Dimensiune Observații/Restricții 1 data_rap Dată 10 setată în forma zz/ll/aaaa, unde zz = ziua, ll = luna, aaaa = anul 2 cod_r Numeric 6 3 tara_ag_p Numeric 3 cod din nomenclatorul Tari 4 cod_ag_p Numeric 6 cod din nomenclatorul de subunități 5 pep_p Numeric 1 cod din nomenclatorul Pep 6 nume_p Caracter 40 7 pren_p Caracter 30 8 cod_p Caracter 13 9 act_id_p Caracter 15 10 cet_p Numeric 3 cod din nomenclatorul Tari 11 data_n_p Dată 10 setată în forma zz/ll/aaaa 12 loca_n_p Caracter 50 13 tara_p Numeric 3 cod din nomenclatorul Tari 14 judet_p Numeric 2 cod din nomenclatorul Judete 15 loca_p Numeric 6 cod din nomenclatorul Loca 16 str_p Caracter 35 17 nr_p Caracter 5 18 sect_p Numeric 1 valori admisibile: 1 la 6 19 tara_ag_b Numeric 3 cod din nomenclatorul Tari 20 cod_ag_b Numeric 6 cod din nomenclatorul de subunități 21 pep_b Numeric 1 cod din nomenclatorul Pep 22 nume_b Caracter 40 23 pren_b Caracter 30 24 cod_b Caracter 13 25 act_id_b Caracter 15 26 cet_b Numeric 3 cod din nomenclatorul Tari 27 data_n_b Dată 10 setată în forma zz/ll/aaaa 28 loca_n_b Caracter 50 29 tara_b Numeric 3 cod din nomenclatorul Tari 30 judet_b Numeric 2 cod din nomenclatorul Judete 31 loca_b Numeric 6 cod din nomenclatorul Loca 32 str_b Caracter 35 33 nr_b Caracter 5 34 sect_b Numeric 1 valori admisibile: 1 la 6 35 cod_tr Caracter 15 36 data_op Dată 10 setată în forma zz/ll/aaaa 37 cod_val Caracter 3 cod din nomenclatorul Valute 38 suma_op Numeric 6 >=1 39 euro Numeric 6 >=1 40 observatii Caracter 200
III.
Conținutul raportului privind transferurile de fonduri pentru activitatea de remitere de bani RTF conține, conform prevederilor art. 7 alin. (5) din lege, transferurile de fonduri pentru activitatea de remitere de bani a căror limită minimă reprezintă echivalentul în lei a 2.000 euro. Toate transferurile de fonduri din ziua/perioada pentru care se face raportarea sunt incluse într-un singur RTF.
Pentru instituțiile emitente de monedă electronică și instituțiile de plată persoane juridice române, RTF conține operațiunile de transferuri de fonduri pentru activitatea de remitere de bani derulate atât prin agenții(le) proprii, cât și prin parteneri - persoane juridice române sau persoane juridice străine care nu au puncte unice de contact stabilite pe teritoriul României.
Pentru punctele unice de contact stabilite pe teritoriul României ale instituțiilor emitente de monedă electronică și ale instituțiilor de plată - persoane juridice străine, RTF conține operațiunile de transferuri de fonduri pentru activitatea de remitere de bani derulate prin agenții proprii sau parteneri, inclusiv prin agenții care sunt, la rândul lor, instituții emitente de monedă electronică sau instituții de plată persoane juridice române.
RTF conține următoarele categorii de informații: - data raportării și date de identificare ale entității raportoare (prestatorul de servicii de plată) și ale entității partenere (coloanele 1 la 4, 19 și 20);
- date de identificare și administrative ale plătitorului sumei transferate (coloanele 5 la 18);
- date de identificare și administrative ale beneficiarului plății sumei transferate (coloanele 21 la 34);
- date despre transferul de fonduri pentru activitatea de remitere de bani (coloanele 35 la 40).
Conținutul RTF este prezentat în detaliu în cele ce urmează, precizându-se și unele aspecte referitoare la obligativitatea și modul de completare a coloanelor indicate în forma raportului (punctul II): 1.
Coloana 1: „data_rap” conține data la care este raportat RTF, în format ZZ/LL/AAAA - zi/lună/an.
2.
Coloana 2: „cod_r” conține codul de identificare al entității raportoare, care este un număr secvențial obținut la înregistrarea acesteia în sistem.
3.
Coloana 3: „tara_ag_p” conține codul de identificare al țării unde se află sediul prestatorului de servicii de plată al plătitorului, fie agent al entității raportoare, fie partener al acesteia, conform nomenclatorului aferent.
4.
Coloana 4: „cod_ag_p” conține codul intern unic de identificare al prestatorului de servicii de plată al plătitorului, fie agent al entității raportoare, fie partener al acesteia.
5.
Coloana 5: „pep_p” se referă la statutul de „persoană expusă public” al plătitorului sumei transferate (denumit în continuare plătitor), în sensul prevăzut de art. 3 alin. (1) din lege. Coloana conține codul de identificare al funcției publice importante [menționate la art. 3 alin. (2) din lege] pe care o ocupă plătitorul, conform nomenclatorului aferent.
6.
Coloana 6: „nume_p” conține numele de familie al plătitorului, așa cum este înscris în documentul de identitate.
7.
Coloana 7: „pren_p” conține prenumele întreg al plătitorului, așa cum este înscris în documentul de identitate.
8.
Coloana 8: „cod_p” conține codul numeric personal al plătitorului, așa cum este înscris în documentul de identitate. În cazul în care plătitorul persoană fizică străină nu are cod numeric personal, în această coloană se completează numărul de identificare al plătitorului, conform art. 4 alin. (1) pct. c) din Regulamentul (UE) nr. 847/2015.
9.
Coloana 9: „act_id_p” conține seria și numărul actului de identitate al plătitorului.
10.
Coloana 10: „cet_p” conține codul de identificare al țării corespunzătoare cetățeniei plătitorului, conform nomenclatorului aferent.
11.
Coloana 11: „data_n_p” conține, sub forma zi/lună/an, data nașterii plătitorului, așa cum este înscrisă în documentul de identitate.
12.
Coloana 12: „loca_n_p” conține locul nașterii plătitorului.
13.
Coloana 13: „tara_p” conține codul de identificare al țării de domiciliu/reședință a plătitorului, conform nomenclatorului aferent.
14.
Coloana 14: „judet_p” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința plătitorului, conform nomenclatorului aferent.
15.
Coloana 15: „loca_p” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința plătitorului, conform nomenclatorului aferent.
16.
Coloana 16: „str_p” conține denumirea străzii unde este situat(ă) domiciliul/reședința plătitorului. În cazul în care domiciliul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzătoare.
17.
Coloana 17: „nr_p” conține numărul aferent străzii unde este situat(ă) domiciliul/reședința plătitorului.
18.
Coloana 18: „sect_p” conține numărul sectorului unde este situat(ă) domiciliul/reședința plătitorului. Coloana se completează numai în cazul în care domiciliul/sediul plătitorului este în București. Valorile admisibile pentru această coloană sunt numerele întregi de la 1 la 6.
19.
Coloana 19: „tara_ag_b” conține codul de identificare al țării unde se află sediul prestatorului de servicii de plată al beneficiarului, fie agent al entității raportoare, fie partener al acesteia, conform nomenclatorului aferent.
20.
Coloana 20: „cod_ag_b” conține codul intern unic de identificare al prestatorului de servicii de plată al beneficiarului plății, fie agent al entității raportoare, fie partener al acesteia.
21.
Coloana 21: „pep_b” se referă la statutul de „persoană expusă public” al beneficiarului sumei transferate (denumit în continuare beneficiar), în sensul prevăzut de art. 3 alin. (1) din lege. Coloana conține codul de identificare al funcției publice importante [menționate la art. 3 alin. (2) din lege], pe care o ocupă beneficiarul, conform nomenclatorului aferent.
22.
Coloana 22: „nume_b” conține numele de familie al beneficiarului, așa cum este înscris în documentul de identitate.
23.
Coloana 23: „pren_b” conține prenumele întreg al beneficiarului, așa cum este înscris în documentul de identitate.
24.
Coloana 24: „cod_b” conține codul numeric personal al beneficiarului, așa cum este înscris în documentul de identitate. În cazul în care beneficiarul este persoană străină și nu are cod numeric personal, în această coloană se completează numărul de identificare al beneficiarului, conform art. 4 alin. (1) pct. c) din Regulamentul (UE) nr. 847/2015.
25.
Coloana 25: „act_id_b” conține seria și numărul actului de identitate al beneficiarului.
26.
Coloana 26: „cet_b” conține codul de identificare al țării corespunzătoare cetățeniei beneficiarului, conform nomenclatorului aferent.
27.
Coloana 27: „data_n_b” conține, sub forma zi/lună/an, data nașterii beneficiarului, așa cum este înscrisă în documentul de identitate.
28.
Coloana 28: „loca_n_b” conține locul nașterii beneficiarului.
29.
Coloana 29: „tara_b” conține codul de identificare al țării de domiciliu/reședință a beneficiarului, conform nomenclatorului aferent.
30.
Coloana 30: „județ_b” conține, dacă este cazul, codul de identificare al județului în care se află domiciliul/reședința beneficiarului, conform nomenclatorului aferent.
31.
Coloana 31: „loca_b” conține, dacă este cazul, codul de identificare al localității în care se află domiciliul/reședința beneficiarului, conform nomenclatorului aferent.
32.
Coloana 32: „str_b” conține denumirea străzii unde este situat(ă) domiciliul/reședința beneficiarului. În cazul în care domiciliul se află în străinătate, în această coloană se completează în plus și denumirea orașului/localității corespunzătoare.
33.
Coloana 33: „nr_b” conține numărul aferent străzii unde este situat domiciliul/reședința beneficiarului.
34.
Coloana 34: „sect_b” conține numărul sectorului unde este situat(ă) domiciliul/reședința beneficiarului. Coloana se completează numai în cazul în care domiciliul beneficiarului este în București. Valorile admisibile pentru această coloană sunt numerele întregi de la 1 la 6.
35.
Coloana 35: „cod_tr” conține codul unic de identificare al tranzacției, așa cum este definit la art. 3 (11) din Regulamentul UE nr. 847/2015.
36.
Coloana 36: „data_op” conține data la care a fost efectuată operațiunea raportată, sub forma zi/lună/an.
37.
Coloana 37: „cod_val” conține codul de identificare al valutei corespunzătoare sumei plătite, conform nomenclatorului aferent.
38.
Coloana 38: „suma_op” conține suma plătită în cadrul transferului de fonduri, exprimată în valuta al cărei cod de identificare este completat în coloana 37. Dacă suma respectivă este un număr zecimal, aceasta se rotunjește.
39.
Coloana 39: „euro” conține echivalentul în euro al sumei completate în coloana 38, obținut folosind cursul de referință al Băncii Naționale a României din ziua în care s-a efectuat tranzacția. Dacă rezultatul aplicării cursului de referință este un număr zecimal, acesta se rotunjește.
40.
Coloana 40: „observatii” conține eventuale precizări suplimentare pe care le poate face entitatea raportoare în legătură cu transferul raportat. În cazul în care plătitorul sau beneficiarul are statut de PEP, în această coloană se completează datele și informațiile care au condus la încadrarea persoanei în respectiva categorie. În situația în care suma transferată a fost remisă beneficiarului la o dată diferită de data plății, această coloană conține obligatoriu data remiterii sumei, sub forma zi/lună/an.
În situația în care suma remisă beneficiarului este diferită de suma plătită, această coloană conține obligatoriu suma remisă, valuta corespunzătoare și echivalentul în euro al sumei remise.
Completarea cu date a coloanelor 1 la 40 din RTE este obligatorie, cu următoarele excepții: 1.
În cazul în care plătitorul nu are statut de PEP, coloana 5 nu se completează.
2.
Coloanele 14 și 30 nu se completează dacă valoarea aferentă coloanei 13, respectiv 29 corespunzătoare este alta decât 642 (România).
3.
Coloanele 14 și 30 nu se completează dacă valoarea aferentă coloanei 13, respectiv 29 corespunzătoare este 642 (România) și valoarea aferentă coloanei 15, respectiv 31 este 403 (București).
4.
În cazul în care beneficiarul nu are statut de PEP, coloana 5 nu se completează.
5.
În cazul în care coloana 11 nu este completată, completarea coloanelor 8, 9 și 13 la 18 este obligatorie.
6.
În cazul în care coloana 11 este completată, coloanele 8 la 10 și 13 la 18 sunt facultative.
7.
În cazul în care coloana 27 nu este completată, completarea coloanelor 24, 25 și 29 la 34 este obligatorie.
8.
În cazul în care coloana 27 este completată, coloanele 24, 25 și 29 la 34 sunt facultative.
9.
Pentru persoanele străine rezidente în România, în coloanele 13 la 18, respectiv 29 la 34 din fișier se completează cu prioritate adresa/sediul din România. Dacă aceste informații nu sunt disponibile, coloanele 13, 16 și 17, respectiv 29, 32 și 33 conțin adresa din străinătate a persoanei respective.
10.
Completarea coloanelor 10 și 12 este facultativă în cazul în care coloana 11 nu este completată.
11.
Completarea coloanelor 26 și 28 este facultativă în cazul în care coloana 27 nu este completată.
12.
La cele de mai sus se adaugă excepțiile prevăzute expres (în context) pentru fiecare coloană în paragraful privind conținutul RTF.
RTF este un fișier agregat, având forma și conținutul descrise în acest capitol, extras din baza de date a entității raportoare, folosind proceduri proprii. Acest fișier, denumit cccccczzllaaaa_f.DBF, se transmite prin sistem de către entitatea raportoare.
Pentru completarea unor coloane din acest fișier sunt folosite nomenclatoarele enumerate în anexa nr. 2 la ordin, după cum urmează:
a)
Tari.dbf - nomenclatorul conține valorile admisibile pentru coloanele 3, 10, 13, 19, 26 și 29 din RTF;
b)
Judete.dbf - nomenclatorul conține valorile admisibile pentru coloanele 14 și 30 din RTF;
c)
Loca.dbf - nomenclatorul conține valorile admisibile pentru coloanele 15 și 31 din RTF;
d)
Valute.dbf - nomenclatorul conține valorile admisibile pentru coloana 37 din RTF;
e)
Pep.dbf - nomenclatorul conține valorile admisibile pentru coloanele 5 și 21 din RTF;
f) cccccc.dbf - nomenclatorul de subunități - descris în anexa nr. 2, care conține valorile admisibile pentru coloanele 4 și 20 din RTF.
Nomenclatorul de subunități conține atât codurile de identificare ale tuturor agenți(i)lor entității raportoare, cât și ale instituțiilor de plată partenere ale acesteia, după caz. Nomenclatorul de subunități se gestionează în sistem de către entitatea raportoare.
Oficiul Național de Prevenire și Combatere a Spălării Banilor pune la dispoziția entităților raportoare, pe site-ul www.onpcsb.ro, un format de RTF: fișierul cccccczzllaaaa_f.DBF.
