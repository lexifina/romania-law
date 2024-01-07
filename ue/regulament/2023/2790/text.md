REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2023/2790 AL COMISIEI
din 14 decembrie 2023
de stabilire a specificațiilor funcționale și tehnice pentru modulul de interfață de raportare al ghișeelor unice naționale în domeniul maritim
(Text cu relevanță pentru SEE)
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) 2019/1239 al Parlamentului European și al Consiliului din 20 iunie 2019 de stabilire a unui mediu aferent ghișeului unic european în domeniul maritim și de abrogare a Directivei 2010/65/UE (1), în special articolul 6 alineatul (1) și articolul 12 alineatul (4),
după consultarea Comitetului pentru facilitarea transportului și a comerțului digital,
întrucât:
(1) Specificațiile modulului de interfață de raportare trebuie să se bazeze pe o tehnologie ușor accesibilă, ușor de instalat și ușor de integrat în toate ghișeele unice naționale în domeniul maritim (Maritime National Single Windows, MNSW) și trebuie să permită o integrare și o întreținere fără probleme în viitor.
(2) Specificațiile funcționale și tehnice ale modulului de interfață de raportare trebuie să se bazeze pe orientările de proiectare privind modelul de arhitectură a soluțiilor pentru cerințele de interoperabilitate de înalt nivel (HL SAT), pentru a permite trasabilitatea între cerințele de interoperabilitate de nivel înalt și cele detaliate.
(3) Având în vedere că expeditorii utilizează sisteme de raportare diferite, iar MNSW-urile sunt implementate utilizând tehnologii diferite, modulul de interfață de raportare trebuie să fie construit cu ajutorul unor tehnologii care să permită schimbul de informații între sisteme de informații diferite care utilizează un protocol standardizat, permițând o interoperabilitate sporită.
(4) Obligațiile de raportare enumerate în anexa la Regulamentul (UE) 2019/1239 pot impune declaranților să transmită date cu caracter personal prin intermediul modulului de interfață de raportare, care trebuie să schimbe informații în așa fel încât toate datele cu caracter personal să fie prelucrate în conformitate cu Regulamentele (UE) 2018/1725 (2) și (UE) 2016/679 (3) ale Parlamentului European și ale Consiliului.
(5) Întrucât modulul de interfață de raportare este dezvoltat și actualizat de Comisie și distribuit statelor membre în vederea integrării, distribuirea de noi versiuni ale modulului de interfață de raportare, monitorizarea instalării corecte a software-ului și actualizarea ghidului de implementare a mesajelor trebuie gestionate la nivel central, ținând cont, acolo unde este posibil, de cerințele de securitate informatică ale MNSW-urilor.
(6) Pentru a garanta stabilitatea, securitatea și performanța modulului de interfață de raportare, statele membre trebuie să fie în măsură să monitorizeze traficul din rețea și să analizeze evenimentele, erorile și excepțiile sistemului, precum și să integreze aceste informații în sistemele și procesele lor de monitorizare existente. În acest scop, modulul de interfață de raportare trebuie să ofere funcționalități adecvate care să permită înregistrarea și stocarea evenimentelor și să furnizeze statelor membre informații privind traficul din rețea.
(7) Pentru a asigura un schimb de informații securizat prin intermediul modulului de interfață de raportare, expeditorii necesită autentificarea. În acest scop, sistemul comun de gestionare a accesului și a registrului utilizatorilor trebui să aibă drept componente-cheie un serviciu central de autentificare și un registru central. Aceste componente trebuie să funcționeze împreună pentru a permite autentificarea expeditorului în toate modulele de interfață de raportare, asigurând un mecanism de autentificare unificat.
(8) Pentru a face schimb de informații în condiții de siguranță utilizând modulul de interfață de raportare și pentru a asigura faptul că utilizatorii sunt recunoscuți la nivelul UE atunci când accesează oricare dintre modulele de interfață de raportare, expeditorii trebuie să obțină un certificat calificat pentru sigiliile electronice conform cu cerințele stabilite în Regulamentul (UE) nr. 910/2014 al Parlamentului European și al Consiliului (4).
(9) Pentru a oferi expeditorilor o înregistrare unică pentru schimbul de informații prin intermediul interfețelor de raportare armonizate în diferite state membre, statele membre trebuie să poată înregistra expeditorii în registrul central. Acest lucru ar trebui să reducă sarcina înregistrărilor multiple pentru operațiunile transfrontaliere în mai multe MNSW-uri. Toate datele cu caracter personal din registrul central trebuie gestionate în conformitate cu Regulamentele (UE) 2018/1725 și (UE) 2016/679.
(10) Pentru a reduce la minimum dependența statelor membre de serviciile centrale și având în vedere că MNSW-urile pot fi deja suportate de serviciile naționale de autentificare, statelor membre trebuie să li se permită, de asemenea, să își reutilizeze propriile servicii naționale de autentificare și propriile registre naționale pentru a autentifica expeditorii care doresc să utilizeze modulul de interfață de raportare, ca alternativă la sistemul de gestionare a accesului și a registrului utilizatorilor din cadrul mediului aferent ghișeului unic european în domeniul maritim (EMSWe).
(11) Pentru a permite statelor membre să integreze corect modulul de interfață de raportare și sistemul de gestionare a accesului și a registrului utilizatorilor în MNSW-uri, prezentul regulament trebuie să se aplice de la aceeași dată ca Regulamentul (UE) 2019/1239.
(12) Autoritatea Europeană pentru Protecția Datelor a fost consultată în conformitate cu articolul 42 alineatul (1) din Regulamentul (UE) 2018/1725 și a emis un aviz la 18 octombrie 2023,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Definiții
În sensul prezentului regulament, se aplică următoarele definiții:
1. „modul de interfață de raportare” înseamnă o componentă middleware a MNSW menționată la articolul 2 punctul 4 din Regulamentul (UE) 2019/1239;
2. „expeditor” înseamnă un declarant sau un furnizor de servicii de date care operează sistemul informatic și care trimite mesaje electronice către MNSW sau le primește prin intermediul modulului de interfață de raportare;
3. „formalitate” înseamnă formalitatea definită la articolul 1 din Regulamentul de punere în aplicare (UE) 2023/204 al Comisiei (5);
4. „AS4” înseamnă un protocol de mesaj bazat pe servicii web pentru schimbul securizat de mesaje între două părți;
5. „mesaj” înseamnă o reprezentare digitală a formalităților sau a mesajelor de răspuns utilizate pentru schimbul dintre expeditor și MNSW;
6. „punct de acces AS4” înseamnă un software de operare pentru servere compatibil cu protocolul de mesagerie AS4 și cu cerințele modulului de interfață de raportare, care permite transmiterea și primirea de informații în numele unui expeditor de la și către modulul de interfață de raportare;
7. „nucleu MNSW” înseamnă o componentă tehnică MNSW cu care este integrat modulul de interfață de raportare;
8. „validarea sintaxei” înseamnă procesul prin care se verifică dacă un mesaj electronic nu conține erori de programare, structurale sau stilistice;
9. „validare semantică” înseamnă un proces prin care se verifică conformitatea datelor cu normele specifice privind datele din cadrul unei formalități;
10. „ghid de implementare a mesajelor” înseamnă o specificație funcțională care stabilește standardele și mesajele care urmează să fie schimbate între expeditori și MNSW-uri prin intermediul modulului de interfață de raportare;
11. „înregistrare” înseamnă un proces prin care o persoană fizică sau juridică se identifică și creează un cont pe lângă autoritatea menționată la articolul 12 alineatul (2) din Regulamentul (UE) 2019/1239;
12. „identificare” înseamnă o identificare electronică în sensul definiției de la articolul 3 punctul 1 din Regulamentul (UE) nr. 910/2014;
13. „mijloc de identificare electronică” înseamnă o identificare electronică în sensul definiției de la articolul 3 punctul 2 din Regulamentul (UE) nr. 910/2014;
14. „autentificare” înseamnă o autentificare în sensul definiției de la articolul 3 punctul 5 din Regulamentul (UE) nr. 910/2014;
15. „certificat” înseamnă un certificat calificat pentru sigiliul electronic definit la articolul 3 punctul 30 din Regulamentul (UE) nr. 910/2014, emis de un prestator de servicii de încredere calificat, astfel cum este definit la articolul 3 punctul 20 din Regulamentul (UE) nr. 910/2014;
16. „număr EORI” înseamnă un număr de identificare, astfel cum este definit la articolul 1 punctul 18 din Regulamentul delegat (UE) 2015/2446 al Comisiei (6);
17. „sistem EMSWe de gestionare a accesului și a registrului utilizatorilor” înseamnă un sistem gestionat de Comisie care cuprinde un registru central și un serviciu central de autentificare și care asigură recunoașterea reciprocă a mijloacelor de identificare electronică și a autentificării pentru schimbul transfrontalier securizat de date între expeditori și MNSW-uri prin intermediul modulului de interfață de raportare;
18. „registru central” înseamnă un registru gestionat de Comisie care deține datele de înregistrare ale expeditorilor, furnizate de statele membre cu scopul de a facilita autentificarea expeditorilor;
19. „registru național” înseamnă un registru gestionat de un stat membru care deține date de înregistrare ale expeditorilor și care poate fi utilizat pentru a facilita autentificarea expeditorilor dacă aceștia se conformează cerințelor serviciului central de autentificare;
20. „serviciu central de autentificare” înseamnă un serviciu gestionat de Comisie care autentifică expeditorii ce utilizează modulul de interfață de raportare;
21. „serviciu național de autentificare” înseamnă un serviciu operat de un stat membru, care poate fi utilizat pentru autentificarea expeditorilor ce utilizează modulul de interfață de raportare.
Articolul 2
Modulul de interfață de raportare trebui să fir conform cu specificațiile funcționale și tehnice stabilite în partea I din anexă.
Pentru a contribui la integrarea modulului de interfață de raportare în MNSW-uri, Comisia, în strânsă colaborare cu coordonatorii naționali pentru EMSWe:
— definește orientări pentru testarea și configurarea modulului de interfață de raportare în vederea integrării în MNSW-urile respective;
— definește și întreține, cu asistență din partea Agenției Europene pentru Siguranță Maritimă, ghidul de implementare a mesajelor.
Articolul 3
Registrul central și serviciul central de autentificare se înființează conform specificațiilor tehnice, standardelor și procedurilor prevăzute în partea II din anexă.
Articolul 4
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Se aplică de la 15 august 2025.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 14 decembrie 2023.
Pentru Comisie
Președinta
Ursula VON DER LEYEN
(1) JO L 198, 25.7.2019, p. 64.
(2) Regulamentul (UE) 2018/1725 al Parlamentului European și al Consiliului din 23 octombrie 2018 privind protecția persoanelor fizice în ceea ce privește prelucrarea datelor cu caracter personal de către instituțiile, organele, oficiile și agențiile Uniunii și privind libera circulație a acestor date și de abrogare a Regulamentului (CE) nr. 45/2001 și a Deciziei nr. 1247/2002/CE (JO L 295, 21.11.2018, p. 39).
(3) Regulamentul (UE) 2016/679 al Parlamentului European și al Consiliului din 27 aprilie 2016 privind protecția persoanelor fizice în ceea ce privește prelucrarea datelor cu caracter personal și privind libera circulație a acestor date și de abrogare a Directivei 95/46/CE (Regulamentul general privind protecția datelor) (JO L 119, 4.5.2016, p. 1).
(4) Regulamentul (UE) nr. 910/2014 al Parlamentului European și al Consiliului din 23 iulie 2014 privind identificarea electronică și serviciile de încredere pentru tranzacțiile electronice pe piața internă și de abrogare a Directivei 1999/93/CE (JO L 257, 28.8.2014, p. 73).
(5) Regulamentul de punere în aplicare (UE) 2023/204 al Comisiei din 28 octombrie 2022 de stabilire a specificațiilor tehnice, a standardelor și a procedurilor pentru mediul aferent ghișeului unic european în domeniul maritim în temeiul Regulamentului (UE) 2019/1239 al Parlamentului European și al Consiliului (JO L 33, 3.2.2023, p. 1).
(6) Regulamentul delegat al Comisiei (UE) 2015/2446 din 28 iulie 2015 de completare a Regulamentului (UE) nr. 952/2013 al Parlamentului European și al Consiliului în ceea ce privește normele detaliate ale anumitor dispoziții ale Codului vamal al Uniunii (JO L 343, 29.12.2015, p. 1).
ANEXĂ
PARTEA I
MODULUL DE INTERFAȚĂ DE RAPORTARE (RIM)
ARHITECTURĂ ȘI DOMENIU DE APLICARE
RIM face parte dintr-un model cu patru colțuri pentru mesajele schimbate între expeditori (colțul 1) și nucleul MNSW (colțul 4), transmise prin punctele de acces AS4 (colțurile 2 și 3) către fiecare parte care implementează protocolul AS4 pentru transport și securitate, după cum urmează:
Colțul 1: serviciul administrativ al expeditorului, care pregătește, transmite și primește mesajele de la și către nucleul MNSW;
Colțul 2: punctul de acces AS4 al expeditorului;
Colțul 3: RIM;
Colțul 4: nucleul MNSW care recepționează mesajele și trimite mesaje de răspuns expeditorului.
[figură]
Figura 1 – Nivelul superior al arhitecturii RIM
RIM nu mai efectuează validarea semantică a mesajelor dincolo de specificațiile ghidului de implementare a mesajelor, nu mai tratează secvența acestora și nici nu mai stochează mesajele după ce ele au fost transferate cu succes către nucleul MNSW sau către expeditor.
În conformitate cu articolul 5 alineatul (3) litera (c) din Regulamentul (UE) 2019/1239, odată ce mesajul este transferat de la RIM la nucleul MNSW, statele membre, după caz, traduc, validează și transferă datele de formalitate către sistemele autorităților relevante în conformitate cu specificațiile sistemelor respective.
SPECIFICAȚIILE FUNCȚIONALE ALE RIM
ID | Funcție | Descriere
LR1 | Înregistrare și monitorizare | Funcția asigură înregistrarea și stocarea evenimentelor (livrări eșuate, întârzieri și erori de destinatar).
LR2 | Stocarea metadatelor | Funcția asigură stocarea metadatelor mesajelor schimbate.
OA1 | Stocarea și consultarea datelor tehnice | Funcția asigură stocarea și consultarea datelor tehnice necesare pentru configurarea și funcționarea RIM cu ajutorul unei interfețe (de exemplu, adresele tehnice ale punctelor de acces AS4 ale expeditorilor, schemele mesajelor din ghidul de implementare a mesajelor etc.).
OA2 | Tratarea excepțiilor | Funcția furnizează notificări cu privire la erorile de prelucrare și/sau la condițiile anormale detectate prin intermediul unei interfețe pentru utilizatori.
OA3 | Accesul la informații și metadate privind înregistrarea și monitorizarea | Funcția asigură accesul nucleului MNSW la informațiile și metadatele privind înregistrarea și monitorizarea mesajelor schimbate prin intermediul unei interfețe de la sistem la sistem.
OA4 | Autentificarea expeditorului | Funcția declanșează procesul de autentificare al unui expeditor care utilizează un serviciu de autentificare central sau național.
OA5 | Validarea mesajului | Funcția efectuează validarea sintactică și semantică a mesajelor primite în conformitate cu specificațiile tehnice ale mesajelor definite în ghidul de implementare a mesajelor. Ghidul de implementare a mesajelor trebuie să specifice validările care trebuie efectuate de RIM. RIM notifică erorile în consecință.
MF1 | Tratarea mesajelor | Funcția asigură transferarea fără modificări, în colțul relevant, a conținutului mesajelor primite (formalitate sau răspuns), dacă validările au fost efectuate cu succes.
SPECIFICAȚIILE TEHNICE ALE RIM
Integrare
ID | Denumire | Descriere
IA1. | Standard privind protocolul de mesagerie | RIM utilizează protocolul de mesagerie AS4 pentru a facilita interoperabilitatea cu diferite tehnologii și sisteme de raportare ale expeditorilor.
Schimbul de mesaje
ID | Denumire | Descriere
AP1. | Model asincron de schimb de mesaje | RIM trebuie să permită transmiterea asincronă a mesajelor către și dinspre (formalitate și răspuns) nucleul MNSW prin intermediul unui mecanism „push/pull”.
Securitate
ID | Denumire | Descriere
SA1. | Confidențialitatea și securitatea schimbului de informații | RIM asigură confidențialitatea informațiilor și protecția oricăror date cu caracter personal schimbate, prin criptarea informațiilor schimbate între punctele de acces AS4 ale expeditorilor și RIM. RIM decriptează și pune mesajele trimise de un expeditor la dispoziția nucleului MNSW. RIM utilizează ca standard un protocol „Web Service Security” (WSS) pentru a permite schimbul securizat de mesaje între punctul de acces AS4 al expeditorului și RIM.
SA2. | Nerespingerea mesajelor | Comunicarea și validarea mesajelor prin intermediul RIM includ măsuri de securitate pentru a asigura autenticitatea mesajelor și pentru a evita respingerea acestora.
SA3. | Integritate | Se instituie măsuri tehnice pentru a se asigura integritatea datelor schimbate.
SA4. | Securitatea aplicației | RIM se bazează pe cele mai bune practici în materie de dezvoltare a software-ului care permit detectarea activităților răuvoitoare și transferul securizat al informațiilor sensibile.
SA5. | Disponibilitatea serviciului | Pentru o comunicare și o distribuție fiabilă a informațiilor între expeditori și ghișeele unice naționale în domeniul maritim, RIM pune în aplicare mecanisme care asigură faptul că mesajele schimbate cu RIM nu sunt pierdute în caz de indisponibilitate a serviciului.
Performanță și scalabilitate
ID | Denumire | Descriere
PS1. | Performanță și scalabilitate | RIM trebuie să fie în măsură să îndeplinească obiective de performanță existente și viitoare, cum ar fi timpul de răspuns, numărul de expeditori concomitenți și volumul/dimensiunea mesajelor schimbate.
Portabilitate și instalare
ID | Denumire | Descriere
PD1. | Independența platformei | RIM trebuie să fie compatibil cu arhitectura hardware și sistemele de operare cele mai comune în care acesta urmează să fie instalat. RIM trebuie să nu necesite echipamente hardware sau software brevetate pentru instalare sau configurare.
PD2. | Aplicația de autoinstalare | RIM trebuie furnizat sub forma unui pachet de software care include toate componentele aplicației pe care le necesită RIM. Dependențele furnizate și necesare sunt enumerate în fiecare notă de lansare a RIM.
PARTEA II
SISTEMUL EMSWE DE GESTIONARE A ACCESULUI ȘI A REGISTRULUI UTILIZATORILOR
REGISTRUL CENTRAL
La cererea expeditorului, statele membre care nu furnizează un registru național conform cu specificațiile registrului central prevăzute în prezenta anexă înregistrează numărul EORI și certificatul expeditorului în registrul central și sunt responsabile pentru verificarea, acuratețea și gestionarea datelor în conformitate cu articolul 12 alineatul (2) din Regulamentul (UE) 2019/1239. Registrul central pune la dispoziția statelor membre o interfață pentru a efectua înregistrarea și gestionarea expeditorilor.
SERVICIUL CENTRAL DE AUTENTIFICARE
Diagrama de mai jos ilustrează etapele secvențiale pentru autentificarea unui expeditor care pregătește și trimite un mesaj către RIM (etapele 1, 2).
RIM trebuie să execute funcția de „autentificare a expeditorului” (1) utilizând serviciul central de autentificare (etapa 3.a).
Etapa 3.a: Serviciul central de autentificare autentifică expeditorul prin interogarea registrului central și verificarea înregistrării relevante (3.a.i) sau, în cazul în care expeditorul nu este prezent în registrul central, prin interogarea registrului național al țării expeditorului, dacă este disponibil, și prin verificarea înregistrării relevante (etapa 3.a.ii).
Etapa 3.b: Atunci când într-un stat membru este stabilit și pus la dispoziție un serviciu național de autentificare, RIM execută funcția de „autentificare a expeditorului” utilizând respectivul serviciu național de autentificare numai pentru autentificarea expeditorilor care utilizează un certificat eliberat în statul membru respectiv.
Etapa 4: Rezultatul autentificării se trimite înapoi la RIM. În cazul unei autentificări reușite, mesajul trebuie pus la dispoziție în colțul 4 (nucleul MNSW) (etapa 5). Dacă autentificarea eșuează, se trimite un mesaj de eșuare către colțul 2.
[figură]
Figura 2
SPECIFICAȚIILE TEHNICE ALE URAM
Integrare
ID | Denumire | Descriere
URAM.01 | Standarde interoperabile | Software-ul URAM trebuie să respecte protocoale standard și să utilizeze elemente de securitate solide atunci când își expune interfețele și se combină cu alte componente.
URAM.02 | Conformitatea eIDAS | Software-ul URAM trebuie să utilizeze standarde și soluții UE deschise și trebuie să implementeze mecanismele de control necesare pentru a verifica certificatele expeditorului în raport cu listele de încredere publicate de statele membre în conformitate cu articolul 22 din Regulamentul (UE) nr. 910/2014 și cu Decizia de punere în aplicare (UE) 2015/1505 a Comisiei(2), inclusiv informațiile referitoare la prestatorii de servicii de încredere calificați care emit certificatele utilizate pentru sigiliile electronice.
Securitate
ID | Denumire | Descriere
URAM.03 | Confidențialitatea schimbului de informații | Pentru a asigura securitatea software-ului URAM și a schimbului de date cu caracter personal, se implementează următoarele protocoale și metode de criptare: — „Transport Layer Security” (TLS, securitatea pe nivelul de transport): toate software-urile din cadrul URAM trebuie să fie securizate cu ajutorul TLS pentru a se asigura criptarea și integritatea datelor la nivel de rețea contribuind astfel la protejarea datelor în timpul transmisiei și prevenind accesul neautorizat sau manipularea frauduloasă. — Pentru a comunica cu software-ul URAM, se implementează o configurație TLS.
URAM.04 | Securitatea aplicației | Software-ul URAM trebuie să garanteze detectarea activităților răuvoitoare și transferul securizat al informațiilor sensibile.
URAM 05 | Protecția datelor cu caracter personal | Drepturile de acces se acordă autorităților statelor membre în conformitate cu articolul 12 alineatul (2) din Regulamentul (UE) 2019/1239 în scopul înregistrării expeditorilor. Software-ul URAM trebuie să implementeze mecanisme de control al accesului pentru a asigura protecția acelor informații furnizate de utilizatori care reprezintă date cu caracter personal, care trebuie prelucrate exclusiv în scopul creării de conturi de utilizator și al gestionării drepturilor de acces corespunzătoare. Serviciul central de autentificare trebuie să păstreze datele cu caracter personal ale expeditorilor nu mai mult decât este necesar în scopul autentificării. Registrul central nu păstrează datele cu caracter personal ale expeditorilor mai mult decât este necesar pentru gestionarea contului.
Sustenabilitate și portabilitate
ID | Denumire | Descriere
URAM.06 | Independența tehnologică | Software-ul URAM trebuie să permit interacțiuni cu RIM și cu alte servicii relevante fără a fi nevoie de a utiliza software sau hardware brevetat și trebuie să permită integrarea în RIM, indiferent de mediul tehnologic în care este implementat RIM.
URAM.07 | Instalare independentă | Software-ul URAM nu trebuie să impună asupra RIM o cerință specifică de implementare. RIM trebui numai să asigure o conectivitate la internet și respectarea standardelor legate de securitatea și protocoalele software-ului URAM.
Funcțiile serviciului central de autentificare
Următoarele servicii trebuie să fie puse la dispoziția RIM de la serviciul central de autentificare.
ID | Denumire | Descriere
URAM.08 | Serviciul de autentificare | Serviciul central de autentificare este responsabil cu autentificarea expeditorilor prin verificarea valabilității certificatului, a numărului EORI și a asocierii dintre numărul EORI al expeditorului și certificatul acestuia. El prelucrează cererile de autentificare trimise de RIM și furnizează răspunsuri care indică o autentificare reușită sau nereușită.
Specificațiile registrului central
ID | Denumire | Descriere
URAM.09 | Înregistrarea expeditorului | Registrul central trebuie să pună la dispoziția statelor membre o interfață grafică de utilizator pentru înregistrarea datelor expeditorului. Odată înregistrat în registrul central, expeditorul este înregistrat în toate statele membre.
URAM.10 | Vizualizarea și căutarea expeditorului | Registrul central trebuie să permită unui stat membru să vizualizeze toate datele expeditorilor pe care le-a înregistrat anterior. Acesta trebuie, de asemenea, să ofere o funcționalitate de căutare pentru extragerea datelor expeditorilor înregistrați, pe baza mai multor criterii de căutare.
URAM.11 | Actualizarea expeditorului | Registrul central trebuie să permită unui stat membru să modifice toate datele expeditorilor înregistrați anterior, pentru a asigura acuratețea și valabilitatea datelor.
URAM.12 | Dezactivarea expeditorului | Registrul central trebuie să permită unui stat membru să își dezactiveze expeditorii înregistrați anterior.
URAM.13 | Audit și raportare | Registrul central trebuie să ofere capacități de raportare care să permită unui stat membru să analizeze date specifice ale expeditorilor săi înregistrați anterior, cum ar fi data înregistrării și valabilitatea certificatului.
URAM.14 | Notificări | Registrul central trebuie să ofere statelor membre posibilitatea de a primi o notificare din partea registrului central de fiecare dată când un expeditor înregistrat anterior de statul membru respectiv este înregistrat, actualizat sau dezactivat, precum și la expirarea certificatului acestuia.
(1) Identificată ca OA4 în secțiunea privind specificațiile funcționale RIM din partea I a prezentei anexe.
(2) Decizia de punere în aplicare (UE) 2015/1505 a Comisiei din 8 septembrie 2015 de stabilire a specificațiilor tehnice și a formatelor pentru listele sigure în temeiul articolului 22 alineatul (5) din Regulamentul (UE) nr. 910/2014 al Parlamentului European și al Consiliului privind identificarea electronică și serviciile de încredere pentru tranzacțiile electronice pe piața internă (JO L 235, 9.9.2015, p. 26).
ELI: http://data.europa.eu/eli/reg_impl/2023/2790/oj
