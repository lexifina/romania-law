# Anexa
------ (Anexa nr. 1.4 la norme) ------------------------ Modalități de transmitere pe cale electronică a Declarațiilor privind evidența nominală a asiguraților și a obligațiilor de plată către bugetul asigurărilor sociale Condiții generale Declarațiile privind evidența nominală a asiguraților și a obligațiilor de plată către bugetul asigurărilor sociale se vor face numai pe suport electronic. Declarațiile în format electronic se depun odată cu declarațiile nominale pe suport de hârtie (ANEXA 1.1, ANEXA 1.2 listate la calculator, semnate și ștampilate), la Casa Teritorială de Pensii pe raza căreia se află sediul sau domiciliul angajatorului. Condiții tehnice standard pentru formatul electronic Declarațiile în format electronic vor fi transmise numai pe suport tip: dischetă FD 3,5" Microsoft DOS sau CD+ROM, în dublu exemplar. Suporturile vor fi etichetate cu informațiile următoare: - denumire fișier; - Codul unic de înregistrare sau codul fiscal al angajatorului, după caz; - numărul suportului magnetic în cadrul setului de suporturi ex: 1/3, 2/3, 3/3, dacă setul are 3 suporturi. Suportul magnetic va conține două fișiere de tip DBF sau TXT, (înregistrări de lungime fixă) pentru fiecare tip de declarație, care va avea în mod obligatoriu următoarele denumiri și conținut: A11.DBF sau A11.TXT - (ANEXA 1.1) conține datele aferente asiguraților A12.DBF sau A12.TXT - (ANEXA 1.2) conține datele totalizatoare ale fișierului A11.DBF sau A11.TXT Ordinea câmpurilor din structura fișierelor este obligatorie, indiferent dacă acestea se completează sau nu și sunt de lungime fixă. În descrierea de mai jos "Tip câmp" are următoarea semnificație: N - numeric, aliniat la dreapta C - caracter (alfanumeric), aliniat la stânga, fără:.......(semne diacritice). În situația transmiterii fișierelor tip DBF se va respecta obligatoriu denumirea câmpurilor date în structurile de fișier. Descrierea organizării înregistrărilor din fișiere: Fișierul A11.DBF sau A11.TXT (ANEXA 1.1) conține câte o înregistrare pentru fiecare asigurat și are următoarea structură:
Denumire câmp Tip câmp Lung. Explicații
Anul AN N 4 Se completează cu anul pentru care se întocmește declarația
Luna LN N 2 Se completează cu luna anului pentru care se întocmește declarația
Cod unic de înregistrare (CUI)/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/ codului fiscal atribuit angajatorilor - persoane juridice
Cod județ din Nr. de înmatriculare în Registrul Comerțului RJ C 3 Conține primele trei caractere din numărul de înmatriculare în Registrul Comerțului al angajatorului
Nr. de înregistrare din Registrul Comerțului RN N 5 Conține caracterele 4-8 din numărul de înmatriculare în Registrul Comerțului al angajatorului (nr. în RC)
Anul din Nr. de înmatriculare în Registrul Comerțului RA N 4 Conține ultimele patru caractere din numărul de înmatriculare în Registrul Comerțului al angajatorului
Nume și prenume asigurat NUME C 29 Conține numele și prenumele asiguratului
Cod asigurat CNP N 13 Conține codul numeric personal al asiguratului
Contract individual de muncă CM N 1 Se completează cu:
1 pentru asigurații cu contract de muncă cu normă întreagă, 0 în rest
Contract individual de muncă cu timp parțial CV N 1 Se completează cu:
1 pentru codificări anterioare
2 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 2 ore pe zi;
3 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 3 ore pe zi;
4 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 4 ore pe zi;
5 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 5 ore pe zi;
6 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 6 ore pe zi;
7 pentru asigurații care lucrează cu contract de muncă cu timp parțial, 7 ore pe zi;
0 în rest
Pensionar PE N 1 Se completează cu:
1 pentru codificări anterioare,
2 pentru pensionarii care lucrează cu contract de muncă cu timp parțial 2 ore pe zi;
3 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 3 ore pe zi;
4 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 4 ore pe zi;
5 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 5 ore pe zi;
6 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 6 ore pe zi;
7 pentru pensionarii care lucrează cu contract de muncă cu timp parțial, 7 ore pe zi;
8 pentru pensionarii cu contract de muncă cu normă întreagă; 0 în rest
Șomer SOM N 1 Se completează numai de ANOFM/AJOFM cu:
1 pentru beneficiarii de ajutor de șomaj;
2 pentru beneficiarii de alocație de sprijin;
3 pentru beneficiarii de plăți compensatorii;
4 pentru alte beneficii suportate din fondul de șomaj, potrivit legii;
0 în rest.
Total zile lucrate TT N 2 Conține suma zilelor lucrate și a zilelor în care asiguratul a beneficiat de prestații de asigurări sociale, inclusiv zilele nelucrate plătite din fondul de salarii și pentru care se achită contribuție de asigurări sociale, care nu poate fi mai mare decât numărul de zile lucrătoare din lună stabilit conform Legii nr. 53/2003 (Codul muncii)
Zile lucrate în condiții normale NN N 2 Conține număr zile lucrate de asigurat în condiții normale de muncă
Zile lucrate în condiții deosebite DD N 2 Conține număr zile lucrate de asigurat în condiții deosebite de muncă
Zile lucrate în condiții speciale SS N 2 Conține număr zile lucrate de asigurat în condiții speciale de muncă
Total zile prestații în condiții normale PP N 2 Conține numărul total de zile în care asiguratul a beneficiat de prestații de asigurări sociale în condiții normale de muncă (număr total zile lucrătoare aferente prestației acordate)
Total venit realizat de asigurat TV N 10 Conține venitul total realizat de asigurat
Venit realizat de asigurat în condiții normale TVN N 10 Conține venitul realizat de asigurat în condiții normale de muncă
Venit realizat de asigurat în condiții deosebite TVD N 10 Conține venitul realizat de asigurat în condiții deosebite de muncă
Venit realizat de asigurat în condiții speciale TVS N 10 Conține venitul realizat de asigurat în condiții speciale de muncă
CAS datorat de asigurat CASAT N 9 Conține Contribuția de asigurări sociale reținută de la asigurat
Total prestații de asigurări sociale CASTOT N 9 Conține cuantumul aferent prestațiilor de asigurări sociale, exclusiv ajutorul de deces
Prestații suportate din BASS BASS N 9 Conține cuantumul aferent prestațiilor de asigurări sociale suportat din Bugetul asigurărilor sociale de stat, exclusiv ajutorul de deces
Cod unic de înregistrare (CUI) angajator persoane fizice CNPA N 13 Conține Codul unic de înregistrare atribuit prin Certificatul de înregistrare a angajatorilor persoane fizice și care reprezintă codul numeric personal al angajatorului
Norma zilnică de lucru NORMA N 1 Se completează cu programul normal de lucru specific locului de muncă al asiguratului, exprimat în ore. Prin program normal de lucru se înțelege programul prevăzut la art. 109 alin. (1) din Legea nr. 53/2003 sau programul normal de lucru sub 8 ore stabilit cu respectarea prevederilor Legii nr. 31/1991 sau alin. (2) din art. 109 din Codul Muncii. Norma zilnică poate să fie de 8, 7 sau 6 ore.
Tipul declarației TIPD C 1 Se completează cu R pentru declarația rectificativă, spațiu în rest
Declarația rectificativă se completează astfel:
a. anexa a11 se completează numai pentru pozițiile modificate față de declarația inițială (înregistrările cu modificări față de declarația inițială, înregistrări noi față de declarația inițială)
b. anexa a12 se recalculează ținând cont de modificările efectuate față de declarația inițială.
Tip rectificare TIPR C 1 Se completează cu următoarele caractere:
M - modificare sume, zile, CNP sau nume asigurat pentru asigurații raportați anterior,
A - adăugare asigurat nou
S - ștergere asigurat existent în declarația anterioară
Nume înainte de rectificare NUMEANT C 29 Nume înainte de rectificare, se completează numai dacă se modifică numele (TIPR = M), spațiu în rest
CNP înainte de rectificare CNPANT N 13 CNP înainte de rectificare, se completează numai dacă se modifică CNP-ul (TIPR = M), 0 în rest
Total zile prestații în condiții speciale PPS N 2 Conține numărul total de zile lucrătoare corespunzătoare concediului medical pentru incapacitate temporară de muncă, în situația în care asiguratul a lucrat în ziua premergătoare concediului medical în condiții speciale de muncă.
(Nu se înregistrează zilele de concediu de maternitate, concediu creștere copil, concediu îngrijire copil sau prestații pentru prevenirea îmbolnăvirilor și recuperarea capacității de muncă, care sunt corespunzătoare în aceste situații condițiilor normale de muncă)
Total zile prestații în condiții deosebite PPD N 2 Conține numărul total de zile lucrătoare corespunzătoare concediului medical pentru incapacitate temporară de muncă, în situația în care asiguratul a lucrat în ziua premergătoare concediului medical în condiții deosebite de muncă.
(Nu se înregistrează zilele de concediu de maternitate, concediu creștere copil, concediu îngrijire copil sau prestații pentru prevenirea îmbolnăvirilor și recuperarea capacității de muncă, care sunt corespunzătoare în aceste situații condițiilor normale de muncă)
Zile prestații suportate din BASS PPBASS N 2 Zile lucrătoare prestații pentru cuantum prestații suportat din BASS
Zile prestații suportate din FAAMBP PPFAAMBP N 2 Zile lucrătoare prestații pentru cuantum prestații suportat din FAAMBP
Total cuantum prestații de asigurări sociale de suportat din Fondul pentru accidente de muncă și boli profesionale FAAMBP N 9 Conține total cuantum prestații de asigurări sociale de suportat din Fondul de accidente de muncă și boli profesionale.
Acest câmp este completat numai pentru Concediile medicale cauzate de accidente de muncă sau boli profesionale.
TT=NN+DD+SS+PP+PPD+PPS
PPBASS + PPFAAMBP <=PP+PPD+PPS
CASTOT >= BASS +FAAMBP
Fisierul A12.DBF sau A12.TXT (ANEXA 1.2) contine o singura înregistrare cu date centralizatoare referitoare la oblibațiile de plată ale angajatorului și are urmatoarea structura:
Denumire câmp Tip câmp Lung. Explicații
Anul AN N 4 Se completează cu anul pentru care se întocmește declarația
Luna LN N 2 Se completează cu luna anului pentru care se întocmește declarația
Ziua lichidării drepturilor salariale DCZZ N 2 Se completează cu ziua lichidării drepturilor salariale
Luna lichidării drepturilor salariale DCLL N 2 Se completează cu luna lichidării drepturilor salariale
Anul lichidării drepturilor salariale DCAA N 4 Se completează cu anul lichidării drepturilor salariale
Denumire angajator DEN C 29 Conține denumirea angajatorului
Cod unic de înregistrare CUI/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/cod fiscal atribuit angajatorilor - persoane juridice
Cod județ din Nr. de înmatriculare în Registrul Comerțului RJ C 3 Conține primele trei caractere din numărul de înmatriculare în Registrul Comerțului al angajatorului
Nr. de înregistrare din Registrul Comerțului RN N 5 Conține caracterele 4-8 din numărul de înmatriculare în Registrul Comerțului al angajatorului (nr. în RC)
Anul din Nr. de înmatriculare în Registrul Comerțului RA N 4 Conține ultimele patru caractere din numărul de înmatriculare în Registrul Comerțului al angajatorului
Număr mediu asigurați NRM N 8.2 Numărul mediu de asigurați se calculează cu 2 zecimale prin rotunjire matematică. Lungimea câmpului este 8.2 (5 cifre partea întreagă, respectiv 2 cifre partea zecimală)
Ex.: dacă din calcul rezultă 10,172895, atunci numărul mediu de asigurați este 10,17;
Dacă din calcul rezultă 10,175110, atunci numărul mediu de asigurați este 10,18 Începând cu 1.07.2005, numărul mediu de asigurați reprezintă media aritmetică simplă rezultată din suma efectivelor zilnice de asigurați din luna respectivă, indiferent de tipul contractului individual de muncă cu care sunt încadrați, exclusiv zilele de repaus săptămânal și de sărbători legale, raportat la numărul total de zile lucrătoare din luna, stabilit conform Legii nr. 53/2003 La stabilirea numărului mediu de asigurați se iau în considerare numai perioadele pentru care se datorează contribuția de asigurări sociale, conform legii.
NRM = SUMĂ(NN+DD+SS)/Nr. zile lucrătoare din lună
Această formulă este valabilă și pentru perioada 1.04.2001 - 28.02.2003.
Pentru perioada 01.03.2003 - 30.06.2005 se păstrează vechea formulă de calcul.
Formula de calcul a nr. mediu asigurați pentru perioada 01.03.2003 - 30.06.2005
Notatii:
A= Norma zilnica 1
B= Norma zilnica 2
C= Norma zilnica 3 Σ (Suma) se calculeaza după numar zile lucrate.
Formula pentru calculul numărului mediu de asigurați este:
NRM = [SUMĂ(Nr. asigurați cu contract de muncă cu normă întreagă * A * Zile lucrate) + + SUMĂ(Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile lucrate) +....... + + SUMĂ(Nr. Asigurați cu contract de muncă cu timp parțial * 7 ore * Nr. Zile lucrate)]/(Zile lucrătoare din lună * A)] + [SUMĂ(Nr. asigurați cu contract de muncă cu normă întreagă * B * Zile lucrate) + SUMĂ(Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile lucrate) +.... + SUMĂ(Nr. Asigurați cu contract de muncă cu timp parțial * 6 ore * Zile lucrate)]/(Nr. Zile lucrătoare din lună * B) + [SUMĂ(Nr. asigurați cu contract de muncă cu normă întreagă * C * Zile lucrate) + SUMĂ(Nr. Asigurați cu contract de muncă cu timp parțial * 2 ore * Zile lucrate) +.... + SUMĂ(Nr. Asigurați cu contract de muncă cu timp parțial * 5 ore * Zile lucrate)]/(Zile lucrătoare din lună * C)
Norma zilnică poate să fie de 8, 7 sau 6 ore (câmpul NORMĂ).
Ex.:
Norma 1 = 8 ore
Norma 2 = 7 ore
O firma are 9 angajați în luna martie 2003, din care:
- cu norma 1 3 angajați lucreaza 21 zile 1 angajat lucreaza 10 zile și 11 zile este în concediu medical 1 angajat lucreaza 21 zile cu contract de muncă cu timp parțial 3 ore 1 angajat lucreaza 18 zile cu contract de muncă cu timp parțial 2 ore
- cu norma 2 1 angajat lucreaza 21 zile 1 angajat lucreaza 15 zile și 6 zile este în concediu medical 1 angajat lucreaza 21 zile cu contract de muncă cu timp parțial 4 ore
NRM=[(((3*8*21)+(1*8*10)+(1*3*21)+(1*2*18))/(21*8))+ (((1*7*21)+(1*7*15)+(1*4*21))/(21*7))] = 6.35
Rotunjirea aritmetica se efectueaza la rezultatul final
Total fond salarii brute realizate FS N 13 Conține total fond de salarii brute realizate pe unitate
Total salarii brute realizate în condiții normale muncă FSN N 13 Conține total salarii brute realizate în condiții normale de muncă
Total salarii brute realizate în condiții deosebite de muncă FSD N 13 Conține total salarii brute realizate în condiții deosebite de muncă
Total salarii brute realizate în condiții speciale de muncă FSS N 13 Conține total salarii brute realizate în condiții speciale de muncă
Total contribuții individuale de asigurări sociale de virat CASS N 13 Conține total Contribuție individuală de asigurări sociale de virat
Total CAS datorat de angajator CASAN N 13 Conține total Contribuție de asigurări sociale datorate de angajator
Total cuantum prestații de asigurări sociale de suportat din BASS BASS N 13 Conține total cuantum prestații de asigurări sociale de suportat din Bugetul asigurărilor sociale de stat, inclusiv ajutorul de deces
CASS conform art. 54 alin. 2 din OUG nr. 150/2002 (exclusiv accidente de muncă și boli profesionale) CASS145 N 13 Conține Contribuția de asigurări de sănătate aferente Concediilor medicale exclusiv concediile medicale aferente accidentelor de muncă și bolilor profesionale, conform art. 54 alin. 2 din O.U.G. nr. 150/2002
Total CAS angajator de virat CASVIR N 13 Conține total CAS angajator de virat
Formula de calcul pentru 2001-2003:
CASVIR = CASS + CASAN - BASS - CASS145
Formula de calcul pentru = 2004: CASVIR = CASAN - CASS145 - BASS
Formula de calcul pentru = 2005: CASVIR = CASAN - CASS145 - BASS
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
Contribuție asigurări pentru accidente de muncă și boli profesionale (art. 140 CAAMBP N 13 Conține contribuție asigurări pentru accidente de muncă și boli profesionale (art. 140 Legea nr. 346/2002 completată și modificată),
Legea nr. 346/2002)
Pentru anii 2003, 2004:
CAAMBP = ROUND(FS * 0.5/100,0)
Începând cu anul 2005:
CAAMBP = ROUND(FS * PCAMBP/100,0)
Localitatea (oraș, comună) A_LOCA C 21 Adresa sediu angajator - localitate (oraș sau comună)
- se completează obligatoriu
Strada (strada, satul) A_STR C 21 Adresa sediu angajator - strada sau sat
- dacă se completează orașul, se completează obligatoriu și strada
Număr A_NR C 7 Adresa sediu angajator - număr
Bloc A_BL C 5 Adresa sediu angajator - bloc
Scara A_SC C 4 Adresa sediu angajator - scara
Etaj A_ET C 2 Adresa sediu angajator - etaj
Apartament A_AP C 4 Adresa sediu angajator - apartament
Telefon TELEFON N 10 Telefon de legătură angajator
Județ A_JUD C 3 Adresa sediu angajator - Cod județ - se completează obligatoriu*
Sector A_SECT N 2 Adresa sediu angajator - sector (numai pentru București)
E-mail E_MAIL C 45 Adresa e-mail angajator
Tipul declarației TIPD C 1 Se completează cu R pentru declarația rectificativă, spațiu în rest.
Declarația rectificativă pentru anexa a12 se completează astfel:
- se recalculează a12 ținând cont de modificările efectuate în anexa a11 față de declarația inițială.
Nr. cazuri indemnizație pentru incapacitate temporară de muncă NRCAZB N 5 Nr. total cazuri indemnizație pentru incapacitate temporară de muncă la nivel de unitate, exclusiv pentru accidente de muncă și boli profesionale
Nr. cazuri accidente de muncă și boli profesionale NRCAZA N 5 Nr. total cazuri accidente de muncă și boli profesionale la nivel de unitate pentru anii (câmpul nu se mai folosește din anul 2005)
Nr. cazuri prevenire îmbolnăviri NRCAZP N 5 Nr. total cazuri prevenire îmbolnăviri la nivel de unitate = sumă de cazuri de:
- trecere temporară în altă muncă
- reducerea timpului de muncă
- carantină
Nr. cazuri sarcină și lăuzie NRCAZL N 5 Nr. total cazuri sarcină și lăuzie la nivel de unitate
Nr. cazuri îngrijire copil bolnav NRCAZI N 5 Nr. total cazuri îngrijire copil bolnav la nivel de unitate
Nr. cazuri creștere copil până la 2 ani/3 ani NRCAZC N 5 Nr. total cazuri creștere copil până la 2 ani/3 ani la nivel de unitate
Nr. cazuri ajutoare de deces NRCAZD N 5 Nr. total cazuri ajutoare de deces la nivel de unitate
Nr. cazuri indemnizație de risc maternal NRCAZR N 5 Nr. total cazuri cu indemnizație de risc maternal la nivel de unitate
Nr. total zile prestații indemnizație pentru incapacitate temporară de muncă NRPPB N 6 Nr. total zile lucrătoare indemnizație pentru incapacitate temporară de muncă la nivel de unitate din certificatele medicale
Nr. total zile prestații accidente de muncă și boli profesionale NRPPA N 6 Nr. total zile lucrătoare prestații accidente de muncă și boli profesionale, la nivel de unitate din certificatele medicale (câmpul nu se mai folosește din anul 2005)
Nr. total zile prestații prevenire îmbolnăviri NRPPP N 6 Nr. total zile lucrătoare prestații prevenire îmbolnăviri la nivel de unitate din certificatele medicale
Nr. total zile prestații sarcină și lăuzie NRPPL N 6 Nr. total zile lucrătoare prestații sarcină și lăuzie la nivel de unitate din certificatele medicale
Nr. total zile prestații îngrijire copil bolnav NRPPI N 6 Nr. total zile lucrătoare prestații îngrijire copil bolnav la nivel de unitate din certificatele medicale
Nr. total zile prestații creștere copil până la 2 ani/3 ani NRPPC N 6 Nr. total zile lucrătoare prestații creștere copil până la 2 ani/3 ani la nivel de unitate
Nr. total zile prestații indemnizație de risc maternal NRPPR N 6 Nr. total zile lucrătoare prestații indemnizație de risc maternal la nivel de unitate din certificatele medicale
Sumă prestații pentru indemnizație pentru incapacitate temporară de muncă suportate din BASS SUMAB N 12 Sumă prestații indemnizație pentru incapacitate temporară de muncă la nivel de unitate suportate din BASS
Sumă prestații pentru accidente de muncă și boli profesionale suportate din BASS SUMAA N 12 Sumă prestații pentru accidente de muncă și boli profesionale la nivel de unitate suportate din BASS (câmpul nu se mai folosește din anul 2005)
Sumă prestații pentru prevenire îmbolnăviri suportate din BASS SUMAP N 12 Sumă prestații pentru prevenire îmbolnăviri la nivel de unitate suportate din BASS
Sumă prestații pentru sarcina și lăuzie suportate din BASS SUMAL N 12 Sumă prestații pentru sarcină și lăuzie la nivel de unitate suportate din BASS
Sumă prestații pentru îngrijire copil bolnav suportate din BASS SUMAI N 12 Sumă prestații pentru îngrijire copil bolnav la nivel de unitate suportate din BASS
Sumă prestații pentru creștere copil până la 2 ani/3 ani suportate din BASS SUMAC N 12 Sumă prestații pentru creștere copil până la 2 ani/3 ani la nivel de unitate suportate din BASS
Sumă ajutoare de deces suportată din BASS SUMAD N 12 Sumă totală ajutoare de deces la nivel de unitate suportate din BASS
Sumă prestații pentru indemnizație de risc maternal suportată din BASS SUMAR N 12 Sumă prestații pentru indemnizație de risc maternal la nivel de unitate suportate din BASS
Cod CAEN COD CAEN C 4 Se completează cu Codul CAEN al angajatorului conform nomenclatorului privind clasificarea activităților economice la nivel național
Total zile prestații pentru prestațiile de la pct. L1, L2, L3, L4, L5, L7, folosit la calcul contribuției de sănătate TPP N 6 Conține nr. total zile prestații (atât plătite de angajator cât și suportate din BASS)
Procent contribuție de asigurări pentru accidente de muncă și boli profesionale PCAMBP N 5(3) Procent contribuție de asigurări pentru accidente de muncă și boli profesionale, funcție de încadrarea în clasele de risc (cod CAEN)
Total zile prestații pentru prestațiile de la pct. P1, P2, P3, P4, folosit la calcul contribuției de sănătate TPPA N 6 Conține nr. total zile prestații pentru accidente de muncă și boli profesionale (atât plătite de angajator cât și suportate din FAAMBP)
CASS conform art. 54 alin. 2 din OUG nr. 150/2002, aferente accidentelor de muncă și bolilor profesionale CASS145A N 13 Conține Contribuția de asigurări de sănătate aferente Concediilor medicale cauzate de accidente de muncă și boli profesionale conform art. 54 alin. 2 din O.U.G. nr. 150/2002
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
Contribuție de asigurări pentru accidente de muncă și boli profesionale de virat FAMBPV N 13 Conține contribuția de asigurări pentru accidente de muncă și boli profesionale de virat FAMBPV = CAAMBP - PFAAMBP - CASS145A
Datorează contribuție pentru accidente de muncă și boli profesionale DATORAT N 1 Se completează astfel: 1 - datorează contribuție de accidente de muncă și boli profesionale 0 - nu datorează contribuție de accidente de muncă și boli profesionale (pentru angajatorii la care nu se aplică prevederile Legii nr. 346/2002 modificată și completată)
Total BASS din a11 = SUMAB+SUMAA+SUMAP+SUMAL+SUMAI+SUMAC+ SUMAR(SUMAA=0
începând cu anul 2005)
BASS din a12= SUMAB+SUMAA+SUMAP+SUMAL+SUMAI+SUMAC+ SUMAD+SUMAR (SUMAA=0
începând cu anul 2005)
Total PP +PPD+PPS din a11 = NRPPB+NRPPA+NRPPP+NRPPL+NRPPI+NRPPC+NRPPR +
NRPPIT + NRPPTT + NRPPRT + NRPPCC (NRPPA=0 din 2005)
TPP din a12 = NRPPB+ NRPPA+ NRPPP+ NRPPL+ NRPPI+ NRPPC + NRPPR (NRPPA=0
începând cu anul 2005)
TPPA din a12 = NRPPIT + NRPPTT + NRPPRT + NRPPCC
Total FAAMBP din a11 = SUMAIT+SUMATT+SUMART+SUMACC
PFAAMBP din a12 = SUMAIT+SUMATT+SUMART+SUMACC
Total FAAMBP din a11 = PFAAMBP din a12
versiunea anterioara a programului)
*Codurile de judete
Cod judet
Denumire judet
011
Alba
021
Arad
031
Arges
041
Bacau
051
Bihor
061
Bistrita
071
Botosani
081
Brasov
091
Braila
101
Buzau
111
Caras Severin
121
Cluj
131
Constanta
141
Covasna
151
Dambovita
161
Dolj
171
Galați
181
Gorj
191
Harghita
201
Hunedoara
211
Ialomita
221
Iasi
231
Giurgiu
241
Maramures
251
Mehedinti
261
Mures
271
Neamt
281
Olt
291
Prahova
301
Satu Mare
311
Salaj
321
Sibiu
331
Suceava
341
Teleorman
351
Timiș
361
Tulcea
371
Vaslui
381
Valcea
391
Vrancea
401
Calarasi
411
București
471
Ilfov
----------
