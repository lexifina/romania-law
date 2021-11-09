# Anexa nr. 3
Procedura și condițiile de transmitere a fișierului standard de control fiscal (SAF-T)
1.
Pentru pregătirea și transmiterea fișierului standard de control fiscal prin intermediul Declarației informative D406 se derulează următoarele activități: a) generarea fișierului SAF-T în format XML de către sistemul informatic al contribuabilului/plătitorului;
b) verificarea structurii fișierului XML și a corelațiilor dintre date prin programul informatic „Validator” pus la dispoziție de către Agenția Națională de Administrare Fiscală (ANAF);
c) generarea Declarației informative D406 ca document electronic în format PDF cu XML atașat (dacă acesta a îndeplinit condițiile de verificare) semnat electronic.
2.
Pentru pregătirea Declarației informative D406, ANAF pune la dispoziția contribuabilului/plătitorului două forme de asistență: a) specificațiile pentru formatul și conținutul Declarației informative D406;
b) programul „Validator” pentru fișierul SAF-T în format XML - program independent, în format executabil, interpretat, scris în limbaj Java, cu care contribuabilii/plătitorii pot valida sintactic și în parte semantic raportarea, înainte de a o încărca pe portalul ANAF.
3.
În cadrul procesului de pregătire a fișierului XML, contribuabilii/plătitorii au la dispoziție mai multe metode de lucru, cum ar fi: a) pentru contribuabilii/plătitorii care dispun de sisteme informatice de contabilitate sau sisteme ERP, „generare automată” din sistemul informatic a fișierului în format XML;
b) pregătirea cu un editor de XML a declarației prin editarea pe schema SAF-T cu introducerea directă a datelor relevante. Validarea declaraților informative D406 se poate face cu validatorul pus la dispoziție de către ANAF. Această metodă poate fi utilizată de către contribuabilii/plătitorii care nu dispun de sisteme informatice de contabilitate sau sisteme ERP;
c)
„Generare externă”, prin prelucrarea fișierului de către un operator de date specializat. Această metodă poate fi utilizată de contribuabilii/plătitorii care folosesc servicii financiar-contabile externalizate.
4.
Declarantul poate genera fișierul SAF-T în format XML cu ajutorul validatorului (program Soft J), pus la dispoziție de către ANAF. Acesta poate fi utilizat independent de către contribuabil/plătitor pentru verificări în sistemul informatic propriu, la sediul său, cu mijloacele sale tehnice. Validatorul Soft J realizează verificările și validările sintactice ale fișierului în format XML (formă, formatul datelor, conținut etc.) și o serie de verificări semantice doar asupra fișierului în format XML. Declarația informativă D406 - în format PDF cu XML atașat - se generează în mod automat prin intermediul Soft J pus la dispoziție de Agenția Națională de Administrare Fiscală.
5.
În situația în care contribuabilul/plătitorul optează să nu folosească capabilitatea din Soft J, pusă la dispoziție de Agenția Națională de Administrare Fiscală, următoarele reguli trebuie să fie respectate când PDF-ul este generat programatic: A.
Documentul PDF trebuie să conțină următoarele câmpuri de metadate (în engleză: macrofields): a) cif = cui declarant, fără prefixul RO;
b) an_r = anul raportării;
c) luna_r = luna raportării;
d) d_rec = I sau R (inițială sau rectificativă);
e) totalPata_A = suma de control;
f) universalCode = tipDeclaratie_versiunePrg = D406_J1.0.0.
B.
Documentul PDF trebuie să respecte formularul (modelul) prevăzut în anexa nr. 2 la ordin.
6.
În cadrul programului Soft J se urmăresc pașii de mai jos: - pasul 1. Selectarea și încărcarea fișierului XML generat pentru validare, prin apăsarea butonului „Alege fișiere”;
- pasul 2. Selectarea tipului de declarație: Declarație informativă D406 pentru raportarea SAF-T sau Declarație informativă D406T pentru raportarea unei declarații de test (pentru testarea aplicației de către contribuabili/plătitori).
7.
Pentru etapa de validare a fișierului XML există 3 opțiuni din care se poate alege: - opțiunea 1. Validarea fișierului XML pentru verificarea erorilor, prin apăsarea butonului „Validare”;
- opțiunea 2. Validarea fișierului XML și crearea Declarației informative D406 - Fișierul standard de control fiscal (SAF-T), cu XML atașat, prin apăsarea butonului „Validare + creare PDF”;
- opțiunea 3. Validarea fișierului XML, crearea Declarației informative D406 - Fișierul standard de control fiscal (SAF-T) cu XML atașat și semnarea electronică, urmate de apăsarea butonului „Validare + creare PDF semnat”.
8.
La sfârșitul etapei prevăzute la pct. 6, contribuabilul/ plătitorul are pregătită Declarația informativă D406 pe care o transmite către ANAF utilizând canalele electronice specifice.
9.
Pentru a putea încărca în portalul ANAF Declarația informativă D406, împreună cu fișierul XML atașat, aceasta trebuie semnată electronic cu certificat digital calificat, rezultând astfel un fișier PDF cu XML atașat și semnat electronic.
10.
Transmiterea unei Declarații informative D406 se face doar în situația în care procesarea a fost realizată cu succes.
11.
Dimensiunea Declarației informative D406 în format PDF cu XML atașat nu trebuie să depășească limita maximă specificată în „Ghidului contribuabilului pentru pregătirea și transmiterea Declarației informative D406 - Fișierul standard de control fiscal (SAF-T)”, care se publică pe site-ul Agenției Naționale de Administrare Fiscală. Dacă Declarația informativă D406 are o dimensiune mai mare decât limita maximă, documentul nu va fi acceptat la încărcare în platforma eguvernare.ro sau prin portalul ANAF. Pentru a putea încărca toate informațiile solicitate, la generare, declarația trebuie împărțită în segmente, conform informațiilor prezentate la pct. 27 și 28, până când toate informațiile aferente perioadei de raportat sunt transmise.
12.
În situația în care, ca urmare a încercării de transmitere a Declarației D406, sunt primite mesaje de eroare/erori, utilizatorul trebuie să verifice cauza erorii prin analiza documentului generat de programul „Validator”, fișierul SAFT.xml.err.txt. Odată identificată eroarea sau identificate erorile, se corectează problema semnalată de către utilizator și se generează un nou fișier XML. Cu fișierul nou-obținut se reiau pașii prezentați la pct. 5 și 6, pentru validarea și generarea Declarației informative D406, începând cu pasul 1. Dacă nu s-au primit mesaje de eroare, declarația este pregătită pentru semnarea electronică și transmitere.
13.
Transmiterea Declarației informative D406 se poate face de către contribuabilii/plătitorii cu obligația de depunere, începând cu prima zi calendaristică a lunii următoare perioadei pentru care obligația devine activă, până la data-limită de depunere - ultima zi a lunii care urmează perioadei pentru care se face raportarea.
14.
Transmiterea se poate face doar de către contribuabilul/ plătitorul cu obligație de depunere sau de către împuternicitul/ reprezentantul legal al acestuia folosind certificatul calificat de semnătură digitală cu care aceștia sunt înrolați în sistemul Agenției Naționale de Administrare Fiscală cu drept de depunere a documentelor și formularelor fiscale în format electronic.
15.
La transmiterea Declarației informative D406 se efectuează verificarea și validarea identității contribuabilului/ plătitorului pentru care se depune Declarația informativă D406, în raport cu identitatea cu care acesta sau împuternicitul/ reprezentantul acestuia este înrolat în sistemul Agenției Naționale de Administrare Fiscală pentru depunerea declarațiilor și formularelor fiscale în format electronic.
16.
Formularele și fișierele SAF-T atașate pentru care nu este validată identitatea sunt respinse.
17.
Declarația informativă D406 se depune doar online, în format electronic, prin intermediul serviciului public digital „Servicii online - Depunere declarații” al Agenției Naționale de Administrare Fiscală sau prin intermediul site-ului www.e-guvernare.ro, serviciul „Depunere declarații ANAF”.
18.
Prima Declarație informativă D406 validată, depusă pentru o lună sau un trimestru de către un contribuabil/plătitor este considerată declarație inițială. Declarațiile ulterioare depuse pentru aceeași perioadă (lună/trimestru) sunt automat considerate declarații rectificative.
19.
După încărcarea Declarației informative D406 - Fișierul standard de control fiscal (SAF-T) se afișează indexul de încărcare, pe baza căruia contribuabilul/plătitorul sau împuternicitul/reprezentantul acestuia se poate informa despre stadiul procesării declarațiilor și formularelor depuse și despre rezultatele procesării acestora.
20.
Rezultatele procesării cuprind eventualele erori și avertismente detectate la încărcare și procesare și un fișier recipisă care confirmă că declarația depusă a fost depusă la termen și că a fost corect procesată.
21.
Declarațiile rectificative care se depun pentru corectarea unei erori materiale, omisiuni etc. trebuie să cuprindă toate informațiile din declarația inițială, plus cele asupra cărora s-au efectuat corecții.
22.
În urma încărcării Declarației informative D406, în portalul Agenției Naționale de Administrare Fiscală, documentul este verificat și analizat, iar în cazul în care contribuabilul/ plătitorul este înregistrat în Spațiul Privat Virtual (SPV), acesta poate primi eventuale mesaje de validare, eroare, atenționare în secțiunea „Mesaje”.
23.
Recipisa și informațiile despre procesarea Declarației informative D406 sunt transmise în mod automat de către Agenția Națională de Administrare Fiscală contribuabilului/plătitorul înscris în SPV sau împuternicitului/reprezentantului acestuia prin SPV. Alternativ, contribuabilii/plătitorii pot verifica stadiul și rezultatele procesării folosind indexul de încărcare prin interogare directă pe site-ul Agenției Naționale de Administrare Fiscală.
24.
În cazul în care un contribuabil/plătitor a primit o recipisă în care se menționează că încărcarea s-a realizat cu erori, acesta este responsabil să corecteze respectivele erori în fișierul XML generat în format SAF-T și să retransmită declarația reluând pașii descriși la pct. 5 și 6.
25.
În cazul depunerii Declarației informative D406, pentru o perioadă de raportare, prin mai multe formulare D406 (ce conțin date raportate modal), se va genera o recipisă pentru fiecare formular depus. Confirmarea transmiterii valide a declarației poate fi realizată doar în ultima recipisă din serie. De exemplu, dacă transmiterea s-a făcut prin 3 fișiere D406 - primele două recipise semnalează că respectivele formulare D406 au fost transmise, care sunt eventualele erori și dacă nu au fost identificate erori - este transmisă confirmarea că nu are erori), iar a treia recipisă semnalează că declarația a fost transmisă, de exemplu, că nu are erori și că declarația în ansamblu este conformă.
26.
În cazul contribuabililor/plătitorilor cu activitate economică mare, materializată într-un număr foarte mare de înregistrări contabile și informații de transmis prin Fișierul standard de control fiscal (SAF-T) - modul de pregătire și depunere a Declarației informative D406 permite transmiterea folosind mai multe formulare D406 (raportare modală), fiecare cu secțiuni sau subsecțiuni din declarația informativă, transmise succesiv de către contribuabilii/plătitorii respectivi pentru perioada de depunere (lună, trimestru), până la data-limită. Sistemele ANAF asigură primirea, procesarea și păstrarea integrală a declarațiilor informative D406.
27.
Raportarea modală reprezintă raportarea datelor în mai multe părți. Raportarea modală privește strict planul de transport al datelor de la contribuabil/plătitor la ANAF, pentru raportarea în format electronic. Raportarea modală se aplică pe un fișier XML generat și funcționează identic pentru toate fișierele extrase/pregătite, indiferent de numărul câmpurilor și conținutul lor. Împărțirea fișierelor XML pentru raportare modală cu mai multe formulare D406 pentru aceeași lună este în sarcina contribuabilului/plătitorului, la pregătirea Declarației informative D406. Această metodă se folosește în cazul unor declarații de dimensiuni foarte mari, iar împărțirea se face la nivel de subsecțiune. Validarea unui fișier XML cu informații SAF-T, transmise modal, se face individual, fișier cu fișier. Regulile de validare sunt următoarele: - secțiunea „HEADER” trebuie să fie prezentă în fiecare fișier XML generat - pentru a identifica a cui este raportarea, cine transmite, ce transmite, pentru ce perioadă, în ce context;
- secțiunile „MASTERFILES”, „GENERAL LEDGER” și „SOURCE DOCUMENTS” se raportează de oricâte ori este nevoie pentru a acoperi conținutul informațional al acestora, respectând criteriul de dimensiune maximă permisă a fișierului XML;
- în cazul în care o secțiune raportată în întregime din punctul de vedere al conținutului informațional duce la depășirea dimensiunii maxime admise pentru fișierul XML, se generează fișiere XML care conțin doar date extrase din subsecțiuni ale secțiunii, astfel încât să fie respectată dimensiunea maximă a documentului XML;
- în cazul în care într-o perioadă de raportare, pentru o anumită secțiune sau subsecțiune, contribuabilul/plătitorul nu are date noi de raportat, prin comparație cu ce a raportat deja în perioada anterioară, secțiunea sau subsecțiunea respectivă poate fi lăsată vidă, adică se specifică în documentul XML doar tagul XML de început și cel de sfârșit al secțiunii sau subsecțiunii.
28.
Raportarea modală este considerată completă dacă sunt prezente concomitent toate secțiunile și câmpurile obligatorii ale fișierului standard de control SAF-T, fapt ce se verifică pentru fiecare depunere de acest tip ce aparține unei perioade de raportare lunară/trimestrială.
29.
Informații detaliate referitoare la procedura de depunere a Declarației informative D406 se publică pe site-ul Agenției Naționale de Administrare Fiscală, prin intermediul „Ghidului contribuabilului pentru pregătirea și transmiterea Declarației informative D406 - Fișierul standard de control fiscal (SAF-T)”.
