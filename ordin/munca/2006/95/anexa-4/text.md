# Anexa nr. 4
Anexa 4 (Anexa nr. 1.4 la norme) ------------------------ Modalități de transmitere pe cale electronică a Declaratiilor privind evidenta nominala a asiguratilor și a obligațiilor de plată către bugetul asigurarilor sociale Condiții generale Declaratiile privind evidenta nominala a asiguratilor și a obligațiilor de plată către bugetul asigurarilor sociale de stat se vor face numai pe suport electronic. Declaratiile în format electronic se depun odata cu declaratiile nominale pe suport de hartie (ANEXA 1.1, ANEXA 1.2 listate la calculator, semnate și stampilate), la Casa Teritoriala de Pensii pe raza careia se afla sediul sau domiciliul angajatorului. Condiții tehnice standard pentru formatul electronic Declaratiile în format electronic vor fi transmise numai pe suport tip: discheta FD 3,5" Microsoft DOS sau CD+ROM, în dublu exemplar. Suporturile vor fi etichetate cu informațiile urmatoare: - denumire fisier; - Codul unic de înregistrare sau codul fiscal al angajatorului, după caz; - numărul suportului magnetic în cadrul setului de suporturi ex: 1/3, 2/3, 3/3, dacă setul are 3 suporturi. Suportul magnetic va contine doua fisiere de tip DBF sau TXT, (înregistrări de lungime fixa) pentru fiecare tip de declaratie, care va avea în mod obligatoriu urmatoarele denumiri și continut: A11.DBF sau A11.TXT - (ANEXA 1.1) contine datele aferente asiguratilor A12.DBF sau A12.TXT - (ANEXA 1.2) contine datele totalizatoare ale fisierului A11.DBF sau A11.TXT Ordinea campurilor din structura fisierelor este obligatorie, indiferent dacă acestea se completeaza sau nu și sunt de lungime fixa. În descrierea de mai jos "Tip camp" are urmatoarea semnificație: N - numeric, aliniat la dreapta C - caracter (alfanumeric), aliniat la stanga, fără:.......(semne diacritice). În situația transmiterii fisierelor tip DBF se va respecta obligatoriu denumirea campurilor date în structurile de fisier. Descrierea organizarii înregistrărilor din fisiere: Fisierul A11.DBF sau A11.TXT (ANEXA 1.1) contine cate o înregistrare pentru fiecare asigurat și are urmatoarea structura:
Denumire câmp Tip câmp Lung. Explicații
Anul AN N 4 Se completează cu anul pentru care se întocmește declarația
Luna LN N 2 Se completează cu luna anului pentru care se întocmește declarația
Cod unic de înregistrare (CUI)/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/codului fiscal atribuit angajatorilor - persoane juridice
Cod județ din Nr. de înmatriculare în Registrul comerțului RJ C 3 Conține primele trei caractere din numărul de înmatriculare în registrul Comerțului al angajatorului
Nr. de înregistrare din Registrul Comerțului RN N 5 Conține caracterele 4-8 din numărul de înmatriculare în registrul comerțului al angajatorului (nr. în RC)
Anul din Nr. de înmatriculare în Registrul comerțului RA N 4 Conține ultimele patru caractere din numărul de înmatriculare în registrul Comerțului al angajatorului
Nume și prenume asigurat NUME C 29 Conține numele și prenumele asiguratului
Cod asigurat CNP N 13 Conține codul numeric personal al asiguratului
Contract individual de CM N 1 Se completează cu:
muncă
1 pentru asigurații cu contract de muncă cu normă întreagă;
Începând cu raportarea aferentă lunii ianuarie 2006
2 pentru raportarea efectuată de Casele de sănătate pentru asigurații beneficiari O.U.G. nr. 158/2005 - art. 1 alin. (2), art. 23 alin. (2) și art. 32 alin. (1) și (2);
0 în rest.
Contract individual de CV N 1 Se completează cu:
muncă cu timp parțial
1 pentru codificări anterioare;
2 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 2 ore pe zi;
3 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 3 ore pe zi;
4 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 4 ore pe zi;
5 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 5 ore pe zi;
6 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 6 ore pe zi;
7 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 7 ore pe zi;
0 în rest.
Pensionar PE N 1 Se completează cu:
1 pentru codificări anterioare;
2 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 2 ore pe zi;
3 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 3 ore pe zi;
4 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 4 ore pe zi;
5 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 5 ore pe zi;
6 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 6 ore pe zi;
7 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 7 ore pe zi;
8 pentru pensionarii cu contract de muncă cu normă întreagă;
0 în rest.
Șomer SOM N 1 Se completează numai de ANOFM/AJOFM cu:
1 pentru beneficiarii de ajutor de șomaj;
2 pentru beneficiarii de alocație de sprijin;
3 pentru beneficiarii de plăți compensatorii;
4 pentru alte beneficii suportate din fondul de șomaj, potrivit legii;
0 în rest.
Total zile TT N 2 Conține suma zilelor lucrate și a zilelor în care asiguratul a beneficiat de indemnizații prevăzute de O.U.G. nr. 158/2005, de prestații prevăzute de Legea nr. 346/2002 și respectiv, de prestații de asigurări sociale conform Legiinr. 19/2000, în cazul declarațiilor rectificative anterioare datei de 01.01.2006, cu respectarea termenului general de prescripție (3 ani). De asemenea, se includ și zilele nelucrate plătite din fondul de salarii și pentru care se achită contribuție de asigurări sociale. Total zile nu poate fi mai mare decât numărul de zile lucrătoare din lună stabilit conform Legii nr. 53/2003 (Codulmuncii)
Zile lucrate în condiții normale NN N 2 Conține număr zile lucrate de asigurat în condiții normale de muncă
Zile lucrate în condiții deosebite DD N 2 Conține număr zile lucrate de asigurat în condiții deosebite de muncă
Zile lucrate în condiții speciale SS N 2 Conține număr zile lucrate de asigurat în condiții speciale de muncă
Total zile indemnizații în condiții normale PP N 2 Conține numărul total de zile în care asiguratul a beneficiat de indemnizații prevăzute de O.U.G. 158/2005, de prestații prevăzute de Legea nr. 346/2002 și respectiv, de prestații de asigurări sociale conform Legii nr. 19/2000, în cazul declarațiilor rectificative anterioare datei de 1.01.2006, cu respectarea termenului general de prescripție (3 ani).
(număr total zile lucrătoare aferente prestației și/sau indemnizației acordate)
Total venit realizat de asigurat TV N 10 Conține venitul total realizat de asigurat
Venit realizat de asigurat în condiții normale TVN N 10 Conține venitul realizat de asigurat în condiții normale de muncă
Venit realizat de asigurat în condiții deosebite TVD N 10 Conține venitul realizat de asigurat în condiții deosebite de muncă
Venit realizat de asigurat în condiții speciale TVS N 10 Conține venitul realizat de asigurat în condiții speciale de muncă
CAS datorat de asigurat CASAT N 9 Începând cu raportarea aferentă lunii ianuarie 2006
Conține Contribuția de asigurări sociale reținută de la asigurat;
Cota CAS asigurat se aplică la venitul realizat pentru perioada lucrată plus baza de calcul a contribuției la BASS aferentă indemnizațiilor conform art. 45 din O.U.G. nr. 158/2005, proporțional cu nr. de zile de concediu medical pentru care se calculează CAS, suma plafonată la max. 5 salarii medii brute
- Dacă TV + BASS <= 5 * salariul mediu brut din Legea BASS:
CASAT = ROUND ((TV + BASS) * cota CAS asigurat/100,0),
- Dacă TV + BASS > 5 * salariul mediu brut din Legea BASS:
CASAT = ROUND (5 * salariul mediu brut din Legea BASS * cota CAS asigurat/100,0)
Pentru perioada de raportare 2001-2005
Conține Contribuția de asigurări sociale reținută de la asigurat pentru venitul realizat
Total venit asigurat din indemnizații/prestații CASTOT N 9 Începând cu raportarea aferentă lunii ianuarie 2006
Conține cuantumul indemnizației pentru incapacitate temporară de muncă cauzată de accident de muncă sau boală profesională plus baza de calcul a contribuției la BASS aferentă indemnizațiilor conform art. 45 din O.U.G. nr. 158/2005 (salariul de bază minim brut pe țară garantat în plată, proporțional cu nr. zile de indemnizație pentru care se calculează CAS), conform legilor în vigoare, exclusiv ajutorul de deces.
Pentru perioada de raportare 2001-2005
Conține cuantumul aferent prestațiilor de asigurări sociale, exclusiv ajutorul de deces, aplicabil doar în cazul declarațiilor rectificative anterioare datei de 1.01.2006
Baza de calcul a contribuției la BASS BASS N 9 Începând cu raportarea aferentă lunii ianuarie 2006
aferentă indemnizațiilor conform art. 45 din O.U.G. 158/2005, proporțional cu nr. zile de indemnizație
Conține cuantumul rezultat din salariul de bază minim brut pe țară garantat în plată proporțional cu nr. zile de indemnizație, exclusiv ajutorul de deces.
pentru care se calculează
Pentru perioada de raportare 2001-2005
CAS (fost Prestații suportate din BASS)
Conține cuantumul aferent prestațiilor de asigurări sociale suportat din Bugetul asigurărilor sociale de stat, exclusiv ajutorul de deces, aplicabil doar în cazul declarațiilor rectificative anterioare datei de 1.01.2006
Cod unic de înregistrare (CUI) angajator persoane fizice CNPA N 13 Conține Codul unic de înregistrare atribuit prin Certificatul de înregistrare angajatorilor persoane fizice și care reprezintă codul numeric personal al angajatorului
Norma zilnică de lucru NORMA N 1 Se completează cu programul normal de lucru specific locului de muncă al asiguratului, exprimat în ore. Prin program normal de lucru se înțelege programul prevăzut la art. 109 alin. (1) din Legea nr. 53/2003sau programul normal de lucru sub 8 ore stabilit cu respectarea prevederilor Legii nr. 31/1991sau alin. (2) din art. 109 din Codul Muncii.
Norma zilnică poate să fie de 8, 7 sau 6 ore.
Tipul declarației TIPD C 1 Se completează cu R pentru declarația rectificativă, spațiu în rest.
Declarația rectificativă se completează astfel:
a. anexa a11 se completează numai pentru pozițiile modificate față de declarația inițială (înregistrările cu modificări față de declarația inițială, înregistrări noi față de declarația inițială);
b. anexa a12 se recalculează, ținând cont de modificările efectuate față de declarația inițială.
Tip rectificare TIPR C 1 Se completează cu următoarele caractere:
M - modificare sume, zile, CNP sau nume asigurat pentru asigurații raportați anterior;
A - adăugare asigurat nou;
S - ștergere asigurat existent în declarația anterioară.
Nume înainte de rectificare NUMEANT C 29 Nume înainte de rectificare, se completează numai dacă se modifică numele (TIPR = M), spațiu în rest
CNP înainte de rectificare CNPANT N 13 CNP înainte de rectificare, se completează numai dacă se modifică CNP-ul (TIPR = M), 0 în rest
Total zile indemnizații în condiții speciale PPS N 2 Conține numărul total de zile lucrătoare corespunzătoare concediului medical pentru incapacitate temporară de muncă, în situația în care asiguratul a lucrat în ziua premergătoare concediului medical în condiții speciale de muncă.
(Nu se înregistrează zilele de concediu de maternitate, concediu creștere copil, concediu îngrijire copil sau prestații pentru prevenirea îmbolnăvirilor și recuperarea capacității de muncă, care sunt corespunzătoare în aceste situații condițiilor normale de muncă)
Total zile indemnizații în condiții deosebite PPD N 2 Conține numărul total de zile lucrătoare corespunzătoare concediului medical pentru incapacitate temporară de muncă, în situația în care asiguratul a lucrat în ziua premergătoare concediului medical în condiții deosebite de muncă.
(Nu se înregistrează zilele de concediu de maternitate, concediu creștere copil, concediu îngrijire copil sau prestații pentru prevenirea îmbolnăvirilor și recuperarea capacității de muncă, care sunt corespunzătoare în aceste situații condițiilor normale de muncă)
Zile prestații suportate din BASS PPBASS N 2 Nu se mai completează începând cu raportarea aferentă lunii ianuarie 2006.
Pentru perioada de raportare 2001-2005
Zile lucrătoare prestații pentru cuantum prestații suportat din BASS
Zile prestații suportate din FAAMBP PPFAAMBP N 2 Zile lucrătoare prestații pentru cuantum prestații suportat din FAAMBP
Total cuantum prestații de asigurări sociale de suportat din Fondul pentru FAAMBP N 9 Conține total cuantum prestații de asigurări sociale de suportat din Fondul de accidente de muncă și boli profesionale.
accidente de muncă și boli profesionale
Acest câmp este completat numai pentru concediile medicale cauzate de accidente de muncă sau boli profesionale
Zile indemnizații pentru calculul CAS PPCAS N 2 Conține nr. zile indemnizații pentru care se calculează CAS, conform O.U.G. nr. 158/2005 art. 45
TT = NN+DD+SS+PP+PPD+PPS
PPBASS + PPFAAMBP <=PP+PPD+PPS, unde începând cu raportarea lunii ianuarie 2006 PPBASS=0
PPCAS+ PPFAAMBP <=PP+PPD+PPS începând cu raportarea lunii ianuarie 2006
CASTOT >= BASS+FAAMBP
Fisierul A12.DBF sau A12.TXT (ANEXA 1.2) contine o singura înregistrare cu date centralizatoare referitoare la oblibațiile de plată ale angajatorului și are urmatoarea structura:
Denumire câmp Tip câmp Lung. Explicații
Anul AN N 4 Se completează cu anul pentru care se întocmește declarația
Luna LN N 2 Se completează cu luna anului pentru care se întocmește declarația
Ziua lichidării drepturilor salariale DCZZ N 2 Se completează cu ziua lichidării drepturilor salariate
Luna lichidării drepturilor salariale DCLL N 2 Se completează cu luna lichidării drepturilor salariale
Anul lichidării drepturilor salariale DCAA N 4 Se completează cu anul lichidării drepturilor salariale
Denumire angajator DEN C 29 Conține denumirea angajatorului
Cod unic de înregistrare CUI/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/cod fiscal atribuit angajatorilor - persoane juridice
Cod județ din Nr. de înmatriculare în Registrul Comerțului RJ C 3 Conține primele trei caractere din numărul de înmatriculare în registrul comerțului al angajatorului
Nr. de înregistrare din Registrul Comerțului RN N 5 Conține caracterele 4-8 din numărul de înmatriculare în registrul comerțului al angajatorului (nr. în RC)
Anul din Nr. de înmatriculare în Registrul Comerțului RA N 4 Conține ultimele patru caractere din numărul de înmatriculare în registrul comerțului al angajatorului
Număr mediu asigurați NRM N 8.2 Numărul mediu de asigurați se calculează cu 2 zecimale prin rotunjire matematică. Lungimea câmpului este 8.2 (5 cifre partea întreagă, respectiv 2 cifre partea zecimală)
Ex.: dacă din calcul rezultă 10,172895, atunci numărul mediu de asigurați este 10,17;
Dacă din calcul rezultă 10,175110, atunci numărul mediu de asigurați este 10,18
Începând cu 1.07.2005, numărul mediu de asigurați reprezintă media aritmetică simplă rezultată din suma efectivelor zilnice de asigurați din luna respectivă, indiferent de tipul contractului individual de muncă cu care sunt încadrați, exclusiv zilele de repaus săptămânal și de sărbători legale, raportată la numărul total de zile lucrătoare din lună, stabilit conform Legiinr. 53/2003.
La stabilirea numărului mediu de asigurați se iau în considerare numai perioadele pentru care se datorează contribuția de asigurări sociale, conform legii.
NRM = SUMĂ(NN + DD + SS)/Nr. zile lucrătoare din lună
Această formulă este valabilă și pentru perioada 1.04.2001-28.02.2003.
Pentru perioada 01.03.2003-30.06.2005 se păstrează vechea formulă de calcul.
Formula de calcul a nr. mediu asigurați pentru perioada 01.03.2003 - 30.06.2005
Notații:
A = Norma zilnică 1
B = Norma zilnică 2
C = Norma zilnică 3
SUMA se calculează după număr zile lucrate.
Formula pentru calculul numărului mediu de asigurați este:
NRM = [SUMĂ (Nr. asigurați cu contract de muncă cu normă întreagă * A * Zile lucrate) + + SUMĂ (Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile lucrate) +..... + + SUMĂ (Nr. Asigurați cu contract de muncă cu timp parțial * 7 ore * Nr. Zile lucrate)]/ (Zile lucrătoare din lună * A)] +
[SUMĂ (Nr. asigurați cu contract de muncă cu normă întreagă * B * Zile lucrate) + SUMĂ (Nr.
Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile lucrate) +..... + SUMĂ (Nr.
Asigurați cu contract de muncă cu timp parțial * 6 ore * Zile lucrate)]/(Nr. Zile lucrătoare din lună * B)+
[SUMĂ (Nr. asigurați cu contract de muncă cu normă întreagă * C * Zile lucrate) + SUMĂ (Nr.
Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile lucrate) +..... + SUMĂ (Nr.
Asigurați cu contract de muncă cu timp parțial * 5 ore * Zile lucrate)]/(Zile lucrătoare din lună * C)
Norma zilnică poate să fie de 8, 7 sau 6 ore (câmpul NORMA).
Ex.:
Norma 1 = 8 ore
Norma 2 = 7 ore
O firmă are 9 angajați în luna martie 2003, din care:
- cu norma 1
3 angajați lucrează 21 zile
1 angajat lucrează 10 zile și 11 zile este în concediu medical
1 angajat lucrează 21 zile cu contract de muncă cu timp parțial 3 ore
1 angajat lucrează 18 zile cu contract de muncă cu timp parțial 2 ore
- cu norma 2
1 angajat lucrează 21 zile
1 angajat lucrează 15 zile și 6 zile este în concediu medical
1 angajat lucrează 21 zile cu contract de muncă cu timp parțial 4 ore
NRM = [(((3*8*21)+(1*8*10)+(1*3*21)+(1*2*18))/(21*8))+ (((1*7*21)+(1*7*15)+(1*4*21))/(21*7))] = 6.35
Rotunjirea aritmetică se efectuează la rezultatul final.
Total fond salarii brute realizate FS N 13 Conține total fond de salarii brute realizate pe unitate conform art. 24 din Legea nr. 19/2000
Total salarii brute realizate în condiții normale de muncă FSN N 13 Conține total salarii brute realizate în condiții normale de muncă
Total salarii brute realizate în condiții deosebite de muncă FSD N 13 Conține total salarii brute realizate în condiții deosebite de muncă
Total salarii brute realizate în condiții speciale de muncă FSS N 13 Conține total salarii brute realizate în condiții speciale de muncă
Total contribuții individuale de asigurări sociale de virat CASS N 13 Conține total Contribuție individuală de asigurări sociale de virat
Total CAS datorat de angajator CASAN N 13 Conține total Contribuție de asigurări sociale datorată de angajator.
Total cuantum prestații de asigurări sociale de suportat din BASS BASS N 13 Începând cu raportarea aferentă lunii ianuarie 2006
Conține numai cuantumul ajutorului de deces
Pentru perioada de raportare 2001-2005
Conține total cuantum prestații de asigurări sociale de suportat din
Bugetul asigurărilor sociale de stat, inclusiv ajutorul de deces
CASS conform art. 54 alin (2) din OUG nr. 150/2002 (exclusiv accidente de muncă și boli profesionale) CASS145 N 13 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Conține Contribuția de asigurări de sănătate aferente Concediilor medicale, exclusiv concediile medicale aferente accidentelor de muncă și bolilor profesionale, conform art. 54 alin. (2) din O.U.G. nr. 150/2002
Total CAS angajator de virat CASVIR N 13 Conține total CAS angajator de virat
Formula de calcul începând cu raportarea aferentă lunii ianuarie 2006:
CASVIR = CASAN - BASS
Formula de calcul pentru perioada aferentă anilor 2001-2003:
CASVIR = CASS + CASAN - BASS - CASS145
Formula de calcul pentru perioada aferentă anului 2004:
CASVIR = CASAN - CASS145 - BASS
Formula de calcul pentru perioada aferentă anului 2005:
CASVIR = CASAN - CASS145 - BASS
Număr total de file de la ANEXA 1.1 NRF N 3 Conține număr file de la ANEXA 1.1
Banca B1 C 16
Filiala F1 C 16
Cont C1 C 35
Banca B2 C 16
Filiala F2 C 16
Cont C2 C 35
Banca B3 C 16
Filiala F3 C 16
Cont C3 C 35
Banca B4 C 16
Filiala F4 C 16
Cont C4 C 35
Cod unic de înregistrare (CUI) pentru angajatori persoane fizice CNPA N 13 Conține Codul unic de înregistrare atribuit prin Certificatul de înregistrare angajatorilor persoane fizice și care reprezintă codul numeric personal al angajatorului
Contribuție asigurări pentru accidente de muncă și boli profesionale (art. 140 Legea 346/2002) CAAMBP N 13 Conține contribuție asigurări pentru accidente de muncă și boli profesionale (art. 140 Legea 346/2002 completată și modificată),
Pentru anii 2003, 2004:
CAAMBP = ROUND(FS*0.5/100,0)
Începând cu anul 2005:
CAAMBP = ROUND(FS*PCAMBP/100,0)
Localitatea (oraș, comună) A_LOCA C 21 Adresă sediu angajator - localitate (oraș sau comună)
- se completează obligatoriu
Strada (strada, satul) A_STR C 21 Adresă sediu angajator - stradă sau sat
- dacă se completează orașul, se completează obligatoriu și strada
Număr A_NR C 7 Adresă sediu angajator - număr
Bloc A_BL C 5 Adresă sediu angajator - bloc
Scară A_SC C 4 Adresă sediu angajator - scară
Etaj A_ET C 2 Adresă sediu angajator - etaj
Apartament A_AP C 4 Adresă sediu angajator - apartament
Telefon TELEFON N 10 Telefon de legătură angajator
Județ A_JUD C 3 Adresă sediu angajator - Cod județ
- se completează obligatoriu(
Sector A_SECT N 2 Adresă sediu angajator - sector (numai pentru București)
E-mail E_MAIL C 45 Adresă e-mail angajator
Tipul declarației TIPD C 1 Se completează cu R pentru declarația rectificativă, spațiu în rest.
Declarația rectificativă pentru anexa a12 se completează astfel:
- se recalculează a12 ținând cont de modificările efectuate în anexa a11 față de declarația inițială.
Nr. cazuri indemnizație pentru incapacitate temporară de muncă NRCAZB N 5 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Număr total cazuri indemnizație pentru incapacitate temporară de muncă la nivel de unitate, exclusiv pentru accidente de muncă și boli profesionale
Nr. cazuri accidente de muncă și boli profesionale NRCAZA N 5 Număr total cazuri accidente de muncă și boli profesionale la nivel de unitate (câmpul nu se mai folosește din anul 2005)
Nr. cazuri prevenire îmbolnăviri NRCAZP N 5 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Număr total cazuri prevenire îmbolnăviri la nivel de unitate = sumă de cazuri de:
- trecere temporară în altă muncă
- reducerea timpului de muncă
- carantină
Nr. cazuri sarcină și lăuzie NRCAZL N 5 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Număr total cazuri sarcină și lăuzie la nivel de unitate
Nr. cazuri îngrijire copil bolnav NRCAZI N 5 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Număr total cazuri îngrijire copil bolnav la nivel de unitate
Nr. cazuri creștere copil până la 2 ani/3 ani NRCAZC N 5 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total cazuri creștere copil până la 2 ani/3 ani la nivel de unitate
Nr. cazuri ajutoare de deces NRCAZD N 5 Nr. total cazuri ajutoare de deces la nivel de unitate
Nr. cazuri indemnizație de risc maternal NRCAZR N 5 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total cazuri cu indemnizație de risc maternal la nivel de unitate
Nr. total zile prestații indemnizație pentru incapacitate temporară de muncă NRPPB N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total zile lucrătoare indemnizație pentru incapacitate temporară de muncă la nivel de unitate din certificatele medicale
Nr. total zile prestații accidente de muncă și boli profesionale NRPPA N 6 Nr. total zile lucrătoare prestații accidente de muncă și boli profesionale, la nivel de unitate din certificatele medicale (câmpul nu se mai folosește din anul 2005)
Nr. total zile prestații prevenire îmbolnăviri NRPPP N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total zile lucrătoare prestații prevenire îmbolnăviri la nivel de unitate din certificatele medicale
Nr. total zile prestații sarcină și lăuzie NRPPL N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total zile lucrătoare prestații sarcină și lăuzie la nivel de unitate din certificatele medicale
Nr. total zile prestații îngrijire copil bolnav NRPPI N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total zile lucrătoare prestații îngrijire copil bolnav la nivel de unitate din certificatele medicale
Nr. total zile prestații creștere copil până la 2 ani/3 ani NRPPC N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total zile lucrătoare prestații creștere copil până la 2 ani/3 ani la nivel de unitate
Nr. total zile prestații indemnizație de risc maternal NRPPR N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Nr. total zile lucrătoare prestații indemnizație de risc maternal la nivel de unitate din certificatele medicale
Sumă prestații pentru indemnizație pentru incapacitate temporară de muncă suportate din BASS SUMAB N 12 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Sumă prestații indemnizație pentru incapacitate temporară de muncă la nivel de unitate suportate din BASS
Sumă prestații pentru accidente de muncă și boli profesionale suportate din BASS SUMAA N 12 Sumă prestații pentru accidente de muncă și boli profesionale la nivel de unitate suportate din BASS (câmpul nu se mai folosește din anul 2005)
Sumă prestații pentru prevenire îmbolnăviri suportate din BASS SUMAP N 12 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Sumă prestații pentru prevenire îmbolnăviri la nivel de unitate suportate din BASS
Sumă prestații pentru sarcină și lăuzie suportate din BASS SUMAL N 12 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Sumă prestații pentru sarcină și lăuzie la nivel de unitate suportate din BASS
Sumă prestații pentru îngrijire copil bolnav suportate din BASS SUMAI N 12 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Sumă prestații pentru îngrijire copil bolnav la nivel de unitate suportate din BASS
Sumă prestații pentru creștere copil până la 2 ani/3 ani suportate din BASS SUMAC N 12 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Sumă prestații pentru creștere copil până la 2 ani/3 ani la nivel de unitate suportate din BASS
Sumă ajutoare de deces suportată din BASS SUMAD N 12 Sumă totală ajutoare de deces la nivel de unitate suportate din BASS
Sumă prestații pentru indemnizație de risc maternal suportată din BASS SUMAR N 12 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
Pentru perioada de raportare 2001-2005
Sumă prestații pentru indemnizație de risc maternal la nivel de unitate suportate din BASS
Cod CAEN CODCAEN C 4 Se completează cu Codul CAEN al angajatorului conform nomenclatorului privind clasificarea activităților economice la nivel național
Total zile prestații pentru prestațiile de la pct. TPP N 6 Începând cu raportarea aferentă lunii ianuarie 2006 nu se mai completează
L1, L2, L3, L4, L5, L7, folosit la calcul contribuție sănătate
Pentru perioada de raportare 2001-2005
Conține nr. total zile prestații (atât plătite de angajator, cât și suportate din BASS)
Procent contribuție de asigurări pentru accidente de muncă și boli profesionale PCAMBP N 5(3) Procent contribuție de asigurări pentru accidente de muncă și boli profesionale, în funcție de încadrarea în clasele de risc (cod CAEN)
Total zile prestații pentru prestațiile de la pct. O1, O2, O3, O4 folosit la calcul contribuție sănătate TPPA N 6 Conține nr. total zile prestații pentru accidente de muncă și boli profesionale (atât plătite de angajator, cât și suportate din FAAMBP)
CASS conform art. 54 alin (2) din OUG nr. 150/2002, aferente accidentelor de muncă și bolilor profesionale CASS145A N 13 Conține Contribuția de asigurări de sănătate aferente Concediilor medicale cauzate de accidente de muncă și boli profesionale conform art. 54 alin. (2) din O.U.G. nr. 150/2002
CASS145A = ROUND (salariul minim brut pe țară * 2 * 6.5%/Nr. zile lucrătoare din luna de raportare) * Nr. total zile de indemnizație, 0)
Total cuantum prestații de asigurări sociale de suportat din Fondul de accidente de muncă și boli profesionale PFAAMBP N 13 Conține total cuantum prestații de asigurări sociale de suportat din Fondul de accidente de muncă și boli profesionale
Nr. cazuri indemnizație pentru incapacitate temporară de muncă cauzate de accidente de muncă și boli profesionale NRCAZIT N 5 Nr. total cazuri indemnizație pentru incapacitate temporară de muncă cauzate de accidente de muncă și boli profesionale la nivel de unitate
Nr. cazuri indemnizație pentru trecerea temporară în alt loc de muncă cauzate de accidente de muncă și boli profesionale NRCAZTT N 5 Nr. total cazuri indemnizație pentru trecerea temporară în alt loc de muncă cauzată de accidente de muncă și boli profesionale la nivel de unitate
Nr. cazuri indemnizație pentru reducerea timpului de lucru cauzate de accidente de muncă și boli profesionale NRCAZRT N 5 Nr. total cazuri indemnizație pentru reducerea timpului de lucru cauzată de accidente de muncă și boli profesionale la nivel de unitate
Nr. cazuri indemnizație pe durata cursurilor de calificare și reconversie profesională cauzate de accidente de muncă și boli profesionale NRCAZCC N 5 Nr. total cazuri indemnizație pe durata cursurilor de calificare și reconversie profesională cauzată de accidente de muncă și boli profesionale la nivel de unitate
Nr. total zile prestații indemnizație pentru incapacitate temporară de muncă cauzate de accidente de muncă și boli profesionale NRPPIT N 6 Nr. total zile lucrătoare prestații pentru incapacitate temporară de muncă cauzate de accidente de muncă și boli profesionale la nivel de unitate din certificatele medicale
Nr. total zile prestații pentru trecerea temporară în alt loc de muncă cauzate de accidente de muncă și boli profesionale NRPPTT N 6 Nr. total zile lucrătoare prestații pentru trecerea temporară în alt loc de muncă cauzată de accidente de muncă și boli profesionale la nivel de unitate din certificatele medicale
Nr. total zile prestații pentru reducerea timpului de lucru cauzate de accidente de muncă și boli profesionale NRPPRT N 6 Nr. total zile lucrătoare prestații pentru reducerea timpului de lucru cauzată de accidente de muncă și boli profesionale la nivel de unitate din certificatele medicale
Nr. total zile prestații pe durata cursurilor de calificare și reconversie profesională cauzate de accidente de muncă și boli profesionale NRPPCC N 6 Nr. total zile lucrătoare prestații pe durata cursurilor de calificare și reconversie profesională cauzată de accidente de muncă și boli profesionale la nivel de unitate din certificatele medicale
Sumă prestații pentru incapacitate temporară de muncă cauzată de accidente de muncă și boli profesionale, suportate din FAAMBP SUMAIT N 12 Sumă prestații pentru incapacitate temporară de muncă cauzate de accidente de muncă și boli profesionale la nivel de unitate suportate din FAAMBP
Sumă prestații pentru trecerea temporară în alt loc de muncă cauzate de accidente de muncă și boli profesionale, suportate din FAAMBP SUMATT N 12 Sumă prestații pentru trecerea temporară în alt loc de muncă cauzată de accidente de muncă și boli profesionale la nivel de unitate suportate din FAMMBP
Sumă prestații pentru reducerea timpului de lucru cauzate de accidente de muncă și boli profesionale, suportate din FAAMBP SUMART N 12 Sumă prestații pentru reducerea timpului de lucru cauzată de accidente de muncă și boli profesionale la nivel de unitate suportate din FAMMBP
Sumă prestații pe durata cursurilor de calificare și reconversie profesională cauzate de accidente de muncă și boli profesionale, suportate din FAAMBP SUMACC N 12 Sumă prestații pe durata cursurilor de calificare și reconversie profesională cauzată de accidente de muncă și boli profesionale la nivel de unitate suportate din FAAMBP
Contribuție de asigurări pentru accidente de muncă și boli profesionale de virat FAMBPV N 13 Conține contribuția de asigurări pentru accidente de muncă și boli profesionale de virat
FAMBPV = CAAMBP - PFAAMBP - CASS145A
Datorează contribuție pentru accidente de muncă și boli profesionale DATORAT N 1 Se completează astfel:
1 - datorează contribuție de accidente de muncă și boli profesionale
0 - nu datorează contribuție de accidente de muncă și boli profesionale (pentru angajatorii la care nu se aplică prevederile Legii 346/2002, modificată și completată)
TPPA din a12 = NRPPIT + NRPPTT + NRPPRT + NRPPCC
Total PP + PPS + PPD din a11 >= NRPPIT + NRPPTT + NRPPRT + NRPPCC
Total PPFAAMBP din a11 <= NRPPIT + NRPPTT + NRPPRT + NRPPCC
Total FAAMBP din a11 = SUMAIT + SUMATT + SUMART + SUMACC
PFAAMBP din a12 = SUMAIT + SUMATT + SUMART + SUMACC
Total FAAMBP din a11 = PFAAMBP din a12
*Codurile de judete
Cod județ Denumire județ
011 Alba
021 Arad
031 Argeș
041 Bacău
051 Bihor
061 Bistrița
071 Botoșani
081 Brașov
091 Brăila
101 Buzău
111 Caraș Severin
121 Cluj
131 Constanța
141 Covasna
151 Dâmbovița
161 Dolj
171 Galați
181 Gorj
191 Harghita
201 Hunedoara
211 Ialomița
221 Iași
231 Giurgiu
241 Maramureș
251 Mehedinți
261 Mureș
271 Neamț
281 Olt
291 Prahova
301 Satu Mare
311 Sălaj
321 Sibiu
331 Suceava
341 Teleorman
351 Timiș
361 Tulcea
371 Vaslui
381 Vâlcea
391 Vrancea
401 Călărași
411 București
471 Ilfov
