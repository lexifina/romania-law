# Anexa 3
------- (inlocuieste Anexa nr. 3 ------------------------ la procedura) ------------ Fisierul Cap 1. DBF sau Cap 1. TXT contine cate o înregistrare pentru fiecare asigurat*1) și are urmatoarea structura: 1) pentru persoanele care au mai multe contracte individuale de muncă la același angajator, declarația se va completa cu câte o înregistrare pentru fiecare contract în parte.
Denumire câmp Tip câmp Lung Semnificație
Luna declarației LD N 2 Se completează cu luna anului pentru care se întocmește declarația.
Anul declarației AD N 4 Se completează cu anul pentru care se întocmește declarația.
Cod unic de înregistrare (CUI)/CF pentru angajatori persoane juridice CF N 10 Se completează partea numerică a codului unic de înregistrare/codului fiscal atribuit angajatorilor - persoane juridice.
Cod unic de înregistrare (CUI)/CNP angajator persoane fizice CNPA N 13 Conține Codul unic de înregistrare atribuit prin Certificatul de înregistrare angajatorilor persoane fizice (codul numeric personal al angajatorului).
Nume și prenume asigurat NUME C 30 Conține numele și prenumele asiguratului.
Cod numeric personal CNP N 13 Conține codul numeric personal al asiguratului.
Cod numeric personal anterior CNPANT N 13 Se completează numai în cazul declarațiilor rectificative (REC = "C") și conține codul numeric personal al asiguratului din declarația inițială care trebuie schimbat.
Tip contract TC C 2 Se completează cu:
"1" - pentru toate raporturile de muncă/serviciu cu durata normală a timpului de muncă/lucru cu normă întreagă;
"2" - pentru contractul individual de muncă cu timp parțial de lucru, unde timpul normal de lucru este de 8 ore;
"3" - pentru contractul individual de muncă cu timp parțial de lucru, unde timpul normal de lucru este de 7 ore;
"4" - pentru contractul individual de muncă cu timp parțial de lucru, unde timpul normal de lucru este de 6 ore;
"5" - pentru contract de muncă temporară cu durata normală a timpului de muncă/lucru cu normă întreagă;
"6" - pentru contract de muncă temporară cu timp parțial de lucru, unde timpul normal de lucru este de 8 ore;
"7" - pentru contract de muncă temporară cu timp parțial de lucru, unde timpul normal de lucru este de 7 ore;
"8" - pentru contract de muncă temporară cu timp parțial de lucru, unde timpul normal de lucru este de 6 ore;
"9" - pentru toate raporturile de muncă/serviciu ale angajaților militari cu durata normală a timpului de muncă/lucru cu normă întreagă.
Număr ore normă în zi NON N 2 Se completează cu numărul de ore de lucru normate în zi conform tipului de contract.
Dacă TC = 1, 5 sau 9
NON = 6, 7 sau 8
Dacă TC = 2 sau 6
NON = 2, 3, 4, 5, 6, 7
Dacă TC = 3 sau 7
NON = 2, 3, 4, 5, 6
Dacă TC = 4 sau 8
NON = 2, 3, 4, 5
Număr de zile lucrate în lună NZL N 2 Se completează cu numărul de zile efectiv lucrate în lună, conform tipului de contract (mai mic sau egal cu numărul de zile lucrătoare din luna respectivă, sau după caz, mai mic sau egal cu numărul de zile calendaristice din luna respectivă). Pentru persoana care are raporturile de muncă sau de serviciu suspendate pentru incapacitate temporară de muncă de cel mult 30 de zile, rubrica se va completa în același mod în care se completează pentru persoanele care au lucrat toată luna.
Număr de zile suspendate în lună NZS N 2 Se completează cu numărul de zile suspendate în lună, conform legii, cu excepția suspendării pentru incapacitate temporară de muncă de cel mult 30 de zile.
Baza de calcul BC N 10 Se completează cu drepturile bănești determinate în conformitate cu prevederile art. 14 din Normelemetodologice de aplicare a Legii nr. 76/2002 privind sistemul asigurărilor pentru șomaj și stimularea ocupării forței de muncă, aprobate prin Hotărârea Guvernului nr. 174/2002, cu modificările și completările ulterioare, pentru asigurații prevăzuți la art. 19 din Legea nr. 76/2002, cu modificările și completările ulterioare. În lunile în care raporturile de muncă sau de serviciu se stabilesc, încetează, se suspendă, respectiv se reiau, cu excepția suspendării pentru incapacitate temporară de muncă, dacă aceasta nu depășește 30 de zile, baza de calcul se consideră în funcție de numărul de ore efectiv lucrate în luna respectivă. Pentru persoana care are raporturile de muncă sau de serviciu suspendate pentru incapacitate temporară de muncă de cel mult 30 de zile, rubrica se va completa în același mod cum se completează pentru persoanele care au lucrat toată luna.
Contribuția individuală datorată CID N 8 Conține contribuția datorată de asigurat și reținută de angajator (1% din BC - cu rotunjire potrivit prevederilor legale).
Rectificativă REC C 1 - spațiu dacă declarația nu este rectificativă
- "M" dacă se dorește modificarea înregistrării inițiale
- "A" dacă se dorește adăugarea unei înregistrări noi
- "S" dacă se dorește ștergerea înregistrării inițiale
- "C" dacă se dorește modificarea CNP-ului din declarația inițială.
----------
