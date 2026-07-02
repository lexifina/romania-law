REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2026/1233 AL COMISIEI
din 11 iunie 2026
de stabilire a specificațiilor serviciului comun de adresare pentru mediul aferent ghișeului unic european în domeniul maritim
(Text cu relevanță pentru SEE)
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) 2019/1239 al Parlamentului European și al Consiliului din 20 iunie 2019 de stabilire a unui mediu aferent ghișeului unic european în domeniul maritim și de abrogare a Directivei 2010/65/UE (1), în special articolul 13,
după consultarea Comitetului pentru facilitarea transportului și comerțului digital,
întrucât:
(1) În contextul mediului aferent ghișeului unic european în domeniul maritim instituit prin Regulamentul (UE) 2019/1239, declaranții și furnizorii de servicii de date (expeditorii) își pot îndeplini obligațiile de raportare printr-o conexiune de tip „de la sistem la sistem” la modulul de interfață de raportare (RIM) al ghișeelor unice naționale în domeniul maritim (MNSW).
(2) RIM, dezvoltat în conformitate cu specificațiile prevăzute în Regulamentul de punere în aplicare (UE) 2023/2790 al Comisiei (2), asigură interoperabilitatea tehnică și utilizarea unui set armonizat de mesaje pentru schimbul de date cu MNSW. Înainte ca expeditorii să facă schimb de date cu MNSW prin RIM, detaliile conexiunii trebuie configurate manual. Acest lucru este necesar și în cazul modificării detaliilor conexiunii. Serviciul comun de adresare ar trebui să rezolve această problemă prin facilitarea configurării automate a conexiunii directe de la sistem la sistem.
(3) Serviciul comun de adresare ar trebui să utilizeze o descoperire dinamică care să asigure flexibilitatea și scalabilitatea rețelei de MNSW. Expeditorii ar trebui să poată utiliza serviciul comun de adresare pentru a iniția o conexiune directă de date de la sistem la sistem între punctul lor de acces AS4 și un RIM prin extragerea automată a celor mai recente detalii de conectare ale unui RIM.
(4) Serviciul comun de adresare ar trebui să reducă la minimum necesitatea intervențiilor umane și, prin urmare, ar trebui să reducă proporțional costurile și riscurile de erori, făcând rețeaua flexibilă atunci când are loc o modificare a detaliilor de conectare ale participanților săi, cum ar fi informațiile privind punctele terminale și certificatul public.
(5) Pentru a asigura interoperabilitatea și reducerea costurilor de punere în aplicare, serviciul comun de adresare ar trebui să se bazeze pe aceleași tehnologii și standarde ca cele utilizate pentru RIM.
(6) Nodul localizator central ar trebui să conțină identificatorii participanților și locația nodului editor și ar trebui să fie găzduit la nivel central pentru a se asigura că aceste date sunt actualizate în sistemul public de nume de domenii (DNS).
(7) Pentru a spori reziliența serviciului și a atenua riscul unui punct unic de eșec, fiecare stat membru ar trebui să găzduiască propriul nod editor, care ar trebui să conțină toate detaliile necesare privind conexiunea ale RIM corespunzător.
(8) Pentru a asigura scalabilitatea și flexibilitatea și pentru autoritățile statelor membre care gestionează MNSW, statele membre ar trebui, de asemenea, să poată stoca în nodurile lor editoare detaliile de conectare ale punctelor de acces AS4 ale expeditorilor, ca alternativă la preconfigurarea manuală a acestora în RIM-ul lor.
(9) Pentru ca nodurile lor editoare să poată fi descoperite de utilizatorii serviciului comun de adresare, pentru a asigura corectitudinea și disponibilitatea adresei nodului editor în DNS public și pentru a împiedica utilizatorii serviciului comun de adresare să descopere noduri editoare dezactivate sau inexistente, statele membre ar trebui să poată înregistra, actualiza și șterge detaliile nodurilor lor editoare prin intermediul nodului localizator central.
(10) Ghișeele unice naționale în domeniul maritim constituie un serviciu public digital transfrontalier în sensul Regulamentului (UE) 2024/903 al Parlamentului European și al Consiliului (3) („Regulamentul privind Europa interoperabilă”). Prezentul regulament introduce noi cerințe obligatorii care afectează serviciul (serviciile) public(e) digital(e) menționat(e) anterior și, ca atare, face obiectul obligației de evaluare a interoperabilității în temeiul articolului 3 din Regulamentul privind Europa interoperabilă. În consecință, a fost efectuată o evaluare a interoperabilității, iar raportul întocmit în urma acesteia urmează să fie publicat pe portalul Europa interoperabilă,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
În sensul prezentului regulament, se aplică definițiile prevăzute la articolul 1 din Regulamentul de punere în aplicare (UE) 2023/2790 al Comisiei.
De asemenea, se aplică următoarele definiții:
1. „descoperire dinamică” înseamnă un mecanism care permite atât punctelor de acces AS4 ale expeditorilor, cât și RIM să obțină automat detalii de conectare reciproce pentru a iniția o conexiune directă;
2. „eDelivery” înseamnă un set de specificații și standarde tehnice pentru schimbul electronic de mesaje elaborat de Comisie;
3. „nod localizator central” înseamnă un localizator de metadate de servicii (Service Metadata Locator – SML) conform cu specificațiile profilului eDelivery (4), care facilitează descoperirea dinamică prin intermediul sistemului public de nume de domenii (DNS);
4. „nod editor” înseamnă un editor de metadate de servicii (Service Metadata Publisher – SMP) conform cu specificațiile profilului eDelivery (5), care conține detaliile de conectare ale modulelor de interfață de raportare (RIM) și ale punctelor de acces AS4 ale expeditorilor;
5. „serviciu comun de adresare” înseamnă serviciul menționat la articolul 2 punctul 10 din Regulamentul (UE) 2019/1239.
Articolul 2
Specificațiile funcționale și tehnice, mecanismele de control al calității și procedurile pentru implementarea, întreținerea și utilizarea serviciului comun de adresare sunt stabilite în anexa la prezentul regulament.
Articolul 3
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 11 iunie 2026.
Pentru Comisie
Președinta
Ursula VON DER LEYEN
(1) JO L 198, 25.7.2019, p. 64, ELI: http://data.europa.eu/eli/reg/2019/1239/oj.
(2) Regulamentul de punere în aplicare (UE) 2023/2790 al Comisiei din 14 decembrie 2023 de stabilire a specificațiilor funcționale și tehnice pentru modulul de interfață de raportare al ghișeelor unice naționale în domeniul maritim (JO L, 2023/2790, 18.12.2023, ELI: http://data.europa.eu/eli/reg_impl/2023/2790/oj).
(3) Regulamentul (UE) 2024/903 al Parlamentului European și al Consiliului din 13 martie 2024 de stabilire a unor măsuri pentru un nivel ridicat de interoperabilitate a sectorului public în întreaga Uniune (Regulamentul privind Europa interoperabilă) (JO L, 2024/903, 22.3.2024, ELI: http://data.europa.eu/eli/reg/2024/903/oj).
(4) https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/SML+service.
(5) https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/SMP+software.
ANEXĂ
IMPLEMENTAREA, ÎNTREȚINEREA ȘI UTILIZAREA SERVICIULUI COMUN DE ADRESARE
Serviciul comun de adresare constă într-un nod localizator central, operat și întreținut de Comisie, și în noduri editoare exploatate și întreținute de fiecare stat membru în conformitate cu specificațiile eDelivery.
Expeditorii pot utiliza serviciul comun de adresare pentru a iniția o conexiune directă de date de la sistem la sistem între punctul lor de acces AS4 și un modul de interfață de raportare utilizând descoperirea dinamică în locul detaliilor de conectare preconfigurate manual ale modulului de interfață de raportare în punctul lor de acces AS4.
Pentru a extrage detaliile de conectare RIM, punctul de acces AS4 al expeditorului contactează un nod editor, care stochează informațiile de conectare relevante. Detaliile de conectare ale unui anumit RIM sau ale unui punct de acces AS4 se stochează exclusiv într-un singur nod editor. Nodul localizator central facilitează acest proces prin gestionarea nodurilor editoare în DNS public și prin permiterea descoperirii dinamice.
Ca alternativă la preconfigurarea manuală a detaliilor de conectare ale punctului de acces AS4 al expeditorilor în modulul de interfață de raportare, statele membre pot utiliza nodul editor pentru a stoca detaliile de conectare ale punctelor de acces AS4 ale expeditorilor.
SPECIFICAȚII FUNCȚIONALE ȘI TEHNICE
Nod localizator central
Nodul localizator central trebuie să furnizeze următoarele funcționalități:
ID | Nume | Descriere
C1 | Repertoriul și consultarea adreselor de rețea | Nodul localizator central acționează ca un repertoriu central al identificatorilor RIM și al punctelor de acces AS4 și al identificatorilor nodurilor editoare respective și le face să poată fi descoperite prin intermediul DNS public.
C2 | Gestionarea centrală a nodurilor editoare | Nodul localizator central înregistrează, actualizează și șterge metadatele nodurilor editoare din DNS public. Statele membre sunt în măsură să își gestioneze detaliile privind nodul editor direct prin intermediul interfeței de la sistem la sistem a nodului localizator central.
C3 | Încredere și securitate | Nodul localizator central permite înregistrarea și comunicarea doar prin intermediul nodurilor editoare care prezintă un certificat valabil de securitate reciprocă pe nivelul de transport (mutual Transport Layer Security – mTLS) eliberat de o autoritate publică de certificare recunoscută și de încredere, în conformitate cu orientările eDelivery privind certificatele digitale.
Noduri editoare
Nodurile editoare trebuie să furnizeze următoarele funcționalități:
ID | Nume | Descriere
D4 | Furnizarea metadatelor | Nodul editor stochează și furnizează, la cerere, detalii privind conectarea la RIM sau la punctul de acces AS4 al expeditorului.
D5 | Încredere și securitate | Nodurile editoare sunt accesibile prin internet utilizând un certificat TLS valabil eliberat de o autoritate publică de certificare recunoscută și de încredere, în conformitate cu orientările eDelivery privind certificatele digitale.
D6 | Gestionarea registrelor | Nodul editor trebuie să ofere posibilitatea de a gestiona (înregistra, actualiza, elimina sau migra) detaliile conectării RIM și a punctului de acces AS4 al expeditorului stocate în nodul editor. Actualizările legate de aceste informații și de un nod editor care necesită modificarea înregistrărilor DNS se sincronizează cu nodul localizator central.
Nodul editor trebuie să cuprindă cel puțin următoarele informații:
ID | Nume | Descriere
E1 | Informații privind punctul terminal | Adresele tehnice ale RIM sau ale punctelor de acces AS4 la care sunt trimise mesajele AS4.
E2 | Certificat public | Certificatul public de încredere necesar pentru criptarea mesajelor AS4.
MECANISME DE CONTROL AL CALITĂȚII
ID | Nume | Descriere
L1 | Informații privind înregistrarea și monitorizarea | Nodurile localizatoare centrale și nodurile editoare oferă capacități de înregistrare și monitorizare în scopul controlului calității.
L2 | Tratarea excepțiilor | Nodurile localizatoare centrale și nodurile editoare trebuie să fie în măsură să detecteze și să gestioneze excepțiile și erorile și să raporteze atunci când acestea apar.
ELI: http://data.europa.eu/eli/reg_impl/2026/1233/oj
