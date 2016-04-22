REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2016/480 AL COMISIEI
din 1 aprilie 2016
de stabilire a unor norme comune privind interconectarea registrelor electronice naționale ale întreprinderilor de transport rutier și de abrogare a Regulamentului (UE) nr. 1213/2010
(Text cu relevanță pentru SEE)
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (CE) nr. 1071/2009 al Parlamentului European și al Consiliului din 21 octombrie 2009 de stabilire a unor norme comune privind condițiile care trebuie îndeplinite pentru exercitarea ocupației de operator de transport rutier și de abrogare a Directivei 96/26/CE a Consiliului (1), în special articolul 16 alineatul (5),
întrucât:
(1) Articolul 16 alineatul (1) din Regulamentul (CE) nr. 1071/2009 prevede obligația statelor membre de a păstra un registru electronic național al întreprinderilor de transport rutier care au primit din partea unei autorități competente autorizația de exercitare a ocupației de operator de transport rutier. Datele relevante conținute de registrele electronice naționale ar trebui să fie accesibile tuturor autorităților competente ale celorlalte state membre. Articolul 16 alineatele (5) și (6) din Regulamentul (CE) nr. 1071/2009 prevede interconectarea registrelor electronice naționale până la 31 decembrie 2012, mandatând Comisia să adopte norme comune referitor la această interconectare. Pe baza respectivului mandat, Comisia a adoptat Regulamentul (UE) nr. 1213/2010 (2), pentru a facilita interconectarea registrelor electronice naționale prin intermediul unui sistem de schimb de informații denumit ERRU (European Registers of Road Transport Undertakings, Registrul european al întreprinderilor de transport rutier). Acesta a devenit operațional la 31 decembrie 2012.
(2) În cursul ultimilor trei ani de funcționare a ERRU, Comisia, împreună cu experți din statele membre, a identificat anumite aspecte legate de utilizarea practică a ERRU care nu corespund în totalitate proceselor administrative instituite în statele membre.
(3) Prin urmare, este necesar să se remedieze deficiențele identificate în funcționarea zilnică a ERRU, astfel încât sistemul să funcționeze conform dispozițiilor relevante din Regulamentul (CE) nr. 1071/2009, Regulamentul (CE) nr. 1072/2009 al Parlamentului European și al Consiliului (3) și Regulamentul (CE) nr. 1073/2009 al Parlamentului European și al Consiliului (4) și să se garanteze o utilizare uniformă a ERRU de către autoritățile competente de pe întregul teritoriu al UE. În plus, este necesar să se adapteze normele existente la progresul tehnic și științific.
(4) Regulamentul (UE) 2016/403 al Comisiei (5) referitor la clasificarea încălcărilor grave ale normelor Uniunii stabilește o nouă listă a categoriilor, tipurilor și gradelor de gravitate ale încălcărilor grave ale normelor Uniunii, care, pe lângă cele prevăzute în anexa IV la Regulamentul (CE) nr. 1071/2009, pot conduce la pierderea bunei reputații a întreprinderii de transport rutier sau a managerului de transport. Prin urmare, este necesar să se permită transmiterea de către ERRU a informațiilor referitoare la noua listă a încălcărilor.
(5) Dispozițiile privind protecția datelor cu caracter personal, stabilite în special de Directiva 95/46/CE a Parlamentului European și a Consiliului (6), se aplică prelucrării oricăror date cu caracter personal în temeiul Regulamentului (CE) nr. 1071/2009. În mod particular, statele membre trebuie să implementeze măsuri de securitate corespunzătoare, pentru a preveni utilizarea abuzivă a datelor cu caracter personal.
(6) După caz, dispozițiile privind protecția datelor cu caracter personal, stabilite de Regulamentul (CE) nr. 45/2001 al Parlamentului European și al Consiliului (7), se aplică prelucrării oricăror date cu caracter personal în temeiul Regulamentului (CE) nr. 1071/2009;
(7) Având în vedere numărul substanțial al modificărilor care ar trebui aduse normelor comune privind implementarea interconectării registrelor electronice naționale, este necesară înlocuirea Regulamentului (UE) nr. 1213/2010 cu un nou act. Prin urmare, Regulamentul (UE) nr. 1213/2010 ar trebui să fie abrogat.
(8) Măsurile prevăzute de prezentul regulament sunt conforme cu avizul comitetului menționat la articolul 42 alineatul (1) din Regulamentul (UE) nr. 165/2014 al Parlamentului European și al Consiliului (8),
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Obiect
Prezentul regulament stabilește cerințele referitoare la conectarea registrelor electronice naționale ale întreprinderilor de transport rutier la sistemul de mesagerie ERRU, conform prevederilor articolului 16 alineatul (5) din Regulamentul (CE) nr. 1071/2009.
Articolul 2
Definiții
În sensul prezentului regulament și pe lângă definițiile stabilite la articolul 2 din Regulamentul (CE) nr. 1071/2009, se aplică următoarele definiții:
(a) „ERRU (European Registers of Road Transport Undertakings, Registrul european al întreprinderilor de transport rutier)” înseamnă un sistem de interconectare a registrelor electronice naționale, instituit în conformitate cu articolul 16 alineatul (5) din Regulamentul (CE) nr. 1071/2009;
(b) „interfață asincronă” înseamnă un proces prin care un mesaj de răspuns la o solicitare este transmis printr-o nouă conexiune HTTP;
(c) „căutare pluridirecțională” înseamnă un mesaj de solicitare din partea unui stat membru, adresat tuturor celorlalte state membre;
(d) „hub central” înseamnă sistemul informatic care permite direcționarea mesajelor ERRU între statele membre;
(e) „CCP” înseamnă certificatul de competență profesională menționat la articolul 8 alineatul (8) din Regulamentul (CE) nr. 1071/2009;
(f) „stat membru al încălcării” înseamnă statul membru în care o întreprindere de transport a comis o încălcare;
(g) „stat membru de stabilire” înseamnă statul membru în care este stabilită o întreprindere;
(h) „sistem național” înseamnă sistemul informatic instituit în fiecare stat membru în scopul de a emite, a prelucra și a răspunde la mesaje ERRU;
(i) „interfață sincronă” înseamnă un proces prin care un mesaj de răspuns la o solicitare este transmis prin aceeași conexiune HTTP utilizată pentru solicitare;
(j) „stat membru solicitant” înseamnă statul membru care emite o solicitare sau o notificare care este apoi direcționată către statele membre respondente;
(k) „stat membru respondent” înseamnă statul membru către care este direcționată solicitarea sau notificarea ERRU.
Articolul 3
Obligația de a se conecta la ERRU
Statele membre realizează interconectarea la ERRU a registrelor electronice naționale menționate la articolul 16 din Regulamentul (CE) nr. 1071/2009 în conformitate cu procedurile și cu cerințele tehnice stabilite de prezentul regulament.
Articolul 4
Specificații tehnice
ERRU îndeplinește specificațiile tehnice prevăzute în anexele I-VII la prezentul regulament.
Articolul 5
Utilizarea ERRU
(1) Atunci când fac schimb de informații prin intermediul ERRU, autoritățile competente urmează procedurile stabilite în anexa VIII la prezentul regulament.
(2) Statele membre acordă propriilor organisme de control responsabile cu controalele în trafic acces la funcția Check Community Licence („Verificarea licenței comunitare”) a ERRU.
(3) Atunci când la controalele în trafic participă mai multe organisme naționale de control, statul membru decide cărora dintre organismele respective li se acordă accesul menționat la alineatul (2).
Articolul 6
Abrogare
Regulamentul (UE) nr. 1213/2010 se abrogă de la data aplicării prezentului regulament. Trimiterile la regulamentul abrogat se interpretează ca trimiteri la prezentul regulament.
Articolul 7
Intrarea în vigoare
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Se aplică de la 30 ianuarie 2019.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 1 aprilie 2016.
Pentru Comisie
Președintele
Jean-Claude JUNCKER
(1) JO L 300, 14.11.2009, p. 51.
(2) Regulamentul (UE) nr. 1213/2010 al Comisiei din 16 decembrie 2010 de stabilire a normelor comune privind interconectarea registrelor electronice naționale ale întreprinderilor de transport rutier (JO L 335, 18.12.2010, p. 21).
(3) Regulamentul (CE) nr. 1072/2009 al Parlamentului European și al Consiliului din 21 octombrie 2009 privind normele comune pentru accesul la piața transportului rutier internațional de mărfuri (JO L 300, 14.11.2009, p. 72).
(4) Regulamentul (CE) nr. 1073/2009 al Parlamentului European și al Consiliului din 21 octombrie 2009 privind normele comune pentru accesul la piața internațională a serviciilor de transport cu autocarul și autobuzul și de modificare a Regulamentului (CE) nr. 561/2006 (JO L 300, 14.11.2009, p. 88).
(5) Regulamentul (UE) 2016/403 al Comisiei din 18 martie 2016 de completare a Regulamentului (CE) nr. 1071/2009 al Parlamentului European și al Consiliului în ceea ce privește clasificarea încălcărilor grave ale normelor Uniunii, care pot determina pierderea de către un operator de transport rutier a bunei reputații și de modificare a anexei III la Directiva 2006/22/CE a Parlamentului European și a Consiliului (JO L 74, 19.3.2016, p. 8).
(6) Directiva 95/46/CE a Parlamentului European și a Consiliului din 24 octombrie 1995 privind protecția persoanelor fizice în ceea ce privește prelucrarea datelor cu caracter personal și libera circulație a acestor date (JO L 281, 23.11.1995, p. 31).
(7) Regulamentul (CE) nr. 45/2001 al Parlamentului European și al Consiliului din 18 decembrie 2000 privind protecția persoanelor fizice cu privire la prelucrarea datelor cu caracter personal de către instituțiile și organele comunitare și privind libera circulație a acestor date (JO L 8, 12.1.2001, p. 1).
(8) Regulamentul (UE) nr. 165/2014 al Parlamentului European și al Consiliului din 4 februarie 2014 privind tahografele în transportul rutier, de abrogare a Regulamentului (CEE) nr. 3821/85 al Consiliului privind aparatura de înregistrare în transportul rutier și de modificare a Regulamentului (CE) nr. 561/2006 al Parlamentului European și al Consiliului privind armonizarea anumitor dispoziții ale legislației sociale în domeniul transporturilor rutiere (JO L 60, 28.2.2014, p. 1).
ANEXA I
ASPECTE GENERALE ALE ERRU
1. ARHITECTURĂ
ERRU este compus din următoarele părți:
1.1. Un hub central, capabil să primească o solicitare din partea statului membru solicitant, să o valideze și să o prelucreze prin transmiterea ei către statele membre respondente. Hubul central va aștepta ca fiecare stat membru respondent să răspundă, va consolida toate răspunsurile și va transmite răspunsul consolidat statului membru solicitant.
1.2. Un sistem național per stat membru, care este echipat cu o interfață capabilă să transmită solicitări către hubul central și să primească răspunsurile corespunzătoare. Pentru a transmite și a recepționa mesaje de la hubul central, sistemele naționale pot utiliza software brevetat sau software comercial.
1.3. Ca alternativă la punctul 1.1, statele membre pot decide să utilizeze o rețea comercială compatibilă pentru efectuarea schimbului de mesaje. În acest caz, fiecare autoritate competentă va furniza hubului central statistici privind mesajele schimbate prin intermediul rețelei în cauză.
2. GESTIONARE
2.1. Hubul central este administrat de Comisie, care este responsabilă cu funcționarea tehnică și cu întreținerea hubului central.
2.2. Hubul central nu stochează date pentru perioade de peste șase luni, cu excepția datelor de logare și a datelor statistice prevăzute în anexa VII.
2.3. Hubul central nu oferă acces la datele cu caracter personal decât personalului autorizat al Comisiei, atunci când acest lucru este necesar în scopul întreținerii și al depanării.
2.4. Statele membre sunt responsabile pentru:
2.4.1. Crearea și administrarea propriilor sisteme naționale, inclusiv a interfeței cu hubul central.
2.4.2. Instalarea și întreținerea propriilor sisteme naționale, atât în materie de hardware, cât și de software, indiferent dacă acestea sunt brevetate sau comerciale.
2.4.3. Interoperabilitatea corectă a propriului sistem național cu hubul central, inclusiv administrarea mesajelor de eroare primite de la hubul central.
2.4.4. Luarea tuturor măsurilor pentru a asigura confidențialitatea, integritatea și disponibilitatea informațiilor.
2.4.5. Operarea sistemelor naționale în conformitate cu nivelurile de servicii prevăzute în anexa VI.
2.5. Portalul web MOVEHUB
Comisia furnizează o aplicație web cu acces securizat, denumită „portalul web MOVEHUB”, care asigură cel puțin următoarele servicii:
(a) statistici cu privire la disponibilitate, per stat membru;
(b) notificarea intervențiilor de întreținere la hubul central și la sistemele naționale ale statelor membre;
(c) rapoarte agregate;
(d) administrarea datelor de contact;
(e) schemele XSD.
2.6. Administrarea datelor de contact
Funcția de administrare a datelor de contact va asigura fiecărui stat membru posibilitatea de a administra datele de contact ale propriilor săi utilizatori din punct de vedere politic, economic, operativ și tehnic, autoritatea competentă a fiecărui stat membru fiind responsabilă cu întreținerea propriilor date de contact. Datele de contact ale celorlalte state membre vor putea fi vizualizate, dar nu vor putea fi modificate.
ANEXA II
FUNCȚIILE ERRU
| 1. | Prin intermediul ERRU se asigură următoarele funcții: 1.1. Check Good Repute (CGR) (verificarea bunei reputații): permite statului membru solicitant să transmită o interogare către unul sau către toate statele membre respondente, pentru a stabili adecvarea unui manager de transport și, prin urmare, autorizația de a exploata o întreprindere de transport. 1.2. Infringement Notification (INF) (notificarea încălcării): permite statului membru al încălcării să notifice statului membru de stabilire faptul că întreprinderea de transport a comis o încălcare gravă, astfel cum se menționează la articolul 6 alineatul (2) litera (b) din Regulamentul (CE) nr. 1071/2009. Această funcție permite, de asemenea, statului membru al încălcării să solicite aplicarea de sancțiuni întreprinderii de transport, în statul membru de stabilire. 1.3. Check Community Licence (CCL) (verificarea licenței comunitare): permite statului membru solicitant să transmită o interogare statului membru respondent (adică statului membru de stabilire), pentru a stabili dacă o întreprindere de transport funcționează cu o licență comunitară valabilă.
| 2. | Se includ și alte tipuri de mesaje considerate adecvate pentru funcționarea eficientă a sistemului ERRU, de exemplu notificările de eroare.
ANEXA III
DISPOZIȚII REFERITOARE LA MESAJELE ERRU
1. CERINȚE TEHNICE GENERALE
1.1. Pentru schimbul de mesaje, hubul central va asigura atât interfețe sincrone, cât și interfețe asincrone. Statele membre pot alege tehnologia cea mai adecvată pentru interfața cu propriile aplicații.
1.2. Toate mesajele schimbate între hubul central și sistemele naționale trebuie să fie codificate UTF-8.
1.3. Statele membre se asigură că sistemele lor naționale pot primi și prelucra mesajele care conțin caractere grecești sau chirilice.
2. STRUCTURA MESAJELOR XML ȘI DEFINIȚIA SCHEMEI (XSD)
2.1. Structura generală a mesajelor XML respectă formatul definit de schemele XSD instalate în hubul central.
2.2. Hubul central și sistemele naționale transmit și recepționează mesaje care sunt conforme cu schema XSD a mesajelor.
2.3. Sistemele naționale vor avea capacitatea de a transmite, de a recepționa și de a prelucra toate mesajele care corespund oricăreia dintre funcțiile prevăzute în anexa II.
2.4. Mesajele XML includ cel puțin cerințele minime prevăzute în apendicele la prezenta anexă.
Apendice
Cerințe minime privind conținutul mesajelor XML
Antet comun | Obligatoriu
Version (Versiune) | Versiunea oficială a specificațiilor XML va fi specificată prin namespace (spațiul de nume) definit în XSD a mesajului și în atributul version (versiune) din elementul antet al oricărui mesaj XML. Numărul versiunii („n.m”) va fi definit ca valoare fixă la fiecare lansare a fișierului de definiție a schemei XML (xsd). | Da
Test Identifier (Identificator testare) | ID opțional pentru testare. Inițiatorul testului va completa ID-ul, iar toți ceilalți participanți la fluxul de lucru vor redirecționa/returna același ID. În producție, el trebuie ignorat și nu va fi folosit dacă este furnizat. | Nu
Technical Identifier (Identificator tehnic) | Un UUID care identifică în mod unic fiecare mesaj. Expeditorul generează un UUID și completează acest atribut. Această informație nu se utilizează în niciun scop legat de activități economice. | Da
Workflow Identifier (Identificator al fluxului de lucru) | Identificatorul fluxului de lucru este un UUID și trebuie să fie generat de statul membru solicitant. Acest ID este apoi utilizat în toate mesajele pentru a corela fluxul de lucru. | Da
Sent At (Transmis la) | Data și ora (UTC) la care a fost transmis mesajul. | Da
Timeout (Timpul a expirat) | Acesta este un atribut opțional în ceea ce privește data și ora (în format UTC). Această valoare va fi stabilită doar de hub pentru solicitările redirecționate. Aceasta va informa statul membru respondent cu privire la ora la care expiră solicitarea. Această valoare nu este necesară nici în MS2TCN_< x >_Req, nici în toate mesajele de răspuns. Ea este facultativă, pentru a permite utilizarea aceleiași definiții de antet pentru toate tipurile de mesaje, indiferent dacă atributul timeoutValue este necesar sau nu. | Nu
From (De la) | Codul ISO 3166-1 alfa 2 al statului membru care transmite mesajul sau „UE”. | Da
To (Către) | Codul ISO 3166-1 alfa 2 al statului membru căruia i se transmite mesajul sau „UE”. | Da
Check Good Repute (Verificarea bunei reputații)
Check Good Repute Request (Solicitare de verificare a bunei reputații) | Obligatoriu
Business Case Identifier (Identificator de dosar) | Este vorba despre un număr de serie sau de referință care identifică fiecare solicitare în parte. | Da
Requesting Competent Authority (Autoritatea competentă solicitantă) | Autoritatea competentă care a emis solicitarea de căutare. | Da
Informații privind managerul de transport | Da, dacă nu există informații privind CCP
Family Name (Nume de familie) | Numele de familie al managerului de transport, așa cum apare în CCP. | Da
First Name (Prenume) | Prenumele complet al managerului de transport, așa cum apare în certificatul de competență profesională. | Da
Date of Birth (Data nașterii) | Data nașterii managerului de transport, în format ISO 8601 (AAAA-LL-ZZ). | Da
Place of Birth (Locul nașterii) | Locul nașterii managerului de transport. | Nu
Informații privind CCP | Da, dacă nu există informații privind managerul de transport
CPC Number (Numărul CCP) | Numărul certificatului de competență profesională. | Da
CPC Issue Date (Data eliberării CCP) | Data eliberării CCP, în format ISO 8601 (AAAA-LL-ZZ). | Da
CPC Issue Country (Țara care a eliberat CCP) | Țara care a eliberat CCP, în format ISO 3166-1 alfa 2. | Da
Check Good Repute Response (Răspuns la solicitarea de verificare a bunei reputații) | Obligatoriu
Business Case Identifier (Identificatorul dosarului) | Este vorba despre un număr de serie sau de referință care corespunde identificatorului de dosar al solicitării. | Da
Requesting Competent Authority (Autoritatea competentă solicitantă) | Autoritatea competentă care emite solicitarea de căutare. | Da
Responding Competent Authority (Autoritatea competentă respondentă) | Autoritatea competentă care a răspuns solicitării de căutare. | Da
Status Code (Cod de stare) | Codul de stare al căutării [de ex. found (găsit), not found (nu a fost găsit), error (eroare) etc.]. | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Informații găsite privind managerul de transport | Da, în cazul în care codul de stare este „Găsit”
Family Name (Nume de familie) | Numele de familie al managerului de transport, așa cum a fost înregistrat în registru. | Da
First Name (Prenume) | Prenumele complet al managerului de transport, așa cum a fost înregistrat în registru. | Da
Date of Birth (Data nașterii) | Data nașterii managerului de transport, în format ISO 8601 (AAAA-LL-ZZ), așa cum a fost înregistrată în registru. | Da
Place of Birth (Locul nașterii) | Locul nașterii managerului de transport, așa cum a fost înregistrat în registru. | Da
CPC Number (Numărul CCP) | Numărul certificatului de competență profesională, așa cum a fost înregistrat în registru. | Da
CPC Issue Date (Data eliberării CCP) | Data eliberării CCP, în format ISO 8601 (AAAA-LL-ZZ), așa cum a fost înregistrată în registru. | Da
CPC Issue Country (Țara care a eliberat CCP) | Țara care a eliberat CCP, în format ISO 3166-1 alfa 2, așa cum a fost înregistrată în registru. | Da
Total Managed Undertakings (Total întreprinderi administrate) | Numărul întreprinderilor de transport cu care este asociat managerul de transport. | Da
Total Managed Vehicles (Total vehicule administrate) | Numărul total al vehiculelor cu care este asociat managerul de transport. | Da
Fitness (Adecvare) | Se menționează „Adecvat” sau „Neadecvat”. | Da
End Date of Unfitness (Data de încheiere a neadecvării) | Data de încheiere a neadecvării managerului de transport, în format ISO 8601 (AAAA-LL-ZZ). Aplicabil dacă la rubrica „Adecvare” se menționează „Neadecvat”. | Nu
Search Method (Metoda de căutare) | Metoda utilizată pentru găsirea managerului de transport: NYSIIS, CCP, personalizată. | Da
Întreprinderea de transport (pentru fiecare manager de transport găsit) | Da, dacă numărul întreprinderilor administrate > 0
Transport Undertaking Name (Denumirea întreprinderii de transport) | Denumirea întreprinderii de transport (denumire și forma juridică), așa cum a fost înregistrată în registru. | Da
Transport Undertaking Address (Adresa întreprinderii de transport) | Adresa întreprinderii de transport (adresa, codul poștal, orașul, țara), așa cum a fost înregistrată în registru. | Da
Community Licence Number (Numărul licenței comunitare) | Numărul de serie al licenței comunitare a întreprinderii de transport, așa cum a fost înregistrat în registru. | Da
Community Licence Status (Starea licenței comunitare) | Starea licenței comunitare a întreprinderii de transport, așa cum a fost înregistrată în registru. | Da
Managed Vehicles (Vehicule administrate) | Numărul de vehicule administrate, așa cum a fost înregistrat în registru. | Da
Infringement Notification (Notificarea încălcării)
Infringement Notification Request (Solicitare de notificare a încălcării) | Obligatoriu
Business Case Identifier (Identificator de dosar) | Este vorba despre un număr de serie sau de referință care identifică fiecare solicitare în parte. | Da
Notifying Authority (Autoritatea notificatoare) | Autoritatea competentă care emite notificarea încălcării. | Da
Întreprinderea de transport | Da
Transport Undertaking Name (Denumirea întreprinderii de transport) | Denumirea întreprinderii de transport împotriva căreia se înregistrează încălcarea. | Da
Community Licence Number (Numărul licenței comunitare) | Numărul de serie al copiei legalizate a licenței comunitare a întreprinderii de transport. | Da
Vehicle Registration Number (Numărul de înmatriculare al vehiculului) | Numărul de înmatriculare al vehiculului cu care s-a comis încălcarea. | Da
Vehicle Registration Country (Țara de înmatriculare a vehiculului) | Țara în care este înmatriculat vehiculul. | Da
Încălcare gravă | Da
Date of Infringement (Data încălcării) | Data încălcării, în format ISO 8601. (AAAA-LL-ZZ) | Da
Category (Categoria) | Categoria încălcării: — MSI (most serious infringement) – încălcare extrem de gravă — VSI (very serious infringement) – încălcare foarte gravă — SI (serious infringement) – încălcare gravă | Da
Infringement Type (Tip de încălcare) | În conformitate cu clasificarea prevăzută în anexa IV la Regulamentul (CE) nr. 1071/2009 și în anexa I la Regulamentul (UE) 2016/403. | Da
Date of Check (Data verificării) | Data la care s-a efectuat verificarea care a confirmat încălcarea, în formatul ISO 8601 (AAAA-LL-ZZ). | Da
Sancțiune impusă (pentru fiecare încălcare gravă) | Da
Penalty Imposed Identifier (Identificatorul sancțiunii impuse) | Numărul de serie al sancțiunii individuale impuse. | Da
Final Decision Date (Data deciziei finale) | Data deciziei finale referitoare la sancțiunea impusă, în formatul ISO 8601 (AAAA-LL-ZZ). | Da
Penalty Type Imposed (Tipul de sancțiune impusă) | Se menționează: — 101 – „Warning” („Avertisment”) — 201 – „Temporary ban on cabotage operations” („Interzicere temporară a operațiunilor de cabotaj”) — 202 – „Fine” („Amendă”) — 203 – „Prohibition” („Interdicție”) — 204 – „Immobilisation” („Imobilizare”) — 102 – „Other” („Altele”) | Da
Start Date (Data de începere) | Data de începere a sancțiunii impuse, în formatul ISO 8601 (AAAA-LL-ZZ). | Nu
End Date (Data de încetare) | Data de încetare a sancțiunii impuse, în formatul ISO 8601 (AAAA-LL-ZZ). | Nu
Este executată | Yes/No (Da/Nu) | Da
Sancțiune solicitată (pentru fiecare încălcare gravă) | Nu
Penalty Requested Identifier (Identificatorul sancțiunii solicitate) | Numărul de serie al sancțiunii individuale solicitate. | Da
Penalty Type Requested (Tipul de sancțiune solicitată) | Se menționează: — 101 – „Warning” („Avertisment”) — 301 – „Temporary withdrawal of some or all of the certified true copies of the Community licence” („Retragerea temporară a unora sau a tuturor copiilor legalizate ale licenței comunitare”) — 302 – „Permanent withdrawal of some or all of the certified true copies of the Community licence” („Retragerea permanentă a unora sau a tuturor copiilor legalizate ale licenței comunitare”) — 303 – „Temporary withdrawal of the Community licence” („Retragerea temporară a licenței comunitare”) — 304 – „Permanent withdrawal of the Community licence” („Retragerea permanentă a licenței comunitare”) — 305 – „Suspension of the issue of driver attestations” („Suspendarea eliberării de atestate de conducător auto”) — 306 – „Withdrawal of driver attestations” („Retragerea atestatelor de conducător auto”) — 307 – „Issue of driver attestations subject to additional conditions in order to prevent misuse” („Eliberare a atestatelor de conducător auto supusă unor condiții suplimentare, pentru a preveni utilizarea abuzivă”) | Da
Duration (Durată) | Durata sancțiunii solicitate (zile calendaristice). | Nu
Infringement Notification Response (Răspuns la solicitarea de notificare a încălcării) | Obligatoriu
Business Case Identifier (Identificator de dosar) | Este vorba despre un număr de serie sau de referință care corespunde identificatorului de dosar al solicitării. | Da
Originating Authority (Autoritatea emitentă) | Autoritatea competentă care a emis notificarea inițială a încălcării. | Da
Licensing Authority (Autoritatea care acordă licența) | Autoritatea competentă care răspunde la notificarea încălcării. | Da
Status Code (Cod de stare) | Codul de stare al răspunsului la solicitarea de notificare a încălcării [de exemplu, found (găsit), not found (nu a fost găsit), error (eroare) etc.]. | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Întreprinderea de transport | Da
Transport Undertaking Name (Denumirea întreprinderii de transport) | Denumirea întreprinderii de transport, așa cum a fost înregistrată în registru. | Da
Sancțiune impusă | Nu
Penalty Imposed Identifier (Identificatorul sancțiunii impuse) | Numărul de serie al sancțiunii individuale impuse [menționat în Penalty Requested Identifier (Identificatorul sancțiunii solicitate) al Infringement Notification (Notificării încălcării)]. | Da
Authority Imposing Penalty (Autoritatea care impune sancțiunea) | Denumirea autorității care impune sancțiunea. | Da
Este impusă | Yes/No (Da/Nu) | Da
Penalty Type Imposed (Tipul de sancțiune impusă) | Se menționează: — 101 – „Warning” („Avertisment”) — 301 – „Temporary withdrawal of some or all of the certified true copies of the Community licence” („Retragerea temporară a unora sau a tuturor copiilor legalizate ale licenței comunitare”) — 302 – „Permanent withdrawal of some or all of the certified true copies of the Community licence” („Retragerea permanentă a unora sau a tuturor copiilor legalizate ale licenței comunitare”) — 303 – „Temporary withdrawal of the Community licence” („Retragerea temporară a licenței comunitare”) — 304 – „Permanent withdrawal of the Community licence” („Retragerea permanentă a licenței comunitare”) — 305 – „Suspension of the issue of driver attestations” („Suspendarea eliberării de atestate de conducător auto”) — 306 – „Withdrawal of driver attestations” („Retragerea atestatelor de conducător auto”) — 307 – „Issue of driver attestations subject to additional conditions in order to prevent misuse” („Eliberare a atestatelor de conducător auto supusă unor condiții suplimentare, pentru a preveni utilizarea abuzivă”) — 102 – „Other” („Altele”) | Da
Start Date (Data de începere) | Data de începere a sancțiunii impuse, în format ISO 8601 (AAAA-LL-ZZ). | Nu
End Date (Data de încetare) | Data de încetare a sancțiunii impuse, în format ISO 8601 (AAAA-LL-ZZ). | Nu
Motiv | Motivul neimpunerii sancțiunii. | Nu
Infringement Notification Acknowledgement (Confirmare de primire a notificării încălcării) | Obligatoriu
Business Case Identifier (Identificator de dosar) | Este vorba despre un număr de serie sau de referință care corespunde identificatorului de dosar al notificării sau al răspunsului. | Da
Status Code (Cod de stare) | Codul de stare al confirmării de primire. | Da
Status Message (Mesaj de stare) | Șirul mesajului de stare. | Nu
Originating Authority (Autoritatea emitentă) | Pentru o confirmare de primire a notificării încălcării (IN_Ack): în legislație, acest câmp este reprezentat ca „Identificatorul autorității competente destinatare”. Pentru o confirmare de primire a răspunsului la notificarea încălcării (IR_Ack): în legislație, acest câmp este reprezentat ca „Identificatorul autorității competente care confirmă primirea”. | Da
Licensing Authority (Autoritatea care acordă licența) | Pentru o confirmare de primire a notificării încălcării (IN_Ack): în legislație, acest câmp este reprezentat ca „Identificatorul autorității competente care confirmă primirea”. Pentru o confirmare de primire a răspunsului la notificarea încălcării (IR_Ack): în legislație, acest câmp este reprezentat ca „Identificatorul autorității competente destinatare”. | Da
Acknowledgement type (Tipul de confirmare) | Definirea tipului de confirmare. Coduri posibile: — „IN_Ack” — „IR_Ack” | Da
Check Community Licence (Verificarea licenței comunitare)
Check Community Licence Request (Solicitare de verificare a licenței comunitare) | Obligatoriu
Business Case Identifier (Identificator de dosar) | Este vorba despre un număr de serie sau de referință care identifică fiecare solicitare în parte. | Da
Originating Authority (Autoritatea emitentă) | Autoritatea care emite solicitarea de căutare. | Nu
Întreprinderea de transport | Da
Transport Undertaking Name (Denumirea întreprinderii de transport) | Denumirea întreprinderii de transport în legătură cu care se solicită informațiile privind licența comunitară. | Da
Community Licence Number (Numărul licenței comunitare) | Numărul de serie al copiei legalizate a licenței comunitare în legătură cu care se solicită informații. | Da
Vehicle Registration Number (Numărul de înmatriculare al vehiculului) | Numărul de înmatriculare al vehiculului pentru care se emite copia legalizată a licenței comunitare. | Nu
Check Community Licence Response (Răspuns la solicitarea de verificare a licenței comunitare) | Obligatoriu
Business Case Identifier (Identificator de dosar) | Este vorba despre un număr de serie sau de referință care identifică fiecare solicitare în parte. | Da
Originating Authority (Autoritatea emitentă) | Autoritatea care a emis solicitarea de căutare. | Nu
Întreprinderea de transport | Da
Transport Undertaking Name (Denumirea întreprinderii de transport) | Denumirea întreprinderii de transport (denumire și forma juridică), așa cum a fost înregistrată în registru. | Da
Transport Undertaking Address (Adresa întreprinderii de transport) | Adresa întreprinderii de transport (adresa, codul poștal, orașul, țara), așa cum a fost înregistrată în registru. | Da
Informații privind licența comunitară | Da
Licence Number (Numărul licenței) | Numărul de serie al licenței comunitare a întreprinderii de transport, așa cum a fost înregistrat în registru. | Da
Licence Status (Starea licenței) | Starea licenței comunitare a întreprinderii de transport, așa cum a fost înregistrată în registru: — „Active” (Activă) — „Suspended” („Suspendată”) — „Withdrawn” („Retrasă”) — „Expired” („Expirată”) — „Lost/stolen” („Pierdută/furată”) — „Annulled” („Anulată”) — „Returned” („Returnată”) | Da
Licence Type (Tipul de licență) | Tipul de licență comunitară, așa cum a fost înregistrat în registru. O declarație privind: — „Community licence for passenger transport” („Licența comunitară pentru transportul de pasageri”) — „National licence for passenger transport” („Licența națională pentru transportul de pasageri”) — „Community licence for goods transport” („Licența comunitară pentru transportul de mărfuri”) — „National licence for goods transport” („Licența națională pentru transportul de mărfuri”) | Da
Start Date (Data de începere) | Data de începere a valabilității licenței comunitare. | Da
Expiry Date (Data de expirare) | Data de expirare a valabilității licenței comunitare. | Da
Withdrawal Date (Data retragerii) | Data retragerii licenței comunitare. | Nu
Suspension Date (Data suspendării) | Data suspendării licenței comunitare. | Nu
Suspension Expiry Date (Data de expirare a suspendării) | Data la care expiră suspendarea licenței comunitare. | Nu
Managed Vehicles (Vehicule administrate) | Numărul de vehicule administrate, așa cum a fost înregistrat în registru. | Da
Certified True Copy Details (Informații privind copia legalizată) | Da
Licence Number (Numărul licenței) | Numărul de serie al copiei legalizate a licenței comunitare a întreprinderii de transport, așa cum este înregistrat în registru (este vorba despre numărul licenței care a fost primit odată cu solicitarea). | Da
Licence Status (Starea licenței) | Starea copiei legalizate a licenței comunitare a întreprinderii de transport, așa cum a fost înregistrată în registru: — „Active” („Activă”) — „Suspended” („Suspendată”) — „Withdrawn” („Retrasă”) — „Expired” (Expirată) — „Lost/stolen” („Pierdută/furată”) — „Annulled” (Anulată) — „Returned” („Returnată”) | Da
Licence Type (Tipul de licență) | Tipul de copie legalizată a licenței comunitare, așa cum a fost înregistrat în registru. O declarație privind: — „Community licence for passenger transport” („Licența comunitară pentru transportul de pasageri”) — „National licence for passenger transport” („Licența națională pentru transportul de pasageri”) — „Community licence for goods transport” („Licența comunitară pentru transportul de mărfuri”) — „National licence for goods transport” („Licența națională pentru transportul de mărfuri”) | Da
Start Date (Data de începere) | Data de începere a valabilității copiei legalizate a licenței comunitare. | Da
Expiry Date (Data de expirare) | Data de expirare a valabilității copiei legalizate a licenței comunitare. | Da
Withdrawal Date (Data retragerii) | Data retragerii copiei legalizate a licenței comunitare. | Nu
Suspension Date (Data suspendării) | Data suspendării copiei legalizate a licenței comunitare. | Nu
Suspension Expiry Date (Data de expirare a suspendării) | Data la care expiră suspendarea copiei legalizate a licenței comunitare. | Nu
ANEXA IV
SERVICII DE TRANSLITERARE ȘI SERVICII NYSIIS
1. Pentru a codifica numele tuturor managerilor de transport în registrul național se utilizează algoritmul NYSIIS, implementat în hubul central.
2. Atunci când caută numele unui manager de transport în registru prin intermediul funcției CGR, statele membre trebuie să utilizeze întotdeauna cheia NYSIIS, ca mecanism de căutare principal.
3. În plus, statele membre pot utiliza un algoritm personalizat, pentru a obține rezultate suplimentare.
4. Rezultatele căutării vor indica mecanismul de căutare prin intermediul căruia a fost găsită înregistrarea: NYSIIS, CCP sau personalizat.
ANEXA V
CERINȚE DE SECURITATE
1. Pentru schimbul de mesaje între hubul central și sistemele naționale trebuie utilizat întotdeauna protocolul HTTPS.
2. Sistemele naționale vor utiliza certificatele PKI furnizate de Comisie, pentru a securiza transmisia mesajelor între sistemul național și hub.
3. Sistemele naționale implementează cel puțin certificate care utilizează algoritmul hash semnătură SHA-2 (SHA-256) și o lungime a cheilor publice de 2 048 de biți.
ANEXA VI
NIVELURILE SERVICIULUI
1. Sistemele naționale asigură următorul nivel minim al serviciului:
1.1. Sunt disponibile 24 de ore pe zi, 7 zile pe săptămână.
1.2. Disponibilitatea lor este monitorizată prin intermediul unui mesaj heartbeat emis de hubul central.
1.3. Rata lor de disponibilitate este de 98 %, în conformitate cu tabelul următor (cifrele au fost rotunjite la cea mai apropiată unitate):
O disponibilitate de | înseamnă o indisponibilitate de
Zilnică | Lunară | Anuală
98 % | 0,5 ore | 15 ore | 7,5 zile
Statele membre sunt încurajate să respecte rata de disponibilitate zilnică; este recunoscut, însă, faptul că anumite activități necesare, cum ar fi întreținerea sistemului, vor necesita o perioadă de indisponibilitate de peste 30 de minute. Cu toate acestea, ratele de disponibilitate lunare și anuale rămân obligatorii.
1.4. Statele membre răspund la minimum 98 % din solicitările redirecționate către ele într-o lună calendaristică.
1.5. Atunci când transmit răspunsuri la solicitările de verificare a bunei reputații, confirmări de primire a notificării încălcării și răspunsuri la solicitările de verificare a licenței comunitare în conformitate cu anexa VIII.
1.5.1. Ele răspund solicitărilor în cel mult 10 secunde.
1.5.2. Durata globală de așteptare a solicitării (timpul în care solicitantul poate să aștepte un răspuns) nu depășește 20 de secunde.
1.5.3. Ele sunt capabile să proceseze solicitări la o rată de șase mesaje pe secundă.
1.6. Sistemele naționale nu vor transmite solicitări către hubul ERRU la o rată care depășește 2 solicitări pe secundă.
1.7. Fiecare sistem național trebuie să fie capabil să facă față eventualelor probleme tehnice ale hubului central sau ale sistemelor naționale din alte state membre. Acestea includ, dar nu se limitează la:
(a) pierderea legăturii cu hubul central;
(b) neprimirea unui răspuns la o solicitare;
(c) primirea răspunsurilor după ce durata de așteptare a mesajului a expirat;
(d) primirea de mesaje nesolicitate;
(e) primirea de mesaje incorecte.
2. Hubul central:
2.1. Prezintă o rată de disponibilitate de 98 %.
2.2. Transmite sistemelor naționale notificări ale oricăror erori, fie prin intermediul mesajului de răspuns, fie prin intermediul unui mesaj de eroare specific. La rândul lor, sistemele naționale primesc aceste mesaje de eroare specifice și dispun de un flux de lucru progresiv (escalation workflow) pentru a lua toate măsurile adecvate în vederea remedierii erorii notificate.
3. Întreținere
Statele membre notifică celorlalte state membre și Comisiei, prin intermediul aplicației web, orice activități de întreținere de rutină, cu cel puțin o săptămână înainte de începerea respectivelor activități, dacă acest lucru este posibil din punct de vedere tehnic.
ANEXA VII
REGISTRE ȘI STATISTICI
1. Prezenta anexă prevede detalii privind datele din registre și datele statistice culese la nivelul hubului central, nu la cel al statelor membre.
2. Pentru a se asigura confidențialitatea, datele în scopuri statistice trebuie să fie anonimizate. Datele de identificare a unui anumit manager de transport, a unei anumite întreprinderi de transport sau a unui anumit CCP nu vor fi disponibile în scopuri statistice.
3. Informațiile din registre trebuie să țină evidența tuturor tranzacțiilor, în scopul monitorizării și al corectării erorilor de sistem și trebuie să permită generarea de statistici referitoare la respectivele tranzacții.
4. Datele cu caracter personal nu sunt păstrate în registre mai mult de șase luni. Informațiile statistice vor fi păstrate pe o perioadă nedeterminată.
5. Datele statistice utilizate pentru raportare vor include:
(a) statul membru solicitant;
(b) statul membru respondent;
(c) tipul mesajului;
(d) codul de stare al răspunsului;
(e) data și ora mesajelor;
(f) timpul de răspuns.
ANEXA VIII
UTILIZAREA ERRU
1. VERIFICAREA BUNEI REPUTAȚII A MANAGERILOR DE TRANSPORT
Atunci când verifică prin intermediul ERRU în conformitate cu articolul 11 alineatul (4) din Regulamentul (CE) nr. 1071/2009 dacă un manager de transport a fost declarat într-un stat membru drept neadecvat pentru administrarea activităților de transport ale unei întreprinderi, statele membre efectuează o căutare pluridirecțională CGR, prin transmiterea unei solicitări de verificare a bunei reputații (Check Good Repute Request). Statele membre respondente răspund solicitării prin transmiterea unui răspuns la solicitarea de verificare a bunei reputații (Check Good Repute Response).
2. SCHIMBUL DE INFORMAȚII CU PRIVIRE LA ÎNCĂLCĂRI
2.1. Cu ocazia schimbului de informații privind încălcările grave, efectuat prin intermediul ERRU în conformitate cu articolul 13 alineatul (1) din Regulamentul (CE) nr. 1072/2009 sau cu articolul 23 alineatul (1) din Regulamentul (CE) nr. 1073/2009, statul membru al încălcării notifică statului membru de stabilire cazul sau cazurile în care o întreprindere de transport comite o încălcare, în temeiul articolului 16 din Regulamentul (CE) nr. 1071/2009. Notificarea se realizează prin transmiterea unei solicitări de notificare a încălcării (Infringement Notification Request).
2.2. Solicitarea de notificare a încălcării (Infringement Notification Request) trebuie transmisă cât mai curând posibil și cel mai târziu în termen de șase săptămâni de la adoptarea deciziei finale în materie. Ea va oferi informații referitoare la încălcări, la statutul sancțiunilor impuse și, dacă este cazul, la sancțiunile solicitate în statul membru de stabilire.
2.3. Statul membru de stabilire răspunde solicitării de notificare a încălcării (Infringement Notification Request) prin transmiterea unui răspuns la solicitarea de notificare a încălcării (Infringement Notification Response), cât mai curând posibil și cel mai târziu în termen de șase săptămâni de la adoptarea deciziei finale în materie, informând dacă sancțiunile solicitate de statul membru de încălcare au fost impuse și care sunt acestea. Dacă aceste sancțiuni nu sunt impuse, răspunsul la solicitarea de notificare a încălcării (Infringement Notification Response) furnizează o justificare.
2.4. În toate cazurile, o notificare a încălcării (Infringement Notification) trebuie confirmată întotdeauna printr-o confirmare de primire a notificării încălcării (Infringement Notification Acknowledgment).
3. VERIFICAREA LICENȚEI COMUNITARE
3.1. Atunci când verifică disponibilitatea licenței comunitare prevăzute la articolul 4 din Regulamentele (CE) nr. 1072/2009 și (CE) nr. 1073/2009, un stat membru poate solicita, prin intermediul unei solicitări de verificare a licenței comunitare (Check Community Licence Request) transmise statului membru de stabilire, informațiile referitoare la licența comunitară menționate la articolul 16 alineatul (2) litera (d) din Regulamentul (CE) nr. 1071/2009.
3.2. Statul membru de stabilire răspunde prin transmiterea unui răspuns la solicitarea de verificare a licenței comunitare (Check Community Licence Response).
