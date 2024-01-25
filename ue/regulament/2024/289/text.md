REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2024/289 AL COMISIEI
din 12 ianuarie 2024
de modificare a Regulamentului de punere în aplicare (UE) 2016/323 în ceea ce privește datele necesare pentru documentele de asistență administrativă reciprocă referitoare la deplasările de produse accizabile destinate a fi exportate în regim suspensiv de accize în conformitate cu Regulamentul (UE) nr. 389/2012 al Consiliului
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) nr. 389/2012 al Consiliului din 2 mai 2012 privind cooperarea administrativă în domeniul accizelor și de abrogare a Regulamentului (CE) nr. 2073/2004 (1), în special articolul 9 alineatul (2), articolul 15 alineatul (5) și articolul 16 alineatul (3),
întrucât:
(1) Directiva (UE) 2020/262 a Consiliului (2) stabilește procedura care trebuie urmată în cazul deplasărilor de produse accizabile între statele membre, precum și procedurile aplicabile deplasărilor de produse accizabile care sunt exportate în afara Uniunii și monitorizarea și supravegherea acestor deplasări prin intermediul sistemului informatizat menționat la articolul 1 din Decizia (UE) 2020/263 a Parlamentului European și a Consiliului (3) (denumit în continuare „sistemul informatizat”).
(2) Articolul 21 alineatul (5) din Directiva (UE) 2020/262 impune autorităților competente din statul membru de export să trimită, prin intermediul sistemului informatizat, o notificare autorităților competente din statul membru de expediție, în cazul în care produsele nu vor mai fi scoase de pe teritoriul vamal al Uniunii.
(3) Regulamentul de punere în aplicare (UE) 2016/323 al Comisiei (4) stabilește normele privind cooperarea și schimbul de informații între statele membre în ceea ce privește deplasările de produse aflate în regim suspensiv de accize. Pentru a ține seama de modificările introduse prin articolul 21 alineatul (5) din Directiva (UE) 2020/262, este necesar să se modifice datele necesare pentru documentele de asistență administrativă reciprocă menționate la articolul 9 alineatul (2), la articolul 15 alineatul (5) și la articolul 16 alineatul (3) din Regulamentul (UE) nr. 389/2012 pentru a permite schimbul de informații pentru deplasările de produse accizabile destinate a fi exportate în regim suspensiv de accize, astfel încât autoritățile competente să poată controla și aceste deplasări ale produselor supuse accizelor.
(4) Prin urmare, Regulamentul de punere în aplicare (UE) 2016/323 trebuie modificat în consecință.
(5) Se preconizează că sistemul informatizat va fi interconectat cu sistemul automatizat de export al UE până la 13 februarie 2024, când notificările menționate la articolul 21 alineatul (5) din Directiva (UE) 2020/262 nu vor mai putea fi efectuate prin alte mijloace decât prin sistemul informatizat, astfel cum se prevede la articolul 54 din directiva respectivă. Întrucât prezentul regulament se referă la procedurile aplicabile deplasărilor produselor accizabile aflate în regim suspensiv de accize care sunt exportate în afara Uniunii, aplicarea prezentului regulament ar trebui amânată până la acea dată.
(6) Măsurile prevăzute în prezentul regulament sunt conforme cu avizul Comitetului pentru accize,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Anexele I și II la Regulamentul de punere în aplicare (UE) 2016/323 se modifică în conformitate cu anexa la prezentul regulament.
Articolul 2
Prezentul regulament intră în vigoare în a treia zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Se aplică de la 13 februarie 2024.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 12 ianuarie 2024.
Pentru Comisie
Președinta
Ursula VON DER LEYEN
(1) JO L 121, 8.5.2012, p. 1.
(2) Directiva (UE) 2020/262 a Consiliului din 19 decembrie 2019 de stabilire a regimului general al accizelor (JO L 58, 27.2.2020, p. 4).
(3) Decizia (UE) 2020/263 a Parlamentului European și a Consiliului din 15 ianuarie 2020 privind informatizarea circulației și a controlului produselor accizabile (JO L 58, 27.2.2020, p. 43).
(4) Regulamentul de punere în aplicare (UE) 2016/323 al Comisiei din 24 februarie 2016 de stabilire a unor norme detaliate referitoare la cooperarea și schimbul de informații între statele membre în ceea ce privește mărfurile aflate în regim suspensiv de accize în conformitate cu Regulamentul (UE) nr. 389/2012 al Consiliului (JO L 66, 11.3.2016, p. 1).
ANEXĂ
Anexele I și II la Regulamentul de punere în aplicare (UE) 2016/323 se modifică după cum urmează:
1. În anexa I, tabelele 1-16 se înlocuiesc cu următorul text:
„Tabelul 1
(menționat la articolul 4)
Cerere de descărcare a deplasării
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Identificator de corelare a cererii | R | | Valoarea câmpului <Identificator de corelare a cererii> este unică pentru fiecare stat membru. | an..44
2 | e-AD/e-SAD PRIVIND DEPLASAREA DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
| c | Indicatorul „Informații solicitate privind deplasarea națională” | R | | Formatul Boolean este digital: „0” sau „1” („0” = Nu sau Fals; „1” = Da sau Adevărat) | n1
| d | Statut | R | | Valorile posibile sunt: — X01 = Acceptat — X02 = Anulat — X03 = Livrat — X04 = Deviat — X05 = Respins — X06 = Înlocuit — X07 = e-AD/e-SAD închis manual — X08 = Refuzat — X09 = Nul/Inexistent — X10 = Refuzat parțial — X11 = Export în curs — X12 = Acceptat pentru export — X13 = Oprit — X14 = Declarație de export acceptată — X15 = Cerere de e-AD acceptată pentru export | an3
| e | Tipul ultimului mesaj primit | R | | Valorile posibile sunt: — IE801 = E-AD/E-SAD — IE803 = NOTIFICARE PRIVIND UN E-AD/E-SAD DEVIAT — IE807 = INTRERUPEREA DEPLASĂRII — IE810 = ANULAREA UNUI E-AD — IE813 = SCHIMBAREA DESTINAȚIEI — IE818 = RAPORT DE PRIMIRE/EXPORT ACCEPTAT SAU (PARȚIAL) REFUZAT — IE819 = ALERTĂ SAU RESPINGERE A UNUI E-AD/E-SAD — IE829 = NOTIFICARE DE ACCEPTARE A EXPORTULUI — IE836 = NOTIFICARE DE INVALIDARE A DECLARAȚIEI DE EXPORT CĂTRE ASM DE EXPEDIȚIE/A EXPEDITORULUI — IE839 = RESPINGEREA DE CĂTRE AUTORITĂȚILE VAMALE A E-AD — IE881 = RĂSPUNS PRIVIND ÎNCHIDEREA MANUALĂ — IE905 = CONFIRMAREA STATUTULUI — None = NUL/INEXISTENT Notă: | Mesajul IE905 ar trebui inclus numai pentru deplasările istorice care au fost închise manual prin intermediul unui mesaj IE905. | an..5
| f | Tipul de mesaj al cererii privind statutul | O | | Valorile posibile sunt: — 1 = Cerere de sincronizare a statutului — 2 = Cerere privind istoricul deplasării | n1
Tabelul 2
(menționat la articolul 4)
Răspuns la cererea de descărcare a deplasării
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Identificator de corelare a cererii | R | | Valoarea câmpului <Identificator de corelare a cererii> este unică pentru fiecare stat membru. | an..44
2 | e-AD/e-SAD PRIVIND DEPLASAREA DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
| c | Statut | R | | Valorile posibile ale câmpului <Statut> sunt: — X01 = Acceptat — X02 = Anulat — X03 = Livrat — X04 = Deviat — X05 = Respins — X06 = Înlocuit — X07 = e-AD/e-SAD închis manual — X08 = Refuzat — X09 = Nul/Inexistent — X10 = Refuzat parțial — X11 = Export în curs — X12 = Acceptat pentru export — X13 = Oprit — X14 = Declarație de export acceptată — X15 = Cerere de e-AD acceptată pentru export | an3
| d | Tipul ultimului mesaj primit | | | Valorile posibile sunt: — IE801 = E-AD/E-SAD — IE803 = NOTIFICARE PRIVIND UN E-AD/E-SAD DEVIAT — IE807 = INTRERUPEREA DEPLASĂRII — IE810 = ANULAREA UNUI E-AD — IE813 = SCHIMBAREA DESTINAȚIEI — IE818 = RAPORT DE PRIMIRE/EXPORT ACCEPTAT SAU (PARȚIAL) REFUZAT — IE819 = ALERTĂ SAU RESPINGERE A UNUI E-AD/E-SAD — IE829 = NOTIFICARE DE ACCEPTARE A EXPORTULUI — IE836 = NOTIFICARE DE INVALIDARE A DECLARAȚIEI DE EXPORT CĂTRE ASM DE EXPEDIȚIE/A EXPEDITORULUI — IE839 = RESPINGEREA E-AD DE CĂTRE AUTORITĂȚILE VAMALE — IE881 = RĂSPUNS PRIVIND ÎNCHIDEREA MANUALĂ — IE905 = CONFIRMAREA STATUTULUI — None = NUL/INEXISTENT Notă: | Mesajul IE905 ar trebui inclus numai pentru deplasările istorice care au fost închise manual prin intermediul unui mesaj IE905. | an..5
Tabelul 3
(menționat la articolul 4)
Istoricul deplasării
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Identificator de corelare a cererii | R | | Valoarea câmpului <Identificator de corelare a cererii> este unică pentru fiecare stat membru. | an..44
2 | Toate e-AD-urile/e-SAD-urile validate | R | | Ansamblul tuturor proiectelor de documente administrative electronice (simplificate) sau al tuturor documentelor administrative electronice (simplificate) referitoare la o deplasare, a căror structură este prezentată în tabelul 1 din anexa I la Regulamentul delegat (UE) 2022/1636 | 99x
3 | Toate rapoartele de primire/export | O | | Ansamblul tuturor mesajelor „Raport de primire/Raport de export” referitoare la o deplasare, a căror structură este prezentată în tabelul 6 din anexa I la Regulamentul delegat (UE) 2022/1636 | 99x
4 | Ultima notificare privind un e-AD deviat | O | | Conținutul ultimului mesaj „Notificare de schimbare a destinației/Notificare de divizare” referitor la o deplasare, a cărui structură este prezentată în tabelul 4 din anexa I la Regulamentul delegat (UE) 2022/1636 | 1x
5 | Toate rapoartele de control | O | | Setul tuturor mesajelor „Raport de control” referitoare la o deplasare, a căror structură este prezentată în tabelul 11 | 99x
6 | Toate rapoartele de eveniment | O | | Setul tuturor mesajelor „Raport de eveniment” referitoare la o deplasare, a căror structură este prezentată în tabelul 12 | 99x
7 | Toate explicațiile întârzierilor la livrare | O | | Setul tuturor mesajelor „Explicație a întârzierii la livrare” referitoare la o deplasare | 99x
7.1 | ATRIBUTE | R | | |
| a | Rolul mesajului | R | | Valorile posibile sunt: — 1 = Explicație a întârzierii în transmiterea raportului de primire/export — 2 = Explicație a întârzierii în indicarea destinației | n1
| b | Data și ora validării explicației întârzierii | C | – „R” după validarea cu succes – Nu se aplică în alte cazuri | | dateTime
| c | Tipul depunătorului | R | | Valorile posibile sunt: — 1 = Expeditor — 2 = Destinatar | n1
| d | Identificatorul depunătorului | R | | <Identificatorul depunătorului> este un cod de acciză valid al operatorului. [a se vedea lista de coduri 1 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| e | Codul explicației | R | | (a se vedea lista de coduri 7 din anexa II) | n..2
| f | Informații complementare | C | — „R” dacă <Codul explicației> este „Altele” — „O” în celelalte cazuri (a se vedea Codul explicației, în caseta 7.1e) | | an..350
| g | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
7.2 | DEPLASARE DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
8 | Toate notificările de acceptare a exportului | O | | Setul tuturor mesajelor „Notificare de acceptare a exportului” referitoare la deplasare | 99x
8.1 | ATRIBUTE | R | | |
| a | Data și ora emiterii | R | | | dateTime
8.2 | e-AD PRIVIND DEPLASAREA DE PRODUSE ACCIZABILE | R | | | 99x
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
| c | Acceptarea declarației de export sau Acordarea liberului de vamă pentru export | R | | Valori posibile: 0 = Nu sau Fals 1 = Da sau Adevărat 0 corespunde acceptării declarației de export, iar 1 corespunde acordării liberului de vamă pentru export. | n1
8.3 | OPERATOR Destinatar | R | | |
| a | Identificarea operatorului | C | — „R” dacă <Codul tipului de destinație> este: — „Destinație – Antrepozit fiscal” — „Destinație – Destinatar înregistrat” — „Destinație – Destinatar înregistrat temporar” — „Destinație – Livrare directă” — „O” dacă <Codul tipului de destinație> este: — „Destinație – Export” — Nu se aplică în alte cazuri | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Numărul EORI | C | — „O” pentru Codul tipului de destinație „6” — Nu se aplică în alte cazuri [A se vedea caseta 1a din tabelul 1 din anexa I la Regulamentul delegat (UE) 2022/1636] | Specificați numărul EORI al persoanei responsabile cu depunerea declarației de export, așa cum se prevede la articolul 21 alineatul (2) din Directiva (UE) 2020/262 a Consiliului. | an..17
| c | Denumirea operatorului | R | | | an..182
| d | Strada | R | | | an..65
| e | Numărul | O | | | an..11
| f | Codul poștal | R | | | an..10
| g | Localitatea | R | | | an..50
| h | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
8.4 | BIROUL VAMAL Locul de export | O | | |
| a | Numărul de referință | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
8.5 | ACCEPTAREA/ELIBERAREA DECLARAȚIEI DE EXPORT | R | | |
| a | Numărul de referință al Biroului vamal al expeditorului | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| b | Identificatorul agentului vamal al expeditorului | O | | | an..35
| c | Data acceptării | C | — „R” pentru Acceptarea declarației de export — Nu se aplică pentru Acordarea liberului de vamă pentru export (A se vedea caseta 8.2c) | | data
| d | Data eliberării | C | — „R” pentru Acordarea liberului de vamă pentru export — Nu se aplică pentru Acceptarea declarației de export (A se vedea caseta 8.2c) | | data
| e | Numărul de referință al documentului | R | | Un MRN valabil confirmat de datele vamale, în funcție de situația vamală. MRN (Movement Reference Number) = număr de referință al deplasării | an..21
9 | Toate notificările de invalidare ale autorităților vamale | O | | Setul tuturor mesajelor de invalidare a declarației de export de către autoritățile vamale referitor la deplasare | 99x
9.1 | DEPLASARE DE PRODUSE ACCIZABILE | R | | | 999X
| a | Codul de referință administrativ | R | | Specificați codul ARC al e-AD. A se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636. | an21
| b | Număr secvențial | R | | Valoarea acestui câmp trebuie să fie mai mare ca zero. | n..2
9.1.1 | OPERAȚIUNEA DE EXPORT | R | | |
| a | MRN (numărul de referință principal) | R | | | an18
| b | Data invalidării | R | | | an10
9.1.2 | BIROUL VAMAL DE EXPORT | R | | |
| a | Numărul de referință | R | | Specificați codul biroului autorităților competente ale Statului membru de export responsabile cu controlul accizelor la locul de export. A se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636. | an8
9.1.3 | ASM DE EXPORT | R | | |
| a | Codul de țară | R | | Specificați statul membru pe teritoriul căruia se efectuează exportul produselor accizabile, utilizând Codul de țară din lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
9.1.4 | EXPEDIEREA MĂRFURILOR | O | | |
9.1.4.1 | DOCUMENTUL ANTERIOR | O | | | 999X
| a | Numărul secvențial | R | | | n..5
| b | Tip | R | | | an4
| c | Numărul de referință | R | | | an..70
10 | Toate notificările de invalidare ale autorităților vamale | O | | Setul tuturor mesajelor de refuz al e-AD-urilor, transmise de autoritățile vamale referitor la deplasare | 99x
10.1 | ATRIBUTE | R | | |
| a | Data și ora emiterii | R | | | dateTime
10.2 | Proiectul de e-AD în cauză | C | — „R” pentru Codurile motivului de respingere „1” sau „2” — Nu se aplică Codurilor motivului de respingere „4” și „5” (a se vedea Codul motivului de respingere, în caseta 10.4) | |
| a | Număr de referință local | R | | | an..22
10.3 | Toate e-AD-urile validate în cauză | C | — „R” pentru Codul motivului de respingere „4” sau „5” — Nu se aplică Codurilor motivului de respingere „1” și „2” (a se vedea Codul motivului de respingere, în caseta 10.4) | | 99X
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | | n..2
10.4 | RESPINGERE | R | | |
| a | Data și ora respingerii | R | | | dateTime
| b | Codul motivului de respingere | R | | Valorile posibile sunt: — 1 = Datele de import nu au fost găsite — 2 = Conținutul e-AD nu corespunde datelor de import — 3 = (rezervat) — 4 = Rezultat negativ al controlului încrucișat — 5 = Rezultat nesatisfăcător al controlului la biroul de export | n1
10.5 | INFORMAȚII PRIVIND DECLARAȚIA DE EXPORT | C | — „R” pentru Codul motivului de respingere „4” sau „5” — Nu se aplică Codurilor motivului de respingere „1” și „2” (a se vedea Codul motivului de respingere, în caseta 10.4b) | |
| a | Număr de referință local | C | — „R” pentru Codul motivului de respingere „4” — Nu se aplică Codului motivului de respingere „5” (A se vedea caseta 10.4b) | | an..22
| b | Numărul de referință al documentului | C | — „R” pentru Codul motivului de respingere „5” — Nu se aplică Codului motivului de respingere „4” (A se vedea caseta 4b) | Un MRN valabil confirmat de datele vamale, în funcție de situația vamală. MRN (Movement Reference Number) = număr de referință al deplasării | an..21
10.5.1 | REZULTAT NEGATIV AL VALIDĂRII PRIN CONTROL ÎNCRUCIȘAT | C | — „R” pentru Codul motivului de respingere „4” — Nu se aplică Codurilor motivului de respingere „1”, „2” și „5” (A se vedea Codul motivului de respingere, în caseta 10.4b) | | 99X
10.5.1.1 | REZULTATUL CONTROLULUI ÎNCRUCIȘAT UBR | R | | | 999X
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Numărul unic de referință al corpului de date | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..3
| c | Codul diagnosticului | R | | Valorile posibile sunt: — 1 = (rezervat) — 2 = Nu există un număr unic de referință al corpului (Body Record Unique Reference) în e-AD sau nu există un ARTICOL DE MARFĂ corespondent în declarația de export — 3 = (rezervat) — 4 = Greutatea/masa nu corespunde — 5 = (rezervat) — 6 = Codurile NC nu corespund — 7 = Greutatea/masa nu corespund, iar codurile NC nu corespund | n1
| d | Rezultatul validării | R | | Valori posibile: 0 = Nu sau Fals 1 = Da sau Adevărat 0 înseamnă că rezultatul validării este negativ, iar 1 înseamnă că rezultatul validării este pozitiv. | n1
| e | Motivul respingerii | O | | | an..512
10.5.1.1.1 | REZULTATUL CONTROLULUI ÎNCRUCIȘAT AL CODURILOR DIN NOMENCLATURA COMBINATĂ | C | — „R” dacă: — valoarea din caseta 10.5.1.1.d este „1” (Rezultatul validării este pozitiv), iar valoarea din caseta 10.5.1.1.c este „6” (Codul diagnosticului este „Codurile NC nu corespund”) sau; — dacă valoarea din caseta 10.5.1.1.d este „0” (Rezultatul validării este negativ); — Nu se aplică în alte cazuri | |
| a | Rezultatul validării | R | | Valori posibile: 0 = Nu sau Fals 1 = Da sau Adevărat 0 înseamnă că rezultatul validării este negativ, iar 1 înseamnă că rezultatul validării este pozitiv. | n1
| b | Motivul respingerii | O | | | an..512
10.5.1.1.2 | REZULTATUL CONTROLULUI ÎNCRUCIȘAT AL MASEI NETE | C | — „R”, dacă valoarea din caseta 10.5.1.1.d este „1” (Rezultatul validării este pozitiv), iar valoarea din caseta 10.5.1.1.c este „4” (Codul diagnosticului este „Greutatea/masa nu corespunde”); — Nu se aplică în alte cazuri. | |
| a | Rezultatul validării | R | | Valori posibile: 0 = Nu sau Fals 1 = Da sau Adevărat 0 înseamnă că rezultatul validării este negativ, iar 1 înseamnă că rezultatul validării este pozitiv. | n1
| b | Motivul respingerii | O | | | an..512
10.5.2 | Toate notificările de neacordare a liberului de vamă pentru export | C | — „R” pentru Codul motivului de respingere „5” — Nu se aplică Codurilor motivului de respingere „1”, „2” și „4” (A se vedea caseta 10.4b) | |
| a | Numărul de referință al documentului | R | | | an..21
10.6 | OPERATOR Destinatar | R | | |
| a | Identificarea operatorului | C | — „R” dacă <Codul tipului de destinație> este: — „Destinație – Antrepozit fiscal” — „Destinație – Destinatar înregistrat” — „Destinație – Destinatar înregistrat temporar” — „Destinație – Livrare directă” — „O” dacă <Codul tipului de destinație> este: — „Destinație – Export” — Nu se aplică în alte cazuri | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Numărul EORI | C | — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Specificați numărul EORI al persoanei responsabile cu prezentarea declarației de export, așa cum se prevede la articolul 21 alineatul (2) din Directiva (UE) 2020/262. | an..17
| c | Denumirea operatorului | R | | | an..182
| d | Strada | R | | | an..65
| e | Numărul | O | | | an..11
| f | Codul poștal | R | | | an..10
| g | Localitatea | R | | | an..50
| h | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp | a2
10.7 | BIROUL VAMAL Locul de export | O | | |
| a | Numărul de referință | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
11 | Întreruperea posibilă a deplasării | O | | Conținutul unui mesaj de tip „Întreruperea posibilă a deplasării” referitor la o deplasare, a cărui structură este prezentată în tabelul 13 | 1x
12 | Anularea posibilă a e-AD-ului | O | | Conținutul unui mesaj de tip „Anularea posibilă a e-AD” referitor la deplasare, a cărui structură este prezentată în tabelul 2 din anexa I la Regulamentul delegat (UE) 2022/1636 | 1x
13 | Toate schimbările destinației | O | | Setul tuturor mesajelor „Schimbarea destinației” referitoare la o deplasare, a căror structură este prezentată în tabelul 3 din anexa I la Regulamentul delegat (UE) 2022/1636 | 99x
14 | Toate alertele sau respingerile privind un e-AD/e-SAD | O | | Setul tuturor mesajelor „Alertă sau respingere privind un e-AD/e-SAD” referitoare la o deplasare, a căror structură este prezentată în tabelul 14 | 99x
14.1 | ATRIBUTE | R | | |
| a | Data și ora validării alertei sau respingerii | C | — „R” după validarea cu succes — Nu se aplică în alte cazuri | | dateTime
14.2 | DEPLASARE DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
14.3 | OPERATOR Destinatar | R | | |
| a | Identificarea operatorului | C | — „R” dacă <Codul tipului de destinație> este: — „Destinație – Antrepozit fiscal” — „Destinație – Destinatar înregistrat” — „Destinație – Destinatar înregistrat temporar” — „Destinație – Livrare directă” — „Destinație – Destinatar certificat” — „Destinație – Destinatar certificat temporar” — „Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite” — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
9 – | Destinație – Destinatar certificat | Codul de acciză (6) | Orice identificator (*)
10 – | Destinație – Destinatar certificat temporar | Referința autorizației temporare (7) | Orice identificator (*)
11 – | Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite | Cod de acciză (8) sau Referința autorizației temporare (9) | Orice identificator (*)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(6) Tipul de operator al destinatarului este „Destinatar certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(7) Tipul de operator al destinatarului este „Destinatar certificat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(8) Tipul de operator al destinatarului este „Expeditor certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(9) Un identificator existent <Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ> cu Codul tipului de operator „Expeditor certificat temporar”.
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Numărul EORI | C | — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Specificați numărul EORI al persoanei responsabile cu prezentarea declarației de export, așa cum se prevede la articolul 21 alineatul (2) din Directiva (UE) 2020/262. | an..17
| c | Denumirea operatorului | R | | | an..182
| d | Strada | R | | | an..65
| e | Numărul | O | | | an..11
| f | Codul poștal | R | | | an..10
| g | Localitatea | R | | | an..50
| h | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
14.4 | BIROUL de destinație | R | | |
| a | Numărul de referință al biroului | R | | [a se vedea lista de coduri 5 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
14.5 | ALERTĂ | R | | |
| a | Data alertei | R | | | data
| b | Indicatorul respingerii deplasării | R | | Formatul Boolean este digital: „0” sau „1” („0” = Nu sau Fals; „1” = Da sau Adevărat) | n1
14.6 | Codul MOTIVULUI DE ALERTĂ SAU DE RESPINGERE A DEPLASĂRII | C | — „R” dacă <Indicatorul respingerii deplasării> este Adevărat — „O” dacă <Indicatorul respingerii deplasării> este Fals (a se vedea Indicatorul respingerii deplasării, în caseta 14.5b) | | 9x
| a | Codul motivului de alertă sau de respingere a deplasării | R | | (a se vedea lista de coduri 5 din anexa II) | n..2
| b | Informații complementare | C | — „R” dacă <Codul motivului de alertă sau de respingere a deplasării> este „Altele” — „O” în celelalte cazuri (a se vedea Codul motivului de alertă sau de respingere a deplasării, în caseta 14.6 a) | | an..350
| c | Informații complementare_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
15 | Toate explicațiile privind motivul lipsei | O | | | 99x
15.1 | ATRIBUTE | R | | |
| a | Tipul depunătorului | R | | Valorile posibile sunt: — 1 = Expeditor — 2 = Destinatar | n1
| b | Data și ora validării explicației lipsei | C | — „R” după validarea cu succes — Nu se aplică în alte cazuri | | dateTime
15.2 | DEPLASARE DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
15.3 | OPERATOR Expeditor | C | — „R” dacă <Tipul depunătorului> este „Expeditor” — Nu se aplică în alte cazuri (a se vedea Tipul depunătorului, în caseta 15.1 a) | |
| a | Codul de acciză al operatorului | R | | Pentru OPERATOR Expeditor Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI> <Codul tipului de operator> de la atributul <OPERATOR> menționat trebuie să fie: — „Antrepozitar autorizat”; SAU — „Expeditor înregistrat” SAU — „Expeditor certificat” SAU Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>. <Codul tipului de operator> de la atributul <OPERATOR> menționat trebuie să fie „Expeditor certificat temporar”. Pentru OPERATOR Locul expediției Un identificator existent <Referința antrepozitului fiscal> (Numărul de acciză în SEED). [a se vedea lista de coduri 1 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| b | Denumirea operatorului | R | | | an..182
| c | Strada | R | | | an..65
| d | Numărul | O | | | an..11
| e | Codul poștal | R | | | an..10
| f | Localitatea | R | | | an..50
| g | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
15.4 | OPERATOR Destinatar | C | — „R” dacă <Tipul depunătorului> nu este „Expeditor” — Nu se aplică în alte cazuri (a se vedea Tipul depunătorului, în caseta 15.1 a) | |
| a | Identificarea operatorului | C | — „R” dacă <Codul tipului de destinație> este: — „Destinație – Antrepozit fiscal” — „Destinație – Destinatar înregistrat” — „Destinație – Destinatar înregistrat temporar” — „Destinație – Livrare directă” — „Destinație – Destinatar certificat” — „Destinație – Destinatar certificat temporar” — „Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite” — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
8 – | Destinație necunoscută | (Nu se aplică) | (Nu se aplică)
9 – | Destinație – Destinatar certificat | Codul de acciză (6) | Orice identificator (*)
10 – | Destinație – Destinatar certificat temporar | Referința autorizației temporare (7) | Orice identificator (*)
11 – | Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite | Cod de acciză (8) sau Referința autorizației temporare (9) | Orice identificator (*)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(6) Tipul de operator al destinatarului este „Destinatar certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(7) Tipul de operator al destinatarului este „Destinatar certificat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(8) Tipul de operator al destinatarului este „Expeditor certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(9) Un identificator existent <Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ> cu Codul tipului de operator „Expeditor certificat temporar”.
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Numărul EORI | | — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Specificați numărul EORI al persoanei responsabile cu depunerea declarației de export, așa cum se prevede la articolul 21 alineatul (1) din Directiva (UE) 2020/262 a Consiliului. | an..17
| c | Denumirea operatorului | R | | | an..182
| d | Strada | R | | | an..65
| e | Numărul | O | | | an..11
| f | Codul poștal | R | | | an..10
| g | Localitatea | R | | | an..50
| h | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
15.5 | ANALIZĂ | C | Cel puțin unul dintre câmpurile <ANALIZĂ> sau <Corpul ANALIZEI> trebuie să fie prezent. | |
| a | Data analizei | R | | | data
| b | Explicație globală | R | | | an..350
| c | Explicație globală _LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
15.6 | Corpul ANALIZEI | C | Cel puțin unul dintre câmpurile <ANALIZĂ> sau <Corpul ANALIZEI> trebuie să fie prezent. | | 999x
| a | Numărul unic de referință al corpului de date | R | | Valoarea câmpului trebuie să fie mai mare ca zero. <Numărul unic de referință al corpului de date> trebuie să fie unic în cadrul mesajului și trebuie să se refere la un <Număr unic de referință al corpului de date> e-AD/e-SAD al e-AD-ului/e-SAD-ului asociat pentru care au fost declarate excedente sau lipsuri. | n..3
| b | Codul produsului accizabil | R | | [a se vedea lista de coduri 10 din anexa II la Regulamentul delegat (UE) 2022/1636] | an4
| c | Explicație | O | | | an..350
| d | Explicație_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| e | Cantitate efectivă | O | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
16 | Toate mesajele de atenționare privind Deplasarea de produse accizabile | O | | | 99x
16.1 | ATRIBUTE | R | | |
| a | Tipul mesajului | R | | Valorile posibile sunt: — 1 = Mesaj de atenționare la expirarea termenului de schimbare a destinației (sau de divizare) — 2 = Mesaj de atenționare la expirarea termenului de transmitere a raportului de primire/export — 3 = Mesaj de atenționare la expirarea termenului de furnizare a informațiilor privind destinația (articolul 22 din Directiva (UE) 2020/262) | n1
| b | Data și ora emiterii atenționării | R | | | dateTime
| c | Data și ora-limită | R | | | dateTime
| d | Informații privind atenționarea | O | | | an..350
| e | Informații privind atenționarea_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
16.2 | DEPLASARE DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
Tabelul 4
(menționat la articolul 5)
Cerere comună
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul cererii | R | | Valorile posibile sunt: 1 = (rezervat) 2 = Cerere de date de referință 3 = (rezervat) 4 = (rezervat) 5 = Cerere de resincronizare a registrului operatorilor economici 6 = Cerere de recuperare a unei liste de e-AD-uri/e-SAD-uri 7 = Cerere de statistici SEED 8 = Cerere de recuperare a unei liste de e-AD-uri 9 = Cerere de recuperare a unei liste de e-SAD-uri | n1
| b | Denumirea mesajului cererii | C | — „R” dacă <Tipul cererii> este „2” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | Valorile posibile sunt: „C_COD_DAT” | = | listă comună de coduri „C_PAR_DAT” | = | parametrii comuni ai sistemului „ALL” | = | pentru o structură completă | a..9
| c | Biroul solicitant | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| d | Identificator de corelare a cererii | C | — „R” dacă <Tipul cererii> este „2”, „5”, „6” sau „7” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | Valoarea câmpului <Identificator de corelare a cererii> este unică pentru fiecare stat membru. | An..44
| e | Data de începere | C | Pentru 1e și f: — „R” dacă <Tipul cererii> este „2” sau „5” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | | Data
| f | Data de încetare | C | | Data
| g | Data unică | C | — „R” dacă <Tipul cererii> este „2” sau „5” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | | Data
2 | CEREREA LISTEI DE e-AD/e-SAD | C | — „R” dacă <Tipul cererii> este „6”, „8” sau „9” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Codul statului membru | R | | [a se vedea lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636] | a2
2.1 | AC_CRITERIU PRIMAR | R | | | 99x
| a | Codul tipului de criteriu primar | R | | Valorile posibile sunt: 1 = ARC 2 = Marca comercială a produsului 3 = Categorii de produse accizabile ale deplasării 4 = (rezervat) 5 = (rezervat) 6 = (rezervat) 7 = (rezervat) 8 = Orașul destinatarului 9 = Orașul expeditorului 10 = Orașul garantului 11 = (rezervat) 12 = Orașul locului de livrare 13 = Orașul antrepozitului fiscal de expediere 14 = Orașul transportatorului 15 = Codul NC al produsului 16 = Data facturii 17 = Codul de acciză al destinatarului 18 = Codul de acciză al expeditorului 19 = Codul de acciză al garantului 20 = (rezervat) 21 = (rezervat) 22 = Codul de acciză al antrepozitului fiscal de destinație 23 = Codul de acciză al antrepozitului fiscal de expediere 24 = (rezervat) 25 = Codul produsului accizabil 26 = Durata transportului 27 = Statul membru de destinație 28 = Statul membru de expediere 29 = Denumirea destinatarului 30 = Denumirea expeditorului 31 = Denumirea garantului 32 = (rezervat) 33 = Denumirea locului de livrare 34 = Denumirea antrepozitului fiscal de expediere 35 = Denumirea transportatorului 36 = Numărul facturii 37 = Codul poștal al destinatarului 38 = Codul poștal al expeditorului 39 = Codul poștal al garantului 40 = (rezervat) 41 = Codul poștal al locului de livrare 42 = Codul poștal al antrepozitului fiscal de expediere 43 = Codul poștal al transportatorului 44 = Cantitatea de produse (în corpul e-AD/e-SAD) 45 = Numărul de referință local, adică un număr de serie atribuit de expeditor 46 = Tipul de transport 47 = (rezervat) 48 = (rezervat) 49 = Codul de TVA al destinatarului 50 = (rezervat) 51 = Codul de TVA al transportatorului 52 = Schimbarea destinației (numărul de ordine ≥ 2) | n..2
2.1.1 | AC_VALOARE PRIMARĂ | O | | | 99x
| a | Valoare | R | | Dacă <Codul tipului de criteriu primar> este „46” (Tipul de transport), atunci se va utiliza un <Cod al modului de transport> existent din lista <MODURI DE TRANSPORT>. | An..255
3 | CERERE_STA | C | — „R” dacă <Tipul cererii> este „7” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Tip de statistică | R | | Valorile posibile sunt: 1 = Operatori economici activi/ inactivi și eliminați 2 = Expirări iminente 3 = Operatori economici pe tip și antrepozite fiscale 4 = Activitate legată de accize 5 = Modificări ale autorizațiilor de accize | n1
3.1 | Codul LISTA STATELOR MEMBRE | R | | | 99x
| a | Codul statului membru | R | | [a se vedea lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636] | a2
4 | PERIOADĂ_STA | C | — „R” dacă <Tipul cererii> este „7” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Anul | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | N4
| b | Semestrul | C | Pentru 4 b, c și d: Următoarele trei câmpuri de date sunt opționale și exclusive: — <Semestru> — <Trimestru> — <Lună> Și anume, dacă unul dintre aceste câmpuri de date este completat, atunci celelalte două câmpuri de date nu se aplică. | Valorile posibile sunt: 1 = Primul semestru 2 = Al doilea semestru | n1
| c | Trimestru | C | Valorile posibile sunt: 1 = Primul trimestru 2 = Al doilea trimestru 3 = Al treilea trimestru 4 = Al patrulea trimestru | n1
| d | Lună | C | Valorile posibile sunt: 1 = Ianuarie 2 = Februarie 3 = Martie 4 = Aprilie 5 = Mai 6 = Iunie 7 = Iulie 8 = August 9 = Septembrie 10 = Octombrie 11 = Noiembrie 12 = Decembrie | n..2
5 | SINCRONIZAREA REFERINȚELOR | C | — „R” dacă <Tipul cererii> este „2” sau „5” — Nu se aplică în alte cazuri. (A se vedea Tipul cererii din caseta 1a) | |
| a | Perioada de la data | R | – | Acest câmp trebuie să fie anterior sau egal cu câmpul 5b. În cazul în care se solicită o extracție, câmpurile „Perioada de la data” și/sau „Perioada până la data” vor fi utilizate pentru a solicita evenimente valabile în perioada specificată. În schimb, în cazul în care se solicită o recuperare, câmpurile „Perioada de la data” și/sau „Perioada până la data” vor fi utilizate pentru a solicita evenimente modificate și publicate în perioada specificată. (A se vedea caseta 5c) | data
| b | Perioada până la data | R | – | În cazul în care se solicită o extracție, câmpurile „Perioada de la data” și/sau „Perioada până la data” vor fi utilizate pentru a solicita evenimente valabile în perioada specificată. În schimb, în cazul în care se solicită o recuperare, câmpurile „Perioada de la data” și/sau „Perioada până la data” vor fi utilizate pentru a solicita evenimente modificate și publicate în perioada specificată. (A se vedea caseta 5c) | data
| c | Extracție | O | – | Valoarea acestui câmp este: — 0: pentru recuperare (sau lipsă pentru a permite o compatibilitate inversă); — 1: pentru extracție; — 2: pentru înregistrările neanulate. | N1
| d | Codul statului membru | O | – | [a se vedea lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636] | a2
6 | REF_CERERE | C | — „R” dacă <Tipul cererii> este „2” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Indicatorul „Criterii comune de evaluare a riscurilor” | O | | Valorile posibile sunt: 0 = Nu sau Fals 1 = Da sau Adevărat | n1
6.1 | Codul LISTA CODURILOR | O | | | 99x
| a | Lista codurilor solicitată | O | | Valorile posibile sunt: 1 = Unități de măsură 2 = Tipuri de evenimente 3 = Tipuri de dovezi 4 = (rezervat) 5 = (rezervat) 6 = Coduri lingvistice 7 = Administrații naționale 8 = Coduri de țară 9 = Coduri de ambalaje 10 = Motivele recepției nesatisfăcătoare sau ale raportului de control 11 = Motive de întrerupere 12 = (rezervat) 13 = Moduri de transport 14 = Unități de transport 15 = Zone vitivinicole 16 = Coduri de operațiuni cu vinuri 17 = Categorii de produse accizabile 18 = Produse accizabile 19 = Coduri NC 20 = Corespondențe cod NC – produs accizabil 21 = Motivele anulării 22 = Motivele alertei sau respingerii privind e-AD 23 = Justificările întârzierii 24 = (rezervat) 25 = Persoane care semnalează evenimentul 26 = Motivele refuzului 27 = Motivele întârzierii rezultatului 28 = Acțiuni solicitate 29 = Motivele cererii 30 = (rezervat) 31 = (rezervat) 32 = (rezervat) 33 = (rezervat) 34 = Motivele care împiedică acțiunea de cooperare administrativă 35 = (rezervat) 36 = Tipul documentului 37 = (rezervat) 38 = (rezervat) 39 = Motivele cererii de închidere manuală 40 = Motivele respingerii închiderii manuale 41 = Administrație națională – grade Plato | n..2
Tabelul 5
[menționat la articolul 5 alineatul (2)]
Listă de e-AD-uri/e-SAD-uri rezultată în urma unei cereri generale de informații
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Biroul solicitant | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| b | Identificator de corelare a cererii | R | | Valoarea câmpului <Identificator de corelare a cererii> este unică pentru fiecare stat membru. | An..44
2 | ELEMENT AL LISTEI e-AD/e-SAD | O | | | 99x
| a | Data expedierii | R | | | data
2.1 | DEPLASARE DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Data și ora validării e-AD/e-SAD | R | | | dateTime
| c | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
2.2 | OPERATOR Expeditor | R | | |
| a | Codul de acciză al operatorului | R | | Specificați un număr de înregistrare SEED valabil al antrepozitarului autorizat, al expeditorului înregistrat, al expeditorului certificat sau al expeditorului certificat temporar. [a se vedea lista de coduri 1 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| b | Denumirea operatorului | R | | | an..182
2.3 | OPERATOR Locul expediției | C | DACĂ <Codul tip origine al e-AD/e-SAD> este „Origine – Antrepozit fiscal” sau „Origine – accize plătite” ATUNCI <OPERATOR Locul expediției> este „R” <BIROU de expediție – Import> nu se aplică DACĂ NU <OPERATOR Locul expediției> nu se aplică <BIROU de expediție – Import> este „R” | |
| a | Numărul de referință al Antrepozitului fiscal | C | Nu se aplică codului tip de origine „3” din caseta 9d [Pentru codul tip de origine, a se vedea caseta 9d din tabelul 1 din Regulamentul delegat (UE) 2022/1636] | Pentru OPERATOR Locul expediției Un identificator existent <Referința antrepozitului fiscal> (Numărul de acciză în SEED). [a se vedea lista de coduri 1 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| b | Denumirea operatorului | C | „R” dacă, în caseta 9d, Codul tip origine este „3” [Pentru codul tip de origine, a se vedea caseta 9d din tabelul 1 din Regulamentul delegat (UE) 2022/1636] | | an..182
2.4 | BIROU de expediție – Import | C | DACĂ <Codul tip origine al e-AD> este „Origine – Antrepozit fiscal” sau „Origine – accize plătite” ATUNCI <OPERATOR Locul expediției> este „R” <BIROU de expediție – Import> nu se aplică DACĂ NU <OPERATOR Locul expediției> nu se aplică <BIROU de expediție – Import> este „R” | |
| a | Numărul de referință al biroului | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
2.5 | OPERATOR Destinatar | C | „R” cu excepția Codului tipului de destinație 8 | |
| a | Identificarea operatorului | C | DACĂ <Codul tipului de destinație> este în: — „Destinație – Antrepozit fiscal” — „Destinație – Destinatar înregistrat” — „Destinație – Destinatar înregistrat temporar” — „Destinație – Livrare directă” — „Destinație – Destinatar certificat” — „Destinație – Destinatar certificat temporar” — „Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite” ATUNCI <OPERATOR Destinatar.Identificarea operatorului> este „R” DACĂ NU DACĂ <Codul tipului de destinație> este: — „Destinație – Export” ATUNCI <OPERATOR Destinatar.Identificarea operatorului> este „O” DACĂ NU <OPERATOR Destinatar.Identificarea operatorului> nu se aplică | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
8 – | Destinație necunoscută | (Nu se aplică) | (Nu se aplică)
9 – | Destinație – Destinatar certificat | Codul de acciză (6) | Orice identificator (*)
10 – | Destinație – Destinatar certificat temporar | Referința autorizației temporare (7) | Orice identificator (*)
11 – | Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite | Cod de acciză (8) sau Referința autorizației temporare (9) | Orice identificator (*)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(6) Tipul de operator al destinatarului este „Destinatar certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(7) Tipul de operator al destinatarului este „Destinatar certificat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(8) Tipul de operator al destinatarului este „Expeditor certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(9) Un identificator existent <Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ> cu Codul tipului de operator „Expeditor certificat temporar”.
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Numărul EORI | C | — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Specificați numărul EORI al persoanei responsabile cu depunerea declarației de export, așa cum se prevede la articolul 21 alineatul (1) din Directiva (UE) 2020/262 a Consiliului. | an..17
| c | Denumirea operatorului | R | | | an..182
2.6 | OPERATOR Locul livrării | C | Opțiunile privind câmpul <OPERATOR Locul livrării> sunt descrise mai jos, în funcție de câmpul <Codul tipului de destinație>: — „R” pentru Codurile tipului de destinație 1, 4, 9 și 10 — „O” pentru Codurile tipului de destinație 2, 3 și 5 — Nu se aplică în alte cazuri. | – | –
| a | Identificarea operatorului | C | DACĂ <Codul tipului de destinație> este „Destinație – Antrepozit fiscal” sau „Destinație – Destinatar certificat” sau „Destinație – Destinatar certificat temporar” ATUNCI <OPERATOR Locul livrării. Identificarea operatorului> este „R” DACĂ NU DACĂ <Codul tipului de destinație> este „Destinație – Livrare directă” ATUNCI <OPERATOR Locul livrării. Identificarea operatorului> nu se aplică DACĂ NU <OPERATOR Locul livrării. Identificarea operatorului> este „O” | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
8 – | Destinație necunoscută | (Nu se aplică) | (Nu se aplică)
9 – | Destinație – Destinatar certificat | Codul de acciză (6) | Orice identificator (*)
10 – | Destinație – Destinatar certificat temporar | Referința autorizației temporare (7) | Orice identificator (*)
11 – | Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite | Cod de acciză (8) sau Referința autorizației temporare (9) | Orice identificator (*)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(6) Tipul de operator al destinatarului este „Destinatar certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(7) Tipul de operator al destinatarului este „Destinatar certificat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(8) Tipul de operator al destinatarului este „Expeditor certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(9) Un identificator existent <Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ> cu Codul tipului de operator „Expeditor certificat temporar”.
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Denumirea operatorului | C | DACĂ <Codul tipului de destinație> este „Destinație – Livrare directă” ATUNCI <Denumirea operatorului> este „O” DACĂ NU <Denumirea operatorului> este „R” | | an..182
2.7 | BIROU Locul livrării – Vamă | C | Opțiunile privind câmpul <BIROU Locul livrării – Vamă> sunt descrise mai jos, în funcție de <Codul tipului de destinație>: — „R” pentru Codul tipului de destinație 6 — Nu se aplică în alte cazuri. | |
| a | Numărul de referință al biroului | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
2.8 | Codul CATEGORIA DE PRODUSE ACCIZABILE | R | | | 9x
| a | Codul categoriei de produse accizabile | R | | [a se vedea lista de coduri 3 din anexa II la Regulamentul (UE) nr. 612/2013] | a1
2.9 | OPERATOR Organizatorul transportului | C | DACĂ <Antetul e-AD/e-SAD. Organizarea transportului> (IE801) [sau <Antetul e-AD/e-SAD. Organizarea transportului> (IE815)] este „Expeditor” sau „Destinatar” ATUNCI <OPERATOR Organizatorul transportului> nu se aplică DACĂ NU <OPERATOR Organizatorul transportului> este „R” | |
| a | Numărul VAT | O | | | an..14
| b | Denumirea operatorului | R | | | an..182
2.10 | OPERATOR Primul transportator | O | | |
| a | Numărul VAT | O | | | an..14
| b | Denumirea operatorului | R | | | an..182
Tabelul 6
(menționat la articolul 5)
Refuzarea cererii comune
A | B | C | D | E | F | G
1 | Mesajul de cerere comună | R | | Contextul mesajului „Cerere comună” referitor la o deplasare, a cărui structură este prezentată în tabelul 4 |
2 | Respingere | R | | | 99x
| a | Data și ora respingerii | R | | | dateTime
| b | Codul motivului de respingere | R | | Valorile posibile sunt: — 0 = Altul — 2 = Niciun e-AD/e-SAD recuperat nu corespunde criteriilor de selecție — 3 = Datele de referință nu sunt disponibile — 4 = Lista cu birourile pentru accize nu este disponibilă — 5 = Datele SEED nu sunt disponibile — 7 = Date solicitate necunoscute — 8 = Număr incremental în afara intervalului — 26 = Duplicat constatat — 112 = Valoare incorectă (a codului) — 115 = Nu se acceptă în această poziție | n..3
Tabelul 7
[menționat la articolul 6 alineatul (1)]
Cerere comună de cooperare administrativă
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul cererii | R | | Valorile posibile sunt: 1 = Cooperare administrativă 2 = rezervat | n1
| b | Termenul de obținere a rezultatelor | R | | | data
2 | MONITORIZARE | R | | |
| a | Identificatorul de corelare de monitorizare | R | | (a se vedea lista de coduri 1 din anexa II) | an28
| b | Data emiterii | R | | | data
| c | Codul statului membru al expeditorului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| d | Numărul de referință al biroului expeditorului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| e | Agentul expeditorului | O | | | an..35
| f | Codul statului membru al destinatarului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| g | Numărul de referință al biroului destinatarului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| h | Agentul destinatarului | O | | | an..35
| i | Identificatorul național de referință al cazului | O | | | an..99
3 | ACO_CERERE | C | — „R” dacă <Tipul cererii> este „1” — Nu se aplică în alte cazuri (a se vedea Tipul cererii din caseta 1a) | |
| a | Informații privind cererea de cooperare administrativă | R | | | an..999
| b | Informații privind cererea de cooperare administrativă_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Indicator | O | | Valorile posibile sunt: 0 = Nu sau Fals 1 = Da sau Adevărat | n1
3.1 | Codul MOTIVULUI CERERII | R | | | 99x
| a | Codul motivului cererii de cooperare administrativă | R | | (a se vedea lista de coduri 8 din anexa II) | n..2
| b | ACO_Informații complementare | C | — „R” dacă <Codul motivului cererii de cooperare administrativă> este „Altele” — „O” în celelalte cazuri | – | an..999
| c | ACO_Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
3.1.1 | REFERINȚA EVALUĂRII RISCURILOR | O | | | 99x
| a | Alt profil de risc | O | | | an..999
| b | Alt profil de risc_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
3.2 | Lista ARC | O | | | 99x
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | O | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
3.3 | OPERATOR Persoană | O | | | 99x
| a | Codul de acciză al operatorului | C | Pentru 3.3 a, b și c: trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Număr VAT> — <Denumirea operatorului> | Un identificator (Cod de acciză) < Codul de acciză al operatorului > existent în setul < AUTORIZAȚIA OPERATORULUI > sau <Referința autorizației temporare> existent în setul <AUTORIZAȚIE TEMPORARĂ>. [a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| b | Numărul VAT | C | | an..14
| c | Denumirea operatorului | C | | an..182
| d | Codul statului membru | C | — „R” dacă <Denumirea operatorului> este furnizată, însă <Codul de acciză al operatorului> și <Numărul TVA> nu sunt furnizate — Nu se aplică în alte cazuri (a se vedea Codul de acciză al operatorului, în caseta 3.3a, Numărul TVA, în caseta 3.3b, Denumirea operatorului, în caseta 3.3c) | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| e | Strada | O | | | an..65
| f | Numărul | O | | | an..11
| g | Codul poștal | O | | | an..10
| h | Localitatea | O | | | an..50
| i | NAD_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| j | Numărul de telefon | O | | | an..35
| k | Numărul de fax | O | | | an..35
| l | Adresa de e-mail | O | | | an..70
3.4 | DOCUMENTE JUSTIFICATIVE | O | | | 9x
| a | Scurtă descriere a documentului justificativ | C | — „R” dacă <Tipul documentului justificativ> este „Altele” — Nu se aplică în alte cazuri (a se vedea Referința documentului justificativ, în caseta 3.4c, și Imaginea documentului, în caseta 3.4e) | | an..999
| b | Scurtă descriere a documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Referința documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Scurtă descriere a documentului justificativ, în caseta 3.4a, și Imaginea documentului, în caseta 3.4e) | | an..999
| d | Referința documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| e | Imaginea documentului | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Scurtă descriere a documentului justificativ, în caseta 3.4a, și Imaginea documentului, în caseta 3.4c) | |
| f | Tipul documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> A se vedea Referința documentului justificativ, în caseta 3.4c, și Imaginea documentului, în caseta 3.4e | (a se vedea lista de coduri 15 din anexa II) | an..4
3.5 | ACȚIUNI solicitate | O | | | 99x
| a | Codul acțiunii de cooperare administrativă | R | | (a se vedea lista de coduri 9 din anexa II) | n..2
| b | Complement acțiune ACO | C | — „R” dacă <Codul acțiunii de cooperare administrativă> este „Altele” — „O” în celelalte cazuri (a se vedea Codul acțiunii de cooperare administrativă, în caseta 3.5a) | | an..999
| c | Complement acțiune ACO_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
4 | CONTACT | O | | |
| a | Numărul de referință al biroului | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| b | Ofițerul de accize care prezintă cererea | O | | | an..35
| c | Numărul de telefon | O | | | an..35
| d | Numărul de fax | O | | | an..35
| e | Adresa de e-mail | O | | | an..70
Tabelul 8
(menționat la articolul 7)
Mesaj de răspuns
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul mesajului | R | | Valorile posibile sunt: — 1 = Mesaj de răspuns privind cooperarea administrativă — 2 = rezervat | n1
2 | MONITORIZARE | R | | |
| a | Identificatorul de corelare de monitorizare | R | | (a se vedea lista de coduri 1 din anexa II) | an28
| b | Data emiterii | R | | | data
| c | Codul statului membru al expeditorului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| d | Numărul de referință al biroului expeditorului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| e | Agentul expeditorului | O | | | an..35
| f | Codul statului membru al destinatarului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| g | Numărul de referință al biroului destinatarului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| h | Agentul destinatarului | O | | | an..35
| i | Identificatorul național de referință al cazului | C | – „O” dacă <Identificatorul de corelare de monitorizare> nu corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere — „R” dacă <Identificatorul de corelare de monitorizare> corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere ȘI <Identificatorul național de referință al cazului> este prezent în mesajul de cerere | DACĂ <Identificatorul de corelare de monitorizare> corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere ȘI <Identificatorul național de referință al cazului> este prezent în mesajul de cerere ATUNCI <Identificatorul național de referință al cazului> trebuie să fie egal cu valoarea câmpului <Identificatorul național de referință al cazului> din mesajul de cerere. | an..99
3 | RĂSPUNS | R | | |
| a | Termenul de obținere a rezultatelor | C | Pentru 3 a și b: — „R” dacă este furnizat <Codul motivului de refuz> — Nu se aplică în alte cazuri (a se vedea Codul motivului de refuz, în caseta 3c) | | dateTime
| b | Codul motivului întârzierii rezultatului | C | (a se vedea lista de coduri 3 din anexa II) | n..2
| c | Codul motivului de refuz | O | | (a se vedea lista de coduri 4 din anexa II) | n..2
| d | Complementul motivului de refuz | C | — „R” dacă <Codul motivului de refuz> este „Altele” — Nu se aplică în alte cazuri (a se vedea Codul motivului de refuz, în caseta 3c) | | an..999
| e | Complementul motivului de refuz_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
Tabelul 9
(menționat la articolul 7)
Mesaj de atenționare privind cooperarea administrativă
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul mesajului | R | | Valorile posibile sunt: — 1 = Mesaj de atenționare privind rezultatele cooperării administrative — 2 = Rezervat | n1
2 | MONITORIZARE | R | | |
| a | Identificatorul de corelare de monitorizare | R | | (a se vedea lista de coduri 1 din anexa II) | an28
| b | Data emiterii | R | | | data
| c | Codul statului membru al expeditorului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| d | Numărul de referință al biroului expeditorului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| e | Agentul expeditorului | O | | | an..35
| f | Codul statului membru al destinatarului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| g | Numărul de referință al biroului destinatarului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| h | Agentul destinatarului | O | | | an..35
| i | Identificatorul național de referință al cazului | C | — „O” dacă <Identificatorul de corelare de monitorizare> nu corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere — „R” dacă <Identificatorul de corelare de monitorizare> corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere ȘI <Identificatorul național de referință al cazului> este prezent în mesajul de cerere — Nu se aplică în alte cazuri. | DACĂ <Identificatorul de corelare de monitorizare> corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere ȘI <Identificatorul național de referință al cazului> este prezent în mesajul de cerere ATUNCI <Identificatorul național de referință al cazului> trebuie să fie egal cu valoarea câmpului <Identificatorul național de referință al cazului> din mesajul de cerere. | an..99
Tabelul 10
[menționat la articolul 6 alineatul (3), la articolul 9 alineatul (1) și la articolele 10 și 16]
Rezultatele cooperării administrative
A | B | C | D | E | F | G
1 | MONITORIZARE | R | | |
| a | Identificatorul de corelare de monitorizare | R | | (a se vedea lista de coduri 1 din anexa II) | an28
| b | Data emiterii | R | | | data
| c | Codul statului membru al expeditorului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| d | Numărul de referință al biroului expeditorului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| e | Agentul expeditorului | O | | | an..35
| f | Codul statului membru al destinatarului | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| g | Numărul de referință al biroului destinatarului | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| h | Agentul destinatarului | O | | | an..35
| i | Identificatorul național de referință al cazului | C | — „O” dacă <Identificatorul de corelare de monitorizare> nu corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere — „R” dacă <Identificatorul de corelare de monitorizare> corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere ȘI <Identificatorul național de referință al cazului> este prezent în mesajul de cerere — Nu se aplică în alte cazuri. | DACĂ <Identificatorul de corelare de monitorizare> corespunde cu <Identificatorul de corelare de monitorizare> într-un mesaj de cerere ȘI <Identificatorul național de referință al cazului> este prezent în mesajul de cerere ATUNCI <Identificatorul național de referință al cazului> trebuie să fie egal cu valoarea câmpului <Identificatorul național de referință al cazului> din mesajul de cerere. | an..99
2 | CONTACT | O | | |
| a | Numărul de referință al biroului | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| b | Ofițerul de accize care prezintă cererea | O | | | an..35
| c | Numărul de telefon | O | | | an..35
| d | Numărul de fax | O | | | an..35
| e | Adresa de e-mail | O | | | an..70
3 | REZULTATUL ACȚIUNII_ACO | O | | | 99x
| a | ARC | O | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | C | — „O” dacă se utilizează <ARC> — Nu se aplică în alte cazuri (a se vedea ARC, în caseta 3a) | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
| c | Codul acțiunii de cooperare administrativă | R | | (a se vedea lista de coduri 9 din anexa II) | n..2
| d | Complement acțiune ACO | C | — „R” dacă <Codul acțiunii de cooperare administrativă> este „Altele” — „O” în celelalte cazuri (a se vedea Codul acțiunii de cooperare administrativă, în caseta 3c) | | an..999
| e | Complement acțiune ACO_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| f | Codul motivului care împiedică acțiunea ACO | O | | (a se vedea lista de coduri 11 din anexa II) | n..2
| g | Complementul motivului care împiedică acțiunea ACO | C | — „R” dacă <Codul motivului care împiedică acțiunea ACO> este „Altele” — „O” în celelalte cazuri (a se vedea Codul motivului care împiedică acțiunea ACO, în caseta 3f) | | an..999
| h | Complementul motivului care împiedică acțiunea ACO_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| i | Constatare la destinație | O | | Valorile posibile sunt: 0 = Altă constatare 1 = (rezervat) 2 = Expediție regulamentară 3 = Produsele expediate nu au ajuns la destinație 4 = Produsele expediate au ajuns târziu 5 = Lipsă constatată 6 = Produse accizabile neregulamentare 7 = Expediție neînscrisă în evidența stocurilor 8 = Operatorul nu a putut fi contactat 9 = Operator lipsă 10 = Excedent constatat 11 = EPC incorect 12 = Cod al tipului de destinație incorect 13 = Diferențe confirmate 14 = Închidere manuală recomandată 15 = Întrerupere recomandată 16 = Nereguli identificate | n..2
| j | Alt tip de constatare | C | — „R” dacă <Constatare la destinație> este „Altă constatare” — Nu se aplică în alte cazuri (a se vedea Constatarea la destinație, în caseta 3i) | | an..999
| k | Alt tip de constatare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| l | Explicații complementare | O | | | an..999
| m | Explicații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| n | Referința raportului de control | O | | (a se vedea lista de coduri 2 din anexa II) În sistem există un mesaj „Raport de control” (inclusiv atunci când este încapsulat în mesajul „Istoricul deplasării” primit), având aceeași valoare a câmpului <Referința raportului de control> cu cea a mesajului prezentat. În plus, dacă în mesajul prezentat se furnizează <ARC>, atunci valoarea acestui câmp coincide cu valoarea câmpului <ARC> din mesajul „Raport de control” menționat. (a se vedea ARC, în caseta 3a) | an16
4 | CERERE DE RAPORTARE | O | | |
| a | Raportare solicitată sau furnizată | R | | Valorile posibile sunt: 0 = Nu s-a solicitat raportare 1 = Raportare solicitată 2 = Raportare furnizată | n1
| b | Acțiuni de monitorizare | C | Cel puțin unul dintre aceste două câmpuri dacă este furnizată caseta 4a: — <Acțiuni de monitorizare> — <Relevanța informațiilor> | – | an..999
| c | Acțiuni de monitorizare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| d | Relevanța informațiilor furnizate | C | Cel puțin unul dintre aceste două câmpuri dacă este furnizată caseta 4a: — <Acțiuni de monitorizare> — <Relevanța informațiilor> | – | an..999
| e | Relevanța informațiilor_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5 | DOCUMENTE JUSTIFICATIVE | O | | | 9x
| a | Scurtă descriere a documentului justificativ | C | — „R” dacă <Tipul documentului justificativ> este „Altele” — Nu se aplică în alte cazuri (a se vedea Tipul documentului justificativ, în caseta 5f) | | an..999
| b | Scurtă descriere a documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Referința documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Scurtă descriere a documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Scurtă descriere a documentului justificativ, în caseta 5a, și Imaginea documentului, în caseta 5e) | | an..999
| d | Referința documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| e | Imaginea documentului | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Scurtă descriere a documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Scurtă descriere a documentului justificativ, în caseta 5 a, și Imaginea documentului, în caseta 5c) | |
| f | Tipul documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Scurtă descriere a documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Scurtă descriere a documentului justificativ, în caseta 5a, Referința documentului justificativ, în caseta 5c și Imaginea documentului, în caseta 5e) | (a se vedea lista de coduri 15 din anexa II) | an..4
Tabelul 11
[menționat la articolul 9 alineatul (2) și la articolul 11]
Raport de control
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul mesajului | R | | Valorile posibile sunt: 1 = Document validat | n1
| b | Data și ora validării raportului de control | C | — „R” după validarea cu succes — Nu se aplică în alte cazuri | – | dateTime
2 | ANTETUL RAPORTULUI DE CONTROL | R | | |
| a | Referința raportului de control | R | | (a se vedea lista de coduri 2 din anexa II) | an16
2.1 | BIROUL DE CONTROL | R | | |
| a | Numărul de referință al biroului de control | O | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| b | Codul statului membru | C | Pentru 2.1 b, c, d, e, f și g: — „R”, cu excepția <Numărului străzii>, care este „O”, dacă nu se furnizează <Numărul de referință al biroului de control> — Nu se aplică în alte cazuri (a se vedea Numărul de referință al biroului de control, în caseta 2.1a) | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| c | Denumirea biroului de control | C | | an..35
| d | Strada | C | | an..65
| e | Numărul | C | | an..11
| f | Codul poștal | C | | an..10
| g | Localitatea | C | | an..50
| h | Numărul de telefon | C | Pentru 2.1 h, i și j: Dacă nu se furnizează <Numărul de referință al biroului de control>, trebuie să fie prezent cel puțin unul dintre următoarele trei atribute: — <Numărul de telefon> — <Numărul de fax> — <Adresa de e-mail> — în caz contrar, nu este aplicabil niciunul dintre cele trei atribute (a se vedea Numărul de referință al biroului de control, în caseta 2.1a) | | an..35
| i | Numărul de fax | C | | an..35
| j | Adresa de e-mail | C | | an..70
| k | NAD_LNG | C | „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
3 | DEPLASARE DE PRODUSE ACCIZABILE | C | Trebuie completat unul dintre câmpurile <DEPLASARE DE PRODUSE ACCIZABILE> sau<ALT DOCUMENT ÎNSOȚITOR> | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
4 | ALT DOCUMENT ÎNSOȚITOR | C | Trebuie completat unul dintre câmpurile <DEPLASARE DE PRODUSE ACCIZABILE> sau<ALT DOCUMENT ÎNSOȚITOR> | |
| a | Tipul altui document însoțitor | R | | Valorile posibile sunt: 0 = Altele 2 = (rezervat) | n1
| b | Scurtă descriere a altui documentului însoțitor | C | „R” dacă <Tipul altui document însoțitor> este „Altele” Nu se aplică în alte cazuri | | an…350
| c | Scurtă descriere a altui documentului însoțitor_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | n2
| d | Numărul altui document însoțitor | R | | | an…350
| e | Data altui document însoțitor | R | | | data
| f | Imaginea altui document însoțitor | O | | |
| g | Statul membru de expediere | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| h | Statul membru de destinație | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
4.1 | OPERATOR Persoana implicată în deplasare | O | | | 9x
| a | Codul de acciză al operatorului | C | Trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Identificarea operatorului> — <Denumirea operatorului> | Un identificator (Cod de acciză) < Codul de acciză al operatorului > existent în setul < AUTORIZAȚIA OPERATORULUI > sau <Referința autorizației temporare> existent în setul <AUTORIZAȚIE TEMPORARĂ>. [a se vedea lista de coduri 1 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| b | Identificarea operatorului | C | Trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Identificarea operatorului> — <Denumirea operatorului> | Un număr TVA sau orice alt număr național. | an16
| c | Denumirea operatorului | C | Trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Identificarea operatorului> — <Denumirea operatorului> | – | an..182
| d | Tipul Operatorului Persoană | O | | Valorile posibile sunt următoarele: 1 = Expeditor 2 = Destinatar 3 = Reprezentant fiscal 4 = Vânzător 5 = Persoană debitoare 6 = Client persoană fizică | n..2
| e | Codul statului membru | C | R” dacă <Denumirea operatorului> este furnizată, ÎNSĂ <Codul de acciză al operatorului> și <Identificarea operatorului> nu sunt furnizate Nu se aplică în alte cazuri | [a se vedea lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636] | a2
| f | Strada | O | | | an..65
| g | Numărul | O | | | an..11
| h | Codul poștal | O | | | an..10
| i | Localitatea | O | | | an..50
| j | NAD_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| k | Numărul de telefon | O | | | an..35
| m | Adresa de e-mail | O | | | an..70
4.2 | ARTICOL | O | | | 999x
| a | Descrierea mărfurilor | O | | | an..55
| b | Codul NC | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 4 și 4f) | Valoarea câmpului trebuie să fie mai mare ca zero. | n8
| c | Descriere comercială a mărfurilor | O | | | an..999
| d | Cod suplimentar | O | | | an..35
| e | Cantitate | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 4 și 4f) | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
| f | Codul unității de măsură | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 4 și 4f) | [a se vedea lista de coduri 11 din anexa II la Regulamentul delegat (UE) 2022/1636] | n..2
| g | Masa brută | O | | Masa brută trebuie să fie cel puțin egală cu Masa netă. Valoarea câmpului trebuie să fie mai mare ca zero. | n..16,6
| h | Masa netă | O | | Masa brută trebuie să fie cel puțin egală cu Masa netă. Valoarea câmpului trebuie să fie mai mare ca zero. | n..16,6
4.3 | MIJLOC DE TRANSPORT | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 4 și 4f) | |
| a | Denumirea operatorului | R | | | an..182
| b | Strada | R | | | an..65
| c | Numărul | O | | | an..11
| d | Țara transportatorului | R | | Specificați un „cod de țară” menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| e | Codul poștal | R | | | an..10
| f | Localitatea | R | | | an..50
| g | Codul modului de transport | R | | Specificați modul de transport, utilizând codurile din lista de coduri 6 din anexa II la Regulamentul delegat (UE) 2022/1636. | n..2
| h | ACO_Informații complementare | C | — „R” dacă <MIJLOC DE TRANSPORT. Codul modului de transport> este „Altele” — Nu se aplică în alte cazuri (a se vedea caseta 4.3 g) | | an..999
| i | ACO_Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| j | Înmatriculare | R | | | an..35
| k | Țara de înmatriculare | R | | Specificați un „cod de țară” menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
5 | RAPORTUL DE CONTROL | R | | |
| a | Data controlului | R | | | data
| b | Locul controlului | R | | | an..350
| c | Locul controlului_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| d | Tipul controlului | R | | Valorile posibile sunt: 1 = Control fizic 2 = Controlul documentelor | n1
| e | Motivul controlului | R | | Valorile posibile sunt: 0 = Alt motiv 1 = Control început aleatoriu 2 = Eveniment semnalat 3 = Primire cerere de asistență 4 = Cerere din partea unui alt birou 5 = Primire alertă | n1
| f | Referința complementară privind originea | O | | | an..350
| g | Referința complementară privind originea_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| h | Identitatea controlorului vamal | R | | | an..350
| i | Identitatea controlorului vamal_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| j | Concluzia generală privind controlul | R | | Valorile posibile sunt: 1 = Satisfăcător 2 = Discrepanțe minore constatate 3 = Întrerupere recomandată 4 = Intenția de a prezenta o cerere în conformitate cu articolul 9 sau articolul 46 din Directiva (UE) 2020/262 a Consiliului 5 = Pierdere admisibilă constatată, în legătură cu articolul 6 sau articolul 45 din Directiva (UE) 2020/262 a Consiliului | n1
| k | Control la sosire solicitat | R | | Valorile posibile sunt: 0 = Nu sau Fals 1 = Da sau Adevărat | n1
| l | Indicator | R | | Valorile posibile sunt: 0 = Nu sau Fals 1 = Da sau Adevărat | n1
| m | Observații | O | | | an..350
| n | Observații_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5.1 | ACȚIUNEA DE CONTROL EFECTUATĂ | R | | | 99x
| a | Acțiunea de control efectuată | R | | Valorile posibile sunt: 0 = Alte acțiuni de control 1 = Pachete numărate verificate 2 = Descărcate 3 = Pachete deschise 4 = Exemplar pe hârtie vizat al documentelor 5 = Numărare 6 = Eșantionare 7 = Control administrativ 8 = Mărfuri cântărite/măsurate 9 = Verificare aleatorie 10 = Controlul înregistrărilor 11 = Compararea documentelor prezentate cu e-AD/e-SAD | n..2
| b | Alte acțiuni de control | C | — „R” dacă <Acțiunea de control efectuată> este „0” — Nu se aplică în alte cazuri (a se vedea Acțiunea de control efectuată, în caseta 5.1 a) | | an..350
| c | Alte acțiuni de control_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5.2 | DOVADA EVENIMENTULUI | C | — „R” dacă <Motivele controlului> este „2” — „O” în celelalte cazuri (a se vedea Motivul controlului, în caseta 5e) | | 9x
| a | Autoritate emitentă | O | | | an..35
| b | Autoritate emitentă_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Codul tipului de dovadă | R | | (a se vedea lista de coduri 6 din anexa II) | n..2
| d | Complementul tipului de dovadă | C | — „R” dacă <Codul tipului de dovadă> este „Altele” — Nu se aplică în alte cazuri (a se vedea Codul tipului de dovadă, în caseta 5.2c) | | an..350
| e | Complementul tipului de dovadă_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| f | Referința dovezii | O | | | an..350
| g | Referința dovezii_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| h | Imaginea dovezii | O | | |
5.3 | MOTIV NESATISFĂCĂTOR | O | | | 9x
| a | Codul motivului nesatisfăcător | R | | (a se vedea lista de coduri 12 din anexa II) | n..2
| b | Informații complementare | C | — R” dacă <Codul motivului nesatisfăcător> este „Altele” — Nu se aplică în alte cazuri (a se vedea Codul motivului nesatisfăcător, în caseta 5.3a) | | an..350
| c | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5.4 | DETALII PRIVIND TRANSPORTUL | O | | | 99x
| a | Codul unității de transport | R | | [a se vedea lista de coduri 7 din anexa II la Regulamentul delegat (UE) 2022/1636] | n..2
| b | Identitatea unităților de transport | C | — „R” dacă <Codul unității de transport> nu este „Instalații de transport fixe” — Nu se aplică în alte cazuri (a se vedea Codul unității de transport, în caseta 5.4 a) | | an..35
| c | Identitatea sigiliului comercial | O | | | an..35
| d | Informații privind sigiliul | O | | | an..350
| e | Informații privind sigiliul_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| f | Informații complementare | O | | | an..350
| g | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5.5 | RAPORT DE CONTROL Organism | O | | | 99x
| a | Numărul unic de referință al corpului de date | C | — „R” dacă este prezent câmpul <DEPLASARE DE PRODUSE ACCIZABILE> — Nu se aplică în alte cazuri | Valoarea se referă la <Numărul unic de referință al corpului de date> al corpului e-AD/e-SAD al e-AD-ului/e-SAD-ului asociat și trebuie să fie unică în cadrul mesajului. Valoarea câmpului trebuie să fie mai mare ca zero. | n..3
| b | Descrierea mărfurilor | C | — „O” dacă este prezent câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri | – | an..55
| c | Codul NC | C | — „R” dacă este prezent câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri | Valoarea câmpului trebuie să fie mai mare ca zero. | n8
| d | Cod suplimentar | C | — „O” dacă este prezent câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri | – | an..35
| e | Indicator de lipsă sau excedent | O | | Valorile posibile sunt: S = Lipsă E = Excedent | a1
| f | Lipsa sau excedentul constatate | C | — R” dacă este furnizat câmpul <Indicator de lipsă sau excedent> — Nu se aplică în alte cazuri (a se vedea Indicatorul de lipsă sau excedent, în caseta 5.5e) | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
| g | Observații | O | | | an..350
| h | Observații_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5.5.1 | MOTIV NESATISFĂCĂTOR | O | | | 9x
| a | Codul motivului nesatisfăcător | R | | (a se vedea lista de coduri 12 din anexa II) | n..2
| b | Informații complementare | C | — R” dacă <Codul motivului nesatisfăcător> este „Altele” — „O” în celelalte cazuri (a se vedea Indicatorul codului motivului nesatisfăcător, în caseta 5.5.1a) | | an..350
| c | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
Tabelul 12
(menționat la articolul 14)
Raport de eveniment
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Tipul mesajului | R | | Valorile posibile sunt: 1 = Depunere inițială 3 = Document validat | n1
| b | Data și ora validării raportului de eveniment | C | — „R” după validarea cu succes, — Nu se aplică în alte cazuri | – | dateTime
2 | ANTETUL RAPORTULUI DE EVENIMENT | R | | |
| a | Numărul raportului de eveniment | C | — „R” dacă <Tipul mesajului> este „3” — Nu se aplică în alte cazuri (a se vedea Tipul mesajului, în caseta 1a) | (a se vedea lista de coduri 2 din anexa II) | an16
| b | Referința raportului de eveniment al SM de prezentare | C | — „R” dacă <Tipul mesajului> este „1” sau „3”, iar SM de prezentare este diferit de SM în care are loc evenimentul — „O” dacă <Tipul mesajului> este „1” sau „3”, iar SM de prezentare este SM în care are loc evenimentul — Nu se aplică în alte cazuri (a se vedea Tipul mesajului, în caseta 1a) | Formatul câmpului <Referința raportului de eveniment al SM de prezentare> este: — 2 caractere alfabetice: Identificatorul administrației naționale de prezentare a raportului de eveniment — urmate de un cod unic, atribuit la nivel național | an..35
| c | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| d | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
3 | ALT DOCUMENT ÎNSOȚITOR | C | Trebuie completat unul dintre câmpurile <DEPLASARE DE PRODUSE ACCIZABILE > sau <ALT DOCUMENT ÎNSOȚITOR> | |
| a | Tipul altui document însoțitor | R | | Valorile posibile sunt: 0 = Altele 2 = (rezervat) | n1
| b | Scurtă descriere a altui documentului însoțitor | C | — „R” dacă <Tipul altui document însoțitor> este „Altele” — Nu se aplică în alte cazuri | – | an..350
| c | Scurtă descriere a altui documentului însoțitor_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | – | a2
| d | Numărul altui document însoțitor | R | | | an..350
| e | Data altui document însoțitor | R | | | data
| f | Imaginea altui document însoțitor | O | | |
| g | Statul membru de expediere | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| h | Statul membru de destinație | R | | O administrație națională identificată printr-un cod de țară menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
3.1 | OPERATOR Persoana implicată în deplasare | O | | | 9x
| a | Codul de acciză al operatorului | C | — Trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Identificarea operatorului> — <Denumirea operatorului> | Un identificator (Cod de acciză) < Codul de acciză al operatorului > existent în setul < AUTORIZAȚIA OPERATORULUI > sau <Referința autorizației temporare> existent în setul <AUTORIZAȚIE TEMPORARĂ>. [a se vedea lista de coduri 1 din anexa II la Regulamentul (UE) nr. 612/2013] | an13
| b | Identificarea operatorului | C | — Trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Identificarea operatorului> — <Denumirea operatorului> | Un număr TVA sau orice alt număr național. | an16
| c | Denumirea operatorului | C | — Trebuie să fie prezent cel puțin unul dintre următoarele atribute: — <Codul de acciză al operatorului> — <Identificarea operatorului> — <Denumirea operatorului> | – | an..182
| d | Tipul Operatorului Persoană | O | | Valorile posibile sunt următoarele: 1 = Expeditor 2 = Destinatar 3 = Reprezentant fiscal 4 = Vânzător 5 = Persoană debitoare 6 = Client persoană fizică | n..2
| e | Codul statului membru | C | — R” dacă <Denumirea operatorului> este furnizată, ÎNSĂ <Codul de acciză al operatorului> și <Identificarea operatorului> nu sunt furnizate — Nu se aplică în alte cazuri | [a se vedea lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636] | a2
| f | Strada | O | | | an..65
| g | Numărul | O | | | an..11
| h | Codul poștal | O | | | an..10
| i | Localitatea | O | | | an..50
| j | NAD_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| k | Numărul de telefon | O | | | an..35
| l | Numărul de fax | O | | | an..35
| m | Adresa de e-mail | O | | | an..70
3.2 | ARTICOL | O | | | 999x
| a | Descrierea mărfurilor | O | | | an..55
| b | Codul NC | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR. Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 3 și 3f) | Valoarea câmpului trebuie să fie mai mare ca zero. | n8
| c | Descriere comercială a mărfurilor | O | | | an..999
| d | Cod suplimentar | O | | | an..35
| e | Cantitate | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 3 și 3f) | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
| f | Codul unității de măsură | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 3 și 3f) | [a se vedea lista de coduri 11 din anexa II la Regulamentul delegat (UE) 2022/1636] | n..2
| g | Masa brută | O | | Masa brută trebuie să fie cel puțin egală cu Masa netă. Valoarea câmpului trebuie să fie mai mare ca zero. | n..16,6
| h | Masa netă | O | | Masa brută trebuie să fie cel puțin egală cu Masa netă. Valoarea câmpului trebuie să fie mai mare ca zero. | n..16,6
3.3 | MIJLOC DE TRANSPORT | C | — „R” dacă <ALT DOCUMENT ÎNSOȚITOR.Imaginea altui document însoțitor> nu apare în câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri (a se vedea casetele 3 și 3f) | |
| a | Denumirea operatorului | R | | | an..182
| b | Strada | R | | | an..65
| c | Numărul | O | | | an..11
| d | Țara transportatorului | R | | Specificați un „cod de țară” menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
| e | Codul poștal | R | | | an..10
| f | Localitatea | R | | | an..50
| g | Codul modului de transport | R | | Specificați modul de transport, utilizând codurile din lista de coduri 6 din anexa II la Regulamentul delegat (UE) 2022/1636. | n..2
| h | ACO_Informații complementare | C | — „R” dacă <MIJLOC DE TRANSPORT.Codul modului de transport> este „Altele” — Nu se aplică în alte cazuri (a se vedea caseta 3.3 g) | | an..999
| i | ACO_Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| j | Înmatriculare | R | | | an..35
| k | Țara de înmatriculare | R | | Specificați un „cod de țară” menționat în lista de coduri 3 din anexa II la Regulamentul delegat (UE) 2022/1636. | a2
4 | RAPORT DE EVENIMENT | R | | |
| a | Data evenimentului | R | | | data
| b | Locul evenimentului | R | | | an..350
| c | Locul evenimentului_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| d | Identificarea ofițerului de accize | O | | | an..35
| e | Persoana care semnalează evenimentul | R | | | an..35
| f | Codul persoanei care semnalează evenimentul | R | | (a se vedea lista de coduri 10 din anexa II) | n..2
| g | Complementul persoanei care semnalează evenimentul | C | — „R” dacă <Codul persoanei care semnalează evenimentul> este „Altele” — „O” în celelalte cazuri (a se vedea Codul persoanei care semnalează evenimentul, în caseta 4f) | | an..350
| h | Complementul persoanei care semnalează evenimentul_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| i | Organizarea transportului modificată | O | | Valorile posibile sunt: 1 = Expeditor 2 = Destinatar 3 = Proprietar al produselor 4 = Altele | n1
| j | Observații | O | | | an..350
| k | Observații_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
5 | DOVADA EVENIMENTULUI | O | | | 9x
| a | Autoritate emitentă | O | | | an..35
| b | Autoritate emitentă_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Codul tipului de dovadă | R | | (a se vedea lista de coduri 6 din anexa II) | n..2
| d | Complementul tipului de dovadă | C | — „R” dacă <Codul tipului de dovadă> este „Altele” — Nu se aplică în alte cazuri (a se vedea Codul tipului de dovadă, în caseta 5c) | | an..350
| e | Complementul tipului de dovadă_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | 2
| f | Referința dovezii | R | | | an..350
| g | Referința dovezii_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| h | Imaginea dovezii | O | | |
6 | OPERATOR Noul organizator al transportului | C | — Nu se aplică dacă valoarea câmpului <Organizarea transportului modificată> este „1”, „2” sau dacă câmpul nu este utilizat — „R” în celelalte cazuri (a se vedea Organizarea transportului modificată, în caseta 4i) | |
| a | Numărul VAT | O | | | an..14
| b | Denumirea operatorului | R | | | an..182
| c | Strada | R | | | an..65
| d | Numărul | O | | | an..11
| e | Codul poștal | R | | | an..10
| f | Localitatea | R | | | an..50
| g | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
7 | OPERATOR Noul transportator | O | | |
| a | Numărul VAT | O | | | an..14
| b | Denumirea operatorului | R | | | an..182
| c | Strada | R | | | an..65
| d | Numărul | O | | | an..11
| e | Codul poștal | R | | | an..10
| f | Localitatea | R | | | an..50
| g | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
8 | DETALII PRIVIND TRANSPORTUL | O | | | 99x
| a | Codul unității de transport | R | | [a se vedea lista de coduri 7 din anexa II la Regulamentul delegat (UE) 2022/1636] | n..2
| b | Identitatea unităților de transport | C | — Nu se aplică dacă <Codul unității de transport> este „Instalații de transport fixe”. — „R” în celelalte cazuri (a se vedea Codul unității de transport, în caseta 8 a) | | an..35
| c | Identitatea sigiliului comercial | O | | | an..35
| d | Informații privind sigiliul | O | | | an..350
| e | Informații privind sigiliul_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| f | Informații complementare | O | | | an..350
| g | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
9 | Corpul RAPORTULUI DE EVENIMENT | C | — „O” dacă se utilizează < OPERATOR Noul organizator al transportului> sau dacă se utilizează <OPERATOR Noul transportator> sau dacă se utilizează <DETALII PRIVIND TRANSPORTUL> — „R” în celelalte cazuri (a se vedea OPERATOR Noul organizator al transportului în caseta 6, OPERATOR Noul transportator în caseta 7 și DETALII PRIVIND TRANSPORTUL în caseta 8) | | 99x
| a | Codul tipului de eveniment | R | | (a se vedea lista de coduri 14 din anexa II) | n..2
| b | Informații conexe | C | — „R” dacă <Codul tipului de eveniment> este „0” — „O” în celelalte cazuri (a se vedea Codul tipului de eveniment, în caseta 9 a) | | an..350
| c | Informații conexe_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| d | Numărul unic de referință al corpului de date | C | — „R” dacă este prezent câmpul <DEPLASARE DE PRODUSE ACCIZABILE> — Nu se aplică în alte cazuri | Valoarea se referă la <Numărul unic de referință al corpului de date> al corpului e-AD/e-SAD al e-AD-ului/e-SAD-ului asociat și trebuie să fie unică în cadrul mesajului. Valoarea câmpului trebuie să fie mai mare ca zero. | n..3
| e | Descrierea mărfurilor | C | — „O” dacă este prezent câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri | – | an..55
| f | Codul NC | C | — „R” dacă este prezent câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri | Valoarea câmpului trebuie să fie mai mare ca zero. | n8
| g | Cod suplimentar | C | — „O” dacă este prezent câmpul <ALT DOCUMENT ÎNSOȚITOR> — Nu se aplică în alte cazuri | – | an..35
| h | Indicator de lipsă sau excedent | C | Pentru 9h și 9i: — „R” dacă se indică <Numărul unic de referință al corpului de date> sau <Descrierea mărfurilor> sau <Codul NC> sau <Codul suplimentar> — Nu se aplică în alte cazuri (a se vedea Numărul unic de referință al corpului de date, în caseta 9d, Descrierea mărfurilor, în caseta 9e, Codul NC, în caseta 9f, și Codul suplimentar, în caseta 9g) | Valorile posibile sunt: S | = | Lipsă E | = | Excedent | a1
| i | Lipsa sau excedentul constatate | C | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
Tabelul 13
(menționat la articolul 12)
Întreruperea deplasării
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | ARC | R | | [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Data și ora emiterii | R | | | dateTime
| c | Codul motivul întreruperii | R | | (a se vedea lista de coduri 13 din anexa II) | n..2
| d | Numărul de referință al biroului pentru accize | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
| e | Identificarea ofițerului de accize | O | | | an..35
| f | Informații complementare | C | — „R” dacă <Codul motivul întreruperii> este „Altele” — „O” în celelalte cazuri (a se vedea Codul motivului întreruperii din caseta 1c) | | an..350
| g | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
2 | Referința RAPORTULUI DE CONTROL | O | | | 9x
| a | Referința raportului de control | R | | (a se vedea lista de coduri 2 din anexa II) În sistem există un mesaj „Raport de control” (inclusiv atunci când este încapsulat în mesajul „Istoricul deplasării” primit), având aceeași valoare a câmpului <Referința raportului de control> și <ARC> cu cea a mesajului prezentat. (a se vedea ARC, în caseta 1 a) | an16
3 | Referința RAPORTULUI DE EVENIMENT | O | | | 9x
| a | Numărul raportului de eveniment | R | | (a se vedea lista de coduri 2 din anexa II) În sistem există un mesaj „Raport de eveniment” (inclusiv atunci când este încapsulat în mesajul „Istoricul deplasării” primit), având aceeași valoare a câmpului <Numărul raportului de eveniment> și <ARC> cu cea a mesajului prezentat. (a se vedea ARC, în caseta 1 a) | an16
Tabelul 14
(menționat la articolul 13)
Alertă sau Respingere privind un e-AD/e-SAD
A | B | C | D | E | F | G
1 | ATRIBUTE | R | | |
| a | Data și ora validării alertei sau respingerii | C | — R dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | – | dateTime
2 | DEPLASARE DE PRODUSE ACCIZABILE | R | | |
| a | ARC | R | | Specificați codul ARC al e-AD/e-SAD. [a se vedea lista de coduri 2 din anexa la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Valoarea câmpului trebuie să fie mai mare ca zero. | n..2
3 | OPERATOR Destinatar | D | „R” cu excepția Codului tipului de destinație 8 (A se vedea Codul tipului de destinație în caseta 1a din tabelul 1 din Regulamentul delegat (UE) 2022/1636) | |
| a | Identificarea operatorului | C | — „R” dacă <Codul tipului de destinație> este: — „Destinație – Antrepozit fiscal” — „Destinație – Destinatar înregistrat” — „Destinație – Destinatar înregistrat temporar” — „Destinație – Livrare directă” — „Destinație – Destinatar certificat” — „Destinație – Destinatar certificat temporar” — „Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite” — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Valorile posibile ale câmpului <Identificarea operatorului> sunt descrise în tabelul următor: | an..16
Codul tipului de destinație | OPERATOR DESTINATAR. Identificarea operatorului | OPERATOR Locul livrării. Identificarea operatorului
1 – | Destinație – Antrepozit fiscal | Codul de acciză (1) | Referința antrepozitului fiscal (Codul de acciză) (5)
2 – | Destinație – Destinatar înregistrat | Codul de acciză (2) | Orice identificator (*)
3 – | Destinație – Destinatar înregistrat temporar | Referința autorizației temporare (4) | Orice identificator (*)
4 – | Destinație – Livrare directă | Codul de acciză (3) | (Nu se aplică)
5 – | Destinație – Destinatar scutit | (Nu se aplică) | Orice identificator (*)
6 – | Destinație – Export | Număr TVA (facultativ) | (Câmpul <OPERATOR Locul livrării> nu există)
9 – | Destinație – Destinatar certificat | Codul de acciză (6) | Orice identificator (*)
10 – | Destinație – Destinatar certificat temporar | Referința autorizației temporare (7) | Orice identificator (*)
11 – | Destinație – Returnare la locul de expediție al expeditorului, pentru o deplasare B2B cu accize plătite | Cod de acciză (8) sau Referința autorizației temporare (9) | Orice identificator (*)
(1) Tipul de operator al destinatarului este „Antrepozitar autorizat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(2) Tipul de operator al destinatarului este „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(3) Tipul de operator al destinatarului este fie „Antrepozitar autorizat”, fie „Destinatar înregistrat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(4) Tipul de operator al destinatarului este „Destinatar înregistrat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(5) Un identificator existent <Referința antrepozitului fiscal> în setul <ANTREPOZIT FISCAL>;
(6) Tipul de operator al destinatarului este „Destinatar certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(7) Tipul de operator al destinatarului este „Destinatar certificat temporar”. Un identificator existent < Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ>;
(8) Tipul de operator al destinatarului este „Expeditor certificat”. Un identificator existent <Codul de acciză al operatorului> în setul <AUTORIZAȚIA OPERATORULUI>;
(9) Un identificator existent <Referința autorizației temporare> în setul <AUTORIZAȚIE TEMPORARĂ> cu Codul tipului de operator „Expeditor certificat temporar”.
(*) | Pentru locul de livrare, „Orice identificator” înseamnă: un număr TVA sau orice alt identificator; utilizarea sa este facultativă.
[a se vedea lista de coduri 1 și lista de coduri 2 din anexa II la Regulamentul (UE) nr. 612/2013, dacă este cazul]
| b | Numărul EORI | C | — „O” dacă <Codul tipului de destinație> este „Destinație – Export” — Nu se aplică în alte cazuri | Specificați numărul EORI al persoanei responsabile cu prezentarea declarației de export, așa cum se prevede la articolul 21 alineatul (2) din Directiva (UE) 2020/262. | an..17
| c | Denumirea operatorului | R | | | an..182
| d | Strada | R | | | an..65
| e | Numărul | O | | | an..11
| f | Codul poștal | R | | | an..10
| g | Localitatea | R | | | an..50
| h | NAD_LNG | R | | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
4 | BIROUL DE DESTINAȚIE | R | | |
| a | Numărul de referință al biroului | R | | [a se vedea lista de coduri 4 din anexa II la Regulamentul delegat (UE) 2022/1636] | an8
5 | ALERTĂ | R | | |
| a | Data alertei | R | | | data
| b | Indicatorul e-AD/e-SAD Respins | R | | Formatul Boolean este digital: „0” sau „1” („0” = Nu sau Fals; „1” = Da sau Adevărat) | n1
6 | Codul MOTIVULUI DE ALERTĂ SAU DE RESPINGERE PRIVIND e-AD/e-SAD | C | — „R” dacă <Indicatorul e-AD/e-SAD Respins> este Adevărat — „O” în celelalte cazuri | – | 9x
| a | Codul motivului de alertă sau de respingere a deplasării | R | | (a se vedea lista de coduri 5 din anexa II) | n..2
| b | Informații complementare | C | — „R” dacă <Codul motivului de alertă sau de respingere a deplasării> este „Altele” — „O” în celelalte cazuri (a se vedea Codul motivului de alertă sau de respingere a deplasării, în caseta 6 a) | | an..350
| c | Informații complementare_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
Tabelul 15
(menționat la articolul 6a)
Cerere de închidere manuală
A | B | C | D | E | F | G
1 | ATRIBUT | R | | |
| a | ARC | R | | Specificați codul ARC al e-AD/e-SAD. [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Specificați numărul secvențial al e-AD/e-SAD. | n..2
| c | Codul motivului cererii de închidere manuală | R | | (a se vedea lista de coduri 16 din anexa II) | n1
| d | Complementul motivului închiderii manuale | C | — „R” dacă <Codul motivului cererii de închidere manuală> este „Altele” — „O” în celelalte cazuri | | an..999
| e | Complementul motivului închiderii manuale_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
2 | DOCUMENTE JUSTIFICATIVE | O | | | 9x
| a | Scurtă descriere a documentului justificativ | C | — „R” dacă <Tipul documentului justificativ> este „Altele” — Nu se aplică în alte cazuri | | an..999
| b | Scurtă descriere a documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Referința documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Imaginea documentului, în caseta 2e, și Tipul documentului justificativ, în caseta 2f) | | an..999
| d | Referința documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| e | Imaginea documentului | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Referința documentului justificativ, în caseta 2c, și Tipul documentului justificativ, în caseta 2f) | |
| f | Tipul documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Referința documentului justificativ, în caseta 2c, și Imaginea documentului, în caseta 2e) | (a se vedea lista de coduri 15 din anexa II) | an..4
3 | Corpul ÎNCHIDERII MANUALE | O | | | 999X
| a | Numărul unic de referință al corpului de date | R | | Valoarea se referă la <Numărul unic de referință al corpului de date> al corpului e-AD-ului/e-SAD-ului asociat și trebuie să fie unică în cadrul mesajului. Valoarea acestui câmp trebuie să fie mai mare ca zero. | n..3
| b | Indicator de lipsă sau excedent | O | | Valorile posibile sunt: S | = | Lipsă E | = | Excedent | a1
| c | Lipsa sau excedentul constatate | C | — R” dacă este furnizat câmpul <Indicator de lipsă sau excedent> — Nu se aplică în alte cazuri (a se vedea Indicatorul de lipsă sau excedent, în caseta 3b) | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
| d | Codul produsului accizabil | O | | [a se vedea lista de coduri 10 din anexa II la Regulamentul delegat (UE) 2022/1636] | an4
| e | Cantitatea refuzată | O | | Valoarea acestui câmp trebuie să fie mai mare ca zero. | n..15,3
| f | Informații complementare | O | | | an..350
| g | Informații complementare_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
Tabelul 16
(menționat la articolul 14 a)
Răspuns privind închiderea manuală
A | B | C | D | E | F | G
1 | ATRIBUT | R | | |
| a | ARC | R | | Specificați codul ARC al e-AD/e-SAD. [a se vedea lista de coduri 2 din anexa II la Regulamentul delegat (UE) 2022/1636] | an21
| b | Număr secvențial | R | | Specificați numărul secvențial al e-AD/e-SAD. | n..2
| c | Data sosirii produselor accizabile | O | | Data la care se încheie deplasarea, în conformitate cu articolul 19 alineatul (2) din Directiva (UE) 2020/262 a Consiliului. | data
| d | Concluzia generală a primirii | O | | Valorile posibile sunt: 1 = Primire acceptată și satisfăcătoare 2 = Primire acceptată deși nesatisfăcătoare 3 = Primire refuzată 4 = Primire refuzată parțial 21 = Ieșire acceptată și satisfăcătoare 22 = Ieșire acceptată cu neconcordanțe minore detectate, 23 = Ieșire refuzată | n..2
| e | Informații complementare | O | | | an..350
| f | Informații complementare_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| g | Codul motivului cererii de închidere manuală | R | | (a se vedea lista de coduri 16 din anexa II) | n1
| h | Complementul motivului închiderii manuale | C | — „R” dacă <Codul motivului cererii de închidere manuală> este „Altele” — „O” în celelalte cazuri | | an..999
| i | Complementul motivului închiderii manuale_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| j | Cerere de închidere manuală acceptată | R | – | Formatul Boolean este digital: „0” sau „1” („0” = Nu sau Fals; „1” = Da sau Adevărat) | n1
| k | Codul motivului de respingere a închiderii manuale | C | — „R” dacă <Cerere de închidere manuală acceptată> este „0” — Nu se aplică în alte cazuri | (a se vedea lista de coduri 17 din anexa II) | n1
| l | Complementul respingerii închiderii manuale | C | — „R” dacă <Codul motivului de respingere a închiderii manuale> este „Altele” — „O” în celelalte cazuri | | an..999
| m | Complementul respingerii închiderii manuale_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
2 | DOCUMENTE JUSTIFICATIVE | O | | | 9x
| a | Scurtă descriere a documentului justificativ | C | — „R” dacă <Tipul documentului justificativ> este „Altele” — Nu se aplică în alte cazuri | | an..999
| b | Scurtă descriere a documentului justificativ_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| c | Referința documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Imaginea documentului, în caseta 2e, și Tipul documentului justificativ, în caseta 2f) | | an..999
| d | Referința documentului justificativ_LNG | C | — „R” dacă se utilizează câmpul sau câmpurile de text liber corespunzătoare — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2
| e | Imaginea documentului | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Referința documentului justificativ, în caseta 2c, și Tipul documentului justificativ, în caseta 2f) | |
| f | Tipul documentului justificativ | C | Trebuie să fie prezent cel puțin unul dintre aceste trei câmpuri: — <Tipul documentului justificativ> — <Referința documentului justificativ> — <Imaginea documentului> (a se vedea Referința documentului justificativ, în caseta 2c, și Imaginea documentului, în caseta 2e) | (a se vedea lista de coduri 15 din anexa II) | an..4
3 | Corpul ÎNCHIDERII MANUALE | O | | | 999X
| a | Numărul unic de referință al corpului de date | R | | Valoarea se referă la <Numărul unic de referință al corpului de date> al corpului e-AD-ului/e-SAD-ului asociat și trebuie să fie unică în cadrul mesajului. Valoarea acestui câmp trebuie să fie mai mare ca zero. | n..3
| b | Indicator de lipsă sau excedent | O | | Valorile posibile sunt: S | = | Lipsă E | = | Excedent | a1
| c | Lipsa sau excedentul constatate | C | — R” dacă este furnizat câmpul <Indicator de lipsă sau excedent> — Nu se aplică în alte cazuri (a se vedea Indicatorul de lipsă sau excedent, în caseta 3b) | Valoarea câmpului trebuie să fie mai mare ca zero. | n..15,3
| d | Codul produsului accizabil | O | | [a se vedea lista de coduri 10 din anexa II la Regulamentul delegat (UE) 2022/1636] | an4
| e | Cantitatea refuzată | O | | Valoarea acestui câmp trebuie să fie mai mare ca zero. | n..15,3
| f | Informații complementare | O | | | an..350
| g | Informații complementare_LNG | C | — „R” dacă este utilizat câmpul de text corespunzător — Nu se aplică în alte cazuri | Specificați codul lingvistic prezentat în lista de coduri 1 din anexa II la Regulamentul delegat (UE) 2022/1636, pentru a defini limba utilizată în acest câmp. | a2”
2. În anexa II, lista de coduri 15 se înlocuiește cu următorul text:
„ Lista de coduri 15: Tipul documentului
Cod | Descriere
0 Altele
1 e-AD
2 e-SAD
3 Factură
4 Bon de livrare
5 CMR
6 Conosament
7 Scrisoare de transport
8 Contract
9 Cererea operatorului
10 Înregistrare oficială
11 Cerere
12 Răspuns
13 Documente de rezervă, copii de rezervă
14 Fotografie
15 Declarație de export
16 Aviz anticipat de export
17 Rezultate la ieșire
18 Declarația vamală
19 Certificat de mic producător independent de băuturi alcoolice
<CODUL TARIC> | Orice cod TARIC utilizat în elementul de date 1203000000 (subelementul 002000) al declarației de export”
ELI: http://data.europa.eu/eli/reg_impl/2024/289/oj
