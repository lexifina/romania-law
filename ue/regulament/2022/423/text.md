REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2022/423 AL COMISIEI
din 14 martie 2022
de stabilire a specificațiilor, a măsurilor și a altor cerințe tehnice necesare pentru implementarea sistemului informatic descentralizat menționat în Regulamentul (UE) 2020/1784 al Parlamentului European și al Consiliului
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) 2020/1784 al Parlamentului European și al Consiliului din 25 noiembrie 2020 privind notificarea sau comunicarea în statele membre a actelor judiciare și extrajudiciare în materie civilă sau comercială (notificarea sau comunicarea actelor) (1), în special articolul 25 alineatul (1),
întrucât:
(1) În vederea instituirii sistemului informatic descentralizat, este necesar să se definească și să se adopte specificații, măsuri și alte cerințe tehnice pentru implementarea sistemului respectiv.
(2) Au fost dezvoltate o serie de instrumente pentru schimbul digital de date legate de cauze, fără a se înlocui sistemele informatice deja existente în statele membre și fără a fi necesare modificări costisitoare ale respectivelor sisteme. Sistemul e-CODEX (e-Justice Communication via On-line Data Exchange) este principalul instrument de acest tip dezvoltat până în prezent.
(3) Sistemul informatic descentralizat ar trebui să fie alcătuit din sistemele back-end ale statelor membre și din puncte de acces interoperabile, prin intermediul cărora să fie interconectate sistemele respective. Punctele de acces ale sistemului informatic descentralizat ar trebui să se bazeze pe e-CODEX.
(4) Odată ce va fi elaborat sistemul informatic descentralizat, comitetul director va asigura funcționarea și întreținerea acestuia. Comitetul director ar trebui să fie instituit de Comisie printr-un act separat.
(5) Autoritatea Europeană pentru Protecția Datelor a fost consultată în conformitate cu articolul 42 alineatul (1) din Regulamentul (UE) 2018/1725 al Parlamentului European și al Consiliului (2) și a emis un aviz la 24 ianuarie 2022.
(6) Măsurile prevăzute de prezentul regulament sunt conforme cu avizul Comitetului pentru notificarea sau comunicarea în statele membre a actelor judiciare și extrajudiciare în materie civilă sau comercială,
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Specificații tehnice ale sistemului informatic descentralizat
Specificațiile, măsurile și celelalte cerințe tehnice necesare pentru implementarea sistemului informatic descentralizat menționat la articolul 25 din Regulamentul (UE) 2020/1784 sunt prevăzute în anexă.
Articolul 2
Intrare în vigoare
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în statele membre în conformitate cu tratatele.
Adoptat la Bruxelles, 14 martie 2022.
Pentru Comisie
Președintele
Ursula VON DER LEYEN
(1) JO L 405, 2.12.2020, p. 40.
(2) Regulamentul (UE) 2018/1725 al Parlamentului European și al Consiliului din 23 octombrie 2018 privind protecția persoanelor fizice în ceea ce privește prelucrarea datelor cu caracter personal de către instituțiile, organele, oficiile și agențiile Uniunii și privind libera circulație a acestor date și de abrogare a Regulamentului (CE) nr. 45/2001 și a Deciziei nr. 1247/2002/CE (JO L 295, 21.11.2018, p. 39).
ANEXĂ
Specificații, măsuri și alte cerințe tehnice ale sistemului informatic descentralizat menționat la articolul 1
1. Introducere
Sistemul de schimb pentru notificarea sau comunicarea actelor este un sistem informatic descentralizat bazat pe e-CODEX, care poate efectua schimburi de documente și de date legate de procesul de notificare sau comunicare a actelor între diferitele state membre în conformitate cu Regulamentul (UE) 2020/1784. Caracterul descentralizat al sistemului informatic ar permite schimbul de date exclusiv între state membre, fără ca vreuna dintre instituțiile Uniunii să fie implicată în respectivul schimb.
2. Definiții
| 2.1. | „protocoale de transport hipertext securizate” (HyperText Transport Protocol Secure) sau „HTTPS” înseamnă canale de comunicații criptate și de conectare securizată;
| 2.2. | „portal” înseamnă soluția de implementare de referință sau soluția de sistem back-end național conectată la sistemul informatic descentralizat;
| 2.3. | „nerepudierea originii” înseamnă măsurile care furnizează dovada integrității și a originii datelor prin metode precum certificarea digitală, infrastructura de chei publice și semnăturile digitale;
| 2.4. | „nerepudierea primirii informațiilor” înseamnă măsurile care îi furnizează emitentului dovada primirii informațiilor de către destinatarul preconizat prin metode precum certificarea digitală, infrastructura de chei publice și semnăturile digitale;
| 2.5. | „protocol simplu de acces la obiecte” (SOAP) înseamnă, în conformitate cu standardele consorțiului World Wide Web, o specificație a protocolului de mesagerie pentru schimbul de informații structurate cu privire la implementarea serviciilor web în rețelele informatice;
| 2.6. | „serviciu web” înseamnă un sistem software conceput pentru a sprijini interacțiunea interoperabilă între calculatoare în cadrul unei rețele; acesta are o interfață descrisă într-un format care poate fi prelucrat de un calculator;
| 2.7. | „schimb de date” înseamnă schimbul de mesaje și de documente prin intermediul sistemului informatic descentralizat.
3. Metode de comunicare prin mijloace electronice
În scopul schimbului de mesaje și de documente, sistemul de schimb pentru notificarea sau comunicarea actelor utilizează metode de comunicare bazate pe servicii, cum ar fi serviciile web sau alte infrastructuri de servicii digitale reutilizabile.
Mai precis, acesta va utiliza infrastructura e-CODEX, care este alcătuită din două componente principale: conectorul și dispozitivul poartă (gateway).
Conectorul asigură comunicarea cu soluția de implementare de referință sau cu implementările naționale. Acesta poate procesa schimbul de mesaje cu dispozitivul poartă în ambele direcții, poate urmări mesajele și le poate recunoaște utilizând standarde precum probele ETSI-REM, poate valida semnăturile documentelor comerciale, poate crea un token care să conțină rezultatul validării în format PDF și XML și poate crea un container utilizând standarde precum ASIC-S, în care conținutul comercial al unui mesaj este structurat și semnat.
Dispozitivul poartă este responsabil pentru schimbul de mesaje și este agnostic la conținutul mesajului. Acesta poate trimite mesaje către conector și poate primi mesaje de la acesta, poate valida informațiile din antet, poate identifica modul de prelucrare corect, poate semna și cripta mesajele și le poate transfera către alte dispozitive poartă.
4. Protocoale de comunicare
Sistemul de schimb pentru notificarea sau comunicarea actelor utilizează protocoale internet securizate, cum ar fi HTTPS pentru comunicarea dintre componentele portalului și ale sistemului informatic descentralizat, precum și protocoalele de comunicare standard, cum ar fi SOAP, pentru transmiterea de date și de metadate structurate.
În mod specific, e-CODEX asigură un grad ridicat de securitate a informațiilor, datorită beneficiilor oferite de procedura de autentificare de ultimă generație și de protocolul criptografic multistrat.
5. Standarde de securitate
În ceea ce privește comunicarea și difuzarea informațiilor prin intermediul sistemului de schimb pentru notificarea sau comunicarea actelor, printre măsurile tehnice de asigurare a standardelor minime de securitate informatică se numără:
(a) măsuri care să asigure confidențialitatea informațiilor, inclusiv prin utilizarea unor canale securizate (HTTPS);
(b) măsuri care să asigure integritatea datelor în momentul schimbului de date;
(c) măsuri care să asigure nerepudierea originii expeditorului informațiilor în cadrul sistemului de schimb pentru notificarea sau comunicarea actelor și nerepudierea primirii informațiilor;
(d) măsuri care să asigure păstrarea evidenței evenimentelor care ar putea compromite securitatea informațiilor, în conformitate cu recomandările internaționale recunoscute pentru standardele de securitate informatică;
(e) măsuri care să asigure autentificarea și autorizarea tuturor utilizatorilor înregistrați și măsuri care să vizeze verificarea identității sistemelor conectate la sistemul de schimb pentru notificarea sau comunicarea actelor;
(f) sistemul de schimb pentru notificarea sau comunicarea actelor va fi dezvoltat în conformitate cu principiul protecției datelor începând cu momentul conceperii și în mod implicit.
6. Disponibilitatea serviciilor
| 6.1. | Serviciul funcționează 24 de ore din 24, șapte zile din șapte, cu o rată de disponibilitate tehnică a sistemului de cel puțin 98 %, cu excepția operațiunilor de întreținere programate.
| 6.2. | Statele membre transmit Comisiei o notificare cu privire la activitățile de întreținere după cum urmează: (a) înainte cu cinci zile lucrătoare pentru operațiunile de întreținere care pot duce la o perioadă de indisponibilitate de până la patru ore; (b) înainte cu 10 zile lucrătoare pentru operațiunile de întreținere care pot duce la o perioadă de indisponibilitate de până la 12 ore; (c) înainte cu 30 de zile lucrătoare pentru operațiunile de întreținere care pot duce la o perioadă de indisponibilitate de până la șase zile pe an.
| 6.3. | În măsura în care este posibil, în zilele lucrătoare, operațiunile de întreținere trebuie să fie planificate în intervalul 20.00-7.00 CET.
| 6.4. | În cazul în care statele membre au stabilit intervale săptămânale pentru serviciul de întreținere, acestea informează Comisia cu privire la momentul și la ziua din săptămână în care sunt planificate aceste intervale săptămânale fixe. Fără a aduce atingere obligațiilor stabilite la punctul 6.2, în cazul în care sistemele statelor membre sunt indisponibile într-un astfel de interval fix, statele membre pot opta să nu notifice Comisia de fiecare dată.
| 6.5. | În cazul unor defecțiuni tehnice neașteptate ale sistemelor statelor membre, statele membre informează fără întârziere Comisia cu privire la indisponibilitatea sistemului lor, precizând și momentul reluării preconizate a serviciului, dacă acesta se cunoaște.
| 6.6. | În cazul unor defecțiuni neașteptate ale bazei de date a autorităților competente, Comisia informează fără întârziere statele membre cu privire la indisponibilitatea respectivă, precizând și momentul reluării preconizate a serviciului, dacă acesta se cunoaște.
