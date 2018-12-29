REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2018/2032 AL COMISIEI
din 20 noiembrie 2018
de modificare a Regulamentului (CE) nr. 416/2007 al Comisiei privind specificațiile tehnice ale notificărilor transmise comandanților de nave
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Directiva 2005/44/CE a Parlamentului European și a Consiliului din 7 septembrie 2005 privind serviciile de informații fluviale (RIS) armonizate pe căile navigabile interioare de pe teritoriul Comunității (1), în special articolul 5 alineatul 1 litera (c),
întrucât:
(1) Regulamentul (CE) nr. 416/2007 al Comisiei (2) ar trebui să fie actualizat și să fie supus unui proces suplimentar de îmbunătățire și clarificare ținând cont de evoluțiile tehnologice și de experiența dobândită ca urmare a aplicării Regulamentului (CE) nr. 416/2007.
(2) Specificațiile tehnice pentru Notificările transmise comandanților de nave ar trebui să aibă la bază principiile tehnice prevăzute în anexa II la Directiva 2005/44/CE.
(3) Pentru a îmbunătăți siguranța navigației, notificările transmise comandanților de nave ar trebui să fie extinse pentru a include un nou tip de mesaj dedicat avizelor meteo.
(4) Tabelele de referință privind mirele ar trebui să fie eliminate din anexa la Regulamentul (CE) nr. 416/2007, deoarece datele de referință cuprinse în acestea, precum valorile de referință privind nivelul scăzut și nivelul ridicat ale apei, sunt dinamice. Astfel de date ar trebui să fie incluse și păstrate în Sistemul european de gestionare a datelor de referință operat de către Comisie.
(5) Se impune îmbunătățirea consecvenței la nivelul editării și al dezvoltării aplicațiilor pentru a crea servicii cu un nivel mai ridicat de interoperabilitate. Prin urmare, Ghidurile privind codificarea pentru editori și pentru dezvoltatorii de aplicații ar trebui să fie incluse în specificațiile tehnice drept apendicele A și B la anexă.
(6) Schimbul de date între autorități este recomandat în conformitate cu Regulamentul (CE) nr. 416/2007. Pentru a îmbunătăți astfel de schimburi de date, specificațiile legate de schimbul de date ar trebui să fie prezentate în apendicele D la anexă pentru a permite statelor membre să asigure interoperabilitatea sistemelor lor.
(7) Pentru a garanta că statele membre pot să codifice notificările transmise comandanților de nave într-un mod consecvent și interoperabil, tabelele de referință incluse în apendicele E ar trebui să fie îmbunătățite. În acest sens, ar trebui să se definească noi coduri într-un nou tabel de referință care să cuprindă etichete de interfețe de căutare armonizate pentru interfața grafică a utilizatorului. Mai mult, ar trebui să se adauge noi etichete, valori și coduri în tabelele de referință existente, iar elementele redundante ar trebui să fie eliminate.
(8) Specificațiile tehnice revizuite ar trebui să garanteze disponibilitatea tabelelor de referință din apendicele E inclusiv în format electronic în cadrul Sistemului european de gestionare a datelor de referință operat de Comisia Europeană.
(9) În conformitate cu articolul 12 alineatul (2) din Directiva 2005/44/CE, pentru a respecta prevederile articolului 4 din prezenta directivă, statele membre ar trebui să ia măsurile necesare pentru a pune în aplicare cerințele prevăzute în prezentul regulament în cel mult 30 de luni de la intrarea în vigoare a acestuia.
(10) Prin urmare, Regulamentul (CE) nr. 416/2007 ar trebui modificat în consecință.
(11) Măsurile prevăzute în prezentul regulament sunt conforme cu avizul comitetului menționat la articolul 11 din Directiva 2005/44/CE,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Anexa la Regulamentul (CE) nr. 416/2007 se înlocuiește cu textul anexei la prezentul regulament.
Articolul 2
Prezentul regulament intră în vigoare în ziua următoare datei publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulamentul este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 20 noiembrie 2018.
Pentru Comisie
Președintele
Jean-Claude JUNCKER
(1) JO L 255, 30.9.2005, p. 152.
(2) Regulamentul (CE) nr. 416/2007 al Comisiei din 22 martie 2007 privind specificațiile tehnice ale notificărilor transmise comandanților de nave menționate la articolul 5 din Directiva 2005/44/CE a Parlamentului European și a Consiliului privind serviciile de informații fluviale (RIS) armonizate pe căile navigabile interioare de pe teritoriul Comunității (JO L 105, 23.4.2007, p. 88).
ANEXĂ
CUPRINS
1. | DISPOZIȚII GENERALE | 4
1.1. | Definiții | 4
1.2. | Funcții principale și cerințe de performanță pentru notificările transmise comandanților de nave (NtS) | 4
2. | TRANSMITEREA DE NOTIFICĂRI COMANDANȚILOR DE NAVE | 5
3. | TIPURI DE MESAJE NtS | 5
4. | STRUCTURA NtS ȘI CODIFICAREA MESAJELOR NtS | 5
4.1. | Structura generală | 5
4.1.1. | Secțiunea privind identificarea | 6
4.1.2. | Mesaj privind șenalul navigabil și traficul pe căile navigabile | 6
4.1.3. | Date despre apă | 6
4.1.4. | Mesajul privind gheața | 7
4.1.5. | Mesaj meteo | 7
4.2. | Explicarea etichetelor XML și a valorilor codurilor din tabelele de referință NtS | 7
4.3. | Identificarea secțiunilor șenalelor navigabile și a obiectelor din mesajele NtS | 7
4.4. | Reguli pentru codificarea mesajelor NtS | 8
Apendicele A: Ghid privind codificarea NtS pentru editori | 9
Apendicele B: Ghid privind codificarea NtS pentru dezvoltatori de aplicații | 22
Apendicele C: Definirea schemei XML a NtS (XSD) | 50
Apendicele D: Specificația serviciului web NtS (WSDL) | 87
1. DISPOZIȚII GENERALE
1.1. Definiții
Serviciile de informare privind șenalele navigabile (FIS) înseamnă informații geografice, hidrologice și administrative privind căile navigabile (șenalele navigabile) care sunt utilizate de conducători de nave și administratori de flote în vederea planificării, executării și monitorizării unui voiaj. Termenii „conducător de navă” și „comandant de navă”, care sunt utilizați în prezentul standard, sunt considerați a fi echivalentul termenului „comandant de navă” utilizat în Orientările privind serviciile de informații fluviale (RIS) [Regulamentul (CE) nr. 414/2007 al Comisiei (1)], în timp ce termenul „administrator de flotă” este definit în Regulamentul (CE) nr. 415/2007 al Comisiei (2).
FIS furnizează informații dinamice (precum nivelurile apei, prognoze privind nivelul apei), precum și informații statice (precum orarul de funcționare al ecluzelor și podurilor) privind utilizarea și situația infrastructurii căilor navigabile interioare, sprijinind astfel deciziile tactice și strategice de navigație.
Mijloacele tradiționale de furnizare a FIS includ materialele vizuale ajutătoare pentru navigație, notificările adresate comandanților de nave pe hârtie și cele transmise prin radio, respectiv prin telefonie fixă pe ecluze. Telefonia mobilă a oferit noi posibilități de comunicare vocală și de transmisie a datelor, dar rețeaua celulară nu este disponibilă în orice loc și la orice moment. FIS-urile personalizate pot fi furnizate prin servicii de radiotelefonie pe căile navigabile interioare, prin servicii de Internet sau prin serviciul de hărți electronice de navigație, precum sistemul de informații și afișare a hărților electronice pentru navigația pe căile navigabile interioare (ECDIS interior) cu hartă electronică pentru navigație (ENC).
1.2. Principalele funcții și cerințele de performanță pentru notificările adresate comandanților de nave (NtS)
Această specificație tehnică pentru NtS precizează regulile pentru transmiterea de date în vederea informării privind șenalele navigabile prin internet.
NtS:
(a) oferă informații legate de condițiile șenalelor navigabile, trafic, vreme, de nivelurile apei și de gheață pentru Serviciile de informare privind șenalele navigabile;
(b) asigură traducerea automată a celor mai importante informații din notificările adresate comandanților de nave, folosind vocabularul standard pe baza listelor de coduri (tabelele de referință pentru NtS prezentate în apendicele E);
(c) oferă o structură standardizată a seturilor de date pentru a facilita integrarea notificărilor în sistemele de planificare a parcursurilor;
(d) este compatibil cu structura datelor din Index RIS și ECDIS interior pentru a facilita integrarea NtS în ECDIS interior, astfel cum este prevăzut în Directiva 2005/44/EC din 7 septembrie 2005 privind RIS armonizate pe căile navigabile interioare din Comunitate.
Specificațiile tehnice pentru NtS facilitează schimbul de date între sistemele NtS ale diferitelor țări și cu alte aplicații care utilizează date NtS, inclusiv ECDIS interior.
Unele informații cuprinse în mesajele NtS pot fi standardizate, altele nu.
Partea standardizată acoperă toate informațiile care sunt:
(a) importante pentru siguranța navigației pe căile interioare (spre exemplu: ambarcațiune mică scufundată pe partea dreaptă a șenalului navigabil la Dunăre, km fluviu 2010);
(b) necesare planificării voiajelor, inclusiv închiderea ecluzelor și reducerea înălțimii libere de trecere.
Informațiile suplimentare care nu sunt relevante pentru siguranță sau planificarea voiajelor, inclusiv cauza închiderii unei ecluze, pot fi furnizate ca text liber, fără o traducere automată. Utilizarea textului liber este cât se poate de limitată.
2. TRANSMITEREA DE NOTIFICĂRI COMANDANȚILOR DE NAVE
Statele membre se asigură de faptul că mesajele NtS sunt accesibile online și prin serviciul web standardizat NtS, în conformitate cu specificațiile tehnice descrise în prezenta anexă și în apendicele la aceasta. Specificația privind serviciul web NtS standardizat este inclusă în apendicele D sub forma unui „Limbaj pentru descrierea serviciilor web” (WSDL).
Serviciile web NtS standardizate oferă utilizatorului posibilitatea de a selecta mesaje pe baza cel puțin a unuia dintre următoarele criterii:
(a) o secțiune specifică a căilor navigabile;
(b) o porțiune specifică din calea navigabilă, definită de indicatoarele kilometrice fluviale inițiale și finale;
(c) durata de valabilitate a notificării (data inițială și data finală ale perioadei de valabilitate);
(d) data publicării notificării (data și ora publicării).
Mesajele NtS care respectă standardele prevăzute în această anexă pot fi transmise, printre altele, folosind următoarele instrumente:
(a) aplicații mobile (aplicații);
(b) servicii e-mail.
Se poate realiza schimbul de date între sistemele NtS care funcționează în diferite țări. Toate sistemele care utilizează standardele descrise în anexa la prezentul regulament pot integra NtS din alte sisteme în serviciile proprii, cu condiția să nu se modifice conținutul mesajului. Utilizatorii sunt informați în cazul în care conexiunea cu o sursă de NtS integrate este întreruptă sau indisponibilă.
3. TIPURI DE MESAJE NtS
Mesajele NtS sunt mesaje esențiale la nivelul cel mai ridicat posibil de standardizare.
Există patru tipuri de mesaje NtS, și anume:
(a) mesaj privind șenalul navigabil și traficul;
(b) date despre apă;
(c) mesajul privind gheața;
(d) mesaj meteo.
4. STRUCTURA NtS ȘI CODIFICAREA MESAJELOR NtS
Acest capitol descrie structura și codificarea NtS electronice standardizate.
Un mesaj NtS este un mesaj structurat care utilizează elemente standardizate, ori de câte ori este posibil. Utilizarea textului liber în elementele datelor este cât se poate de limitată.
Definiția schemei limbajului de marcare extensibil (XML) pentru NtS standardizat, denumită XSD în prezentul standard, cuprinde valorile codurilor standardizate, iar în apendicele C sunt incluse formate posibile.
Valorile codurilor standardizate și etichetele XML, sensul și traducerea acestora sunt prezentate în tabelele de referință NtS din apendicele E și, de asemenea, sunt disponibile în format electronic în Sistemul european de gestionare a datelor de referință (ERDMS) operat de Comisia Europeană.
4.1. Structura generală
Un mesaj NtS cuprinde următoarele secțiuni:
(a) secțiunea privind identificarea;
(b) secțiunea care definește obiectul (obiectele) aplicabil(e) sau secțiunea (secțiunile) șenalelor navigabile la care se face referire în mesaj;
(c) restricția (restricțiile) în cazul unui mesaj privind șenalul navigabil și traficul, valoarea (valorile) de măsurare pentru date despre apă, starea (stările) gheții în cazul unui mesaj privind gheața sau (un) raport (rapoarte) în cazul unui mesaj meteo.
Figura 1
Structura notificărilor transmise comandanților de nave
[figură]
4.1.1. Secțiunea privind identificarea
Fiecare mesaj trebuie să cuprindă o secțiune de identificare. Secțiunea privind identificarea cuprinde informații generale despre emitent și data publicării mesajului.
4.1.2. Mesaj privind șenalul navigabil și traficul pe căile navigabile
Mesajul privind șenalul navigabil și traficul pe căile navigabile cuprinde informații pentru secțiunea (secțiunile) șenalelor navigabile sau obiectul (obiectele) și este utilizat pentru a indica restricția (restricțiile) în următoarele scopuri:
(a) „Alertă”: relevant pentru siguranță. Alerta trebuie să conțină cel puțin o restricție care determină în mod direct și concret punerea în pericol a persoanelor, a navelor sau a facilităților, precum lucrările de sudură pe un pod, care generează scântei, o cabină de verificare/lucrători suspendați pe un pod, un obstacol pe șenalul navigabil;
(b) „Anunț”: relevant pentru planificarea sau siguranța voiajelor. Anunțul poate conține restricții, precum blocarea sasului unei ecluze din cauza unor lucrări de întreținere sau de dragare a șenalului navigabil;
(c) „Serviciu informativ”: informații generale care nu sunt legate în mod direct de planificarea sau siguranța voiajelor. Mesajul informativ nu trebuie să conțină restricții specifice, prin urmare nu este direct relevant pentru planificarea sau siguranța voiajelor. Astfel de informații ar putea include informații generale precum reguli de trafic local, o actualizare ECDIS interior.
4.1.3. Date despre apă
Secțiunea privind apa cuprinde valori sau previziuni pentru:
(a) nivelul apei;
(b) adâncimea minimă;
(c) înălțimea liberă de trecere;
(d) situația barajului;
(e) debitul;
(f) regimul.
De regulă, informațiile privind nivelul apei sunt generate și publicate în mod automat pe baza datelor primite de la echipamentul cu senzori (precum mira de maree), de la sisteme (precum modelul nivelului apei) sau de la infrastructură (precum situația barajului). Ar putea exista diferiți factori declanșatori pentru publicare, precum publicarea periodică sau atingerea unei anumite valori.
4.1.4. Mesajul privind gheața
Mesajul privind gheața cuprinde informații despre condițiile existente sau prognozate ale gheții pe secțiunea (secțiunile) șenalelor navigabile. Informațiile privind gheața sunt generate, de regulă, de personalul competent pe baza observațiilor locale și a evaluării profesionale.
4.1.5. Mesaj meteo
Mesajul meteo cuprinde informații despre condițiile climatice (periculoase) pentru navigația pe căile interioare.
Pentru a facilita distribuția informațiilor hidrologice și meteo din rețelele hidro-metrologice către comandații de nave, pot fi publicate mesaje meteo.
4.2. Explicarea etichetelor XML și a valorilor codurilor din tabelele de referință NtS
Sensul diferitelor elemente utilizate în definiția schemei XML (XSD) a NtS este descris în tabelele de referință NtS prezentate în apendicele E. Structura, formatul și posibilele valori ale tuturor elementelor XML sunt descrise în XSD NtS din apendicele C.
(a) Coordonatele de latitudine și longitudine sunt codificate conform sistemului geodezic mondial din 1984 și prezentate în grade și minute cu cel puțin trei (dar de preferință patru) zecimale ([d]d mm.mmm[m] N, [d][d]d mm.mmm[m] E).
(b) Zecimalele din câmpurile numerice sunt indicate cu un punct zecimal („.”). Nu se folosesc separatori de mii.
(c) Mesajele NtS folosesc doar următoarele unități pentru valorile incluse în mesajul XML: cm, m3/s, h, km/h și kW, m/s (vânt), mm/h (precipitații) și grade Celsius. Aplicațiile naționale pot transforma unitățile pentru o facilitarea citirii de către utilizator.
4.3. Identificarea secțiunilor șenalelor navigabile și a obiectelor din mesajele NtS
Pentru a îndeplini cerințele privind datele minime pentru furnizarea de informații despre obiecte relevante pentru navigația pe căile interioare, astfel cum este prevăzut la articolul 4 alineatul (3) litera (a) din Directiva 2005/44/CE, codul de localizare ISRS trebuie să fie utilizat în secțiunea obiectelor. Codul de localizare ISRS este utilizat pentru a identifica în mod unic obiecte și secțiuni ale șenalului și pentru a asigura sisteme și servicii RIS interoperabile (precum combinarea informațiilor despre infrastructură din indexul RIS, ECDIS interior și NtS pentru planificarea voiajelor).
Codul de localizare ISRS este un cod alfanumeric format din 20 de cifre, care este utilizat pentru a stabili o relație unică și standardizată între obiectele din serviciile de informații fluviale. Acesta cuprinde următoarele elemente de date obligatorii aranjate în patru blocuri de informații:
(a) Secțiunea 1: UN/LOCODE (5 litere, alfanumeric), cuprinzând
— codul de țară (2 cifre, alfanumeric) (3) și
— Codul de localizare (3 cifre, alfanumeric, „XXX” dacă nu este disponibil)
(b) Secțiunea 2: Codul secțiunii șenalului navigabil (5 cifre, alfanumeric, se stabilește de către autoritatea națională)
(c) Secțiunea 3: Codul de referință a obiectului (5 cifre, alfanumeric, „XXXXX” dacă nu este disponibil)
(d) Secțiunea 4: Hectometrul secțiunii șenalului navigabil (5 cifre, numeric, hectometru în centrul zonei sau „00000” dacă nu este disponibil).
Codurile de localizare ISRS și datele de referință ale obiectelor sunt păstrate de statele membre în indexul RIS și transmise în ERDMS operat de către Comisia Europeană conform procedurilor de întreținere pentru indexul RIS publicat pe site-ul ERDMS.
4.4. Reguli pentru codificarea mesajelor NtS
Mesajele NtS sunt codificate în conformitate cu Ghidul privind codificarea NtS pentru editori (apendicele A) și cu Ghidul privind codificarea NtS pentru dezvoltatorii de aplicații (apendicele B).
(1) Regulamentul (CE) nr. 414/2007 al Comisiei din 13 martie 2007 privind orientările tehnice pentru planificarea, punerea în aplicare și utilizarea operațională a serviciilor de informații fluviale (RIS) menționate la articolul 5 din Directiva 2005/44/CE a Parlamentului European și a Consiliului privind serviciile de informații fluviale (RIS) armonizate pe căile navigabile interioare de pe teritoriul Comunității (JO L 105, 23.4.2007, p. 1).
(2) Regulamentul (CE) nr. 415/2007 al Comisiei din 13 martie 2007 privind specificațiile tehnice pentru sistemele de urmărire și reperare a navelor menționate la articolul 5 din Directiva 2005/44/CE a Parlamentului European și a Consiliului privind serviciile de informații fluviale (RIS) armonizate pe căile navigabile interioare de pe teritoriul Comunității (JO L 105, 23.4.2007, p. 35).
(3) Codurile de țară ale ONU sunt definite în conformitate cu punctul 2.4.2.12 din anexa la Regulamentul (UE) nr. 164/2010 al Comisiei (JO L 57, 6.3.2010, p. 1). Codurile de țară ale ONU sunt identice cu codurile de țară ISO 3166-1 Alpha-2.
A. GHIDUL PRIVIND CODIFICAREA NOTIFICĂRILOR TRANSMISE COMANDANȚILOR DE NAVE PENTRU EDITORI
CUPRINS
1. | Contextul, structura și scopul Ghidurilor privind codificarea NtS | 10
2. | Selecția tipului de mesaj NtS | 10
3. | Considerații de bază privind FTM, acțiunile întreprinse pentru publicarea unui FTM | 10
4. | Explicarea codurilor FTM | 12
5. | Considerații de bază privind WRM | 20
6. | Considerații de bază privind ICEM, acțiunile întreprinse pentru publicarea unui ICEM | 20
7. | Considerații de bază privind WERM | 20
8. | Reguli pentru anumite elemente | 21
Abrevieri:
Abreviere | Sens
CEVNI | Codul european pentru căile de navigație interioară (European Code for Inland Waterways) (http://www.unece.org/trans/main/sc3/sc3res.html)
ENC | Hartă electronică de navigație
FTM | Mesaj privind șenalul navigabil și traficul pe căile navigabile
ICEM | Mesaj privind gheața
Sistemul ECDIS interior | Sistemul de afișare a hărților electronice și de informare pentru navigația interioară
Codul de localizare ISRS | Codul de localizare „Standardul internațional privind raportarea navelor”
NtS | Notificări transmise comandanților de nave
RIS | Servicii de informații fluviale
VHF | banda maritimă mobilă
WERM | Mesaj meteo
BYS | Date despre apă
WSDL | Limbaj pentru descrierea serviciilor web
XML | Limbaj de marcare extensibil
XSD | Definiția schemei XML
1. Contextul, structura și scopul Ghidurilor privind codificarea NtS
Standardul NtS este îmbunătățit permanent. Un progres semnificativ a fost marcat de lansarea serviciului web NtS care facilitează schimbul de mesaje NtS între autorități, precum și între autorități și utilizatorii NtS.
Au fost elaborate două documente pentru a facilita codificarea armonizată a mesajelor NtS la nivel național și internațional: ghidul privind codificarea NtS pentru editori și Ghidul privind codificarea NtS pentru dezvoltatorii de aplicații. Aceste ghiduri sunt valabile pentru NtS XSD 4.0 și pentru serviciul web NtS WSDL 2.0.4.0.
Având în vedere rata ridicată de utilizare a serviciului web NtS, mesajele NtS trebuie armonizate în continuare pentru a asigura afișarea adecvată a conținutului în sistemele terților. Codificarea uniformă a mesajelor este, de asemenea, o cerință preliminară pentru a ține cont de mesaje în aplicații privind planificarea voiajelor.
Elementele care conțin doar valori standard sau implicite sunt omise dacă sunt condiționate, deoarece conduc la supraîncărcarea mesajului, fără o valoare adăugată.
Ghidul privind codificarea NtS pentru editori este conceput pentru persoanele care editează (și publică) mesajele NtS, incluzând instrucțiuni pas cu pas pentru a crea tipurile de mesaje adecvate, precum și o explicare a codurilor. Ghidul privind codificarea NtS explică aplicabilitatea celor patru tipuri de mesaje NtS, prezintă instrucțiuni de completare și coduri care să fie utilizate pentru anumite evenimente. Ghidul privind codificarea NtS pentru editori este inclus în prezentul apendice A.
Ghidul privind codificarea NtS pentru dezvoltatorii de aplicații include orientări pentru dezvoltarea și lansarea aplicației NtS, cu explicații privind logica, procesele și valorile automate/implicite ale acesteia. Ghidul privind codificarea NtS pentru dezvoltatorii de aplicații este inclus în apendicele B la anexa la prezentul regulament.
2. Selecția tipului de mesaj NtS
— FTM: Alegeți acest tip dacă doriți să creați un „mesaj privind șenalul navigabil și traficul pe căile navigabile” pentru căile navigabile sau obiectele de pe căile navigabile [consultați capitolul 3].
— WRM: Alegeți acest tip dacă doriți să creați un „mesaj cu date privind apa”, care permite furnizarea de informații cu privire la nivelurile existente și cele preconizate ale apei, precum și alte informații. Datele privind apa cuprind informații despre un obiect sau o secțiune a șenalului navigabil. Obiectul este identificat prin codul aferent de localizare ISRS, iar secțiunea șenalului navigabil este definită prin codurile de localizare ISRS de început și sfârșit.
— ICEM: Alegeți acest tip dacă doriți să creați un „mesaj privind gheața”. Secțiunea cu mesajul privind gheața cuprinde informații despre condițiile gheții pe o întindere a șenalului navigabil definită prin codurile de localizare ISRS de început și de sfârșit.
— WERM: Alegeți acest tip dacă doriți să creați un „mesaj meteo”, care să permită furnizarea de informații despre situațiile climatice actuale și cele prognozate pe o întindere a șenalului navigabil definită prin codurile de localizare ISRS de început și de sfârșit.
3. Considerații de bază privind FTM, acțiunile întreprinse pentru publicarea unui FTM
Informații detaliate despre codurile care trebuie să fie utilizate sunt prezentate în capitolul 4. Considerațiile prezentate începând de la punctul 3.3 nu sunt neapărat în ordinea datelor dintr-un instrument de editare FTM.
| 3.1. | Este necesar ca informațiile să fie publicate prin intermediul NtS FTM conform standardului NtS? Toate informațiile relevante privind siguranța și planificarea voiajelor trebuie să fie publicate prin intermediul mesajelor NtS. Pot fi publicate informații care nu sunt relevante în ceea ce privește siguranța și planificarea voiajelor. Fiecare temă/incident/eveniment trebuie să fie publicat(ă) într-un mesaj separat.
| 3.2. | Există deja un FTM valabil în legătură cu situația actuală (legat de conținut și de perioada de valabilitate)?
| 3.2.1. | Da: FTM deja existent trebuie să fie actualizat. Mesajul respectiv publicat trebuie să fie selectat și actualizat în instrumentul de editare FTM. Un FTM expirat nu mai poate fi actualizat.
| 3.2.2. | Nu: Trebuie să fie compilat un nou FTM. În cazul în care un eveniment similar este deja codificat într-un FTM existent, FTM respectiv poate fi utilizat ca proiect pentru crearea unui nou FTM (dacă această funcție este disponibilă), sau se poate utiliza un șablon (dacă această funcție este disponibilă).
| 3.3. | Se stabilește aria geografică valabilă
| 3.3.1. | În cazul în care FTM este legat de o anumită întindere a unei căi navigabile, întinderea respectivă trebuie să fie inclusă și definită prin punctele sale de început și sfârșit. În cazul în care conținutul este valabil pentru mai multe secțiuni ale aceleiași căi navigabile sau pentru căi navigabile diferite, acestea pot fi enumerate toate într-un FTM.
| 3.3.2. | În cazul în care FTM este legat de un anumit obiect (de exemplu, pod, ecluză etc.) pe căile navigabile, obiectul respectiv va fi selectat din lista obiectelor disponibile (dacă selecția este disponibilă). Nu este nevoie să se definească o întindere a unei căi navigabile în mesaj. În cazul în care un FTM este valabil pentru mai multe obiecte, toate acestea pot fi incluse într-un singur FTM.
| 3.3.3. | Combinarea informațiilor despre obiecte și șenalul navigabil este posibilă într-un singur mesaj atâta timp cât informațiile se referă la o cauză/un eveniment specific(ă) (același subiect și cod al evenimentului).
| 3.3.4. | Deși coordonatele sunt condiționate, acestea sunt transmise pentru a susține afișarea pe hărți (deseori aceste coordonate sunt transmise automat de către aplicația NtS).
| 3.4. | Se introduce cuprinsul FTM Toate informațiile care pot fi exprimate cu ajutorul tabelelor de referință NtS trebuie să fie codificate în câmpurile de mesaje standardizate. Doar informațiile suplimentare (care nu pot fi codificate altfel) sunt prezentate în câmpurile pentru text liber.
| 3.5. | Grupul (grupurile) țintă privind tipul navelor și direcțiile afectate este/sunt introdus(e) dacă este cazul.
| 3.5.1. | În cazul în care mesajul este valabil pentru toate navele (toate tipurile de nave) în toate direcțiile, grupul țintă este omis pentru a codifica astfel doar informațiile esențiale. Dacă mesajul/restricția se adresează unui anumit grup-țintă sau unei anumite direcții, sunt selectate codurile respective.
| 3.5.2. | În cazul în care întregul mesaj este valabil pentru anumite grupuri-țintă, informațiile despre grupul-țintă sunt transmise în partea generală a FTM [nu repetate în secțiunea (secțiunile) dedicate restricției].
| 3.5.3. | În cazul în care există grupuri-țintă diferite aplicabile unor restricții diferite, informațiile despre grupul-țintă sunt transmise în limitele restricțiilor respective (nu repetate în partea generală).
| 3.5.4. | În cazul în care se permit excepții de la restricții pentru nave individuale sau pentru traficul local de către autoritățile competente (de exemplu, navele care participă la un eveniment pentru care este aplicabil un blocaj general, traficul local al feriboturilor în zonele blocate), astfel de excepții nu trebuie să fie luate în considerare la codificarea grupului (grupurilor) țintă. Astfel de informații pot fi menționate în câmpul aferent textului liber pentru informații suplimentare.
| 3.6. | Secțiunea privind comunicațiile se completează dacă este cazul Dacă există informații suplimentare obținute prin intermediul unei anumite surse, acestea trebuie să fie menționate în această secțiune. Dacă există o obligație suplimentară de a raporta pe o anumită cale, aceasta trebuie să fie menționată în această secțiune.
| 3.7. | Secțiunea privind restricțiile se completează dacă este cazul Dacă există restricții, se completează secțiunea privind restricțiile. Dacă se cunosc valori legate de restricții, acestea trebuie să fie menționate. Este obligatoriu să se prezinte valori pentru dimensiunile navelor, limita de viteză și spațiul disponibil pentru navigație. Toate restricțiile trebuie să includă perioadele de restricție pentru a permite efectuarea de calcule corecte în aplicațiile privind planificarea voiajelor (pentru a facilita munca, ar putea exista o funcție în aplicația NtS utilizată pentru a copia perioadele de restricție sau a selecta mai multe restricții pentru o perioadă de restricție).
| 3.8. | Se va fixa data inițială a perioadei de valabilitate a mesajului În cazul în care data de sfârșit a perioadei de valabilitate a unui mesaj este deja cunoscută, se fixează și aceasta. Data de sfârșit a perioadei de valabilitate nu trebuie să fie înainte de data actuală. Este de remarcat faptul că informațiile privind perioada de valabilitate vor fi utilizate de către aplicații pentru selecția mesajelor, care vor fi afișate utilizatorilor pentru un timp solicitat. În cazul în care mesajul este retras: (a) înainte ca perioada sa de valabilitate să înceapă să curgă, data inițială și data finală trebuie să fie fixate la data retragerii. (b) și perioada de valabilitate a început deja, noile date de sfârșit pentru toate restricțiile sunt fixate în trecut, iar data de sfârșit a perioadei de valabilitate trebuie să fie fixată la data retragerii.
| 3.9. | Mesajul poate fi publicat
4. Explicarea codurilor FTM
4.1. Subiectul notificării:
Definiția utilizării subiectelor notificării:
— „Alarmă”: relevantă pentru siguranță. Alarma trebuie să conțină cel puțin o restricție care determină în mod direct și concret punerea în pericol a persoanelor, a navelor sau a facilităților, de exemplu, lucrări de sudură pe un pod, care generează scântei, o cabină de verificare/lucrători suspendați pe un pod, un obstacol pe șenalul navigabil,
— „Anunț”: relevant pentru planificarea voiajelor sau pentru siguranță. Anunțul poate conține restricții, de exemplu, blocarea unui sas al ecluzei din cauza unor lucrări de întreținere, dragarea șenalului navigabil, reguli de trafic suplimentare față de cele din legislația națională,
— „Serviciu informativ”: informații generale care nu sunt legate direct de planificarea voiajelor sau de siguranță. Mesajul informativ nu trebuie să conțină restricții specifice, prin urmare nu este direct relevant pentru planificarea sau siguranța voiajelor. Astfel de informații ar putea include, de exemplu, reguli de trafic local, o actualizare a ECDIS interior. Perioada de valabilitate este utilizată pentru a indica ora de afișare a mesajului informativ pentru utilizatori, nu pentru perioada de valabilitate a informațiilor furnizate (de exemplu, o lună sau conform prevederilor din procedurile naționale).
— „Mesaj anulat”
Subiectul notificării „Mesaj anulat” este utilizat doar dacă
— data actuală este înainte de data inițială a perioadei de valabilitate. În acest caz, doar conținutul din câmpul „informații suplimentare în limba de origine” poate fi modificat; conținutul rămas al mesajului trebuie să rămână neschimbat. În acest caz, funcția „Mesaj anulat” este utilizată pentru a retrage o notificare înainte ca ea să devină valabilă. Aceasta înseamnă că funcția „Mesaj anulat” este utilizată pentru notificări care nu au ajuns la data inițială a perioadei de valabilitate și/sau pentru măsuri planificate care nu vor fi derulate (de exemplu, a fost planificată dragarea, însă aceasta nu poate fi pornită din cauza nivelului ridicat al apei);
— perioada de valabilitate a început deja, iar datele noi de sfârșit pentru toate restricțiile sunt fixate în trecut. Data de sfârșit a perioadei de valabilitate trebuie să fie fixată la data retragerii.
În acest caz, măsurile/evenimentele iau sfârșit înainte de încheierea perioadei de valabilitate fixate inițial pentru un FTM deja existent.
4.2. Codul evenimentului
Trebuie să se completeze secțiunea aferentă codului evenimentului pentru a oferi informații suplimentare comandanților de nave.
Definiția utilizării codurilor evenimentelor:
lucrări de construcții | Anunțarea de lucrări de construcții
calamitate | Alarmă pentru o calamitate
modificări la șenalul navigabil | Anunțarea unor modificări la șenalul navigabil
modificarea marcajelor | Anunțarea unor modificări la marcajele șenalului navigabil
restricționarea șenalului navigabil | Anunțarea unei lățimi reduse a șenalului navigabil dacă nu există un cod al evenimentului
marcaje/semne deteriorate | Anunțarea de marcare/semne deteriorate
scafandru sub apă | Alarmă în legătură cu un scafandru în apă
dragaj | Anunțarea lucrărilor de dragaj
eveniment | Anunțarea de evenimente, de exemplu, o competiție de înot, de navigație sau de vâsle
exerciții | Anunțarea de exerciții, de exemplu, exerciții de salvare sau militare
operațiune de deminare | Anunțarea unei operațiuni de deminare
deversare extinsă | Anunțarea unor rate mai mari de evacuare decât de obicei prin baraje sau ecluze din motive de gestionare a apei
materiale care cad | Anunțarea de materiale care prezintă pericol de cădere, de exemplu, blocuri de gheață, crengi de copaci
ecouri radar false | Anunțarea posibilității existenței unor ecouri radar false
artificii | Anunțarea focurilor de artificii
materii plutitoare | Anunțarea existenței de materii plutitoare deasupra nivelului apei (vizibile) și sub nivelul apei (invizibile)
măsurarea debitului | Anunțarea activităților de măsurare
risc pentru sănătate | Alarmă sau anunț, de exemplu, cu privire la omida procesionară a stejarului, la scăpări de gaze etc.
un cablu de înaltă tensiune | Anunțarea intersecției cu un cablu de înaltă tensiune
nivel ridicat al apei | Anunțarea existenței unui nivel ridicat al apei înainte de atingerea nivelului apei care impune interdicții
gheață | Anunțarea existenței gheții; informații suplimentare se vor transmite prin intermediul mesajelor cu informații despre gheață (mesajul privind gheața)
Actualizarea ECDIS interior | Un serviciu informativ privind o actualizare a ECDIS interior
inspecție | Anunțarea unor lucrări de inspecție; se utilizează doar în cazul inspecției; nu se utilizează pentru lucrări de (reparații/construcții) Pot exista restricții din cauza vehiculelor/cuștilor de inspecție sau a schelelor
lansare | Anunțarea plecării unui vas de pe șantierul naval
reguli de trafic local | Serviciu informativ privind reguli suplimentare sau schimbate ale unor legi sau regulamente valabile, fără restricții, date ale restricțiilor sau date de valabilitate speciale
nivel scăzut al apei | Anunțarea existenței unui nivel scăzut al apei înainte de atingerea nivelului apei care impune interdicții
reducerea nivelului apei | Anunțarea unei reduceri controlate a nivelului apei pentru inspecții sau lucrări ori din motive de gestionare a apei
deversare minimă | Anunțarea unor rate mai reduse de evacuare decât de obicei prin baraje sau ecluze din motive de gestionare a apei
un nou obiect | Anunțarea de informații privind un nou obiect disponibil, de exemplu, un pod, o dană
obstacol | Anunțarea unei înălțimi reduse a apei și/sau a unei lățimi reduse a șenalului navigabil din cauza unui obstacol deasupra nivelului apei
restricție sub apă | Anunțarea unei adâncimi disponibile reduse a apei și/sau a unei lățimi reduse a șenalului navigabil din cauza unui obstacol sub apă
existența unui nivel al apei care impune interdicții | Anunțarea unui nivel (ridicat sau scăzut) al apei, ceea ce determină interzicerea navigației
acoperire radio | Anunțarea unei acoperiri radio
eliminarea unui obiect | Anunțarea eliminării unui obiect
reparații | Anunțarea unor defecțiuni sau a unor stări de nefuncționare care trebuie remediate, de exemplu privind sistemul de control al ecluzelor; această cale poate fi utilizată, de asemenea, pentru reparații planificate
existența unui nivel în creștere al apei | Anunțarea unor creșteri naturale ale nivelurilor apei, care nu sunt puse pe seama gestionării apei
aluvionare | Anunțarea unei adâncimi disponibile reduse din cauza aluvionării
lucrări de consolidare | Anunțarea unor lucrări de consolidare
marcaje speciale | Anunțarea utilizării unor marcaje speciale, de exemplu, pentru blocarea pătrunderii în anumite ape sau zone de pescuit
transport special | Anunțarea unor transporturi speciale
grevă | Anunțarea unei greve a personalului operator cu impact asupra disponibilității infrastructurii căilor navigabile
nivel al apei care impune o navigație atentă | Anunțarea unui nivel (ridicat sau scăzut) al apei care impune o atenție specială la navigare
lucrări | Anunțarea de lucrări generale la obiecte, la maluri și/sau în albia căilor navigabile (fluvii sau canale)
restricții | Se utilizează doar pentru a indica existența unor restricții dacă nu se aplică niciun cod al evenimentului
altele | Nu se utilizează; în cazul în care nu se potrivește niciun alt cod al evenimentului, secțiunea aferentă codului evenimentului nu se completează
4.3. Limitation_code:
Definiția utilizării codurilor de restricții:
— blocaj:
În cazul în care nicio formă de navigație nu este posibilă:
— prin sasuri ale ecluze;
— printr-o deschidere de pod;
— printr-un punct specific al șenalului navigabil;
— pe o secțiune specifică a șenalului navigabil.
— restricție parțială:
Toate părțile infrastructurii (de exemplu, sasuri ale ecluzelor, deschideri de pod) au propriul cod de localizare ISRS. În cazul în care astfel de coduri încă lipsesc, restricția poate fi utilizată în cazul în care este posibilă navigația limitată (de exemplu, este disponibil doar obiectul din zona ecluzei în cazul unei ecluze care are două sasuri paralele)
— prin unul sau mai multe sasuri ale unei ecluze, lăsând deschis cel puțin unul dintre acestea;
— prin unul sau mai multe deschideri de pod, lăsând cel puțin o deschidere.
— întreruperea serviciului:
se utilizează în cazul în care podul mobil nu funcționează pe parcursul unei perioade specificate. Această perioadă trebuie să se încadreze în orarul normal de funcționare.
Întreruperea serviciului unui pod mobil înseamnă că trecerea pe sub pod este încă posibilă. În caz contrar, este vorba despre un „Blocaj” Nicio funcționare a unei ecluze nu este codificată ca „Blocaj”.
— modificarea serviciului:
se utilizează în cazul în care orarul normal de funcționare al obiectelor [de exemplu, ecluze, poduri (mobile)] este schimbat, prelungit sau redus.
— Dacă există restricții legate de dimensiuni permise ale navei/convoiului (nu în legătură directă cu infrastructura), restricția este codificată cu următoarele elemente de text:
— pescajul navei;
— lățimea navei;
— lățimea convoiului;
— lungimea navei;
— lungimea convoiului;
— înălțimea deasupra liniei de plutire.
Dacă există, se menționează o valoare absolută.
— Dacă există restricții legate de dimensiunea disponibilă a unui obiect sau a unei secțiuni a căii navigabile, se utilizează următoarele coduri:
— gabaritul de înălțime;
— lungimea disponibilă;
— gabaritul de lățime;
— adâncimea disponibilă.
Dacă există, se menționează o valoare absolută.
— adâncimea minimă: se utilizează în cazul în care adâncimea poate pune probleme (de exemplu, din cauza aluvionării). Se prezintă o valoare pentru adâncimea absolută (denumită valoare de referință) sau reducerea adâncimii. Dacă există, se menționează o valoare absolută.
— întârziere: se utilizează în cazul în care apare o restricție/un incident cu o durată limitată la un obiect sau pe o secțiune a căii navigabile între o dată specificată și data de sfârșit.
Durata maximă estimată a restricției/incidentului se codifică. Întârzierea nu se utilizează în cazurile în care unul sau mai multe sasuri ale unei ecluze nu este/sunt disponibil(e).
— Dacă sunt interzise anumite manevre sau acțiuni, se codifică restricțiile respective. Aceste restricții se codifică doar dacă nu sunt deja anunțate pe calea semnalelor de navigație sau prin regulamente care sunt codificate pe harta ENC oficială pentru apele interioare:
— putere minimă;
— instrucțiune de trafic alternativă;
— întoarcerea interzisă;
— trecerea interzisă;
— depășirea interzisă;
— andocarea interzisă;
— interdicție de acostare;
— ancorarea interzisă;
— formarea valurilor interzisă;
— limita de viteză;
— nu este permis să se meargă la țărm.
Dacă este disponibilă, se indică o valoare absolută pentru limita de viteză și puterea minimă.
— atenționare specială: În cazul în care FTM (sau o parte dintr-un FTM) este legat de un șenal navigabil/o cale navigabilă, această restricție este utilizată pentru a indica în ce parte a șenalului navigabil/fluviului/canalului are loc un incident.
De asemenea, aceasta este utilizată în cazurile în care nu este posibilă descrierea detaliată a restricției, însă este utilă sau necesară pentru a avertiza sau a informa comandanții de nave că trebuie să fie prudenți și să acorde atenție informațiilor radio.
— nu există restricții: se utilizează doar în cazul în care se precizează în mod explicit că nu există restricții într-o anumită perioadă de timp.
4.4. Limitation interval_code: definirea utilizării codurilor de intervale:
— „permanent”: se utilizează în cazul restricțiilor care sunt valabile fără întrerupere de la o dată/oră inițială până la o dată/oră de sfârșit (de exemplu, blocaj de la 01.01.2016, orele 00:00 până la 31.03.2016, orele 23:59 și, de asemenea, blocaj în data de 17.09.2016 în intervalul orar 08.00-18.00).
— „zilnic”: se utilizează aplicarea repetată și în mod regulat a unei restricții (de exemplu, se interzice formarea valurilor în timpul programului de funcționare într-o zonă de dragare – în perioada 07.04.2016-11.04.2016, zilnic de la orele 6.00 până la orele 18.00).
— în timpul zilei (conform definiției din CEVNI): Termenul „zi” înseamnă perioada dintre răsărit și apus.
— în timpul nopții (conform definiției din CEVNI): Termenul „noapte” înseamnă perioada dintre apus și răsărit.
— Zilele săptămânii: dacă există intervale legate de diferite zile ale săptămânii, acestea trebuie să fie selectate dintre următoarele elemente de text:
— luni,
— marți,
— miercuri,
— joi,
— vineri,
— sâmbătă,
— duminică,
— de luni până vineri,
— zilele de sâmbătă și duminică.
— „în caz de vizibilitate redusă”: se utilizează dacă restricția este aplicată doar în cazul condițiilor în care vizibilitatea este redusă din cauza ceții, a negurii, a zăpezii, a ploii sau din alte motive.
— „cu excepția”: aceasta nu trebuie să fie utilizată; Intervalele întrerupte trebuie să fie date ca perioade de restricție separate în cadrul aceleiași restricții. Acest lucru se datorează faptului că software-ul pentru planificarea voiajelor nu poate interpreta acest cod în mod corect ca nefiind desfășurate la o anumită dată sau oră. Astfel, nu este posibil să se calculeze în mod corect ETA (orele estimate de sosire).
— „De luni până vineri, cu excepția sărbătorilor legale”: se utilizează doar dacă sărbătorile legale se încadrează în perioada de valabilitate a restricției. Ca serviciu pentru utilizatori, sărbătorile legale pot fi indicate în secțiunea aferentă textului liber din FTM. Software-ul pentru planificarea voiajelor nu va putea să țină cont de sărbătorile legale naționale la calcularea ETA.
4.5. Indication_code:
Secțiunea Indication_code este prevăzută a fi utilizată pentru informații despre valori specifice privind anumite restricții (de exemplu, limita de viteză, puterea minimă, adâncimea disponibilă). Pentru a stabili anumite dimensiuni, este necesară o trimitere fie la un sistem de referință (geografic sau hidrologic) extern (de exemplu, gabaritul de înălțime, adâncimea disponibilă, adâncimea minimă), fie la dimensiuni cunoscute ale unor structuri artificiale (de exemplu, lungimea disponibilă, gabaritul de lățime).
| 4.5.1. | Dacă se cunosc dimensiuni sau trimiteri absolute, acestea trebuie să fie utilizate. Se utilizează valori relative doar dacă nu este posibil să se facă trimitere la un sistem de referință extern.
| 4.5.2. | reducere cu | → aceasta este o valoare relativă
| 4.5.3. | maximum | → aceasta este o valoare absolută
| 4.5.4. | minimum | → aceasta este o valoare absolută
| 4.5.5. | Dacă dimensiunea care indică o restricție se referă la o coordonată geografică sau hidrologică, sistemul de referință respectiv trebuie să fie indicat în mesajul NtS (de exemplu, gabarit de înălțime de minimum 4 m față de cel mai înalt nivel navigabil al apei); adâncimea disponibilă de minimum 1,7 m față de nivelul redus reglat al apei)
| 4.5.6. | Dacă dimensiunea care indică o restricție se referă la o dimensiune a unei structuri artificiale (de exemplu, pod, sas), trimiterea poate fi dată raportat la dimensiuni cunoscute (de exemplu, gabaritul de înălțime redus cu 1,5 m, lungimea disponibilă redusă cu 27 m).
4.6. Position_code (obiecte):
Ori de câte ori este posibil, secțiunea Position_code se referă la partea șenalului navigabil pe care se află obiectul față de axa șenalului (stânga/mijloc/dreapta) sau la alte informații (vechi/noi) cunoscute, de regulă, sau la direcția geografică (nord/sud/est/vest). Secțiunea position_code pentru obiecte poate fi completată în prealabil în mod automat din datele de referință din indexul RIS. Stânga/dreapta șenalului navigabil este definită a fi partea privită în direcția în aval.
4.7. Position_code (șenaluri/căi navigabile):
Nu este prevăzută o secțiune Position_code pentru un FTM (sau o parte dintr-un FTM) care să se refere la un șenal navigabil sau la o cale navigabilă. Pentru a indica pe ce parte a șenalului/canalului/fluviului/lacului are loc un incident, se utilizează restricția „Vigilență mărită”, în combinație cu restricția adecvată Position_code.
4.8. Position_code (restricții):
| 4.8.1. | Ori de câte ori este posibil, secțiunea Position_code se referă la partea șenalului navigabil sau a obiectului unde apare restricția (stânga/dreapta). Stânga/dreapta șenalului navigabil este definită a fi partea privită în aval.
| 4.8.2. | Secțiunea Position_code direcționează atenția comandantului navei spre partea șenalului navigabil unde se află, de exemplu, o zonă de interes special, un pericol sau un obstacol. Prin urmare, este suficientă o indicație estimativă (de exemplu, malul stâng – stânga – mijloc – dreapta – malul drept). Nu este prevăzută o subdiviziune mai precisă.
| 4.8.3. | Dacă este necesar, ar fi preferabil să se ofere informații mai precise privind poziția prin intermediul hărților sau al schițelor (fișier anexat, a se vedea capitolul 3.6).
| 4.8.4. | În cazul secțiunilor pe care indicația obișnuită a poziției, în funcție de partea șenalului (stânga/dreapta) nu pare adecvată (de exemplu, bazine în port, anumite secțiuni de canale fără o direcție distinctă de curgere), se pot utiliza punctele cardinale (nord/est/sud/vest).
4.9. Target_group_code (a se vedea capitolul 3.5)
4.10. Reporting_code
| 4.10.1. | Secțiunea Reporting_code se utilizează, ca regulă generală, doar în cazul în care există o nevoie specială de comunicare (de exemplu, o obligație suplimentară de raportare la autoritatea locală în contextul unui regulament de trafic local) sau în cazul în care sunt disponibile informații suplimentare (de exemplu, punctul de contact VHF, precum numele canalului sau indicativul de apel pentru poziția actuală a dragei) cu relevanță directă pentru FTM.
| 4.10.2. | Se evită reiterarea de rutină a datelor de comunicare disponibile public (de exemplu, numere de telefon ale autorităților locale, canalele VHF ale ecluzelor etc.) dacă nu există o legătură directă a unei astfel de comunicări în raport cu FTM.
| 4.10.3. | Mijloacele de comunicare cu aplicabilitate generală conform reglementării oficiale (de exemplu, comunicarea VHF între nave și între nave și țărm, astfel cum este prevăzut în CEVNI sau prin norme regionale sau naționale pentru navigație) nu se repetă, de regulă, în secțiunea Reporting_code dacă nu există o legătură directă pentru o astfel de comunicare în raport cu FTM).
4.11. Communication_code
se utilizează următorul format (exemple):
— VHF „număr, indicativ de apel”: „10, Schifffahrtsaufsicht Wien”
— Număr de telefon sau fax: „+43123456789, Schifffahrtsaufsicht Wien”
— Adresa de internet: „http://example.com”
— Semnalizare sonoră: „long blast / langer Ton”
— E-mail: „example@authority.eu”
— Număr căsuță poștală EDI: „900012345@edi.bics.nl”
— Teletext: „ARD, 992 – 995”
4.12. Type_code:
O cale navigabilă este un canal, un lac sau un fluviu.
— zonă de ancorare
— mal
— baliză
— dană
— control la frontieră
— pod
— deschidere pod
— geamandură
— cablu aerian
— canal [termenul „canal” este utilizat dacă un mesaj se referă la întregul canal (nu doar la șenalul navigabil)]
— pod peste canal: apeduct
— conductă
— șenal navigabil (termenul „șenal navigabil” înseamnă partea căii navigabile care poate fi utilizată efectiv pentru navigație).
— feribot
— doc plutitor
— stăvilar (un stăvilar este utilizat pentru a proteja o zonă în cazul unor niveluri ridicate ale apei)
— port
— facilitate portuară
— căpitănie
— lac [termenul „lac” este utilizat dacă un mesaj se referă la întregul lac (nu doar la șenalul navigabil)]
— indicator luminos
— bazinul ecluzei: sas individual al unei ecluze
— Ecluză: întregul complex al ecluzei
— posibilitate de acostare
— panou de semnalizare
— conductă
— conducte suspendate
— rampă
— stație de colectare a deșeurilor
— punct raportare
— lac de acumulare
— fluviu [termenul „fluviu” este utilizat dacă un mesaj se referă la întregul fluviu (nu doar la șenalul navigabil)]
— ridicare navă
— șantier naval
— stație de semnalizare
— terminal
— miră de maree
— tunel
— loc de rondou
— centru de trafic nave
— baraj (un baraj este utilizat pentru a controla nivelul apei din fluvii)
5. Considerații de bază privind WRM
Datele despre apă sunt generate, de regulă, în mod automat. În cazul în care acest lucru nu este posibil, generarea manuală a WRM respectă cât mai strict procesele prevăzute pentru WRM generate automat (a se vedea Ghidul privind codificarea NtS pentru dezvoltatori).
6. Considerații de bază privind ICEM, acțiunile întreprinse pentru publicarea unui ICEM
Mesajele privind gheața depind de observația și evaluarea locală și, de regulă, vor fi generate de către personalul autorizat.
În cazul gheții, se emite un ICEM. Gheața nu determină neapărat restricționarea navigației, însă pot fi oferite informații despre starea gheții care nu îngreunează navigația.
| 6.1. | Este necesar ca informațiile să fie publicate prin intermediul NtS ICEM? Primul mesaj privind gheața pentru o porțiune se publică doar în cazul în care există gheață pe căile navigabile sau pe afluenți și, de asemenea, atunci când nu există restricții.
| 6.2. | Există deja un ICEM valabil pentru porțiunea afectată a căii navigabile?
| 6.2.1. | Da: Dacă există un mesaj (încă) valabil pentru porțiunea afectată, mesajul deja existent va fi actualizat. Mesajele existente privind gheața pot fi actualizate chiar dacă aria de aplicabilitate se schimbă (de exemplu, suprafața cu gheață se extinde, iar suprafața porțiunii afectate crește).
| 6.2.2. | Nu: Dacă nu există un mesaj valabil privind gheața pentru porțiunea afectată, va fi creat un nou mesaj.
| 6.3. | însă pot fi oferite și informații despre starea gheții care nu îngreunează navigația.
| 6.4. | Un ICEM este întotdeauna valabil pentru o singură porțiune a căii navigabile. Aria geografică valabilă se stabilește prin definirea căii navigabile și a punctelor hectometrice respective de început și sfârșit (sau prin alegerea anumitor secțiuni consecutive, în funcție de aplicarea la nivel național).
| 6.5. | Se introduce timpul de măsurare. Stările respective ale gheții se introduc folosind cel puțin una dintre listele de coduri (în funcție de cerințele naționale).
| 6.5.1. | Ice_condition_code
| 6.5.2. | Ice_accessibility_code
| 6.5.3. | Ice_classification_code
| 6.5.4. | Ice_situation_code (codul privind situația gheții trebuie să fie indicat întotdeauna pentru a permite prezentarea situației gheții pe o hartă folosind culori de „semafor”).
| 6.6. | ICEM poate fi publicat. Mesajele privind gheața vor fi valabile în mod automat până în următoarea zi după publicare sau până la momentul prevăzut prin procedurile naționale.
7. Considerații de bază privind WERM
Ținând cont de abundența serviciilor și aplicațiilor web disponibile pentru prognoza meteo și pentru alerte meteo, WERM trebuie utilizat doar pentru informații despre vreme de o anumită importanță pentru navigație, care nu sunt acoperite de serviciile generale de informare meteorologică.
Mesajele despre vreme sunt generate, de regulă, în mod automat. Atunci când acest lucru nu este posibil, generarea manuală a WERM respectă cât mai strict procesele prevăzute pentru WERM generate automat (a se vedea Ghidul privind codificarea NtS pentru dezvoltatorii de aplicații).
8. Reguli pentru anumite elemente
8.1. Reguli pentru elementul „nume” legat de obiecte
Numele obiectelor sunt, de regulă, completate în prealabil de instrumentul de editare NtS pe baza datelor de referință din indexul RIS. Numele sunt introduse în limbajul local; astfel, se pot utiliza, de exemplu, și diacritice sau litere chirilice. (de exemplu, Baarlerbrücke, Volkeraksluis sau Mannswörth).
Nu se includ informații despre caracteristici, iar tipul obiectului nu se repetă în nume, cu excepția cazului în care sunt oferite informații suplimentare pentru tipul obiectului.
De exemplu: Ecluza „Schleuse Freudenau” este denumită doar „Freudenau”, tipul obiectului „ecluză” este adăugat automat pe baza funcției type_code.
De exemplu: Numele obiectului pentru podul peste calea ferată din Krems (AT) este „Eisenbahnbrücke Krems”. Informațiile despre obiectul „pod peste calea ferată” sunt incluse în numele obiectului, întrucât adaugă informații în plus față de type_code „pod”.
De exemplu: Numele obiectului pentru un pod în Linz (AT) este „Nibelungenbrücke”. Termenul „brücke” se menține în interiorul numelui obiectului deoarece face parte din numele podului.
De exemplu: Indicatorul nivelului apei căii navigabile „Pegelstelle Wildungsmauer” este denumit „Wildungsmauer”, deoarece informațiile privind faptul că acest obiect este un indicator de nivel sunt deja codificate în type_code.
Dacă o secțiune a căii navigabile constituie demarcația dintre două țări cu limbi diferite, numele național al obiectului poate fi indicat în ambele limbi (de exemplu, „Staatsgrenze AT-SK/Statna hranica AT-SK”).
8.2. Reguli pentru elementul „nume” legat de șenaluri navigabile
Numele șenalurilor navigabile sunt, de regulă, completate în prealabil de instrumentul de editare NtS pe baza datelor de referință din indexul RIS. Câmpul „nume” conține numele local al respectivei secțiuni a șenalului (de exemplu, „Rhein”) În funcție de procesele naționale, ar putea fi posibil să se editeze numele șenalului navigabil pentru a include nume sau structuri adăugate utilizate frecvent la nivel local (de exemplu, „Rhein am Deutschen Eck”).
8.3. Reguli pentru elementele „valoare” și „unitate” fără restricții
Cu excepția cazului când se prevede altfel, în mesajele NtS se permite doar utilizarea cm, m3/s, h, km/h și kW, m/s (vânt), mm/h (precipitații) și a gradelor Celsius.
B. GHIDUL PRIVIND CODIFICAREA NOTIFICĂRILOR TRANSMISE COMANDANȚILOR DE NAVE PENTRU DEZVOLTATORII DE APLICAȚII
CUPRINS
1. | Context și structură | 24
1.1. | Scopul Ghidului privind codificarea NtS | 24
1.1.1. | Ghid privind codificarea NtS pentru editori | 24
1.1.2. | Ghid privind codificarea NtS pentru dezvoltatori de aplicații (acest document) | 24
2. | Mesaje și secțiuni NtS | 24
3. | Considerații de bază privind WRM | 26
3.1. | Completarea secțiunii nts_number în WRM | 26
3.2. | Completarea WRM, inclusiv a previziunilor | 26
4. | Procesele ICEM | 27
4.1. | Un ICEM nou | 28
4.2. | Actualizarea unui ICEM existent | 28
5. | Considerații de bază privind WERM | 29
5.1. | Completarea secțiunii nts_number în WERM | 29
5.2. | Completarea secțiunii „weather_category_code” din WERM | 29
6. | Procesele FTM | 30
6.1. | Un FTM nou | 30
6.2. | Actualizarea/retragerea unui FTM existent | 30
6.3. | FTM privind căile navigabile și/sau obiectul | 31
6.4. | Ordonarea automată a codurilor de restricție | 31
6.5. | Gestionarea perioadelor de restricții | 32
7. | Norme generale privind punerea în aplicare | 33
7.1. | Completarea secțiunii „number_section” | 33
7.2. | Completarea elementelor „expeditorul mesajului”, „autorul informațiilor”, „organizația” și „sursa notificării (autoritatea)” | 33
7.3. | Omiterea elementelor | 34
7.4. | Completarea automată a secțiunii date_issue | 34
7.5. | Gestionarea informațiilor privind fusul orar în mesajele NtS | 34
7.6. | Gestionarea secundelor în mesajele NtS | 34
7.7. | Formatul zecimalelor în mesajele NtS | 34
7.8. | Unitățile utilizate în mesajele NtS | 34
7.9. | Reguli pentru elementele „name”, „position_code” și „type_code” | 34
7.10. | Reguli pentru elementul „fairway_name” | 38
7.11. | Clarificări pentru traducerile din foaia de calcul „reference_code” | 38
7.12. | Recomandare pentru elementul „coordinate” | 38
7.13. | Abordarea grupurilor-țintă | 38
7.14. | Afișarea mesajelor valabile la o oră dată | 39
7.15. | Funcții opționale pentru creșterea gradului de accesibilitate a instrumentelor de editare a NtS pentru utilizatori | 39
8. | Structura mesajului NtS XML | 39
9. | Serviciul web NtS | 39
9.1. | Obiectiv | 39
9.2. | Principii de bază și restricții | 40
9.2.1. | Standarde web | 40
9.2.2. | Modelul de interacțiune și metoda de codificare pentru NtS WS | 40
9.3. | Specificații și recomandări generale | 40
9.3.1. | Specificații: Informații privind versiunea | 40
9.3.2. | Specificații: Structura spațiilor de nume | 41
9.3.3. | Recomandare: Utilizarea spațiilor de nume | 41
9.3.4. | Recomandare: Utilizarea prefixelor în spațiile de nume | 41
9.3.5. | Specificații: Utilizarea codurilor de localizare ISRS | 41
9.4. | Serviciul de mesaje NtS (specificație pentru implementare) | 46
9.4.1. | Solicitare | 46
9.4.2. | Memoriu în răspuns | 47
9.5. | Generarea de servicii și clienți | 48
Glosar | 48
1. Context și structură
Notificările transmise comandanților navelor (NtS) au fost puse în aplicare în diferite țări europene în temeiul Regulamentului (CE) nr. 416/2007 al Parlamentului European și al Consiliului privind specificațiile tehnice ale notificărilor transmise comandanților de nave menționate la articolul 5 din Directiva 2005/44/CE (RIS). Standardul NtS se află într-un proces continuu de îmbunătățire, iar un pas important înainte îl constituie lansarea serviciului web NtS (NtS Web Service) care facilitează schimbul de mesaje NtS între autorități și între autorități și utilizatorii NtS, precum și a aplicației NtS XSD 4.0 care uniformizează codificarea mesajelor NtS.
1.1. Scopul Ghidului privind codificarea NtS
Ghidul privind codificarea NtS explică aplicabilitatea celor patru tipuri de mesaje NtS, precum și codurile care se utilizează în cazul anumitor evenimente. Acesta oferă editorilor NtS instrucțiuni de completare a mesajelor NtS, permițând astfel codificarea armonizată a mesajelor NtS la nivel național și internațional.
Având în vedere rata ridicată de utilizare a serviciului web NtS, mesajele NtS trebuie armonizate în continuare pentru a asigura afișarea adecvată a conținutului în sistemele terților. Codificarea uniformă a mesajelor este, de asemenea, o cerință preliminară pentru a ține cont de mesaje în aplicațiile privind planificarea voiajelor. Versiunea 1.0 a Ghidului privind codificarea NtS se aplică în cazul NtS XSD 4.0 și al serviciul web pentru NtS WSDL 2.0.4.0.
1.1.1. Ghid privind codificarea NtS pentru editori
Ghidul privind codificarea NtS pentru editori este conceput pentru personalul care editează (și publică) mesajele NtS, incluzând instrucțiuni pas cu pas pentru crearea tipurilor de mesaje adecvate, precum și explicarea codurilor. Ghidul privind codificarea pentru editori include, de asemenea, informații relevante pentru dezvoltatorii de aplicații.
1.1.2. Ghid privind codificarea NtS pentru dezvoltatori de aplicații (acest document)
Ghidul privind codificarea NtS pentru dezvoltatori include orientări pentru lansarea aplicației NtS, cu explicații privind logica, procesele și valorile automate/implicite ale acesteia.
2. Mesaje și secțiuni NtS
Un mesaj NtS cuprinde următoarele:
— secțiunea privind identificarea
— secțiunea care definește obiectul (obiectele) aplicabil(e) sau porțiunea (porțiunile) șenalelor navigabile la care se face referire în mesaj;
— una sau mai multe dintre următoarele secțiuni conform tipului de mesaj:
— restricția (restricții) pentru mesajul privind șenalul navigabil și traficul pe căile navigabile,
— valoarea (valorile) de măsurare pentru datele despre apă,
— starea (stările) gheții pentru mesajul privind gheața,
— raportul (rapoartele) despre vreme pentru mesajul meteo.
Figura 2
Vizualizarea structurii mesajului NtS: element obligatoriu (1), element obligatoriu care poate apărea o dată sau de două ori (1…2), element obligatriu care trebuie să apară de două ori (2), elemente obligatorii care pot apărea oricât de frecvent este necesar (1-n), element opțional care poate apărea oricât de frecvent este necesar (0…n)
[figură]
Secțiunea privind identificarea este obligatorie și include informații generale privind autorul mesajului, expeditorul, data emiterii, țara și limba de origine, care sunt furnizate împreună cu unul dintre cele patru tipuri diferite de secțiuni de mesaj NtS:
— Secțiunea privind șenalul navigabil și traficul pe căile navigabile: un „Mesaj privind șenalul navigabil și traficul pe căile navigabile” (FTM) este creat, de regulă, de către editorii NtS cu respectarea Ghidului privind codificarea NtS pentru editori. Acesta este legat de porțiunile căilor navigabile (definite prin codurile de localizare ISRS de început și de sfârșit) și/sau obiectele de pe căile navigabile definite prin codul de localizare ISRS respectiv [consultați capitolul 6].
— Secțiunea privind nivelul apei: o secțiune „Date despre apă” (WRM) facilitează furnizarea de informații cu privire la nivelurile existente și cele preconizate ale apei, precum și alte informații. De regulă, WRM sunt create în mod automat (și periodic) pe baza unor măsurători ale senzorilor sau a stării infrastructurii care nu necesită o interacțiune cu editorul NtS. Secțiunea cu date despre apă cuprinde informații pentru un obiect (de exemplu, stația indicatoare de nivel) sau o secțiune privind un șenal navigabil (de exemplu, adâncimea minimă pentru o porțiune de apă, regimul aplicabil pe o secțiune a căii navigabile). Obiectul este identificat prin codul aferent de localizare ISRS, iar secțiunea șenalului navigabil este definită prin codurile de localizare ISRS de început și sfârșit [consultați capitolul 3].
— Secțiunea privind gheața: o secțiune „Date privind gheața” (ICEM) cuprinde informații despre condițiile gheții pe o întindere a șenalului navigabil definită prin codurile de localizare ISRS de început și de sfârșit [consultați capitolul 4].
— Secțiunea privind vremea: un „mesaj meteo” (WERM) permite furnizarea de informații despre situațiile climatice actuale și cele prognozate pe o întindere a șenalului navigabil definită prin codurile de localizare ISRS de început și de sfârșit [consultați capitolul 5].
În plus, codul de localizare ISRS (Standardul internațional privind raportarea navelor) este utilizat pentru a defini obiectul (obiectele) aplicabil(e) sau secțiunea (secțiunile) șenalului aplicabil(e) de care este legat mesajul.
Codul de localizare ISRS este definit la punctul 4.3 din anexa la prezentul regulament.
3. Considerații de bază privind WRM
Informațiile privind nivelul apei sunt foarte importante atât pentru planificarea voiajelor, cât și pentru siguranța ei. În prezent, nu există un standard comun de referință pentru informațiile privind nivelul apei. Valorile mirelor se bazează pe niveluri diferite ale mării sau pe puncte speciale de referință. Pentru a oferi o referință adecvată, secțiunea „reference_code” trebuie să fie întotdeauna completată cu valoarea. WRM poate fi utilizat pentru a oferi următoarele informații:
— nivelul apei (inclusiv previziuni),
— adâncimea minimă (inclusiv previziuni),
— înălțime liberă de trecere (inclusiv previziuni),
— debitul (inclusiv previziuni),
— situația barajului,
— regimul.
Clarificările privind traducerile din tabelul „reference_code” sunt prezentate în capitolul 7.11.
De regulă, WRM sunt create și publicate în mod automat pe baza informațiilor primite de la echipamentul senzor sau a informațiilor primite de la infrastructură (de exemplu, predicții, situația barajului). Pot exista diferiți factori declanșatori pentru publicarea WRM, de exemplu, periodic sau atunci când se ating anumite valori.
3.1. Completarea secțiunii nts_number în WRM
În NtS XSD 4.0, numărul NtS este opțional în mesajele WRM. Dacă acesta este indicat, fiecare număr trebuie să fie unic (organizație/an/număr/serie) pe tip de mesaj și este de resortul organizației care transmite WRM să garanteze atribuirea de numere unice (nu se cere să existe numere consecutive).
3.2. Completarea WRM, inclusiv a previziunilor
Secțiunea date_start din validity_period trebuie să fie completată cu data actuală (date_issue) și date_end din validity_period trebuie să fie completată cu următoarea zi după date_issue.
Pentru a furniza, de exemplu, modificări privind nivelul apei într-un mod care să faciliteze utilizarea, se poate indica în secțiunea aferentă diferenței WRM diferența față de o măsurătoare comparativă anterioară. În afară de modificarea valorii (de exemplu, - 5 [cm]), trebuie să fie indicată, de asemenea, diferența de timp față de măsurătoarea comparativă.
În cazul previziunilor, „measure_date” constituie data/ora pentru care este valabilă previziunea.
Previziunile privind nivelul apei includ întotdeauna un factor de incertitudine. De regulă, sunt calculate modele cu parametri diferiți (de exemplu, prognoze meteo), care conduc la diferite valori prevăzute ale apei. Pentru a permite indicarea unei valori estimate minime și maxime, de exemplu, vizualizarea unui interval de încredere pentru previziunea privind nivelul apei, în secțiunea privind „măsura” WRM sunt incluse două câmpuri suplimentare opționale de date.
În următoarea figură se prezintă o ilustrare a intervalului de încredere a previziunilor privind nivelul apei:
Figura 3
Vizualizarea intervalului de încredere a estimării nivelului apei: valoarea cea mai probabilă (de culoare neagră), limita superioară a intervalului de încredere (de culoare violetă), limita inferioară a intervalului de încredere (de culoare roșie), nivelul măsurat al apei (de culoare albastră)
(Axa x indică timpul; axa y indică nivelul apei în cm.)
[figură]
În NtS XSD sunt disponibile două elemente:
<value_min> | cea mai mică valoare a intervalului de încredere
<value_max> | cea mai mare valoare a intervalului de încredere
În afară de nivelurile prevăzute ale apei, intervalul de încredere poate fi utilizat, de asemenea, pentru a indica incertitudinea adâncimii minime publicate și informații privind înălțimea liberă de trecere.
Secțiunile value_min și value_max pentru intervalul de încredere permit indicarea intervalului de încredere a valorilor WRM prin intermediul NtS WRM Message standardizat pentru utilizare în grafice. Datele brute în sine nu se afișează utilizatorilor IWT (de exemplu, în formatul codului).
Secțiunea measure_code „NOM” nu trebuie să fie utilizată. În cazul în care nu există nicio măsurătoare pentru un anumit tip de WRM, elementele valorilor trebuie să fie omise dacă trebuie oricum să se transmită un mesaj.
4. Procesele ICEM
Mesajele privind gheața depind de observațiile și evaluarea locală și, de regulă, sunt generate manual (în cazul generării automate, trebuie să fie respectate regulile privind crearea manuală, a se vedea Ghidul privind codificarea NtS pentru editori).
ICEM este publicat pentru o anumită secțiune a șenalului navigabil (fairway_section) definită prin codurile sale ISRS de localizare de început și de sfârșit și conține starea gheții (ice_condition) la o anumită dată de măsurare.
Valabilitatea ICEM începe la data publicării (fixată automat prin aplicația NtS). Pentru a evita afișarea ICEM utilizatorilor care nu mai sunt validați, aplicația NtS trebuie să completeze automat secțiunea validity date_end cu ziua ulterioară publicării (cu excepția cazului în care procesele naționale asigură obținerea unei date de sfârșit a valabilității pentru mesaje de îndată ce informațiile incluse în mesaj nu mai sunt de actualitate).
În Ghidul privind codificarea NtS pentru editori se descriu condițiile în care un editor NtS creează un nou ICEM sau actualizează un ICEM existent. Se aplică următoarele procese:
4.1. Un ICEM nou
1) Aplicațiile NtS pot asigura pentru editorii NtS
(a) utilizarea notificărilor existente ca proiect la crearea unui nou ICEM (de exemplu, în cazul în care starea gheții este similară cu cea din notificarea existentă) și/sau
(b) utilizarea modelelor de notificări pentru anumite situații.
2) Conținutul (de exemplu, timpul de măsurare sau condițiile respective ale gheții) trebuie să fie introdus de către editor în conformitate cu capitolul 6 din Ghidul privind codificarea NtS pentru editori. Data și ora măsurătorii ar putea fi fixată, de asemenea, de către aplicație conform definițiilor naționale.
3) Atunci când un editor/factor de publicare NtS declanșează acțiunea de publicare,
(a) se verifică dacă întregul conținut obligatoriu este prezentat în conformitate cu NtS XSD [în caz contrar, se revine la punctul (2)],
(b) nts_number este generat de aplicația NtS,
(i) „organisation” este completată cu numele sau codul organizației responsabile în funcție de rolul utilizatorului care publică,
(ii) „year” este completată cu anul curent,
(iii) se atribuie următorul „number” (număr) disponibil,
(iv) se atribuie „serial number” (numărul de serie) 0.
(c) „date_issue” este completată automat cu data/ora efectivă a acțiunii de publicare,
(d) „validity_period” – „date_start” se completează automat cu data efectivă a publicării.
(e) „validity_period” – „date_end” se completează automat cu următoarea zi de la publicare (cu excepția cazului în care se asigură prin procesele naționale că mesajelor li se va atribui o dată de sfârșit a valabilității de îndată ce informațiile incluse în mesaj nu mai sunt de actualitate).
4.2. Actualizarea unui ICEM existent
1) Mesajul respectiv publicat trebuie să fie selectat pentru a fi actualizat în instrumentul de editare ICEM. Trebuie să se copieze sau să se modifice mesajul ICEM original în baza de date (în funcție de procesele naționale). Mesajele ICEM expirate (care au trecut de validity_date_end) nu mai pot fi actualizate, iar în acest caz, editorii NtS trebuie să creeze un nou ICEM.
2) Conținutul (de exemplu, timpul de măsurare sau respectivele condițiile respective ale gheții) trebuie să fie modificat de către editor în conformitate cu capitolul 6 din Ghidul privind codificarea NtS pentru editori. De asemenea, aplicația poate modifica data și ora măsurătorii conform definițiilor naționale.
3) Atunci când un editor/responsabil cu publicarea NtS declanșează acțiunea de publicare,
(a) se verifică dacă întregul conținut obligatoriu este prezentat în conformitate cu NtS XSD [în caz contrar, reveniți la punctul (2)],
(b) nts_number este generat de aplicația NtS,
(i) „organisation” rămâne neschimbat,
(ii) „year” rămâne neschimbat,
(iii) „number” rămâne neschimbat,
(iv) „serial number” crește (cu 1)
(c) „date_issue” este completată automat cu data/ora efectivă a acțiunii de publicare
(d) „validity_period” – „date_start” este completată automat cu data efectivă a publicării
(e) „validity_period” – „date_end” se completează automat cu următoarea zi de la publicare (cu excepția cazului în care se asigură prin procesele naționale că mesajelor li se va atribui o dată de sfârșit a valabilității de îndată ce informațiile incluse în mesaj nu mai sunt de actualitate).
5. Considerații de bază privind WERM
De regulă, WERM sunt create și publicate în mod automat pe baza informațiilor primite de la echipamentul senzor sau pe baza informațiilor primite de la infrastructură. date_start din validity_period trebuie să fie completată cu data actuală (date_issue), iar date_end din validity_period trebuie să fie completată cu următoarea zi după date_issue.
Secțiunea privind șenalul navigabil din WERM este indicată ca o porțiune între două puncte de pe șenalul navigabil, mai exact ca zona de aplicabilitate a stației meteo (a mirei).
Data și ora măsurătorii/prognozei trebuie să fie indicate chiar dacă nu este obligatoriu în mesajele WERM.
În cazul prognozelor, datele din secțiunea „measure_date” constituie data/ora la care este valabilă prognoza.
5.1. Completarea secțiunii nts_number în WERM
În NtS XSD 4.0, numărul NtS este opțional în mesajele WERM. Dacă este indicat, fiecare număr trebuie să fie unic (organizație/an/număr/serie) pe tip de mesaj și este de resortul organizației care transmite WERM să atribuie numere unice (nu este obligatorie folosirea numerelor consecutive).
5.2. Completarea secțiunii „weather_category_code” din WERM
Viteza vântului din secțiunea „weather_category_code” (valorile de la 0 la 12) este indicată în concordanță cu scara Beaufort publicată de Organizația Meteorologică Internațională (World Meteorological Organization) în manualul său privind serviciile meteorologice marine „WMO-No. 558” (Manual on Marine Meteorological Services).
Vizibilitatea din secțiunea „weather_category_code” (valorile de la 13 la 22) este indicată astfel cum este definită în următorul tabel:
Valoare, sens | Vizibilitate | Informații suplimentare
13, ceață foarte densă | sub 50 de metri |
14, ceață densă | sub 100 de metri |
15, ceață moderată | sub 200 de metri |
16, ceață | sub 1 000 de metri | Ceața este formată din picături de apă.
17, ceață slabă | între 1 și 4 km | Ceața slabă este formată din picături de apă. Ceața slabă este un termen folosit pentru „ceața uscată”, un fenomen care, de regulă, se produce înainte de răsăritul soarelui.
18, negură | între 1 și 4 km | Negura este formată din particule uscate.
19, negură ușoară | între 4 și 10 km |
20, senin | între 10 și 20 km |
21, foarte senin | nu există o limitare a vizibilității |
22, ceață absentă | | situația „ceață absentă” este utilizată pentru a indica faptul că nu există ceață, în funcție de cerințele naționale/locale.
6. Procesele FTM
În Ghidul privind codificarea NtS pentru editori se descriu împrejurările în care un editor NtS creează un nou FTM sau efectuează actualizări ale unui FTM existent. Se aplică următoarele procese:
6.1. Un FTM nou
1) Aplicațiile NtS pot asigura pentru editorii NtS
(a) utilizarea avizelor existente ca baze de proiecte pentru elaborarea unui FTM nou și/sau
(b) utilizarea modelelor de notificări pentru anumite situații.
2) Conținutul (de exemplu, timpul de valabilitate, restricții) trebuie să fie introdus de către editor în conformitate cu capitolele 3 și 4 din Ghidul privind codificarea NtS pentru editori.
3) Atunci când un editor/responsabil cu publicarea NtS declanșează acțiunea de publicare,
(a) se verifică dacă întregul conținut obligatoriu este prezentat în conformitate cu NtS XSD [în caz contrar, se revine la punctul (2)],
(b) nts_number este generat de aplicația NtS,
(i) secțiunea „organisation” (organizație) este completată cu numele sau codul organizației responsabile în funcție de rolul utilizatorului care publică,
(ii) „year” este completată cu anul curent,
(iii) se atribuie următorul „number” (număr) disponibil în cazul în care a fost introdus un număr specific de către editorul NtS sau un proces din aplicație preia această funcție în etapa nr. 2 [dat fiind faptul că organizația/anul/numărul/seria este unic(ă), astfel cum este explicat la capitolul 15.1]
(iv) se atribuie „serial number” (număr de serie) 0
(c) Secțiunea „date_issue” este completată automat cu data/ora efectivă a acțiunii de publicare
6.2. Actualizarea/retragerea unui FTM existent
1) Mesajul respectiv publicat trebuie să fie selectat pentru a fi actualizat în instrumentul de editare FTM, iar FTM original trebuie să fie copiat sau modificat în baza de date (în funcție de procesele naționale).
(a) Mesajele FTM expirate (care au depășit validity_date_end) nu mai pot fi actualizate, iar în acest caz, editorul NtS trebuie să creeze un nou FTM.
(b) Subiectul notificării „Mesaj anulat” este utilizat doar dacă
(i) data actuală precedă data indicată în secțiunea validity_date_start. În cazul în care doar conținutul din câmpul „informații suplimentare în limba de origine” poate fi modificat, conținutul codificat al mesajului (etapa a doua) trebuie să rămână neschimbat.
(ii) perioada de valabilitate a început deja, iar noua dată de sfârșit pentru toate restricțiile este în trecut. Data de sfârșit a restricției trebuie să fie reglată la data corectă.
(c) Dacă o notificare este retrasă, data de sfârșit a perioadei de valabilitate trebuie să fie stabilită ca fiind data retragerii.
2) Conținutul (de exemplu, timpul de valabilitate, restricții) trebuie să fie modificat de către editor în conformitate cu capitolele 3 și 4 din Ghidul privind codificarea NtS pentru editori.
3) Atunci când un editor/responsabil cu publicarea NtS declanșează acțiunea de publicare,
(a) se verifică dacă întregul conținut obligatoriu este prezentat în conformitate cu NtS XSD [în caz contrar, se revine la punctul (2)],
(b) nts_number este generat de aplicația NtS,
(i) secțiunea „organisation” rămâne neschimbată,
(ii) secțiunea „year” rămâne neschimbată,
(iii) secțiunea „number” rămâne neschimbată,
(iv) „serial number” crește (cu 1)
(c) Secțiunea „date_issue” este completată automat cu data/ora efectivă a acțiunii de publicare
(d) FTM având codul subiectului „Notice withdrawn” (Notificare retrasă) nu (mai) este luat în considerare la planificarea voiajelor.
6.3. FTM privind căile navigabile și/sau obiectul
Un FTM privind o cale navigabilă cuprinde informații despre una sau mai multe porțiuni ale căii navigabile respective. O porțiune a căii navigabile este definită în secțiunea „fairway_section” prin codurile sale de localizare de început și de sfârșit ISRS.
Un FTM privind un obiect cuprinde informații despre una sau mai multe obiecte de pe calea navigabilă. Un obiect este definit în secțiunea „object” prin codul său de localizare ISRS.
Un FTM trebuie să se refere
— la una sau mai multe secțiuni ale căii navigabile sau
— la unul sau mai multe obiecte de pe una sau mai multe secțiuni ale căii navigabile
6.4. Ordonarea automată a codurilor de restricție
Diferite restricții au un impact diferit asupra navigației. Pentru a permite afișarea celei mai drastice restricții, de exemplu, pe o listă sintetică de mesaje FTM, se are în vedere următoarea ordine, începând cu cea mai drastică restricție având nivelul 1:
Nivel | Valoare | Sens (RO)
1 | OBSTRU | blocaj
2 | PAROBS | ob parțial
3 | NOSERV | întreruperea serviciului
4 | SERVIC | serviciu modificat
5 | VESDRA | pescajul navei
6 | VESBRE | lățimea navei
7 | CONBRE | lățimea convoiului
8 | VESLEN | lungimea navei
9 | CONLEN | lungimea convoiului
10 | CLEHEI | gabaritul de înălțime
11 | VESHEI | înălțimea deasupra liniei de plutire
12 | AVALEN | lungimea disponibilă
13 | CLEWID | gabaritul de lățime
14 | AVADEP | adâncimea disponibilă
15 | LEADEP | adâncimea minimă
16 | DELAY | întârziere
17 | ALTER | trafic cu sensuri alternative
18 | TURNIN | întoarcerea interzisă
19 | PASSIN | traversarea interzisă
20 | OVRTAK | depășirea interzisă
21 | NOBERT | andocarea interzisă
22 | NOMOOR | acostarea interzisă
23 | ANCHOR | ancorarea interzisă
24 | VITEZĂ | limită de viteză
25 | WAVWAS | formarea valurilor interzisă
26 | NOSHORE | nu este permis accesul la mal
27 | MINPWR | putere minimă
28 | CAUTIO | vigilență mărită
29 | NOLIM | fără restricții
6.5. Gestionarea perioadelor de restricții
— Restricțiile având aceleași perioade de restricții ar trebui să fie grupate/incluse pe aceeași listă/combinate pentru ca afișajul să fie ușor de citit.
— Instrumentele de editare a NtS trebuie să ofere editorilor o funcție pentru a evita reintroducerea perioadelor de restricții.
— Toate restricțiile trebuie să includă o perioadă de restricții cu un cod de interval pentru a permite efectuarea corectă a calculelor în aplicațiile de planificare a voiajelor. Pentru a facilita activitatea editorilor NtS, pot fi aplicate următoarele funcții:
— Instrumentul de editare NtS poate asigura o funcție de copiere a restricțiilor deja introduse pentru a evita retastarea perioadei de restricții de către editorul NtS.
— Instrumentele de editare a NtS pot să ofere o funcție destinată selectării a mai multor coduri de restricții pentru o anumită perioadă de restricție și, în mod automat, pot să creeze secțiunile restricționate necesare ca urmare a informațiilor introduse de editorul NtS.
— „De luni până vineri cu excepția sărbătorile legale”: Valoarea „holidays” (sărbători) este foarte dificilă pentru aplicațiile de planificare a voiajelor. Pentru o calculare corectă, este necesară o listă de sărbători pentru fiecare țară. Dacă nu există o astfel de listă disponibilă, restricțiile respective vor fi totuși asociate cu sărbătorile legale.
— „cu excepția”: secțiunea nu trebuie să fie utilizată; Intervalele întrerupte trebuie să fie indicate ca perioade de restricții separate în cadrul aceleiași restricții; prin urmare, acest cod nu este afișat/disponibil pentru editorii de notificări.
— Logica și afișarea informațiilor aplicabile în cazul codului de interval „continuous” (permanent):
<date_start>2015-04-01+01</date_start>
<date_end>2015-06-30+02</date_end>
<time_start>06:00:00</time_start>
<time_end>10:00:00</time_end>
<interval_code>CON</interval_code>
Dacă interval_code este permanent, start_time aparține secțiunii start_date, iar end_time aparține secțiunii end_date, de exemplu, de la 1 aprilie, orele 6.00 la 30 iunie, orele 10.00
— Logica și afișarea informațiilor aplicabile în cazul oricărui alt cod de interval, în afară de „continuous” (permanent):
<date_start>2015-04-01+01</date_start>
<date_end>2015-06-30+02</date_end>
<time_start>06:00:00</time_start>
<time_end>10:00:00</time_end>
<interval_code>WRK</interval_code>
Dacă secțiunea interval_code are o altă valoare, secțiunea start_time și end_time aparțin acestei secțiuni interval_code, de exemplu, de la 1 aprilie la 30 iunie, de luni până vineri, în intervalul orar 6.00-10.00
— Ora de sfârșit a restricției trebuie să fie indicată întotdeauna în ultima versiune a unui mesaj.
7. Norme generale privind punerea în aplicare
Sunt avute în vedere următoarele:
— Tabelul „GUI_labels” din tabelele de referință NtS este avut în vedere la dezvoltarea aplicațiilor NtS (măști de căutare, formular de abonare la serviciul de e-mail, afișarea mesajelor).
— Valoarea din secțiunea date_end nu poate fi înaintea valorii din secțiunea date_start.
— Codurile care au fost dezactivate (care nu mai sunt utilizate) prin intermediul solicitărilor de modificare NtS (a se vedea observațiile din NtS XSD) nu sunt afișate editorilor NtS la crearea de mesaje noi. Codurile sunt totuși incluse în enumerările NtS XSD pentru retrocompatibilitate.
7.1. Completarea secțiunii „number_section”
Fiecare număr (organizație/an/număr/serie) trebuie să fie unic pe tip de mesaj. Aceasta înseamnă că mesajele de diferite tipuri pot avea același număr NtS.
Pentru utilizatori, numerele mesajelor sunt relevante doar pentru FTM și ICEM, iar pentru toate celelalte tipuri de mesaje, afișarea numărului mesajului poate fi omisă în funcție de cerințele naționale.
Pentru utilizatori, numărul mesajului poate fi afișat în următorul format „Tip mesaj/țară/organizație/an/număr/serie” (acesta poate fi scurtat în funcție de filtrele aplicate dacă nu se pierd informații).
7.2. Completarea elementelor „expeditorul mesajului”, „autorul informațiilor”, „organizația” și „sursa notificării (autoritatea)”
Elementul „expeditorul mesajului” din secțiunea de identificare este completat cu numele sistemului național care transmite mesajul (de exemplu, ELWIS, DoRIS, SLOVRIS, FLARIS).
Elementul „autorul informațiilor” este organizația care introduce mesajele în sistemele naționale.
Elementul „sursa notificării (autoritatea)” este autoritatea pentru care se publică FTM-urile.
Elementul „organizația” din secțiunea nts_number este numele organizației care atribuie nts_number (furnizorul NtS).
7.3. Omiterea elementelor
Elementele care conțin doar valori standard sau implicite sunt omise dacă sunt condiționate, deoarece conduc la supraîncărcarea mesajului, fără o valoare adăugată.
Sunt vizate următoarele elemente:
— Grupul-țintă: target_group_code ALL cu direction_code ALL (dacă nu există alte grupuri-țintă specifice în cadrul mesajului),
— position_code: AL,
— reason_code: OTHER.
7.4. Completarea automată a secțiunii date_issue
FTM și ICEM
În cazul FTM și ICEM, valoarea elementului date_issue reprezintă data și ora efectivă ale publicării. În cazul mesajelor actualizate, date_issue reprezintă data și ora publicării actualizării.
WRM și WERM
În cazul WRM și WERM, valoarea elementului date_issue reprezintă data și ora solicitării de prelucrare, deoarece pot exista mai multe măsurători cu diferite marcaje temporale de emitere în cadrul unui mesaj W(E)RM.
7.5. Gestionarea informațiilor privind fusul orar în mesajele NtS
Data și ora sunt indicate întotdeauna în ora locală, incluzând informații privind fusul orar în mesajele NtS XML.
Singurele excepții de la această dispoziție sunt valorile „time_start” și „time_end” din secțiunea „limitation_period”. Aceasta se justifică prin faptul că în secțiunea aferentă limitării poate fi aplicat un interval. Dacă data de început și cea de sfârșit au regimuri de timp diferite (de exemplu, CEST și CET), acest fapt ar determina modificarea informațiilor privind fusul orar în acest interval. Această modificare nu poate fi exprimată printr-o singură perioadă de limitare. În loc de a crea diferite perioade de limitare pentru fiecare modificare de timp, se utilizează doar o singură perioadă de limitare fără informații despre fusul orar pentru a reduce supraîncărcarea mesajului la prelucrare și transmitere.
7.6. Gestionarea secundelor în mesajele NtS
Ca regulă generală, secundele trebuie să fie indicate în câmpurile aferente (datei)/orei, însă nu sunt afișate utilizatorilor NtS. Minutele sunt suficiente pentru granularitatea NtS.
7.7. Formatul zecimalelor în mesajele NtS
Zecimalele din câmpurile numerice sunt indicate cu un . (punct). Nu se folosesc separatori de mii.
Numărul zecimalelor utilizate pentru valori trebuie limitat la o cantitate rezonabilă care să asigure o afișare ușor de utilizat.
7.8. Unitățile utilizate în mesajele NtS
Doar utilizarea cm, m3/s, h, km/h și kW, m/s (vânt), mm/h (precipitații) și a gradelor Celsius ca unități este permisă în cadrul mesajelor NtS; aplicațiile pot converti unitățile pentru a facilita citirea acestora.
În cazul în care unitățile de intrare diferă de unitățile standardizate, valorile introduse trebuie să fie convertite de către aplicație în mod corespunzător.
7.9. Reguli pentru elementele „name”, „position_code” și „type_code”
Elementul „name” (nume) este completat în prealabil în mod automat din datele de referință din indexul RIS din secțiunea „national object name” (numele național al obiectului) (editorii NtS ar putea modifica numele completat în prealabil dacă aceasta este o cerință națională). Convențiile de numire pentru numele obiectelor sunt incluse în Ghidul privind codificarea indexului RIS, versiunea 2.0 sau versiunile superioare. Exemple de nume corecte ale obiectelor sunt prezentate, de asemenea, în Ghidul privind codificarea NtS pentru editori.
Codul tipului este adăugat la obiect prin intermediul aplicației NtS, în fața numelui obiectului.
Poziția obiectelor este codificată prin codul de poziție și adăugată la obiect prin intermediul aplicației NtS din indexul RIS. Editorii pot modifica tipul și codurile de poziții completate în prealabil. Un cod de poziție a obiectului nu este indicat pentru geo_objects în secțiunea fairway_section.
Un nume complet al obiectului este compus din codul său de poziție, codul tipului și nume.
Pentru a facilita activitatea editorilor NtS, se poate aplica următoarea structură în instrumentele de editare a NtS, oferind sprijin editorilor să găsească/selecteze obiectele adecvate pe baza secțiunii function_code din indexul RIS sau a secțiunii NtS type_code:
Tabelul 1
Corespondențe „RIS Index function_code” – „NtS type_code”
Function Code | Function Code Meaning | Type Code | Type Code Meaning
— | — | |
BUAARE | E.1.1 | Built-Up Areas | | to be selected by editor
BUISGL | E.1.2 | Building of Navigational Significance | | to be selected by editor
brgare | G.1.1 | - G.1.6 Bridge Area [C_AGGR()] | BRI | bridge
bridge_5 | G.1.1 | Bascule Bridge | BRO | bridge opening
bridge_1 | G.1.2 | Bridges with Bridge Arches | BRO | bridge opening
bridge_1 | G.1.3 | Fixed Bridge | BRO | bridge opening
bridge_4 | G.1.4 | Lift Bridge | BRO | bridge opening
bridge_12 | G.1.5 | Suspension Bridge | BRO | bridge opening
bridge_3 | G.1.6 | Swing Bridge | BRO | bridge opening
cblohd | G.1.8 | Overhead Cable | CAB | cable overhead
pipohd | G.1.9 | Overhead Pipe | PPO | pipeline overhead
bridge_7 | G.1.12 | Drawbridge | BRO | bridge opening
bunsta | G.3.2 | Bunker / Fuelling Station | BUS | Bunker / Fuelling Station
cranes | G.3.4 | Crane | | to be selected by editor
hrbare | G.3.9 | Harbour Area | HAR | harbour
hrbbsn | G.3.10 | Harbour Basin | HAR | harbour
ponton | G.3.11 | Landing Stage, Pontoon | | to be selected by editor
morfac | G.3.12 | Mooring Facility | MOO | mooring facility
hulkes | G.3.14 | Permanently Moored Vessel or Facility | | to be selected by editor
prtare | G.3.15 | Port Area | HAR | harbour
refdmp | G.3.17 | Refuse Dump | REF | refuse dump
termnl | G.3.19 | Terminal | TER | terminal
trm01 | G.3.19 | RORO-terminal | TER | terminal
trm03 | G.3.19 | Ferry-terminal | TER | terminal
trm07 | G.3.19 | Tanker-Terminal | TER | terminal
trm08 | G.3.19 | Passenger Terminal | TER | terminal
trm10 | G.3.19 | Container Terminal | TER | terminal
trm11 | G.3.19 | Bulk Terminal | TER | terminal
vehtrf | G.3.20 | Vehicle Transfer Location | BER | berth
lokbsn | G.4.3 | Lock Basin | LKB | lock basin
lkbspt | G.4.4 | Lock Basin Part | LKB | lock basin
lokare | G.4.3 | / G.4.4 Lock Area [C_AGGR()] | LCK | lock
excnst | G.4.8 | Exceptional Navigational Structure | SLI | ship lift
| | TUN | tunnel
| | CBR | canal bridge
gatcon | G.4.9 | Opening Barrage | BAR | weir
| | FLO | flood gate
wtwgag | I.3.4 | Waterway Gauge | GAU | tide gauge
FERYRT_2 | L.2.1 | Cable Ferry | FER | ferry
FERYRT_1 | L.2.2. | Free Moving Ferry | FER | ferry
feryrt_4 | L.2.3. | Swinging Wire Ferry | FER | ferry
dismar | L.3.2 | Distance Mark along Waterway Axis | RIV | river
achare | M.1.1 | Anchorage Area | ANC | anchoring area
achbrt | M.1.2 | Anchorage Berth | BER | berth
berths_3 | M.1.3 | Berth / Fleeting Areas | BER | berth
berths_1 | M.1.4 | Transhipment Berth | BER | berth
trnbsn | M.4.5 | Turning Basin | TUR | turning basin
| | CAN | canal
| | FWY | fairway
rdocal | Q.2.1 | Radio Calling-In Point (notification point) | REP | reporting point
chkpnt | R.1.1 | Check Point | BCO | border control
sistat_8 | R.2.1 | Traffic Sistat – Bridge Passage | SIG | signal station
sistat_6 | R.2.2 | Traffic Sistat – Lock | SIG | signal station
sistat_10 | R.2.3 | Traffic Sistat – Oncoming Traffic Indicator | SIG | signal station
sistat_2 | R.2.4 | Traffic Sitat – Port Entry and Departure | SIG | signal station
pas | Passage Points | | to be selected by editor
riscen | RIS centre | VTC | vessel traffic centre
specon | Special Construction | | to be selected by editor
trafp | Traffic Points (first reporting points) | REP | reporting point
junction | Waterway node / end of waterway / Junction | | to be selected by editor
waypt | Waypoint | | to be selected by editor
Legend:
green | Direct match (1:1 relation)
yellow | matching example, other TypeCodes possible (1:n relation)
blue | no direct match / to be selected by editor
7.10. Reguli pentru elementul „fairway_name”
Pentru a evita logica/necesitatea aplicării datelor de referință adecvate în sistemul receptor (software care afișează notificarea pentru utilizator), elementul opțional „fairway_name” este inclus întotdeauna în „geo_object” și este completat automat de către aplicația NtS cu „Waterway name” din indexul RIS. Editorii NtS nu trebuie să modifice conținutul elementului fairway_name.
7.11. Clarificări pentru traducerile din foaia de calcul „reference_code”
Pentru valorile aferente secțiunii reference_code din tabelele de referință NtS se utilizează următoarea definiție:
— NAP: În Țările de Jos, se utilizează și se înțelege abrevierea NAP, NAP nu se traduce
— KP: „nivelul de referință local” se traduce în forma prezentată în limba de origine
— FZP: se utilizează doar abrevierea „FZP” (în prezent, aceasta este oricum utilizată rar)
— ADR: „marea Adriatică” se traduce în forma prezentată în limba de origine
— TAW/DNG: „Tweede algemene waterpassing” (limba olandeză) – „Deuxième Nivellement Général” (limba franceză) reprezintă înălțimea de referință utilizată în Belgia pentru exprimarea măsurătorilor pentru înălțime. 0 reprezintă nivelul mediu al apei mării la nivelul minim în Oostende
— Olandeză: TAW
— Franceză: DNG
— Toate celelalte limbi: TAW/DNG
— LDC: „nivelul minim al apei – Comisia Dunării” se traduce astfel cum este furnizat în limba de origine
— HDC: „nivelul maxim al apei – Comisia Dunării” se traduce astfel cum este furnizat în limba de origine
— ETRS: „Sistemul de Referință Terestru European 1989” – abrevierea „ETRS89” este utilizată în toate limbile
7.12. Recomandare pentru elementul „coordinate”
Deși elementul „coordinate” din secțiunea geo_object este condiționat, coordonatele geografice sunt date în WGS84 în formatul [z]z mm.mmm[m] N (latitudine) și [z][z]z mm.mmm[m] E (longitudine). Această alegere este preferată pentru a stabili referința geografică a mesajelor NtS.
7.13. Abordarea grupurilor-țintă
Secțiunea aferentă grupurilor-țintă cuprinde codul grupului-țintă și codul direcției. Dacă ambele au valoarea ALL, întreaga secțiune se omite în cazul în care nu există alte grupuri-țintă specifice în cadrul mesajului. Dacă este indicat doar unul dintre aceste două coduri, celălalt trebuie să fie completat cu valoarea implicită ALL, deoarece ambele elemente sunt obligatorii.
Informații suplimentare cu privire la grupurile-țintă se găsesc în Ghidul privind codificarea NtS pentru editori.
7.14. Afișarea mesajelor valabile la o oră dată
Secțiunea validity_period se utilizează de către aplicații pentru selectarea mesajelor, care vor fi afișate utilizatorilor pentru un timp solicitat.
Dacă subject_code este INFSER (mesaj informativ), perioada de valabilitate este utilizată pentru a indica ora de afișare a mesajului informativ pentru utilizatori, nu pentru perioada de valabilitate a informațiilor furnizate (de exemplu, o lună).
7.15. Funcții opționale pentru creșterea gradului de accesibilitate a instrumentelor de editare a NtS pentru utilizatori
În funcție de cerințele naționale, următoarele funcții pot fi oferite editorilor NtS:
— Aplicațiile NtS pot oferi editorilor NtS posibilitatea de a salva mesaje NtS în proiect (nu trebuie să fie menționate toate informațiile obligatorii pentru a salva mesaje în proiect)
— Diferite roluri de utilizator pot corespunde diferiților editori (de exemplu, editori care au permisiunea să introducă/modifice notificări, responsabili cu publicarea care au permisiunea să publice notificări, în plus față de editare)
8. Structura mesajului NtS XML
Structura mesajului NtS XML, precum și conținutul și scopul elementelor datelor, sunt definite și explicate mai detaliat în apendicele C: Definirea schemei NtS XML (XSD).
9. Serviciul web NtS
9.1. Obiectiv
Grupul de experți NtS a identificat tehnologia pentru serviciile web ca fiind un mijloc adecvat de transmitere a notificărilor către navigatori.
Acest capitol prezintă specificația serviciului web pentru transmiterea notificărilor către navigatori, pe scurt NtS Web Service. S-a pus accent în special pe utilizarea standardelor internaționale consacrate.
Unul dintre obiectivele proiectului conceptual a fost de a asigura un echilibru adecvat între flexibilitatea și soliditatea serviciului web rezultat. Parametrii de filtrare indicați în solicitări sunt în esență criteriile prevăzute în standardul NtS (secțiunea căii navigabile, incluzând în mod opțional km de fluviu, durata de valabilitate și data publicării notificării). Această modalitate pare să fie suficient de relevantă având în vedere cazurile de utilizare a serviciului web și, în același timp, limitările privind complexitatea executării.
Rezultatul de bază este reprezentat de un contract pentru serviciul web, în care sunt specificate solicitările și răspunsurile. Utilizatorii serviciului web se pot baza pe acest contract, iar furnizorii trebuie să îl respecte. Acest contract este elaborat cu respectarea standardului internațional WSDL.
Fiecare stat membru participant implementează unul sau mai multe servicii web pentru diferite tipuri de mesaje din NtS (FTM, WRM, ICEM, WERM) și le furnizează pe internet („Serviciul de mesaje NtS”),
Detaliile tehnice ale implementării NtS WS, de exemplu, alegerea seturilor de date, a aplicațiilor și a platformelor adecvate, nu intră în domeniul de aplicare al acestei specificații și constituie responsabilitatea fiecărui stat membru participant.
Pentru a stabili o comunicare securizată, trebuie să fie avute în vedere diferite aspecte privind securitatea și obiectivele de protecție. În funcție de împrejurări, nu toate aceste aspecte trebuie să fie avute în vedere. Prioritatea diferitelor aspecte privind securitatea și gradul de realizare a acestora poate să difere. De asemenea, fezabilitatea unei anumite măsuri poate fi limitată de capacitățile de implementare tehnică. În contextul NtS, toate informațiile sunt publice. Astfel, nu este nevoie să se asigure datele NtS în sine sub aspectul protecției datelor. Prin urmare, fiecare furnizor trebuie să stabilească individual în ce măsură va implementa acest aspect în cadrul serviciului său.
9.2. Principii de bază și restricții
9.2.1. Standarde web
NtS Web Service trebuie să respecte WS-I Basic Profile 1.1. Acest profil „oferă orientări privind interoperabilitatea pentru un set esențial de specificații pentru servicii web publice, precum SOAP, WSDL și UDDI” (1). Cele mai relevante standarde din acesta sunt
— Definirea schemei XML (XSD),
— Protocol simplu de acces la obiecte (SOAP),
— Limbaj pentru descrierea serviciilor web (WSDL) și
— Descriere, descoperire și integrare universale (UDDI).
Mesajul de răspuns al NtS WS este un mesaj NtS definit în Definirea schemei XML (XSD) din apendicele C la prezentul Regulament al Comisiei.
SOAP | este un protocol de executare pentru transmiterea datelor între sisteme informatice și este standardizat de World Wide Web Consortiums (W3C). Elementele specifice pentru NtS Web Service sunt definite în concordanță cu specificațiile WSDL aferente din apendicele D la prezentul regulament al Comisiei. Schema standardului NtS (XSD) este inclusă împreună cu o declarație de import.
UDDI | (Descriere, descoperire și integrare universale) este înregistrat aici ca fiind un registru central, posibil internațional, pentru servicii web, în care ar putea fi înregistrat NtS Web Service. În acest registru, potențiali consumatori ai serviciului web ar putea să caute și să găsească serviciul în cauză. Însă, deoarece furnizorii potențiali ai NtS Web Service sunt limitați de către statele membre participante și specificația WSDL este o parte integrantă din standard, nu este stringentă nevoia unei înregistrări independente a NtS Web Service.
9.2.2. Modelul de interacțiune și metoda de codificare pentru NtS WS
Pentru NtS Web Service se utilizează metoda de codificare „Document-literal wrapped”, deoarece ea permite validarea față de o schemă XML, iar numele operațiunilor definite în specificația WSDL sunt utilizate în mod direct ca nume de etichetă XML în mesajele SOAP.
9.3. Specificații și recomandări generale
9.3.1. Specificații: Informații privind versiunea
Partea cu informații privind versiunea a serviciului web NtS cuprinde două secțiuni:
— versiunea serviciului web ca atare
— versiunea schemei NtS utilizată de serviciul web
Secțiunea serviciului web ca atare cuprinde două părți:
— versiunea majoră a serviciului web
— versiunea minoră a serviciului web
Versiunea majoră este dată ca număr întreg pozitiv care denotă versiunea majoră a serviciului web.
Versiunea minoră este dată ca număr întreg non-negativ care denotă versiunea minoră a serviciului web în cadrul versiunii majore.
Secțiunea schemei NtS cuprinde versiunea schemei NtS astfel cum este definită de grupul de experți NtS.
Prin urmare, versiunea serviciului web NtS indicată în prezentul document este 2.0.4.0, unde 2.0 este versiunea serviciului web ca atare, iar 4.0 este versiunea schemei NtS utilizate.
Nu sunt necesare informații explicite privind versiunea în solicitările sau răspunsurile NtS Web Service. Există doar câteva versiuni ale serviciilor prevăzute a fi online în același timp. Versiunile diferite sunt furnizate cu URL-uri diferite. Prin urmare, fiecare eveniment de executare a serviciului web NtS corespunde unei versiuni specifice a serviciului web NtS.
9.3.2. Specificații: Structura spațiilor de nume
Spațiile de nume din serviciul web NtS sunt bazate pe domeniul web al grupului de experți RIS, http://www.ris.eu/.
Spațiile de nume cuprind o particulă care indică serviciul aferent și informații privind versiunea. Prin urmare, serviciul indicat în prezentul document utilizează următorul spațiu de nume:
Serviciul de mesaje NtS: http://www.ris.eu/nts.ms/2.0.4.0
9.3.3. Recomandare: Utilizarea spațiilor de nume
Pentru o mai mare transparență a documentelor XML, se recomandă să se definească spațiilor de nume în cel mai îndepărtat element adecvat din scheme, precum și în documentele de instanță și să nu se utilizeze definiții locale ale spațiilor de nume în elemente imbricate.
9.3.4. Recomandare: Utilizarea prefixelor în spațiile de nume
Solicitările și răspunsurile din serviciul web NtS utilizează elementele XML în formă calificată, mai exact, cu un prefix explicit al spațiului de nume, iar atributele XML în formă necalificată, mai exact, fără un prefix al spațiului de nume.
Se recomandă să se utilizeze prefixe intuitive pentru spațiile de nume, precum „nts”, pentru a facilita citirea de către persoane.
9.3.5. Specificații: Utilizarea codurilor de localizare ISRS
Codul de localizare ISRS este explicat în capitolul 2 din Ghidul privind codificarea NtS pentru dezvoltatorii de aplicații, precum și în Ghidul privind codificarea indexului RIS.
Prin interogarea seviciului web NtS, clientul poate face trimitere la diferite obiecte, de exemplu, secțiuni ale șenalului navigabil, indicatoare de nivel sau ecluze. Dacă se utilizează parametrii corespondenți, și anume elementele de identificare, aceștia trebuie să conțină coduri de localizare ISRS. Acești parametri sunt indicați, de regulă, în elemente de identificare, fiecare conținând una sau două date de identificare.
Atunci când se folosesc acești parametri, trebuie să fie respectate următoarele convenții generale:
— Identificatorii trebuie să fie indicați sub forma unor coduri complete de 20 de semne, mai exact, fără trunchierea zerourilor de la sfârșit.
— Dacă se utilizează două date de identificare în cadrul unui element de identificare, ambii identificatori trebuie să facă trimitere la aceeași cale navigabilă. Aceasta înseamnă că respectivele coduri includ unele cifre identice aflate în partea aferentă fairway_section din codul de localizare ISRS. Codul aferent secțiunii șenalului navigabil, împreună cu hectometrul șenalului navigabil, definește o porțiune a căii navigabile indicată sub forma unei perechi de elemente de identificare.
Pentru indicarea porțiunilor căii navigabile (perechi de elemente de identificare în cadrul secțiunii fairway_section geo_object) din mesajele NtS, trebuie să fie avute în vedere următoarele aspecte în ceea ce privește identificatorii:
— cifrele 1 și 2 (codurile de țară):
— trebuie să fie identice în cadrul perechii de date de identificare, însă
— în cadrul unei perechi de date de identificare, pot fi definite diferite coduri de țară în cazul în care țările învecinate utilizează același cod al secțiunii șenalului navigabil pentru o anumită cale navigabilă și același sistem pentru definirea hectometrilor,
— cifrele 3-5 (codul de localizare al ONU):
— nu sunt relevante, pot conține diferite informații în cadrul aceleiași perechi de date de identificare,
— cifrele 6-10 (codul secțiunii șenalului navigabil):
— trebuie să fie identice în cadrul perechii de date de identificare, însă
— [excepție]: în cazul în care se utilizează codurile ISRS belgiene în cadrul NtS WS, ar trebui să se utilizeze doar cifrele 6-8 pentru identificarea secțiunii șenalului navigabil, deoarece mesajele NtS vor fi publicate în diferite secțiuni din cadrul unui singur șenal navigabil,
— cifrele 11-15 (codul de referință al obiectului):
— nu sunt relevante, pot conține diferite informații în cadrul aceleiași perechi de date de identificare,
— cifrele 16-20 (hectometrul șenalului navigabil):
— cuprinde cinci cifre care definesc hectometrul și, prin urmare, va conține, de regulă, diferite informații în cadrul perechii de date de identificare. Exemplu: „00235” pentru șenalul navigabil la km 23,5; „00001” pentru șenalul navigabil la km 0,1,
— [excepție]: în cazul Țărilor de Jos, nu există întotdeauna o legătură directă între hectometru și kilometrul fizic al șenalului navigabil din cauza definirii începutului porțiunii șenalului în modelul de rețea și în lumea reală. În astfel de cazuri, codul de referință al obiectului pentru obiecte de tipul „dismar” începe cu Kxxxx [xxxx include kilometrul fizic, de exemplu, NLSVG00130K000300191 (km 3)]. Însă pentru alte tipuri de obiecte, nu există o relație directă cu kilometrul șenalului navigabil în codurile ISRS, de exemplu, podul Sas van Gent de pe același șenal navigabil la km 2,5 are codul ISRS NLSVG001300521600186. Pentru Kanaal Gent-Terneuzen, kilometrul fizic 0,0 începe la granița dintre Belgia și Țările de Jos, iar hectometrul șenalului 0,0 începe la începutul canalului în Gent.
În cazul în care un mesaj vizează mai multe căi navigabile sau secțiuni ale șenalului navigabil, toate secțiunile șenalului navigabil trebuie să fie definite prin punctul lor de început și de sfârșit în elemente XML aferente secțiunii „fairway_section” separate.
Pentru unele țări/regiuni, este necesar să se construiască o funcționalitate de filtrare. Spre exemplu, dacă codul de localizare ISRS (1-2) este BE, utilizați codul de localizare ISRS (6-8) ca ID pentru stabilirea referinței liniare cu hectometrul șenalului navigabil (codul de localizare ISRS 16-20). Exemple de porțiuni ale șenalului navigabil (perechi de elemente de identificare valabile în fairway_section) care includ excepțiile definite mai sus:
— Cei doi identificatori NL constituie o definire valabilă a porțiunii căii navigabile (indicând excepția NL față de kilometrul șenalului navigabil): NLSVG00130K000300191 (km 3,0 la Sas van Gent pe Kanaal Gent-Terneuzen) – NLWDP00130K000400200 (km 4,0 la Westdorpe pe Kanaal Gent-Terneuzen),
— Cei doi identificatori BE constituie o definire valabilă a porțiunii căii navigabile (indicând excepția BE față de codul secțiunii șenalului navigabil („020” Albertkanaal): BEGNK02016L010100414 (ecluza Genk situată la km 41,4 pe Albert Canal) – BEOSH02033L010500772 (ecluza Ham situată la km 77,2 pe Albert Canal).
Următoarea figură arată contraexemple de utilizare a codului de localizare ISRS pentru fiecare dintre convențiile generale (nicio excepție de la convențiile generale nu se aplică pentru porțiunile căii navigabile SK):
[figură]
Interogări nevalide ale codului de localizare ISRS
Observație generală: Nu există un serviciu pentru interogarea identificatorilor valabili care să fie compatibil cu serviciul web NtS. Identificatorii sunt indicați în Sistemul european de gestionare a datelor de referință (ERDMS).
Utilizarea corectă a identificatorului în interogări și interpretarea acestor coduri este prezentată în următoarele cinci cazuri.
Cazul 1: Nu există niciun element de identificare în solicitare
Elementul de identificare este o parte opțională a solicitării, mai exact, se permite o interogare fără elemente de identificare:
[figură]
Interogare validă fără parametrul de identificare
Dacă nu se indică niciun element de identificare, sunt redate toate mesajele (desigur în funcție de alte criterii de filtrare precum validity_period sau dates_issue).
Cazul 2: Există un element de identificare în solicitare
Fiecare element de identificare poate conține unul sau două elemente de identificare. Cazul unul element de identificare este prezentat în figura de mai jos:
[figură]
Interogare validă cu un parametru de identificare
Dacă se primește o astfel de interogare, serverul redă toate mesajele care se potrivesc cu un hectometru de început ≤ valoarea dată (240,7 în exemplu) și un hectometru de sfârșit ≥ această valoare. Figura de mai jos ilustrează această selecție de mesaje: Poziția interogată se află între valorile hectometrului de început și de sfârșit din mesajele 1, 3 și 4, care ar fi redate. Mesajele 2, 5 și 6 nu se suprapun cu poziția de interogare, astfel că acestea nu sunt redate.
Dacă codul de localizare ISRS dat denotă un singur obiect, de exemplu, un indicator de nivel sau o ecluză, serviciul web redă mesajele care includ acest obiect.
[figură]
Concordanța și neconcordanța mesajelor pentru un parametru de identificare
Cazul 3: Există două elemente de identificare în solicitare
Fiecare element de identificare poate conține unul sau două elemente de identificare. Cazul a două elemente de identificare este prezentat în figura de mai jos:
[figură]
Interogare validă cu doi parametri de identificare
Toate valorile hectometrului interogate sunt tratate ca fiind valabile, chiar dacă secțiunea șenalului navigabil aferent are puncte de început și de sfârșit diferite. Spre exemplu, dacă secțiunea șenalului navigabil începe la hectometrul 100,0 și se sfârșește la hectometrul 300,0, ar fi valabilă o solicitare care interoghează valorile hectometrului 20,0 până la 400,0. La nivel intern, desigur, se caută doar partea „reală” a secțiunii șenalului navigabil.
Astfel, se permite, de asemenea, căutarea tuturor mesajelor pe un șenal navigabil fără a se cunoaște plaja exactă a hectometrului (cineva ar trimite identificatorul cu valori ale hectometrului pe „00000” sau „99999”).
Sunt redate toate mesajele care se potrivesc și care se intersectează cu intervalul dat al hectometrului. Următoarea diagramă ilustrează această situație:
[figură]
Potrivirea și nepotrivirea mesajelor pentru doi parametri de identificare
Figura de mai sus ilustrează modul de definire a „intersectării”. Chiar dacă aria de cuprindere a mesajelor 1-4 se suprapune cu cea a intervalului hectometrului interogat (parțial sau complet), aria de cuprindere a mesajelor 5 și 6 nu, prin urmare vor fi redate mesajele 1-4, iar mesajele 5 și 6 nu vor fi redate.
Condiția tehnică pentru ca un mesaj să se intersecteze cu un interval [A, B] este: Hectometrul de început al mesajului este ≤ B, iar cel de sfârșit este ≥ A.
Combinație: Există elemente multiple de identificare în solicitare
[figură]
O interogare validă cu multiple elemente de identificare
Combinația mai multor elemente de identificare în solicitare conduce la o unire a mesajelor aferente. Toate elementele de identificare sunt tratate individual și este redat un mesaj dacă acesta se potrivește cel puțin cu unul dintre aceste elemente. Prin urmare, ar fi redate următoarele mesaje pentru exemplul dat:
— Toate mesajele pentru obiectul având codul de localizare ISRS SKXXX0000010000***** cu hectometrul de început =0 și hectometrul de sfârșit ≥ 0 (a se vedea cazul 2)
— Toate mesajele pentru obiectul având codul de ISRS SKXXX0000500000***** care se intersectează cu intervalul hectometrului [11,0, 15,0] (a se vedea cazul 3)
— Toate mesajele pentru obiectul având codul de localizare ISRS SKXXX0000200000***** cu hectometrul de început ≤ 110,5 și hectometrul de sfârșit ≥ 110,5 (a se vedea cazul 2)
— Toate mesajele pentru obiectul având codul de localizare ISRS SKXXX0000500000***** care se intersectează cu intervalul hectometrului [220,0, 300,0] (a se vedea cazul 3)
9.4. Serviciul de mesaje NtS (specificație pentru implementare)
În acest capitol este prezentată specificația privind implementarea serviciului de mesaje NtS, dedusă din considerațiile și alegerile din capitolele anterioare.
Serviciul de mesaje NtS furnizează cele patru tipuri de mesaje în NtS:
1. NtS FTM (mesaj privind șenalul navigabil și traficul pe căile navigabile)
2. NtS WRM (date despre apă)
3. NtS ICEM (date privind gheața)
4. NtS WERM (mesaj meteo)
O implementare a serviciului de mesaje NtS poate susține toate tipurile de mesaje sau doar o selecție. Se permite unui stat membru participant să ofere mai multe servicii pentru un anumit tip de mesaj, care să se completeze.
9.4.1. Solicitare
Pentru a asigura caracterul robust la nivel maxim al serviciului, menținând în același timp un nivel scăzut de complexitate, nu se utilizează un limbaj suplimentar de interogare pentru serviciul web NtS. În schimb, se aplică elementele constructive oferite de WSDL. Operațiunile specifice, împreună cu parametrii acestora, sunt menționate integral în specificația WSDL. În cazul serviciului de mesaje NtS, este definită o singură operațiune.
Criteriile de filtrare pe subiect sunt preluate din standardul NtS, dar sunt în ceea ce privește nivelul multiplicității parametrilor:
— tipul mesajului (obligatoriu; unul dintre „FTM”, „WRM”, „ICEM”, „WERM”)
— secțiuni specifice ale căii navigabile sau părți din acestea, ori obiecte specifice (opțional; descrise de coduri de localizare ISRS unici și/sau de perechi de coduri de localizare ISRS)
— durata valabilității (opțional; data de început și data de sfârșit)
— data publicării notificării (opțional; date unice și/sau intervale de date)
Serviciul redă numai mesajele care corespund criteriilor date.
Mecanismul de paginare
Pentru a controla cantitatea de date, este integrat un mecanism de paginare. Parametrul de paginare este definit cu un tip complex care conține următoarele elemente:
— abaterea: seria primului mesaj redat (număr întreg ≥ 0)
— limita: numărul maxim de mesaje (număr întreg ≥ 0)
— număr total: marcare, dacă este redat numărul total de mesaje (valoare booleană)
Parametrul de paginare complexă este opțional, însă, dacă există, trebuie indicate toate elementele din cadrul acestuia. Atunci, mecanismul de secționare funcționează în felul următor:
Numărul total de mesaje nu va depăși parametrul limită, cu excepția faptului că o valoare 0 înseamnă „nelimitat”. Răspunsul omite atâtea mesaje câte sunt definite în parametrul abatere. Pentru a asigura acest mecanism, serviciul trebuie să respecte o secvență temporară stabilă de mesaje (însă arbitrară), de exemplu, între două actualizări ale datelor din mesaj în setul de date subiacente ale serviciului web. Aceasta înseamnă că două apelări identice consecutive trebuie să redea același mesaj în aceeași ordine. Parametrul număr total stabilește dacă răspunsul transmite numărul total de mesaje care sunt în concordanță cu criteriile subiectului în cauză. De regulă, ar trebui să fie suficientă solicitarea acestor informații în primul răspuns și omiterea lor în toate răspunsurile consecutive. Aceasta ar trebui să conducă la o mai bună performanță a serviciului web.
Mecanismul de paginare oferă un mijloc de solicitare a mesajelor în mod iterativ în „pagini”. Pentru ca mecanismul de paginare să funcționeze corect, trebuie să fie furnizați în fiecare apelare aceiași parametri pentru subiectul în cauză.
9.4.2. Memoriu în răspuns
În cazul unei solicitări reușite, răspunsul serviciului web NtS conține mesaje NtS care sunt în concordanță cu parametrii de solicitare. Mesajele NtS trebuie să respecte schema NtS și pot fi validate în raport cu schema respectivă. Deoarece tipul mesajului este un parametru de solicitare obligatoriu, fiecare răspuns poate conține doar mesaje NtS ale aceluiași tip de mesaj, FTM, WRM, ICEM sau WERM.
Dacă serviciul detectează erori la prelucrarea solicitării, acesta poate reda un număr arbitrar de mesaje de eroare, folosind codurile de eroare enumerate în subcapitolul următor.
Un răspuns al unui serviciu web NtS poate conține în același timp mesaje NtS și mesaje de eroare.
Sunt redate informații opționale despre paginare dacă solicitarea a cuprins parametri de paginare. În acest caz, abaterea și numărul de mesaje conținute sunt obligatorii, iar numărul total trebuie furnizat doar dacă a fost solicitat.
Notă: Se presupune că comunicarea dintre serviciul web și utilizator este stabilită tehnic, mai exact, serviciul primește solicitarea, iar utilizatorul primește răspunsul aferent. În acest caz, nu sunt luate în considerare erorile tehnice, de exemplu, întreruperea conexiunii la internet sau inaccesibilitatea serviciului web din motive de întreținere sau avariere. În schimb, sunt luate în considerare doar situațiile de eroare care apar „dincolo de” stratul serviciului web din punctul de vedere al utilizatorilor.
Mesaje de eroare
Codurile de eroare pentru situațiile de eroare neprevăzute sunt enumerate mai jos, alături de o explicație. Doar codul de eroare este cuprins în răspuns, aceasta fiind procedura obișnuită în schema XML a NtS.
Coduri de eroare pentru serviciul de mesaje NtS
Code | Description | Explanation
e010 | message type not supported | web service does not support the requested message type
e030 | paging parameters inconsistent with messages | parameters for paging mechanism do not fit the available messages, e.g. Offset >= Total Count
e100 | syntax error in request | request violates the schema for requests; can be specified in more detail by further e1xx-Codes
e110 | incorrect message type | given message type is not known
e120 | incorrect type-specific parameters | type-specific parameters are erroneous
e130 | incorrect paging parameters | given parameters for the paging mechanism are erroneous
e200 | operation not known | the requested operation is unknown
e300 | data source unavailable | data source of the web service for the NtS data is temporarily unavailable (technical problem)
e310 | too many results for request, | server is unable to handle number of results
9.5. Generarea de servicii și clienți
Dacă abordarea „contractul primează” este respectată cu rigoare, și anume, dacă unul sau mai multe contracte cu descrieri complete ale interfețelor sunt furnizate sub formă de documente WSDL, o implementare a serviciului (serviciilor), precum și a clientului aferent, poate fi generată automat cu ajutorul instrumentelor software adecvate. Într-o situație ideală, nu trebuie să fie efectuate modificări manuale la nivelul codului sursă generat.
Însă, în majoritatea cazurilor, sunt necesare mai multe iterații pentru ca specificația WSDL să îndeplinească cerințele precise ale unui astfel de instrument. De regulă, instrumentul realizează solicitări individuale cu privire la utilizarea standardului WSDL pentru a funcționa fără probleme. În consecință, ar putea fi necesară efectuarea de modificări la nivelul specificației WSDL, deși specificația WSDL a fost inițial o specificație validă în conformitate cu standardul WSDL. Dacă specificația WSDL a serviciului web este modificată după ce se generează serviciul sau clientul, ar putea fi necesară o nouă generare, în funcție de modificările efectuate.
Glosar
Termen | Explicație
Codul de localizare ISRS | Codul de localizare „Standardul internațional privind raportarea navelor”
ID | Identificare
NtS | Notificări transmise comandanților de nave
ONU | Organizația Națiunilor Unite
RIS | Servicii de informații fluviale
SGM 84 | Sistemul geodezic global din 1984
SOAP | Protocol simplu de acces la obiecte; protocolul rețelei este utilizat, de regulă pentru servicii web
UDDI | Descriere, descoperire și integrare universale; standardul pentru servicii de înregistrare în contextul serviciilor web
URL | Localizator uniform de resurse; amplasamentul unei resurse a rețelei utilizat, de regulă, pentru adrese de internet
WS | Serviciul web; serviciu care își prezintă interfețele pe internet și este utilizat prin comunicare pe internet
WSDL | Limbaj pentru descrierea serviciilor web; standard pentru specificația serviciilor web
WS-I | Organizația pentru Interoperabilitatea Serviciilor Web; un consorțiu în domeniu având obiectivul de a susține interoperabilitatea serviciilor web
XML | Limbaj de marcare extensibil; metalimbaj pentru reprezentarea structurată și independentă, pe platformă, a datelor
XSD | Definiția schemei XML; standard pentru specificarea structurii documentelor XML
(1) Descriere citată de pe site-ul WS-I: http://www.ws-i.org
Apendicele C
No | Tag (Group headers and closers are boldly printed) | Description | Occ. | Rule
xmlns:nts="http://www.ris.eu/nts/4.0.4.0"
| <RIS_Message> | Notice to Skippers | |
1s | <identification> | Identification section | M | 1
1.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |
1.2 | <from>xs:string (64)</from> | Sender (System) of the message | M |
1.3 | <originator>xs:string (64)</originator> | Originator (initiator) of the information in this message | M |
1.4 | <country_code>nts:country_code_enum</country_code> | Country where message is valid | M |
1.5 | <language_code>nts:language_code_enum</language_code> | Original language used in the textual info. (contents) | M |
1.6 | <district>xs:string (64)</district> | District / Region within the specified country, where the message is applicable | C |
1.7 | <date_issue>xs:dateTime<date_issue> | Date and time of publication including time zone (yyyy-mm-ddThh:mm:ss+hh:mm) | M |
1e | </identification> | | |
2s | <ftm> | Fairway and traffic related section | C | 1
2.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |
2.2s | <nts_number> | NtS Number | M |
2.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M |
2.2.2 | <year>xs:gYear (1900-9999)</year> | Year of first issuing of the notice | M |
2.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (per year, starting with: 1, 0 shall not be used for published notices) | M |
2.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of notice (replacements and withdrawals), original notice: 0 | M |
2.2e | </nts_number> | | |
2.3s | <target_group> | Target group information | C |
2.3.1 | <target_group_code>nts:target_group_code_enum</target_group_code> | Target group (vessel type) for this message | M | 5
2.3.2 | <direction_code>nts:direction_code_enum</direction_code> | Upstream or downstream traffic, or both | M | 5
2.3e | </target_group> | | |
2.4 | <subject_code>nts:subject_code_enum</subject_code> | Subject code | M |
2.5s | <validity_period> | Overall period of validity | M |
2.5.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |
2.5.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |
2.5e | </validity_period> | | |
2.6 | <contents>xs:string (500)</contents> | Additional information in local language | C |
2.7 | <source>xs:string (64)</source> | Notice source (name of authority) | C |
2.8 | <reason_code>nts:reason_code_enum</reason_code> | Reason / justification of notice | C |
2.9s | <communication> | Communication channel information | C |
2.9.1 | <reporting_code>nts:reporting_code_enum</reporting_code> | Reporting regime (information or duty to report) | M | 5
2.9.2 | <communication_code>nts:communication_code_enum</communication_code> | Communication code (telephone, VHF etc.) | M | 5
2.9.3 | <number>xs:string (128)</number> | Telephone, VHF number (including callsign), e-mail address, URL or teletext | C |
2.9.4 | <label>xs:string (256)</label> | Name of the attachment or additional information | C |
2.9.5 | <remark>xs:string (1024)</remark> | Additional remarks concerning the communication | C |
2.9e | </communication> | | |
2.10s | <fairway_section> | Fairway section, also available for objects (no 2.11) | C | 2
2.10.1s | <geo_object> | Geo information of fairway | M | 5
2.10.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the fairway section (2x) Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 7
2.10.1.2 | <name>xs:string (256)</name> | Local name of the fairway section (f.e.: Rhine between bridge A and bridge B) | M |
2.10.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object (default=FWY) | M |
2.10.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the fairway | C |
2.10.1.5s | <coordinate> | Fairway section begin and end coordinates (2x) | C | 7
2.10.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5
2.10.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5
2.10.1.5e | </coordinate> | | |
2.10.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |
2.10.1e | </geo_object> | | |
2.10.2s | <limitation> | Fairway section limitations | C |
2.10.2.1s | <limitation_period> | Limitation periods / intervals (All limitations have to include a limitation period with an interval code in order to allow proper calculations within voyage planning applications) | C |
2.10.2.1.1 | <date_start>xs:date</date_start> | Start date of limitation period (overall) INCLUDING time zone format=yyyy-mm-dd+hh:mm | M | 5
2.10.2.1.2 | <date_end>xs:date</date_end> | End date of limitation period INCLUDING time zone format=yyyy-mm-dd+hh:mm | C |
2.10.2.1.3 | <time_start>xs:time</time_start> | Start time of limitation period WITHOUT time zone format=hh:mm:ss [whereas ss=00] | C |
2.10.2.1.4 | <time_end>xs:time</time_end> | End time of limitation period WITHOUT time zone format=hh:mm:ss [whereas ss=00] | C |
2.10.2.1.5 | <interval_code>nts:interval_code_enum</interval_code> | Interval for limitation (mandatory M(5) but is set to C to be compatible with former XSD version) | C |
2.10.2.1e | </limitation_period> | | |
2.10.2.2 | <limitation_code>nts:limitation_code_enum</limitation_code> | Kind of limitation | M | 5
2.10.2.3 | <position_code>nts:position_code_enum</position_code> | Describes the position of the limitation related to the fairway | C |
2.10.2.4 | <value>xs:float</value> | Value of limitation (i.e. max draught) | C |
2.10.2.5 | <unit>nts:unit_enum</unit> | Unit of the value of the limitation | C |
2.10.2.6 | <reference_code>nts:reference_code_enum</reference_code> | Value reference | C |
2.10.2.7 | <indication_code>nts:indication_code_enum</indication_code> | Minimum or maximum or reduced by | C |
2.10.2.8s | <target_group> | Target group information | C |
2.10.2.8.1 | <target_group_code>nts:target_group_code_enum</target_group_code> | Target group (vessel type) for this limitation | M | 5
2.10.2.8.2 | <direction_code>nts:direction_code_enum</direction_code> | Upstream or downstream traffic, or both | M | 5
2.10.2.8e | </target_group> | | |
2.10.2e | </limitation> | | |
2.10e | </fairway_section> | | |
2.11s | <object> | Object section | C | 2
2.11.1s | <geo_object> | Geo Information of object | M | 5
2.11.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the object (1x) Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 8
2.11.1.2 | <name>xs:string (256)</name> | Local name of the aggregated object | M |
2.11.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object | M |
2.11.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the object | C |
2.11.1.5s | <coordinate> | Object coordinates (1x) | C | 8
2.11.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5
2.11.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5
2.11.1.5e | </coordinate> | | |
2.11.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |
2.11.1e | </geo_object> | | |
2.11.2s | <limitation> | Object limitation section | C |
2.11.2.1s | <limitation_period> | Limitation periods / intervals (All limitations have to include a limitation period with an interval code in order to allow proper calculations within voyage planning applications) | C |
2.11.2.1.1 | <date_start>xs:date</date_start> | Start date of limitation period (overall) INCLUDING time zone format=yyyy-mm-dd+hh:mm | M | 5
2.11.2.1.2 | <date_end>xs:date</date_end> | End date of limitation period INCLUDING time zone format=yyyy-mm-dd+hh:mm | C |
2.11.2.1.3 | <time_start>xs:time</time_start> | Start time of limitation period WITHOUT time zone format=hh:mm:ss [whereas ss=00] | C |
2.11.2.1.4 | <time_end>xs:time</time_end> | End time of limitation period WITHOUT time zone format=hh:mm:ss [whereas ss=00] | C |
2.11.2.1.5 | <interval_code>nts:interval_code_enum</interval_code> | Interval for limitation (mandatory M(5) but is set to C to be compatible with former XSD version) | C |
2.11.2.1e | </limitation_period> | | |
2.11.2.2 | <limitation_code>nts:limitation_code_enum</limitation_code> | Kind of limitation | M | 5
2.11.2.3 | <position_code>nts:position_code_enum</position_code> | Describes the position of the limitation related to the fairway | C |
2.11.2.4 | <value>xs:float</value> | Value of limitation (i.e. max draught) | C |
2.11.2.5 | <unit>nts:unit_enum</unit> | Unit of the value of the limitation | C |
2.11.2.6 | <reference_code>nts:reference_code_enum</reference_code> | Value reference | C |
2.11.2.7 | <indication_code>nts:indication_code_enum</indication_code> | Minimum or maximum or reduced by | C |
2.11.2.8s | <target_group> | Target group information | C |
2.11.2.8.1 | <target_group_code>nts:target_group_code_enum</target_group_code> | Target group (vessel type) for this limitation | M | 5
2.11.2.8.2 | <direction_code>nts:direction_code_enum</direction_code> | Upstream or downstream traffic, or both | M | 5
2.11.2.8e | </target_group> | | |
2.11.2e | </limitation> | | |
2.11e | </object> | | |
2e | </ftm> | | |
3s | <wrm> | Water related section | C | 1
3.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |
3.2s | <nts_number> | NtS Number | C |
3.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M | 5
3.2.2 | <year>xs:gYear (1900-9999)</year> | Current year of the notice | M | 5
3.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (see Developers Guide for WRM-Message Number generation) | M | 5
3.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of the notice (see Developers Guide for WRM-Message Serial Number generation) | M | 5
3.2e | </nts_number> | | |
3.3s | <validity_period> | Overall period of validity | M |
3.3.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |
3.3.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |
3.3e | </validity_period> | | |
3.4s | <geo_object> | Geo Information of measurement location | M | 5
3.4.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the object/fairway (1x or 2x) Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 9
3.4.2 | <name>xs:string (256)</name> | Local name of the object/fairway | M |
3.4.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object/fairway | M |
3.4.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the object/fairway | C |
3.4.5s | <coordinate> | Object/Fairway coordinates (1x or 2x) | C | 9
3.4.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5
3.4.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5
3.3.5e | </coordinate> | | |
3.3.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |
3.4e | </geo_object> | | |
3.5 | <reference_code>nts:reference_code_enum</reference_code> | Value reference (measurement reference) | C | 6
3.6s | <measure> | Measurements (normal or predicted values) | M | 5
3.6.1 | <predicted>xs:boolean</predicted> | Predicted measurement (1 or true) or real measurement (0 or false) | M |
3.6.2 | <measure_code>nts:measure_code_enum</measure_code> | Kind of water related information | M |
3.6.3 | <value>xs:float</value> | Measured or predicted value | C | 10
3.6.4 | <value_min>xs:float</value_min> | Lowest value of confidence interval | C |
3.6.5 | <value_max>xs:float</value_max> | Highest value of confidence interval | C |
3.6.6 | <unit>nts:unit_enum</unit> | Unit of the water related value | C |
3.6.7 | <barrage_code>nts:barrage_code_enum</barrage_code> | Barrage status | C | 11
3.6.8 | <regime_code>nts:regime_code_enum</regime_code> | Regime applicable | C | 12
3.6.9 | <measuredate>xs:dateTime</measuredate> | Date and Time of measurement or predicted value including time zone Format=yyyy-mm-ddThh:mm:ss+hh:mm | M |
3.6.10s | <difference> | Difference with comparative value | C |
3.6.10.1 | <value_difference>xs:float</value_difference> | Difference with comparative value | M | 5
3.6.10.2 | <time_difference>xs:duration</time_difference> | Time difference to measuredate of comparative value | M | 5
3.6.10e | </difference> | | |
3.6e | </measure> | | |
3e | </wrm> | | |
4s | <icem> | Ice related section | C | 1
4.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |
4.2s | <nts_number> | NtS Number | M |
4.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M |
4.2.2 | <year>xs:gYear (1900-9999)</year> | Current year of the notice | M |
4.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (per year, starting with: 1, 0 shall not be used for published notices) | M |
4.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of notice, original notice: 0 | M |
4.2e | </nts_number> | | |
4.3s | <validity_period> | Overall period of validity | M |
4.3.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |
4.3.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |
4.3e | </validity_period> | | |
4.4s | <fairway_section> | Fairway section — the limitation inside the fairway section cannot be used in the ICEM | M | 5
4.4.1s | <geo_object> | Geo Information of fairway | M | 5
4.4.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the fairway section (2x) Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M |
4.4.1.2 | <name>xs:string (256)</name> | Local Name of the fairway section (f.e.: Rhine between bridge A and bridge B) | M |
4.4.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object (default=FWY) | M |
4.4.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the fairway | C |
4.4.1.5s | <coordinate> | Fairway section begin and end coordinates (2x) | C | 7
4.4.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5
4.4.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5
4.4.1.5e | </coordinate> | | |
4.4.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |
4.4.1e | </geo_object> | | |
4.4e | </fairway_section> | | |
4.5s | <ice_condition> | Ice conditions | M |
4.5.1 | <measuredate>xs:dateTime</measuredate> | Date and Time of measurement or prediction including time zone Format=yyyy-mm-ddThh:mm:ss+hh:mm | M |
4.5.2 | <ice_condition_code>nts:ice_condition_code_enum</ice_condition_code> | Condition code | C | 4
4.5.3 | <ice_accessibility_code>nts:ice_accessibility_code_enum</ice_accessibility_code> | Accessibility code | C | 4
4.5.4 | <ice_classification_code>nts:ice_classification_code_enum</ice_classification_code> | Classification code | C | 4
4.5.5 | <ice_situation_code>nts:ice_situation_code_enum</ice_situation_code> | Situation code | C | 4
4.5e | </ice_condition> | | |
4e | </icem> | | |
5s | <werm> | Weather related section | C | 1
5.1 | <internal_id>xs:string (64)</internal_id> | Internal ID | C |
5.2s | <nts_number> | NtS Number | C |
5.2.1 | <organisation>xs:string (64)</organisation | Name of the publishing organisation (NtS Provider) | M | 5
5.2.2 | <year>xs:gYear (1900-9999)</year> | Year of issuing of the notice | M | 5
5.2.3 | <number>xs:integer (0-99999999)</number> | Number of the notice (per year, starting with: 1, 0 shall not be used for published notices) | M | 5
5.2.4 | <serial_number>xs:integer (0-99)</serial_number> | Serial number of notice, original notice: 0 | M | 5
5.2e | </nts_number> | | |
5.3s | <validity_period> | Overall period of validity | M | 13
5.3.1 | <date_start>xs:date</date_start> | Start date of validity period including time zone (yyyy-mm-dd+hh:mm) | M |
5.3.2 | <date_end>xs:date</date_end> | End date of validity period including time zone (yyyy-mm-dd+hh:mm) | C |
5.3e | </validity_period> | | |
5.4s | <fairway_section> | Fairway section | M |
5.4.1s | <geo_object> | Geo Information of fairway | M |
5.4.1.1 | <id>nts:isrs_code_type</id> | ISRS Location Code of the fairway section (2x) Pattern=[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5} | M | 7
5.4.1.2 | <name>xs:string (256)</name> | Local name of the fairway section (f.e.: Rhine between bridge A and bridge B) | M |
5.4.1.3 | <type_code>nts:type_code_enum</type_code> | Type of geographical object (default=FWY) | M |
5.4.1.4 | <position_code>nts:position_code_enum</position_code> | Describes the position related to the fairway | C |
5.4.1.5s | <coordinate> | Fairway section begin and end coordinates (2x) | C | 7
5.4.1.5.1 | <lat>xs:string (10-12)</lat> | [d]d mm.mmm[m] N | M | 5
5.4.1.5.2 | <long>xs:string (10-13)</long> | [d][d]d mm.mmm[m] E | M | 5
5.4.1.5e | </coordinate> | | |
5.4.1.6 | <fairway_name>xs:string (256)</fairway_name> | Waterway name (usefull if no RIS Index is available). | C |
5.4.1e | </geo_object> | | |
5.4e | </fairway_section> | | |
5.5s | <weather_report> | Weather Report (1x or 2x) | M |
5.5.1 | <measuredate>xs:dateTime</measuredate> | Date and Time of measurement or predicted value including time zone Format=yyyy-mm-ddThh:mm:ss+hh:mm | C |
5.5.2 | <forecast>xs:boolean</forecast> | Forecast (true or 1) OR Actual report (false or 0) | M |
5.5.3 | <weather_class_code>nts:weather_class_code_enum</weather_class_code> | Classification of weather report (0..Nx) | M | 3
5.5.4s | <weather_item> | Weather items (0..Nx) | C |
5.5.4.1 | <weather_item_code>nts:weather_item_code_enum</weather_item_code> | Weather item type (Wind, Wave etc) | M | 5
5.5.4.2 | <value_min>xs:float</value_min> | Actual or Minimum value | M | 5
5.5.4.3 | <value_max>xs:float</value_max> | Maximum value | C |
5.5.4.4 | <value_gusts>xs:float</value_gusts> | Gusts value (Wind) | C |
5.5.4.5 | <unit>nts:unit_enum</unit> | Unit of the value | C |
5.5.4.6 | <weather_category_code>nts:weather_category_code_enum</weather_category_code> | Classification of wind report | C |
5.5.4.7 | <direction_code_min>nts:weather_direction_code_enum</direction_code_min> | Direction of wind or wave | C |
5.5.4.8 | <direction_code_max>nts:weather_direction_code_enum</direction_code_max> | Direction of wind or wave | C |
5.5.4e | </weather_item> | | |
5.5e | </weather_report> | | |
5e | </werm> | | |
Legend for Occurrence (Occ.):
Mandatory (M)
Conditional (C)
Rules applicable to table "NtS XSD V.4.0.4.0":
1. In one <RIS Message> at least two sections have to be filled in:
— the <identification> section (1),
— one of the following sections:
— <ftm> (fairway and traffic related messages) (2),
— <wrm> (water related message) (3),
— <icem> (ice message) (4),
— <werm> (weather related message) (5).
2. At least one of the Group 2.10 (<fairway section>) or Group 2.11 (<object>) has to be given within <ftm>.
3. A combinations of <weather_class_code> tags (5.5.3) in section <weather_report> can be given.
4. In group 4.5 (<ice condition>) at least one of the conditional elements 4.5.2 to 4.5.5 have to be given.
5. If a conditional group contains mandatory subgroups or elements these will only be mandatory if the group on the higher level is applied.
6. Element <reference_code> is only mandatory for "WAL" (water level) in <wrm> (3.5).
7. A <geo_object> in <fairway section> (<ftm> 2.10.1 , <icem> 4.4.1, <werm> 5.4.1) is defined by the begin and end
ISRS Location Codes and coordinates (2 ISRS Location Codes and 2 sets of coordinates).
8. A <geo_object> in <object> section (<ftm> 2.11.1) is defined by the ISRS Location Code and coordinates of its center point (1 ISRS Location Code 1 set of coordinates).
9. A <geo_object> in <wrm> has 2 ISRS Location Codes and 2 sets of coordinates in case the <type_code> (3.4.3) is "FWY", "RIV" or "CAN", otherwise only 1 ISRS Location Code and 1 set of coordinates has to be given.
10. If there is a measurement the elements <value> (3.6.3) or <value_min> (3.6.4) and <value_max> (3.6.5) is/are mandatory if <measure_code> (3.6.2) is either "DIS", "VER", "LSD" or "WAL".
In case there is no measurement (and a message should be sent anyhow) the value elements shall be omitted.
11. Element <barrage_code> (3.6.7) is mandatory if <measure code> (3.6.2) is "BAR".
12. Element <regime_code> (3.6.8) is mandatory if <measure code> (3.6.2) is "REG".
13. Predictions for more than one <validity_period> (5.3) require individual <werm> messages.
14. In case of <icem> (4.4.2) and <werm> a <limitation> section is not applicable. Limitations shall be provided via FTM notices.
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:nts="http://www.ris.eu/nts/4.0.4.0" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace=">http://www.ris.eu/nts/4.0.4.0" elementFormDefault="qualified" attributeFormDefault="unqualified" version="4.0.4.0">
<!--
===========================================
= definition of main element RIS_Message =
= and corresponding type RIS_Message_Type =
===========================================
-->
<xs:element name="RIS_Message" type="nts:RIS_Message_Type">
<xs:annotation>
<xs:documentation>River Information Service Message</xs:documentation>
</xs:annotation>
</xs:element>
<xs:complexType name="RIS_Message_Type">
<xs:sequence>
<xs:element name="identification" type="nts:identification_type">
<xs:annotation>
<xs:documentation>Identification section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:choice>
<xs:annotation>
<xs:documentation>One msg contains one of these sections</xs:documentation>
</xs:annotation>
<xs:element name="ftm" type="nts:ftm_type" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Fairway and traffic related section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="wrm" type="nts:wrm_type" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Water related section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="icem" type="nts:icem_type" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Ice related section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="werm" type="nts:werm_type" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Weather related section</xs:documentation>
</xs:annotation>
</xs:element>
</xs:choice>
</xs:sequence>
</xs:complexType>
<!--
==========================================
= definition of identification_type, =
= used in definition of RIS_Message_Type =
==========================================
-->
<xs:complexType name="identification_type">
<xs:sequence>
<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">
<xs:annotation>
<xs:documentation>Internal ID</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="from">
<xs:annotation>
<xs:documentation>Sender (System) of the message</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="64"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="originator">
<xs:annotation>
<xs:documentation>Originator (initiator) of the information in this message</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="64"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="country_code" type="nts:country_code_enum">
<xs:annotation>
<xs:documentation>Country where message is valid</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="language_code" type="nts:language_code_enum">
<xs:annotation>
<xs:documentation>Original language used in the textual info. (contents)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="district" minOccurs="0">
<xs:annotation>
<xs:documentation>District / Region within the specified country, where the message is applicable</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="64"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="date_issue" type="xs:dateTime">
<xs:annotation>
<xs:documentation>Date and time of publication including time zone</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<!--
===================================================
= types used in definition of identification_type =
===================================================
-->
<xs:simpleType name="country_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="2"/>
<xs:enumeration value="AT"/>
<xs:enumeration value="BE"/>
<xs:enumeration value="BG"/>
<xs:enumeration value="CH"/>
<xs:enumeration value="CY"/>
<xs:enumeration value="CZ"/>
<xs:enumeration value="DE"/>
<xs:enumeration value="DK"/>
<xs:enumeration value="EE"/>
<xs:enumeration value="ES"/>
<xs:enumeration value="FI"/>
<xs:enumeration value="FR"/>
<xs:enumeration value="GB"/>
<xs:enumeration value="GR"/>
<xs:enumeration value="HR"/>
<xs:enumeration value="HU"/>
<xs:enumeration value="IE"/>
<xs:enumeration value="IT"/>
<xs:enumeration value="LT"/>
<xs:enumeration value="LU"/>
<xs:enumeration value="LV"/>
<xs:enumeration value="MD"/>
<xs:enumeration value="ME"/>
<xs:enumeration value="MT"/>
<xs:enumeration value="NL"/>
<xs:enumeration value="PL"/>
<xs:enumeration value="PT"/>
<xs:enumeration value="RO"/>
<xs:enumeration value="RS"/>
<xs:enumeration value="SE"/>
<xs:enumeration value="SI"/>
<xs:enumeration value="SK"/>
<xs:enumeration value="RU"/>
<xs:enumeration value="UA"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="language_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="2"/>
<xs:enumeration value="DE"/>
<xs:enumeration value="EN"/>
<xs:enumeration value="FR"/>
<xs:enumeration value="NL"/>
<xs:enumeration value="SK"/>
<xs:enumeration value="HU"/>
<xs:enumeration value="HR"/>
<xs:enumeration value="SR"/>
<xs:enumeration value="BG"/>
<xs:enumeration value="RO"/>
<xs:enumeration value="RU"/>
<xs:enumeration value="CS"/>
<xs:enumeration value="PL"/>
<xs:enumeration value="PT"/>
<xs:enumeration value="ES"/>
<xs:enumeration value="SV"/>
<xs:enumeration value="FI"/>
<xs:enumeration value="DA"/>
<xs:enumeration value="ET"/>
<xs:enumeration value="LV"/>
<xs:enumeration value="LT"/>
<xs:enumeration value="IT"/>
<xs:enumeration value="MT"/>
<xs:enumeration value="EL"/>
<xs:enumeration value="SL"/>
</xs:restriction>
</xs:simpleType>
<!--
==========================================
= definition of ftm_type, =
= used in definition of RIS_Message_Type =
==========================================
-->
<xs:complexType name="ftm_type">
<xs:sequence>
<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">
<xs:annotation>
<xs:documentation>Internal ID</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="nts_number" type="nts:nts_number_type">
<xs:annotation>
<xs:documentation>NtS Number</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="target_group" type="nts:target_group_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Target group information</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="subject_code" type="nts:subject_code_enum">
<xs:annotation>
<xs:documentation>Subject code must contain one of the following: Announcement (ANNOUN), Warning (WARNIN), Notice withdrawn (CANCEL) or Information service (INFSER). More information on the use of codes can be found in the NtS Encoding Guide.</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="validity_period" type="nts:validity_period_type">
<xs:annotation>
<xs:documentation>Overall period of validity</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="contents" minOccurs="0">
<xs:annotation>
<xs:documentation>Additional information in local language</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="500"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="source" minOccurs="0">
<xs:annotation>
<xs:documentation>Notice source (name of authority)</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="64"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="reason_code" type="nts:reason_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Reason / justification of the notice</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="communication" type="nts:communication_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Communication channel information</xs:documentation>
</xs:annotation>
</xs:element>
<xs:choice maxOccurs="unbounded">
<xs:element name="fairway_section" type="nts:fairway_section_type">
<xs:annotation>
<xs:documentation>Fairway section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="object" type="nts:object_type">
<xs:annotation>
<xs:documentation>Object section</xs:documentation>
</xs:annotation>
</xs:element>
</xs:choice>
</xs:sequence>
</xs:complexType>
<!--
========================================
= types used in definition of ftm_type =
========================================
-->
<xs:simpleType name="subject_code_enum">
<xs:restriction base="xs:string">
<xs:minLength value="3"/>
<xs:maxLength value="6"/>
<xs:enumeration value="ANNOUN"/>
<xs:enumeration value="WARNIN"/>
<xs:enumeration value="CANCEL"/>
<!-- the following values are added due to CR 128 -->
<xs:enumeration value="INFSER"/>
<!-- obsolete values due to CR 128 but still valid for backwards compatibility -->
<xs:enumeration value="OBSTRU"/>
<xs:enumeration value="PAROBS"/>
<xs:enumeration value="DELAY"/>
<xs:enumeration value="VESLEN"/>
<xs:enumeration value="VESHEI"/>
<xs:enumeration value="VESBRE"/>
<xs:enumeration value="VESDRA"/>
<xs:enumeration value="AVALEN"/>
<xs:enumeration value="CLEHEI"/>
<xs:enumeration value="CLEWID"/>
<xs:enumeration value="AVADEP"/>
<xs:enumeration value="NOMOOR"/>
<xs:enumeration value="SERVIC"/>
<xs:enumeration value="NOSERV"/>
<xs:enumeration value="SPEED"/>
<xs:enumeration value="WAVWAS"/>
<xs:enumeration value="PASSIN"/>
<xs:enumeration value="ANCHOR"/>
<xs:enumeration value="OVRTAK"/>
<xs:enumeration value="MINPWR"/>
<xs:enumeration value="DREDGE"/>
<xs:enumeration value="WORK"/>
<xs:enumeration value="EVENT"/>
<xs:enumeration value="CHGMAR"/>
<xs:enumeration value="CHGSER"/>
<xs:enumeration value="SPCMAR"/>
<xs:enumeration value="EXERC"/>
<xs:enumeration value="LEADEP"/>
<xs:enumeration value="LEVDEC"/>
<xs:enumeration value="LEVRIS"/>
<xs:enumeration value="LIMITA"/>
<xs:enumeration value="MISECH"/>
<xs:enumeration value="ECDISU"/>
<xs:enumeration value="NEWOBJ"/>
<xs:enumeration value="CHWWY"/>
<xs:enumeration value="CONWWY"/>
<xs:enumeration value="DIVER"/>
<xs:enumeration value="SPECTR"/>
<xs:enumeration value="LOCRUL"/>
<xs:enumeration value="VHFCOV"/>
<xs:enumeration value="HIGVOL"/>
<xs:enumeration value="TURNIN"/>
<xs:enumeration value="CONBRE"/>
<xs:enumeration value="CONLEN"/>
<xs:enumeration value="REMOBJ"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="reason_code_enum">
<xs:restriction base="xs:string">
<xs:minLength value="3"/>
<xs:maxLength value="6"/>
<xs:enumeration value="EVENT"/>
<xs:enumeration value="WORK"/>
<xs:enumeration value="DREDGE"/>
<xs:enumeration value="EXERC"/>
<xs:enumeration value="HIGWAT"/>
<xs:enumeration value="HIWAI"/>
<xs:enumeration value="HIWAII"/>
<xs:enumeration value="LOWWAT"/>
<xs:enumeration value="SHALLO"/>
<xs:enumeration value="CALAMI"/>
<xs:enumeration value="LAUNCH"/>
<xs:enumeration value="DECLEV"/>
<xs:enumeration value="FLOMEA"/>
<xs:enumeration value="BLDWRK"/>
<xs:enumeration value="REPAIR"/>
<xs:enumeration value="INSPEC"/>
<xs:enumeration value="FIRWRK"/>
<xs:enumeration value="LIMITA"/>
<xs:enumeration value="CHGFWY"/>
<xs:enumeration value="CONSTR"/>
<xs:enumeration value="DIVING"/>
<xs:enumeration value="SPECTR"/>
<xs:enumeration value="EXT"/>
<xs:enumeration value="MIN"/>
<xs:enumeration value="SOUND"/>
<xs:enumeration value="OTHER"/>
<xs:enumeration value="STRIKE"/>
<xs:enumeration value="FLOMAT"/>
<xs:enumeration value="EXPLOS"/>
<xs:enumeration value="ICE"/>
<xs:enumeration value="OBSTAC"/>
<!--the following values are added due to CR 128-->
<xs:enumeration value="CHGMAR"/>
<xs:enumeration value="DAMMAR"/>
<xs:enumeration value="FALMAT"/>
<xs:enumeration value="MISECH"/>
<xs:enumeration value="HEARIS"/>
<xs:enumeration value="HIGVOL"/>
<xs:enumeration value="ECDISU"/>
<xs:enumeration value="LOCRUL"/>
<xs:enumeration value="NEWOBJ"/>
<xs:enumeration value="OBUNWA"/>
<xs:enumeration value="VHFCOV"/>
<xs:enumeration value="REMOBJ"/>
<xs:enumeration value="LEVRIS"/>
<xs:enumeration value="SPCMAR"/>
<!--the following value is added due to CR 155-->
<xs:enumeration value="WERMCO"/>
<!--obsolete values due to CR 128 but still valid for backwards compatibility -->
<xs:enumeration value="INFSER"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="communication_type">
<xs:sequence>
<xs:element name="reporting_code" type="nts:reporting_code_enum">
<xs:annotation>
<xs:documentation>Reporting regime (information, or duty to report)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="communication_code" type="nts:communication_code_enum">
<xs:annotation>
<xs:documentation>Communication code (telephone, VHF etc.)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="number" minOccurs="0">
<xs:annotation>
<xs:documentation>Telephone, VHF number (including callsign), e-mail address, URL or teletext</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="128"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="label" minOccurs="0">
<xs:annotation>
<xs:documentation>Name of the attachment or additional information</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="256"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="remark" minOccurs="0">
<xs:annotation>
<xs:documentation>Additional remarks concerning the communication</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="1024"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="reporting_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="INF"/>
<xs:enumeration value="ADD"/>
<xs:enumeration value="REG"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="communication_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="TE"/>
<xs:enumeration value="AP"/>
<xs:enumeration value="EM"/>
<xs:enumeration value="AH"/>
<xs:enumeration value="TT"/>
<xs:enumeration value="FX"/>
<xs:enumeration value="LS"/>
<xs:enumeration value="FS"/>
<xs:enumeration value="SO"/>
<xs:enumeration value="EI"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="object_type">
<xs:sequence>
<xs:element name="geo_object" type="nts:geo_object_type">
<xs:annotation>
<xs:documentation>Geo Information of object</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="limitation" type="nts:limitation_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Object limitation section</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<!--
==========================================
= definition of wrm_type, =
= used in definition of RIS_Message_Type =
==========================================
-->
<xs:complexType name="wrm_type">
<xs:sequence>
<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">
<xs:annotation>
<xs:documentation>Internal ID</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="nts_number" type="nts:nts_number_type" minOccurs="0">
<xs:annotation>
<xs:documentation>NtS Number</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="validity_period" type="nts:validity_period_type">
<xs:annotation>
<xs:documentation>Overall period of validity</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="geo_object" type="nts:geo_object_type">
<xs:annotation>
<xs:documentation>Object section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="reference_code" type="nts:reference_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Value reference (measurement reference)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="measure" type="nts:measure_type" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Measurements (normal or predicted values)</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<!--
========================================
= types used in definition of wrm_type =
========================================
-->
<xs:complexType name="measure_type">
<xs:sequence>
<xs:element name="predicted" type="xs:boolean">
<xs:annotation>
<xs:documentation>Predicted measurement (1 or true) or real measurement (0 or false)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="measure_code" type="nts:measure_code_enum">
<xs:annotation>
<xs:documentation>Kind of water related information</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value" type="xs:float" minOccurs="0">
<xs:annotation>
<xs:documentation>Measured or predicted value</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value_min" type="xs:float" minOccurs="0">
<xs:annotation>
<xs:documentation>Lowest value of confidence interval</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value_max" type="xs:float" minOccurs="0">
<xs:annotation>
<xs:documentation>Highest value of confidence interval</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="unit" type="nts:unit_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Unit of the water related value</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="barrage_code" type="nts:barrage_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Barrage status</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="regime_code" type="nts:regime_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Regime applicable</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="measuredate" type="xs:dateTime">
<xs:annotation>
<xs:documentation>Date and Time of measurement or predicted value including time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="difference" type="nts:difference_type" minOccurs="0">
<xs:annotation>
<xs:documentation>Difference with comparative value</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="measure_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="DIS"/>
<xs:enumeration value="REG"/>
<xs:enumeration value="BAR"/>
<xs:enumeration value="VER"/>
<xs:enumeration value="LSD"/>
<xs:enumeration value="WAL"/>
<!-- obsolete values due to CR 151 but still valid for backwards compatibility -->
<xs:enumeration value="NOM"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="barrage_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="CLD"/>
<xs:enumeration value="OPG"/>
<xs:enumeration value="CLG"/>
<xs:enumeration value="OPD"/>
<xs:enumeration value="OPN"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="regime_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="2"/>
<xs:enumeration value="NO"/>
<xs:enumeration value="HI"/>
<xs:enumeration value="II"/>
<xs:enumeration value="I"/>
<xs:enumeration value="NN"/>
<xs:enumeration value="LO"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="difference_type">
<xs:sequence>
<xs:element name="value_difference" type="xs:float">
<xs:annotation>
<xs:documentation>Difference with comparative value</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="time_difference" type="xs:duration">
<xs:annotation>
<xs:documentation>Time difference with measuredata of comparative measurement</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<!--
==========================================
= definition of icem_type, =
= used in definition of RIS_Message_Type =
==========================================
-->
<xs:complexType name="icem_type">
<xs:sequence>
<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">
<xs:annotation>
<xs:documentation>Internal ID</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="nts_number" type="nts:nts_number_type">
<xs:annotation>
<xs:documentation>NtS Number</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="validity_period" type="nts:validity_period_type">
<xs:annotation>
<xs:documentation>Overall period of validity</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="fairway_section" type="nts:fairway_section_type">
<xs:annotation>
<xs:documentation>Fairway section — the limitation inside the fairway section cannot be used in the ICEM</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="ice_condition" type="nts:ice_condition_type" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Ice conditions</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<!--
=========================================
= types used in definition of icem_type =
=========================================
-->
<xs:complexType name="ice_condition_type">
<xs:sequence>
<xs:element name="measuredate" type="xs:dateTime">
<xs:annotation>
<xs:documentation>Date and Time of measurement or prediction including time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="ice_condition_code" type="nts:ice_condition_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Condition code</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="ice_accessibility_code" type="nts:ice_accessibility_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Accessibility code </xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="ice_classification_code" type="nts:ice_classification_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Classification code </xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="ice_situation_code" type="nts:ice_situation_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Situation code </xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="ice_condition_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="1"/>
<xs:enumeration value="A"/>
<xs:enumeration value="B"/>
<xs:enumeration value="C"/>
<xs:enumeration value="D"/>
<xs:enumeration value="E"/>
<xs:enumeration value="F"/>
<xs:enumeration value="G"/>
<xs:enumeration value="H"/>
<xs:enumeration value="K"/>
<xs:enumeration value="L"/>
<xs:enumeration value="M"/>
<xs:enumeration value="P"/>
<xs:enumeration value="R"/>
<xs:enumeration value="S"/>
<xs:enumeration value="U"/>
<xs:enumeration value="O"/>
<xs:enumeration value="V"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="ice_accessibility_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="1"/>
<xs:enumeration value="A"/>
<xs:enumeration value="B"/>
<xs:enumeration value="F"/>
<xs:enumeration value="L"/>
<xs:enumeration value="C"/>
<xs:enumeration value="D"/>
<xs:enumeration value="E"/>
<xs:enumeration value="G"/>
<xs:enumeration value="H"/>
<xs:enumeration value="M"/>
<xs:enumeration value="K"/>
<xs:enumeration value="T"/>
<xs:enumeration value="P"/>
<xs:enumeration value="V"/>
<xs:enumeration value="X"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="ice_classification_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="1"/>
<xs:enumeration value="A"/>
<xs:enumeration value="B"/>
<xs:enumeration value="C"/>
<xs:enumeration value="D"/>
<xs:enumeration value="E"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="ice_situation_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="NOL"/>
<xs:enumeration value="LIM"/>
<xs:enumeration value="NON"/>
</xs:restriction>
</xs:simpleType>
<!--
===========================================
= definition of werm_type, =
= used in definition of RIS_Message_Type =
===========================================
-->
<xs:complexType name="werm_type">
<xs:sequence>
<xs:element name="internal_id" type="nts:internal_id_type" minOccurs="0">
<xs:annotation>
<xs:documentation>Internal ID</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="nts_number" type="nts:nts_number_type" minOccurs="0">
<xs:annotation>
<xs:documentation>NtS Number</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="validity_period" type="nts:validity_period_type">
<xs:annotation>
<xs:documentation>Overall period of validity</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="fairway_section" type="nts:fairway_section_werm_type">
<xs:annotation>
<xs:documentation>Fairway section</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="weather_report" type="nts:weather_report_type" maxOccurs="2">
<xs:annotation>
<xs:documentation>Actual or Forecast report sections</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<!--
=========================================
= types used in definition of werm_type =
=========================================
-->
<xs:complexType name="fairway_section_werm_type">
<xs:sequence>
<xs:element name="geo_object" type="nts:geo_object_type">
<xs:annotation>
<xs:documentation>Geo Information of fairway</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="weather_report_type">
<xs:sequence>
<xs:element name="measuredate" type="xs:dateTime" minOccurs="0">
<xs:annotation>
<xs:documentation>Date and time of measurement or predicted value including time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="forecast" type="xs:boolean">
<xs:annotation>
<xs:documentation>Forecast (true or 1) OR Actual report (false or 0)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="weather_class_code" type="nts:weather_class_code_enum" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Classification of weather report</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="weather_item" type="nts:weather_item_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Weather items</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="weather_class_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="6"/>
<xs:enumeration value="CLR"/>
<xs:enumeration value="CLDY"/>
<xs:enumeration value="OCST"/>
<xs:enumeration value="DZZL"/>
<xs:enumeration value="RAIN"/>
<xs:enumeration value="LRAIN"/>
<xs:enumeration value="ORAIN"/>
<xs:enumeration value="HRAIN"/>
<xs:enumeration value="SLEET"/>
<xs:enumeration value="SNOW"/>
<xs:enumeration value="SNFALL"/>
<xs:enumeration value="HAIL"/>
<xs:enumeration value="SHWRS"/>
<xs:enumeration value="THSTRM"/>
<xs:enumeration value="HAZY"/>
<xs:enumeration value="FOG"/>
<xs:enumeration value="FOGPAT"/>
<xs:enumeration value="GALE"/>
<xs:enumeration value="STRM"/>
<xs:enumeration value="HURRC"/>
<xs:enumeration value="FZRA"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="weather_item_type">
<xs:sequence>
<xs:element name="weather_item_code" type="nts:weather_item_code_enum">
<xs:annotation>
<xs:documentation>Weather item type (Wind, Wave etc)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value_min" type="xs:float">
<xs:annotation>
<xs:documentation>Actual or Minimum value</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value_max" type="xs:float" minOccurs="0">
<xs:annotation>
<xs:documentation>Maximum value</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value_gusts" type="xs:float" minOccurs="0">
<xs:annotation>
<xs:documentation>Gusts value (Wind)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="unit" type="nts:unit_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Unit of the value</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="weather_category_code" type="nts:weather_category_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Classification of wind report</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="direction_code_min" type="nts:weather_direction_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Direction of wind or wave</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="direction_code_max" type="nts:weather_direction_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Direction of wind or wave</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="weather_item_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="2"/>
<xs:enumeration value="WI"/>
<xs:enumeration value="WA"/>
<xs:enumeration value="FG"/>
<xs:enumeration value="RN"/>
<xs:enumeration value="SN"/>
<xs:enumeration value="AT"/>
<xs:enumeration value="WT"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="weather_category_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="2"/>
<xs:enumeration value="0"/>
<xs:enumeration value="1"/>
<xs:enumeration value="2"/>
<xs:enumeration value="3"/>
<xs:enumeration value="4"/>
<xs:enumeration value="5"/>
<xs:enumeration value="6"/>
<xs:enumeration value="7"/>
<xs:enumeration value="8"/>
<xs:enumeration value="9"/>
<xs:enumeration value="10"/>
<xs:enumeration value="11"/>
<xs:enumeration value="12"/>
<xs:enumeration value="13"/>
<xs:enumeration value="14"/>
<xs:enumeration value="15"/>
<xs:enumeration value="16"/>
<xs:enumeration value="17"/>
<xs:enumeration value="18"/>
<xs:enumeration value="19"/>
<xs:enumeration value="20"/>
<xs:enumeration value="21"/>
<xs:enumeration value="22"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="weather_direction_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="N"/>
<xs:enumeration value="NE"/>
<xs:enumeration value="E"/>
<xs:enumeration value="SE"/>
<xs:enumeration value="S"/>
<xs:enumeration value="SW"/>
<xs:enumeration value="W"/>
<xs:enumeration value="NW"/>
<xs:enumeration value="WRB"/>
</xs:restriction>
</xs:simpleType>
<!--
=====================================
= types used in several definitions =
=====================================
-->
<xs:simpleType name="internal_id_type">
<xs:annotation>
<xs:documentation>Internal ID — best practice: global unique identifier</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string">
<xs:maxLength value="64"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="nts_number_type">
<xs:sequence>
<xs:element name="organisation">
<xs:annotation>
<xs:documentation>Name of the publishing organisation (NtS Provider)</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="64"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="year">
<xs:annotation>
<xs:documentation>Year of first issuing of the notice</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:gYear">
<xs:minInclusive value="1900"/>
<xs:maxInclusive value="9999"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="number">
<xs:annotation>
<xs:documentation>Number of the notice (per year, starting with: 1, 0 shall not be used for published notices)</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:integer">
<xs:minInclusive value="00000000"/>
<xs:maxInclusive value="99999999"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="serial_number">
<xs:annotation>
<xs:documentation>Serial number of notice (replacements and withdrawals), original notice: 0</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:integer">
<xs:minInclusive value="00"/>
<xs:maxInclusive value="99"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="validity_period_type">
<xs:sequence>
<xs:element name="date_start" type="xs:date">
<xs:annotation>
<xs:documentation>Start date of validity period including time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="date_end" type="xs:date" minOccurs="0">
<xs:annotation>
<xs:documentation>End date of validity period including time zone</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="fairway_section_type">
<xs:sequence>
<xs:element name="geo_object" type="nts:geo_object_type">
<xs:annotation>
<xs:documentation>Geo information of fairway</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="limitation" type="nts:limitation_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Fairway section limitations</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="geo_object_type">
<xs:sequence>
<xs:element name="id" type="nts:isrs_code_type" maxOccurs="2">
<xs:annotation>
<xs:documentation>ISRS Location Code of the fairway/object</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="name">
<xs:annotation>
<xs:documentation>Local name of the fairway section</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="256"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="type_code" type="nts:type_code_enum" default="FWY">
<xs:annotation>
<xs:documentation>Type of geographical object</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="position_code" type="nts:position_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Describes the position related to the fairway</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="coordinate" type="nts:coordinate_type" minOccurs="0" maxOccurs="2">
<xs:annotation>
<xs:documentation>Fairway section begin and end coordinates</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="fairway_name" minOccurs="0">
<xs:annotation>
<xs:documentation>Waterway name (usefull if no RIS Index is available)</xs:documentation>
</xs:annotation>
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:maxLength value="256"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="isrs_code_type">
<xs:annotation>
<xs:documentation>ISRS location code, unique identification of the geo object as defined in RIS Index encoding guide</xs:documentation>
</xs:annotation>
<xs:restriction base="xs:string">
<xs:length value="20"/>
<xs:pattern value="[A-Z]{2}[A-Z]{3}[A-Z0-9]{5}[A-Z0-9]{5}[0-9]{5}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="type_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="RIV"/>
<xs:enumeration value="CAN"/>
<xs:enumeration value="LAK"/>
<xs:enumeration value="FWY"/>
<xs:enumeration value="LCK"/>
<xs:enumeration value="BRI"/>
<xs:enumeration value="RMP"/>
<xs:enumeration value="BAR"/>
<xs:enumeration value="BNK"/>
<xs:enumeration value="GAU"/>
<xs:enumeration value="BUO"/>
<xs:enumeration value="BEA"/>
<xs:enumeration value="ANC"/>
<xs:enumeration value="BER"/>
<xs:enumeration value="MOO"/>
<xs:enumeration value="TER"/>
<xs:enumeration value="HAR"/>
<xs:enumeration value="FDO"/>
<xs:enumeration value="CAB"/>
<xs:enumeration value="FER"/>
<xs:enumeration value="PIP"/>
<xs:enumeration value="PPO"/>
<xs:enumeration value="HFA"/>
<xs:enumeration value="HMO"/>
<xs:enumeration value="SHY"/>
<xs:enumeration value="REF"/>
<xs:enumeration value="MAR"/>
<xs:enumeration value="LIG"/>
<xs:enumeration value="SIG"/>
<xs:enumeration value="TUR"/>
<xs:enumeration value="CBR"/>
<xs:enumeration value="TUN"/>
<xs:enumeration value="BCO"/>
<xs:enumeration value="REP"/>
<xs:enumeration value="FLO"/>
<xs:enumeration value="SLI"/>
<xs:enumeration value="DUK"/>
<xs:enumeration value="VTC"/>
<xs:enumeration value="RES"/>
<xs:enumeration value="LKB"/>
<xs:enumeration value="BRO"/>
<!--the following value is added due to CR 157-->
<xs:enumeration value="BNS"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="coordinate_type">
<xs:sequence>
<xs:element name="lat">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:minLength value="10"/>
<xs:maxLength value="12"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
<xs:element name="long">
<xs:simpleType>
<xs:restriction base="xs:string">
<xs:minLength value="10"/>
<xs:maxLength value="13"/>
</xs:restriction>
</xs:simpleType>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="limitation_type">
<xs:sequence>
<xs:element name="limitation_period" type="nts:limitation_period_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Limitation periods / intervals</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="limitation_code" type="nts:limitation_code_enum">
<xs:annotation>
<xs:documentation>Kind of limitation</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="position_code" type="nts:position_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Describes the position of the limitation related to the fairway</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="value" type="xs:float" minOccurs="0">
<xs:annotation>
<xs:documentation>Value of limitation (i.e. max draught)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="unit" type="nts:unit_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Unit of the value of the limitation</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="reference_code" type="nts:reference_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Value reference</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="indication_code" type="nts:indication_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Minimum or maximum or reduced by</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="target_group" type="nts:target_group_type" minOccurs="0" maxOccurs="unbounded">
<xs:annotation>
<xs:documentation>Target group information</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="limitation_period_type">
<xs:sequence>
<xs:element name="date_start" type="xs:date">
<xs:annotation>
<xs:documentation>Start date of limitation period including time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="date_end" type="xs:date" minOccurs="0">
<xs:annotation>
<xs:documentation>End date of limitation period including time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="time_start" type="xs:time" minOccurs="0">
<xs:annotation>
<xs:documentation>Start time of limitation period without time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="time_end" type="xs:time" minOccurs="0">
<xs:annotation>
<xs:documentation>End time of limitation period without time zone</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="interval_code" type="nts:interval_code_enum" minOccurs="0">
<xs:annotation>
<xs:documentation>Interval for limitation if applicable</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="interval_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="CON"/>
<xs:enumeration value="DAY"/>
<xs:enumeration value="WRK"/>
<xs:enumeration value="WKN"/>
<xs:enumeration value="SUN"/>
<xs:enumeration value="MON"/>
<xs:enumeration value="TUE"/>
<xs:enumeration value="WED"/>
<xs:enumeration value="THU"/>
<xs:enumeration value="FRI"/>
<xs:enumeration value="SAT"/>
<xs:enumeration value="DTI"/>
<xs:enumeration value="NTI"/>
<xs:enumeration value="RVI"/>
<xs:enumeration value="EXC"/>
<xs:enumeration value="WRD"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="limitation_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="6"/>
<xs:enumeration value="OBSTRU"/>
<xs:enumeration value="PAROBS"/>
<xs:enumeration value="DELAY"/>
<xs:enumeration value="VESLEN"/>
<xs:enumeration value="VESHEI"/>
<xs:enumeration value="VESBRE"/>
<xs:enumeration value="VESDRA"/>
<xs:enumeration value="AVALEN"/>
<xs:enumeration value="CLEHEI"/>
<xs:enumeration value="CLEWID"/>
<xs:enumeration value="AVADEP"/>
<xs:enumeration value="NOMOOR"/>
<xs:enumeration value="SERVIC"/>
<xs:enumeration value="NOSERV"/>
<xs:enumeration value="SPEED"/>
<xs:enumeration value="WAVWAS"/>
<xs:enumeration value="PASSIN"/>
<xs:enumeration value="ANCHOR"/>
<xs:enumeration value="OVRTAK"/>
<xs:enumeration value="MINPWR"/>
<xs:enumeration value="ALTER"/>
<xs:enumeration value="CAUTIO"/>
<xs:enumeration value="NOLIM"/>
<xs:enumeration value="TURNIN"/>
<xs:enumeration value="NOSHORE"/>
<xs:enumeration value="CONBRE"/>
<xs:enumeration value="CONLEN"/>
<!-- the following value is added due to CR 128 -->
<xs:enumeration value="LEADEP"/>
<!-- the following value is added due to CR 148 -->
<xs:enumeration value="NOBERT"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="position_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="2"/>
<xs:enumeration value="AL"/>
<xs:enumeration value="LE"/>
<xs:enumeration value="MI"/>
<xs:enumeration value="RI"/>
<xs:enumeration value="LB"/>
<xs:enumeration value="RB"/>
<xs:enumeration value="N"/>
<xs:enumeration value="NE"/>
<xs:enumeration value="E"/>
<xs:enumeration value="SE"/>
<xs:enumeration value="S"/>
<xs:enumeration value="SW"/>
<xs:enumeration value="W"/>
<xs:enumeration value="NW"/>
<xs:enumeration value="BI"/>
<xs:enumeration value="SM"/>
<xs:enumeration value="OL"/>
<xs:enumeration value="EW"/>
<xs:enumeration value="MP"/>
<xs:enumeration value="FP"/>
<xs:enumeration value="VA"/>
<xs:enumeration value="RY"/>
<xs:enumeration value="GY"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="reference_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="4"/>
<xs:enumeration value="NAP"/>
<xs:enumeration value="KP"/>
<xs:enumeration value="FZP"/>
<xs:enumeration value="ADR"/>
<xs:enumeration value="TAW"/>
<xs:enumeration value="PUL"/>
<xs:enumeration value="NGM"/>
<xs:enumeration value="ETRS"/>
<xs:enumeration value="POT"/>
<xs:enumeration value="LDC"/>
<xs:enumeration value="HDC"/>
<xs:enumeration value="ZPG"/>
<xs:enumeration value="GLW"/>
<xs:enumeration value="HSW"/>
<xs:enumeration value="LNW"/>
<xs:enumeration value="HNW"/>
<xs:enumeration value="IGN"/>
<xs:enumeration value="WGS"/>
<xs:enumeration value="RN"/>
<xs:enumeration value="HBO"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="indication_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="MAX"/>
<xs:enumeration value="MIN"/>
<xs:enumeration value="RED"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="target_group_type">
<xs:sequence>
<xs:element name="target_group_code" type="nts:target_group_code_enum" default="ALL">
<xs:annotation>
<xs:documentation>Target group (vessel type)</xs:documentation>
</xs:annotation>
</xs:element>
<xs:element name="direction_code" type="nts:direction_code_enum" default="ALL">
<xs:annotation>
<xs:documentation>Upstream or downstream traffic, or both</xs:documentation>
</xs:annotation>
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:simpleType name="target_group_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="ALL"/>
<xs:enumeration value="CDG"/>
<xs:enumeration value="COM"/>
<xs:enumeration value="PAX"/>
<xs:enumeration value="PLE"/>
<xs:enumeration value="CNV"/>
<xs:enumeration value="PUS"/>
<xs:enumeration value="NNU"/>
<xs:enumeration value="LOA"/>
<xs:enumeration value="SMA"/>
<xs:enumeration value="CND"/>
<xs:enumeration value="WOC"/>
<xs:enumeration value="MOV"/>
<xs:enumeration value="NMV"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="direction_code_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="3"/>
<xs:enumeration value="ALL"/>
<xs:enumeration value="UPS"/>
<xs:enumeration value="DWN"/>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="unit_enum">
<xs:restriction base="xs:string">
<xs:maxLength value="4"/>
<xs:enumeration value="cm"/>
<xs:enumeration value="m3/s"/>
<xs:enumeration value="h"/>
<xs:enumeration value="km/h"/>
<xs:enumeration value="kW"/>
<xs:enumeration value="m/s"/>
<xs:enumeration value="mm/h"/>
<xs:enumeration value="°C"/>
</xs:restriction>
</xs:simpleType>
</xs:schema>
Apendicele D]
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions
xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
xmlns:http= "http://schemas.xmlsoap.org/wsdl/http/"
xmlns:xs= "http://www.w3.org/2001/XMLSchema"
xmlns:soapenc= "http://schemas.xmlsoap.org/soap/encoding/"
xmlns:mime= "http://schemas.xmlsoap.org/wsdl/mime/"
xmlns:nts= "http://www.ris.eu/nts/4.0.4.0"
xmlns:tns= "http://www.ris.eu/nts.ms/2.0.4.0"
targetNamespace= "http://www.ris.eu/nts.ms/2.0.4.0"
name="NtS-Message-Service">
<!--
= specification of types =
-->
<wsdl:types>
<!--
= xml-schema for types =
-->
<xs:schema
targetNamespace="http://www.ris.eu/nts.ms/2.0.4.0"
xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:nts= "http://www.ris.eu/nts/4.0.4.0"
xmlns:nts-ms= "http://www.ris.eu/nts.ms/2.0.4.0"
elementFormDefault="qualified"
attributeFormDefault="unqualified"
version="2.0.4.0">
<!-- import NtS schema -->
<xs:import
namespace="http://www.ris.eu/nts/4.0.4.0"
schemaLocation="http:// www.ris.eu/nts/4.0/NtS_XSD_V.4.0.4.0.xsd" />
<!-- query with filters, parameters according to the NtS standard -->
<xs:element name="get_messages_query">
<xs:complexType>
<xs:sequence>
<!-- type of message (FTM, WRM, ICEM, WERM) -->
<xs:element name="message_type" type="nts-ms:message_type_type"/>
<!-- ISRS codes for fairway sections or objects -->
<xs:element name="ids" type="nts-ms:id_pair" minOccurs="0" maxOccurs="unbounded"/>
<!-- time of validity -->
<xs:element name="validity_period" type="nts:validity period type"
minOccurs="0"/>
<!-- date of publication of the notice -->
<xs:element name="dates_issue" type="nts-ms:date_pair" minOccurs="0" maxOccurs="unbounded"/>
<!-- optional parameter for paging mechanism -->
<xs:element name="paging_request" type="nts-ms:paging_request_type" minOccurs="0"/>
</xs:sequence>
</xs:complexType>
</xs:element>
<!-- result to query — can contain
— "nts:RIS_MessageType", arbitrary number, defined in the NtS-xsd (see www.ris.eu)
— "nts-ms:error_code_type", arbitrary number, defined in this schema
— "nts-ms:paging_result_type", optional, defined in this schema -->
<xs:element name="get_messages_result">
<xs:complexType>
<xs:sequence>
<xs:element name="result_message" type="nts:RIS_Message_Type" minOccurs= "0" maxOccurs="unbounded"/>
<xs:element name="result_error" type="nts-ms:error_code_type" minOccurs= "0" maxOccurs="unbounded"/>
<xs:element name="paging_result" type="nts-ms:paging_result_type" minOccurs="0"/>
</xs:sequence>
</xs:complexType>
</xs:element>
<!-- type definitions used in request -->
<xs:simpleType name="message_type_type">
<xs:restriction base="xs:string">
<xs:enumeration value="FTM"/>
<xs:enumeration value="WRM"/>
<xs:enumeration value="ICEM"/>
<xs:enumeration value="WERM"/>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="id_pair">
<xs:sequence>
<xs:element name="id" type="nts:isrs_code_type" minOccurs="1" maxOccurs="2" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="date_pair">
<xs:sequence>
<xs:element name="date_start" type="xs:date"/>
<xs:element name="date_end" type="xs:date" minOccurs="0"/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="paging_request_type">
<xs:sequence>
<xs:element name="offset" type="xs:nonNegativeInteger"/>
<xs:element name="limit" type="xs:nonNegativeInteger"/>
<xs:element name="total_count" type="xs:boolean"/>
</xs:sequence>
</xs:complexType>
<!-- type definitions used in response -->
<xs:simpleType name="error_code_type">
<xs:restriction base="xs:string">
<xs:enumeration value="e010">
<xs:annotation>
<xs:documentation>Description: message type not supported, Explanation: web service does not support the requested message type</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e030">
<xs:annotation>
<xs:documentation>Description: paging parameters inconsistent with messages, Explanation: parameters for paging mechanism do not fit the available messages, e.g. Offset >= Total Count</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e100">
<xs:annotation>
<xs:documentation>Description: syntax error in request, Explanation: request violates the schema for requests</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e110">
<xs:annotation>
<xs:documentation>Description: incorrect message type, Explanation: given message type is not known</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e120">
<xs:annotation>
<xs:documentation>Description: incorrect type-specific parameters, Explanation: type-specific parameters are erroneous</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e130">
<xs:annotation>
<xs:documentation>Description: incorrect paging parameters, Explanation: given parameters for the paging mechanism are erroneous</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e200">
<xs:annotation>
<xs:documentation>Description: operation not known, Explanation: the requested operation is unknown</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e300">
<xs:annotation>
<xs:documentation>Description: data source unavailable, Explanation: data source of the web service for the NtS data is temporarily unavailable</xs:documentation>
</xs:annotation>
</xs:enumeration>
<xs:enumeration value="e310">
<xs:annotation>
<xs:documentation>Description: too many results for request, Explanation: server is unable to handle number of results</xs:documentation>
</xs:annotation>
</xs:enumeration>
</xs:restriction>
</xs:simpleType>
<xs:complexType name="paging_result_type">
<xs:sequence>
<xs:element name="offset" type="xs:nonNegativeInteger"/>
<xs:element name="count" type="xs:nonNegativeInteger"/>
<xs:element name="total_count" type="xs:nonNegativeInteger" minOccurs="0"/>
</xs:sequence>
</xs:complexType>
</xs:schema>
</wsdl:types>
<!--
= specification of messages =
-->
<wsdl:message name="get_messages_request">
<wsdl:part name="parameters" element="tns:get_messages_query"/>
</wsdl:message>
<wsdl:message name="get_messages_response">
<wsdl:part name="parameters" element="tns:get_messages_result"/>
</wsdl:message>
<!--
= specification of port type =
-->
<wsdl:portType name="NtS_message_service">
<wsdl:operation name="get_messages">
<wsdl:input message="tns:get_messages_request"/>
<wsdl:output message="tns:get_messages_response"/>
</wsdl:operation>
</wsdl:portType>
<!--
= specification of binding =
-->
<wsdl:binding name="NtS_message_service_soap_binding" type="tns:NtS_message_service">
<soap:binding style="document" transport= "http://schemas.xmlsoap.org/soap/http" />
<wsdl:operation name="get_messages">
<soap:operation soapAction= "http://www.ris.eu/nts.ms/get_messages" />
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<!--
= specification of service =
-->
<wsdl:service name="NtS_message_service_service">
<wsdl:port name="NtS_message_service" binding="tns:NtS_message_service_soap_binding">
<soap: address location= "http://nts-ms.example.org/NtS_message_service" />
</wsdl:port>
</wsdl:service>
</wsdl:definitions>
ETICHETE
Eticheta XML | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
RIS_message | NtS message | NtS съобщение | Mensaje NtS | Zpráva NtS | NtS-meddelelse | NtS Nachricht | NtS teade | Mήνυμα NtS (Σύστ. Πληρ. Εσ. Ναυσ.) | Message NtS | NtS poruka | messaggio NtS | NtS ziņojums | NtS pranešimas
Identification | Identification section | Идентификационен раздел | Sección de identificación | Identifikační úsek | Identifikationsrubrik | Identifikationsabschnitt | Identifitseerimise jaotis | Τμήμα αναγνώρισης | Identification | Identifikacijski dio | identificazione del tratto | Identifikācija | Identifikavimas
From | Sender of the message | Подател | Remitente | Odesilatel | Afsender | Absender | Teate saatja | Αποστολέας του μηνύματος | Expéditeur du message | Pošiljatelj | mittente del messaggio | Nosūtītājs | Pranešimo siuntėjas
Originator | Originator of the information | Автор на информацията | Origen de la información | Autor zprávy | Informationskilde | Urheber der Nachricht | Teavitaja | Προέλευση των πληροφοριών | Origine de l’information | Izvor informacija | origine dell'informazione | Informācijas autors | Informacijos pateikėjas
Country_code | Country where message is valid | Държава, в която е валидно съобщението | País en que el mensaje es válido | Dotčená země | Berørt land | Betroffenes Land | Riik, kus teade kehtib | Χώρα ισχύος του μηνύματος | Pays où le message est valide | Država gdje poruka vrijedi | Stato interessato | Ziņojuma valsts | Šalis, kurioje galioja pranešimas
Language_code | Original language | Оригинален език | Lengua original | Originální jazyk | Originalsprog | Originalsprache | Algkeel | Πρωτότυπη γλώσσα | Langue d'origine | Originalni jezik | lingua originale | Ziņojuma valoda | Originalo kalba
District | District/region within country | Регион от държавата | Región del país | Dotčená oblast v zemi | Berørt region/område | Betroffenes Gebiet im Land | Riigi piirkond | Περιοχή/περιφέρεια χώρας | Région | Područje unutar države | area/regione interessata | Rajons/ valsts reģions | Rajonas / regionas šalyje
Date_issue | Date of issue | Дата на издаване | Fecha de emisión | Datum vydání | Offentliggørelsesdato | Herausgabedatum | Väljaandmise kuupäev | Ημερομηνία έκδοσης | Date de publication | Datum izdavanja | data di emissione | Sastādīšanas datums | Išdavimo data
Time_issue | Time of issue | Час на издаване | Hora de emisión | Čas vydání | Offentliggørelsestidspunkt | Herausgabezeit | Väljaandmise kellaaeg | Ώρα έκδοσης | Heure de publication | Vrijeme izdavanja | orario di emissione | Sastādīšanas laiks | Išdavimo laikas
Ftm | Fairway and traffic related message | Известие до корабоводителите | Mensaje sobre vía navegable y tráfico | Zpráva týkající se vodních cest a provozu | Farvands- og trafikrelaterede meddelelser | Wasserstraßen- und verkehrsbezogene Nachricht | Teated faaravaatri ja liikluse kohta | Μήνυμα σχετικά με δίαυλο και κυκλοφορία | Message lié à la voie d’eau et au trafic | Priopćenje brodarstvu | messaggio relativo a canale navigabile e traffico | Ziņojums par kuģu ceļu un satiksmi | Su farvateriu ir laivų eismu susijęs pranešimas
NtS_number | Number section | Номер на секция | Número de la sección | Číslo sekce | Nummerrubrik | Nummerierungsabschnitt | Numbri osa | Tμήμα αρίθμησης | Numéro | Odjeljak za broj poruke | numero del tratto | Numuru sadaļa | Numeris
Organisation | Publishing organisation | Издаваща организация | Organización que publica el mensaje | Vydávající organizace | Offentliggørende organisation | Herausgebende Organisation | Väljaandev organisatsioon | Οργανισμός έκδοσης | Entité émettrice | Organizacija | organizzazione emittente | Publicējošā organizācija | Skelbianti organizacija
Year | Year | Година | Año | Rok | År | Jahr | Aasta | Έτος | Année | Godina | anno | Gads | Metai
Number | Number (of the notice) | Номер | Número (del aviso) | Číslo zprávy | (Meddelelsens) nr. | Nummer (der Nachricht) | (Teatise) number | Αριθμός (μηνύματος) | Numéro (de l'avis) | Broj (poruke) | numero (dell'avviso) | (Ziņojuma) numurs | Numeris (pranešimo)
Serial_number | Serialnumber | Сериен номер | Número de serie | Číslo verze | Serienummer | Versionsnummer | Seerianumber | Αύξων αριθμός | Numéro de série | Serijski broj | numero progressivo | Sērijas numurs | Serijos numeris
Target_group | Information about target group | Информация за група получатели | Información sobre el usuario destinatario | Cílová skupina | Målgruppe — strækning | Information zur Zielgruppe | Sihtrühma jaotis | Τμήμα στοχευόμενης ομάδας | Type d'usagers concernés | Ciljana skupina | gruppo destinatario | Mērķgrupa | Tikslinė grupė
Target_group_code | Target group | Код на групата получатели | Código usuario destinatario | Kód cílové skupiny | Kode for målgruppe | Zielgruppe | Sihtrühma kood | Κωδικός στοχευόμενης ομάδας | Code usagers concernés | Oznaka ciljane skupine | codice gruppo destinatario | Mērķgrupas kods | Tikslinės grupės kodas
Direction_code | Affected direction | Код за направление | Dirección tráfico | Směr | Kode for sejlretning | Betroffene Richtung | Sõidusuuna kood | Κωδικός κατεύθυνσης κυκλοφορίας | Sens de parcours | Oznaka smjera prometa | codice direzione traffico | Satiksmes virziena kods | Eismo krypties kodas
Subject_code | Subject | Тема | Asunto | Předmět | Emne | Betrifft | Teema | Θέμα | Sujets de l'avis | Predmet | codice oggetto | Ziņojuma temats | Tema
Validity_period | Period of validity | Срок на валидност | Período de validez | Doba platnosti | Gyldighedsperiode | Gültigkeitszeitraum | Kehtivusaeg | Περίοδος ισχύος | Période de validité | Rok valjanosti | periodo di validità | Derīguma termiņš | Galiojimo laikas
Date_start | From | От дата | De | Od | Startdato | Ab | Alates | Από | Date de début | Od | da (aaaammgg) | No | Nuo
Date_end | Until | До дата | Α | Do | Slutdato | Bis | Kuni | Έως | Date de fin | Do | fino a (aaaammgg) | Līdz | Iki
Contents | Additional information | Съдържание | Contenido | Text | Indhold | Ergänzende Informationen | Sisu | Περιεχόμενα | Contenu | Sadržaj | testo | Saturs | Turinys
Source | Notice source (authority) | Официален източник на известието | Fuente del aviso (autoridad) | Vydavatel zprávy | Infokilde (myndighed) | Herausgeber der Nachricht | Teatise allikas (ametiasutus) | Προέλευση μηνύματος (Αρχή) | Source | Izvor priopćenja | fonte dell'avviso (autorità) | Informācijas avots (iestāde) | Pranešimo šaltinis (institucija)
Reason_code | Reason of notice | Причина за известието | Motivo del aviso | Důvod zprávy | Årsag til meddelelse | Grund der Nachricht | Teatise põhjus | Αιτία μηνύματος | Evènement | Razlog priopćenja | motivazione | Ziņojuma iemesls | Pranešimo paskirtis
Communication | Communication information | Информация за комуникация | Sección comunicación | Informace o komunikačním kanále | Kommunikationsdel | Information zu Kommunikationswegen | Teabevahetuse jaotis | Τμήμα επικοινωνίας | Canal d'information | Informacije o komunikacijskom kanalu | comunicazione | Paziņojums | Ryšio kanalas
Reporting_code | Reporting regime | Режим за известяване | Régimen de notificación | Režim hlášení | Rapporteringskanal | Meldungsart | Aruandluse kord | Καθεστώς αναφοράς | Obligation de s'annoncer | Režim javljanja | regime di segnalazione | Paziņojuma veids | Pranešimo režimas
Communication_code | Means of communication | Средство за свръзка | Medio de comunicación | Prostředky komunikace | Kommunikationsmiddel | Kommunikationsweg | Sidevahendid | Μέσο επικοινωνίας | Moyen de communication | Sredstvo komunikacije | mezzo di comunicazione | Saziņas līdzekļi | Ryšio priemonės
Number (Communication section) | Number or address | Номер или адрес | Número o dirección | Číslo nebo adresa | Nr. eller adresse | Nummer oder Adresse | Number või aadress | Αριθμός ή διεύθυνση | Numéro ou adresse | Broj ili adresa | numero o indirizzo | Numurs vai adrese | Numeris arba adresas
Fairway_section | Waterway or waterway section | Плавателен воден път или негов участък | Vía navegable o tramo | Úsek vodní cesty | Vandvejs- eller farvandsstrækning | Wasserstraße oder -abschnitt | Veetee või faarvaatri jaotis | Τμήμα πλωτής οδού ή διαύλου | Voie ou section de voie | Dionica vodnog ili plovnog puta | tratto idrovia o canale navigabile | Ūdensceļš vai kuģu ceļš | Vandens kelias arba vandens kelio ruožas
Geo_object | Location | Географска информация за водния път или обекта | Ubicación | Geografické informace o vodní cestě nebo objektu | Position | Geoinformation | Geo-teave veetee või objekti kohta | Γεωγραφικές πληροφορίες πλωτής οδού ή αντικειμένου | Objet géo-référencé | Geografske informacije o vodnom putu ili objektu | definizione geografica dell'idrovia o dell'oggetto | Ģeogrāfiskā informācija par ūdensceļu vai objektu | Geografinė informacija apie vandens kelią arba objektą
Id (Geo_Object section) | ISRS Location Code | Идентификация (на географския обект) | Código de posición ISRS | Identifikace | ISRS Location Code | ISRS Location Code | Identifitseerimine | Στοιχεία αναγνώρισης | Identifiant | Identifikacija | identificativo oggetto geografico | Identifikācija | Identifikavimo kodas
Name (Geo_Object section) | Name of object | Наименование на географския обект | Denominación de objeto geográfico | Název geografického objektu | Navn på objekt | Name | Geo-objekti nimi | Ονομασία γεωγραφικού αντικειμένου | Toponyme | Ime geo objekta | denominazione dell'oggetto geografico | Ģeogrāfiskā objekta nosaukums | Geografinio objekto pavadinimas
Type_code (Geo_Object section) | Type | Тип на географския обект | Tipo de vía navegable | Typ objektu | Type | Objekttyp | Veetee tüüp | Τύπος πλωτής οδού | Type | Vrsta objekta | tipo di idrovia | Ūdensceļa veids | Vandens kelio tipas
Coordinate | Coordinates | Координати на началото и края на участъка от фарватера | Coordenadas | Souřadnice počátečních a koncových bodů | Koordinater | Koordinaten | Faarvaatri algus- ja lõppkoordinaadid | Γεωγραφικές συντεταγμένες αρχής και τέλους διαύλου | Coordonnées | Koordinate početka i kraja plovnog puta | coordinate dei punti di delimitazione del tratto navigabile | Kuģu ceļa sākuma un beigu koordinātas | Farvaterio pradžios ir pabaigos koordinatės
Lat (Coordinate) | Latitude | Географска ширина (в десетична стойност) | Latitud | Zeměpisná šířka (desetinné číslo) | Breddegrad | Breitengrad | Laiuskraad (kümnendmurd) | Γεωγραφικό πλάτος (δεκαδικά) | Latitude (décimale) | Geografska širina (decimalno) | latitudine (decimali) | Platums (decimāldaļskaitlis) | Platuma (dešimtųjų tikslumu)
Long (Coordinate) | Longitude | Географска дължина (в десетична стойност) | Longitud | Zeměpisná délka (desetinné číslo) | Længdegrad | Längengrad | Pikkuskraad (kümnendmurd) | Γεωγραφικό μήκος (δεκαδικά) | Longitude (décimale) | Geografska dužina (decimalno) | longitudine (decimali) | Garums (decimāldaļskaitlis) | Ilguma (dešimtųjų tikslumu)
Limitation | Limitation | Раздел за ограничения | Limitación | Druh omezení | Begrænsning | Einschränkung | Piirangu jaotis | Τμήμα περιορισμών | Restriction | Ograničenja | limitazione | Ierobežojums | Apribojimo būdas
Limitation_period | (Limitation) periods/intervals | Срок на действие на ограничението | (Limitación) períodos /intervalos | (omezení) období/interval | (Begrænsning) perioder/tidsintervaller | Zeitliche Gültigkeit der Einschränkung | (Piirangu) perioodid/intervallid | (Περιορισμοί) περίοδοι/διαστήματα | Période de restriction | Trajanje (ograničenja) | durata della limitazione | (Ierobežojuma) darbības laiks/ intervāli | (Apribojimo) laikotarpis / intervalas
Date_start (Limitation_period) | From | От дата | De | Od | Fra | Ab | Alates | Από | Date de début | Od | da (aaaammgg) | No | Nuo
Date_end (Limitation_period) | Until | До дата | A | Do | Til | Bis | Kuni | Έως | Date de fin | Do | fino a (aaaammgg) | Līdz | Iki
Time_start (Limitation_period) | From (hh:mm) | От час (ччмм) | De (hhmm) | Od (hhmm) | Fra kl. (tt:mm) | Ab (hh:mm) | Alates (ttmm) | Από (ωωλλ) | Heure de début (hh:mm) | Od (hh:mm) | dalle (hhmm) | No (hhmm) | Nuo (hh:mm)
Time_end (Limitation_period) | Until (hh:mm) | До час (ччмм) | A (hhmm) | Do (hhmm) | Til kl. (tt:mm) | Bis (hh:mm) | Kuni (ttmm) | Έως (ωωλλ) | Heure de fin (hh:mm) | Do (hh:mm) | alle (hhmm) | Līdz (hhmm) | Iki (hh:mm)
Interval_code (Limitation_period) | Interval | Интервал | Intervalo | Interval | Interval | Intervall | Intervall | Συχνότητα | Périodicité | Interval | periodicità | Intervāls | Intervalas
Limitation_code | Kind of limitation | Вид на ограничението | Tipo de limitación | Druh omezení | Begrænsningens art | Art der Einschränkung | Piirangu liik | Είδος περιορισμών | Code de la restriction | Vrsta ograničenja | tipo di limitazione | Ierobežojuma veids | Apribojimo rūšis
Position_code | Position | Позиция | Posición | Poloha (omezení) | Position | Lage | (Piirangu) positsioon | Στίγμα των περιορισμών | Position | Pozicija (ograničenja) | localizzazione (della limitazione) | (Ierobežojuma) pozīcija | (Apribojimo) pozicija
Value | Numerical value | Числова стойност | Valor numérico | Číselný hodnota (omezení) | Numerisk værdi | Zahlenwert | (Piirangu) arvväärtus | Αριθμητική τιμή (περιορισμών) | Valeur | Brojčana vrijednost (ograničenja) | attributo numerico (della limitazione) | (Ierobežojuma) skaitliskā vērtība | (Apribojimo) skaitinė vertė
Unit | Unit | Мерна единица | Unidad | Jednotka | Enhed | Einheit | Ühik | Μονάδα | Unité | Jedinica | unità di misura | Mērvienība | Vienetai
Fairway_name | Waterway | Име на воден път | Vía navegable | Vodní cesta | Vandvej | Wasserstraße | Veetee | Ονομασία της πλωτής οδού | Nom de la voie d’eau | Plovni put | via navigabile | Ūdensceļš | Vandens kelias
Reference_code | Value reference | Код за справка | Referencia | Jednotka | Referenceværdi | Bezugssystem | Väärtuse viide | Τιμή αναφοράς | Référentiel de la valeur | Referentna vrijednost | parametro di riferimento | Atsauces vērtība | Atskaitos sistema
Indication_code | Indication of limitation | Означение за ограничение | Indicación de limitación | Indikace omezení | Angivelse af begrænsning | Hinweis zum Einschränkungswert | Märge piirangu kohta | Ένδειξη περιορισμών | Indication de la restriction | Oznaka ograničenja | indicazione del valore di limitazione | Ierobežojuma norāde | Apribojimo rodmenys
Object | Object | Обект | Objeto | Objekt | Objekt | Objekt | Objekt | Αντικείμενο | Objet | Objekt | oggetto | Objekts | Objektas
Geo_object section for an Object | Location | Географска информация за обекта | Ubicación | Geografická informace o objektu | Position | Geografische Definition des Objekts | Objekti geo-teave | Γεωγραφικές πληροφορίες αντικειμένου | Géo-Objet de référence pour l'objet | Geografske informacije o objektu | oggetto — informazione geografica | Ģeogrāfiskā informācija par objektu | Objekto geografinė informacija
Type_code (Geo_object section) | Type of object | Тип на обекта | Tipo objeto | Typ objektu | Objekttype | Objekttyp | Objekti liik | Τύπος αντικειμένου | Type | Vrsta objekta | tipo di oggetto | Objekta tips | Objekto tipas
Coordinate (Geo_object section) | Object coordinates | Координати на географския обект | Coordenadas objeto | Souřadnice objektu | Objektets koordinater | Koordinaten des Objekts | Objekti koordinaadid | Γεωγραφικές συντεταγμένες αντικειμένου | Coordonnées * | Koordinate objekta | coordinate dell'oggetto | Objekta koordinātas | Objekto koordinatės
Wrm | Water related message | Съобщения за нивото на водата | Mensaje relativo al agua | Hlášení o vodním stavu | Vandstandsrelateret meddelelse | Wasserstandsmeldung | Teade veeolude kohta | Μήνυμα όσον αφορά τα ύδατα | Message de niveau d'eau | Poruka o stanju vodostaja | messaggio riguardante le acque | Informācija par ūdens līmeni | Informacija apie vandens lygį
Measure | Measurements (normal or predicted) | Измерени стойности (типични или прогнозни) | Medidas (reales o previstas) | Měření (normální nebo předpovědní) | Målingens art (målt eller prognose) | Messwerte bzw. Prognosewerte | Mõõtmised (tavapärased või prognoositavad) | Μετρήσεις (κανονικές ή προβλεπόμενες) | Mesures (réelles ou prévues) | Mjerenja (izmjerena ili prognozirana) | livello idrometrico (normale o previsto) | Mērījumu veids (normālais vai prognozētais) | Vandens lygio vertės (įprastos arba numatomos)
Predicted | Prediction | Прогноза | Previsión | Předpověď | Prognose | Vorhersage | Eeldus | Πρόβλεψη | prévu | Prognoza | previsione | Prognoze | Prognozė
Measure_code | Kind of water related information | Тип на измерванията на водата | Tipo de información relativa al agua | Druh hlášení o vodním stavu | Art vandstandsoplysning | Art der Wasserstandsmeldung | Veeolusid käsitleva teate liik | Πληροφορίες όσον αφορά το είδος των υδάτων | Code de la mesure | Vrsta informacije o vodostaju | tipo di informazione idrometrica | Veids informācijai par ūdens līmeni | Pranešimo apie vandens lygį rūšis
Difference | Difference to previous value | Разлика спрямо предишна стойност | Diferencia con respecto al valor anterior | Rozdíl vůči předcházející hodnotě | Ændring i forhold til forrige | Abweichung zum vorherigen Wert | Erinevus | Διαφορά | Différence | Razlika | differenza | Starpība | Skirtumas
Value_difference | value difference to comparative measurement | Разлика в стойността спрямо сравнителното измерване | Diferencia de valor con respecto a la medida comparativa | Rozdíl vůči porovnávacímu měření | Værdiforskel i forhold til komparativ måling | Differenz zur Vergleichsmessung | Väärtuse erinevus võrdlusmõõdust | Διαφορά τιμής ως προς συγκριτική μέτρηση | Différence de valeur | Razlika u vrijednosti | differenza di valore in seguito a misurazione comparativa | Salīdzinošā mērījuma vērtību starpība | lyginamojo matavimo verčių skirtumas
Time_difference | time difference to comparative measurement | Разлика във времето спрямо сравнително измерване | Diferencia de tiempo con respecto a la medida comparativa | Časový rozdíl vůči porovnávacímu měření | Tidsforskel i forhold til komparativ måling | Zeitdifferenz zur Vergleichsmessung | Aja erinevus võrdlusmõõdust | Χρονική διαφορά ως προς συγκριτική μέτρηση | Différence de temps | Razlika u vremenu | differenza di tempo in seguito a misurazione comparativa | Salīdzinošā mērījuma laika starpība | lyginamojo matavimo laiko skirtumas
Barrage_code | Barrage | Бараж | Presa | Jez | Dæmning | Wehrstellung | Pais | Υδατοφράκτης | Barrage | Pregrada | sbarramento | Aizsprosts | Užtvara
Regime_code | Water regime | Воден режим | Régimen | Odtokový režim | Vandregime | Abflussregime | Veerežiim | Ροή υδάτων | Débit | Režim vodnog toka | regime idrico | Ūdens režīms | Vandens režimas
Measuredate | Measuredate | Дата на измерване | Fecha de medición | Datum měření | Dato for målingen | Messdatum | Mõõtmise kuupäev | Ημερομηνία μέτρησης | Date de mesure | Datum mjerenja | data del rilievo | Mērījuma datums | Matavimo data
Measuretime | Measuretime | Час на измерване | Hora de medición | Čas měření | Tidspunkt for målingen | Messzeit | Mõõtmise kellaaeg | Ώρα μέτρησης | Heure de mesure | Vrijeme mjerenja | orario del rilievo | Mērījuma laiks | Matavimo laikas
Icem | Ice message | Съобщения във връзка с ледохода | Mensaje hielo | Zpráva týkající se ledových jevů | Ismelding | Eismeldung | Teade jää kohta | Μήνυμα σχηματισμού πάγου | Message concernant la glace | Poruka o ledu | messaggio relativo alla presenza di ghiaccio | Ziņojums par ledu | Pranešimas apie ledą
Ice_condition | Ice condition on fairway | Състояние на леда | Estado hielo en vía navegable | Ledové podmínky | Isforhold for farvand | Eisverhältnisse im Fahrwasser | Jää seisund | Συνθήκες πάγου | Condition de glace | Stanje leda | condizione del ghiaccio sul canale navigabile | Ledus apstākļi | Ledo sąlygos farvateryje
Ice_condition_code | Ice condition | Код за състоянието на леда | Estado hielo | Ledové podmínky | Isforhold | Eisbeschaffenheit | Jää seisund | Συνθήκες πάγου | Condition de glace | Stanje leda | condizione del ghiaccio | Ledus apstākļi | Ledo sąlygos
Ice_accessibility_code | Accessibility | Условия за корабоплаване при наличие на ледоход | Accesibilidad | Splavnost | Farbarhed | Befahrbarkeit | Juurdepääsetavus | Προσβασιμότητα | Accessibilité | Plovnost | accessibilità | Pieejamība | Tinkamumas laivybai
Ice_classification_code | Ice classification | Класификация (описание) на леда | Clasificación hielo | Klasifikace ledu | Isklasse | Eisklasse | Jää klassifitseerimine | Ταξινόμηση πάγου | Classification de la glace | Klasifikacija leda | tipo di ghiaccio | Ledus klasifikācija | Ledo tipas
Ice_situation_code | Ice situation | Ледова обстановка | Situación hielo | Situace týkající se ledu | Issituation | Eissituation | Jää olukord | Κατάσταση πάγου | Limitations dues à la glace | Stanje leda | stato del ghiaccio | Ledus stāvoklis | Ledo būklė
Werm | Weather message | Съобщения за метеорологичната обстановка | Mensaje sobre condiciones meteorológicas | Zpráva o počasí | Vejrmeddelelse | Wettermeldung | Ilmasõnum | Μετεωρολογικό μήνυμα | Message météo | Vremenska poruka | messaggio meteorologico | Laikapstākļu ziņojums | Meteorologinis pranešimas
Weather_report | Weather report | Доклад за метеорологичната обстановка | Informe meteorológico | Stav počasí | Vejrrapport | Wetterbericht | Ilmateade | Μετεωρολογικό δελτίο | Bulletin météo | Vremenski izvještaj | bollettino meteorologico | Laikapstākļu pārskats | Meteorologinė suvestinė
Forecast | Forecast | Прогноза | Previsión | Předpověď | Forudsigelse | Vorhersage | Prognoos | Πρόγνωση | Prévision | Prognoza | previsioni meteorologiche | Prognoze | Prognozė
Weather_class_code | Weather classification | Класификация за метеорологичната обстановка | Clasificación de las condiciones meteorológicas | Klasifikace počasí | Vejrklassificering | Wetterklassifizierung | Ilma klassifitseerimine | Ταξινόμηση καιρού | Classification de la météo | Klasifikacija vremena | classificazione meteorologica | Laikapstākļu klasifikācija | Oro sąlygų kodas
Weather_item | Weather information | Информация за метеорологичната обстановка | Información de las condiciones meteorológicas | Jednotka počasí | Vejroplysninger | Wetterinformation | Ilmateave | Πληροφορίες καιρού | Point météo | Podatak o vremenu | informazioni meteorologiche | Laikapstākļu informācija | Meteorologinis parametras
Weather_item_code | Weather item | Код на елемента на метеорологичната обстановка | Elemento meteorológico | Jednotka počasí | Vejrelement | Wettergegenstand | Ilma komponent | Στοιχείο καιρού | Code du point météo | Kod podatka o vremenu | codice informazioni meteorologiche | Laikapstākļu elements | Meteorologinio parametro kodas
Value_min | Minimal value | Минимална стойност | Valor mínimo | Minimální hodnota | Minimumsværdi | Tiefstwert | Miinimumväärtus | Minimal value | Valeur minimale | Minimalna vrijednost | valore minimo | Minimālā vērtība | Minimali vertė
Value_max | Maximal value | Максимална стойност | Valor máximo | Maximální hodnota | Maksimumsværdi | Höchstwert | Maksimumväärtus | Μέγιστη τιμή | Valeur maximale | Maksimalna vrijednost | valore massimo | Maksimālā vērtība | Maksimali vertė
Value_gusts | Gusts value | Стойност на поривите на вятъра | Valor ráfagas | Nárazová hodnota | Vindstødsværdi | Spitzenwert | Puhangute tugevus | Τιμή ριπών ανέμου | Valeur des rafales | Vrijednost udara vjetra | valore delle raffiche | Vēja brāzmu vērtība | Gūsių vertė
Weather_category_code | Weather category | Категория на метеорологичната обстановка | Categoría meteorológica | Kategorie počasí | Vejrkategori | Wetterkategorie | Ilma kategooria | Κατηγορία καιρού | Catégorie météo | Kategorija vremena | categoria condizioni meteorologiche | Laikapstākļu kategorija | Oro sąlygų kategorija
Direction_code_min | Direction from | Направление от | Dirección de | Směr od | Retning fra | Richtung von | Lähtesuund | Διεύθυνση από | Direction de | Smjer od | direzione da | Virziens no | Kryptis nuo
Direction_code_max | Direction to | Направление към | Dirección a | Směr k (ku) | Retning mod | Richtung bis | Sihtsuund | Διεύθυνση προς | Direction vers | Smjer prema | direzione verso | Virziens uz | Kryptis iki
ETICHETE
Eticheta XML | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
RIS_message | NtS üzenet | Messaġġ tal-NtS | NtS-bericht | Komunikat NtS | Mensagem NtS | Mesaj NtS | Správa NtS | sporočilo NtS | NtS-sanoma | NtS-meddelande | Сообщение NtS | NtS порука
Identification | Azonosítási szakasz | Sezzjoni ta’ identifikazzjoni | Identificatiesectie | Sekcja identyfikacyjna | Secção identificação | Element de identificare | Identifikačná sekcia | segment za identifikacijo | Tunnisteosio | Identifieringsavsnitt | Идентификация | (Идентификациони део)
From | Az üzenet feladója | Speditur tal-messaġġ | Afzender van het bericht | Nadawca | Remetente | Expeditorul mesajului | Odosielateľ správy | pošiljatelj sporočila | Sanoman lähettäjä | Avsändare | Отправитель | Пошиљалац поруке
Originator | Az információ forrása | Oriġinatur tal-informazzjoni | Oorsprong van de informatie | Autor informacji | Autor | Autorul informațiilor | Pôvodca správy | izvor informacije | Tiedon lähde | Uppgiftslämnare | Источник информации | Порекло-извор информације
Country_code | Az ország, amelyben az üzenet érvényes | Pajjiż fejn il-messaġġ huwa validu | Land waar het bericht geldt | Kraj, którego dotyczy komunikat | País em que a mensagem é válida | Țara în care mesajul este valabil | Krajina platnosti správy | država, v kateri je sporočilo veljavno | Maa, jota sanoma koskee | Berört land | Код страны сообщения | Држава у којој порука важи
Language_code | Eredeti nyelv | Lingwa oriġinali | Oorspronkelijke taal | Język oryginału | Língua original | Limba de origine | Originálny jazyk | izvirni jezik | Alkuperäkieli | Originalspråk | Язык сообщения | Изворни језик
District | Az országon belüli terület/ régió | Distrett/reġjun fil-pajjiż | District/regio in een land | Region kraju | Divisão administrativa (do país) | Regiune | Región | okrožje/regija znotraj države | Kyseinen alue maassa | Distrikt/region | Область в стране | Област-регион у држави
Date_issue | Kiadás dátuma | Data tal-ħruġ | Datum van uitgifte | Data nadania | Data de emissão | Data emiterii | Dátum vydania | datum izdaje | Antamispäivä | Datum för utfärdande | Дата составления | Датум издавања
Time_issue | Kiadás ideje | Ħin tal-ħruġ | Tijd van uitgifte | Godzina nadania | Hora de emissão | Ora emiterii | Čas vydania | čas izdaje | Antamisaika | Tidpunkt för utfärdande | Время составления | Време издавања
Ftm | Hajósoknak szóló hirdetmény | Messaġġ relatat mal-kanali navigabbli u t-traffiku | Bericht met betrekking tot vaarwegen en verkeer | Komunikat dotyczący toru wodnego i ruchu | Mensagem via navegável e tráfego | Aviz către navigatori | Správa týkajúca sa vodnej cesty a premávky | sporočilo v zvezi s plovno potjo in prometom | Väylää tai liikennettä koskeva sanoma | Farleds- och trafikrelaterat meddelande | Сообщения касательно фарватера и движения судов | Порука у вези са пловним путем и саобраћајем
NtS_number | Számozási szakasz | Sezzjoni tan-numru | Nummersectie | Numer sekcji | Secção relativa ao número | Numărul avizului către navigatori | Číslo | segment za številko | Sanoman numero | Numreringsavsnitt | Номер извещения |
Organisation | Közzétevő szervezet | Organizzazzjoni pubblikatriċi | Uitgevende organisatie | Organ wydający | Organização de publicação | Organizația | Vydávajúca organizácia | organizacija, ki objavi sporočilo | Organisaatio | Utfärdare | Организация |
Year | Év | Sena | Jaar | Rok | Ano | Anul | Rok | leto | Vuosi | År | год | Година
Number | (A hirdetmény száma) | Numru (tal-avviż) | Nummer (van het bericht) | Numer (komunikatu) | Número (do aviso) | Numărul (avizului) | Číslo správy | številka (obvestila) | (Ilmoituksen) numero | (Meddelandets) nummer | номер | Број (Саопштења)
Serial_number | Sorozatszám | Numru tas-serje | Serienummer | Numer kolejny (wersji) | Número de série | Numărul de serie | Číslo verzie (série) | zaporedna številka | Sarjanumero | Serienummer | серийный номер | Серијски број
Target_group | Célcsoport szakasz | Informazzjoni dwar il-grupp fil-mira | Informatie over de doelgroep | Informacje o grupie odbiorców | Secção grupo-alvo | Grupul de utilizatori avuți în vedere | Informácie o cieľovej skupine | segment za ciljno skupino | Kohderyhmäosio | Målgrupp | группа получателей | (Део циљне групе)
Target_group_code | Célcsoport kód | Grupp fil-mira | Doelgroep | Kod grupy odbiorców | Código grupo-alvo | Codul grupului de utilizatori avuți în vedere | Cieľová skupina | koda ciljne skupine | Kohderyhmäkoodi | Kod för målgrupp | код группы получателей | Код циљне групе
Direction_code | Forgalmi irány kód | Direzzjoni affettwata | Desbetreffende richting | Kod kierunku ruchu | Sentido do tráfego | Codul sensului de circulație | Dotknutý smer | koda usmerjanja prometa | Liikenteen suunnan koodi | Kod för trafikriktning | код направления движения | Код смера пловидбе
Subject_code | Tárgy | Suġġett | Onderwerp | Temat | Matéria | Subiectul avizului | Predmet | predmet | Aihe | Ämne | тема сообщения | Код предмета
Validity_period | Érvényességi időszak | Perjodu ta’ validità | Geldigheidsperiode | Okres ważności | Período de validade | Perioada de valabilitate | Doba platnosti | čas veljavnosti | Voimassaolo | Giltighetsperiod | срок действия | Рок важности
Date_start | Tól | Minn | Vanaf | od | De | Data de început | Od | od | Alkaa | Från | дата начала | Од (yyyymmdd)
Date_end | Ig | Sa | Tot | do | A | Data de sfârșit | Do | do | Päättyy | Till | дата окончания | До (yyyymmdd)
Contents | Tartalom | Informazzjoni addizzjonali | Aanvullende informatie | Treść | Conteúdo | Conținut | Text / Obsah | dodatne informacije | Sisältö | Innehåll | содержание | Садржај
Source | A hirdetmény kibocsátója (hatóság) | Sors tal-avviż (awtorità) | Bron van het bericht (autoriteit) | Źródło komunikatu (organ) | Fonte do aviso (autoridade) | Sursa avizului (autoritatea) | Zdroj správy | izvor obvestila (organ) | Ilmoituksen lähde (viranomainen) | Källa (myndighet) | Источник информации (официальный) | Извор Саопштења (орган)
Reason_code | A hirdetmény indoka | Raġuni għall-avviż | Reden van het bericht | Przyczyna komunikatu | Motivo do aviso | Codul evenimentului | Dôvod správy | razlog za obvestilo | Ilmoituksen syy | Orsak till meddelandet | Причина извещения | Разлог Саопштења
Communication | Kommunikációs csatorna info szakasz | Informazzjoni ta’ komunikazzjoni | Communicatie-informatie | Informacje o kanale łączności | Secção comunicação | Mijloc de comunicație | Informácie o komunikačnom kanáli | segment za sporočila | Viestintäosio | Kommunikationsavsnitt | Информация о средствах связи | Информације о комуникационом каналу
Reporting_code | A jelentést küldő rendszer | Sistema ta’ rappurtar | Meldingsregime | Sposób meldowania | Regime de transmissão | Modul de raportare | Režim hlásení | način poročanja | Raportointijärjestelmä | Rapporteringsordning | Необходимость ответного сообщения | Режим извештавања
Communication_code | Kommunikációs eszköz | Mezz ta’ komunikazzjoni | Communicatiemiddel | Środek łączności | Meio de comunicação | Codul mijlocului de comunicație | Komunikačné prostriedky | komunikacijska sredstva | Viestintävälineet | Kommunikationsmedel | Средства связи | Средство комуникације
Number (Communication section) | Szám vagy cím | Numru jew indirizz | Nummer of adres | Numer lub adres | Número ou endereço | Numărul adresei | Číslo alebo adresa | številka ali naslov | Numero tai osoite | Nummer eller adress | Контакты для связи | Број или адреса
Fairway_section | Víziút vagy hajóút szakasz | Passaġġ fuq l-ilma jew sezzjoni ta’ passaġġ fuq l-ilma | Waterweg of waterwegsectie | Odcinek kanału żeglownego lub toru wodnego | Via navegável ou troço | Secțiunea de cale navigabilă sau șenal | Vodná cesta (alebo úsek plavebnej dráhy) | vodna pot ali odsek vodne poti | Vesiväylä tai väylänosa | Vattenväg eller avsnitt av vattenväg | Участок фарватера или навигационного пути | Деоница водног или пловног пута
Geo_object | a víziút vagy objektum geo információja | Pożizzjoni | Locatie | Dane geograficzne kanału żeglownego lub obiektu | Dados geográficos via navegável ou objeto | Informația geografică despre calea navigabilă sau obiect | Geografické informácie o vodnej ceste alebo o objekte | geo-informacije o vodni poti ali objektu | vesiväylän tai kohteen maantieteelliset tiedot | Geografisk information om vattenväg eller objekt | информация по данной части фарватера или навигационного пути | (Гео информација o водном путу или објекту)
Id (Geo_Object section) | Azonosítás | Kodiċi tal-Pożizzjoni ISRS | ISRS-locatiecode | Oznaczenie | Identificação | Identificator | Kód lokality ISRS | identifikacija ISRS | Tunnistetiedot | Identifiering | Обозначение | Идентификација
Name (Geo_Object section) | A földrajzi objektum neve | Isem l-oġġett | Naam van het object | Nazwa obiektu geograficznego | Designação do objeto georreferenciado | Numele obiectului geografic | Názov objektu | ime geo-objekta | Maantieteellisen kohteen nimi | Namn på geografiskt objekt | Название объекта | Назив гео објекта
Type_code (Geo_Object section) | Objektum típusa | Tip | Type | Typ obiektu | Tipo de via navegável | Tipul obiectului | Typ objektu | vrsta vodne poti | Vesiväylän tyyppi | Typ av vattenväg | Тип объекта | Тип гео објекта
Coordinate | A hajóút kezdetének és végének koordinátái | Koordinati | Coördinaten | Współrzędne początku i końca toru wodnego | Coordenadas extremos via navegável | Coordonatele începutului și sfârșitului secțiunii | Súradnice | koordinate začetka in konca plovne poti | Väylän alku- ja loppukoordinaatit | Koordinater | Координаты начала и окончания части фарватера или навигационного пути | Почетне и крајње координате пловног пута
Lat (Coordinate) | Szélesség (decimális) | Latitudni | Breedtegraad | Szerokość (do dziesiętnej) | Latitude (decimal) | Latitudine (fracțiuni zecimale) | Zemepisná šírka (desatinné číslo) | zemljepisna širina | Leveysaste (desimaaliluku) | Latitud (decimal) | Широта | Географска ширина (децимално)
Long (Coordinate) | Hosszúság (decimális) | Lonġitudni | Lengtegraad | Długość (do dziesiętnej) | Longitude (decimal) | Longitudine (fracțiuni zecimale) | Zemepisná dĺžka (desatinné číslo) | zemljepisna dolžina | Pituusaste (desimaaliluku) | Longitud (decimal) | Долгота | Географска дужина (децимално)
Limitation | Korlátozott szakasz | Restrizzjoni | Beperking | Informacje o ograniczeniach | Secção restrições | Limitarea secțiunii | Obmedzenie | segment za omejitve | Rajoitusosio | Begränsningsavsnitt | Раздел ограничений | Ограничење
Limitation_period | Korlátozási időszak/időtartam/időköz | Perjodi/intervalli ta’ (restrizzjoni) | Periode/tussentijd (van de beperking) | Czas obowiązywania ograniczeń | Restrição (período/intervalo) | Durata limitării | Čas (obdobie) obmedzenia | (omejitev) obdobja/intervali | (Rajoitus-)jaksot/aikavälit | (Begränsning) perioder/intervaller | срок/интервал действия ограничений | (Ограничење) период/интервал
Date_start (Limitation_period) | Tól | Minn | Vanaf | od | De | Data începerii | Od | od | Alkaa | Från | начало действия ограничения | Од (yyyymmdd)
Date_end (Limitation_period) | Ig | Sa | Tot | do | A | Data sfârșirii | Do | do | Päättyy | Till | Дата окончания действия ограничения | До (yyyymmdd)
Time_start (Limitation_period) | Tól (óra, perc) | Minn (hh:mm) | Vanaf (hh:mm) | od (hhmm) | De (hhmm) | Ora începerii (oomm) | Od (hhmm) | od (hhmm) | Alkaa (hhmm) | Från (hhmm) | Время (ччмм) начала | Од (hhmm)
Time_end (Limitation_period) | Ig (óra, perc) | Sa (hh:mm) | Tot (hh:mm) | do (hhmm) | A (hhmm) | Ora terminării (oomm) | Do (hhmm) | do (hhmm) | Päättyy (hhmm) | Till (hhmm) | Время (ччмм) окончания | До (hhmm)
Interval_code (Limitation_period) | Időköz | Intervall | Tussentijd | Okres | Intervalo | Interval | Interval | interval | Aikaväli | Intervall | Период ограничения | Интервал
Limitation_code | Korlátozás jellege | Tip ta’ restrizzjoni | Soort beperking | Rodzaj ograniczenia | Tipo de restrição | Felul limitării | Druh obmedzenia | vrsta omejitve | Rajoituksen laatu | Typ av begränsning | Тип ограничения | Тип ограничења
Position_code | Korlátozás helye | Pożizzjoni | Positie | Położenie ograniczenia | Localização (da restrição) | Poziția | Poloha | položaj | (Rajoituksen) sijainti | (Begränsningens) position | Местоположение | Позиција (ограничења)
Value | Korlátozás számértéke | Valur numeriku | Numerieke waarde | Wartość numeryczna (ograniczenia) | Valor numérico (da restrição) | Valoare numerică | Číselná hodnota | numerična vrednost | (Rajoituksen) numeroarvo | (Begränsningens) numeriska värde | Величина ограничения | Нумеричка вредност (ограничења)
Unit | Mértékegység | Unità | Eenheid | jednostka | Unidade | Unitate | Jednotka | enota | Yksikkö | Enhet | Единица измерения величины |
Fairway_name | Vízi út | Passaġġ fuq l-ilma | Waterweg | Nazwa toru wodnego | Via navegável | Numele căii navigabile | Vodná cesta | vodna pot | Vesiväylän nimi | Vattenväg | Обозначение водного пути |
Reference_code | Egység | Referenza għall-valur | Waarde referentie | Układ odniesienia | Referência | Valoare de referință | Referencia | vrednost reference | Arvon referenssi | Referensvärde | Эталонная величина | Референтна вредност
Indication_code | Korlátozás jelzése | Indikazzjoni tar-restrizzjoni | Indicatie van de beperking | Oznaczenie ograniczenia | Indicação da restrição | Cod de indicare | Indikácia obmedzenia | označitev omejitve | (Rajoituksen) osoitus | Uppgift om begränsning | Индикация ограничения | Индикација ограничења
Object | Objektum | Oġġett | Object | Obiekt | Objeto | Obiect | Objekt | objekt | Kohde | Objekt | Объект | Објекат
Geo_object section for an Object | Az objektum földrajzi adatai | Pożizzjoni | Locatie | Dane geograficzne obiektu | Dados geográficos do objeto | Poziționarea obiectului | Geografické informácie o objekte | geo-informacije o vodni poti ali objektu | kohteen maantieteelliset tiedot | Geografisk information om objekt | Геоинформация об объекте | (Гео информације објекта)
Type_code (Geo_object section) | Objektum típusa | Tip ta’ oġġett | Soort object | Rodzaj obiektu | Tipo de objeto | Tipul obiectului | Typ objektu | vrsta objekta | kohteen tyyppi | Typ av objekt | Тип объекта | Тип гео објекта
Coordinate (Geo_object section) | Objektum koordinátái | Koordinati tal-oġġett | Coördinaten van het object | Współrzędne obiektu | Coordenadas do objeto | Coordonatele obiectului | Súradnice objektu | koordinate objekta | Kohteen koordinaatit | Objektets koordinater | Координаты объекта | Координате објекта
Wrm | Vízállás jelentés | Messaġġ relatat mal-ilma | Bericht met betrekking tot de waterstand | Komunikat dotyczący stanu wody | Mensagem relativa à água | Date despre apă | Správa o vodnom stave | sporočilo v zvezi z vodo | Vedenkorkeuteen liittyvä sanoma | Meddelande om vattennivån | Информация об уровне воды | Порука у вези са водостајем
Measure | Értékek meghatározása (mért v. előrejelzett) | Kejl (valuri normali jew imbassar) | Meetwaarden (normaal of voorspeld) | Rodzaj wartości (pomiar czy prognoza) | Valores (reais ou previstos) | Secțiunea de măsurare | Merania (normálne alebo predpovedané) | meritve (običajne ali predvidene) | Mittaukset (normaalit tai ennusteet) | Mätning (mätvärde eller beräkning) | Значение уровня воды (фактическое или ожидаемое) | Мерења (стварна или прогноза)
Predicted | Előrejelzés | Tbassir | Voorspelling | Prognoza | Previsão | Prognozat | Predpoveď | predvidevanje | Ennuste | Beräkning | Прогноз | Прогноза
Measure_code | A vízállás információ fajtája | Tip ta’ informazzjoni relatata mal-ilma | Soort informatie over de waterstand | Rodzaj komunikatu o stanie wody | Tipo de informação relativa à água | Codul măsurătorilor | Druh správy o vodnom stave | informacije v zvezi z vrsto vode | Veteen liittyvän sanoman laji | Typ av meddelande om vattennivån | Тип информации об уровне воды | Врста информације у вези са водостајем
Difference | Eltérés | Differenza bi tqabbil mal-valur preċedenti | Verschil t.o.v. de vorige meting | Różnica | Diferença | Diferența | Rozdiel voči predchádzajúcej hodnote | razlika | Ero | Skillnad | Разница | Разлика
Value_difference | Értékbeli eltérés az összehasonlító méréshez képest | differenza fil-valur bi tqabbil mal-kejl kumparattiv | Waardeverschil t.o.v. vergelijkbare meting | Różnica wartości | Diferença de valor em relação à medição comparativa | Diferență de valoare | Rozdiel voči porovnávaciemu meraniu | razlika v vrednosti glede na primerjalno meritev | arvon ero vertailukelpoiseen mittaukseen nähden | Skillnad i värde mot jämförande mätning | Разница значений для сравнительной оценки |
Time_difference | Időbeli eltérés az összehasonlító méréshez képest | differenza fil-ħin bi tqabbil mal-kejl kumparattiv | Tijdsverschil t.o.v. vergelijkbare meting | Różnica czasu | Diferença horária em relação à medição comparativa | Interval de timp | Časový rozdiel voči porovnávaciemu meraniu | razlika v času glede na primerjalno meritev | aikaero vertailukelpoiseen mittaukseen nähden | Skillnad i tid mot jämförande mätning | Временное различие для сравнительной оценки |
Barrage_code | Duzzasztómű | Milqgħa | Stuw | Stan zapory | Barragem | Baraj | Hať | zapora | Avattava pato | Fördämning | Плотина | Преграда
Regime_code | Vízjárás | Rata tal-fluss tal-ilma | Waterregime | Stan wody | Regime | Nivelul apei | Vodný režim | vodni režim | Vedenkorkeussuhteet | Vattenordning | Водный режим | Водни режим
Measuredate | Mérés dátuma | Data tal-kejl | Meetdatum | Data pomiaru | Data medição | Data măsurării | Dátum merania | datum merjenja | Mittauspäivä | Datum för mätning | Дата измерения | Датум мерења (yyyymmdd)
Measuretime | Mérés időpontja | Ħin tal-kejl | Meettijd | Godzina pomiaru | Hora medição | Ora măsurării | Čas merania | čas merjenja | Mittausaika | Tidpunkt för mätning | Время измерения | Време мерења (hhmm)
Icem | Jégjelentés | Messaġġ dwar is-silġ | IJsbericht | Komunikat o lodzie | Mensagem gelo | Date privind gheața | Správy o ľadochode | sporočilo o ledu | Jäätilannetta koskeva sanoma | Meddelande om isförhållanden | Ледовые сообщения | Порука у вези са ледом
Ice_condition | Jégállapot | Kundizzjoni tas-silġ fuq il-kanal navigabbli | IJsconditie op de vaarweg | Lód | Estado do gelo | Condițiile gheții | Ľadové podmienky | stanje ledu na plovni poti | Jäätilanne | Isförhållanden | Ледовые условия | Стање леда
Ice_condition_code | Jégállapot | Kundizzjoni tas-silġ | IJsconditie | Stan lodu | Estado do gelo | Condițiile gheții | Ľadové podmienky | stanje ledu | Jäätilanne | Isförhållanden | Ледовая обстановка | Стање леда
Ice_accessibility_code | Hajózhatóság | Aċċessibbiltà | Toegankelijkheid | Dostępność | Acessibilidade | Accesibilitate | Dostupnosť | dostopnost | Ajettavuus | Farbarhet | Условия плавания во льдах | Пловност у условима леда
Ice_classification_code | Jég osztályozás | Klassifikazzjoni tas-silġ | IJsclassificatie | Klasyfikacja lodu | Classificação do gelo | Clasificarea gheții | Klasifikácia ľadochodu | klasifikacija ledu | Jään luokittelu | Isklassificering | Тип плавания во льдах | Класификација леда
Ice_situation_code | Jéghelyzet | Sitwazzjoni tas-silġ | IJssituatie | Sytuacja lodowa | Restrições devidas à presença de gelo | Starea gheții | Situácia ľadochodu | položaj ledu | Jäätilanne | Isläge | Ограничения плавания во льдах | Стање пловидбе у случају леда
Werm | Időjárás üzenet | Messaġġ relatat mat-temp | Bericht met betrekking tot het weer | Komunikat pogodowy | Mensagem meteorológica | Mesaj meteo | Správa o počasí | sporočilo o vremenu | Sääsanoma | Vädermeddelande | Метеорологические сообщения | Поруке у вези времена
Weather_report | Időjárás jelentés | Rapport tat-temp | Weerbericht | Raport pogodowy | Boletim meteorológico | Buletin meteo | Stav počasia | vremensko poročilo | Sääraportti | Väderrapport | Метеосводка | Извештај о времену
Forecast | Előrejelzés | Tbassir | Voorspelling | Prognoza | Previsão meteorológica | Prognoză | Predpoveď | napoved | Ennuste | Prognos | Прогноз | Прогноза
Weather_class_code | Időjárás besorolás | Klassifikazzjoni tat-temp | Weerclassificatie | Klasyfikacja pogody | Classificação meteorológica | Clasificarea vremii | Klasifikácia počasia | klasifikacija vremena | Sään luokittelu | Väderklassificering | Классификация метеоусловий | Класификација времена
Weather_item | Időjárás elem | Informazzjoni dwar it-temp | Weersinformatie | Prognoza pogody | Informação meteorológica | Felul vremii | Informácie o počasí | informacije o vremenu | Säätiedot | Väderinformation | Метеорологические элементы | Податак о времену
Weather_item_code | Időjárás elem kód | Attribut tat-temp | Weerelement | Przedmiot pogody | Elemento meteorológico | Componentă meteo | Predmet počasia | vremenski pojav | Sääelementti | Väderparameter | Тип метеорологического элемента | Код податка о времену
Value_min | Legkisebb érték | Valur minimu | Minimumwaarde | Wartość minimalna | Valor mínimo | Valoarea minimă | Minimálna hodnota | najnižja vrednost | Alin arvo | Minimivärde | Величина на данный момент или минимальная величина | Минимална вредност
Value_max | Legnagyobb érték | Valur massimu | Maximumwaarde | Wartość maksymalna | Valor máximo | Valoarea maximă | Maximálna hodnota | najvišja vrednost | Ylin arvo | Maximivärde | Максимальная величина | Максимална вредност
Value_gusts | Csúcsérték | Valur tal-buffuri riħ | Windvlagen | Wartość podmuchu | Valor rajadas de vento | Valoarea în rafale | Nárazová hodnota | moč sunkov | Tuulen puuska | Värde för vindbyar | Величина порывов ветра | Јачина удара ветра
Weather_category_code | Időjárás típus | Kategorija tat-temp | Weercategorie | Kategoria pogody | Categoria meteorológica | Categoriile vremii | Kategória počasia | kategorija vremena | Säätyyppi | Väderkategori | Категория метеоусловий | Код категорије времена
Direction_code_min | Irányba | Direzzjoni minn | Vanuit richting | Z kierunku | Direção de | Direcția de la | Smer od | iz | Suunta (mistä) | Riktning från | Направление (ветра или волны) от | Смер од
Direction_code_max | Irányból | Direzzjoni lejn | Naar richting | W kierunku | Direção para | Direcția către | Smer k | v | Suunta (mihin) | Riktning mot | Направление (ветра или волны) к | Смер до
CODUL BARAJULUI
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
CLD | Barrage Closed | Баражът е затворен | Presa cerrada | jez je uzavřen | Dæmning er lukket | Wehr ist geschlossen | Pais suletud | Κλειστός υδατοφράκτης | Barrage relevé | Brana zatvorena | sbarramento chiuso | Aizsprosts slēgts | Užtvara uždaryta
OPG | Barrage Opening | Баражът се отваря | Apertura de presa | jez se otvírá | Dæmning åbner | Wehr wird geöffnet | Paisu avamine | Υδατοφράκτης σε φάση ανοίγματος | Barrage se couchant | Brana se otvara | sbarramento in fase di apertura | Aizsprosts atveras | Užtvara atidaroma
CLG | Barrage Closing | Баражът се затваря | Cierre de presa | jez se zavírá | Dæmning lukker | Wehr wird geschlossen | Paisu sulgemine | Υδατοφράκτης σε φάση κλεισίματος | Barrage se relevant | Brana se zatvara | sbarramento in fase di chiusura | Aizsprosts aizveras | Užtvara uždaroma
OPD | Barrage Opened, no navigation through barrage | Баражът е отворен, но преминаването е забранено | Presa abierta, paso prohibido | jez je otevřen, zákaz plavby přes jez | Dæmning er åben, men gennemsejling er forbudt | Wehr ist geöffnet, keine Schifffahrt durch/über das Wehr | Pais avatud, laevatamist paisu kaudu ei toimu | Ανοικτός υδατοφράκτης, απαγόρευση ναυσιπλοΐας μέσω υδατοφράκτη | Barrage fermé à la navigation | Brana otvorena, nije dopuštena plovidba | sbarramento aperto, nessun transito consentito | Aizsprosts atvērts, kuģošana caur aizsprostu aizliegta | Užtvara atidaryta, laivyba draudžiama
OPN | Barrage laid, opened for navigation through barrage | Баражът е отворен за плаване | Presa abierta, paso autorizado | jez je pro plavbu otevřen | Dæmning er åben for sejlads | Wehr ist geöffnet, Schifffahrt durch/über das Wehr | Pais avatud laevatmiseks | Ανοικτός υδατοφράκτης, επιτρέπεται η ναυσιπλοΐα | Barrage ouvert à la navigation | Brana otvorena za plovidbu | sbarramento aperto, transito consentito | Aizsprosts atvērts kuģošanai caur aizsprostu | Užtvara atidaryta laivybai
CODUL BARAJULUI
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
CLD | Duzzasztómű zárva | Milqgħa Magħluqa | Stuw is gesloten | Zapora zamknięta | Barragem fechada | Baraj închis | hať je zatvorená | zapora zaprta | Avattava pato suljettu | Fördämningen stängd | Плотина закрыта | Преграда затворена
OPG | Duzzasztóművet nyitják | Milqgħa Qed Tinfetaħ | Stuw wordt geopend | Otwieranie zapory | Barragem a abrir | Baraj în deschidere | hať sa otvára | odpiranje zapore | Avattava pato avautuu | Fördämningen öppnas | Плотина открывается | Преграда се отвара
CLG | Duzzasztóművet zárják | Milqgħa Qed Tingħalaq | Stuw wordt gesloten | Zamykanie zapory | Barragem a fechar | Baraj în închidere | hať sa zatvára | zapiranje zapore | Avattava pato sulkeutuu | Fördämningen stängs | Плотина закрывается | Преграда се затвара
OPD | Duzzasztómű nyitva, de áthajózás a duzzasztóművön nem megengedett | Milqgħa Miftuħa, navigazzjoni minn ġol-milqgħa projbita | Stuw is geopend, maar geen doorvaart via stuw | Zapora otwarta, zamknięta dla żeglugi | Barragem aberta, passagem proibida | Baraj deschis, nu se navighează | hať je otvorená, preplávanie cez hať zakázané | zapora odprta, plovba skozi zaporo ni dovoljena | Avattava pato avattu, ei vesiliikennettä padon kautta | Fördämningen öppen, men sjöfart förbjuden | Плотина открыта, но движение судов запрещено | Преграда отворена
OPN | Duzzasztómű az áthajózás számára megnyitva | Milqgħa mifruxa, tista’ ssir navigazzjoni minn ġol-milqgħa | Stuw is geopend voor scheepvaart via stuw | Zapora otwarta dla żeglugi | Barragem aberta, passagem autorizada | Baraj deschis pentru navigație | hať je otvorená pre plavbu | zapora postavljena, odprta za plovbo skozi zaporo | Avattava pato avattu liikenteelle | Fördämningen öppen för sjöfart | Плотина открыта для движения судов | Преграда спуштена, пловидба слободна
COD DE COMUNICAȚII
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
TE | telephone | Телефон | Teléfono | telefon | Telefon | Telefon | Telefon | Τηλέφωνο | Téléphone | Telefon | telefono | Tālrunis | Telefonas
AP | VHF | Метров обхват | VHF | VKV | VHF | UKW | VHF | VHF | VHF | VHF | VHF | UĪV | VHF
EM | e-mail | Електронна поща (e-mail) | Correo electrónico | E-mail | E-mail | E-Mail | E-post | Ηλεκτρονικό ταχυδρομείο | e-mail | E-mail | e-mail | e-pasts | E. paštas
AH | internet | Интернет | Internet | Internet | Internet | Internet | Internet | Διαδίκτυο | Internet | Internet | Internet | Internets | Internetas
TT | teletext | Телетекст | Teletexto | Teletext | Teletekst | Teletext | Teletekst | Tελετέξτ | Télétexte | Teletekst | teletesto | Teleteksts | Teletekstas
FX | telefax | Факс | Fax | Fax | Telefax | Telefax | Telefaks | Τηλεομοιοτυπία | Télécopie | Telefaks | telefax | Telefakss | Telefaksas
LS | light signalling | Светлинна сигнализация | Señal luminosa | světelná signalizace | Lyssignal | Lichtsignal | Valgus-signaalid | Φωτεινή σηματοδότηση | signalisation lumineuse | Svjetlosna signalizacija | segnalazione con fanali | Gaismas signāli | Šviesos signalai
FS | flag signalling | Флагова сигнализация | Bandera | vlajková signalizace | Flagsignal | Flaggensignal | Lipu-signaalid | Σήματα με σημαίες | pavillon | Signalizacija zastavama | segnalazione con bandiere | Signāli ar karodziņiem | Signalai vėliavėlėmis
SO | sound signalling | Звукова сигнализация | Señal acústica | zvuková signalizace | Lydsignal | Tonsignal | Heli-signaalid | Ηχητικά σήματα | signalisation sonore | Zvučna signalizacija | segnalazione acustica | Skaņas signāli | Garsiniai signalai
EI | EDI mailbox number | Номер на пощенската кутия EDI | Número de buzón EDI | číslo EDI schránky | EDI-mailboksnummer | EDI Mailbox Nummer | EDI postkasti number | Αριθμός ηλεκτρονικής θυρίδας EDI | Numéro de boîte EDI | EDI broj pretinca | casella postale EDI | EDI pastkastītes numurs | EDI pašto dėžutės numeris
COD DE COMUNICAȚII
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
TE | telefon | telefown | Telefoon | Telefon | Telefone | telefon | Telefón | telefon | Puhelin | Telefon | Телефон | Телефон
AP | rádiótelefon | VHF | Marifoon | VHF | VHF | VHF | VHF | VHF | VHF | VHF | Радиосвязь на ОВЧ | VHF
EM | e-mail | posta elettronika | E-mail | E-mail | Correio eletrónico | e-mail | E-mail | e-pošta | Sähköposti | E-post | E-mail | E-mail
AH | Internet | internet | Internet | Internet | Internet | internet | Internet | internet | Internet | Internet | Интернет | Интернет
TT | teletext | teletext | Teletekst | Teletekst | Teletexto | teletext | Teletex | teletekst | Tekstitelevisio | Teletext | Телетекст | Телетекст
FX | telefax | telefax | Fax | Telefaks | Telefax | telefax | Telefax | telefaks | Faksi | Fax | Факс | Телефакс
LS | fényjelzés | sinjalar bid-dawl | Lichtsignaal | sygnalizacja świetlna | Sinal luminoso | semnal luminos | svetelná signalizácia | svetlobno signaliziranje | valo-opasteet | Ljus-signalering | Световые сигналы | Светлосна сигнализација
FS | lobogójelzés | sinjalar bil-bnadar | Vlagsignaal | sygnalizacja flagowa | Sinal de bandeira | semnal cu stegulețe | vlajková signalizácia | signaliziranje z zastavicami | lippuopasteet | Flagg-signalering | Сигналы флагами | Сигнализација заставом
SO | hangjelzés | sinjalar bil-ħoss | Geluidssein | sygnalizacja dźwiękowa | Sinal sonoro | semnal sonor | zvuková signalizácia | zvočno signaliziranje | ääniopasteet | Ljud-signalering | Звуковые сигналы | Звучна сигнализација
EI | EDI postafiók szám | Numru tal-kaxxa postali EDI | EDI-mailboxnummer | Numer skrzynki pocztowej EDI | Número caixa postal EDI | număr căsuță poștală EDI | číslo schránky EDI | Številka poštnega predala EDI | EDI mailbox-numero | EDI-postlådenummer | Номер почтового ящика EDI | Број EDI сандучета
CODUL ȚĂRII
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
AT | Austria | Австрия | Austria | Rakousko | Østrig | Österreich | Austria | Αυστρία | Autriche | Austrija | Austria | Austrija | Austrija
BE | Belgium | Белгия | Bélgica | Belgie | Belgien | Belgien | Belgia | Βέλγιο | Belgique | Belgija | Belgio | Beļģija | Belgija
BG | Bulgaria | България | Bulgaria | Bulharsko | Bulgarien | Bulgarian | Bulgaaria | Βουλγαρία | Bulgarie | Bugarska | Bulgaria | Bulgārija | Bulgarija
CH | Switzerland | Швейцария | Suiza | Švýcarsko | Schweiz | Schweiz | Šveits | Ελβετία | Suisse | Švicarska | Svizzera | Šveice | Šveicarija
RS | Serbia | Сърбия | Serbia | Srbsko | Serbien | Serbien | Serbia | Σερβία | Serbie | Srbija | Serbia | Serbija | Serbija
CY | Cyprus | Кипър | Chipre | Kypr | Cypern | Zypern | Küpros | Κύπρος | Chypre | Cipar | Cipro | Kipra | Kipras
CZ | Czech Republic | Република Чехия | Chequia | Česká republika | Tjekkiet | Tschechien | Tšehhi Vabariik | Τσεχική Δημοκρατία | République Tchèque | Češka | Repubblica ceca | Čehija | Čekija
DE | Germany | Германия | Alemania | Německo | Tyskland | Deutschland | Saksamaa | Γερμανία | Allemagne | Njemačka | Germania | Vācija | Vokietija
DK | Denmark | Дания | Dinamarca | Dánsko | Danmark | Dänemark | Taani | Δανία | Danemark | Danska | Danimarca | Dānija | Danija
EE | Estonia | Естония | Estonia | Estonsko | Estland | Estland | Eesti | Εσθονία | Estonie | Estonija | Estonia | Igaunija | Estija
ES | Spain | Испания | España | Španělsko | Spanien | Spanien | Hispaania | Ισπανία | Espagne | Španjolska | Spagna | Spānija | Ispanija
FI | Finland | Финландия | Finlandia | Finsko | Finland | Finnland | Soome | Φινλανδία | Finlande | Finska | Finlandia | Somija | Suomija
FR | France | Франция | Francia | Francie | Frankrig | Frankreich | Prantsusmaa | Γαλλία | France | Francuska | Francia | Francija | Prancūzija
GB | United Kingdom | Великобритания | Reino Unido | Velká Británie | Det Forenede Kongerige | Großbritannien | Ühend-kuningriik | Ηνωμένο Βασίλειο | Royaume-Uni | Ujedinjena Kraljevina | Regno Unito | Apvienotā Karaliste | Jungtinė Karalystė
GR | Greece | Гърция | Grecia | Řecko | Grækenland | Griechenland | Kreeka | Ελλάδα | Grèce | Grčka | Grecia | Grieķija | Graikija
HR | Croatia | Хърватия | Croacia | Chorvatsko | Kroatien | Kroatien | Horvaatia | Κροατία | Croatie | Hrvatska | Croazia | Horvātija | Kroatija
HU | Hungary | Унгария | Hungría | Maďarsko | Ungarn | Ungarn | Ungari | Ουγγαρία | Hongrie | Mađarska | Ungheria | Ungārija | Vengrija
IE | Ireland | Ирландия | Irlanda | Irsko | Irland | Irland | Iirimaa | Ιρλανδία | Irlande | Irska | Irlanda | Īrija | Airija
IT | Italy | Италия | Italia | Itálie | Italien | Italien | Itaalia | Ιταλία | Italie | Italija | Italia | Itālija | Italija
LT | Lithuania | Литва | Lituania | Litva | Litauen | Litauen | Leedu | Λιθουανία | Lituanie | Litva | Lituania | Lietuva | Lietuva
LU | Luxembourg | Люксембург | Luxemburgo | Lucembursko | Luxembourg | Luxemburg | Luksemburg | Λουξεμβούργο | Luxembourg | Luksemburg | Lussemburgo | Luksemburga | Liuksemburgas
LV | Latvia | Латвия | Letonia | Lotyšsko | Letland | Lettland | Läti | Λετονία | Lettonie | Latvija | Lettonia | Latvija | Latvija
MD | Moldova | Молдова | Moldavia | Moldavsko | Moldova | Moldawien | Moldaavia | Μολδαβία | Moldavie | Moldova | Moldova | Moldova | Moldova
MT | Malta | Малта | Malta | Malta | Μalta | Malta | Malta | Μάλτα | Malte | Malta | Malta | Malta | Мalta
NL | Netherlands | Нидерландия | Países Bajos | Nizozemsko | Nederlandene | Niederlande | Madalmaad | Κάτω Χώρες | Pays-Bas | Nizozemska | Paesi Bassi | Nīderlande | Nyderlandai
PL | Poland | Полша | Polonia | Polsko | Polen | Polen | Poola | Πολωνία | Pologne | Poljska | Polonia | Polija | Lenkija
PT | Portugal | Португалия | Portugal | Portugalsko | Portugal | Portugal | Portugal | Πορτογαλία | Portugal | Portugal | Portogallo | Portugāle | Portugalija
RO | Romania | Румъния | Rumanía | Rumunsko | Rumænien | Rumänien | Rumeenia | Ρουμανία | Roumanie | Rumunjska | Romania | Rumānija | Rumunija
RU | Russia | Русия | Rusia | Rusko | Rusland | Russland | Venemaa | Ρωσσία | Russie | Rusija | Russia | Krievija | Rusija
SE | Sweden | Швеция | Suecia | Švédsko | Sverige | Schweden | Rootsi | Σουηδία | Suède | Švedska | Svezia | Zviedrija | Švedija
SI | Slovenia | Словения | Eslovenia | Slovinsko | Slovenien | Slowenien | Sloveenia | Σλοβενία | Slovénie | Slovenija | Slovenia | Slovēnija | Slovėnija
SK | Slovakia | Словакия | Eslovaquia | Slovensko | Slovakiet | Slowakei | Slovakkia | Σλοβακία | Slovaquie | Slovačka | Slovacchia | Slovākija | Slovakija
UA | Ukraine | Украина | Ucrania | Ukrajina | Ukraine | Ukraine | Ukraina | Ουκρανία | Ukraine | Ukrajina | Ucraina | Ukraina | Ukraina
ME | Montenegro | Черна гора | Montenegro | Černá Hora | Montenegro | Montenegro | Montenegro | Μαυροβούνιο | Monténégro | Crna Gora | Montenegro | Melnkalne | Juodkalnija
CODUL ȚĂRII
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
AT | Ausztria | L-Awstrija | Oostenrijk | Austria | Áustria | Austria | Rakúsko | Avstrija | Itävalta | Österrike | Австрия | Аустрија
BE | Belgium | Il-Belġju | België | Belgia | Bélgica | Belgia | Belgicko | Belgija | Belgia | Belgien | Бельгия | Белгија
BG | Bulgária | Il-Bulgarija | Bulgarije | Bułgaria | Bulgária | Bulgaria | Bulharsko | Bolgarija | Bulgaria | Bulgarien | Болгария | Бугарска
CH | Svájc | L-Iżvizzera | Zwitserland | Szwajcaria | Suíça | Elveția | Švajčiarsko | Švica | Sveitsi | Schweiz | Швейцария | Швајцарска
RS | Szerbia | Is-Serbja | Servië | Serbia | Sérvia | Serbia | Srbsko | Srbija | Serbia | Serbien | Сербия | Србија
CY | Ciprus | Ċipru | Cyprus | Cypr | Chipre | Cipru | Cyprus | Ciper | Kypros | Cypern | Кипр | Кипар
CZ | Cseh Köztársaság | Ir-Repubblika Ċeka | Tsjechië | Republika Czeska | República Checa | Republica Cehă | Česko | Češka | Tšekki | Tjeckien | Чешская республика | Чешка Република
DE | Németország | Il-Ġermanja | Duitsland | Niemcy | Alemanha | Germania | Nemecko | Nemčija | Saksa | Tyskland | Германия | Немачка
DK | Dánia | Id-Danimarka | Denemarken | Dania | Dinamarca | Danemarca | Dánsko | Danska | Tanska | Danmark | Дания | Данска
EE | Észtország | L-Estonja | Estland | Estonia | Estónia | Estonia | Estónsko | Estonija | Viro | Estland | Эстония | Естонија
ES | Spanyolország | Spanja | Spanje | Hiszpania | Espanha | Spania | Španielsko | Španija | Espanja | Spanien | Испания | Шпанија
FI | Finnország | Il-Finlandja | Finland | Finlandia | Finlândia | Finlanda | Fínsko | Finska | Suomi | Finland | Финляндия | Финска
FR | Franciaország | Franza | Frankrijk | Francja | França | Franța | Francúzsko | Francija | Ranska | Frankrike | Франция | Француска
GB | Egyesült Királyság | Ir-Renju Unit | Verenigd Koninkrijk | Wielka Brytania | Reino Unido | Regatul Unit | Veľká Británia | Združeno kraljestvo | Yhdistynyt kuningaskunta | Förenade kungariket | Великобритания | Велика Британија
GR | Görögország | Il-Greċja | Griekenland | Grecja | Grécia | Grecia | Grécko | Grčija | Kreikka | Grekland | Греция | Грчка
HR | Horvátország | Il-Kroazja | Kroatië | Chorwacja | Croácia | Croația | Chorvátsko | Hrvaška | Kroatia | Kroatien | Хорватия | Хрватска
HU | Magyarország | L-Ungerija | Hongarije | Węgry | Hungria | Ungaria | Maďarsko | Madžarska | Unkari | Ungern | Венгрия | Мађарска
IE | Írország | L-Irlanda | Ierland | Irlandia | Irlanda | Irlanda | Írsko | Irska | Irlanti | Irland | Ирландия | Ирска
IT | Olaszország | L-Italja | Italië | Włochy | Itália | Italia | Taliansko | Italija | Italia | Italien | Италия | Италија
LT | Litvánia | Il-Litwanja | Litouwen | Litwa | Lituânia | Lituania | Litva | Litva | Liettua | Litauen | Литва | Литванија
LU | Luxemburg | Il-Lussemburgu | Luxemburg | Luksemburg | Luxemburgo | Luxemburg | Luxembursko | Luksemburg | Luxemburg | Luxemburg | Люксембург | Луксембург
LV | Lettország | Il-Latvja | Letland | Łotwa | Letónia | Letonia | Lotyšsko | Latvija | Latvia | Lettland | Латвия | Летонија
MD | Moldávia | Il-Moldova | Moldavië | Mołdawia | Moldávia | Moldova | Moldavsko | Moldavija | Moldova | Moldavien | Молдавия | Молдавија
MT | Málta | Malta | Malta | Malta | Malta | Malta | Malta | Malta | Malta | Malta | Мальта | Малта
NL | Hollandia | In-Netherlands | Nederland | Holandia | Países Baixos | Țările de Jos | Holandsko | Nizozemska | Alankomaat | Nederländerna | Нидерланды | Холандија
PL | Lengyelország | Il-Polonja | Polen | Polska | Polónia | Polonia | Poľsko | Poljska | Puola | Polen | Польша | Пољска
PT | Portugália | Il-Portugall | Portugal | Portugalia | Portugal | Portugalia | Portugalsko | Portugalska | Portugali | Portugal | Португалия | Португал
RO | Románia | Ir-Rumanija | Roemenië | Rumunia | Roménia | România | Rumunsko | Romunija | Romania | Rumänien | Румыния | Румунија
RU | Oroszország | Ir-Russja | Rusland | Rosja | Rússia | Rusia | Rusko | Rusija | Venäjä | Ryssland | Россия | Русија
SE | Svédország | L-Iżvezja | Zweden | Szwecja | Suécia | Suedia | Švédsko | Švedska | Ruotsi | Sverige | Швеция | Шведска
SI | Szlovénia | Is-Slovenja | Slovenië | Słowenia | Eslovénia | Slovenia | Slovinsko | Slovenija | Slovenia | Slovenien | Словения | Словенија
SK | Szlovákia | Is-Slovakkja | Slowakije | Słowacja | Eslováquia | Slovacia | Slovensko | Slovaška | Slovakia | Slovakien | Словакия | Словачка
UA | Ukrajna | L-Ukrajna | Oekraïne | Ukraina | Ucrânia | Ucraina | Ukrajina | Ukrajina | Ukraina | Ukraina | Украина | Украјина
ME | Montenegró | Il-Montenegro | Montenegro | Czarnogóra | Montenegro | Muntenegru | Čierna Hora | Črna gora | Montenegro | Montenegro | Черногория | Црна Гора
CODUL DIRECȚIILOR
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
ALL | all directions | Всички посоки | Todas las direcciones | všechny směry | Alle retninger | alle Richtungen | Kõik suunad | Όλες οι κατευθύνσεις | toutes les directions | Svi smjerovi | tutte le direzioni | Visi virzieni | Visomis kryptimis
UPS | upstream | Срещу течението | Aguas arriba | proti proudu | Opstrøms | Bergfahrt | Ülesvoolu | Ανάντη | montant | Uzvodno | in ascesa | Pret straumi | Prieš srovę
DWN | downstream | По течението | Aguas abajo | po proudu | Nedstrøms | Talfahrt | Allavoolu | Κατάντη | avalant | Nizvodno | in discesa | Pa straumi | Pasroviui
CODUL DIRECȚIILOR
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
ALL | minden irányba | id-direzzjonijiet kollha | Alle richtingen | Wszystkie kierunki | Todas as direções | toate direcțiile | všetky smery | vse smeri | Kaikki suunnat | Alla riktningar | Движение во всех направлениях | Сви смерови
UPS | hegymenet | upstream | Opvaart | Pod prąd | Montante | în amonte | proti prúdu | proti toku | Vastavirtaan | Uppströms | Движение вверх по течению | Узводно
DWN | völgymenet | downstream | Afvaart | Z prądem | Jusante | în aval | po prúde | v smeri toka | Myötävirtaan | Nedströms | Движение вниз по течению | Низводно
CODUL DE LIMBĂ
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
EN | English | Английски | Inglés | anglicky | Engelsk | englisch | inglise | Αγγλικά | Anglais | engleski | inglese | Angļu | Anglų
BG | Bulgarian | Български | Búlgaro | bulharsky | Bulgarsk | bulgarisch | bulgaaria | Βουλγαρικά | Bulgare | bugarski | bulgaro | Bulgāru | Bulgarų
ES | Spanish | Испански | Español | španělsky | Spansk | spanisch | hispaania | Ισπανικά | Espagnol | španjolski | spagnolo | Spāņu | Ispanų
CS | Czech | Чешки | Checo | česky | Tjekkisk | tschechisch | tšehhi | Τσεχικά | Tchèque | češki | ceco | Čehu | Čekų
DA | Danish | Датски | Danés | dánsky | Dansk | dänisch | taani | Δανικά | Danois | danski | danese | Dāņu | Danų
DE | German | Немски | Alemán | německy | Tysk | deutsch | saksa | Γερμανικά | Allemand | njemački | tedesco | Vācu | Vokiečių
ET | Estonian | Естонски | Estonio | estonsky | Estisk | estnisch | eesti | Εσθονικά | Estonien | estonski | estone | Igauņu | Estų
EL | Greek | Гръцки | Griego | řecky | Græsk | griechisch | kreeka | Ελληνικά | Grec | grčki | greco | Grieķu | Graikų
FR | French | Френски | Francés | francouzsky | Fransk | französisch | prantsuse | Γαλλικά | Français | francuski | francese | Franču | Prancūzų
GA | Gaelic | Ирландски | Irlandés | irsky | Irsk | gälisch | iiri | Ιρλανδικά | Gaélique | irski | gaelico | Gēlu | Gėlų
HR | Croatian | Хърватски | Croata | chorvatsky | Kroatisk | kroatisch | horvaatia | Κροατικά | Croate | hrvatski | croato | Horvātu | Kroatų
IT | Italian | Италиански | Italiano | italsky | Italiensk | italienisch | itaalia | Ιταλικά | Italien | talijanski | italiano | Itāliešu | Italų
LV | Latvian | Латвийски | Letón | lotyšsky | Lettisk | lettisch | läti | Λετονικά | Letton | latvijski | lettone | Latviešu | Latvių
LT | Lithuanian | Литовски | Lituano | litevsky | Litauisk | litauisch | leedu | Λιθουανικά | Lituanien | litavski | lituano | Lietuviešu | Lietuvių
HU | Hungarian | Унгарски | Húngaro | maďarsky | Ungarsk | ungarisch | ungari | Ουγγρικά | Hongrois | mađarski | ungherese | Ungāru | Vengrų
MT | Maltese | Малтийски | Maltés | maltsky | Maltesisk | maltesisch | malta | Μαλτέζικα | Maltais | malteški | maltese | Maltiešu | Maltiečių
NL | Dutch | Холандски | Neerlandés | nizozemsky | Nederlandsk | niederländisch | hollandi | Ολλανδικά | Néerlandais | nizozemski | neerlandese | Holandiešu | Nyderlandų
PL | Polish | Полски | Polaco | polsky | Polsk | polnisch | poola | Πολωνικά | Polonais | poljski | polacco | Poļu | Lenkų
PT | Portuguese | Португалски | Portugués | portugalsky | Portugisisk | portugiesisch | portugali | Πορτογαλικά | Portugais | portugalski | portoghese | Portugāļu | Portugalų
RO | Romanian | Румънски | Rumano | rumunsky | Rumænsk | rumänisch | rumeenia | Ρουμανικά | Roumain | rumunjski | rumeno | Rumāņu | Rumunų
SK | Slovak | Словашки | Eslovaco | slovensky | Slovakisk | slowakisch | slovaki | Σλοβακικά | Slovaque | slovački | slovacco | Slovāku | Slovakų
SL | Slovenian | Словенски | Eslovaco | slovinsky | Slovensk | slowenisch | sloveenia | Σλοβενικά | Slovène | slovenski | sloveno | Slovēņu | Slovėnų
FI | Finnish | Финландски | Finés | finsky | Finsk | finnisch | soome | Φινλανδικά | Finnois | finski | finlandese | Somu | Suomių
SV | Swedish | Шведски | Sueco | švédsky | Svensk | schwedisch | rootsi | Σουηδικά | Suédois | švedski | svedese | Zviedru | Švedų
RU | Russian | Руски | Ruso | rusky | Russisk | russisch | vene | Ρωσσικά | Russe | ruski | russo | Krievu | Rusų
SR | Serbian | Сръбски | Serbio | srbsky | Serbisk | serbisch | serbia | Σερβικά | Serbe | srpski | serbo | Serbu | Serbų
CODUL DE LIMBĂ
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
EN | angol | Ingliż | Engels | angielski | Inglês | Engleză | anglicky | angleščina | Englanti | Engelska | Английский | енглески
BG | bolgár | Bulgaru | Bulgaars | bułgarski | Búlgaro | Bulgară | bulharsky | bolgarščina | Bulgaria | Bulgariska | Болгарский | бугарски
ES | spanyol | Spanjol | Spaans | hiszpański | Espanhol | Spaniolă | španielsky | španščina | Espanja | Spanska | Испанский | шпански
CS | cseh | Ċek | Tsjechisch | czeski | Checo | Cehă | česky | češčina | Tšekki | Tjeckiska | Чешский | чешки
DA | dán | Daniż | Deens | duński | Dinamarquês | Daneză | dánsky | danščina | Tanska | Danska | Датский | дански
DE | német | Ġermaniż | Duits | niemiecki | Alemão | Germană | nemecky | nemščina | Saksa | Tyska | Немецкий | немачки
ET | észt | Estonjan | Ests | estoński | Estónio | Estonă | estónsky | estonščina | Viro | Estniska | Эстонский | естонски
EL | görög | Grieg | Grieks | grecki | Grego | Greacă | grécky | grščina | Kreikka | Grekiska | Греческий | грчки
FR | francia | Franċiż | Frans | francuski | Francês | Franceză | francúzsky | francoščina | Ranska | Franska | Французский | француски
GA | ír | Gaelic | Iers | irlandzki | Gaélico | Irlandeză | írsky | irščina | Iiri | Iriska | |
HR | horvát | Kroat | Kroatisch | chorwacki | Croata | Croată | chorvátsky | hrvaščina | Kroatia | Kroatiska | Хорватский | хрватски
IT | olasz | Taljan | Italiaans | włoski | Italiano | Italiană | taliansky | italijanščina | Italia | Italienska | Итальянский | италијански
LV | lett | Latvjan | Lets | łotewski | Letão | Letonă | lotyšsky | latvijščina | Latvia | Lettiska | Латвийский | летонски
LT | litván | Litwen | Litouws | litewski | Lituano | lituaniană | litovsky | litovščina | Liettua | Litauiska | Литовский | литвански
HU | magyar | Ungeriż | Hongaars | węgierski | Húngaro | Maghiară | maďarsky | madžarščina | Unkari | Ungerska | Венгерский | мађарски
MT | máltai | Malti | Maltees | maltański | Maltês | Malteză | maltsky | malteščina | Malta | Maltesiska | Мальтийский | Malteski
NL | holland | Netherlandiż | Nederlands | holenderski | Neerlandês | Olandeză | holandsky | nizozemščina | Hollanti | Nederländska | Голландский | пољски
PL | lengyel | Pollakk | Pools | polski | Polaco | Poloneză | poľsky | poljščina | Puola | Polska | Польский | португалски
PT | portugál | Portugiż | Portugees | portugalski | Português | Portugheză | portugalsky | portugalščina | Portugali | Portugisiska | Португальский | румунски
RO | román | Rumen | Roemeens | rumuński | Romeno | Română | rumunsky | romunščina | Romania | Rumänska | Румынский | руски
SK | szlovák | Slovakk | Slowaaks | słowacki | Eslovaco | Slovacă | slovensky | slovaščina | Slovakki | Slovakiska | Словацкий | словачки
SL | szlovén | Sloven | Sloveens | słoweński | Esloveno | Slovenă | slovinsky | slovenščina | Sloveeni | Slovenska | Словенский | словеначки
FI | finn | Finlandiż | Fins | fiński | Finlandês | Finlandeză | fínsky | finščina | Suomi | Finska | Финский | фински
SV | svéd | Żvediż | Zweeds | szwedzki | Sueco | Suedeză | švédsky | švedščina | Ruotsi | Svenska | Шведский | шведски
RU | orosz | Russu | Russisch | rosyjski | Russo | Rusă | rusky | ruščina | Venäjä | Ryska | Русский | словачки
SR | szerb | Serb | Servisch | serbski | Sérvio | Sârbă | srbsky | srbščina | Serbia | Serbiska | Сербский | српски
CODUL INDICAȚIILOR
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
MAX | maximum | максимум | máximo | maximum | Maksimum | höchstens | maksimum | Μέγιστο | maximum | Najviše | massimo | maksimāli | didžiausia
MIN | minimum | минимум | mínimo | minimum | Minimum | mindestens | miinimum | Ελάχιστο | minimum | Najmanje | minimo | minimāli | mažiausia
RED | reduced by | намалено с | Reducido en | redukován o | Reduceret med | verringert um | vähendatud | Μειωμένο κατά | réduit de | Smanjeno za | diminuito di | samazināts par | sumažinama
CODUL INDICAȚIILOR
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
MAX | Maximum | massima | Maximaal | maksimum | Máximo | maxim | maximum | največje | maksimi | Maximum | максимальный | максимум
MIN | Minimum | minima | Minimaal | minimum | Mínimo | minim | minimum | najmanjše | minimi | Minimum | минимальный | минимум
RED | által csökkentve | imnaqqsa b’ | Verminderd met | ograniczenie o (wartość) | Reduzido de | redus cu | znížený o | zmanjšano za | vähennetty seuraavalla: | Reducerat med | уменьшено на | умањен за
CODUL INTERVALELOR
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
CON | continuous | Непрекъснато | Continuo | nepřetržitě | Kontinuerligt | durchgehend | Pidev | Συνεχής | Permanent | Neprekidno | permanente | Nepārtraukti | Nuolat
DAY | daily | Ежедневно | Diario | denně | Dagligt | täglich | Iga päev | Ημερήσια | Journalier | Dnevno | giornaliero | Ik dienas | Kasdien
WRK | Monday to Friday | От понеделник до петък | Lunes a viernes | pondělí až pátek | Mandag til fredag | Montag bis Freitag | Esmaspäevast reedeni | Δευτέρα έως Παρασκευή | Lundi au Vendredi | Od ponedjeljka do petka | da lunedì a venerdì | No pirmdienas līdz piektdienai | Nuo pirmadienio iki penktadienio
WKN | Saturday and Sunday | Събота и неделя | Sábado y domingo | sobota a neděle | Lørdag og søndag | Samstag und Sonntag | Laupäev ja pühapäev | Σάββατο έως Κυριακή | Samedi et Dimanche | Subotom i nedjeljom | sabato e domenica | Sestdiena un svētdiena | Šeštadienis ir sekmadienis
SUN | Sunday | Неделя | Domingo | neděle | Søndag | Sonntag | Pühapäev | Κυριακή | Dimanche | Nedjeljom | domenica | Svētdiena | Sekmadienis
MON | Monday | Понеделник | Lunes | pondělí | Mandag | Montag | Esmaspäev | Δευτέρα | Lundi | Ponedjeljkom | lunedì | Pirmdiena | Pirmadienis
TUE | Tuesday | Вторник | Martes | úterý | Tirsdag | Dienstag | Teisipäev | Τρίτη | Mardi | Utorkom | martedì | Otrdiena | Antradienis
WED | Wednesday | Сряда | Miércoles | středa | Onsdag | Mittwoch | Kolmapäev | Τετάρτη | Mercredi | Srijedom | mercoledì | Trešdiena | Trečiadienis
THU | Thursday | Четвъртък | Jueves | čtvrtek | Torsdag | Donnerstag | Neljapäev | Πέμπτη | Jeudi | Četvrtkom | giovedì | Ceturtdiena | Ketvirtadienis
FRI | Friday | Петък | Viernes | pátek | Fredag | Freitag | Reede | Παρασκευή | Vendredi | Petkom | venerdì | Piektdiena | Penktadienis
SAT | Saturday | Събота | Sábado | sobota | Lørdag | Samstag | Laupäev | Σάββατο | Samedi | Subotom | sabato | Sestdiena | Šeštadienis
DTI | day-time | През деня | Período diurno | ve dne | Om dagen | bei Tag | päeval | Κατά τη διάρκεια της ημέρας | en journée | Preko dana | diurno | dienā | Dienos metas
NTI | night-time | През нощта | Período nocturno | v noci | Om natten | bei Nacht | öösel | Κατά της διάρκεια της νύχτας | de nuit | Preko noći | notturno | naktī | Nakties metas
RVI | in case of restricted visibility | При ограничена видимост | Con visibilidad reducida | za snížené viditelnosti | Ved nedsat sigt | bei beschränkten Sichtverhältnissen | piiratud nähtavuse korral | Σε περίπτωση περιορισμένης ορατότητας | par mauvaise visibilité | U slučaju smanjene vidljivosti | in caso di visibilità ridotta | ierobežotas redzamības apstākļos | Riboto matomumo atveju
EXC | with the exception of | С изключение на | salvo | s výjimkou | Med undtagelse af | mit Ausnahme von | välja arvatud | Εξαιρουμένου του | à l'exception de | S izuzetkom | ad eccezione di | izņemot | Išskyrus
WRD | Monday to Friday except public holidays | От понеделник до петък, с изключение на официални празници | De lunes a viernes excepto festivos | pondělí až pátek kromě státních svátků | Mandag til fredag undtagen helligdage | Montag bis Freitag ausgenommen Feiertage | Esmaspäevast reedeni, v.a riigipühad | Δευτέρα έως Παρασκευή εκτός επίσημων αργιών | Lundi au vendredi excepté jours fériés | Od ponedjeljka do petka osim praznika | da lunedì a venerdì, eccetto i giorni festivi | No pirmdienas līdz piektdienai, izņemot oficiāli svinamās dienas | Nuo pirmadienio iki penktadienio, išskyrus valstybinių švenčių dienas
CODUL INTERVALELOR
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
CON | folyamatos | (kontinwu) | Onafgebroken | ciągłe | Contínuo | permanent | nepretržite | neprekinjeno | Jatkuva | Fortlöpande | Постоянно | Непрекидан
DAY | naponta | kuljum | Dagelijks | codziennie | Diário | zilnic | denne | dnevno | Päivittäinen | Dagligen | ежедневно | Дневно
WRK | hétfőtől péntekig | Mit-Tnejn sal-Ġimgħa | Van maandag tot en met vrijdag | od poniedziałku do piątku | Segunda a sexta | de luni până vineri | pondelok až piatok | od ponedeljka do petka | Maanantaista perjantaihin | Måndag till fredag | с понедельника по пятницу | Од понедељка до петка
WKN | szombaton és vasárnap | Is-Sibt u l-Ħadd | Zaterdag en zondag | sobota i niedziela | Sábado e domingo | sâmbăta și duminica | sobota a nedeľa | sobota in nedelja | Lauantai ja sunnuntai | Lördag till söndag | суббота и воскресенье | Субота и недеља
SUN | vasárnap | Il-Ħadd | Zondag | niedziela | Domingo | duminică | nedeľa | nedelja | Sunnuntai | Söndag | воскресенье | Недеља
MON | hétfő | It-Tnejn | Maandag | poniedziałek | Segunda | luni | pondelok | ponedeljek | Maanantai | Måndag | понедельник | Понедељак
TUE | kedd | It-Tlieta | Dinsdag | wtorek | Terça | marți | utorok | torek | Tiistai | Tisdag | вторник | Уторак
WED | szerda | L-Erbgħa | Woensdag | środa | Quarta | miercuri | streda | sreda | Keskiviikko | Onsdag | среда | Среда
THU | csütörtök | Il-Ħamis | Donderdag | czwartek | Quinta | joi | štvrtok | četrtek | Torstai | Torsdag | четверг | Четвртак
FRI | péntek | Il-Ġimgħa | Vrijdag | piątek | Sexta | vineri | piatok | petek | Perjantai | Fredag | пятница | Петак
SAT | szombat | Is-Sibt | Zaterdag | sobota | Sábado | sâmbătă | sobota | sobota | Lauantai | Lördag | суббота | Субота
DTI | nappal | matul il-ġurnata | Overdag | w porze dziennej | Período diurno | în timpul zilei | cez deň | podnevi | päivisin | Dagtid | Дневное время | Дању
NTI | éjszaka | matul il-lejl | 's Nachts | w porze nocnej | Período noturno | în timpul nopții | v noci | ponoči | öisin | Nattetid | Ночное время | Ноћу
RVI | korlátozott látási viszonyok esetén | f’każ ta’ viżibbiltà ristretta | Bij beperkt zicht | w przypadku ograniczonej widoczności | Com visibilidade reduzida | în caz de vizibilitate redusă | pri zníženej viditeľnosti | v primeru omejene vidljivosti | näkyvyyden ollessa rajallinen | Vid begränsad sikt | в случае ограниченой видимости | При ограниченој видљивости
EXC | kivéve | bl-eċċezzjoni ta’ | Met uitzondering van | z wyjątkiem | Excetuando | cu excepția | okrem | razen | lukuun ottamatta: | Med undantag av | За исключением | Са изузетком
WRD | hétfőtől péntekig, kivéve ünnepnapokon | Mit-Tnejn sal-Ġimgħa minbarra btajjel pubbliċi | Van maandag tot en met vrijdag, uitgezonderd feestdagen | od poniedziałku do piątku z wyjątkiem świąt | Segunda a sexta exceto feriados | de luni până vineri exceptând sărbătorile | pondelok až piatok okrem sviatkov | od ponedeljka do petka razen v času praznikov | Maanantaista perjantaihin yleisiä vapaapäiviä lukuun ottamatta | Måndag till fredag, utom allmänna helgdagar | C понедельника по пятницу, кроме праздничных дней | Од понедељка до петка, осим празницима
CODUL PRIVIND LIMITĂRILE
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
OBSTRU | blockage | Препятствие | Obstrucción | uzávěra | Blokering | Sperre | Blokeering | Φράγμα | Restriction | Prepreka | ostruzione totale | Bloķēts | Blokavimas
PAROBS | partial obstruction | Частично препятствие | Obstrucción parcial | částečná uzávěra | Delvis blokering | teilweise Sperre | Osaline takistus | Μερική παρεμπόδιση | Restriction partielle | Djelomična prepreka | ostruzione parziale | Daļēji bloķēts | Dalinis blokavimas
DELAY | delay | Закъснение | Retraso | zpoždění | Forsinkelse | Verzögerung | Hilinemine | Καθυστέρηση | Délai | Kašnjenje | ritardo | Aizkavēšanās | Delsa
VESLEN | vessel length | Дължина на кораба | Eslora | délka plavidla | Fartøjets længde | Schiffslänge | Laeva pikkus | Μήκος σκάφους | Longueur du bateau | Duljina broda | lunghezza natante | Kuģa garums | Laivo ilgis
VESHEI | vessel air draught | Височина на кораба | Altura de la obra muerta | výška plavidla nad hladinou | Fartøjets højde over vandlinjen | Schiffshöhe | Laeva kõrgus veepinnast | Μέγιστο ύψος άνωθεν της ισάλου γραμμής | tirant d'air du bateau | Visina najviše fiksne točke broda iznad vode | altezza natante dal pelo dell'acqua | Kuģa virsūdens augstums | Laivo aukštis virš vandens
VESBRE | vessel breadth | Ширина на кораба | Manga | šířka plavidla | Fartøjets bredde | Schiffsbreite | Laeva laius | Μέγιστο πλάτος σκάφους | Largeur du bateau | Širina broda | larghezza del natante | Kuģa platums | Laivo plotis
VESDRA | vessel draught | Газене на кораба | Calado | ponor plavidla | Fartøjets dybgang | Schiffstiefgang | Laeva süvis | Βύθισμα σκάφους | Tirant d'eau du bateau | Gaz broda | pescaggio natante | Kuģa iegrime | Laivo grimzlė
AVALEN | available length | Допустима дължина | Eslora disponible | povolená délka | Disponibel længde | verfügbare Länge | Kasutatav pikkus | Διαθέσιμο μήκος | Longueur disponible | Raspoloživa duljina | lunghezza disponibile | Pieļaujamais garums | Leidžiamas ilgis
CLEHEI | clearance height | Свободна височина | Gálibo vertical | podjezdná výška | Frigang i højden | Durchfahrtshöhe | Kuja kõrgus | Ελεύθερο ύψος διέλευσης | Hauteur libre | Visina plovnog otvora | tirante d'aria | Pieļaujamais augstums | Leidžiamas aukštis
CLEWID | clearance width | Свободна ширина | Gálibo horizontal | průjezdná šířka | Frigang, bredde | Durchfahrtsbreite | Kuja laius | Ελεύθερο πλάτος διέλευσης | Largeur disponible | Širina plovnog otvora | larghezza della via navigabile | Pieļaujamais platums | Leidžiamas plotis
AVADEP | available depth | Допустимо газене | Profundidad disponible | využitelná hloubka | Vanddybde | verfügbare Tiefe | Kasutatav sügavus | Διαθέσιμο πλάτος | Mouillage disponible | Raspoloživa dubina | pescaggio massimo | Ūdens dziļums | Esamas gylis
NOMOOR | no mooring | Забранено швартоване | Prohibición de amarre | zákaz vyvazování | Fortøjning forbudt | Festmacheverbot | Sildumine keelatud | Απαγόρευση αγκυροβολίας | Interdiction d'amarrage | Zabranjen vez | divieto di ormeggio | Pietauvošanās aizliegta | Draudžiama švartuotis
SERVIC | changed service | Променено обслужване | Servicio limitado | omezení provozu | Ændret betjening | geänderte Betriebszeiten | Piiratud teenindus | Περιορισμένη υπηρεσία | Exploitation limitée | Ograničena usluga | servizio / esercizio limitato | Ierobežots pakalpojums | Ribotas aptarnavimas
NOSERV | no service | Няма обслужване | Interrupción del servicio | zastavení provozu | Ingen betjening | kein Betrieb | Ei teenindata | Καμία υπηρεσία | Navigation interrompue | Nema usluge | nessun servizio / esercizio | Pakalpojums nav pieejams | Neaptarnaujama
SPEED | speed limit | Ограничение на скорост | Límite de velocidad | omezení rychlosti | Hastighedsbegrænsning | Höchstgeschwindigkeit | Kiiruspiirang | Όριο ταχύτητας | Limite de Vitesse | Ograničenje brzine | limite di velocità | Ātruma ierobežojums | Ribojamas greitis
WAVWAS | no wash of waves | Забранено създаване на вълни | No crear oleaje | zákaz vytvářet vlnobití a sání | Undgå at lave efterdønninger | Sog und Wellenschlag vermeiden | Voolu tekitamine keelatud | Απαγόρευση πρόκλησης κυματισμών | Remous interdits | Zabranjeno pravljenje valova | divieto di moto ondoso | Neradīt viļņus | Nekelti bangų
PASSIN | no passing | Забранено преминаване | Prohibido el paso | zákaz potkávání | Passage er ikke tilladt | Begegnungsverbot | Läbimine keelatud | Απαγόρευση διέλευσης | Interdiction de croiser | Zabranjen prolaz | divieto di transito | Aizliegts šķērsot | Plaukti draudžiama
ANCHOR | no anchoring | Забранено заставането на котва | Prohibido fondear | zákaz kotvení | Opankring ikke tilladt | Ankerverbot | Ankrusse jäämine keelatud | Απαγόρευση αγκυροβολίας | Ancrage interdit | Zabranjeno sidrenje | divieto di ancoraggio | Noenkuroties aizliegts | Draudžiama nuleisti inkarą
OVRTAK | no overtaking | Забранено изпреварване | Prohibido adelantar | zákaz předjíždění | Overhaling ikke tilladt | Überholverbot | Möödasõit keelatud | Απαγόρευση προσπέρασης | Dépassement interdit | Zabranjeno pretjecanje | divieto di sorpasso | Apdzīt aizliegts | Lenkti draudžiama
MINPWR | minimum power | Минимална мощност | Potencia mínima | minimální výkon | Minimum kraft | Mindestantriebsleistung | Minimaalne võimsus | Ελάχιστη ισχύς | Puissance minimum | Minimalna snaga | potenza minima | Minimālā jauda | Mažiausia galia
ALTER | alternate traffic direction | Еднопосочно движение | Tráfico en sentido alterno | střídavý směr plavby | Skiftende færdselsretning | Einbahnverkehr | Asendus-liiklussuund | Εναλλασσόμενη κατεύθυνση κυκλοφορίας | navigation alternée | Naizmjeničan smjer prometa | traffico in senso alternato | divvirzienu satiksme | Keičiama laivų eismo kryptis
CAUTIO | special caution | Особено внимание | Precaución especial | zvýšená opatrnost | Særlig agtpågivenhed | besondere Vorsicht | Äärmine ettevaatus | Ιδιαίτερη προσοχή | attention spéciale | Poseban oprez | particolare cautela | īpaša piesardzība | Ypatingas perspėjimas
NOLIM | no limitation | Без ограничение | Sin limitaciones | bez omezení | Ingen begrænsninger | keine Einschränkung | Piirang puudub | Κανένας περιορισμός | pas de limitation | Bez ograničenja | nessuna limitazione | bez ierobežojumiem | Apribojimų pabaiga
TURNIN | no turning | Забранено извършване на поворот | Prohibido girar | zákaz provádět obrat | Vending ikke tilladt | Wendeverbot | Pööramine keelatud | Απαγόρευση στροφής | Interdiction de virer | Zabranjeno okretanje | divieto di manovra | pagriezties aizliegts | Apsisukti draudžiama
NOSHORE | not allowed to go ashore | Забранено слизането на брега | Prohibido desembarcar | zákaz vystupovat na břeh | Ikke tilladt at gå i land | Landgangverbot | Maaleminek keelatud | Απαγόρευση αποβίβασης | Interdiction de débarquer | Zabranjen izlazak na obalu | divieto di approdo | doties krastā aizliegts | Išlipti į krantą draudžiama
CONBRE | convoy breadth | Ширина на състава | Manga del convoy | šířka sestavy | Konvojbredde | Verbandsbreite | Konvoi laius | Πλάτος νηοπομπής | Largeur du convoi | Širina sastava | larghezza del convoglio | karavānas platums | Laivų vilkstinės plotis
CONLEN | convoy length | Дължина на състава | Eslora del convoy | délka sestavy | Konvojlængde | Verbandslänge | Konvoi pikkus | Μήκος νηοπομπής | Longueur du convoi | Duljina sastava | lunghezza del convoglio | karavānas garums | Laivų vilkstinės ilgis
LEADEP | least depth sounded | Минимална дълбочина | Profundidad mínima medida | minimální změřená hloubka | Mindste loddede dybde | minimale Tiefe | Looditud väikseim sügavus | Μικρότερο μετρηθέν βάθος | Profondeur minimale | Minimalna dubina | profondità minima rilevata | Mazākais izmērītais dziļums | Mažiausias gylis
NOBERT | no berthing | Забранена стоянка (на котва или на вързала към брега) | Prohibido atracar | zákaz stání | Ikke tilladt at lægge til kaj | Stillliegeverbot | Sildumine keelatud | Απαγόρευση πρόσδεσης | Interdiction de stationner | Zabranjeno pristajanje | divieto di attracco | doties uz piestātni aizliegts | Švartuotis draudžiama
CODUL PRIVIND LIMITĂRILE
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
OBSTRU | zárlat | ostaklu | Stremming | Zamknięcie | Obstrução | blocaj | blokáda | zapora | Este | Blockering | Закрыто | Препрека
PAROBS | részleges tilalom | ostaklu parzjali | Gedeeltelijke stremming | Częściowe zamknięcie | Obstrução parcial | restricție parțială | čiastočné prekážky | delna zapora | Osittainen este | Delvis obstruktion | Частично закрыто | Делимична препрека
DELAY | késedelem | dewmien | Oponthoud | Opóźnienie | Demora | întârziere | meškanie | zamuda | Viivästys | Försening | Задержка | Кашњење
VESLEN | hajóhossz | tul tal-bastiment | Scheepslengte | Długość statku | Comprimento (embarcação) | lungimea navei | dĺžka plavidla | dolžina plovila | Aluksen pituus | Fartygslängd | Длина судна | Дужина пловила
VESHEI | hajó magassága | għoli tal-bastiment | Scheepshoogte | Wysokość statku | Altura acima da linha de água (embarcação) | înălțimea deasupra liniei de plutire | výška plavidla nad hladinou | prosta višina plovila | Aluksen suurin korkeus vedenpinnasta | Fartygets höjd över vattenytan | Высота судна | Максимална висина пловила над водом
VESBRE | hajó szélessége | wisa’ tal-bastiment | Scheepsbreedte | Szerokość statku | Boca (embarcação) | lățimea navei | šírka plavidla | širina plovila | Aluksen leveys | Fartygsbredd | Ширина судна | Ширина пловила
VESDRA | hajó merülése | fundar meħtieġ għall-bastiment | Diepgang | Zanurzenie statku | Calado (embarcação) | pescajul navei | ponor plavidla | ugrez plovila | Aluksen syväys | Fartygets djupgående | Осадка | Газ пловила
AVALEN | rendelkezésre álló hosszúság | tul disponibbli | Doorvaartlengte | Długość użytkowa | Comprimento disponível | lungimea admisă | dostupná dĺžka | razpoložljiva dolžina | Käytettävissä oleva pituus | Tillgänglig längd | Ограничение длины | Расположива дужина
CLEHEI | szabad űrszelvény magasság | fond ta’ spazju ħieles | Doorvaarthoogte | Wysokość w świetle | Altura livre | gabaritul de înălțime | podjazdná výška | prosta višina prehoda | Alikulkukorkeus | Frihöjd | ограничение высоты | Слободна висина
CLEWID | rendelkezésre álló szélesség | wisa’ ta’ spazju ħieles | Doorvaartbreedte | Szerokość w świetle | Largura livre | gabaritul de lățime | prejazdná šírka | prosta širina prehoda | Käytettävissä oleva leveys | Farledsbredd | Ограничение ширины | Слободна ширина
AVADEP | rendelkezésre álló vízmélység | fond disponibbli | Beschikbare diepte | Głębokość użytkowa | Profundidade disponível | adâncimea disponibilă | dostupná hĺbka | razpoložljiva globina | Käytettävissä oleva syväys | Tillgängligt djup | Существующая глубина | Расположива дубина
NOMOOR | veszteglési tilalom | irmiġġ projbit | Afmeerverbod | Zakaz cumowania | Proibição de amarrar | interdicție de acostare | zákaz vyväzovania | prepovedan privez | Kiinnittyminen kielletty | Förtöjning förbjuden | Швартовка запрещена | Забрањено везивање
SERVIC | megváltozott üzem | servizz modifikat | Beperkte service | Usługa ograniczona | Serviço limitado | manevră restricționată | zmenená prevádzka | spremenjena storitev | Rajoitettu palvelu | Begränsad service | Изменения в обслуживании | Измењена услуга
NOSERV | üzemszünet | servizz sospiż | Geen bediening | Usługa niedostępna | Interrupção do serviço | manevră interzisă | zastavená prevádzka | ni storitve | Ei palvelua | Ingen service | Не обслуживаемое | Без услуге
SPEED | sebességkorlátozás | limitu tal-veloċità | Snelheidsbeperking | Ograniczenie prędkości | Limite de velocidade | limită de viteză | najvysššia povolená rýchlosť | omejitev hitrosti | Nopeusrajoitus | Hastighets-begränsning | Ограничение скорости | Ограничење брзине
WAVWAS | hullámkeltést elkerülni | tranja tal-mewġ projbita | Golfslag vermijden | Zakaz tworzenia fal | Não causar ondulação | formarea valurilor interzisă | zákaz vlnobitia a sania | prepovedano povzročanje valov | Voimakkaan aallokon tuottaminen kielletty | Undvik svall | Не создавай волнения | Забрањено прављење таласа
PASSIN | találkozás tilos | passaġġ projbit | Ontmoeten verboden | Zakaz wymijania | Proibição de passar | traversarea interzisă | zákaz stretávania | prepovedan prehod | Ei läpikulkua | Passering förbjuden | Нет прохода | Забрањен пролаз
ANCHOR | horgonyozni tilos | ankraġġ projbit | Ankeren verboden | Zakaz kotwiczenia | Proibição de ancorar | ancorarea interzisă | zákaz kotvenia | prepovedano sidranje | Ei ankkuroitumista | Ankring förbjuden | Якорная стоянка запрещена | Забрањено сидрење
OVRTAK | előzni tilos | projbit il-qbiż ta’ bastimenti oħra | Voorbijlopen verboden | Zakaz wyprzedzania | Proibição de cruzar ou ultrapassar | depășirea interzisă | zákaz predchádzania | prepovedano prehitevanje | Ei ohittamista | Omkörning förbjuden | Обгон запрещен | Забрањено престизање
MINPWR | minimális teljesítmény | potenza minima | Minimaal vermogen | Minimalna moc napędu | Potência mínima | putere minimă | minimálny výkon | najmanjša moč | Vähimmäisteho | Minsta motoreffekt | минимальная мощность | Минимална снага
ALTER | váltakozó forgalmi irány | direzzjoni alternata tat-traffiku | Beurtelings verkeer | Ruch naprzemienny | Sentido alternado | trafic cu sensuri alternative | striedajúci sa smer premávky | izmenično usmerjanje prometa | vaihteleva liikenteen suunta | Alternerande farleds-riktning | Встречное движение | Наизменични смер кретања
CAUTIO | kiemelt óvatosság | attenzjoni speċjali | Bijzondere voorzichtigheid | Szczególna ostrożność | Atenção especial | vigilență mărită | zvýšená opatrnosť | posebna pozornost | erikoisvaroitus | Varning | Соблюдай осторожность | Посебан опрез
NOLIM | nincs korlátozás | ebda restrizzjoni | Geen beperking | Koniec ograniczeń | Sem restrições | fără restricții | bez obmedzenia | brez omejitve | ei rajoitusta | Ingen begränsning | Без ограничений | Без ограничења
TURNIN | megfordulni tilos | dawran projbit | Draaien verboden | Zakaz zawracania | Proibição de inverter marcha | întoarcerea interzisă | zákaz vykonávania obratov | prepovedano obračanje | Kääntyminen kielletty | Vändning förbjuden | Поворот запрещен | Забрањено окретање
NOSHORE | partfuttatás tilos | żbark projbit | Aan wal gaan verboden | Brak pozwolenia wejścia na ląd | Proibição de ir a terra | nu este permis accesul la mal | zákaz vystupovať na breh | prepovedano izkrcanje | Maihinnousu kielletty | Ej tillåtelse att gå i land | Запрещен выход на берег | Забрањен излазак на обалу
CONBRE | kötelék szélesség | wisa’ tal-konvoj | Breedte van de duwsleep | Szerokość zestawu | Largura do comboio | lățimea convoiului | šírka zostavy | širina konvoja | kytkyeen leveys | Konvojbredd | Ширина состава судов | Ширина састава
CONLEN | kötelék hossz | tul tal-konvoj | Lengte van de duwsleep | Długość zestawu | Comprimento do comboio | lungimea convoiului | dĺžka zostavy | dolžina konvoja | kytkyeen pituus | Konvojlängd | Длина состава судов | Дужина састава
LEADEP | minimális mélység | l-inqas fond imkejjel | Minst gepeilde diepte | Najmniejsza zmierzona głębokość | Profundidade mínima medida | adâncimea minimă | najnižšia nameraná hĺbka | najmanjša izmerjena globina | matalin luodattu syvyys | Minsta lodade djup | Минимальная глубина | Најмања измерена дубина
NOBERT | veszteglési tilalom | irmiġġ projbit | Aanleggen verboden | Zakaz cumowanie | Proibição de atracar | amararea interzisă | zákaz státia | prepovedan pristanek | Laituriin kiinnittäminen kielletty | Tilläggning förbjuden | Швартовка запрещена | Забрана пристајања
CODUL MĂSURĂTORILOR
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
DIS | discharge | Отток | Descarga | průtok | Udledning | Abfluss | Lossimine | Εκφόρτωση | Débit | Protok | portata | Ūdens novadīšana | Vandens išleidimas
REG | regime | Режим | Régimen | režim | Vandregime | Regime | Kord | Κατάσταση ροής υδάτων | Régime | Režim | regime | Darba režīms | Režimas
BAR | barrage status | Състояние на бента | Estado presa | stav vzdutí | Status for dæmning | Wehrstellung | Paisu asend | Κατάσταση φράγματος | Statuts des barrages | Status brane | stato sbarramento | Aizsprosta stāvoklis | Užtvaros padėtis
VER | vertical clearance | Свободна височина (габарит) | Gálibo libre | podjezdná výška | Lodret frigang | Durchfahrthöhe | Läbisõidu-kõrgus | Ελεύθερο ύψος | Hauteur libre maximum | Visina slobodnog prolaza | tirante d'aria | Pieļaujamais augstums | Laivo kelio aukštis
LSD | least sounded depth | Минимална дълбочина | Profundidad mínima medida | minimální změřená hloubka | Mindste loddede dybde | minimale Tiefe | Looditud väikseim sügavus | Μικρότερο μετρηθέν βάθος | Profondeur minimale | Minimalna dubina | profondità minima rilevata | Minimālais dziļums | Mažiausias gylis
WAL | water level | Водно ниво | Nivel de agua | vodní stav | Vandstand | Wasserstand | Veetase | Στάθμη υδάτων | Niveaux des eaux | Vodostaj | livello idrometrico | Ūdens līmenis | Vandens lygis
NOM | no measurement | Няма измерване | Sin medida | žádné měření | Ingen måling | kein Messwert | Ei mõõdeta | Καμία μέτρηση | Pas de mesure | Nema mjerenja | nessuna misurazione | nav mērījuma | Neišmatuota
CODUL MĂSURĂTORILOR
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
DIS | lefolyás | ħruġ ta’ ilma | Afvoer | Spust | Descarga | debit | prietok | pretok | Virtaus | Utsläpp | Спуск воды | Протицај
REG | vízjárás | rata tal-fluss | Regime | Reżim | Regime | regim | režim | režim | Vedenkorkeussuhteet | Ordning | Судоходный режим | Режим
BAR | duzzasztási állapot | status tal-milqgħa | Stuwstand | Stan zapory | Status da barragem | starea barajului | stav hate | položaj zapor | Avattavan padon tilanne | Fördämningsstatus | Состояние плотины | Статус преграде
VER | szabad űrszelvény-magasság | fond ħieles | Doorvaarthoogte | Prześwit pionowy | Altura livre | înălțime liberă de trecere | podjazdná výška | prosta višina prehoda | Alikulkukorkeus | Frihöjd | Высота судоходного пролёта | Расположива висина пролаза
LSD | legkisebb vízmélység | l-inqas fond imkejjel | Minst gepeilde diepte | Głębokość minimalna | Profundidade mínima medida | adâncimea minimă | najnižšia nameraná hĺbka | najmanjša izmerjena globina | Matalin luodattu syvyys | Minsta lodade djup | Минимальная глубина | Најмања измерена дубина
WAL | vízállás | livell tal-ilma | Waterstand | Stan wody | Nível da água | nivelul apei | vodný stav | vodostaj | Vedenkorkeus | Vattennivå | Уровень воды | Ниво воде
NOM | nincs mérési adat | ebda kejl | Geen meting | Brak pomiaru | Sem medição | măsurători lipsă | žiadna nameraná hodnota | ni meritve | ei mitattu | Ingen mätning | Нет измерений | Нема мерења
CODUL POZIȚIILOR
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
AL | all | Навсякъде (всички направления) | Todo | vše | Alt | ganz | Kõik | Ολόκληρη η πλωτή οδός | Tout le chenal | Svi smjerovi | intero canale navigabile | Laba redzamība | Visur
LE | left | Ляво | Izquierda | vlevo | Venstre | links | Vasakpoolne | Αριστερά | Gauche | Lijevo | sinistra | Pa kreisi | Kairė
MI | middle | В средата | Centro | střed | Midten | Mitte | Keskmine | Στο μέσο | Milieu | Sredina | centro | Vidū | Vidurys
RI | right | Дясно | Derecha | vpravo | Højre | rechts | Parempoolne | Δεξιά | Droite | Desno | destra | Pa labi | Dešinė
LB | left bank | Ляв бряг | Margen izquierda | levý břeh | Venstre bred | linkes Ufer | Vasak kallas | Αριστερή όχθη | Rive gauche | Lijeva obala | sponda sinistra | Kreisais krasts | Kairysis krantas
RB | right bank | Десен бряг | Margen derecha | pravý břeh | Højre bred | rechtes Ufer | Parem kallas | Δεξιά όχθη | Rive droite | Desna obala | sponda destra | Labais krasts | Dešinysis krantas
N | north | Северно | Norte | sever | Nord | Nord | põhi | Βόρεια | Nord | Sjeverno | nord | Uz ziemeļiem | Šiaurė
NE | north-east | Североизточно | Noreste | severovýchod | Nordøst | Nord-Ost | kirre | Βορειοανατολικά | Nord-est | Sjeveroistočno | nord-est | Uz ziemeļaustrumiem | Šiaurės rytai
E | east | Източно | Este | východ | Øst | Ost | ida | Ανατολικά | Est | Istočno | est | Uz austrumiem | Rytai
SE | south-east | Югоизточно | Sureste | jihovýchod | Sydøst | Süd-Ost | kagu | Νοτιοανατολικά | Sud-est | Jugoistočno | sud-est | UZ dienvidaustrumiem | Pietryčiai
S | south | Южно | Sur | jih | Syd | Süd | lõuna | Νότια | Sud | Južno | sud | Uz dienvidiem | Pietūs
SW | south-west | Югозападно | Suroeste | jihozápad | Sydvest | Süd-West | edel | Νοτιοδυτικά | Sud-ouest | Jugozapadno | sud-ovest | Uz dienvidrietumiem | Pietvakariai
W | west | Западно | Oeste | západ | Vest | West | lääs | Δυτικά | Ouest | Zapadno | ovest | Uz rietumiem | Vakarai
NW | north-west | Северозападно | Noroeste | severozápad | Nordvest | Nord-West | loe | Βορειοδυτικά | Nord-ouest | Sjeverozapadno | nord-ovest | Uz ziemeļrietumiem | Šiaurės vakarai
BI | big | Голям | Grande | velký | Stor | groß | suur | Μεγάλο | grand | Velik | grande | liels | Didelis
SM | small | Малък | Pequeño | malý | Lille | klein | väike | Μικρό | petit | Mali | piccolo | mazs | Mažas
OL | old | Стар | Antiguo | starý | Gammel | alt | vana | Παλαιό | vieux | Star | vecchio | vecs | Senas
EW | new | Нов | Nuevo | nový | Ny | neu | uus | Νέο | nouveau | Nov | nuovo | jauns | Naujas
MP | movable part | Подвижна част | Parte móvil | pohyblivá část | Bevægelig del | beweglicher Teil | avatav osa | Κινητό τμήμα | partie amovible | Pokretni dio | parte mobile | kustīgā daļa | Slankioji dalis
FP | fixed part | Неподвижна част | Parte fija | pevná část | Fast del | fester Teil | fikseeritud osa | Σταθερό τμήμα | partie fixe | Nepokretni dio | parte fissa | nekustīgā daļa | Stacionarioji dalis
VA | variable | променлив | Variable | proměnlivé | Variabel | veränderlich | muutuv | Μεταβλητό | variable | Promjenjivo | variabile | mainīgs | Kintamas
GY | green buoy | Зелен буй | Boya verde | zelená bóje | Grøn bøje | grüne Boje | roheline poi | Πράσινος σημαντήρας | bouée verte | Zelena plutača | boa verde | zaļa boja | Žalias plūduras
RY | red buoy | Червен буй | Boya roja | červená bóje | Rød bøje | rote Boje | punane poi | Κόκκινος σημαντήρας | bouée rouge | Crvena plutača | boa rossa | sarkana boja | Raudonas plūduras
CODUL POZIȚIILOR
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
AL | mind/teljesen | kollha | Geheel | wszędzie | Todas | toată calea navigabilă / întregul obiect | všetky | vse | Kaikki | Hela | Все направления | Све
LE | bal | xellug | Links | po lewej | Esquerda | stânga | vľavo | levo | Vasen | Vänster | Слева | Лево
MI | közép | nofs | Midden | pośrodku | Centro | mijloc | v strede | sredina | Keskimmäinen | Mitten | В середине | Средина
RI | jobb | lemin | Rechts | po prawej | Direita | dreapta | vpravo | desno | Oikea | Höger | Справа | Десно
LB | bal part | xatt tax-xellug | Linkeroever | lewy brzeg | Margem esquerda | malul stâng | ľavý breh | levi breg | Vasen ranta | Vänstra banken | Левый берег | Лева обала
RB | jobb part | xatt tal-lemin | Rechteroever | prawy brzeg | Margem direita | malul drept | pravý breh | desni breg | Oikea ranta | Högra banken | Правый берег | Десна обала
N | észak | it-Tramuntana | Noord | północ | Norte | nord | severne | severno | Pohjoinen | Nord | К северу | Север
NE | észak-kelet | il-Grigal | Noordoost | północny wschód | Nordeste | nord-est | severo-východne | severovzhodno | Koillinen | Nordost | К северо-востоку | Североисток
E | kelet | il-Lvant | Oost | wschód | Leste | est | východne | vzhodno | Itä | Öst | К востоку | Исток
SE | dél-kelet | ix-Xlokk | Zuidoost | południowy wschód | Sudeste | sud-est | juho-východne | jugovzhodno | Kaakko | Sydost | К юго-востоку | Југоисток
S | dél | in-Nofsinhar | Zuid | południe | Sul | sud | južne | južno | Etelä | Syd | К югу | Југ
SW | dél-nyugat | il-Lbiċ | Zuidwest | południowy zachód | Sudoeste | sud-vest | juho-západne | jugozahodno | Lounas | Sydväst | К юго-западу | Југозапад
W | nyugat | il-Punent | West | zachód | Oeste | vest | západne | zahodno | Länsi | Väst | К западу | Запад
NW | észak-nyugat | il-Majjistral | Noordwest | północny zachód | Noroeste | nord-vest | severo-západne | severozahodno | Luode | Nordväst | К северо-западу | Северозапад
BI | nagy | kbir | Groot | duży | Grande | mare | veľký | velik | iso | Stor | большой | Велики
SM | kicsi | żgħir | Klein | mały | Pequeno | mic | malý | majhen | pieni | Liten | малый | Мали
OL | régi | qadim | Oud | stary | Antigo | vechi | starý | star | vanha | Gammal | старый | Стари
EW | új | ġdid | Nieuw | nowy | Novo | nou | nový | nov | uusi | Ny | новый | Нови
MP | mozgatható rész | parti mobbli | Beweegbaar deel | część ruchoma | Parte móvel | parte amovibilă | pohyblivá časť | premični del | liikkuva osa | Rörlig del | подвижная часть | Покретан део
FP | rögzített rész | parti fissa | Vast deel | część stała | Parte fixa | parte fixã | pevná časť | fiksni del | kiinteä osa | Fast del | неподвижная часть | Непокретан део
VA | változó | varjabbli | Variabel | zmienny | Variável | parte variabilă | premenlivá | spremenljiv | vaihtelee | Variabel | переменный | Променљива
GY | zöld úszó | baga ħadra | Groene boei | zielona pława | Boia verde | geaman- dura verde | zelená bója | zelena boja | vihreä poiju | Grön boj | зелёный буй | Зелена бова
RY | piros úszó | baga ħamra | Rode boei | czerwona pława | Boia vermelha | geaman-durã roşie | červená bója | rdeča boja | punainen poiju | Röd boj | красный буй | Црвена бова
CODUL MOTIVELOR
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
EVENT | event | Случай | Suceso | událost | Begivenhed | Veranstaltung | Sündmus | Συμβάν | Evénement | Događaj | avvenimento | Pasākums | Įvykis
WORK | work | Работи (действия) | Obras | práce | Arbejder | Arbeiten | Töötamine | Εργασίες | Travaux | Radovi | lavori | Darbs | Darbai
DREDGE | dredging | Драгажни работи | Dragado | bagrování | Opmudring | Baggerarbeiten | Süvendamine | Βυθοκόρηση | Dragage | Iskapanje | dragaggio | Bagarēšanas darbi | Dugno gilinimas
EXERC | exercises | Упражнения | Ejercicios | cvičení | Øvelser | Übungen | Õppused | Ασκήσεις | exercices | Vježbe | esercitazioni | Vingrinājumi | Pratybos
HIGWAT | high water | Високи води | Nivel de agua elevado | vysoký vodní stav | Højvande | Hochwasser | Kõrgvesi | Υψηλή στάθμη υδάτων | Crue | Visok vodostaj | piena | Augsts ūdens līmenis | Aukštas vandens lygis
HIWAI | water level of cautious navigation | Водно ниво изискващо повишено внимание при корабоплаване | Nivel de agua para navegación prudente | vodní stav zvýšené opatrnosti plavby | Forsigtig sejlads pga. vandstanden | Marke I. | Ettevaatliku laevatamise veetase | Στάθμη υδάτων προσεκτικής ναυσιπλοΐας | Niveau d'eau nécessitant une navigation prudente | Vodostaj oprezne plovidbe | livello idrometrico di prudenza per la navigazione | Ūdens līmenis bīstams kuģošanai | Laivybai pavojingas vandens lygis
HIWAII | prohibitory water level | Водно ниво възпрепятстващо корабоплаването | Nivel de agua de prohibición | vodní stav, při kterém je zakázaná plavba | Forbud mod sejlads pga. vandstanden | Marke II oder Marke III | Laevatamiseks keelatud veetase | Απαγορευτική στάθμη υδάτων | Niveau d'eau d'interdiction | Vodostaj zabrane plovidbe | livello idrometrico proibitivo | Ūdens līmenis, kurā kuģošana aizliegta | Laivybą draudžiantis vandens lygis
LOWWAT | low water | Ниски води | Nivel de agua bajo | nízký vodní stav | Lavvande | Niedrigwasser | Madal vesi | Χαμηλή στάθμη υδάτων | Etiage | Nizak vodostaj | livello di magra | Zems ūdens līmenis | Žemas vandens lygis
SHALLO | siltation | Плитчина | Sedimentación | naplaveniny | Aflejringer | Versandung | Mudastumine | Σχηματισμός ιλύος | Atterissement | Pličina | accumulo di sabbia | Aizsērēšana | Sąnašos
CALAMI | calamity | Бедствие | Accidente | havárie | Nødsituation | Havarie | Õnnetus | Καταστροφή | Accident | Havarija | calamità | Negadījums | Avarija
LAUNCH | launching | Спускане на вода | Lanzamiento | spouštění na vodu | Søsætning | Stapellauf | Veeskamine | Καθέλκυση | Mise à l'eau | Porinuće | varo | Kuģa nolaišana ūdenī | Laivo nuleidimas į vandenį
DECLEV | lowering water level | Понижаване на водното ниво | Nivel de agua en descenso | pokles vodní hladiny | Vandstanden sænkes | Senken des Wasserspiegels | Veetaseme vähenemine | Μειούμενη στάθμη υδάτων | Abaissement du niveau de l'eau | Vodostaj u opadanju | calo del livello idrometrico | Ūdens līmeņa pazemināšana | Vandens lygio slūgimas
FLOMEA | flow measurement | Измерване на оттока | Medición de caudal | měření průtoku | Flowmåling | Strömungsmessung | Voolu mõõtmine | Μέτρηση ροής | Opération de mesure de débit | Mjerenje protoka | portata idrometrica | Straumes ātruma noteikšana | Tėkmės parametrų matavimas
BLDWRK | building work | Строителни работи | Obras de construcción | stavební práce | Anlægsarbejder | Bauarbeiten | Ehitustöö | Κατασκευαστικές εργασίες | Travaux de construction | Izgradnja | lavori di costruzione | Būvdarbi | Statybos
REPAIR | repair | Ремонтни работи | Reparación | opravy | Reparation | Reparaturarbeiten | Remont | Επισκευές | Travaux de réparation | Popravci | intervento di riparazione | Remonts | Remontas
INSPEC | inspection | Инспекция | Inspección | inspekce | Inspektion | Inspektion | Inspekteeri-mine | Επιθεώρηση | Inspection | Inspekcija | ispezione | Inspekcija | Apžiūra
FIRWRK | fireworks | Взривни работи | Fuegos artificiales | ohňostroj | Fyrværkeri | Feuerwerk | Ilutulestik | Πυροτεχνήματα | Feux d'artifice | Vatromet | fuochi d'artificio | Liesmu darbi | Fejerverkai
LIMITA | limitations | Ограничения | limitaciones | omezení | Begrænsninger | Einschränkungen | Piirangud | Περιορισμοί | restriction de la navigation | Ograničenja | limitazioni alla navigazione | Ierobežojumi | Apribojimai
CHGFWY | changes of the fairway | Изменение на фарватера | Cambios en vía navegable | změny plavební dráhy | Ændring af farvandet | Änderungen des Fahrwassers | Muudatused faarvaatris | Μεταβολές στον δίαυλο | modification du chenal navigable | Promjene u plovnom putu | modifiche del canale navigabile | Izmaiņas kuģu ceļā | Pasikeitimai farvateryje
CONSTR | constriction of fairway | Изграждане на воден път | Estrechamiento de vía navegable | zúžení vodní cesty | Indsnævring af vandvejen | Einengung des Fahrwassers | Faarvaatri kontriktsioon | Κατασκευή πλωτής οδού | rétrécissement du chenal navigable | Suženje plovnog puta | restrizione del canale navigabile | Ūdens ceļa sašaurinājums | Farvaterio susiaurėjimas
DIVING | diver under the water | Водолаз под водата | Presencia de submarinistas | práce pod vodou | Dykkere i arbejde | Taucher unter Wasser | Tuuker vee all | Υποβρύχιες εργασίες | plongeurs au travail | Ronilac pod vodom | sommozzatore in immersione | Ūdenslīdēju darbi | Vandenyje naras
SPECTR | special transport | Специализиран транспорт | Transporte especial | zvláštní přeprava | Særlig transport | Sondertransport | Erivedu | Ειδικές μεταφορές | transport spécial | Specijalni prijevoz | trasporto speciale | Īpašs transports | Specialus transportas
EXT | extensive sluicing | Активно изпускане на вода | Barrido extensivo | rozsáhlé vymílání | Omfattende slusedrift | extreme Dotierung | Laialdane lüüsikasutus | Εκτεταμένη εκκένωση υδατοφράτκη | Service étendu | Izrazito istjecanje | regolazione intensiva della portata idrometrica | Liela pārplūde | Gausus vandens nuleidimas
MIN | minimum sluicing | Минимално изпускане на вода | Barrido mínimo | minimální vymílání | Minimum slusedrift | minimale Dotierung | Minimaalne lüüsikasutus | Ελάχιστη εκκένωση υδατοφράκτη | Service minimum | Minimalno istjecanje | regolazione minima della portata idrometrica | Minimāla pārplūde | Minimalus vandens nuleidimas
SOUND | sounding works | Дълбочинно-измервателни работи | Obras de sondeo | měřenί plavební hloubky | Oplodning | Peilarbeiten | Loodimistööd | Εργασίες ηχοβολισμού | Travaux de sondage | Mjerenja dubine | lavori di scandaglio | Zondēšana | Zondavimo darbai
OTHER | others | Друго | Otros | jiné | Andet | andere | Muud | Λοιπά | Autres | Ostalo | diversi | Citi | Kita
INFSER | info service | Информационна служба (няма значение за безопасността на корабоплаването и не изисква планиране на рейса) | Servicio de información | Informační servis (netýká se bezpečnosti ani plánování plavby) | Informationstjeneste | Informationsservice | Teabeteenus (ei ole seotud ohutusega ega ole vajalik reisi korraldamisel) | Πληροφορίες (δεν έχει σχέση με την ασφάλεια και δεν χρειάζεται για τον προγραμματισμό του ταξιδίου) | Information (n'a pas d'impact sur la sécurité et n'est pas nécessaire au calcul d'itinéraire) | Informacijska usluga (ne odnosi se na sigurnost i nije potrebna za planiranje putovanja) | servizio informazioni (senza rilevanza ai fini della sicurezza e della pianificazione dell'itinerario) | Informācijas dienests (nav saistīts ar drošumu un nav vajadzīgs reisa plānošanai) | Informacija (nesusijusi su saugumu ir nebūtina planuojant reisą)
STRIKE | strike | Удар | Huelga | stávka | Strejke | Streik | Streik | Απεργία | Grève | Štrajk | sciopero | Streiks | Streikas
FLOMAT | floating material | Плаващи материали | Material flotante | plovoucí materiál | Flydende materiel | Treibgut | Ujuvmaterjal | Υλικό που επιπλέει | Embâcle | Plutajući predmeti | materiale flottante | Peldošs objekts | Plūduriuojantys daiktai
EXPLOS | explosives clearing operation | Взривни работи за разчистване | Operación de limpieza con explosivos | zneškodňování výbušnin | Rydning af sprængstoffer | Bombenräumung | Demineerimisoperatsioon | Επιχείριση άρσης ναρκοπεδίου | opération de déminage | Raščišćavanje eksplozivom | operazione di sminamento | Sprāgstvielu neitralizēšanas operācija | Sprogmenų šalinimo operacija
OBUNWA | obstruction under water | Подводно препятствие | Obstrucción bajo el agua | plavební překážka | Hindring under vandlinjen | Einschränkung unter Wasser | Veealune takistus | Υποβρύχια παρεμπόδιση | objet immergé | Prepreka ispod vode | ostruzione sommersa | Zemūdens šķērslis | Povandeninė kliūtis
FALMAT | falling material | Падащи материали | Material desprendido | padající materiál | Faldende materiel | herabfallende Gegenstände | Kukkuvad esemed | Πτώση αντικειμένων | chutes d’objets | Padajući predmeti s visine | caduta di materiale | Krītošs objekts | Krentantys daiktai
DAMMAR | damaged marks/signs | Повредена сигнализация/знаци | Marcas/señales estropeadas | poškozená signalizace | Beskadigede sømærker/skiltning | beschädigte Zeichen | Kahjustatud märgid/viidad | Κατεστραμμένα σημεία/σήματα | panneaux de signalisation endommagés | Oštećene oznake | segnaletica danneggiata | Bojātas zīmes/norādes | Pažeistos žymos / ženklai
HEARIS | health risk | Опасност за здравето | Riesgo para la salud | zdravotní riziko | Sundhedsrisiko | Gesundheitsgefahr | Terviseoht | Κίνδυνος για την υγεία | risques pour la santé | Opasnost za zdravlje | rischio per la salute | Veselības risks | Pavojus sveikatai
ICE | ice | Лед | Hielo | led | Is | Eis | Jää | Πάγος | glace | Led | ghiaccio | Ledus | Ledas
OBSTAC | obstacle | Препятствие | Obstáculo | překážka | Hindring | Schifffahrtshindernis | Takistus | Εμπόδιο | obstacle à la navigation | Prepreka | ostacolo alla navigazione | Šķērslis | Kliūtis
CHGMAR | change marks | Изменение в сигнализацията | Cambio de señalización | změna značení | Ændret signalering | Schifffahrtszeichen geändert | Muudatus-tähis | Αλλαγή σημείων | Signalisation modifée | Promjena navigacijske oznake | segnaletica modificata | Mainītas zīmes | Ženklų keitimas
HIGVOL | high voltage cable | Високо напрежение | Línea de alta tensión | vedení vysokého napětí | Højspændingskabler | Hochspannungsleitung | Kõrgepinge-juhtivus | Αγωγός υψηλής τάσης | Ligne haute tension | Visokonaponski kabel | alta tensione | Augstspriegums | Aukštos įtampos kabelis
ECDISU | Inland ECDIS update | Обновяване на ECDIS | Actualización ECDIS fluvial | aktualizace informací Inland ECDIS | Inland ECDIS update | Inland ECDIS Update | Uuendatud sisemaine ECDIS | Επικαιροποίηση ECDIS εσωτ. ναυσ. | Mise à jour des données Inland ECDIS | Ažuriranje sustava Inland ECDIS | aggiornamento ECDIS interno | Inland ECDIS informācijas atjaunošana | Inland ECDIS informacijos atnaujinimas
LOCRUL | local rules of traffic | Местни (локални) правила за движение | Normas locales de tráfico | místní úprava plavebních předpisů | Lokale trafikregler | lokal gültige Verkehrsvorschriften | Kohalikud liiklusees-kirjad | Τοπικοί κανόνες κυκλοφορίας | règlements particuliers de police | Lokalni prometni propisi | regole di traffico locali | Vietēji satiksmes noteikumi | Vietinės laivų eismo taisyklės
NEWOBJ | new object | Нов обект | Nuevo objeto | nový objekt | Nyt objekt | neues Objekt | Uus ese | Νέο αντικείμενο | Nouvel objet | Novi objekt | nuovo oggetto | Jauns objekts | Naujas objektas
MISECH | false radar echos | Грешно радарно ехо | Ecos radar falsos | falešná ozvěna | Falsk radarekko | Geisterechos | Radari vale kajasignaal | Εσφαλμένα σήματα ραντάρ | Faux échos radar | Pogrešan radarski odziv | rilevazioni radar distorte | Maldigs radara ehosignals | Klaidingi radaro rodmenys
VHFCOV | radio coverage | Радио покритие (обхват) | Cobertura de radio | rádiové pokrytí | Radiodækning | Funkabdeckung | Raadio leviala | Κάλυψη ασυρμάτου | Couverture radio | Radijska pokrivenost | copertura radio | Radiosignālu pārklājums | Radijo ryšio zona
REMOBJ | removal of object | Демонтиране на обект | Retirada de un objeto | odstranění objektu | Fjernelse af objekt | Bergungsarbeiten | Eseme eemaldamine | Απομάκρυνση αντικειμένου | enlèvement d'objet | Uklanjanje objekta | rimozione di oggetti | Objekta noņemšana | Objekto šalinimas
LEVRIS | rising water level | Растящо водно ниво | Nivel de agua en ascenso | stoupající vodní stav | Stigende vandstand | steigender Wasserstand | Veetaseme tõusmine | Αυξανόμενη στάθμη υδάτων | Eaux montantes | Vodostaj u porastu | livello idrometrico in aumento | Kāpjošs ūdens līmenis | Kylantis vandens lygis
SPCMAR | special marks | Специална сигнализация | Señalización especial | zvláštní signalizace | Særlig signalering | besondere Zeichen | Eritähised | Ειδικά σημεία | Signalisation spéciale | Posebne oznake | segnaletica speciale | Īpašas zīmes | Specialieji ženklai
WERMCO | weather conditions | Метеорологични условия | Condiciones meteorológicas | povětrnostní podmínky | Vejrforhold | Wetterbedingungen | Ilmastikuolud | Καιρικές συνθήκες | conditions météo | Vremenski uvjeti | condizioni meteorologiche | Laikapstākļi | Oro sąlygos
CODUL MOTIVELOR
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
EVENT | rendezvény | avveniment | Evenement | Impreza | Evento | eveniment | udalosť | prireditev | Tapahtumat | Evenemang | Мероприятие | Догађај
WORK | munkálatok | xogħol | Werkzaamheden | Prace | Trabalhos | lucrări | práce | delo | Työt | Arbeten | Работы | Радови
DREDGE | kotrási munkálatok | tħammil | Baggeren | Pogłębianie | Dragagens | lucrări de dragaj | bagrovanie | poglabljanje dna | Ruoppaustyöt | Muddring | Землечерпательные работы | Багеровање
EXERC | gyakorlatok | eżerċizzji | Oefeningen | Ćwiczenia | Exercícios | exerciții | cvičenia | vaje | Harjoitukset | Övningar | Испытания | Вежбе
HIGWAT | magas vízállás | livell għoli tal-ilma | Hoogwater | Wysoki stan wody | Nível de cheia | ape mari | vysoký vodný stav | visok vodostaj | Korkea vesi | Högvatten | Высокая вода | Велика вода
HIWAI | kíméletes hajózási vízszint | livell tal-ilma li jeħtieġ navigazzjoni b’attenzjoni | Waterstand met beperkte scheepvaart | Stan wody wymagający ostrożnej żeglugi | Nível da água que obriga a navegação prudente | nivelul apei de avertizare pentru navigație | vodný stav pre opatrnú plavbu | vodostaj, ki zahteva previdno plovbo | varovaista liikkumista edellyttävä vedenkorkeus | Försiktig navigering p.g.a. vattennivån | Уровень опасный для судоходства | Водостај при којем је потреба опрезна пловидба
HIWAII | tilalmi vízszint | livell tal-ilma projbittiv | Waterstand met vaarverbod | Stan wody uniemożliwiający żeglugę | Nível da água que impossibilita a navegação | nivelul apei de interdicție | vodný stav pri ktorom je zakázaná plavba | vodostaj, ki ne dovoljuje plovbe | kiellon aiheuttava vedenkorkeus | Förbud p.g.a. vattennivån | Уровень запрещающий судоходство | Водостај при којем се забрањује пловидба
LOWWAT | alacsony vízállás | livell baxx tal-ilma | Laagwater | Niski stan wody | Nível de estiagem | ape mici | nízky vodný stav | nizek vodostaj | Matala vesi | Lågvatten | Низкая вода | Мала вода
SHALLO | gázlóképződés | sediment | Verondieping | Mielizna | Assoreamento | întinsură | naplaveniny | usedlina | Liettyminen | Slam-avsättning | Обмеление | Плићак
CALAMI | havaria/baleset | diżastru | Calamiteit | Wypadek | Acidente | calamitate | havária | nesreča | Onnettomuus | Olycka | Авария | Хаварија
LAUNCH | vízrebocsájtás | varar | Tewaterlating | Wodowanie | Lançamento à água | lansare la apă | spúšťanie na vodu | splavitev | Vesillelasku | Sjösättning | Спуск на воду | Поринуће
DECLEV | vízszint csökkentése | livell tal-ilma li qed jitbaxxa | Waterstandsverlaging | Spadek poziomu wody | Descida do nível da água | nivelul apei în scădere | klesajúca vodná hladina | nižanje vodostaja | Vedenkorkeuden laskeminen | Sjunkande vattennivå | Понижение уровня воды | Водостај у опадању
FLOMEA | áramlás mérése | kejl tal-fluss | Stroomsnelheidsmeting | Pomiar prądu | Caudal | operațiune de măsurare a debitului | meranie prietoku | merjenje pretoka | Virtauksen mittaaminen | Flödes-mätning | измерение скорости течения | Мерење протицаја
BLDWRK | építési munkálatok | xogħol ta’ bini | Bouwwerkzaamheden | Roboty budowlane | Obras | lucrări de construcții | stavebné práce | gradbena dela | Rakennustyöt | Byggnads-arbete | Строительство | Радови
REPAIR | javítási munkálatok | tiswija | Herstelwerkzaamheden | Prace remontowe | Reparações | lucrări de reparații | opravy | popravilo | Korjaustyöt | Reparations-arbete | Ремонтные работы | Поправка
INSPEC | szemle | spezzjoni | Inspectiewerkzaamheden | Inspekcja | Inspeção | inspecție | inšpekcia; prehliadka; kontrola | inšpekcijski pregled | Tarkastus | Inspektion | Инспекция | Инспекција
FIRWRK | tűzijáték | logħob tan-nar | Vuurwerk | Sztuczne ognie | Fogo de artifício | focuri de artificii | ohňostroj | ognjemet | Ilotulitus | Fyrverkerier | Взрывные работы | Ватромет
LIMITA | korlátozás | restrizzjonijiet | Beperkingen | Ograniczenia | Restrições | restricții | obmedzenia | omejitve | Rajoitukset | Begränsningar | Ограничения | Ограничења
CHGFWY | hajóútváltozás | bidliet tal-kanali navigabbli | Verandering van de vaarweg | Zmiany toru wodnego | Alterações no canal navegável | schimbări șenal navigabil | zmeny v plavebnej dráhe | spremembe na plovni poti | muutokset väylällä | Ändringar av farleden | изменение фарватера | Промене пловног пута
CONSTR | hajóútszűkület | restrizzjoni tal-kanal navigabbli | Beperking van de vaarweg | Zwężenie toru wodnego | Estreitamento da via navegável | îngustare cale navigabilă | zúženie vodnej cesty | zoženje plovne poti | vesiväylän kaventuminen | Smalare vattenväg | Сужение фарватера | Сужење пловног пута
DIVING | vízalatti munkák | bugħaddas taħt l-ilma | Duikwerkzaamheden | Nurek pod wodą | Presença de mergulhadores | scafandru în apă | potápač pod vodou | dela pod vodo | sukeltaja veden alla | Dykare i vattnet | Водолазные работы | Подводни радови
SPECTR | különleges szállítás | trasport speċjali | Bijzonder vervoer | Transport specjalny | Transporte especial | transport special | špeciálna preprava | posebni prevoz | erikoiskuljetus | Special-transport | специальная перевозка | Специјални транспорт
EXT | nagymértékű vízeresztés | kontroll estensiv tal-ilma | Uitgebreid schutbedrijf | Intensywne śluzowanie | Regime de descarga máximo | trafic de ecluză intens | rozsiahle dotovanie | ekstenzivno odtekanje | laajamittainen sulutus | Omfattande drift | значительный спуск воды | Значајно истицање
MIN | minimális vízeresztés | kontroll minimu tal-ilma | Minimaal schutbedrijf | Minimalne śluzowanie | Regime de descarga mínimo | trafic de ecluză redus | minimálne dotovanie | minimalno odtekanje | vähimmäissulutus | Minimidrift | минимальный спуск воды | Минимално истицање
SOUND | mélységmérési munka | xogħlijiet ta’ kejl tal-fond | Peilwerkzaamheden | Pomiary głębokości | Sondagens | lucrări de sondaj | sondovacie práce | merjenje globine | luotaustyöt | Lodnings-arbete | промерные работы | Мерења дубина
OTHER | egyéb | oħrajn | Overige | Inne | Outros | altele | Iné | drugo | muutokset väylällä | Annat | другое | Остало
INFSER | Tájékoztatás (nem biztonsági közlemény és útiterv készítéséhez nem szükséges) | servizz ta’ informazzjoni | Informatieservice | Serwis informacyjny (informacje niezwiązane z bezpieczeństwem i niewymagane do planowania rejsu) | Serviço de informações (sem relevância para a segurança e para a planificação de viagem) | mesaj informativ (nu se referă la siguranța traficului și nu este necesar pentru planificarea voiajelor) | Informačná služba (netýka sa bezpečnosti ani plánovania plavby) | informacijska služba | Tietopalvelu (ei ole olennainen turvallisuuden kannalta eikä tarpeen matkan suunnittelussa) | Informations-tjänst (inte säkerhets-relaterad och inte nödvändig för färdplanering) | Информационная служба (не значительна для безопасности и нет необходимости в ней для планирования рейса) | Услуга информисања (није релевантна за безбедност пловидбе и није потребна за планирање путовања)
STRIKE | sztrájk | strajk | Staking | Strajk | Greve | grevă | štrajk | stavka | Lakko | Strejk | Забастовка | Удар
FLOMAT | úszó anyag | materjal f'wiċċ l-ilma | Drijvend materiaal | Materiał pływający | Material flutuante | material plutitor | plávajúci materiál | plavajoči predmeti | Kelluva aines | Flytande föremål | Плавучий материал | Плутајући материјал
EXPLOS | robbanóanyag eltávolítás | operazzjoni ta’ tneħħija ta’ splussivi | Verwijderen van explosieven | Operacja usuwania materiałów wybuchowych | Operação de desminagem | explozive pentru degajare | zneškodňovanie výbušnín | odstranjevanje eksplozivov | Räjähteiden raivaaminen | Röjning av explosivt material | Разминирование | Операција разминирања
OBUNWA | víz alatti akadály | ostaklu taħt l-ilma | Belemmering onder water | Przeszkoda podwodna | Obstrução subaquática | obstacol subacvatic | prekážka pod vodou | zapora pod vodo | Vedenalainen este | Undervattenshinder | Препятствие под водой | Препрека под водом
FALMAT | lehulló anyagok | materjal qed jaqa’ | Vallend materiaal | Materiał spadający | Queda de materiais | material care cade | padajúci materiál | padajoči predmeti | Putoava aines | Fallande föremål | Падающий материал | Матаријал који пада
DAMMAR | sérült jelzés | sinjali bil-ħsara | Beschadigde markeringen/symbolen | Uszkodzone znaki/sygnały | Marcas/sinais danificados | semnale avariate | poškodené signálne znaky | poškodovane oznake/znaki | Vaurioituneet merimerkit | Skadade markeringar/signaler | Поврежденные знаки/огни | Оштећен знак
HEARIS | egészségügyi kockázat | riskju għas-saħħa | Gezondheidsrisico | Zagrożenie dla zdrowia | Risco para a saúde | risc de îmbolnăvire | zdravotné riziko | tveganje za zdravje | Terveysriski | Hälsorisk | Риск здоровью | Опасноист по здравље
ICE | jég | silġ | IJs | Lód | Gelo | gheață | ľad | led | Jää | Is | лед | Лед
OBSTAC | akadály | ostaklu | Obstakel | Przeszkoda | Obstáculo | obstacol | prekážka | ovira | Este | Hinder | Препятствие (помеха) | Препрека
CHGMAR | forgalmi jelek változtatása | bidla fis-sinjali | Gewijzigde markering | Zmiana oznakowania | Alteração da sinalização | semnalizare modificată | zmena značenia | sprememba oznak | Merkit muuttuneet | Ändrad märkning | Изменение СНО | Промена знака
HIGVOL | nagy feszültségű átfeszítés | kejbil b’voltaġġ għoli | Hoogspanningskabel | Linia wysokiego napięcia | Linha de alta tensão | linie de înaltă tensiune | vedenie vysokého napätia | visokonapetostni kabel | Korkeajännitejohto | Högspänningsledning | высоковольтный кабель | Кабл под високим напоном
ECDISU | Inland ECDIS frissítés | aġġornament tal-ECDIS Interna | Inland ECDIS-update | Aktualizacja Inland ECDIS | Atualização ECDIS-fluvial | actualizarea datelor ECDIS | aktualizácia Inland ECDIS | posodobitev celinskega ECDIS | Sisävesiliikenteen ECDIS:n päivitys | Uppdatering av inlands-ECDIS | Обновление информации для Inland ECDIS | Ажуриран Inland ECDIS
LOCRUL | helyi közlekedési rend (R) | regoli lokali tat-traffiku | Lokale verkeersregels | Miejscowe przepisy ruchu statków | Regras de tráfego locais | regulamente locale de trafic | lokálne pravidlá plavby | lokalna prometna pravila | paikalliset liikennöintisäännöt | Lokala trafikregler | Местные правила судоходства | Локална правила пловидбе
NEWOBJ | Új objektum | oġġett ġdid | Nieuw object | Nowy obiekt | Novo objeto | obiect nou | nový objekt | nov objekt | Uusi kohde | Nytt föremål | Новый объект | Нови објекат
MISECH | hamis radarvisszhangok | eki foloz tar-radar | Valse radarecho's | Fałszywe echa radarowe | Ecos radar falsos | ecou radar fals | falošná odozva | napačni odmevi radarja | Virheellisiä tutkakaikuja | Falska radarekon | Ложная радарная цель | Лажни радарски одраз
VHFCOV | rádiós lefedettség | kopertura tar-radju | Radiodekking | Pokrycie radiowe | Cobertura rádio | acoperire radio | rádiové pokrytie | pokritost radijskih zvez | Radion kuuluvuusalue | Radiotäckning | Покрытие радиосигналом | Покривеност радио сигналом
REMOBJ | mentési munkálatok | tneħħija ta’ oġġett | Verwijderen van object | Usuwanie objektu | Remoção de objetos | schimbarea obiectului | odstránenie objektu | odstranitev objekta | Kohteen poistaminen | Bärgning av föremål | Удаление объекта | Уклањање објекта
LEVRIS | emelkedő vízállás | livell tal-ilma qed jogħla | Waterstandsverhoging | Wzrost stanu wody | Subida do nível da água | creşterea nivelului apei | stúpajúca vodná hladina | višanje vodostaja | Vedenkorkeus nousee | Stigande vattennivå | Повышение уровня воды | Ниво воде у порасту
SPCMAR | speciális jelek | sinjali speċjali | Bijzondere markeringen | Znaki specjalne | Sinalização especial | semnalizare specială | špeciálne značenie | posebne oznake | Erikoismerkit | Särskilda markeringar | Специальные знаки | Посебне ознаке
WERMCO | időjárási viszonyok | kundizzjonijiet tat-temp | Weersomstandigheden | Warunki pogodowe | Condições meteorológicas | condiții meteorologice | poveternostné podmienky | vremenske razmere | Sääolosuhteet | Väderförhållanden | метеорологические условия | временски услови
CODUL DE REFERINȚĂ
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
NAP | NAP | NAP | NAP | NAP | Normal vandstand i Amsterdam | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP
KP | channel level | Пегел на канала | Nivel local | kanálový vodočet | Kanalniveau | Kanal Pegel | kp | Στάθμη υδάτων καναλιού | Côte locale | Vodomjer u kanalu | livello canale | Kanāla ūdens līmeņrādis | Kanalo vandens lygis
FZP | FZP | FZP | Nivel de los canales frisones | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP
ADR | Adria | Адриатическа система | Mar Adriático | přes Adrii | Adria | über Adria | Adria | Αδριατική | Mer Adriatique | Razina Jadranskog mora | livello adriatico | Adrijas sistēma | Adrijos sistema
TAW | TAW/DNG | TAW/DNG | 2a nivelación general/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG
PUL | Pulkovo 1942 | Пулково 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942
NGM | Ngm | Нгм | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm
ETRS | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89
POT | Potsdamer Datum | Координатна система Потсдам | Potsdamer Datum | Postupimské datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamas koordinātu sistēma | Potsdamo koordinačių sistema
LDC | low water level Danube Commission | Ниско водно ниво по Дунавската комисия | Comisión del Danubio, nivel bajo de agua | nízký plavební stav podle Dunajské komise | Lav vandstand defineret af Donau-kommissionen | RNW gemäß Donaukommission | Madala veetaseme Doonau komisjon | Χαμηλή στάθμη υδάτων, Επιτροπή Δούναβη | Commission du Danube, niveau bas des eaux | Niski plovidbeni vodostaj po Dunavskoj komisiji | livello di magra Commissione del Danubio | Zems ūdens līmenis, Donavas komisija | Žemas vandens lygis, Dunojaus komisija
HDC | high water level Danube Commission | Високо водно ниво по Дунавската комисия | Comisión del Danubio, nivel alto de agua | nejvyšší plavební vodní stav podle Dunajské komise | Høj vandstand defineret af Donau-kommissionen | HSW gemäß Donaukommission | Kõrge veetaseme Doonau komisjon | Υψηλή στάθμη υδάτων, Επιτροπή Δούναβη | Commission du Danube, niveau haut des eaux | Visoki plovidbeni vodostaj po Dunavskoj komisiji | livello di piena Commissione del Danubio | Augsts ūdens līmenis, Donavas komisija | Aukštas vandens lygis, Dunojaus komisija
ZPG | zero point of gauge | Нула на пегела | Punto de referencia de nivel | nulový bod vodočtu | Profilens nulpunkt | Pegelnullpunkt | Mõõtmiskoha nullpunkt | Μηδενικό σημείο μετρητή | point de référence de niveau | Nulta točka vodomjerne letve | zero idrometrico | Ūdens līmeņrāža nulles punkts | Nulinis vandens lygio rodmuo
GLW | equivalent low water level | Еквивалентно ниско водно ниво | Estiaje | ekvivalentní nízký vodní stav | Tilsvarende lav vandstand | Gleichwertiger Wasserstand (GLW) | Madala veetaseme ekvivalent | Ισοσύναμη χαμηλή στάθμη υδάτων | étiage | Ekvivalentni niski vodostaj | livello equivalente di magra | Minimālais ūdens līmenis | Žemo vandens lygio ekvivalentas
HSW | highest navigable water level | Най-високо корабоплавателно ниво | Nivel máximo navegable | nejvyšší plavební vodní stav | Højeste farbare vandstand | Höchster Schifffahrtswasserstand (HSW) | kõrgeim navigeeritav veetase | Υψηλότερη πλεύσιμη στάθμη υδάτων | Plus hautes eaux navigables | Maksimalni vodostaj dozvoljene plovidbe | massimo livello idrometrico navigabile | Augstākais kuģojamais ūdens līmenis | Aukščiausias laivybos vandens lygis
LNW | Low Navigable Water | Ниско корабоплавателно ниво | Nivel mínimo navegable | nízký plavební vodní stav (národní) | Lav farbar vandstand | RNW (national) | madal navigeeritav vesi | Χαμηλή πλεύσιμη στάθμη υδάτων | Plus basses eaux navigable | Niski vodostaj dozvoljene plovidbe | livello di magra navigabile | Zemākais kuģojamais ūdens līmenis | Žemas laivybos vandens lygis
HNW | High Navigable Water | Високо корабоплавателно ниво | Nivel alto navegable | nejvyšší plavební vodní stav (národní) | Høj farbar vandstand | HSW (national) | kõrge navigeeritav vesi | Υψηλή πλεύσιμη στάθμη υδάτων | Hautes eaux navigables | Visoki vodostaj dozvoljene plovidbe | livello di piena navigabile | Augsts kuģojamais ūdens līmenis | Aukštas laivybos vandens lygis
IGN | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69
WGS | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS84 | WGS 84 | WGS 84 | WGS 84 | WGS 84
RN | normal level | Нормално ниво | Nivel normal | normální stav | Normalniveau | Normaler Pegel | normaaltase | Κανονική στάθμη υδάτων | Retenue normale | Normalna razina | livello idrometrico normale | Normāls ūdens līmenis | Normalus lygis
HBO | high water level of attention | Високо водно ниво преди наводнение | Atención por nivel alto de agua | vysoký vodní stav před vybřežením | Høj vandstand, der kræver forsigtighed | Hochwasser, das besondere Vorsicht erfordert | tähelepanu nõudev kõrge veetase | Υψηλή στάθμη υδάτων, απαιτείται προσοχή | cote d'attention | Visok vodostaj — stanje pripravnosti | livello di piena da sorvegliare | Ievērojami augsts ūdens līmenis | Pavojingai aukštas vandens lygis
CODUL DE REFERINȚĂ
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP | NAP
KP | csatornavíz-szint | livell tal-kanal | Kanaalpeil | kp | Cota local | nivelul de referință local | prevádzková úroveň hladiny v kanáli | vodostaj v kanalu | kp | kp | Судоходный уровень канала | upozorenje od velike vode
FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP | FZP
ADR | az Adriai tenger szintje felett | Adria | Adriapeil | Adria | Adriático | Marea Adriatică | výškový systém ADRIA | nivo Jadranskega morja | Adria | Adria | Адриатическая система | Ниво Јадранског мора
TAW | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG | TAW/DNG
PUL | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Pulkovo 1942 | Пулково 1942 | Пулково 1942
NGM | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Ngm | Нгм | Ngm
ETRS | ETRS89 | ETRS89 | Etrs89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89 | ETRS89
POT | potsdami dátum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Potsdamer Datum | Координатная система Потсдам | Potsdamer датум
LDC | Dunabizottsági hajózási kisvízszint (LKHV) | livell baxx tal-ilma tal-Kummissjoni tad-Danubju | Laagwaterpeil Donaucommissie | niski stan wody wg Komisji Dunajskiej | Nível baixo da água, Comissão do Danúbio | nivelul apei minim — Comisia Dunării | hladina nízkej regulačnej a plavebnej vody podľa DK | nizek vodostaj po Donavski komisiji | Tonavan suojelukomission mukainen pieni vedenkorkeus | Lågvattennivå enligt Donau-kommissionen | Низкий уровень воды ДК | Ниски пловидбени ниво према Дунавској комисији
HDC | Dunabizottsági hajózási nagyvízszint (LNHV) | livell għoli tal-ilma tal-Kummissjoni tad-Danubju | Hoogwaterpeil Donaucommissie | wysoki stan wody wg Komisji Dunajskiej | Nível alto da água, Comissão do Danúbio | nivelul apei maxim — Comisia Dunării | hladina vysokej plavebnej vody podľa DK | visok vodostaj po Donavski komisiji | Tonavan suojelukomission mukainen suuri vedenkorkeus | Högvattennivå enligt Donau-kommissionen | Высокий уровень воды ДК | Високи пловидбени ниво према Дунавској комисији
ZPG | vízmérce nulla pontja | punt żero tal-kejl | Referentiepunt van de peilschaal | punkt zerowy wodowskazu | Ponto zero do fluviómetro | zero miră | nulový bod mernej stanice | ničelna točka vodomera | vedenkorkeusmittarin nollakohta | Vattenståndsmätarens nollpunkt | ноль уровня | ‘0’ водомера
GLW | egyenértékű kisvízszint | livell baxx tal-ilma ewkivalenti | Gelijkwaardige laagwaterstand | równoważny niski stan wody | Nível baixo equivalente da água | nivelul apei minim echivalent | ekvivalentná nízka vodná hladina | ekvivalent nizkega vodostaja | vastaava pieni vedenkorkeus | Ekvivalent lågvattennivå | Низкий уровень воды | Еквивалент малој води
HSW | legnagyobb hajózási vízszint (HNV) | l-ogħla livell tal-ilma navigabbli | Hoogste scheepvaartwaterstand | najwyższy stan wody dopuszczający żeglugę | Nível máximo navegável | cel mai mare nivel al apei pentru navigație | najvyššia plavebná hladina | najvišji vodostaj, pri katerem je mogoča plovba | suurin kulkukelpoinen vedenkorkeus | Högsta navigerbara vattennivå | Наивысший судоходный уровень | Највиши водостај за пловидбу
LNW | hajózási kisvízszint (HKV) | Ilma Navigabbli Baxx | Laagste scheepvaartwaterstand (nationaal) | niski stan wody dopuszczający żeglugę | Nível mínimo navegável | nivelul apei minim pentru navigație | nízka plavebná hladina | nizek vodostaj, pri katerem je mogoča plovba | Matala kulkukelpoinen vesi | Lågt navigerbart vatten | Минимальный судоходный уровень | Ниски пловидбени ниво
HNW | hajózási nagyvízszint (HNV) | Ilma Navigabbli Għoli | Hoogste scheepvaartwaterstand (nationaal) | wysoki stan wody dopuszczający żeglugę | Nível alto navegável | nivelul apei maxim pentru navigație | vysoká plavebná hladina | visok vodostaj, pri katerem je mogoča plovba | Korkea kulkukelpoinen vesi | Högt navigerbart vatten | максимальный судоходный уровень | Високи пловидбени ниво
IGN | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69 | IGN 69
WGS | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | SGM 84 | WGS 84 | WGS 84 | WGS 84 | WGS 84 | WGS84 | WGS 84
RN | szokásos szint | livell normali | Normaal peil | poziom normalny | Nível normal | nivelul apei normal | normálna úroveň | običajen vodostaj | normaali taso | Normal nivå | Нормальный уровень воды | Нормални ниво
HBO | LNHV-t meghaladó vízállás | livell għoli tal-ilma li jeħtieġ attenzjoni | Hoogwaterpeil, aandacht geboden | alarmowy stan wody | Nível alto da água que obriga a navegação atenta | cota de atenție | vysoká hladina — stav bdelosti | opozorilo glede visokega vodostaja | suuri vedenkorkeus, edellyttää erityistä huomiota | Högvattennivå som kräver uppmärksamhet | высокий уровень воды, угроза наводнения | upozorenje od velike vode
CODUL REGIMULUI
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
NO | normal | Нормално водно ниво | Normal | normální vodní stav | Normal vandstand | Regime: Normal Wasserstand | Tavaline | Κανονική | Hauteur d'eau normale | Režim: normalni vodostaj | normale | Normāls ūdens līmenis | Normalus vandens lygis
HI | high | Високи води | Alto | vysoký vodní stav | Højvande | Hochwasser | Kõrge | Υψηλή | Plus Hautes Eaux Navigables | Režim: visok vodostaj | livello idrometrico elevato | Augsts ūdens līmenis | Aukštas vandens lygis
II | prohibitory water level | Водно ниво възпрепятстващо корабоплаването | Nivel de agua de prohibición | vodní stav, při kterém je zakázaná plavba | Vandstand, hvor sejlads forbydes | Sperrung wegen Hochwasser | Keelatud veetase | Απαγορευτική στάθμη υδάτων | Niveau d'eau d'interdiction | Vodostaj zabrane plovidbe | livello idrometrico proibitivo | Ūdens līmenis, kurā kuģošana aizliegta | Laivybą draudžiantis vandens lygis
I | water level of cautious navigation | Водно ниво изискващо корабоплаване с повишено внимание | Nivel de agua para navegación prudente | vodní stav zvýšené opatrnosti plavby | Vandstand, hvor sejlads udføres med særlig agtpågivenhed | Marke I. | Ettevatliku laevatamise veetase | Στάθμη υδάτων προσεκτικής ναυσιπλοΐας | Niveau d'eau nécessitant une navigation prudente | Vodostaj oprezne plovidbe | livello idrometrico di prudenza per la navigazione | Ūdens līmenis bīstams kuģošanai | Laivybai pavojingas vandens lygis
NN | normal water level for navigation | Нормално водно ниво за корабоплаване | Nivel de agua normal para navegación | normální vodní stav pro plavbu | Normal vandstand for skibsfart | normaler Schifffahrtswasserstand | Laevatami-seks normaalne veetase | Κανονική στάθμη υδάτων ναυσιπλοΐας | Niveau Normal de Navigation | Vodostaj normalne plovidbe | livello idrometrico normale per la navigazione | Normāls ūdens līmenis kuģošanai | Laivybai tinkamas vandens lygis
LO | low water | Ниски води | Nivel de agua bajo | nízký vodní stav | Lavvande | Niedrigwasser | Madal vesi | Χαμηλή στάθμη υδάτων | Etiage | Nizak vodostaj | livello di magra | Zems ūdens līmenis | Žemas vandens lygis
CODUL REGIMULUI
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
NO | normál vízállás | normali | Normaal | normalny | Nível da água normal | nivelul normal | normálny vodný stav | normalen | Normaali | Normal | Нормальный уровень | Режим нормалног водостаја
HI | magas vízállás | għoli | Hoogwaterregime | wysoki | Nível da água alto | nivelul maxim navigabil | vysoký vodný stav | visok | Suuri | Hög | Высокая вода (паводок) | Велика вода
II | tilalmi vízszint | livell tal-ilma projbittiv | Waterstand met vaarverbod | stan wody uniemożliwiający żeglugę | Nível da água que impossibilita a navegação | nivelul apei restrictiv pentru navigație | vodný stav, pri ktorom je zakázaná plavba | vodostaj, ki ne dovoljuje plovbe | kiellon aiheuttava vedenkorkeus | Förbud p.g.a. vattennivån | уровень воды, запрещающий судоходство | Водостај при коме се обуставља пловидба
I | kíméletes hajózási vízszint | livell tal-ilma li jeħtieġ navigazzjoni b’attenzjoni | Waterstand met beperkte scheepvaart | stan wody wymagający ostrożnej żeglugi | Nível da água que obriga a navegação prudente | nivelul apei de precauție pentru navigație | vodný stav pre opatrnú plavbu | vodostaj, ki zahteva previdno plovbo | varovaista liikkumista edellyttävä vedenkorkeus | Försiktig navigering p.g.a. vattennivån | уровень воды, опасный для судоходства | Водостај који захтева опрезну пловидбу
NN | normál hajózási vízszint | livell normali tal-ilma għan-navigazzjoni | Normaal waterpeil voor scheepvaart | normalny stan wody dla żeglugi | Nível da água normal para a navegação | nivelul apei normal pentru navigație | normálny vodný stav pre plavbu | normalen vodostaj za plovbo | normaali vedenkorkeus alusliikenteelle | Normal vattennivå för sjöfart | Нормальный уровень воды для судоходства | Нормални водостај за пловидбу
LO | alacsony vízállás | livell baxx tal-ilma | Laagwaterregime | niski stan wody | Nível de estiagem | ape mici | nízky vodný stav | nizek vodostaj | Matala vesi | Lågvatten | Низкая вода | Мала вода
CODUL DE RAPORTARE
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
INF | information | Информация | Información | informace | Informationspunkt | Informationspunkt | Teave | Πληροφορίες | Point d'information | Informacijski | informazione | Informācijas punkts | Informavimas
ADD | additional duty to report | Задължтелно допълнително известяване | Obligación adicional de notificación | dodatečná povinnost hlášení | Yderligere rapporteringspligt | zusätzliche Meldepflicht | Täiendav tollimaks teatada | Πρόσθετο καθήκον αναφοράς | Obligation complémentaire d'annonce | Dodatna obveza izvješćivanja | obbligo di ulteriore segnalazione | Papildu ziņošanas pienākums | Privalomas papildomas pranešimas
REG | regular duty to report | Обичаен режим за известяване | Obligación normal de notificación | normální povinnost hlášení | Normal rapporteringspligt | normale Meldepflicht | Tavatollimaks teatada | Κανονικό καθήκον αναφοράς | Obligation d'annonce normale | Redovna obveza izvješćivanja | regime normale di segnalazione | Pastāvīgas ziņošanas pienākums | Įprastas pranešimo režimas
CODUL DE RAPORTARE
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
INF | információ | informazzjoni | Informatie | Punkt informacyjny | Informação | punct de informare | informácie | informacije | Tiedot | Information | Информация для сведения | Информација
ADD | kiegészítő bejelentkezési kötelezettség | dmir addizzjonali ta’ rappurtar | Extra meldplicht | Obowiązek dodatkowego meldowania | Obrigação adicional de comunicação | obligația suplimentară de a raporta | dodatočná povinnosť hlásenia | dodatna obveznost poročanja | Ylimääräinen raportointivelvollisuus | Extra rapporteringsskyldighet | Дополнительное извещение обязательно | Додатна обавеза извештавања
REG | bejelentkezési kötelezettség | dmir regolari ta’ rappurtar | Normale meldplicht | Obowiązek regularnego meldowania | Obrigação normal de comunicação | obligația de a raporta regulat | normálna povinnosť hlásenia | običajna obveznost poročanja | Säännöllinen raportointivelvollisuus | Regelbunden rapporteringskyldighet | Обычный режим извещения | Редовна обавеза извештавања
CODUL SUBIECTULUI
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
OBSTRU | Blockage | Препятствие | Obstrucción | uzávěra | Blokering | Sperre | Blokeerimine | Φραγμένο | Restriction | Prepreka | interruzione | Bloķēts | Blokavimas
PAROBS | Partial obstruction | Частично препятствие | Obstrucción parcial | částečná uzávěra | Delvis blokering | teilweise Sperre | Osaline takistus | Μερική παρεμπόδιση | Restriction partielle | Djelomična prepreka | ostruzione parziale | Daļēji bloķēts | Dalinis blokavimas
DELAY | Delay | Закъснение | Retraso | zpoždění | Forsinkelse | Verzögerung | Hilinemine | Καθυστέρηση | Délai | Kašnjenje | ritardo | Aizkavējums | Delsa
VESLEN | Vessel Length | Дължина на кораба | Eslora | délka plavidla | Fartøjets længde | Schiffslänge | Laeva pikkus | Μήκος σκάφους | Longueur du bateau | Dužina broda | lunghezza del natante | Kuģa garums | Laivo ilgis
VESHEI | Vessel air draught | Височина на кораба | Altura de la obra muerta | výška plavidla nad hladinou | Fartøjets højde over vandlinjen | Schiffshöhe | Laeva kõrgus veepinnast | Μέγιστο ύψος άνωθεν της ισάλου γραμμής | Tirant d'air du bateau | Visina najviše fiksne točke broda iznad vode | altezza del natante dal pelo dell'acqua | Kuģa virsūdens augstums | Laivo aukštis virš vandens
VESBRE | Vessel breadth | Ширина на кораба | Manga | šířka plavidla | Fartøjets bredde | Schiffsbreite | Laeva laius | Μέγιστο πλάτος σκάφους | Largeur du bateau | Širina broda | larghezza del natante | Kuģa platums | Laivo plotis
VESDRA | Vessel draught | Газене на кораба | Calado | ponor plavidla | Fartøjets dybgang | Schiffstiefgang | Laeva süvis | Βύθισμα σκάφους | Tirant d'eau du bateau | Gaz broda | pescaggio del natante | Kuģa iegrime | Laivo grimzlė
AVALEN | Available length | Допустима дължина | Eslora disponible | povolená délka | Disponibel længde | verfügbare Länge | Kasutatav pikkus | Διαθέσιμο μήκος | Longueur maximum | Raspoloživa duljina | lunghezza massima ammessa | Pieļaujamais garums | Leidžiamas ilgis
CLEHEI | Clearance height | Свободна височина | Gálibo vertical | podjezdná výška | Frigang i højden | Durchfahrtshöhe | Kuja kõrgus | Ελεύθερο ύψος διέλευσης | Tirant d'air maximum | Visina plovnog otvora | tirante d'aria | Pieļaujamais augstums | Leidžiamas aukštis
CLEWID | Clearance width | Свободна ширина | Gálibo horizontal | průjezdná šířka | Frigang, bredde | verfügbare Breite | Kuja laius | Ελεύθερο πλάτος διέλευσης | Largeur maximum | Širina plovnog otvora | larghezza massima della via navigabile | Pieļaujamais platums | Leidžiamas plotis
AVADEP | Available depth | Допустимо газене | Profundidad disponible | využitelná hloubka | Vanddybde | verfügbare Tiefe | Kasutatav sügavus | Διαθέσιμο πλάτος | Tirant d'eau maximum | Raspoloživa dubina | pescaggio massimo | Ūdens dziļums | Esamas gylis
NOMOOR | No mooring | Забранено швартоване | Prohibición de amarre | zákaz přistávání | Fortøjning forbudt | Festmacheverbot | Sildumine keelatud | Απαγόρευση αγκυροβολίας | Interdiction d'amarrage | Zabranjen vez | divieto di ormeggio | Pietauvošanās aizliegta | Draudžiama švartuotis
SERVIC | Limited service | Ограничено обслужване | Servicio limitado | provoz omezen | Begrænset betjening | Betrieb eingeschränkt | Piiratud teenindus | Περιορισμένη υπηρεσία | Exploitation limitée | Ograničena usluga | servizio limitato | Ierobežots pakalpojums | Ribotas aptarnavimas
NOSERV | No service | Няма обслужване | Interrupción del servicio | provoz zastaven | Ingen betjening | Betriebssperre | Ei teenindata | Καμία υπηρεσία | Manœuvre interrompue | Nema usluge | nessun servizio | Pakalpojums nav pieejams | Neaptarnaujama
SPEED | Speed | Допустима скорост | Límite de velocidad | nejvyšší rychlost | Hastighedsbegrænsning | Höchstgeschwindigkeit | Kiirus | Ταχύτητα | Limite de Vitesse | Ograničenje brzine | velocità | Ātruma ierobežojums | Ribojamas greitis
WAVWAS | No wash of waves | Забранено създаване на вълни | No crear oleaje | zákaz vytvářet vlnobití a sání | Undgå at lave efterdønninger | Sog und Wellenschlag vermeiden | Ei tekita voolu | Απαγόρευση πρόκλησης κυματισμών | Remous interdits | Zabranjeno pravljenje valova | divieto di moto ondoso | Neradīt viļņus | Nekelti bangų
PASSIN | No passing | Забранено преминаване | Prohibido el paso | zákaz potkávání | Passage er ikke tilladt | Begegnungsverbot | Läbimine keelatud | Απαγόρευση διέλευσης | Trématage interdit | Zabranjen prolaz | divieto di transito | Aizliegts šķērsot | Plaukti draudžiama
ANCHOR | No anchoring | Забранено хвърляне на котва | Prohibido fondear | zákaz kotvení | Opankring ikke tilladt | Ankerverbot | Ankrusse jäämine keelatud | Απαγόρευση αγκυροβολίας | Mouillage interdit | Zabranjeno sidrenje | divieto di ancoraggio | Noenkuroties aizliegts | Draudžiama nuleisti inkarą
OVRTAK | No overtaking | Забранено изпреварване | Prohibido adelantar | zákaz předjíždění | Overhaling ikke tilladt | Überholverbot | Möödasõit keelatud | Απαγόρευση προσπέρασης | Trématage interdit | Zabranjeno pretjecanje | divieto di sorpasso | Apdzīt aizliegts | Draudžiama lenkti
MINPWR | Minimum power | Минимална мощност | Potencia mínima | minimální výkon | Minimum kraft | Mindestantriebsleistung | Minimaalne võimsus | Ελάχιστη ισχύς | Puissance minimum | Minimalna snaga | potenza minima | Minimālā jauda | Mažiausia galia
DREDGE | Dredging | Драгажни работи | Dragado | bagrovací práce | Opmudring | Baggerarbeiten | Süvendus | Βυθοκόρηση | Dragage | Iskapanje | dragaggio | Bagarēšanas darbi | Dugno gilinimas
WORK | Work | Работи (действия) | Obras | práce | Arbejder | Arbeiten | Töötamine | Εργασίες | Travaux | Radovi | lavori | Darbs | Darbai
EVENT | Event | Случай | Suceso | událost | Begivenhed | Veranstaltung | Sündmus | Συμβάν | Evénement | Događaj | manifestazione | Pasākums | Įvykis
CHGMAR | Change marks | Изменение в знаците | Cambio de señalización | změna značení | Ændret signalering | Schifffahrtszeichen geändert | Muudatus-tähis | Αλλαγή σημείων | Signalisation modifée | Promjena navigacijske oznake | segnaletica modificata | Mainītas zīmes | Ženklų keitimas
CHGSER | Change service | Изменение в услугите | Cambio de servicio | změna provozu | Ændret betjening | Betrieb geändert | Vahetus-teenindus | Αλλαγή υπηρεσίας | manœuvre des ouvrages modifiée | Promjena usluge | regime modificato | Pakalpojums mainīts | Aptarnavimo pasikeitimai
SPCMAR | Special marks | Специална сигнализация | Señalización especial | zvláštní signalizace | Særlig signalering | besondere Zeichen | Eritähised | Ειδικά σημεία | Signalisation spéciale | Posebne oznake | segnaletica speciale | Īpašas zīmes | Specialieji ženklai
EXERC | Exercises | Упражнения | Ejercicios | cvičení | Øvelser | Übungen | Õppused | Ασκήσεις | exercices | Vježbe | esercitazioni | Vingrinājumi | Pratybos
LEADEP | Least depth sounded | Минимална дълбочина | Profundidad mínima medida | minimální změřená hloubka | Mindste loddede dybde | minimale Tiefe | Looditud väikseim sügavus | Μικρότερο μετρηθέν βάθος | Profondeur minimale | Minimalna dubina | profondità minima rilevata | Mazākais izmērītais dziļums | Mažiausias gylis
LEVDEC | Decreasing water level | Намаляващо водно ниво | Nivel de agua en descenso | klesající vodní stav | Faldende vandstand | fallender Wasserstand | Veetaseme alanemine | Μειούμενη στάθμη υδάτων | Décrue | Vodostaj u opadanju | livello idrometrico in diminuzione | Krītošs ūdens līmenis | Mažėjantis vandens lygis
LEVRIS | Rising water level | Растящо водно ниво | Nivel de agua en ascenso | stoupající vodní stav | Stigende vandstand | steigender Wasserstand | Veetaseme tõusmine | Αυξανόμενη στάθμη υδάτων | Eaux montantes | Vodostaj u porastu | livello idrometrico in aumento | Kāpjošs ūdens līmenis | Kylantis vandens lygis
ANNOUN | Announcement | Обява | Aviso | zpráva | Meddelelse | Nachricht | Teadaanne | Αγγελία | Annonce | Najava | annuncio | Paziņojums | Pranešimas
LIMITA | Limitations | Ограничение | Limitaciones | omezení | Begrænsninger | Einschränkungen | Piirangud | Περιορισμοί | Limitations | Ograničenja | limitazioni | Ierobežojumi | Apribojimai
CANCEL | Notice withdrawn | Анулирано известие | Anuncio anulado | zpráva byla zrušena | Efterretning trukket tilbage | Nachricht zurückgezogen | Kehtetu märguanne | Απόσυρση αγγελίας | Avis annulé | Povučena obavijest | segnalazione revocata | Paziņojums atcelts | Pranešimas atšauktas
MISECH | False radar echos | Грешно радарно ехо | Ecos radar falsos | falešná ozvěna | Falsk radarekko | Geisterechos | Radari vale kajasignaal | Εσφαλμένα σήματα ραντάρ | Faux échos radar | Pogrešan radarski odziv | rilevazioni radar distorte | Maldigs radara ehosignals | Klaidingi radaro rodmenys
ECDISU | Inland ECDIS update | Обновяване на ECDIS | Actualización ECDIS fluvial | aktualizace informací Inland ECDIS | Inland ECDIS update | Inland ECDIS Update | Uuendatud sisemaine ECDIS | Επικαιροποίηση ECDIS εσωτ. ναυσ. | Mise à jour des données Inland ECDIS | Ažuriranje sustava Inland ECDIS | aggiornamento ECDIS interno | Inland ECDIS informācijas atjaunošana | Inland ECDIS informacijos atnaujinimas
NEWOBJ | New object | Нов обект | Nuevo objeto | nový objekt | Nyt objekt | neues Objekt | Uus ese | Νέο αντικείμενο | Nouvel objet | Novi objekt | nuovo oggetto | Jauns objekts | Naujas objektas
WARNIN | Warning | Внимание | Alarma | varování | Advarsel | Warnung | Hoiatus | Προειδοποίηση | Avertissement | Upozorenje | allerta | Brīdinājums | Įspėjimas
CHWWY | Changes of the fairway | Промени във водния път | Cambio en la vía navegable | změna na vodní cestě | Ændring af farvandet | Änderungen des Fahrwassers | Veetee muutmine | Αλλαγή εντός πλωτής οδού | modification de la passe navigable | Promjene u plovnom putu | modifiche della via navigabile | Izmaiņas kuģu ceļā | Pasikeitimai farvateryje
CONWWY | Constriction of fairway | Строителни работи по водния път | Estrechamiento de vía navegable | zúžení vodní cesty | Indsnævring af vandvejen | Einengung des Fahrwassers | Veetee konstrikt-sioon | Κατασκευή πλωτής οδού | rétrécissement de la passe navigable | Suženje plovnog puta | strettoia | Ūdens ceļa sašaurinājums | Farvaterio susiaurėjimas
DIVER | Diver under the water | Водолазни работи | Presencia de submarinistas | práce pod vodou | Dykkere i vandet | Taucher unter Wasser | Tuuker vee all | Υποβρύχιες εργασίες | plongeurs au travail | Ronilac pod vodom | sommozzatore in immersione | Ūdenslīdēju darbi | Vandenyje naras
SPECTR | Special transport | Специализиран транспорт | Transporte especial | zvláštní přeprava | Særlig transport | Sondertransport | Erivedu | Ειδικές μεταφορές | transport spécial | Specijalni prijevoz | trasporto speciale | Īpašs transports | Specialus transportas
LOCRUL | Local rules of traffic | Местни (локални) правила за движение | Normas locales de tráfico | místní úprava plavebních předpisů | Lokale trafikregler | lokal gültige Verkehrsvorschriften | Kohalikud liiklusees-kirjad | Τοπικοί κανόνες κυκλοφορίας | règlements de navigation locaux | Lokalni prometni propisi | regole di traffico locali | Vietēji satiksmes noteikumi | Vietinės laivų eismo taisyklės
VHFCOV | Radio coverage | Радио покритие (обхват) | Cobertura de radio | rádiové pokrytí | Radiodækning | Funkabdeckung | Raadio leviala | Κάλυψη ασυρμάτου | Couverture radio | Radijska pokrivenost | copertura radio | Radiosignālu pārklājums | Radijo ryšio zona
HIGVOL | High voltage cable | Високо напрежение | Línea de alta tensión | vedení vysokého napětí | Højspændingskabler | Hochspannungsleitung | Kõrgepinge-juhtivus | Αγωγός υψηλής τάσης | Ligne haute tension | Visokonaponski kabel | alta tensione | Augstspriegums | Aukštos įtampos kabelis
TURNIN | No turning | Забранено извършване на поворот | Prohibido girar | zákaz provádět obrat | Vending ikke tilladt | Wendeverbot | Pööramine keelatud | Απαγόρευση στροφής | Interdiction de viver | Zabranjeno okretanje | divieto di manovra | Pagriezties aizliegts | Apsisukti draudžiama
CONBRE | Convoy breadth | Ширина на състава | Manga del convoy | šířka sestavy | Konvojbredde | Verbandsbreite | Konvoi laius | Πλάτος νηοπομπής | largeur du convoi | Širina sastava | larghezza del convoglio | Karavānas platums | Laivų vilkstinės plotis
CONLEN | Convoy lenght | Дължина на състава | Eslora del convoy | délka sestavy | Konvojlængde | Verbandslänge | Konvoi pikkus | Μήκος νηοπομπής | longueur du convoi | Duljina sastava | lunghezza del convoglio | Karavānas garums | Laivų vilkstinės ilgis
REMOBJ | Removal of object | Премахване на препятствие | Retirada de un objeto | odstranění objektu | Fjernelse af objekt | Bergungsarbeiten | Eseme eemaldamine | Απομάκρυνση αντικειμένου | enlèvement d'objet | Uklanjanje objekta | rimozione di oggetti | Objekta noņemšana | Objekto šalinimas
INFSER | Info service | Информационна служба | Servicio de información | Informační servis | Informationstjeneste | Informationsservice | Teabeteenus | Πληροφορίες | Service d'information | Informacijska usluga | servizio informazioni | Informācijas dienests | Informacija
CODUL SUBIECTULUI
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
OBSTRU | zárlat | Ostaklu | Stremming | Zamknięcie | Obstrução | Restricție | blokáda | zapora | Este | Blockering | Закрыто | Препрека
PAROBS | részleges tilalom | Ostaklu parzjali | Gedeeltelijke stremming | Częściowe zamknięcie | Obstrução parcial | Restricție parțială | čiastočné prekážky | delna zapora | Osittainen este | Delvis obstruktion | Частично закрыто | Делимична препрека
DELAY | késedelem | Dewmien | Oponthoud | Opóźnienie | Demora | Întârziere | meškanie | zamuda | Viivästys | Försening | Задержка | Кашњење
VESLEN | hajó hossza | Tul tal-Bastiment | Scheepslengte | Długość statku | Comprimento (embarcação) | Lungimea navei | dĺžka plavidla | dolžina plovila | Aluksen pituus | Fartygslängd | Длина судна | Дужина пловила
VESHEI | hajó magassága | Għoli tal-bastiment | Scheepshoogte | Wysokość statku | Altura acima da linha de água (embarcação) | Înălțimea deasupra liniei de plutire | výška plavidla nad hladinou | prosta višina plovila | Aluksen suurin korkeus vedenpinnasta | Fartygets höjd över vattenytan | Высота судна | Максимална висина пловила над водом
VESBRE | hajó szélessége | Wisa’ tal-bastiment | Scheepsbreedte | Szerokość statku | Boca (embarcação) | Lățimea navei | šírka plavidla | širina plovila | Aluksen leveys | Fartygsbredd | Ширина судна | Ширина пловила
VESDRA | hajó merülése | Fundar meħtieġ għall-bastiment | Diepgang | Zanurzenie statku | Calado (embarcação) | Pescajul navei | ponor plavidla | ugrez plovila | Aluksen syväys | Fartygets djupgående | Осадка судна | Газ пловила
AVALEN | rendelkezésre álló hosszúság | Tul disponibbli | Doorvaartlengte | Długość użytkowa | Comprimento disponível | Lungimea admisă | dostupná dĺžka | razpoložljiva dolžina | Käytettävissä oleva pituus | Tillgänglig längd | Допустимая длина | Расположива дужина
CLEHEI | szabad űrszelvénymagasság | Fond ta’ spazju ħieles | Doorvaarthoogte | Wysokość w świetle | Altura livre | Gabaritul de înălțime | podjazdná výška | prosta višina prehoda | Alikulkukorkeus | Frihöjd | Допустимая высота | Слободна висина
CLEWID | hasznos szélesség | Wisa’ ta’ spazju ħieles | Doorvaartbreedte | Szerokość w świetle | Largura livre | Gabaritul de lățime | prejazdná šírka | prosta širina prehoda | Käytettävissä oleva leveys | Farledsbredd | Допустимая ширина | Слободна ширина
AVADEP | rendelkezésre álló vízmélység | Fond disponibbli | Beschikbare diepte | Głębokość użytkowa | Profundidade disponível | Adâncimea disponibilă | dostupná hĺbka | razpoložljiva globina | Käytettävissä oleva syväys | Tillgängligt djup | Существующая глубина | Расположива дубина
NOMOOR | veszteglési tilalom | Irmiġġ projbit | Afmeerverbod | Zakaz cumowania | Proibição de amarrar | Interdicția de a acosta | zákaz vyväzovania | prepovedan privez | Kiinnittyminen kielletty | Förtöjning förbjuden | Швартовка запрещена | Забрањено везивање
SERVIC | korlátozott üzem | Servizz limitat | Beperkte service | Usługa ograniczona | Serviço limitado | Manevră restricționată | obmedzená prevádzka | omejena storitev | Rajoitettu palvelu | Begränsad service | Ограниченое обслуживание | Ограничена услуга
NOSERV | üzemszünet | Servizz sospiż | Geen bediening | Usługa niedostępna | Interrupção do serviço | Întreruperea serviciului | zastavená prevádzka | ni storitve | Ei palvelua | Ingen service | Не обслуживаемое | Без услуге
SPEED | sebességkorlátozás | Veloċità | Snelheidsbeperking | Ograniczenie szybkości | Limite de velocidade | Limită de viteză | najvyššia povolená rýchlosť | hitrost | Nopeus | Hastighet | Ограничение скорости | Брзина
WAVWAS | hullámkeltést elkerülni | Tranja tal-mewġ projbita | Golfslag vermijden | Zakaz tworzenia fal | Não causar ondulação | Formarea valurilor interzisă | zákaz vlnobitia a sania | prepovedano povzročanje valov | Voimakkaan aallokon tuottaminen kielletty | Undvik svall | Берегись волны | Забрањено прављење таласа
PASSIN | találkozás tilos | Passaġġ projbit | Ontmoeten verboden | Zakaz wymijania | Proibição de passar | Traversarea interzisă | zákaz preplávania | prepovedan prehod | Ei läpikulkua | Passering förbjuden | Нет прохода | Забрањен пролаз
ANCHOR | horgonyozni tilos | Ankraġġ projbit | Ankeren verboden | Zakaz kotwiczenia | Proibição de ancorar | Ancorarea interzisă | zákaz kotvenia | prepovedano sidranje | Ei ankkuroitumista | Ankring förbjuden | Якорная стоянка запрещена | Забрањено сидрење
OVRTAK | előzni tilos | Projbit il-qbiż ta’ bastimenti oħra | Voorbijlopen verboden | Zakaz wyprzedzania | Proibição de cruzar ou ultrapassar | Depășirea interzisă | zákaz predchádzania | prepovedano prehitevanje | Ei ohittamista | Omkörning förbjuden | Обгон запрещен | Забрањено престизање
MINPWR | minimális teljesítmény | Potenza minima | Minimaal vermogen | Minimalna moc napędu | Potência mínima | Putere minimă | minimálny výkon | najmanjša moč | Vähimmäisteho | Minsta motoreffekt | минимальная мощность | Минимална снага
DREDGE | kotrási munkálatok | Tħammil | Baggerwerkzaamheden | Pogłębianie | Dragagens | Lucrări de dragaj | bagrovacie práce | poglabljanje dna | Ruoppaustyöt | Muddring | Встречное движение | Багеровање
WORK | munkálatok | Xogħol | Werkzaamheden | Prace | Trabalhos | Lucrări | práce | delo | Työt | Arbeten | Проводятся работы | Радови
EVENT | rendezvény | Avveniment | Evenement | Impreza | Evento | Eveniment | udalosť | prireditev | Tapahtumat | Evenemang | Мероприятие | Догађај
CHGMAR | forgalmi jelek változtatása | Bidla fis-sinjali | Gewijzigde markering | Zmiana oznakowania | Alteração da sinalização | Semnalizare modificată | zmena značenia | sprememba oznak | Merkit muuttuneet | Ändrad märkning | Изменение СНО | Промена знака
CHGSER | üzemidõ változtatása | Servizz modifikat | Gewijzigde bediening | Zmiana obsługi | Alteração do serviço | Manevre modificate | zmena prevádzky | sprememba storitve | Palvelu muuttunut | Förändrad drift | Изменение часов работы | Промена услуге
SPCMAR | speciális jelek | Sinjali speċjali | Bijzondere markeringen | Znaki specjalne | Sinalização especial | Semnalizare specială | špeciálne značenie | posebne oznake | Erikoismerkit | Särskilda markeringar | Специальные знаки | Посебне ознаке
EXERC | gyakorlatok | Eżerċizzji | Oefeningen | Ćwiczenia | Exercícios | Exerciții | cvičenia | vaje | Harjoitukset | Övningar | Испытания | Вежбе
LEADEP | minimális mélység | L-inqas fond imkejjel | Minst gepeilde diepte | Najmniejsza zmierzona głębokość | Profundidade mínima medida | Adâncimea minimă | najnižšia nameraná hĺbka | najmanjša izmerjena globina | Matalin luodattu syvyys | Minsta lodade djup | Минимальная глубина | Најмања измерена дубина
LEVDEC | csökkenő vízállás | Livell tal-ilma li qed jitbaxxa | Afnemend water | Spadek stanu wody | Descida do nível da água | Scăderea nivelului apei | klesajúca vodná hladina | nižanje vodostaja | Vedenkorkeus laskee | Sjunkande vattennivå | Снижение уровня воды | Водостај у опадању
LEVRIS | emelkedő vízállás | Livell tal-ilma li qed jogħla | Wassend water | Wzrost stanu wody | Subida do nível da água | Creșterea nivelului apei | stúpajúca vodná hladina | višanje vodostaja | Vedenkorkeus nousee | Stigande vattennivå | Повышение уровня воды | Водостај у порасту
ANNOUN | hirdetmény | Avviż | Aankondiging | Komunikat | Comunicado | Anunț | oznámenie | obvestilo | Ilmoitus | Meddelande | Объявление | Најава
LIMITA | korlátozás | Restrizzjonijiet | Beperkingen | Ograniczenia | Restrições | Limitări | obmedzenia | omejitve | Rajoitukset | begränsningar | Ограничение | Ограничење
CANCEL | hirdetmény visszavonva | Avviż annullat | Bericht ingetrokken | Komunikat odwołany | Aviso anulado | Mesaj anulat | správa bola zrušená | obvestilo preklicano | Ilmoitus peruutettu | Återkallad märkning | Отмена извещения | Повлачење издатог Саопштења
MISECH | hamis radarvisszhangok | Eki foloz tar-radar | Valse radarecho's | Fałszywe echa radarowe | Ecos radar falsos | Ecou radar fals | falošná odozva | napačni odmevi radarja | Virheellisiä tutkakaikuja | Falska radarekon | Ложная радарная цель | Лажни радарски одраз
ECDISU | Inland ECDIS frissítés | aġġornament tal-ECDIS Interna | Inland ECDIS-update | Aktualizacja Inland ECDIS | Atualização ECDIS-fluvial | actualizarea datelor ECDIS | aktualizácia Inland ECDIS | posodobitev celinskega ECDIS | Sisävesiliikenteen ECDIS:n päivitys | Uppdatering av inlands-ECDIS | Обновление информации для Inland ECDIS | Ажуриран Inland ECDIS
NEWOBJ | Új objektum | Oġġett ġdid | Nieuw object | Nowy obiekt | Novo objeto | Obiect nou | nový objekt | nov objekt | Uusi kohde | Nytt föremål | Новый объект | Нови објекат
WARNIN | figyelmeztetés | Twissija | Waarschuwing | Ostrzeżenie | Alerta | Avertisment | varovanie | opozorilo | Varoitus | Varning | Предупреждение | Упозорење
CHWWY | hajóútváltozás | Bidliet tal-kanal navigabbli | Verandering van de vaarweg | Zmiany toru wodnego | Alterações na via navegável | Modificări ale șenalului navigabil | zmeny na vodnej ceste | spremembe na plovni poti | vesiväylän muutos | Ändring av farleden | Изменение фарватера | Промене у пловном путу
CONWWY | hajóútszűkület | Restrizzjoni tal-kanal navigabbli | Beperking van de vaarweg | Zwężenie toru wodnego | Estreitamento da via navegável | Îngustarea șenalului navigabil | zúženie vodnej cesty | zoženje plovne poti | vesiväylän kaventuminen | Smalare farled | Сужение фарватера | Сужење пловног пута
DIVER | vízalatti munkák | Bugħaddas taħt l-ilma | Duikwerkzaamheden | Nurek pod wodą | Presença de mergulhadores | Scafandru în apă | práce pod vodou | dela pod vodo | sukeltaja veden alla | Dykare i vattnet | водолаз под водой | Ронилац под водом
SPECTR | különleges szállítás | Trasport speċjali | Bijzonder vervoer | Transport specjalny | Transporte especial | Transport special | špeciálna preprava | posebni prevoz | erikoiskuljetus | Specialtransport | Специальный транспорт | Специјални транспорт
LOCRUL | helyi közlekedési rend (R) | Regoli lokali tat-traffiku | Lokale verkeersregels | Miejscowe przepisy ruchu statków | Regras de tráfego locais | Regulamente locale de trafic | lokálne pravidlá plavby | lokalna prometna pravila | paikalliset liikennöintisäännöt | Lokala trafikregler | Местные правила судоходства | Локална правила пловидбе
VHFCOV | rádiós lefedettség | Kopertura tar-radju | Radiodekking | Pokrycie radiowe | Cobertura rádio | Acoperire radio | rádiové pokrytie | pokritost radijskih zvez | Radion kuuluvuusalue | Radiotäckning | Покрытие радиосигналом | Покривеност радио сигналом
HIGVOL | nagy feszültségű átfeszítés | Kejbil b’voltaġġ għoli | Hoogspanningskabel | Linia wysokiego napięcia | Linha de alta tensão | Linie de înaltă tensiune | vedenie vysokého napätia | visokonapetostni kabel | Korkeajännitejohto | Högspänningsledning | высоковольтный кабель | Кабл под високим напоном
TURNIN | megfordulni tilos | Dawran projbit | Draaien verboden | Zakaz zawracania | Proibição de inverter marcha | Întoarcerea interzisă | Zákaz vykonávania obratov | prepovedano obračanje | Kääntyminen kielletty | Vändning förbjuden | Поворот запрещен | Забрањено окретање
CONBRE | a kötelék szélessége | Wisa’ tal-konvoj | Breedte van de duwsleep | Szerokość zestawu | Largura do comboio | Lățimea convoiului | šírka zostavy | širina konvoja | kytkyeen leveys | Konvojbredd | Ширина состава судов | Ширина састава
CONLEN | a kötelék hossza | Tul tal-konvoj | Lengte van de duwsleep | Długość zestawu | Comprimento do comboio | Lungimea convoiului | dĺžka zostavy | dolžina konvoja | kytkyeen pituus | Konvojlängd | Длина состава судов | Дужина састава
REMOBJ | mentési munkálatok | Tneħħija ta’ oġġett | Verwijderen van object | Usuwanie objektu | Remoção de objeto | Schimbarea obiectului | odstránenie objektu | odstranitev objekta | Kohteen poistaminen | Bärgning av föremål | Удаление объекта | Уклањање објекта
INFSER | Tájékoztatás | Servizz ta’ informazzjoni | Informatieservice | Serwis informacyjny | Serviço de informações | Mesaj informativ | Informačná služba | informacijska služba | Tietopalvelu | Informationstjänst | Информационная служба | Инфо-сервис
CODUL GRUPULUI-ȚINTĂ
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
ALL | all | Всички | Todos | všichni | Alle | alle | Kõik | Όλα | Tous les usagers | Sve vrste plovila | tutti | Visi | Visi
CDG | vessels with dangerous goods | Търговски кораб превозващ опасни товари | Embarcaciones con mercancías peligrosas | plavidla určená pro přepravu nebezpečného nákladu | Fartøjer med farligt gods | Fahrzeuge mit gefährlichen Gütern | Ohtliku lastiga kaubalaev | Εμπορικά σκάφη με επικίνδυνο φορτίο | Transports de matières dangereuses | Komercijalno plovilo s opasnim teretom | navi mercantili con carichi pericolosi | Komerckuģi ar bīstamu kravu | Prekybos laivai su pavojingu kroviniu
COM | commercial vessels | Търговски кораб | Embarcaciones comerciales | plavidla pro přepravu nákladu | Handelsskibe | kommerzielle Fahrzeuge | Kauba-laevad | Εμπορικά σκάφη | Bateau de commerce | Komercijalno plovilo | navi mercantili | Komerckuģi | Prekybos laivai
PAX | passenger vessels | Пътнически кораб | Embarcaciones de pasajeros | plavidla pro přepravu cestujících | Passagerskibe | Fahrgastschiffe | Reisilaevad | Επιβατηγά σκάφη | Bateau à passagers | Putničko plovilo | navi passeggeri | Pasažieru kuģi | Keleiviniai laivai
PLE | pleasure crafts | Спортен или увеселителен кораб | Embarcaciones de recreo | sportovní plavidla | Fritidsfartøjer | Sportboote | Lõbusõidu-laev | Σκάφη αναψυχής | Bateau de plaisance | Plovilo za razonodu | natanti da diporto | Izpriecceļojumu kuģi | Pramoginiai laivai
CNV | convoys | Състав | Convoyes | sestavy | Konvojer | Verbände | Koosseis | Νηοπομπές | Convoi | Sastav | convogli | Karavānas | Vilkstinės
PUS | pushed convoys | Тласкан състав | Convoyes empujados | tlačné sestavy | Skubbekonvojer | Schubverbände | Tõugatav koosseis | Ωθούμενες νηοπομπές | convois poussés | Potiskivani sastav | convogli spinti | Karavānas ar stūmēju | Stumiamos vilkstinės
NNU | non navigating users | Потребители извън корабоплаването | Usuarios no navegantes | jiní než nautiční uživatelé | Brugere uden for skibsfart | andere als nautische Nutzer | muud kasutajad, v.a alused | Χρήση εκτός ναυσιπλοΐας | usagers non navigants | Korisnici koji ne plove | utilizzatori non in navigazione | Ar kuģošanu nesaistīti izmantotāji | Ne laivybos tikslais
LOA | loaded vessels | Натоварен кораб | Embarcaciones con carga | naložená plavidla | Lastede fartøjer | beladene Fahrzeuge | Laadungis laevad | Φορτωμένα σκάφη | bateaux chargés | Natovareno plovilo | navi cariche | Piekrauti kuģi | Laivai su kroviniu
SMA | small crafts | Малък кораб | Embarcaciones pequeñas | malá plavidla | Små fartøjer | Kleinfahrzeuge | Väikelaevad | Μικρά σκάφη | petites embarcations | Malo plovilo | piccoli natanti | Mazas tonnāžas peldlīdzekļi | Maži laivai
CND | convoys with dangerous goods | Състав превозващ опасен товар | Convoyes con mercancías peligrosas | sestava pro přepravu nebezpečného nákladu | Konvojer med farligt gods | Verbände mit gefährlichen Gütern | Ohtliku lastiga konvoid | Νηοπομπές με επικίνδυνα εμπορεύματα | convois de matières dangereuses | Sastav sa opasnim teretom | convogli con carichi pericolosi | Karavānas ar bīstamu kravu | Vilkstinės su pavojingu kroviniu
MOV | motorized vessels | Моторен кораб | Embarcaciones motorizadas | plavidla s vlastním strojním pohonem | Motordrevne fartøjer | Fahrzeuge mit Maschinenantrieb | Mootorlaevad | Μηχανοκίνητα σκάφη | bateaux motorisés | Plovilo s motorom | navi a motore | Motorizēti kuģi | Motoriniai laivai
NMV | non-motorized vessels | Немоторен кораб | Embarcaciones no motorizadas | plavidla bez vlastního strojního pohonu | Ikkemotordrevne fartøjer | Fahrzeuge ohne Maschinenantrieb | Mootorita laevad | Μη μηχανοκίνητα σκάφη | bateaux non motorisés | Plovilo bez motora | navi non a motore | Nemotorizēti kuģi | Nemotoriniai laivai
WOC | worksite crafts | Работни плаващи средства | Embarcaciones de obras | plavidla vykonávající práce na vodní cestě | Flydende arbejdsplatforme | Baufahrzeuge | Töölaevad | Σκάφη εργοταξίου | bateaux de service | Radno plovilo | navi cantiere | Darblaukuma peldlīdzekļi | Statybvietės plaukiojančios priemonės
CODUL GRUPULUI-ȚINTĂ
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
ALL | mindenkire vonatkozó | kollha | Alle scheepvaart | Wszystkie jednostki | Todos os utentes | toți utilizatorii | všetci (používatelia) | vse | Kaikki | Alla | Все суда | Сви
CDG | kereskedelmi hajó veszélyes áruval | bastimenti b’merkanzija perikoluża | Beroepsvaart gevaarlijke stoffen | Statki handlowe przewożące ładunki niebezpieczne | Embarcações de comércio com mercadorias perigosas | transport de materiale periculoase | plavidlá s nebezpečným tovarom | trgovska plovila z nevarnim blagom | Kauppa-alukset, joissa on vaarallisia aineita | Handelsfartyg med farlig last | Торговое судно с опасным грузом | Комерцијална пловила са опасним теретом
COM | kereskedelmi hajó | bastimenti kummerċjali | Beroepsvaart | Statki handlowe | Embarcações de comércio | navă comercială | obchodné lode | trgovska plovila | Kauppa-alukset | Handelsfartyg | Торговое судно | Комерцијално пловило
PAX | személyszállító hajó | bastimenti tal-passiġġieri | Passagiersschepen | Statki pasażerskie | Embarcações de passageiros | navă de pasageri | osobné lode | potniška plovila | Matkustaja-alukset | Passagerarfartyg | Пассажирское судно | Путничко пловило
PLE | kedvtelési célú hajó | opri tal-baħar għar-rikreazzjoni | Recreatievaart | Statki rekreacyjne | Embarcações de recreio | navă de agrement | rekreačné a športové plavidlá | plovila, namenjena za šport in rekreacijo | Huvialukset | Fritidsbåtar | Прогулочное судно | Спортско-рекреативно пловило
CNV | hajókötelék | konvojs | Samenstel | Zestawy | Comboios | convoi | zostavy | konvoji | Kytkyeet | Konvojer | Состав | Састави
PUS | tolt kötelékek | konvojs imbuttati | Duweenheid | Zestawy pchane | Comboios empurrados | convoi împins | tlačné zostavy | potisni konvoji | Työnnetyt kytkyeet | Påskjuten konvoj | Толкаемый состав | Потискивани састави
NNU | nem hajózási használók | utenti li ma jinnavigawx | Niet nautische gebruikers | Użytkownicy nieżeglujący | Utentes não navegantes | personal nenavigant | neplávajúci užívatelia | uporabniki, ki ne plujejo | muut käyttäjät kuin vesilläliikkujat | Andra än sjöfarande | для несудоходных целей | Корисници који не плове
LOA | berakott hajó | bastimenti mgħobbija | Beladen schepen | Statki załadowane | Embarcações carregadas | nava încărcată | naložené plavidlá | natovorjena plovila | Lastatut alukset | Lastade fartyg | Груженое судно | Натоварено пловило
SMA | kishajó | opri tal-baħar żgħar | Kleine vaartuigen | Mały statek | Pequenas embarcações | șalupă mică | malé plavidlá | mali plovni objekti | Pienet alukset | Småbåtar | Малое судно | Мало пловило
CND | veszélyes árut szállító kötelék | konvojs b’merkanzija perikoluża | Samenstel met gevaarlijke stoffen | Zestaw z ładunkiem niebezpiecznym | Comboios com mercadorias perigosas | convoi cu mărfuri periculoase | zostavy s nebezpečným tovarom | konvoji z nevarnim blagom | Kytkyeet, joissa vaarallisia aineita | Konvojer med farligt gods | Состав с опасными грузами | Састави са опасним теретом
MOV | motoros hajó | bastimenti b’mutur | Vaartuigen met motor | Statek o napędzie mechanicznym | Embarcações motorizadas | nave propulsate | plavidlá s vlastným strojným pohonom | motorizirana plovila | Moottoroidut alukset | Motordrivna fartyg | Моторные суда | Mоторизовано пловило
NMV | motor nélküli hajó | bastimenti li ma għandhomx mutur | Vaartuigen zonder motor | Statek bez napędu mechanicznego | Embarcações não-motorizadas | nave nepropulsate | plavidlá bez vlastného strojného pohonu | plovila brez motorja | Muut kuin moottoroidut alukset | Icke motordrivna fartyg | Безмоторные суда | Немоторизовано пловило
WOC | úszómunkagép | opri tal-baħar ta’ sit tax-xogħol | Schepen voor bouwwerkzaamheden | Statek roboczy | Embarcações de estaleiro | șalupa tehnică | plavidlá vykonávajúce práce na vodnej ceste | plovni objekti na delovni lokaciji | Työmaa-alukset | Arbetsfartyg | Технический флот | Пловни објекат на градилишту
CODUL TIPULUI
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
RIV | river | Река | Río | řeka | Flod | Fluss | Jõgi | Ποταμός | Rivière | Rijeka | fiume | Upe | Upė
CAN | canal | Канал | Canal | kanál | Kanal | Kanal | Kanal | Κανάλι | Canal | Kanal | canale | Kanāls | Kanalas
LAK | lake | Езеро | Lago | jezero | Sø | See | Järv | Λίμνη | Bassin | Jezero | lago | Ezers | Ežeras
FWY | fairway | Фарватер | Vía navegable | plavební dráha | Farvand | Fahrwasser | Faarvaater | Δίαυλος | Chenal | Plovni put | canale navigabile | Kuģu ceļš | Farvateris
LCK | lock | Бараж | Esclusa | plavební stupeň | Sluse | Schleuse | Lüüs | Υδατοφράκτης | Ecluse | Prevodnica | conca | Slūžas | Šliuzas
BRI | bridge | Мост | Puente | most | Bro | Brücke | Sild | Γέφυρα | Pont | Most | ponte | Tilts | Tiltas
RMP | ramp | Рампа | Rampa | rampa | Rampe | Rampe | Ramp | Πλατοφόρμα | Plan incliné | Rampa | rampa | Traps | Rampa
BAR | weir | Бент | Presa | jez | Overløbsdæmning | Wehr | Ülevoolupais | Φράγμα ποταμού | Barrage | Pregrada | sbarramento | Aizsprosts | Užtvanka
BNK | bank | Бряг | Margen | břeh | Bred | Ufer | Kallas | Όχθη | Berge | Obala | sponda | Krasts | Krantas
GAU | tide gauge | Водомерна станция | Mareógrafo | vodočet | Tidevandsmåler | Pegel | Tõusu ja mõõna mõõtur | Παλιρροιογράφος | Échelle/Marégraphe | Vodomjerna postaja | mareometro | Paisuma/ bēguma līmeņrādis | Mareografas
BUO | buoy | Буй | Boyas | bóje | Bøje | Boje | Poi | Σημαντήρας | Bouée | Plutača | boa | Boja | Plūduras
BEA | beacon | Фар | Balizas | maják | Fast sømærke | Bake | Paak | Υφαλοδείκτης | Balise | Svjetleći obalni znak | gavitello | Bāka | Švyturys
ANC | anchoring area | Котвена стоянка | Fondeadero | kotviště | Opankringsområde | Ankerplatz | Ankruplats | Περιοχή αγκυροβολίας | zone de stationnement | Sidrište | area di ancoraggio | Enkurvieta | Inkaravimosi vieta
BER | berth | Корабно място (кей) | Atracadero | vývaziště | Kajplads | Liegestelle | Kai | Αποβάθρα | point de stationnement | Pristanište | attracco | Pietauvošanas vieta | Prieplauka
MOO | mooring facility | Швартово устройство | Amarradero | vyvazovací zařízení | Fortøjningsanlæg | Festmacheeinrichtung | Sildumis-rajatis | Εγκατάσταση πρόσδεσης | Aménagement d'amarrage | Oprema za vezivanje | struttura di ormeggio | Pietauvošanas ierīce | Švartavimosi įrenginys
TER | terminal | Терминал | Terminal | překladiště | Terminal | Umschlagplatz | Terminal | Τερματικός σταθμός | Terminal | Terminal | terminal | Termināls | Terminalas
HAR | harbour | Пристанище | Puerto | přístav | Havn | Hafen | Sadam | Λιμάνι | Port | Luka | porto | Osta | Uostas
FDO | floating dock | Плаващ док | Muelle flotante | plovoucí dok | Flydedok | Schwimmdock | Ujuvdokk | Πλωτή αποβάθρα | Pontons | Plutajući dok | bacino galleggiante | Peldošais doks | Plūdrusis dokas
CAB | cable overhead | Далекопровод | Cable aéreo | vzdušné vedení kabelu | Luftledning | Überspannung | Elektriliin | Εναέριο καλώδιο | Câble suspendu (Chemin de câbles, lignes électriques) | Viseći dalekovod | cavo sospeso | Kabeļu pārvads | Oro linijos kabelis
FER | ferry | Ферибот | Transbordador | přívoz | Kabelfærge | Fähre | Parvlaev | Οχηματαγωγό | Bac | Skela | funivia | Prāmis | Keltas
PIP | pipeline | Тръбопровод | Conductos | potrubí | Rørledning | Pipeline | Torujuhe | Αγωγός | Oléoduc | Cjevovod | conduttura | Cauruļvads | Vamzdynas
PPO | pipeline overhead | Надземен тръбопровод | Conductos aéreos | nadzemní vedení potrubí | Rørbro | Rohrbrücke | Torustiku liin | Εναέριος αγωγός | Oléoduc aérien | Viseći cjevovod | conduttura sospesa | Cauruļvadu pārvads | Virš vandens iškeltas vamzdynas
HFA | harbour facility | Пристанищно оборудване | Instalación portuaria | přístavní zařízení | Havneanlæg | Hafeneinrichtung | Sadama rajatis | Λιμενική εγκατάσταση | Installation portuaire | Lučke građevine | installazione portuale | Ostas iekārta | Uosto įranga
HMO | harbour master's office | Капитан на пристанището | Capitanía de puerto | kancelář vedoucího přístavu | Havnekontor | Hafenmeisterbüro | Sadamakap-teni büroo | Λιμεναρχείο | Capitainerie | Kapetanija | capitaneria di porto | Ostas kapteiņa dienests | Uosto kapitono biuras
SHY | shipyard | Корабостроителница | Astillero | loděnice | Skibsværft | Werft | Laevatehas | Ναυπηγείο | Chantier naval | Brodogradilište | cantiere navale | Kuģu būvētava | Laivų statykla
REF | refuse dump | Пункт за събиране на отпадъци | Depósito de residuos | sběrna odpadu | Affaldsdeponi | Abfallsammelstelle | Prahikallur | Χώρος απόρριψης αποβλήτων | Station de collecte de déchets | Skladište otpadnog materijala | punto raccolta rifiuti | Atkritumu izgāztuve | Atliekų surinkimo aikštelė
MAR | notice mark | Информационно табло | Panel de señalización | plavební znak | Advarselsmærke | Schifffahrtszeichen | Teatise tähis | Προειδοποιητικό σημείο | Panneau de signalisation | Plovidbena oznaka | segnalazione | Informatīva zīme | Įspėjimo ženklas
LIG | light | Светещ знак | Alumbrado | světlo | Lys | Leuchtfeuer | Tuli | Φανός | Feux | Svjetlo | fanale | Gaisma | Šviesos
SIG | signal station | Сигнална станция | Estación de señalización | signální stanice | Signalstation | Signalstation | Märguande-punkt | Σηματοφορικός σταθμός | Station de signalisation | Signalna postaja | stazione di segnalamento | Signālstacija | Signalų postas
TUR | turning basin | Район за поворот | Cuenca de maniobra | obratiště | Vendebassin | Wendestelle | Pöörde eeldokk | Λεκάνη στροφής | Bassin de virage | Mjesto za okretanje | bacino di manovra | Pagriešanās vieta | Apsisukimo baseinas
CBR | canal bridge | Мост на канал | Puente canal | přemostění kanálu | Kanalbro | Kanalbrücke | Kanalisild | Γέφυρα καναλιού | Pont Canal | Most na kanalu | acquedotto | Kanāla tilts | Kanalo tiltas
TUN | tunnel | Тунел | Túnel | tunel | Tunnel | Tunnel | Tunnel | Σήραγγα | Tunnel | Tunel | tunnel | Tunelis | Tunelis
BCO | border control | Граничен контрол | Puesto fronterizo | hraniční kontrola | Grænsekontrol | Grenzstation | Piirikontroll | Συνοριακός έλεγχος | Poste de douane | Granična kontrola | controllo di frontiera | Robežkontrole | Pasienio kontrolė
REP | reporting point | Контролен пост | Puesto de notificación | místo hlášení | Rapporteringspunkt | Meldepunkt | Aruandlus-punkt | Σημείο αναφοράς | Poste de contrôle | Kontrolna točka | punto di controllo | Ziņošanas vieta | Kontrolės punktas
FLO | flood gate | Шлюз | Compuertas | ochranná vrata | Overløbslukke | Sperrtor | Tõusuvee-tõke | Θύρα υδροφράχτη | Porte de garde | Vrata prevodnice | paratoia | Slūžas | Dambos uždoris
SLI | ship lift | Корабен елеватор/подемник | Elevador de barcos | lodní výtah | Skibskran | Schiffshebewerk | Laevalift | Ανυψωτήρας πλοίων | ascenseur à bateaux | Dizalo za brod | ascensore per navi | Kuģu lifts | Laivų keltuvas
DUK | culvert | Водосток | Paso | propustek | Gennemløbsrør | Düker | Toruviik | Υδαταγωγός | caniveau | Odvodni kanal | tomba a sifone | Ūdensvadne | Pralaida
VTC | vessel traffic centre | Център за управление на корабоплаването | Centro de tráfico naval | centrum řízení plavby | Skibstrafikcenter | Verkehrszentrale | Laevaliikluskeskus | Κέντρο ρύθμισης της κυκλοφορίας των πλοίων | centre de gestion de trafic | Kontrolni centar | Centro di controllo del traffico navale | Kuģu satiksmes centrs | Laivų eismo centras
RES | reservoir | Резервоар | Embalse | nádrž | Reservoir | Stauhaltung | Hoidla | Δεξαμενή | bassin réservoir | Akumulacija | bacino | Rezervuārs | Tvenkinys
LKB | lock basin | Шлюзова камера | Esclusa con cabezas separadas | plavební komora | Kedelsluse | Schleusenkammer | Lüüsitiik | Θάλαμος δεξαμενής ανύψωσης | sas d’écluse | Bazen prevodnice | conca di navigazione | Slūžu baseins | Šliuzo baseinas
BRO | bridge opening | Плавателен отвор на мост | Apertura de puente | mostní pole | Oplukkelig bro | Brückendurchfahrtsöffnung | Sild avatud | Άνοιγμα γέφυρας | passe de pont | Otvor mosta | apertura del ponte | Tilta atvērums | Tilto anga
BNS | bunker/fuelling station | Място за бункероване | Tanque/Estación de suministro de combustible | tankovací stanice | bunker/tankstation | Bunkerstation | Punkerdus-/tankimisjaam | Αποθήκη καυσίμων/σταθμός τροφοδοσίας καυσίμων | poste de ravitaillement | Terminal za opskrbu gorivom | stazione di bunkeraggio / rifornimento | Tvertne/uzpildes stacija | Bunkeris / kuro pildymo punktas
CODUL TIPULUI
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
RIV | folyó | xmara | Rivier | Rzeka | Rio | fluviu | rieka | reka | Joki | Flod | Река | Река
CAN | csatorna | kanal | Kanaal | Kanał | Canal | canal | kanál | kanal | Kanava | Kanal | Канал | Канал
LAK | tó | lag | Meer | Jezioro | Lago | lac | jazero | jezero | Järvi | Sjö | Озеро | Језеро
FWY | hajóút | kanal navigabbli | Vaarweg | Tor wodny | Via navegável | șenal | plavebná dráha | plovna pot | Väylä | Farled | Фарватер | Пловни пут
LCK | zsilip | bieb tal-ilma magħluq | Sluis | Śluza | Eclusa | ecluză | plavebný stupeň | zapornica | Sulku | Sluss | Шлюз | Преводница
BRI | híd | pont | Brug | Most | Ponte | pod | most | most | Silta | Bro | Мост | Мост
RMP | rámpa | rampa | Helling | Pochylnia | Rampa | rampă | rampa | rampa | Ramppi | Ramp | Рампа | Рампа
BAR | gát | diga sommerġibbli | Stuw | Jaz | Barragem | baraj | hať | jez | Pato | Damm | Плотина | Устава
BNK | part | xatt | Oever | Brzeg | Margem | banc | breh | breg | Ranta | Bank | берег водоема | Обала (реке, канала, језера)
GAU | vízmérce | kejl il-marea | Peilschaal | Wodowskaz | Fluviómetro/marégrafo | miră de maree | vodomerná stanica | vodomerna postaja | Vuorovesimittari | Tidvattenmätare | водомерная станция, водомер | Водомерна станица
BUO | bója | baga | Boei | Boja | Boia | geamandură | bója | plovec | Poiju | Boj | Буй | Бова
BEA | parti (irány)jel | fanal | Baken | Stawa | Baliza | baliză | maják | svetilnik | Merimerkki | Signalboj | Маяк | Светлећи обалски знак
ANC | horgonyzó-hely | żona ta’ ankraġġ | Ankerplaats | Kotwicowisko | Ancoradouro | sector de ancorare | kotvisko | sidrišče | Ankkurointialue | Ankringsområde | Якорная стоянка | Сидриште
BER | kikötőhely | irmiġġ | Ligplaats | Miejsce postoju | Cais/fundeadouro | punct de ancorare | výväzisko | privez | Laituripaikka | Kaj | Причал | Пристајалиште
MOO | kikötőberendezés | faċilità ta’ rmiġġ | Afmeerfaciliteit | Cumowisko | Posto de amarração | posibilitate de acostare | vyväzovacie zariadenie | naprava za privez | Kiinnittymislaitteisto | Förtöjningsanläggning | Швартовое устройство | Опрема за извезивање
TER | rakodó | terminal | Terminal | Terminal | Terminal | terminal | terminál | terminal | Terminaali | Terminal | Терминал | Терминал
HAR | kikötő | port | Haven | Port | Porto | port | prístav | pristanišče | Satama | Hamn | Порт | Лука
FDO | úszódokk | baċir f’wiċċ l-ilma | Drijvend dok | Dok pływający | Doca flutuante | ponton | plávajúci dok | plavajoči dok | Uiva telakka | Flytdocka | плавучий док | Пловећи док
CAB | átfeszítés | kejbil fl-ajru | Overhangende kabel | Kabel napowietrzny | Cabo aéreo | cablu suspendat | vzdušné vedenie kábla | zračni daljnovod | Kaapeli yläpuolella | Luftledning | Подвесной кабель | Далековод
FER | komp | lanċa | Veerpont | Prom | Ferry | bac | prievozná loď (kompa) | trajekt | Lautta | Färja | Паром | Скела
PIP | csővezeték | pipeline | Pijpleiding | Rurociąg | Conduta | conducte | potrubie | cevovod | Putkijohto | Pipeline | Трубопровод | Цевовод
PPO | csőhíd | pipeline fl-ajru | Overhangende pijpleiding | Rurociąg napowietrzny | Conduta aérea | conducte suspendate | vzdušné vedenie potrubia | zračni cevovod | Putkijohto yläpuolella | Luftpipeline | Надземный трубопровод | Надземни цевовод
HFA | kikötői létesítmény | faċilità portwarja | Havenfaciliteit | Obiekt portowy | Instalação portuária | facilități portuare | prístavné zariadenia | pristaniška naprava | Satamalaitteisto | Hamnanläggning | Портовое оборудование | Лучка инфраструктура
HMO | kikötő kapitányság | kapitanerija | Havenkantoor | Kapitanat portu | Capitania do porto | căpitănie | Kapitanát | pristaniška kapitanija | Satamakonttori | Hamnkaptenens kontor | Капитания порта | Лучка капетанија
SHY | hajógyár | tarzna | Scheepswerf | Stocznia | Estaleiro naval | șantier naval | lodenica | ladjedelnica | Telakka | Varv | Судостроительный завод | Бродоградилиште
REF | hulladéklerakó | post għar-rimi ta’ skart | Afval afgiftepunt | Wysypisko śmieci | Instalação de recolha de resíduos | stație de colectare a deșeurilor | skládka odpadu | odlagališče odpadkov | Jäteasema | Sopinsamlingspunkt | отвал грунта | Складиште отпадних материја
MAR | hajózási jel(zés) | sinjal ta’ avviż | Verkeersteken | Znak informacyjny | Painel de sinalização | panou de semnalizare | plavebný znak | plovbna oznaka | Ilmoitusmerkki | Trafikmärke | Информационный знак | Пловидбени знак
LIG | fény | dawl | Licht | Światło | Luz | semnal luminos | svetlo | svetloba | Valo | Ljus | Огонь | Светло
SIG | jelzőállomás | stazzjon tas-sinjalar | Seinstation | Stacja sygnalizacyjna | Estação de sinalização | stație de semnalizare | signálna stanica | signalna postaja | Merkinantoasema | Signalstation | Сигнальная станция | Сигнална станица
TUR | fordítóhely | baċir għad-dawran | Zwaaikom | Obrotnica | Bacia de viragem | loc de rondou | obratisko | obračališče | Kääntöallas | Vändplats | разворотный бассейн | Базен за маневрисање
CBR | csatornahíd | pont fil-kanal | Aquaduct | Most kanałowy | Ponte-aqueduto | pod canal | akvadukt | most čez kanal | Kanavasilta | Kanalbro | Аквиадук | Мост на каналу
TUN | alagút | mina | Tunnel | Tunel | Túnel | tunel | tunel | predor | Tunneli | Tunnel | Туннель | Тунел
BCO | határállomás | kontroll fil-fruntieri | Grensstation | Kontrola graniczna | Posto fronteiriço | punct control trecere frontieră | hraničná kontrola | mejna kontrola | Rajatarkastus | Gränskontroll | Пограничный контроль | Гранична контрола
REP | jelentkezési pont | punt ta’ rappurtar | Meldpunt | Punkt meldunkowy | Ponto de notificação | punct raportare | miesto hlásenia | točka javljanja | Raportointipiste | Rapporteringspunkt | Точка оповещения | Пријавна тачка
FLO | zsilipkapu | xatba għall-għargħar | Keersluis | Śluza | Comporta | poartă pentru regularizare debit | protipovodňové vráta | drsna vrata | Sulkuportti | Dammlucka | Заградительные ворота шлюза | Устава за евакуацију поплавног таласа
SLI | hajólift | makkinarju għall-irfigħ tal-bastimenti | Scheepslift | Podnośnia statków | Elevador de navios | sincrolift nave | lodný výťah | ladijsko dvigalo | Laivahissi | Fartygshiss | Судоподъемник | Бродски лифт
DUK | búvár | kanal tad-drenaġġ | Duiker | Przepust | Aqueduto | scafandru | zhybka | kanal | Holvirumpu | Kulvert | Водопропуск | Одводни канал
VTC | forgalomirányító központ | ċentru tat-traffiku tal-bastimenti | Verkeersleidingcentrum | Centrum ruchu statków | Centro de tráfego de embarcações | centru de management al traficului | centrum riadenia plavby | prometno središče za plovila | Alusliikennekeskus | Center för fartygstrafik | Центр управления движением судов | Центар за управљање саобраћајем
RES | gyűjtő medence | ġibjun | Spaarbekken | Zbiornik | Albufeira | lac de acumulare | vodná nádrž | akumulacijsko jezero | Patoallas | Vattenmagasin | Водохранилище | Акумулација
LKB | zsilip várakozóhely | baċir ta’ bieb tal-ilma magħluq | Sluiskolk | Komora śluzy | Bacia de eclusa | bazinul ecluzei | plavebná komora | splavnica | Sulkukammio | Slusskammare | Шлюзовая камера | Комора преводнице
BRO | hídnyílás | ftuħ ta’ pont | Brugopening | Otwieranie mostu | Ponte a abrir | pod în deschidere | mostný otvor | prehod mostu | Avattu silta | Broöppning | Разводной мост | Мостовски отвор
BNS | üzemanyagtöltő állomás | stazzjon tal-karburant | Bunker-/tankstation | Bunkierka / Stacja tankowania | Posto de abastecimento | bunker/stație alimentare combustibil | zásobovacia/tankovacia stanica | tank/polnilnica goriva | Tankkausasema | Bunkrings-/tankstation | бункеровка/заправочная станция | Терминал за снадбевање бродова горивом
CODUL DE ACCESIBILITATE A GHEȚII
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
A | navigation normal | Нормално корабоплаване | Navegación normal | normální plavební provoz | Normal skibsfart | Schifffahrt normal | Tavapärane navigatsioon | Κανονική ναυσιπλοΐα | Navigation normale | Normalna plovidba | navigazione normale | Normāla kuģošana | Įprasta laivyba
B | navigation not yet hindered | Корабоплаването все още е възможно | Navegación posible | plavba je ještě možná | Skibsfarten hindres endnu ikke | Schifffahrt wird noch nicht behindert | Navigatsioon ei ole veel takistatud | Ναυσιπλοΐα που δεν παρεμποδίζεται ακόμη | Navigation possible | Plovidba još uvijek moguća | navigazione non ancora ostacolata | Kuģošana vēl nav traucēta | Nekliudoma laivyba
F | low traffic | Слабо корабоплаване | Tráfico escaso | slabý plavební provoz | Lav trafiktæthed | wenig Schifffahrt | Vähene liiklus | Χαμηλός ρυθμός κυκλοφορίας | Trafic faible | Slab promet | scarso traffico | Neliela satiksmes intensitāte | Neintensyvus eismas
L | no navigation without breaking | Корабоплаване само след ледоразбивач | Navegación imposible sin rompehielos | nelze plout bez lámání ledu | Ingen skibsfart uden isbryder | keine Schifffahrt ohne Eisbrecher | Vaid katkestustega liiklus võimalik | Καμία ναυσιπλοΐα χωρίς θραύση των πάγων | navigation seulement derrière brise-glace | Nema plovidbe bez lomljenja leda | nessuna navigazione senza rompighiaccio | Kuģošana tikai ar ledus laušanu | Laivyba įmanoma tik naudojant ledlaužį
C | navigation possible for motorvessels with more than 0,74 kW (1 hp) per 2 tons | Корабоплаването е възможно само за кораби с мощност над 0,5 к.с. на тон | Navegación posible para embarcaciones motorizadas con más de 0,74 Kw (1cv) por 2 toneladas | plavba možná pro motorové lodě s výkonem od 0,74 kW (l ks) na 2 tuny | Skibsfart er mulig for motorbåde med mere end 0,74 Kw (1 HK) pr. 2 tons | Schifffahrt möglich für Motorschiffe ab 0,74 kW (1 PS) pro 2 Tonnen | Mootorlaevade (suurema võimsusega kui 0,74 Kw (1hp)/2 t) navigatsioon võimalik | Ναυσιπλοΐα δυνατή για μηχανοκίνητα σκάφη ισχύος άνω των 0,74 Kw (1 hp) ανά 2 κόρους | La navigation est possible pour automoteurs de plus de 0,74 Kw (1 ch) par 2 tonnes | Plovidba dozvoljena za plovila s motorom snage veće od 0,74 KW(1 ks)/2t | transito possibile per motonavi con potenza superiore a 0,74 kW (1 hp) per 2 tonnellate | Kuģošana iespējama motorkuģiem, kuru jauda ir lielāka nekā 0,74 Kw (1 ZS) uz 2 tonnām | Laivyba leidžiama motorlaiviams, kurių galia yra didesnė nei 0,74 kW (1 hp) 2 tonoms
D | navigation possible for motorvessels with more than 0,74 kW (1 hp) per ton | Корабоплаването е възможно само за кораби с мощност над 1 к.с. на тон | Navegación posible para embarcaciones motorizadas con más de 0,74 Kw (1cv) por tonelada | plavba možná pro motorové lodě s výkonem od 0,74 kW (l ks) na tunu | Skibsfart er mulig for motorbåde med mere end 0,74 Kw (1 HK) pr. ton | Schifffahrt möglich für Motorschiffe ab 0,74 kW (1 PS) pro Tonne | Mootorlaevade (suurema võimsusega kui 0,74 Kw (1hp)/1 t) navigatsioon võimalik | Ναυσιπλοΐα δυνατή για μηχανοκίνητα σκάφη ισχύος άνω των 0,74 Kw (1 hp) ανά κόρο | La navigation est possible pour automoteurs de plus de 0,74 Kw (1 ch) par tonne | Plovidba dozvoljena za plovila s motorom snage veće od 0,74 KW(1 ks)/t | transito possibile per motonavi con potenza superiore a 0,74 kW (1 hp) per tonnellata | Kuģošana iespējama motorkuģiem, kuru jauda ir lielāka nekā 0,74 Kw (1 ZS) uz tonnu | Laivyba leidžiama motorlaiviams, kurių galia yra didesnė nei 0,74 kW (1 hp) tonai
E | navigation possibilities remain constant | Възможностите за корабоплаване не са променени | Posibilidades de navegación estables | setrvalé plavební podmínky | Ingen ændring af de nuværende sejlmuligheder | heutige Fahrmöglichkeiten bleiben gleich | Navigatioonivõimalused konstantsed | Οι δυνατότητες ναυσιπλοΐας παραμένουν σταθερές | Les possibilités de navigation sont constantes | Uvjeti plovidbe ostaju isti | condizioni di transito costanti | Kuģošanas iespējas nemainās | Nepakitusios laivybos sąlygos
G | navigation possibilities may deteriorate rapidly | Възможно е рязко влошаване на условията за корабоплаване | Posibilidades de navegación que pueden deteriorarse rápidamente | plavební podmínky se mohou náhle zhoršit | Sejlmulighederne kan hurtigt forværres | Fahrmöglichkeit kann sich schnell verschlechtern | Navigatsioonivõimalused võivad kiiresti halveneda | Οι δυνατότητες ναυσιπλοΐας μπορούν να επιδεινωθούν ταχέως | Les possibilités de navigation peuvent se détériorer rapidement | Uvjeti plovidbe mogu se naglo pogoršati | navigabilità che può peggiorare rapidamente | Kuģošanas iespējas var strauji pasliktināties | Laivybos sąlygos gali greitai pablogėti
H | no navigation but no obstruction | Корабоплаването е преустановено, но няма препятствия | Navegación imposible pero sin obstrucciones | přerušení plavby bez plavebních překážek | Ingen skibsfart, men ingen hindring | keine Schifffahrt, aber keine Schifffahrtssperre | Navigatsiooni ei toimu, aga takistust ei ole | Καμία ναυσιπλοΐα αλλά ούτε και παρεμπόδιση | Interruption de navigation même sans obstacle | Nema plovidbe, nema prepreka | nessun transito anche senza ostruzione | Kuģošana nenotiek, bet kuģošanas aizliegums nepastāv | Laivyba neleidžiama, tačiau kliūčių nėra
M | navigation possible with the aid of ice breakers | Корабоплаването е възможно само с ледорезни приспособления | Navegación posible con asistencia de rompehielos | plavba je možná s pomocí ledoborce | Skibsfart mulig med støtte fra isbrydere | Schifffahrt mit Eisbrecher möglich | Navigatsioon võimalik jäämurdjate abiga | Ναυσιπλοΐα δυνατή με τη βοήθεια παγοθραυστικών | La navigation est possible à l'aide d'un brise-glace | Plovidba moguća uz upotrebu ledolomca | transito possibile con l'intervento dei rompighiaccio | Kuģošana iespējama ar ledlaužu palīdzību | Laivyba galima naudojant ledlaužį
K | navigation possible in convoy or towage | Корабоплаването е възможно в състав или с буксир | Navegación posible en convoy o remolque | plavba je možná ve skupině plavidel za sebou nebo ve vlečné sestavě | Skibsfart mulig i konvoj eller på slæb | Fahren im Konvoi oder Schlepp möglich | Navigatsioon võimalik kolonnis või pukseerides | Ναυσιπλοΐα δυνατή σε νηοπομπές ή με ρυμούλκιση | La navigation est possible en convois ou avec remorqueur | Plovidba moguća u sastavu ili u teglju | navigazione possibile in convoglio o in traino | Kuģošana iespējama karavānā vai, velkot tauvā | Laivyba galima vilkstine arba su vilkiku
T | navigation possibilities may improve rapidly | Възможно е рязко подобряване на условията за корабоплаване | Posibilidades de navegación que pueden mejorar rápidamente | plavební podmíky se mohou náhle zlepšit | Sejlmulighederne kan hurtigt forbedres | Fahrmöglichkeit kann sich schnell verbessern | Navigatsioonivõimalused võivad kiiresti paraneda | Οι δυνατότητες ναυσιπλοΐας μπορούν να βελτιωθούν ταχέως | Les possibilités de navigation peuvent s'améliorer rapidement | Uvjeti plovidbe se mogu naglo poboljšati | navigabilità che può migliorare rapidamente | Kuģošanas iespējas var strauji uzlaboties | Laivybos sąlygos gali greitai pagerėti
P | inland ports can hardly be reached | Речните пристанища са трудно достъпни | Puertos interiores casi inaccesibles | vnitrozemské přístavy jsou těžko dosažitelné | Indlandshavne svært tilgængelige | Innenhäfen kaum erreichbar | Siseveesadamad raskesti ligipääsetavad | Δύσκολη προσέγγιση των εσωτερικών λιμένων | L'arrivée aux ports intérieurs est très difficile | Riječne luke teško dostupne | porti fluviali difficilmente raggiungibili | Piekļuve iekšzemes ostām apgrūtināta | Vidaus uostai sunkiai pasiekiami
V | no navigation allowed | Преустановено корабоплаване | Navegación prohibida | zákaz plavby | Sejlads ikke tilladt | Fahrverbot | Navigatsioon keelatud | Δεν επιτρέπεται η ναυσιπλοΐα | Navigation interrompue | Plovidba nije dopuštena | nessun transito consentito | Kuģošana aizliegta | Laivyba draudžiama
X | navigation in convoys compulsory | Плаването в състав е задължително | Obligatorio navegar en convoy | přikázaná plavba plavidel ve skupině za sebou | Sejlads i konvoj er påbudt | Konvoifahrt verpflichtend | Navigatsioon kolonnis kohustuslik | Υποχρεωτική ναυσιπλοΐα σε νηοπομπές | Navigation en convois obligatoire | Obvezna plovidba u sastavima | obbligo di navigazione in convoglio | Obligāta kugošana karavānā | Privaloma laivyba vilkstine
CODUL DE ACCESIBILITATE A GHEȚII
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
A | normális/szokásos hajózás | navigazzjoni normali | Scheepvaart normaal | żegluga normalna | Navegação normal | navigație normală | normálna plavba | normalna plovba | normaali alusliikenne | Normal sjöfart | Нормальные условия для судоходства | Нормална пловидба
B | hajózás még nem korlátozott | navigazzjoni għadha mhux imfixkla | Scheepvaart ondervindt nog geen hinder | żegluga jeszcze bez przeszkód | Navegação possível | navigație posibilă | plavba ešte nie je obmedzená | plovba je še vedno možna | alusliikenteessä ei vielä esteitä | Ännu obehindrad sjöfart | судоходство допустимо | Пловидба још увек могућа
F | jelentéktelen hajóforgalom | ftit li xejn traffiku | Scheepvaart gering | niskie natężenie żeglugi | Tráfego ligeiro | trafic scăzut | slabá premávka | malo prometa | vähäinen alusliikenne | Låg sjötrafik | низкий судопоток | Слаб саобраћај
L | jégtörõ nélkül hajózási tilalom | ebda navigazzjoni projbita mingħajr tkissir | Geen vaart indien niet wordt gebroken | żegluga tylko w asyście lodołamacza | Navegação impossível sem quebra-gelos | nu se navighează fără dispozitiv de spargere a gheții | zákaz plavby bez ľadoborca | plovba brez ledolomilca ni dovoljena | ei alusliikennettä ilman jäänmurtamista | Ingen sjöfart utan isbrytning | плавание только под проводкой ледокольных средств | Нема пловидбе без ломљења леда
C | hajózás csak géphajóknak: minimum 0,74 kW 2 tonnánkként | navigazzjoni possibbli għal bastimenti b’mutur ta’ potenza ogħla minn 0,74 kW (1 hp) għal kull 2 tunnellati | Vaart mogelijk voor motorschepen vanaf 0,74 kW (1 pk) per 2 ton | żegluga dozwolona dla jednostek z napędem silnikowym o mocy powyżej 0,74 kW (1 KM) na każde 2 tony masy | Navegação possível a embarcações motorizadas com mais de 0,74 kW (1cv) por 2 toneladas | navigația este posibilă pentru automotoare cu mai mult de 0,74 Kw (1 CP) per 2 tone | plavba možná pre motorové plavidlá s výkonom viac ako 0,74 kW (1 hp) na 2 t | plovba mogoča za motorna plovila z močjo večjo od 0,74 kW (1 KM) na 2 toni | alusliikenne mahdollista moottorialuksille, joiden teho on yli 0,74 Kw (1 hp) 2 tonnia kohden | Sjöfart möjlig med motorfartyg över 0,74 kW(1hp) per 2 ton | навигация только для самоходных судов с удельной мощностью более 1 лошадиной силы на 2 тонны | Пловидба дозвољена за самохотке (пловила са сопственим погоном) са више од 0,74 kW (1KS) по 2t
D | hajózás csak géphajóknak: minimum 0,74 kW tonnánkként | navigazzjoni possibbli għal bastimenti b’mutur ta’ potenza ogħla 0,74 kW (1 hp) għal kull tunnellata | Vaart mogelijk voor motorschepen vanaf 0,74 kW (1 pk) per 1 ton | żegluga dozwolona dla jednostek z napędem silnikowym o mocy powyżej 0,74 kW (1 KM) na tonę masy | Navegação possível a embarcações motorizadas com mais de 0,74 kW (1cv) por tonelada | navigația este posibilă pentru automotoare cu mai mult de 0,74 Kw (1 CP) per tonã | plavba možná pre motorové plavidlá s výkonom viac ako 0,74 kW (1 hp) / t | plovba mogoča za motorna plovila z močjo večjo od 0,74 kW (1 KM) na tono | alusliikenne mahdollista moottorialuksille, joiden teho on yli 0,74 Kw (1 hp) tonnia kohden | Sjöfart möjlig med motorfartyg över 0,74 kW(1hp) per ton | навигация только для самоходных судов с удельной мощностью более 1 лошадиной силы на 1 тонну | Пловидба дозвољена за самохотке (пловила са сопственим погоном) са више од 0,74 kW (1KS) по 1t
E | hajózási feltételek állandósultak | il-possibbiltajiet ta’ navigazzjoni jibqgħu kostanti | Huidige vaarmogelijkheid blijft hetzelfde | warunki żeglugi bez zmian | Possibilidades de navegação estáveis | posibilitățile de navigație rămân constante | súčasné plavebné podmienky zostávajú rovnaké | možnost plovbe ostaja nespremenjena | alusliikennemahdollisuudet pysyvät ennallaan | Farbarhet förblir oförändrad | навигационные условия без изменений | Услови пловидбе остају исти
G | a hajózási lehetõségek gyorsan változhatnak | il-possibbiltajiet ta’ navigazzjoni jistgħu jiddeterjoraw rapidament | Vaarmogelijkheid kan snel verslechteren | możliwość gwałtownego pogorszenia warunków żeglugi | Possibilidades de navegação podem deteriorar-se rapidamente | posibilitățile de navigație se pot deteriora rapid | plavebné podmienky sa môžu rýchlo zhoršiť | možnost plovbe se lahko hitro poslabša | alusliikennemahdollisuudet voivat huonontua nopeasti | Farbarheten kan minska snabbt | возможно резкое ухудшение условий плавания | Услови пловидбе се могу нагло погоршати
H | hajózás akadálymentesség ellenére nincs | ebda navigazzjoni iżda ebda ostaklu | Geen vaart, maar niet gestremd | żegluga przerwana mimo braku zakazu żeglugi | Navegação impossível, mas não há obstruções | nu se navighează dar nu sunt obstrucții | zastavená plavba, bez plavebnej prekážky | plovba ni dovoljena, vendar ni ovir | ei alusliikennettä, vaikkei estettä | Ingen sjöfart, men ingen blockering | судоходства нет, но движение разрешено | Нема пловидбе, нема препрека
M | hajózás jégtörõvel lehetséges | navigazzjoni possibbli bit-tkissir tas-silġ | Scheepvaart met ijsbrekers mogelijk | możliwość żeglugi w asyście lodołamaczy | Navegação possível com a assistência de quebra-gelos | navigația este posibilă cu ajutorul spărgătoarelor de gheață | plavba možná s pomocou ľadoborca | plovba mogoča s pomočjo ledolomilca | alusliikenne mahdollista jäänmurtajien avulla | Sjöfart möjlig med hjälp av isbrytare | плавание под проводкой ледокольных средств разрешено | Пловидба могућа уз употребу ледоломца
K | hajózás kötelékben vagy vontatva lehetséges | navigazzjoni possibbli f’konvoj jew permezz ta’ rmonkar | Varen in konvooi of sleep mogelijk | możliwość żeglugi w konwojach lub za holownikiem | Navegação possível em comboio ou a reboque | navigația este posibilă în convoi sau remorcat | plavba možná v zostave alebo vo vleku | plovba mogoča v konvoju ali z vlečenjem | alusliikenne mahdollista kytkyeessä tai hinauksessa | Sjöfart möjlig i konvoj eller med bogsering | движение в составах или с буксирами | Пловидба могућа за потискиване или тегљене саставе
T | hajózási lehetõségek gyorsan javulhatnak | il-possibbiltajiet ta’ navigazzjoni jistgħu jitjiebu rapidament | Vaarmogelijkheid kan snel verbeteren | możliwość szybkiej poprawy warunków żeglugi | Possibilidades de navegação podem melhorar rapidamente | posibilitățile de navigație se pot ameliora rapid | plavebné podmienky sa môžu rýchlo zlepšiť | možnost plovbe se lahko hitro izboljša | alusliikennemahdollisuudet voivat parantua nopeasti | Farbarheten kan öka snabbt | возможно резкое улучшение условий плавания | Услови пловидбе се могу нагло побољшати
P | belvízi kikötõk alig elérhetõk | diffiċli jintlaħqu l-portijiet interni | Binnenhavens nauwelijks bereikbaar | ograniczone możliwości dotarcia do portów śródlądowych | Portos interiores quase inacessíveis | accesul în porturile interioare poate fi foarte dificil | vnútrozemské prístavy sú ťažko dosiahnuteľné | rečna pristanišča so težko dostopna | vaikea päästä sisävesisatamiin | Inlandshamnar mycket svåråtkomliga | доступ к внутренним портам сильно затруднён | Речне луке тешко доступне
V | hajózási tilalom | navigazzjoni projbita | Vaarverbod | zakaz żeglugi | Navegação proibida | navigația nu este permisă | zákaz plavby | plovba prepovedana | alusliikenne ei ole sallittua | Ingen sjöfart tillåten | навигация запрещена | Пловидба није дозвољена
X | hajózás csak kötelékben engedélyezett | in-navigazzjoni f’konvojs hija obbligatorja | Verplichte konvooivaart | obowiązek żeglugi w konwojach | Obrigatório navegar em comboio | navigația în convoaie este obligatorie | povinná plavba v zostave | obvezna plovba v konvojih | alusliikenne kytkyeissä pakollista | Obligatorisk konvojgång | движение только в составах | Обавезна пловидба у саставима
CODUL DE CLASIFICARE A GHEȚII
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
A | navigable | Свободно корабоплаване | Navegable | splavný | Uhindret sejlads | gut befahrbar | Navigeeritav | Πλεύσιμος | navigable | Plovno | navigabile | kuģojams | Laivyba be kliūčių
B | fairly navigable | Умерено корабоплаване | Razonablemente navegable | dobře splavný | Næsten uhindret sejlads | ziemlich gut befahrbar | Keskmiselt navigeeritav | Πλεύσιμος σε μικρό βαθμό | raisonnablement navigable | Pretežno plovno | abbastanza navigabile | diezgan labi kuģojams | Laivyba beveik be kliūčių
C | navigable with difficulty | Затруднено корабоплаване | Navegación difícil | obtížně splatný | Sejlads vanskelig | schwer befahrbar | Raskustega navigeeritav | Πλεύσιμος με δυσκολία | navigation pénible | Plovno uz teškoće | navigabile con difficoltà | grūti kuģojams | Sunki laivyba
D | navigable only with great difficulty | Силно затруднено корабоплаване | Navegación muy difícil | velmi obtížně splavný | Sejlads meget vanskelig | sehr Schwer befahrbar | Üksnes suurte raskustega navigeeritav | Πλεύσιμος μόνο με μεγάλη δυσκολία | navigation très pénible | Plovno uz velike teškoće | navigabile solo con grande difficoltà | ļoti grūti kuģojams | Laivyba labai sunki
E | no navigation allowed | Преустановено корабоплаване | Navegación prohibida | zákaz plavby | Sejlads ikke tilladt | Fahrverbot | Navigatsioon keelatud | Δεν επιτρέπεται καθόλου η ναυσιπλοΐα | navigation interrompue | Plovidba nije dopuštena | nessuna navigazione consentita | kuģošana aizliegta | Laivyba draudžiama
CODUL DE CLASIFICARE A GHEȚII
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
A | hajózható | navigabbli | Goed bevaarbaar | żeglowny | Navegável | navigabil | splavný | plovno | Kulkukelpoinen | Farbar | беспрепятственное судоходство | Пловно
B | teljes mértékben hajózható | pjuttost navigabbli | Vrij goed bevaarbaar | dość żeglowny | Razoavelmente navegável | navigabil în condiții acceptabile | pomerne dobre splavný | precej dobro plovno | melko kulkukelpoinen | Relativt farbar | достаточно беспрепятственное судоходство | Релативно пловно
C | nehezen hajózható | navigabbli b’xi diffikultajiet | Moeilijk bevaarbaar | żeglowny z trudnościami | Navegação difícil | navigabil cu dificultate | splavný s ťažkosťami | težko plovno | hankalasti kulkukelpoinen | Svårframkomlig | затруднённое судоходство | Пловно уз потешкоће
D | nagyon nehezen hajózható | navigabbli biss b’ħafna diffikultà | Zeer moeilijk bevaarbaar | żeglowny ale z dużymi trudnościami | Navegação muito difícil | navigabil numai cu mare dificultate | splavný len s veľkými ťažkosťami | zelo težko plovno | erittäin hankalasti kulkukelpoinen | Mycket svårframkomlig | сильно затруднённое судоходство | Пловно уз велике потешкоће
E | hajózási tilalom | navigazzjoni projbita | Vaarverbod | zakaz żeglugi | Navegação proibida | navigația nu este permisă | zákaz plavby | plovba prepovedana | alusliikenne ei ole sallittua | Ingen sjöfart tillåten | судоходство запрещено | Пловидба није дозвољена
CODUL CONDIȚIILOR GHEȚII
Valoare | Grosime | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
A | — | clear water | Чиста вода | Aguas normales | volná voda | Isfrit farvand | offenes Wasser | selge vesi | Ύδατα άνευ πάγου | Eaux normales | Vodni put bez leda | acque normali | brīvs ūdens | Ledo nėra
B | 0 — 4 cm | light spread floating ice | Разпръснат плаващ лед | Hielo flotante ligero disperso | ledová tříšť | Let spredt drivis | Treibeis | kergelt leviv triivjää | Ελαφρά διασκορπισμένα τεμάχια επιπλέοντος πάγου | glaces légères dispersées | Slabo formiran tanak plutajući led | leggero ghiaccio galleggiante sparso | izklaidu peldošs plāns ledus | Plonas pasklidęs plūduriuojantis ledas
C | 0 — 4 cm | light floating ice | Рядък плаващ лед | Hielo flotante ligero | slabá ledová tříšť | Let drivis | leichtes Treibeis | kerge triivjää | Ελαφρά τεμάχια επιπλέοντος πάγου | glaces légères flottantes | Tanak plutajući led | ghiaccio leggero galleggiante | plāns peldošs ledus | Plonas plūduriuojantis ledas
D | 0 — 4 cm | light solid ice | Слабо заледяване | Hielo sólido ligero | slabý led | Tynd fast is | leichtes Eis | kerge tahke jää | Ελαφρά τεμάχια συμπαγούς πάγου | glace légère | Tanak sloj leda | leggero ghiaccio solido | plāna ledus kārta | Plonas ištisinis ledas
E | 4 — 8 cm | medium spread floating ice to 40 % covered | Средно разреден плаващ лед (до 40 % покритие) | Hielo flotante disperso medio que cubre hasta un 40 % | středně silná rozpýlená ledová tříšť, pokrytí do 40 % | Middelsvær drivis op til 40 % dækket | mittelschweres zerstreutes Treibeis, bis 40 % eisbedeckt | keskmiselt leviv triivjää kuni 40 % kattuvusega | Μέσου πάχους διασκορπισμένα τεμάχια επιπλέοντος πάγου που καλύπτουν επιφάνεια 40 % | glaces moyennes dispersées couvrant 40 % | Srednje formiran plutajući led, pokrivenost do 40 % | ghiaccio sparso galleggiante di spessore medio con copertura fino al 40 % | vidēji biezs izklaidu peldošs ledus klāj līdz 40 % ūdens virsmas | Vidutinio storio pasklidęs plūduriuojantis ledas (dengia iki 40 % paviršiaus)
F | 4 — 8 cm | medium spread floating ice 40 to 75 % covered | Средно разреден плаващ лед (40 %-70 % покритие) | Hielo flotante disperso medio que cubre entre un 40 % y un 75 % | středně silně rozptýlená ledová tříšť, pokrytí od 40 % do 75 % | Middelsvær drivis 40-75 % dækket | mittelschweres zerstreutes Treibeis, 40 bis 75 % eisbedeckt | keskmiselt leviv triivjää kattuvusega 40 % kuni 75 % | Μέσου πάχους διασκορπισμένα τεμάχια επιπλέοντος πάγου που καλύπτουν επιφάνεια 40 % έως 75 % | glaces moyennes flottantes dispersées couvrant 40 à 75 % | Srednje formiran plutajući led, pokrivenost od 40 do 75 % | ghiaccio sparso galleggiante di spessore medio con copertura compresa tra 40 % e 75 % | vidēji biezs izklaidu peldošs ledus klāj 40 līdz 75 % ūdens virsmas | Vidutinio storio plūduriuojantis ledas (dengia 40–75 % paviršiaus)
G | 4 — 8 cm | medium floating ice more than 75 % in sludge or lead | Плаващ лед със средна дебелина покриващ над 75 % | Hielo flotante medio que cubre más del 75 % del canal | středně silně rozptýlená ledová tříšť, pokrytí vice než 75 % | Middelsvær drivis mere end 75 % dækket | mittelschweres Treibeis, mehr als 75 % der Rinne eisbedeckt | keskmiselt leviv triivjää, rohkem kui 75 % jääpankade või jäävallidena | Μέσου πάχους τεμάχια επιπλέοντος πάγου που καλύπτουν επιφάνεια άνω του 75 % του διαύλου | glaces moyennes flottantes dispersées couvrant plus de 75 % du chenal | Srednje formiran plutajući led, pokrivenost veća od 75 % | ghiaccio galleggiante di spessore medio costituito per più del 75 % da frammenti o canale ricoperto da frammenti | vidēji biezs peldošs ledus, vairāk nekā 75 % ūdens virsmas klāta vižņiem | Vidutinio storio plūduriuojantis ledas (daugiau kaip 75 % sudaro ižas) arba vandens tarpas tarp ledų
H | 4 — 8 cm | medium vast ice | Средно дебел твърд лед | Hielo compacto medio | středně silně pevný led | Middelsvær fast is | mittelschweres festes Eis | keskmine rüsijää | Μέσου πάχους εκτεταμένος πάγος | glace moyenne | Srednje velika santa leda | ghiaccio di spessore medio fisso | vidēji biezs blīvs ledus | Vidutinio storio ištisinis ledas
K | 8 — 12 cm | heavy spread floating ice to 40 % covered | Дебел плаващ лед (до 40 % покритие) | Hielo flotante pesado disperso que cubre hasta un 40 % | silná rozptýlená ledová tříšť, pokrytí do 40 % | Svær drivis op til 40 % dækket | schweres zerstreutes Treibeis, bis 40 % eisbedeckt | mitteleviv triivjää kuni 40 % kattuvusega | Βαρέα διασκορπισμένα τεμάχια επιπλέοντος πάγου σε έκταση 40 % | glaces lourdes flottantes dispersées couvrant jusqu'à 40 % | Dobro formiran plutajući led, pokrivenost do 40 % | ghiaccio spesso galleggiante con copertura fino al 40 % | biezs izklaidu peldošs ledus klāj līdz 40 % ūdens virsmas | Storas pasklidęs plūduriuojantis ledas (dengia iki 40 % paviršiaus)
L | 8 — 12 cm | heavy spread floating ice 40 to 75 % covered | Дебел плаващ лед (40 %-70 % покритие) | Hielo flotante pesado disperso que cubre entre un 40 % y un 75 % | silná rozptýlená ledová tříšť, pokrytí od 40 % do 75 % | Svær drivis 40-75 % dækket | schweres zerstreutes Treibeis, 40 bis 75 % eisbedeckt | mitteleviv triivjää kattuvusega 40 % kuni 75 % | Βαρέα διασκορπισμένα τεμάχια επιπλέοντος πάγου σε έκταση από 40 % έως 75 % | glaces lourdes flottantes dispersées couvrant 40 à 75 % | Dobro formiran plutajući led, pokrivenost od 40 do 75 % | ghiaccio spesso galleggiante con copertura compresa tra il 40 % e il 75 % | biezs izklaidu peldošs ledus klāj 40 līdz 75 % ūdens virsmas | Storas pasklidęs plūduriuojantis ledas (dengia 40–75 % paviršiaus)
M | 8 — 12 cm | heavy dense floating ice with more than 75 % chance on coagulation | Дебел плътен лед с вероятност за заледяване над 75 % | Hielo flotante pesado denso con más del 75 % de posibilidades de cuajar | těžká stlačená ledová tříšť s více než 75 % možnosti koagulace | Svær og pakket drivis mere end 75 % dækket; risiko for fastfrysning | schweres zusammengepferchtes Treibeis mit mehr als 75 %, Gefahr für Dammbildung | paks tihe triivjää jäätumusega rohkem kui 75 % | Βαρέα τεμάχια επιπλέοντος πάγου με πιθανότητες πήξης άνω του 75 % | glaces lourdes flottantes dispersées couvrant plus de 75 % et chance de coagulation | Debele sante leda, 75 % mogućnost zaleđivanja | ghiaccio spesso galleggiante con più del 75 % di probabilità di addensamento | ļoti blīvs peldošs ledus, sablīvējumu veidošanās iespēja — vairāk nekā 75 % | Storas tankus plūduriuojantis ledas, koaguliacijos tikimybė didesnė nei 75 %
P | 8 — 12 cm | heavy floating ice with more than 75 % in sludge or lead currently broken sludge | Дебел плътен лед покриващ над 75 % или току що разбит лед | Hielo flotante pesado que cubre más del 75 % del canal recientemente abierto | těžká ledová tříšť, pokrytí více než 75 %, plavební dráha dnes prolomena | Svær drivis mere end 75 % dækket; sejlrende er brudt for nylig | schweres Treibeis mehr als 75 % der Rinne eisbedeckt, Rinne heute gebrochen | paks triivjää rohkem kui 75 % jääpankadena või ajuti murduvate jäävallidena | Βαρέα τεμάχια προσφάτως θραυσθέντος επιπλέοντος πάγου σε επιφάνεια άνω του 75 % του διαύλου | glaces lourdes flottantes couvrant plus de 75 % du chenal, chenal brisé recemment | Debele sante leda, s više od 75 % leda u komadu ili trenutno polomljenih komada | ghiaccio spesso galleggiante costituito per più del 75 % da frammenti o canale attualmente coperto da ghiaccio frammentato | biezs peldošs ledus ar vairāk nekā 75 % vižņu, kuri nesen salūzuši | Storas plūduriuojantis ledas (daugiau kaip 75 % sudaro ižas) arba šiuo metu tarp ledų pralaužtas vandens tarpas
R | 8 — 12 cm | heavy vast ice | Дебел твърд лед | Hielo compacto pesado | těžký pevný led | Svær fast is | schweres festes Eis | paks rüsijää | Βαρέα τεμάχια εκτεταμένου πάγου | glace solide épaisse | Teška velika santa leda | ghiaccio spesso ed esteso | biezs blīvs ledus | Storas ištisinis ledas
S | > 12 cm | very heavy floating ice en solid ice nearly 100 % covered | Много дебел плаващ твърд лед покриващ почти 100 % | Hielo flotante muy pesado y sólido que cubre casi el 100 % | velmi těžká ledová tříšť a ledové kry, téměř 100 % pokryto ledem | Meget svær drivis og fast is næsten 100 % dækket | sehr schweres Treibeis und Packeis, fast 100 % eisbedeckt | väga paks triivjää tahke jääna peaagu 100 % kattuvusega | Πολύ βαρέα τεμάχια συμπαγούς επιπλέοντος πάγου σε έκταση σχεδόν 100 % | glaces flottantes trés lourdes et banquise couvrant presque 100 % | Vrlo debele sante i tvrdi led sa skoro 100 % pokrivenosti | ghiaccio galleggiante molto spesso e solido con copertura quasi del 100 % | ļoti biezs peldošs ledus un ledus kārta klāj gandrīz 100 % ūdens virsmas | Labai storas plūduriuojantis ledas ir ištisinis ledas dengia beveik 100 % paviršiaus
U | > 40 cm | ice dam or drifting ice | Ледени прегради или струпвания | Barrera de hielo o hielo a la deriva | ledová bariéra nebo nahromadění ledu | Isdæmning eller isspærring | Eisdamm oder Eisstau | rüsijäävallid või rüsijää | Φράγμα πάγου ή παρασυρόμενος πάγος | barrage de glace ou débâcle | Ledena prepreka ili plutajući led | barriera di ghiaccio o ghiaccio alla deriva | ledus aizsprosts vai dreifējošs ledus | Ledo lyčių sangrūda arba dreifuojantis ledas
O | — | disappearing (pap)ice, no longer obstructing | Топящ се лед, няма препятствия | Hielo a punto de fundirse que ya no constituye un obstáculo | tenký měkký led, který již nepřekáží | Smelteis, ingen hindring længere | Pappeis, nicht länger behinderlich | kaduv jää, enam mitte takistav | Εξαφανιζόμενος πάγος που δεν προκαλεί πλέον εμπόδια | glaces fondantes, aucune gêne | Otapanje leda, nema prepreka | ghiaccio in fase di scioglimento, nessuna ostruzione | izzūdošs ledus, vairs nekavē kuģošanu | Tirpstantis, laivybai kliūčių nesudarantis ledas
V | — | navigation interrupted | Корабоплаването е преустановено | Navegación interrumpida | zákaz plavby | Skibsfarten er indstillet | Fahrverbot | navigeerimine katkestatud | Διακοπή ναυσιπλοΐας | navigation interrompue | Zabrana plovidbe | navigazione interrotta | kuģošana pārtraukta | Laivyba nutraukta
CODUL CONDIȚIILOR GHEȚII
Valoare | Grosime | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
A | — | jégmentes víz | ilma nadif | Open water | woda otwarta | Água livre | fără gheață | voľná voda | brez ledu | avovesi | Öppet vatten | чистая вода | Водни пут без леда
B | 0 — 4 cm | vékony szórványos jégtáblák | ftit silġ mifrux f’wiċċ l-ilma | Licht verspreid drijfijs | rozproszona, cienka kra lodowa | Gelo flutuante ligeiro disperso | gheață subțire plutitoare dispersată | ľadová triešť | plavajoči led | ohutta rikkonaista ajojäätä | Lätt spridd drivis | малоразреженный плавучий лёд | Слабо формиран танки плутајући лед
C | 0 — 4 cm | vékony jégtáblák | ftit silġ f’wiċċ l-ilma | Licht drijfijs | cienka kra lodowa | Gelo flutuante ligeiro | gheață subțire plutitoare | slabá ľadová triešť | tanek plavajoči led | ohutta ajojäätä | Lätt drivis | редкий плавучий лёд | Танак плутајући лед
D | 0 — 4 cm | könnyû beállt jég | ftit silġ solidu | Licht vast ijs | cienka pokrywa lodowa | Gelo compacto ligeiro | gheață subțire | slabý ľad | tanek trdni led | ohutta kiintojäätä | Lätt fastis | малосплочённый лёд | Танак слој леда
E | 4 — 8 cm | közepes szórványos jégtáblák 40 %-ig jégfedettségig | ammont medju ta’ silġ mifrux f’wiċċ l-ilma sa kopertura ta’ 40 % | Middelzwaar verspreid drijfijs tot 40 % bedekt | rozproszona kra lodowa średniej grubości, pokrycie do 40 % | Gelo flutuante médio disperso, cobrindo até 40 % | gheață mijlocie plutitoare dispersată acoperind 40 % | stredne silná rozptýlená ľadová triešť, pokrytie do 40 % | srednje debel plavajoči led, pokritost do 40 % | keskiraskasta rikkonaista ajojäätä, enintään peittävyys 40 % | Medelstor spridd drivis, 40 % istäcke | плавучий лёд средней разреженности (до 40 %) | Средње формиран плутајући лед, покривеност до 40 %
F | 4 — 8 cm | közepes szórványos jégtáblák 40 %-70 % közötti jégfedettséggel | ammont medju ta’ silġ mifrux f’wiċċ l-ilma b’kopertura ta’ bejn 40 % u 75 % | Middelzwaar verspreid drijfijs 40 tot 75 % bedekt | rozproszona kra lodowa średniej grubości, pokrycie 40 do 75 % | Gelo flutuante médio disperso, cobrindo 40 % a 75 % | gheață mijlocie plutitoare dispersată acoperind 40 % până la 75 % | stredne silná rozptýlená ľadová triešť, pokrytie od 40 % do 75 % | srednje debel plavajoči led, pokritost od 40 do 75 % | keskiraskasta rikkonaista ajojäätä, peittävyys 40–75 % | Medelstor spridd drivis, 40-75 % istäcke | плавучий лёд средней разреженности (40 % — 70 %) | Средње формиран плутајући лед, покривеност 40 do 75 %
G | 4 — 8 cm | közepes jégtáblák több mint 75 %-ban kásajégként vagy jégmentes sávokban | ammont medju ta’ silġ f’wiċċ l-ilma b’aktar minn 75 % minnu ħama jew ftuħ fis-silġ | Middelzwaar drijfijs met meer dan 75 % in geul of slop | kra lodowa średniej grubości, pokrycie powyżej 75 % kanału | Gelo flutuante médio, cobrindo mais de 75 % da esteira | gheață mijlocie plutitoare dispersată acoperind peste 75 % din șenal | stredne silná rozptýlená ľadová triešť, pokrytie viac ako 75 % | srednje debel plavajoči led, pokritost večja od 75 % | keskiraskasta ajojäätä, peittävyys yli 40–75 % väylästä | Medelstor spridd drivis, över 75 % av farrännan istäckt | плавучий лёд средней разреженности (больше 75 % ледового канала покрыто ледяной кашей) | Средње формиран плутајући лед, покривеност већа од 75 %
H | 4 — 8 cm | közepes beállt jég | silġ vast medju | Middelzwaar vast ijs | pokrywa lodowa średniej grubości | Gelo compacto médio | gheață mijlocie | stredne pevný ľad | srednje debel trdni led | keskiraskasta jäätä | Medeltjock fastis | лёд средней сплочённости | Средње велика санта леда
K | 8 — 12 cm | vastag szórványos jégtáblák 40 %-os jégfedettségig | ħafna silġ mifrux f’wiċċ l-ilma sa kopertura ta’ 40 % | Zwaar verspreid drijfijs tot 40 % bedekt | rozproszona, gruba kra lodowa, pokrycie do 40 % | Gelo flutuante pesado disperso, cobrindo até 40 % | gheață groasă plutitoare dispersată acoperind până la 40 % | silná a rozptýlená ľadová triešť, pokrytie do 40 % | debel plavajoči led, pokritost do 40 % | raskasta rikkonaista ajojäätä, peittävyys enintään 40 % | Tjock, spridd drivis, upp till 40 % istäcke | тяжелый разреженный плавучий лёд (до 40 %) | Добро формиран плутајући лед, покривенотс до 40 %
L | 8 — 12 cm | vastag jégtáblák 40 %-70 % közötti jégfedettséggel | ħafna silġ mifrux f’wiċċ l-ilma b’kopertura ta’ bejn 40 % u 75 % | Zwaar verspreid drijfijs 40 tot 75 % bedekt | rozproszona, gruba kra lodowa, pokrycie 40 do 75 % | Gelo flutuante pesado disperso, cobrindo 40 % a 75 % | gheață groasă plutitoare dispersată acoperind 40 % până la 75 % | silná a rozptýlená ľadová triešť, pokrytie od 40 % do 75 % | debel plavajoči led, pokritost od 40 do 75 % | raskasta rikkonaista ajojäätä, peittävyys 40–75 % | Tjock, spridd drivis, 40-75 % istäcke | тяжелый разреженный плавучий лёд (40 % — 75 %) | Добро формиран плутајући лед, покривеност 40 do 75 %
M | 8 — 12 cm | vastag jégtáblák több mint 75 %-os, torlaszképződés veszély | ħafna silġ dens f’wiċċ l-ilma b’ċans ta’ aktar minn75 % li jagħqad | Zwaar opeengepakt drijfijs met meer dan 75 % kans op propvorming | gęsta, gruba kra lodowa, pokrycie powyżej 75 %, możliwość koagulacji | Gelo flutuante pesado denso, com probabilidade de concreção superior a 75 % | gheață groasă plutitoare dispersată acoperind mai mult de 75 % și șanse de îngheț | hustá ľadová triešť s viac ako 75 % možnosťou koagulácie | debel plavajoči led, pokritost večja od 75 %, možnost sesedanja | raskasta tiheää ajojäätä, peittävyys yli 75 %, hyytymisvaara | Tätt sammanpackad drivis, över 75 % risk för stampisvall | очень сплочённый лёд, более 75 %-ая вероятность образования заторов | Плутајући лед велике густине, са 75 % шансе за коагулацију
P | 8 — 12 cm | vastag jégtáblák több mint 75 %-os fedettség, ma tört hajózócsatornával | ħafna silġ f’wiċċ l-ilma b’aktar minn 75 % minnu ħama jew ftuħ fis-silġ magħmul minn ħama attwalment imkissra | Zwaar drijfijs met meer dan 75 % in geul of slop, heden gebroken geul | gruba kra lodowa, pokrycie powyżej 75 % kanału, świeżo przełamany kanał | Gelo flutuante pesado cobrindo mais de 75 % da esteira, passagem aberta recentemente | gheață groasă plutitoare dispersată acoperind peste 75 % din șenal, șenal spart recent | silná a rozptýlená ľadová triešť, pokrytie viac ako 75 % plavebnej dráhy, dnes rozbitá ryha | debel plavajoči led, pokritost večja od 75 %, trenutno razbit | raskasta ajojäätä, peittävyys yli 75 % väylästä, joka on äskettäin murrettu | Tjock drivis, över 75 % av farrännan täckt, rännan bruten i dag | тяжелый плавучий лёд, более 75 %, в настоящий момент судоходство затруднено из-за ледяной каши в ледовом канале | Тешки плутајући лед са више од 75 % леда у комаду или тренутно поломљених комада
R | 8 — 12 cm | vastag beállt jég | silġ vast qawwi | Zwaar vast ijs | gruba pokrywa lodowa | Gelo compacto pesado | gheață groasă solidă | silne pevný ľad | debel trdni led | raskasta jäätä | Tjock fastis | очень сплочённый лёд | Тешка велика санта леда
S | > 12 cm | nagyon vastag úszó és parti jég közel 100 %-os jégfedettséggel | silġ qawwi ħafna f’wiċċ l-ilma u silġ solidu b’kopertura ta’ kważi 100 % | Zeer zwaar drijfijs en pakijs bijna 100 % bedekt | bardzo gruba kra lodowa i pokrywa lodowa, pokrycie niemal 100 % | Gelo flutuante e gelo compacto ultrapesados, cobrindo quase 100 % | banchize plutitoare groase acoperind aproape 100 % | veľmi pevná ľadová triešť a ľadovce, pokrytie takmer 100 % | zelo debel plavajoči led in trdni led, pokritost skoraj 100 % | erittäin raskasta ajojäätä ja kiintojäätä, peittävyys lähes 100 % | Mycket tjock drivis och fastis med nästan 100 % istäcke | очень тяжёлый плавучий и сплошной лёд (почти 100 %) | Веома тежак плутајући лед са чврстим ледом, покривеност скоро 100 %
U | > 40 cm | jégtorlasz vagy sodródó jég | diga tas-silġ jew silġ jinġarr mal-kurrent | IJsdam of kruiend ijs | bariera lodowa lub zator lodowy | Barreira de gelo ou gelo à deriva | pod de gheață sau gheață plutitoare | ľadová bariéra alebo nahromadenie ľadu | ledena ovira ali naplavine | jääpato tai ajojäätä | Stampisvall eller drivis | ледяной затор или скопление дрейфующего льда | Ледена преграда или лед у покрету
O | — | elolvadó (kásás) jég, akadályozás megszűnt | silġ (artab) li qed jinħall u li ma għadux jostakola | Verdwijnend (pap)ijs, niet meer hinderlijk | zanikający lód (papka), nie przeszkadzający w żegludze | Gelo em fusão, já não causa obstrução | ghețari topiți, nici unul periculos | strácajúci sa tenký ľad, žiadne prekážky | taljenje ledu, brez ovir | sulavaa jäätä, ei enää esteenä | Upplöst issörja, ingen blockering | разрушающийся лёд с проталинами, беспрепятственное судоходство | Отапање леда, нема препрека
V | — | hajózási szünetel | navigazzjoni interrotta | Scheepvaart onderbroken | zakaz żeglugi | Navegação suspensa | navigație întreruptă | zákaz plavby | prepoved plovbe | alusliikenne keskeytetty | Sjöfart förbjuden | судоходство остановлено | Забрана пловидбе
CODUL STĂRII GHEȚII
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
NOL | no limitation | Без ограничение | Sin limitación | bez omezení | Ingen begrænsninger | keine Behinderung | piirangut ei ole | Κανένας περιορισμός | pas de limitation | Nema ograničenja | nessuna limitazione | bez ierobežojumiem | Apribojimų nėra
LIM | limitation | Ограничение | Limitación | omezení | Begrænset | Behinderung | piirang | Περιορισμός | limitation | Ograničenje | limitazione | ierobežojums | Apribojimai
NON | no navigation allowed | Преустановено корабоплаване | Navegación prohibida | zákaz plavby | Sejlads ikke tilladt | gesperrt | navigatsioon keelatud | Δεν επιτρέπεται καμία ναυσιπλοΐα | navigation interdite | Plovidba nije dopuštena | nessuna navigazione consentita | kuģošana aizliegta | Laivyba draudžiama
CODUL STĂRII GHEȚII
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
NOL | nincs korlátozás | ebda restrizzjoni | Geen beperking | brak ograniczeń | Sem restrições | fără restricții | bez obmedzenia | brez omejitve | ei rajoitusta | Ingen begränsning | без ограничений | Без ограничења
LIM | korlátozás | restrizzjoni | Beperking | ograniczenie | Restrições | cu restricții | obmedzenie | omejitev | rajoitus | Begränsad trafk | ограниченно | Ограничење
NON | hajózás nem megengedett | navigazzjoni projbita | Vaarverbod | zakaz żeglugi | Navegação proibida | navigația nu este permisă | zákaz plavby | plovba prepovedana | alusliikenne ei ole sallittua | Ingen sjöfart tillåten | навигация запрещена | Пловидба није дозвољена
CODUL CLASEI METEO
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
CLR | clear | Ясно | Despejado | jasno | Klart | klar | selge | Αίθριος καιρός | clair | Vedro | sereno | skaidrs | giedra
CLDY | cloudy | Облачно | Nublado | oblačno | Skyet | bewölkt | pilvitus | Νεφώσεις | nuageux | Oblačno | nuvoloso | mākoņains | debesuota
OCST | overcast | Заоблачено | Cubierto | zataženo | Overskyet | bedeckt | lauspilvitus | Πλήρως νεφοσκεπής ουρανός | couvert | Jača naoblaka | coperto | apmācies | apsiniaukę
DZZL | drizzle | Ръмеж | Llovizna | mrholení | Støvregn | Nieselregen | uduvihm | Ψεκάδες βροχής | bruine | Rosa | pioviggine | smalks lietus | dulksna
RAIN | rain | Дъжд | Lluvia | déšť | Regn | Regen | vihm | Βροχή | pluie | Kiša | pioggia | lietus | lietus
LRAIN | light rain | Лек дъжд | Lluvia ligera | slabý déšť | Let regn | leichter Regen | kerge vihm | Ασθενής βροχή | légère pluie | Slaba kiša | pioggia debole | viegls lietus | silpnas lietus
ORAIN | occasional rain | Откъслечни превалявания | Lluvia ocasional | občasný déšť | Lejlighedsvis regn | gelegentlich Regen | hoovihm | Σποραδική βροχή | pluie intermittente | Povremena kiša | piogge occasionali | neregulārs lietus | nepastovus lietus
HRAIN | heavy rain | Силен дъжд | Lluvia intensa | silný déšť | Kraftig regn | schwerer Regen | paduvihm | Έντονη βροχόπτωση | forte pluie | Jaka kiša | forti piogge | spēcīgs lietus | smarkus lietus
SLEET | sleet | Лапавица | Aguanieve | déšť se sněhem | Tøsne | Graupel | lörts | Χιονόνερο | neige fondue | Susnježica | nevischio | slapjdraņķis | šlapdriba
SNOW | snow | Сняг | Nieve | sněžení | Sne | Schneefall | lumi | Χιόνι | neige | Snježne oborine | neve | sniegs | snygis
SNFALL | heavy snow fall | Силен снеговалеж | Nieve intensa | silné sněžení | Kraftigt snefald | schwerer Schneefall | tugev lumesadu | Έντονη χιονόπτωση | neige dense | Jake snježne oborine | pesanti nevicate | spēcīgs sniegs | stiprus snygis
HAIL | hail | Град | Granizo | krupobití | Hagl | Hagel | rahe | Χαλάζι | grêle | Tuča | grandine | krusa | kruša
SHWRS | showers | Преваляване | Chubasco | přeháňky | Byer | Schauer | sajuhood | Όμβρος | averses | Pljusak | rovesci | lietusgāzes | liūtys
THSTRM | thunderstorm | Гръмотевична буря | Tormenta eléctrica | bouřka | Tordenvejr | Gewitter | äike | Καταιγίδα | orage | Olujno nevrijeme | temporale | pērkona negaiss | perkūnija
HAZY | hazy | Замъглено | Bruma | zamlženo | Diset | diesig | somp | Υγρή αχλύς | brume | Maglovito | cielo velato | dūmaka | migla
FOG | fog | Мъгла | Niebla | mlha | Tåge | Nebel | udu | Ομίχλη | brouillard | Magla | nebbia | migla | rūkas
FOGPAT | fog patches | Мъгливи участъци | Zonas de niebla | lokální mlha | Pletvis tåge | Nebelbänke | udulaigud | Ομίχλη κατά τόπους | bancs de brouillard | Mjestimična magla | banchi di nebbia | miglas joslas | vietomis rūkas
GALE | gale | Силен вятър | Temporal | vichřice | Hård kuling | stürmischer Wind | raju | Θυελλώδης άνεμος | grand vent | Udari vjetra | burrasca | vētrains | audra
STRM | storm | Буря | Tormenta | bouře | Storm | Sturm | torm | Θύελλα | tempête | Oluja | tempesta | stipra vētra | štormas
HURRC | hurricane | Ураган | Huracán | hurikán | Orkan | Orkan | orkaan | Κυκλώνας | ouragan | Orkan | uragano | orkāns | uraganas
FZRA | freezing rain (black ice) | Суграшица | Lluvia escarchada (hielo glaseado) | mrznoucí déšť | Isslag | gefrierender Regen | allajahtunud vihm (must jää) | Βροχή με παγοκρυστάλλους (υαλόπαγος) | pluie verglaçante | Ledena kiša | vetrone | atkala (melnais ledus) | lijundra (apšalas)
CODUL CLASEI METEO
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
CLR | tiszta | ċar | Helder | bezchmurnie | Céu limpo | senin | bezoblačno (jasno) | jasno | selkeää | Klart | ясно | Ведро
CLDY | felhős | imsaħħab | Bewolkt | pochmurnie | Céu nublado | noros | oblačno | pretežno oblačno | enimmäkseen pilvistä | Molnigt | облачно | Облачно
OCST | borult | mgħajjeb bis-sħab | Betrokken | zachmurzenie | Céu encoberto | acoperit | zamračené | oblačno | pilvistä | Mulet | пасмурно | Наоблачење
DZZL | szitáló eső | irxiex | Motregen | mżawka | Chuvisco | burniță | mrholenie | pršenje | tihkusadetta | Duggregn | изморозь | Роса
RAIN | eső | xita | Regen | deszcz | Chuva | ploaie | dážď | dež | sadetta | Regn | дождь | Киша
LRAIN | gyenge eső | xita ħafifa | Lichte regen | lekki deszcz | Chuva fraca | ploaie ușoară | slabý dážď | rahel dež | heikkoa vesisadetta | Lätt regn | слабый дождь | Слаба киша
ORAIN | szórványos eső | kultant xita | Verspreide regen | sporadyczny deszcz | Chuvas ocasionais | ploaie ocazională | občasný dážď | občasen dež | ajoittaista vesisadetta | Tidvis regn | возможен дождь | Повремена киша
HRAIN | heves eső | xita qalila | Zware regenval | ulewa | Chuva forte | averse de ploaie | silný dážď | močan dež | voimakasta vesisadetta | Kraftigt regn | сильный дождь | Јака киша
SLEET | hódara | taħlita ta’ xita u silġ | Natte sneeuw | deszcz ze śniegiem | Neve molhada | lapoviță | dážď so snehom | leden dež | räntäsadetta | Snöblandat regn | дождь со снегом | Суснежица
SNOW | hó | borra | Sneeuw | śnieg | Neve | ninsoare | sneh (sneženie) | sneg | lumisadetta | Snö | снег | Снег
SNFALL | erős hóesés | borra qalila | Zware sneeuwval | intensywny opad śniegu | Forte nevão | averse de ninsoare | silné sneženie | močno sneženje | runsasta lumisadetta | Kraftigt snöfall | сильный снегопад | Јаке снежне падавине
HAIL | jégeső | xita balal | Hagel | grad | Granizo | grindină | krupobitie | toča | rakeita | Hagel | град | Град
SHWRS | zápor | ħalbiet tax-xita | Buien | przelotny opad śniegu | Aguaceiros | averse | prehánky | plohe | sadekuuroja | Regnskurar | ливни | Пљусак
THSTRM | zivatar | maltempata bir-ragħad | Onweer | burza (z piorunami) | Trovoada | vijelie | silná búrka | nevihta | raju ukonilma | Åskväder | гроза | Олујно невреме
HAZY | párás | imċajpar | Nevelig | mglisto | Bruma | negură | hmlisto | megličasto | auerta | Disigt | дымка | Магловито
FOG | köd | ċpar | Mist | mgła | Nevoeiro | ceață | hmla | megla | sumua | Dimma | туман | Магла
FOGPAT | ködfoltok | irqajja’ mċajprin | Mistbanken | lokalne zamglenie | Banco de nevoeiro | ceață în valuri | občasná hmla | zaplate megle | paikoitellen sumua | Dimbankar | туман местами | Местимична магла
GALE | viharos szél | burraxka | Harde wind | wichura | Vento muito forte | vânt puternic | víchrica | viharni veter | kovaa tuulta | Hård vind | штормовой ветер | Јак ветар
STRM | vihar | maltempata | Storm | burza | Tempestade | furtună | búrka | močan vihar | myrskyä | Storm | шторм | Олуја
HURRC | orkán | uragan | Orkaan | huragan | Furacão | tornadă | hurikán | orkan | hirmumyrskyä | Orkan | ураган | Оркан
FZRA | fagyos eső | xita ffriżata (“black ice”) | IJsregen (zwart ijs) | marznący deszcz | Chuva gelada (geada transparente) | polei | mrznúci dážď | žled (poledica) | jäätävää sadetta (mustaa jäätä) | Underkylt regn | гололед | Ледена киша
CODUL ELEMENTELOR METEOROLOGICE
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
WI | wind | Вятър | Viento | vítr | Vind | Wind | tuul | Άνεμος | vent | Vjetar | vento | vējš | vėjas
WA | waves | Вълнение | Oleaje | vlny | Bølger | Wellen | lained | Κύματα | remous | Valovi | moto ondoso | viļņi | bangos
FG | visibility | Видимост | Visibilidad | dohlednost | Sigtbarhed | Sicht | nähtavus | Ορατότητα | visibilité | Vidljivost | visibilità | redzamība | matomumas
RN | rain | Дъжд | Lluvia | déšť | Regn | Regen | vihm | Βροχή | pluie | Kiša | pioggia | lietus | lietus
SN | snow | Сняг | Nieve | sníh (sněžení) | Sne | Schnee | lumi | Χιόνι | neige | Snijeg | neve | sniegs | snygis
AT | air temperature | Температура на въздуха | Temperatura del aire | teplota vzduchu | Lufttemperatur | Lufttemperatur | õhutemperatuur | Θερμοκρασία αέρα | température de l'air | Temperatura zraka | temperatura dell'aria | gaisa temperatūra | oro temperatūra
WT | water temperature | Температура на водата | Temperatura del agua | teplota vody | Vandtemperatur | Wassertemperatur | veetemperatuur | Θερμοκρασία νερού | température de l'eau | Temperatura vode | temperatura dell'acqua | ūdens temperatūra | vandens temperatūra
CODUL ELEMENTELOR METEOROLOGICE
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
WI | szél | riħ | Wind | wiatr | Vento | vânt | vietor | veter | tuuli | Vind | ветер | Ветар
WA | hullámok | mewġ | Golven | fale | Ondas | valuri | vlny | valovi | aallokko | Vågor | высота волн | Таласи
FG | látótávolság | viżibbiltà | Zicht | mgła | Visibilidade | vizibilitate | viditeľnosť | vidljivost | näkyvyys | Sikt | видимость | видљивост
RN | eső | xita | Regen | deszcz | Chuva | ploaie | dážď | dež | sade | Regn | дождь | Киша
SN | hó | borra | Sneeuw | śnieg | Neve | zăpadă | sneženie | sneg | lumi | Snö | снег | Снег
AT | léghőmérséklet | temperatura tal-arja | Luchttemperatuur | temperatura powietrza | Temperatura do ar | temperatura aerului | teplota vzduchu | temperatura zraka | ilman lämpötila | Lufttemperatur | температура воздуха | Температура ваздуха
WT | vízhőmérséklet | temperatura tal-ilma | Watertemperatuur | temperatura wody | Temperatura da água | temperatura apei | teplota vody | temperatura vode | veden lämpötila | Vattentemperatur | температура воды | Температура воде
CODUL CATEGORIILOR METEO
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
0 | calm | безветрие | Calma | bezvětří | Roligt | Windstille | tuulevaikus | Νηνεμία | calme | Mirno | calma | bezvējš | štilis
1 | light air | тих вятър | Ventolina | vánek | Let vind | leichter Zug | vaikne tuul | Ασθενής άνεμος | courant d'air | Lahor | bava di vento | vēja vēsma | tylus vėjelis
2 | light breeze | лек ветрец | Brisa muy débil | slabý vítr | Let brise | leichte Briese | kerge tuul | Ελαφρά αύρα | brise légère | Povjetarac | brezza leggera | viegls vējš | lengvas vėjas
3 | gentle breeze | лек вятър | Brisa débil | mírný vítr | Blid brise | schwache Briese | nõrk tuul | Ασθενής αύρα | brise douce | Slab vjetar | brezza | lēns vējš | silpnas vėjas
4 | moderate breeze | умерен вятър | Brisa moderada | dosti čerstvý vítr | Moderat brise | mäßige Briese | mõõdukas tuul | Μέτρια αύρα | brise modérée | Umjeren vjetar | brezza vivace | mērens vējš | vidutinis vėjas
5 | fresh breeze | разхлаждащ вятър | Brisa fresca | čerstvý vítr | Frisk brise | frische Briese | kaunis tugev tuul | Δροσερή αύρα | brise fraîche | Umjereno jak vjetar | brezza tesa | mēreni stiprs vējš | gaivus vėjas
6 | strong breeze | силен вятър | Brisa fuerte | silný vítr | Kraftig brise | starker Wind | tugev tuul | Ισχυρή αύρα | vent fort | Jak vjetar | vento fresco | stiprs vējš | stiprus vėjas
7 | near gale | доста силен вятър | Viento fuerte | mírný vichr (prudký vítr) | Tæt på hård kuling | steifer Wind | vali tuul | Σχεδόν θυελλώδης άνεμος | tempête modérée | Snažan vjetar | vento forte | ļoti stiprs vējš | beveik audra
8 | gale | много силен вятър | Temporal | bouřlivý vítr | Hård kuling | stürmischer Wind | väga vali tuul | Θυελλώδης άνεμος | tempête fraîche | Olujni vjetar | burrasca moderata | vētrains | audra
9 | strong gale | силен вихър | Gran temporal | vichřice | Hård kuling | Sturm | rajutuul | Ισχυρός θυελλώδης άνεμος | tempête forte | Jak olujni vjetar | burrasca forte | vētra | stipri audra
10 | storm | много силен вихър | Tormenta | silná vichřice | Storm | schwerer Sturm | torm | Θύελλα | tempête | Orkanski vjetar | tempesta | stipra vētra | štormas
11 | violent storm | стихийна буря | Borrasca | mohutná vichřice | Meget kraftig storm | orkanartiger Sturm | tugev torm | Σφοδρή θύελλα | orage | Jak orkanski vjetar | fortunale | ļoti stipra vētra | stiprus štormas
12 | hurricane | ураган | Huracán | orkán | Orkan | Orkan | orkaan | Κυκλώνας | ouragan | Orkan | uragano | orkāns | uraganas
13 | thick fog | много гъста мъгла | Niebla espesa | velmi hustá mlha | Tyk tåge | dichter Nebel | tihe udu | Πυκνή ομίχλη | brouillard épais | Izrazito gusta magla | nebbia fitta | spēcīga migla | tirštas rūkas
14 | dense fog | гъста мъгла | Niebla densa | hustá mlha | Tæt tåge | dichter Nebel | väga tihe udu | Πυκνή ομίχλη | brouillard dense | Gusta magla | nebbia densa | bieza migla | stiprus rūkas
15 | moderate fog | умерена мъгла | Niebla moderada | mírná mlha | Moderat tåge | mäßiger Nebel | mõõdukas udu | Μέτρια ομίχλη | brouillard modéré | Umjerena magla | nebbia moderata | mērena migla | vidutinis rūkas
16 | fog | слаба мъгла | Niebla | mlha | Tåge | Nebel | udu | Ομίχλη | brouillard | Magla | nebbia | migla | rūkas
17 | mist | мъгла от изпарение | Neblina | kouřmo | Dis | Nebel | hägu | Υγρά αχλύς | brouillard léger | Sumaglica | nebbia leggera | viegla migla | migla
18 | haze | замъглено | Bruma | zákal | Tågedis | Dunst | somp | Ξηρά αχλύς | brume | Izmaglica | foschia | dūmaka | rūkana
19 | light haze | леко замъглено | Bruma ligera | slabý zákal | Let tågedis | leichter Dunst | kerge somp | Ελαφρά ξηρά αχλύς | brume légère | Blaga izmaglica | foschia leggera | viegla dūmaka | lengva rūkana
20 | clear | чисто | Despejado | průzračný vzduch | Klart | klar | selge | Αίθριος καιρός | clair | Vedro | sereno | skaidrs | giedra
21 | very clear | много чисто | Muy despejado | velmi průzračný vzduch | Meget klart | sehr klar | väga selge | Πολύ αίθριος καιρός | très clair | Vrlo vedro | molto sereno | ļoti skaidrs | labai giedra
22 | no fog | липса на мъгла | Sin niebla | bez mlhy | Ingen tåge | kein Nebel | udutu | Απουσία ομίχλης | pas de brouillard | Bez magle | assenza di nebbia | nav miglas | rūko nėra
CODUL CATEGORIILOR METEO
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
0 | szélcsend | kalm | Stil | cisza | Calmo | calm | bezvetrie | brezvetrje | tyyntä | Lugnt | штиль (безветрие) | тихо
1 | gyenge szellő, fuvallat | arja ħafifa | Flauw en stil | powiew | Aragem | vânt perceptibil | vánok | sapica | pientä tuulenvirettä | Svag vind | тихий ветер | лахор
2 | enyhe szél | żiffa ħafifa | Flauwe koelte | słaby wiatr | Brisa ligeira | briză ușoară | slabý vietor | vetrič | heikkoa tuulta | Svag vind | легкий ветер | поветарац
3 | gyenge szél | żiffa ħelwa | Lichte koelte | łagodny wiatr | Pequena brisa | briză slabă | mierny vietor | šibek veter | kohtalaista tuulta | Måttlig vind | слабый ветер | слаб ветар
4 | mérsékelt szél | żiffa moderata | Matige koelte | umiarkowany wiatr | Brisa moderada | briză moderată | dosť čerstvý vietor | zmeren veter | navakkaa tuulta | Måttlig vind | умеренный ветер | умерен ветар
5 | élénk szél | żiffa friska | Frisse bries | dość silny wiatr | Brisa fresca | briză semnificativă | čerstvý vietor | zmerno močan veter | kovaa tuulta | Frisk vind | свежий ветер | умерено јак ветар
6 | erős szél | żiffa qawwija | Stijve bries | silny wiatr | Vento fresco | briză puternică | silný vietor | močan veter | myrskyä | Frisk vind | сильный ветер | јак ветар
7 | viharos szél | kważi burraxka | Harde wind | bardzo silny wiatr | Vento forte | vânt puternic | prudký vietor | zelo močan veter | navakkaa tuulta (near gale) | Hård vind | крепкий ветер | бура
8 | élénk viharos szél, vihar | burraxka | Stormachtig | sztorm/ wicher | Vento muito forte | vânt foarte puternic | búrlivý vietor | viharni veter | kovaa tuulta (gale) | Hård vind | очень крепкий ветер | средња бура
9 | heves vihar | burraxka qalila | Storm | silny sztorm | Vento tempestuoso | furtună | víchrica | vihar | erittäin kovaa tuulta (strong gale) | Mycket hård vind | шторм | јака бура
10 | dühöngő vihar, szélvész | maltempata | Zware storm | bardzo silny sztorm | Tempestade | furtună puternică | silná víchrica | močan vihar | myrskyä (storm) | Storm | сильный шторм | жестока бура
11 | heves szélvész | maltempata qalila | Zeer zware storm | gwałtowny sztorm | Tempestade violenta | furtună violentă | mohutná víchrica | orkanski veter | ankaraa myrskyä (violent storm) | Svår storm | жестокий шторм | жестока олуја
12 | orkán | uragan | Orkaan | huragan | Furacão | uragan | orkán | orkan | hirmumyrskyä (hurricane) | Orkan | ураган | ураган
13 | sürű köd | ċpar oħxon | Zeer dichte mist | gęsta mgła | Nevoeiro cerrado | ceață groasă | veľmi silná hmla | zelo gosta megla | hyvin sakeaa sumua | Tjocka | сильный туман | веома густа магла
14 | tartós köd, 6 órát meghaladja | ċpar dens | Dichte mist | bardzo gęsta mgła | Nevoeiro denso | ceață densă | silná hmla | gosta megla | sakeaa sumua | Tät dimma | плотный (густой) туман | густа магла
15 | enyhe köd | ċpar moderat | Matige mist | lekka mgła | Nevoeiro moderado | ceață moderată | mierna hmla | zmerna megla | kohtalaista sumua | Måttlig dimma | умеренный туман | умерена магла
16 | köd | ċpar | Mist (zichtbaarheid < 1000 m) | mgła | Nevoeiro | ceață | hmla | megla | heikkoa sumua | Dimma | туман | магла
17 | párásság | raxx | Mist (zichtbaarheid > 1000 m) | mgiełka | Neblina | pâclă | dymno | meglica | utua | Lätt dimma | дымка | измаглица
18 | homály | imċajpar | Nevel | przymglenie | Bruma | negură | zákal | suha motnost | auerta | Dis | мгла | сумаглица
19 | száraz légköri homály | ftit imċajpar | Lichte nevel | lekkie przymglenie | Bruma ligeira | ceață subțire | slabý zákal | rahla suha motnost | kevyttä auerta | Lätt dis | легкая мгла | блага сумаглица
20 | tiszta | ċar | Helder | przejrzyście | Limpo | senin | jasno | jasno | selkeää | Klart | ясно | ведро
21 | teljes látás | ċar ħafna | Zeer helder | bardzo przejrzyście | Muito limpo | foarte senin | veľmi jasno | zelo jasno | hyvin selkeää | Helt klart | очень ясно | веома ведро
22 | ködmentes | ebda ċpar | Geen mist | brak mgły | Sem nevoeiro | fără ceață | bez hmly | brez megle | ei sumua | Ingen dimma | нет тумана | без магле
CODUL DIRECȚIILOR METEO
Valoare | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
N | north | Северно | Norte | severně | Nord | Nord | põhi | Βόρεια | Nord | Sjeverno | nord | Uz ziemeļiem | šiaurė
NE | north-east | Североизточно | Noreste | severo-východně | Nordøst | Nord-Ost | kirre | Βορειοανατολικά | Nord-est | Sjeveroistočno | nord-est | Uz ziemeļaustrumiem | šiaurės rytai
E | east | Източно | Este | východně | Øst | Ost | ida | Ανατολικά | Est | Istočno | est | Uz austrumiem | rytai
SE | south-east | Югоизточно | Sureste | jiho-východně | Sydøst | Süd-Ost | kagu | Νοτιοανατολικά | Sud-est | Jugoistočno | sud-est | Uz dienvidaustrumiem | pietryčiai
S | south | Южно | Sur | jižně | Syd | Süd | lõuna | Νότια | Sud | Južno | sud | Uz dienvidiem | pietūs
SW | south-west | Югозападно | Suroeste | jiho-západně | Sydvest | Süd-West | edel | Νοτιοδυτικά | Sud-ouest | Jugozapadno | sud-ovest | Uz dienvidrietumiem | pietvakariai
W | west | Западно | Oeste | západně | Vest | West | lääs | Δυτικά | Ouest | Zapadno | ovest | Uz rietumiem | vakarai
NW | north-west | Северозападно | Noroeste | severo-západně | Nordvest | Nord-West | loe | Βορειοδυτικά | Nord-ouest | Sjeverozapadno | nord-ovest | UZ ziemeļrietumiem | šiaurės vakarai
WRB | variable | Променлив | Variable | proměnlivě | Variabel | veränderlich | muutlik | Μεταβλητός | variable | Promjenjivo | variabile | Mainīgi | nepastovi
CODUL DIRECȚIILOR METEO
Valoare | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
N | észak | it-Tramuntana | Noord | północ | Norte | nord | severne | severni | Pohjoinen | Nord | северный | Север
NE | észak-kelet | il-Grigal | Noordoost | północny wschód | Nordeste | nord-est | severo-východne | severovzhodni | Koillinen | Nordost | северо-восточный | Североисток
E | kelet | il-Lvant | Oost | wschód | Leste | est | východne | vzhodni | Itä | Öst | восточный | Исток
SE | dél-kelet | ix-Xlokk | Zuidoost | południowy wschód | Sudeste | sud-est | juho-východne | jugovzhodni | Kaakko | Sydost | юго-восточный | Југоисток
S | dél | in-Nofsinhar | Zuid | południe | Sul | sud | južne | južni | Etelä | Syd | южный | Југ
SW | dél-nyugat | il-Lbiċ | Zuidwest | południowy zachód | Sudoeste | sud-vest | juho-západne | jugozahodni | Lounas | Sydväst | юго-западный | Југозапад
W | nyugat | il-Punent | West | zachód | Oeste | vest | západne | zahodni | Länsi | Väst | западный | Запад
NW | észak-nyugat | il-Majjistral | Noordwest | północny zachód | Noroeste | nord-vest | severo-západne | severozahodni | Luode | Nordväst | северо-западный | Северозапад
WRB | változó | varjabbli | Veranderlijk | zmienny | Variável | variabil | premenlivo | spremenljiv | vaihtelee | Växlande | Переменный | променљив
ETICHETE GUI
Eticheta XML | EN | BG | ES | CS | DA | DE | ET | EL | FR | HR | IT | LV | LT
area | area | Район | Área | Oblast | Område | Gebiet | piirkond | Ζώνη | zone | Područje | area | Apgabals | sritis
button_back | Back | Назад | Retroceder | Zpět | Tilbage | Zurück | Tagasi | Επιστροφή | Retour | Natrag | indietro | Atpakaļ | Atgal
button_cancel | Cancel | Отказ | Cancelar | Zrušit | Annullér | Abbrechen | Katkesta | Ακύρωση | Annuler | Odustani | annulla | Atcelt | Atšaukti
button_new_search | New search | Ново търсене | Nueva búsqueda | Nové hledání | Ny søgning | Neue Suche | Uus otsing | Νέα έρευνα | nouvelle recherche | Nova pretraga | nuova ricerca | Jauns meklēšanas vaicājums | Nauja paieška
button_register | Register | Регистриране | Registrarse | Registrovat | Registrér | Registrieren | Registreeri | Εγγραφή | S'enregistrer | Registracija | registrare | Reģistrēt | Registruotis
button_save | Save | Запазване | Guardar | Uložit | Gem | Speichern | Salvesta | Αποθήκευση | Sauvegarder | Spremi | salvare | Saglabāt | Išsaugoti
button_search | Search | Търсене | Buscar | Hledat | Søg | Suchen | Otsi | Αναζήτηση | Rechercher | Traži | ricerca | Meklēt | Paieška
button_view | View | Преглед | Visualizar | Zobrazit | Vis | Anzeigen | Vaata | Προβολή | Voir | Pregled | visualizzare | Skatīt | Rodyti
email_address | E-mail address | Адрес на ел. поща | Correo electrónico | E-mailová adresa | E-mailadresse | E-Mail Adresse | E-posti aadress | Διεύθυνση ηλεκτρονικού ταχυδρομείου | Adresse email | Adresa e-pošte | indirizzo e-mail | E-pasta adrese | E. pašto adresas
email_service | e-mail service | E-mail услуга | Servicio de correo electrónico | E-mailová služba | E-mailtjeneste | E-Mail Service | E-posti teenus | Υπηρεσία ηλεκτρονικού ταχυδρομείου | Service email | Usluga elektronske pošte | servizio e-mail | E-pasta pakalpojums | e. | pašto paslauga
email_service_register | Registration e-mail service | Регистриране за E-mail услуга | Registrarse servicio de correo electrónico | Registrace e-mailové služby | Registrering af E-mailtjeneste | Registrierung E-Mail-Service | Registreerimise e-posti teenus | Εγγραφή σε υπηρεσία ηλεκτρονικού ταχυδρομείου | Enregistrement service email | Registracija usluge elektronske pošte | registrare servizio e-mail | Reģistrācijas e-pasta pakalpojums | Registracijos e. pašto paslauga
error_validation | Validation error: | Грешка при валидиране | Error de validación: | Chyba ověření: | Validation error: | Fehler bei der Validierung: | Valideerimise viga: | Σφάλμα επικύρωσης | Erreur de validation: | Pogreška pri provjeri valjanosti: | errore di convalida: | Validācijas kļūda: | Atlikus patikrą aptikta klaida:
format_code | Code | Кодов формат | Código | Kód | Kode | Code | Kood | Κωδικός | Code | Kod | codice | Kods | Kodas
format_pdf | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF
format_select | Select format | Избиране на формат | Seleccionar formato | Vyberte formát | Vælg format | Format wählen | Vali vorming | Επιλογή μορφοτύπου | Sélectionner le format | Odaberite format | seleziona formato | Atlasīt formātu | Pasirinkti formatą
format_text | Full text | Пълен текст | Texto íntegro | Textová zpráva | Fuld tekst | Volltext | Terviktekst | Πλήρες κείμενο | Message intégral | Puni tekst | full-text | Pilns teksts | Visas tekstas
format_xml | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML
gauge | gauge | Водомерна станция | Gálibo | Vodočet | Profil | Pegel | Mõõtur | Αισθητήρας | capteur | Vodomjerna postaja | misuratore | Mērinstruments | Vandens lygio matavimo punktas
ID | ID | Идентификация | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID
km_from | River km from | Речен км. от | Km de río desde | Říční km od | Flod km fra | Stromkilometer von | Jõe km alates | Χιλιόμετρα από | Kilomètres depuis | Riječni km od | km di fiume da | Upes km no | Upės km nuo
km_to | River km to | Речен км. до | Km de río hasta | Říční km do | Flod km til | Stromkilometer bis | Jõe km kuni | Χιλιόμετρα έως | Kilomètres jusqu'a | Riječni km do | km di fiume fino a | Upes km līdz | Upės km iki
language | Language | Език | Lengua | Jazyk | Sprog | Sprache | Keel | Γλώσσα | Langue | Jezik | lingua | Valoda | Kalba
language_select | English | Български | Inglés | Česky | Engelsk | Deutsch | Eesti | Ελληνική | Français | Hrvatski | italiano | Angļu | Anglų
message_search | Search notices | Търсене на съобщения | Buscar avisos | Vyhledat zprávy | Søgemeddelelser | Nachrichtenabfrage | Otsi teadetest | Αναζήτηση ανακοίνωσης | Chercher avis | Pretraži obavijesti | ricerca avvisi | Meklēt paziņojumus | Pranešimų paieška
message_type | Message type | Тип на съобщението | Tipo de mensaje | Typ zprávy | Meddelelsestype | Nachrichtentyp | Teate liik | Τύπος μηνύματος | Type de message | Vrsta poruke | tipo di messaggio | Ziņojuma veids | Pranešimo tipas
nts | Notices to skippers | Известие до корабните водачи | Avisos a los navegantes | Zprávy vůdcům plavidel | Efterretninger for skippere | Nachrichten für die Binnenschifffahrt | Kipritele edastatavad teated | Ανακοινώσεις προς πλοιάρχους | Avis à la batellerie | Priopćenja brodarstvu | avvisi ai naviganti | Paziņojumi kapteiņiem | Pranešimai kapitonams
password | Password | Парола | Contraseña | Heslo | Adgangskode | Passwort | Salasõna | Κωδικός πρόσβασης | Mot de passe | Lozinka | password | Parole | Slaptažodis
password_repeat | Repeat password | Повторете паролата | Repetir contraseña | Zopakovat heslo | Gentag adgangskode | Passwort wiederholen | Korda salasõna | Επανάληψη κωδικού πρόσβασης | Répéter mot de passe. | Potvrda lozinke | ripeti password | Parole vēlreiz | Pakartokite slaptažodį
title | Title | Заглавие | Título | Název | Titel | Titel | Tiitel | Τίτλος | Titre | Naslov | titolo | Nosaukums | Pavadinimas
user_account_management | Manage user account | Управление на акаунта | Gestionar cuenta de usuario | Spravovat uživatelský účet | Forvaltning af brugerkonto | Benutzerkonto verwalten | Kasutajakonto haldamine | Διαχείριση λογαριασμού χρήστη | Gérer votre compte | Upravljanje korisničkim računom | gestisci account utente | Pārvaldīt lietotāja kontu | Tvarkyti vartotojo paskyrą
valid_from | Valid from | Валиден от | Válido desde | Platné od | Gyldig fra | Gültig von | Kehtiv alates | Ισχύει από | Valide à partir de | Važeće od | valido da | Derīgs no | Galioja nuo
valid_till | Valid till | Валиден до | Válido hasta | Platné do | Gyldig til | Gültig bis | Kehtiv kuni | Ισχύει έως | Valide jusqu'à | Važeće do | valido fino a | Derīgs līdz | Galioja iki
waterway | Waterway | Воден път | Vía navegable | Vodní cesta | Vandvej | Wasserstraße | Veetee | Πλωτή οδός | Voie d’eau | Vodni put | via navigabile | Ūdensceļš | Vandens kelias
Waterway_section | Waterway section | Участък от водния път | Tramo de vía navegable | Úsek vodní cesty | Vandvejsstrækning | Wasserstraßenabschnitt | Veetee osa | Τμήμα πλωτής οδού | Section de voie d'eau | Dionica vodnog puta | sezione di via navigabile | Ūdensceļa posms | Vandens kelio ruožas
ETICHETE GUI
Eticheta XML | HU | MT | NL | PL | PT | RO | SK | SL | FI | SV | RU | SR
area | terület | żona | Gebied | obszar | Superfície | zonă | Oblasť | območje | alue | Område | Область | Област
button_back | Vissza | Lura | Terug | Cofnij | Recuar | Înapoi | Späť | nazaj | takaisin | Tillbaka | Назад | Назад
button_cancel | Mégsem | Ikkanċella | Annuleren | Anuluj | Cancelar | Anulează | Zrušiť | prekliči | peruuta | Avbryt | Отменить | Откажи
button_new_search | Új keresés | Tfittxija ġdida | Nieuwe zoekopdracht | Nowe wyszukiwanie | Nova pesquisa | Căutare nouă | Nové hľadanie | novo iskanje | uusi haku | Ny sökning | Новый поиск | Нова претрага
button_register | Regisztráció | Irreġistra | Registreren | Zarejestruj | Registar | Înregistrare | Registrovať | registracija | Rekisteröidy | Registrera | Регистрация | Регистрација
button_save | Mentés | Issejvja | Opslaan | Zapisz | Guardar | Salvează | Uložiť | shrani | Tallenna | Spara | Сохранить | Снимити
button_search | Keresés | Fittex | Zoeken | Szukaj | Pesquisar | Căutare | Vyhľadať | iskanje | Hae | Sök | Поиск | Претрага
button_view | Megtekint | Ara | Bekijken | Pokaż | Visualizar | Vizualizare | Zobraziť | pogled | Katso | Visa | Просмотр | Преглед
email_address | Email cím | Indirizz tal-posta elettronika | E-mailadres | Adres e-mail | Endereço eletrónico | Adresa de e-mail | E-mailová adresa | e-poštni naslov | sähköpostiosoite | e-postadress | Адрес электронной почты | Електронска адреса
email_service | Email szolgáltatás | servizz tal-posta elettronika | E-maildienst | Usługa e-mail | Correio eletrónico | Serviciu e-mail | E-mailová služba | e-poštna storitev | sähköpostipalvelu | e-posttjänst | услуга электронной почты | Услуга електронске поште
email_service_register | Regisztráció az email-küldő szolgáltatásra | Reġistrazzjoni tas-servizz tal-posta elettronika | Registreren e-maildienst | Rejstracja do usługi e-mail | Registo correio eletrónico | Înregistrare pentru serviciu e-mail | Registrácia pre e-mailovú službu | storitev za registracijo e-poštnega naslova | Rekisteröidy sähköpostipalveluun | Registrering, e-posttjänst | Регистрация услуг электронной почты | Регистрација сервиса електронске поште
error_validation | Érvényesítési hiba | Żball fil-validazzjoni: | Validatiefout | Błąd walidacji | Erro de validação: | Eroare de validare: | Chyba validácie: | napaka pri potrjevanju | Validointivirhe: | Valideringsfel: | Ошибка валидации: | Грешка у провери:
format_code | Kód | Kodiċi | Code | Kod | Código | Cod | Kód | koda | Koodi | Kod | Код | Код
format_pdf | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF | PDF
format_select | Válasszon formátumot | Agħżel il-format | Formaat kiezen | Wybierz format | Selecionar formato | Selectați formatul | Vyberte formát | izberi format | Valitse formaatti | Välj format | Выберите формат | Изабери формат
format_text | Teljes szöveg | Test sħiħ | Volle tekst | Pełny tekst | Texto integral | Mesaj text integral | Textová správa | celotno besedilo | Kokoteksti | Fulltext | Полный текст сообщения | Цео текст
format_xml | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML | XML
gauge | mérce | kejl | Gauge | Wodowskaz | Gabarito | miră | Vodomerná stanica | merilnik | Vedenkorkeusmittari | Vattenståndsmätare | Водомерный пост | Водомерна станица
ID | Azonosító | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID | ID
km_from | Folyó-km-tól | Km tax-xmara minn | Rivier-km vanaf | km rzeki od | Km do rio a partir de | De la kilometrul | Riečny km od | rečni km od | Jokikilometrejä lähtöpaikasta | Från flodkilometer | От км | Речни километар од
km_to | Folyó km-ig | Km tax-xmara sa | Rivier-km tot | km rzeki od | Km do rio até | Până la kilometrul | Riečny km do | rečni km do | Jokikilometrejä kohteeseen | Till flodkilometer | До км | Речни километар до
language | Nyelv | Lingwa | Taal | Język | Língua | Limba | Jazyk | jezik | Kieli | Språk | язык | Језик
language_select | Magyar | Ingliż | Nederlands | polski | Inglês | Română | Slovensky | slovenščina | suomi | Svenska | Русский | српски
message_search | Hírlevelek keresése | Fittex avviżi | Berichten zoeken | Szukaj komunikatu | Pesquisar avisos | Caută avize | Vyhľadať správy | išči obvestila | Viestihaku | Sök meddelanden | Поиск извещения | Претрага Саопштења
message_type | Üzenettípus | Tip ta’ messaġġ | Berichttype | Typ wiadomości | Tipo de mensagem | Tip de mesaj | Typ správy | vrsta sporočila | Viestin laji | Typ av meddelande | Тип сообщения | Тип поруке
nts | Hajósoknak szóló információk | Avviżi lill-Kaptani | Berichten aan de scheepvaart | Komunikaty dla kapitanów | Avisos à navegação | Aviz către navigatori | Správy pre veliteľov lodí | obvestila kapitanom | Ilmoitukset kapteenille | Meddelanden till befälhavare | Извещения судоводителям | Саопштење бродарству
password | Jelszó | Password | Wachtwoord | Hasło | Senha | Parola | Heslo | geslo | Salasana | Lösenord | Пароль | Лозинка
password_repeat | Jelszó újra | Irripeti l-password | Wachtwoord herhalen | Powtórz hasło | Repetir senha | Reintroduceți parola | Zopakovať heslo | ponovno vpiši geslo | Toista salasana | Upprepa lösenord | Пожалуйста, повторите пароль. | Поновите лозинку
title | Cím | Titlu | Titel | Tytuł | Título | Titlu | Názov | naslov | Nimi | Titel | Название | Назив
user_account_management | Felhasználói számla kezelése | Immaniġġja l-kont tal-utent | Gebruikersaccount beheren | Zrządzaj kontem użytkownika | Gerir conta utilizador | Setează cont | Spravovať účet | upravljanje uporabniškega računa | Hallinnoi käyttäjätiliä | Hantera användarkonto | Управление аккаунтом | Управљање корисничким налогом
valid_from | Érvényesség kezdete | Validu minn | Geldig vanaf | Ważne od | Válido de | Valabil din | Platné od | veljavno od | Voimassa … alkaen | Giltigt från och med | Действует с | Важи од
valid_till | Érvényesség lejárata | Validu sa | Geldig tot | Ważne do | Válido até | Valabil până la | Platné do | veljavno do | Voimassa … asti | Giltigt till och med | действительна до | Важи до
waterway | Víziút | Passaġġ fuq l-ilma | Waterweg | Droga wodna | Via navegável | Numele căii navigabile | Vodná cesta | vodna pot | Vesiväylä | Vattenväg | Водный путь | Водни пут
Waterway_section | Víziút szakasz | Sezzjoni ta’ passaġġ fuq l-ilma | Waterwegsectie | Odcinek drogi wodnej | Troço via navegável | Secțiunea căii navigabile | Úsek vodnej cesty | odsek vodne poti | Vesiväylän osa | Avsnitt av vattenväg | Участок водного пути | Део водног пута
