REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2016/68 AL COMISIEI
din 21 ianuarie 2016
privind procedurile și specificațiile comune necesare pentru interconectarea registrelor electronice ale cardurilor de conducător auto
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) nr. 165/2014 al Parlamentului European și al Consiliului din 4 februarie 2014 privind tahografele în transportul rutier (1), în special articolul 31 alineatul (5),
întrucât:
(1) Regulamentul (UE) nr. 165/2014 prevede obligația statelor membre de a face schimb electronic de date pentru a asigura unicitatea cardurilor de conducător auto eliberate.
(2) Pentru a facilita schimbul electronic de informații între statele membre cu privire la cardurile de conducător auto, Comisia a instituit sistemul de mesagerie TACHOnet, care permite statelor membre să solicite informații celorlalte state membre cu privire la eliberarea cardurilor de conducător auto, precum și cu privire la starea acestor carduri.
(3) Regulamentul (UE) nr. 165/2014 face obligatorie interconectarea registrelor electronice naționale privind cardurile de conducător auto în întreaga Uniune, folosind fie sistemul de mesagerie TACHOnet, fie un sistem compatibil. Totuși, în cazul utilizării unui sistem compatibil, schimbul de date electronice cu toate celelalte state membre trebuie să fie posibil prin intermediul sistemului de mesagerie TACHOnet.
(4) Prin urmare, este necesar să se stabilească procedurile și specificațiile comune obligatorii pentru TACHOnet, inclusiv formatul datelor schimbate, procedurile tehnice pentru consultarea electronică a registrelor electronice naționale, procedurile de acces și mecanismele de securitate.
(5) Măsurile prevăzute în prezentul regulament sunt conforme cu avizul comitetului menționat la articolul 42 alineatul (3) din Regulamentul (UE) nr. 165/2014,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Obiect
Prezentul regulament stabilește cerințele privind conectarea obligatorie a registrelor electronice naționale cu privire la cardurile de conducător auto la sistemul de mesagerie TACHOnet menționat la articolul 31 din Regulamentul (UE) nr. 165/2014.
Articolul 2
Definiții
Pe lângă definițiile prevăzute la articolul 2 din Regulamentul (UE) nr. 165/2014, se aplică următoarele definiții:
(a) „interfață asincronă” înseamnă un proces prin care un mesaj de răspuns la o solicitare este transmis printr-o nouă conexiune HTTP;
(b) „căutare pluridirecțională” înseamnă un mesaj de solicitare din partea unui stat membru, adresat tuturor celorlalte state membre;
(c) „autoritate emitentă a cardului” („AEC”) înseamnă entitatea împuternicită de un stat membru pentru emiterea și gestionarea cardurilor de tahograf;
(d) „hub central” înseamnă sistemul de informații care permite direcționarea mesajelor TACHOnet între statele membre;
(e) „sistem național” înseamnă sistemul informatic instituit în fiecare stat membru în scopul de a emite, prelucra și răspunde la mesaje TACHOnet;
(f) „interfață sincronă” înseamnă un proces prin care un mesaj de răspuns la o solicitare este transmis prin aceeași conexiune HTTP utilizată pentru solicitare;
(g) „stat membru solicitant” înseamnă statul membru care emite o solicitare sau o notificare, care este apoi direcționată către statul membru respondent corespunzător sau către statele membre respondente corespunzătoare;
(h) „stat membru respondent” înseamnă statul membru căruia i se adresează solicitarea sau notificarea TACHOnet;
(i) „căutare unidirecțională” înseamnă un mesaj de solicitare din partea unui stat membru adresat unui singur stat membru;
(j) „card de tahograf” înseamnă fie un card de conducător auto, fie un card de atelier, astfel cum sunt definite la articolul 2 literele (f) și (k) din Regulamentul (UE) nr. 165/2014.
Articolul 3
Obligația de a se conecta la TACHOnet
Statele membre conectează registrele electronice naționale menționate la articolul 31 alineatul (1) din Regulamentul (UE) nr. 165/2014 la sistemul de mesagerie TACHOnet.
Articolul 4
Specificații tehnice
Sistemul de mesagerie TACHOnet îndeplinește specificațiile tehnice prevăzute în anexele I-VII.
Articolul 5
Utilizarea sistemului TACHOnet
Statele membre urmează procedurile stabilite în anexa VIII.
Statele membre asigură accesul la sistemul de mesagerie TACHOnet autorităților naționale emitente ale cardurilor și agenților de control care îndeplinesc sarcinile prevăzute la articolul 38 din Regulamentul (UE) nr. 165/2014, pentru a facilita realizarea unor verificări eficace ale valabilității, stării și unicității cardurilor de conducător auto.
Articolul 6
Intrare în vigoare
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Se aplică de la 2 martie 2018.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 21 ianuarie 2016.
Pentru Comisie
Președintele
Jean-Claude JUNCKER
(1) JO L 60, 28.2.2014, p. 1.
ANEXA I
Aspecte generale referitoare la sistemul de mesagerie TACHOnet
1. Arhitectură
Sistemul de mesagerie TACHOnet este compus din următoarele părți:
1.1. Un hub central, care poate primi o solicitare din partea statului membru solicitant și o poate valida și prelucra prin transmiterea ei către statele membre respondente. Hubul central așteaptă ca fiecare stat membru respondent să răspundă, consolidează toate răspunsurile și transmite răspunsul consolidat statului membru solicitant.
Toate mesajele TACHOnet sunt direcționate de către hubul central.
1.2. Sistemele naționale ale statelor membre, care trebuie să fie echipate cu o interfață capabilă să transmită solicitări către hubul central și să primească răspunsurile corespunzătoare. Sistemele naționale pot utiliza software brevetat sau comercial pentru a transmite și a recepționa mesaje de la hubul central.
2. Administrare
2.1. Hubul central este administrat de Comisie, care este responsabilă de funcționarea tehnică și de întreținerea hubului central.
2.2. Hubul central nu stochează datele mai mult de șase luni, cu excepția datelor de logare și a datelor statistice prevăzute în anexa VII.
2.3. Hubul central nu oferă acces la datele cu caracter personal decât personalului autorizat al Comisiei, atunci când acest lucru este necesar în scopul monitorizării, al întreținerii și al depanării.
2.4. Statele membre sunt responsabile pentru:
2.4.1. crearea și administrarea sistemelor naționale, inclusiv interfața cu hubul central;
2.4.2. instalarea și întreținerea sistemelor naționale, atât în materie de hardware, cât și de software, indiferent dacă este brevetat sau comercial;
2.4.3. interoperabilitatea corectă a sistemului național cu hubul central, inclusiv administrarea mesajelor de eroare primite de la hubul central;
2.4.4. luarea tuturor măsurilor pentru asigurarea confidențialității, a integrității și a disponibilității informațiilor;
2.4.5. operarea sistemelor naționale în conformitate cu nivelurile de servicii prevăzute în anexa VI.
2.5. Portalul web MOVEHUB
Comisia furnizează o aplicație web cu acces securizat, denumită „portalul web MOVEHUB”, care asigură cel puțin următoarele servicii:
(a) statistici cu privire la disponibilitatea statelor membre;
(b) notificarea intervențiilor de întreținere la hubul central și la sistemele naționale ale statelor membre;
(c) rapoarte agregate;
(d) administrarea datelor de contact;
(e) schemele XSD.
2.6. Administrarea datelor de contact
2.6.1. Funcția de administrare a datelor de contact asigură fiecărui stat membru posibilitatea de a administra datele de contact ale utilizatorilor cu interese politice, economice, operaționale și tehnice din statul membru respectiv; autoritatea competentă a fiecărui stat membru deține responsabilitatea întreținerii propriilor date de contact. Este posibilă consultarea, dar nu modificarea datelor de contact ale altor state membre.
2.6.2. TACHOnet utilizează datele de contact menționate la punctul 2.6.1 pentru a completa datele de contact în mesajele de răspuns.
ANEXA II
Funcțiile sistemului de mesagerie TACHOnet
1. Sistemul de mesagerie TACHOnet asigură următoarele funcții:
1.1. Check Issued Cards (CIC) (Verificarea cardurilor eliberate): permite statului membru solicitant să trimită o solicitare de verificare a cardurilor eliberate (Check Issued Cards Request) către un stat membru respondent sau către toate statele membre respondente, pentru a stabili dacă un solicitant de card deține deja un card de conducător auto eliberat de statele membre respondente. Statele membre respondente răspund solicitării prin trimiterea unui răspuns de verificare a cardurilor eliberate (Check Issued Cards Response);
1.2. Check Card Status (CCS) (Verificarea stării cardului): permite statului membru solicitant să ceară statului membru respondent detalii cu privire la un card eliberat de acesta din urmă, prin trimiterea unei solicitări de verificare a stării cardului (Check Card Status Request). Statul membru respondent răspunde solicitării prin trimiterea unui răspuns de verificare a stării cardului (Check Card Status Response);
1.3. Modify Card Status (MCS) (Modificarea stării cardului): permite statului membru solicitant să notifice statului membru respondent, printr-o solicitare de modificare a stării cardului (Modify Card Status Request), că starea unui card eliberat de acesta din urmă s-a schimbat. Statul membru respondent răspunde printr-un mesaj de luare la cunoștință a modificării stării cardului (Modify Card Status Acknowledgement);
1.4. Issued Card Driving License (ICDL) (Permisul de conducere pe baza căruia a fost eliberat cardul): permite statului membru solicitant să notifice statului membru respondent, prin intermediul unei solicitări de tipul Issued Card Driving Licence Request, că a fost eliberat un card de către statul membru solicitant pe baza unui permis de conducere eliberat de către statul membru respondent. Statul membru respondent răspunde printr-un mesaj Issued Card Driving Licence Response.
2. Se includ și alte tipuri de mesaje considerate adecvate pentru funcționarea eficientă a sistemului TACHOnet, de exemplu notificările de eroare.
3. Sistemele naționale trebuie să recunoască stările cardului care figurează în apendicele la prezenta anexă, atunci când se utilizează oricare dintre funcțiile descrise la punctul 1 Cu toate acestea, statele membre nu sunt obligate să pună în aplicare o procedură administrativă care să utilizeze toate stările enumerate.
4. Atunci când un stat membru primește un răspuns sau o notificare indicând o stare care nu este folosită în cadrul procedurilor sale administrative, sistemul național transpune starea din mesajul primit în valoarea corespunzătoare din procedura respectivă. Mesajul nu trebuie să fie respins de statul membru respondent, atât timp cât starea din mesaj figurează în apendicele la prezenta anexă.
5. Starea cardului care figurează în apendicele la prezenta anexă nu trebuie utilizată pentru a stabili dacă un card de conducător auto este valabil pentru conducerea unui autovehicul. Atunci când un stat membru interoghează registrul statului membru emitent al cardului prin intermediul funcției CCS, răspunsul trebuie să conțină câmpul dedicat „valabil pentru conducerea unui autovehicul”. Procedurile administrative naționale trebuie să fie de așa natură încât răspunsurile CCS să conțină întotdeauna valoarea adecvată în câmpul „valabil pentru conducerea unui autovehicul”.
Apendice
Stări ale cardului
Starea cardului | Definiție
Application (Cerere) | AEC a primit o cerere de eliberare a unui card de conducător auto. Aceste informații au fost înregistrate și stocate în baza de date cu cheile de căutare generate.
Approved (Aprobat) | AEC a aprobat cererea de eliberare a unui card de tahograf.
Rejected (Respins) | AEC nu a aprobat cererea.
Personalised (Personalizat) | Cardul de tahograf a fost personalizat.
Dispatched (Expediat) | Autoritatea națională a expediat cardul de conducător auto conducătorului auto sau agenției de livrare corespunzătoare.
Handed Over (Înmânat) | Autoritatea națională a înmânat cardul de conducător auto conducătorului auto.
Confiscated (Confiscat) | Cardul de conducător auto a fost preluat de la conducătorul auto de către autoritatea competentă.
Suspended (Suspendat) | Cardul de conducător auto a fost preluat temporar de la conducătorul auto.
Withdrawn (Retras) | AEC a decis să retragă cardul de conducător auto. Cardul a fost anulat definitiv.
Surrendered (Predat) | Cardul de tahograf a fost returnat AEC și a fost declarat inutil.
Lost (Pierdut) | Cardul de tahograf a fost declarat pierdut la AEC.
Stolen (Furat) | Cardul de tahograf a fost declarat furat la AEC. Un card furat este considerat pierdut.
Malfunctioning (Defect) | Cardul de tahograf a fost declarat defect la AEC.
Expired (Expirat) | Perioada de valabilitate a cardului de tahograf a expirat.
Replaced (Înlocuit) | Cardul de tahograf, care a fost declarat pierdut, furat sau defect, a fost înlocuit cu un nou card. Datele de pe noul card sunt aceleași, cu excepția indicelui de înlocuire din numărul cardului, care a fost mărit cu o unitate.
Renewed (Reînnoit) | Cardul de tahograf a fost reînnoit în urma modificării unor date administrative sau a expirării perioadei de valabilitate. Datele de pe noul card sunt aceleași, cu excepția indicelui de reînnoire din numărul cardului, care a fost mărit cu o unitate.
In Exchange (În curs de schimbare) | AEC care a eliberat un card de conducător auto a primit o notificare prin care este anunțată că a fost demarată procedura de schimbare a cardului respectiv cu un card de conducător auto eliberat de către AEC din alt stat membru.
Exchanged (Schimbat) | AEC care a eliberat un card de conducător auto a primit o notificare prin care este anunțată că a fost finalizată procedura de schimbare a cardului respectiv cu un card de conducător auto eliberat de către AEC din alt stat membru.
ANEXA III
Dispoziții privind mesajele în sistemul de mesagerie TACHOnet
1. Cerințe tehnice generale
1.1. Hubul central asigură atât interfețe sincrone, cât și asincrone pentru schimbul de mesaje. Statele membre pot alege tehnologia cea mai adecvată pentru interfața cu aplicațiile proprii.
1.2. Toate mesajele schimbate între hubul central și sistemele naționale trebuie să fie codificate UTF-8.
1.3. Sistemele naționale trebuie să aibă capacitatea de a primi și de a procesa mesaje care conțin caractere grecești sau chirilice.
2. Structura mesajelor XML și definiția schemei (XSD)
2.1. Structura generală a mesajelor XML respectă formatul definit de schemele XSD instalate în hubul central.
2.2. Hubul central și sistemele naționale transmit și recepționează mesaje care sunt conforme cu schema XSD a mesajelor.
2.3. Sistemele naționale au capacitatea de a transmite, de a recepționa și de a procesa toate mesajele care corespund oricăreia dintre funcțiile prevăzute în anexa I.
2.4. Mesajele XML trebuie să includă cel puțin cerințele minime prevăzute în apendicele la prezenta anexă.
Apendice
Cerințele minime pentru conținutul mesajelor XML
Antet comun | Obligatoriu
Version (Versiune) | Versiunea oficială a specificațiilor XML va fi stabilită prin spațiul de nume (namespace) definit în XSD a mesajului și în atributul version din elementul antet al oricărui mesaj XML. Numărul versiunii („n.m”) va fi definit ca valoare fixă la fiecare lansare a fișierului de definiție a schemei XML (xsd). | Da
Test Identifier (Identificator testare) | ID opțional pentru testare. Inițiatorul testului va completa ID-ul, iar toți ceilalți participanți la fluxul de lucru vor redirecționa/returna același ID. În producție trebuie ignorat și nu va fi folosit dacă este furnizat. | Nu
Technical Identifier (Identificator tehnic) | Un UUID care identifică în mod unic fiecare mesaj. Expeditorul generează un UUID și completează acest atribut. Această informație nu se utilizează în niciun scop legat de activitatea economică. | Da
Workflow Identifier (Identificator flux de lucru) | Identificatorul fluxului de lucru este un UUID și ar trebui să fie generat de statul membru solicitant. Acest ID este apoi utilizat în toate mesajele pentru a corela fluxul de lucru. | Da
Sent At (Transmis la) | Data și ora (UTC) la care a fost transmis mesajul. | Da
Timeout (Timpul a expirat) | Acesta este un atribut opțional de dată și de oră (în format UTC). Această valoare va fi stabilită doar de hub pentru solicitările redirecționate. Aceasta va informa statul membru respondent cu privire la ora la care expiră solicitarea. Această valoare nu este necesară în mesajele MS2TCN_<x>_Req și în mesajele de răspuns. Utilizarea sa este facultativă, astfel încât să se poată folosi aceeași definiție de antet pentru toate tipurile de mesaje, indiferent dacă atributul timeoutValue este necesar sau nu. | Nu
From (De la) | Codul ISO 3166-1 alfa 2 al statului membru care transmite mesajul sau „UE”. | Da
To (Către) | Codul ISO 3166-1 alfa 2 al statului membru căruia i se transmite mesajul sau „UE”. | Da
Check Issued Cards Request (Solicitare de verificare a cardurilor eliberate) | Obligatoriu
Family Name (Nume de familie) | Numele de familie al conducătorului auto, astfel cum este înscris pe card. | Da
First Name (Prenume) | Prenumele conducătorului auto, astfel cum este înscris pe card (lipsa unui prenume nu indică o căutare cu metacaractere). | Nu
Date of Birth (Data nașterii) | Data nașterii conducătorului auto, astfel cum este înscrisă pe card. | Da
Driving Licence Number (Numărul permisului de conducere) | Numărul permisului de conducere al conducătorului auto. | Nu
Driving Licence Issuing Country (Țara de eliberare a permisului de conducere) | Țara care a eliberat permisul de conducere al conducătorului auto. | Nu
Check Issued Cards Response (Răspuns de verificare a cardurilor eliberate) | Obligatoriu
Status Code (Cod de stare) | Codul de stare al căutării [de ex. found (găsit), not found (nu a fost găsit), error (eroare), etc.]. | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Found Driver Details (Datele conducătorului auto găsit) | Da
Family Name (Nume de familie) | Numele de familie ale conducătorilor auto găsiți. | Da
First Name (Prenume) | Prenumele conducătorilor auto găsiți. | Nu
Date of Birth (Data nașterii) | Datele de naștere ale conducătorilor auto găsiți. | Da
Place of Birth (Locul nașterii) | Locurile de naștere ale conducătorilor auto găsiți. | Nu
Driver Card Number (Numărul cardului de conducător auto) | Numărul cardului conducătorului auto găsit. | Da
Driver Card Status (Starea cardului de conducător auto) | Starea cardului conducătorului auto găsit. | Da
Driver Card Issuing Authority (Autoritatea emitentă a cardului de conducător auto) | Denumirea autorității care a eliberat cardul conducătorului auto găsit. | Da
Driver Card Start of Validity Date (Data de la care este valabil cardul de conducător auto) | Data de la care este valabil cardul conducătorului auto găsit. | Da
Driver Card Expiry Date (Data de expirare a cardului de conducător auto) | Data de expirare a cardului conducătorului auto găsit. | Da
Driver Card Status Modified Date (Data de modificare a stării cardului de conducător auto) | Data la care a fost modificat ultima dată cardul conducătorului auto găsit. | Da
Search Mechanism (Mecanism de căutare) | Cardul a fost găsit în urma unei căutări NYSIIS sau în urma unei căutări personalizate. | Da
Temporary Card (Card temporar) | Cardul găsit este un card temporar. | Nu
Driving Licence Number (Numărul permisului de conducere) | Numărul permisului de conducere al conducătorului auto găsit. | Da
Driving Licence Issuing Country (Țara de eliberare a permisului de conducere) | Țara care a eliberat permisul de conducere al conducătorului auto găsit. | Da
Driving Licence Status (Starea permisului de conducere) | Starea permisului de conducere al conducătorului auto găsit. | Nu
Driving Licence Issuing Date (Data de eliberare a permisului de conducere) | Data de eliberare a permisului de conducere al conducătorului auto găsit. | Nu
Driving Licence Expiry Date (Data de expirare a permisului de conducere) | Data de expirare a permisului de conducere al conducătorului auto găsit. | Nu
Check Card Status Request (Solicitare de verificare a stării cardului) | Obligatoriu
Driver Card Number (Numărul cardului de conducător auto) | Numărul cardului pentru care sunt solicitate detalii. | Da
Check Card Status Response (Răspuns de verificare a stării cardului) | Obligatoriu
Status Code (Cod de stare) | Codul de stare al solicitării de detalii [de ex. found (găsit), not found (nu a fost găsit), error (eroare) etc.]. | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Card Status (Starea cardului) | Starea cardului solicitat. | Da
Card Issuing Authority (Autoritatea emitentă a cardului) | Denumirea autorității care a eliberat cardul solicitat. | Da
Card Start of Validity Date (Data de la care este valabil cardul) | Data de la care este valabil cardul solicitat. | Da
Card Expiry Date (Data de expirare a cardului) | Data de expirare a cardului solicitat. | Da
Card Status Modified Date (Data de modificare a stării cardului) | Data la care a fost modificat ultima dată cardul solicitat. | Da
Valid for Driving (Valabil pentru conducerea unui autovehicul) | Cardul găsit este/nu este valabil pentru a conduce un autovehicul. | Da
Temporary Card (Card temporar) | Cardul găsit este un card temporar. | Nu
Workshop Card (Card de atelier)
Workshop Name (Denumirea atelierului) | Denumirea atelierului pentru care a fost eliberat cardul. | Da
Workshop Address (Adresa atelierului) | Adresa atelierului pentru care a fost eliberat cardul. | Da
Family Name (Nume de familie) | Numele de familie al persoanei pentru care a fost eliberat cardul. | Nu
First Name (Prenume) | Prenumele persoanei pentru care a fost eliberat cardul. | Nu
Date of Birth (Data nașterii) | Data nașterii persoanei pentru care a fost eliberat cardul. | Nu
Card Holder Details (Datele titularului cardului)
Family Name (Nume de familie) | Numele de familie al conducătorului auto pentru care a fost eliberat cardul. | Da
First Name (Prenume) | Prenumele conducătorului auto pentru care a fost eliberat cardul. | Nu
Date of Birth (Data nașterii) | Data nașterii conducătorului auto pentru care a fost eliberat cardul. | Da
Place of Birth (Locul nașterii) | Locul nașterii conducătorului auto pentru care a fost eliberat cardul. | Nu
Driving Licence Number (Numărul permisului de conducere) | Numărul permisului de conducere al conducătorului auto pentru care a fost eliberat cardul. | Da
Driving Licence Issuing Country (Țara de eliberare a permisului de conducere) | Țara care a eliberat permisul de conducere al conducătorului auto pentru care a fost eliberat cardul. | Da
Driving Licence Status (Starea permisului de conducere) | Starea permisului de conducere al conducătorului auto pentru care a fost eliberat cardul. | Nu
Driving Licence Issuing Date (Data de eliberare a permisului de conducere) | Data de eliberare a permisului de conducere al conducătorului auto pentru care a fost eliberat cardul. | Nu
Driving Licence Expiry Date (Data de expirare a permisului de conducere) | Data de expirare a permisului de conducere al conducătorului auto pentru care a fost eliberat cardul. | Nu
Modify Card Status Request (Solicitare de modificare a stării cardului) | Obligatoriu
Driver Card Number (Numărul cardului de conducător auto) | Numărul cardului a cărui stare a fost modificată. | Da
New Driver Card Status (Noua stare a cardului de conducător auto) | Starea în care se află cardul în urma modificării. | Da
Modification Reason (Motivul modificării) | Motivul (text liber) care stă la baza modificării stării cardului. | Nu
Driver Card Status Modified Date (Data de modificare a stării cardului de conducător auto) | Data și ora la care s-a modificat starea cardului. | Da
Declared By (Declarat de)
Authority (Autoritatea) | Denumirea autorității care a operat modificarea stării cardului. | Da
Family Name (Nume de familie) | Numele de familie al persoanei care a operat modificarea stării cardului. | Nu
First Name (Prenume) | Prenumele persoanei care a operat modificarea stării cardului. | Nu
Phone (Telefon) | Numărul de telefon al persoanei care a operat modificarea stării cardului. | Nu
E-mail | Adresa de e-mail a persoanei care a operat modificarea stării cardului. | Nu
Modify Card Status Acknowledgement (Confirmare de recepție a modificării stării cardului) | Obligatoriu
Status Code (Cod de stare) | Codul de stare al confirmării [de ex. ok (OK), not found (nu a fost găsit), error (eroare) etc.]. | Da
Acknowledgement type (Tip de confirmare) | Tipul de confirmare: pentru solicitare sau răspuns | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Modify Card Status Response (Răspuns privind modificarea stării cardului) | Obligatoriu
Status Code (Cod de stare) | Codul de stare al actualizării registrului [de ex. ok (OK), not ok (nu este OK), error (eroare) etc.]. | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Issued Card Driving License Request (Solicitare privind permisul de conducere pe baza căruia a fost eliberat un card) | Obligatoriu
Driver Card Number (Numărul cardului de conducător auto) | Numărul cardului de conducător auto care a fost eliberat. | Da
Driving Licence Number (Numărul permisului de conducere) | Numărul permisului de conducere străin care a fost utilizat pentru a solicita cardul de conducător auto. | Da
Issued Card Driving License Response (Răspuns privind permisul de conducere pe baza căruia a fost eliberat un card) | Obligatoriu
Status Code (Cod de stare) | Un cod de stare care confirmă recepția notificării [de ex. ok (OK), not ok (nu este OK), error (eroare) etc.]. | Da
Status Message (Mesaj de stare) | O descriere explicativă a stării (dacă este necesară). | Nu
Family Name (Nume de familie) | Numele de familie al conducătorului auto pentru care a fost eliberat cardul. | Da
First Name (Prenume) | Prenumele conducătorului auto pentru care a fost eliberat cardul. | Nu
Date of Birth (Data nașterii) | Data nașterii conducătorului auto pentru care a fost eliberat cardul. | Da
ANEXA IV
Servicii de transliterare și NYSIIS (New York State Identification and Intelligence System)
1. Algoritmul NYSIIS implementat în hubul central este folosit pentru a codifica numele tuturor conducătorilor auto în registrul național.
2. La căutarea unui card prin intermediul funcției CIC se utilizează cheile NYSIIS ca mecanism principal de căutare.
3. În plus, statele membre pot utiliza un algoritm personalizat pentru a obține mai multe rezultate.
4. Rezultatele căutării trebuie să indice mecanismul de căutare care a fost utilizat pentru a găsi o înregistrare, fie NYSIIS, fie un algoritm personalizat.
5. În cazul în care un stat membru alege să înregistreze notificările ICDL, atunci cheile NYSIIS conținute în notificare se înregistrează ca parte a datelor ICDL.
5.1. La căutarea datelor ICDL, statul membru utilizează cheile NYSIIS ale numelui solicitantului.
ANEXA V
Cerințe privind securitatea
1. Pentru schimbul de mesaje între hubul central și sistemele naționale se utilizează protocolul HTTPS.
2. Sistemele naționale utilizează certificatele PKI furnizate de Comisie pentru a securiza transmiterea de mesaje între sistemul național și hubul central.
3. Sistemele naționale implementează cel puțin certificate care utilizează algoritmul hash semnătură SHA-2 (SHA-256) și o lungime a cheilor publice de 2 048 de octeți.
ANEXA VI
Nivelurile serviciului
1. Sistemele naționale trebuie să asigure următorul nivel minim de serviciu:
1.1. ele trebuie să fie disponibile 24 de ore pe zi, 7 zile pe săptămână;
1.2. disponibilitatea lor este monitorizată prin intermediul unui mesaj heartbeat emis de hubul central;
1.3. rata lor de disponibilitate trebuie să fie de 98 %, în conformitate cu tabelul următor (cifrele au fost rotunjite până la cea mai apropiată unitate):
O disponibilitate de | înseamnă o indisponibilitate de
Zilnică | Lunară | Anuală
98 % | 0,5 ore | 15 ore | 7,5 zile
Statele membre sunt încurajate să respecte rata de disponibilitate zilnică; cu toate acestea, este recunoscut faptul că anumite activități necesare, cum ar fi întreținerea sistemului, necesită o perioadă de indisponibilitate de peste 30 de minute. Totuși, ratele de disponibilitate lunare și anuale rămân obligatorii;
1.4. statele membre trebuie să răspundă la minimum 98 % din solicitările care sunt redirecționate către ele într-o lună calendaristică;
1.5. ele trebuie să răspundă solicitărilor în termen de cel mult 10 secunde;
1.6. durata globală de așteptare a solicitării (timpul în care solicitantul poate să aștepte un răspuns) nu trebuie să depășească 20 de secunde;
1.7. ele trebuie să fie în măsură să proceseze solicitările la o rată de 6 mesaje pe secundă;
1.8. Sistemele naționale nu pot transmite solicitări către hubul TACHOnet la o rată care depășește 2 solicitări pe secundă;
1.9. fiecare sistem național trebuie să poată face față eventualelor probleme tehnice ale hubului central sau ale sistemelor naționale din alte state membre. Acestea includ, dar nu se limitează la:
(a) pierderea legăturii cu hubul central;
(b) neprimirea unui răspuns la o solicitare;
(c) primirea răspunsurilor după ce durata de așteptare a mesajului a expirat;
(d) primirea de mesaje nesolicitate;
(e) primirea de mesaje incorecte.
2. Hubul central trebuie:
2.1. să aibă o rată de disponibilitate de 98 %;
2.2. să transmită către sistemele naționale notificări ale oricăror erori, fie prin intermediul mesajului de răspuns, fie prin intermediul unui mesaj de eroare specific. Sistemele naționale, la rândul lor, trebuie să primească aceste mesaje de eroare specifice și să dispună de un flux de lucru progresiv (escalation workflow) pentru a lua toate măsurile adecvate în vederea remedierii erorii notificate.
3. Întreținere
Statele membre trebuie să notifice celorlalte state membre și Comisiei orice activități de întreținere de rutină prin intermediul aplicației web, cu cel puțin o săptămână înainte de începerea acestor activități, dacă este posibil din punct de vedere tehnic.
ANEXA VII
Registrul și statisticile datelor colectate la nivelul hubului central
1. Pentru a se asigura confidențialitatea, datele prezentate în scopuri statistice trebuie să fie anonimizate. Datele de identificare a unui anumit card, conducător auto sau permis de conducere nu sunt disponibile în scopuri statistice.
2. Informațiile din registru trebuie să țină evidența tuturor tranzacțiilor, în scopul monitorizării și al corectării erorilor sistemului, și să permită generarea de statistici cu privire la respectivele tranzacții.
3. Datele cu caracter personal nu sunt păstrate în registre mai mult de 6 luni. Informațiile statistice sunt păstrate pe o perioadă nedeterminată.
4. Datele statistice utilizate pentru raportare trebuie să includă:
(a) statul membru solicitant;
(b) statul membru respondent;
(c) tipul de mesaj;
(d) codul de stare al răspunsului;
(e) data și ora mesajelor;
(f) timpul de răspuns.
ANEXA VIII
Utilizarea sistemului de mesagerie TACHOnet
1. Eliberarea cardurilor de conducător auto
1.1. În cazul în care solicitantul unui card de conducător auto deține un permis de conducere eliberat într-un stat membru diferit de statul membru în care depune cererea, se efectuează o căutare pluridirecțională Check Issued Card de către statul membru în care se depune cererea.
1.2. Statele membre care eliberează un card de conducător auto pentru un conducător auto care deține un permis de conducere eliberat într-un alt stat membru trebuie să notifice imediat respectivului stat membru, prin intermediul funcției Issued Card Driving Licence, faptul că a fost eliberat un card de conducător auto.
1.3. În cazul în care solicitantul unui card de conducător auto deține un permis de conducere eliberat în statul membru în care depune cererea și pentru care a fost înregistrată anterior o notificare ICDL în registrul național aferent, statul membru trebuie să efectueze o căutare CIC sau Check Card Status unidirecțională adresată statului membru care a transmis notificarea ICDL.
1.4. Fiecare notificare ICDL se înregistrează în registrul național al statului membru care o primește.
1.5. Statele membre efectuează o căutare CIC pluridirecțională pentru cel puțin 30 % din cererile prezentate de către conducătorii auto care dețin un permis de conducere eliberat în statul membru respectiv.
1.6. Statele membre pot alege să nu utilizeze funcția ICDL astfel cum se prevede la punctele 1.3-1.5. În acest caz, ele efectuează o căutare CIC pluridirecțională pentru fiecare cerere primită.
1.7. Statele membre notifică Comisiei, cel târziu până la data de aplicare a prezentului regulament, dacă vor înregistra notificările ICDL în registrele lor naționale sau dacă vor urma procedura de la punctul 1.6.
1.8. Statele membre care, timp de cinci ani sau mai puțin înainte de data de aplicare a prezentului regulament, nu au înregistrat notificările ICDL în registrele lor naționale, astfel cum se prevede la punctul 1.4, efectuează o căutare CIC pluridirecțională pentru 100 % din cereri, cu excepția permiselor de conducere pentru care s-a înregistrat o notificare ICDL, caz în care se aplică punctul 1.3.
1.9. Obligația prevăzută la punctul 1.8 se aplică pentru o perioadă de cinci ani începând de la data la care a fost pusă efectiv în aplicare înregistrarea notificărilor ICDL în registrul național al fiecărui stat membru.
2. Carduri de conducător auto retrase, suspendate sau furate
2.1. În cazul în care, în conformitate cu articolul 26 alineatul (7) și cu articolul 29 alineatul (2) din Regulamentul (UE) nr. 165/2014, un card de conducător auto a fost retras, suspendat sau declarat furat într-un alt stat membru decât statul membru emitent, autoritatea competentă din primul stat membru:
(a) verifică starea actuală a cardului prin transmiterea unei solicitări CCS către statul membru emitent. În cazul în care numărul de card nu este cunoscut, se transmite o solicitare CIC unidirecțională înainte de transmiterea solicitării CCS menționate anterior;
(b) transmite o notificare MCS prin intermediul sistemului de mesagerie TACHOnet statului membru emitent.
3. Schimbarea cardurilor de conducător auto
3.1. În cazul în care titularul unui card de conducător auto depune o cerere de schimbare a cardului de conducător auto într-un alt stat membru decât statul membru emitent, autoritatea competentă din primul stat membru verifică starea reală a cardului prin transmiterea unei solicitări CCS statului membru emitent.
3.2. După ce starea cardului de conducător auto a fost verificată și permite schimbarea, autoritatea competentă din statul membru în care a fost depusă cererea transmite statului membru emitent o solicitare MCS prin intermediul sistemului de mesagerie TACHOnet.
3.3. Statele membre care reînnoiesc sau schimbă un card de conducător auto pentru un conducător auto care deține un permis de conducere eliberat într-un alt stat membru trebuie să notifice imediat statului membru emitent, prin intermediul funcției ICDL, faptul că a fost reînnoit sau schimbat cardul de conducător auto.
