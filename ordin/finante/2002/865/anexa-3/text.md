# Anexa 4
CONDIȚII pentru transmiterea formularului "Decont privind taxa pe valoarea adăugată" pe cale electronică 1. Condiții generale Formularul "Decont privind taxa pe valoarea adăugată" în format electronic se depune la același termen ca și formularele tipărite ale decontului, la unitatea fiscală la care persoanele impozabile sunt înregistrate ca plătitori de taxa pe valoarea adăugată. Formularul "Decont privind taxa pe valoarea adăugată" în format electronic va fi transmis pe discheta de 3 1/2 inch, 1.440 MB, compatibila MS-DOS. Discheta va fi însoțită de exemplarul listat pentru unitatea fiscală, semnat și stampilat. 2. Condiții tehnice standard pentru formatul electronic al formularului "Decont privind taxa pe valoarea adăugată" Informațiile din decont vor fi transmise într-un fisier format text ASCII, în care înregistrarea se termina cu "carriage return" și "linefeed". Separatorul dintre câmpuri va fi virgula, iar delimitatorul pentru campurile de tip caracter va fi #. Ordinea campurilor din structura fisierelor este obligatorie, indiferent dacă acestea se completează sau nu. Fisierul conține o singura înregistrare cu 42 de câmpuri, dintre care 2 de tip caracter și 40 de tip numeric. Fisierul text va avea în mod obligatoriu următoarea denumire: 300_LLAA_Xnnnnnnnnnnnnn.txt, unde: - 300 = codul formularului; - LL = luna decontului; - AA = anul decontului din două caractere; - X = F pentru persoane fizice sau J pentru persoane juridice; - nnnnnnnnnnnnn = codul de înregistrare fiscală/ codul unic de înregistrare, dacă persoana impozabilă este persoana juridică, sau codul numeric personal/numărul de identificare fiscală, dacă persoana impozabilă este persoana fizica (de exemplu: 300_1202_J123456.txt sau 300_1102_F1234567890123.txt). Fisierul va avea următoarea structura:
Descrierea câmpului Tipul câmpului Lungimea maximă Explicații
Cod formular N 3 - se completează cu 300
Cod plătitor de T.V.A. N 13 - se completează codul de înregistrare fiscală/codul unic de înregistrare, dacă persoana impozabilă este persoană juridică
- se completează codul numeric personal/ numărul de identificare fiscală, dacă persoana impozabilă este persoană fizică
Atenție! Fără atributul R.
Luna N 2 - se completează cu luna pentru care se întocmește decontul T.V.A.
Anul N 4 - se completează cu anul pentru care se întocmește decontul T.V.A.
Rd. 1 - Valoare N 15 - se completează cu valoare - Livrări de bunuri/prestări de servicii în țară
Rd. 1 - T.V.A. N 15 - se completează cu T.V.A. - Livrări de bunuri/prestări de servicii în țară
Rd. 2 - T.V.A. N 15 - se completează cu T.V.A. - Operațiuni pentru care beneficiarul a plătit T.V.A. în contul furnizorului potrivit art. 7 din Legea nr. 345/2002
Rd. 3 - Valoare N 15 - se completează cu valoare -
Regularizări
Rd. 3 - T.V.A. N 15 - se completează cu T.V.A. -
Regularizări
Rd. 4 - Valoare N 15 - se completează cu valoare -
Operațiuni scutite cu drept de deducere
Rd. 5. - Valoare N 15 - se completează cu valoare -
Operațiuni pentru care locul livrării/ prestării este în străinătate
Rd. 6 - Valoare N 15 - se completează cu valoare -
Operațiuni scutite fără drept de deducere
Rd. 7 - Valoare N 15 - se completează cu valoare - Total
Rd. 7 - T.V.A. N 15 - se completează cu T.V.A. - Total
Rd. 8 - Pro rata N 6.2 - se completează cu pro rata
Rd. 9 - Valoare N 15 - se completează cu valoare -
Achiziții de bunuri/servicii destinate realizării de operațiuni care dau drept de deducere
Rd. 9 - T.V.A. N 15 - se completează cu T.V.A. - Achiziții de bunuri/servicii destinate realizării de operațiuni care dau drept de deducere
Rd. 10 - Valoare N 15 - se completează cu valoare - Regularizări
Rd. 10 - T.V.A. N 15 - se completează cu T.V.A. - Regularizări
Rd. 11 - Valoare N 15 - se completează cu valoare -
Achiziții de bunuri/servicii destinate realizării de operațiuni care dau/nu dau drept de deducere
Rd. 11 - T.V.A. N 15 - se completează cu T.V.A. - Achiziții de bunuri/servicii destinate realizării de operațiuni care dau/nu dau drept de deducere
Rd. 12 - Valoare N 15 - se completează cu valoare - Regularizări
Rd. 12 - T.V.A. N 15 - se completează cu T.V.A. - Regularizări
Rd. 13 - T.V.A. N 15 - se completează cu T.V.A. de dedus
Rd. 14 - Valoare N 15 - se completează cu valoare -
Achiziții de bunuri/servicii destinate realizării de operațiuni care nu dau drept de deducere
Rd. 14 - T.V.A. N 15 - se completează cu T.V.A. - Achiziții de bunuri/servicii destinate realizării de operațiuni care nu dau drept de deducere
Rd. 15 - Valoare N 15 - se completează cu valoare - Regularizări
Rd. 15 - T.V.A. N 15 - se completează cu T.V.A. - Regularizări
Rd. 16 - Valoare N 15 - se completează cu valoare - Achiziții scutite de T.V.A.
Rd. 17 - Valoare N 15 - se completează cu valoare - Total
Rd. 18 - T.V.A. N 15 - se completează cu T.V.A. intermediar de plată în luna de raportare
Rd. 19 - T.V.A. N 15 - se completează cu T.V.A. intermediar de rambursat în luna de raportare
Rd. 20 - T.V.A. N 15 - se completează cu T.V.A. de plată din decontul lunii precedente
Rd. 21 - T.V.A. N 15 - se completează cu T.V.A. de rambursat din decontul lunii precedente
Rd. 22 - T.V.A. N 15 - se completează cu T.V.A. - Suma pentru care s-a aprobat rambursarea sau compensarea în luna de raportare
Rd. 23 - T.V.A. N 15 - se completează cu T.V.A. - Suma plătită în luna de raportare din T.V.A. de plată rezultată din decontul lunii precedente
Rd. 24 - T.V.A. N 15 - se completează cu T.V.A. - Compensări efectuate potrivit art. 29 lit. D. h) din Legea nr. 345/2002
Rd. 25 - T.V.A. N 15 - se completează cu T.V.A. efectiv restituită cumpărătorilor străini, inclusiv comisionul unităților autorizate
Rd. 26 - T.V.A. N 15 - se completează cu T.V.A. de plată
Rd. 27 - T.V.A. N 15 - se completează cu T.V.A. de rambursat
Banca C 50 - se completează banca
Cont bancar C 50 - se completează contul bancar
--------
