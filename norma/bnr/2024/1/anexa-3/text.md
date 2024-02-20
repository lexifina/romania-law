# Anexa nr. 3
CORELAREA informațiilor din mesajul XML Core Bulk Large Remittance Credit Transfer, necesar a fi comunicate de către participanți, pentru a se asigura decontarea automată și reconcilierea finală în relația cu ceilalți participanți la sistemul SENT
1.
La mențiunile <DbtrAcc> și <CdtrAcc> se va completa codul IBAN alocat de participant respectivului cont al unității teritoriale respective.
2.
La mențiunea <DbtrAcc> se va completa după cum urmează: a)
IBAN plătitor, în cazul în care plata este făcută în numele unui client; sau
b) codul BIC al centralei participantului plătitor, precedat de caracterele RO00, sau un cod IBAN alocat de către respectivul participant unui cont intern al centralei proprii, după caz, atunci când plata este făcută de centrala participantului în nume propriu; sau
c) codul IBAN al contului unității teritoriale din care se face plata, în cazul în care plata este ordonată de către o unitate teritorială a participantului, în nume propriu, sau în cazul în care plata este ordonată de către un client care nu are cont deschis la unitatea teritorială respectivă.
3.
Câmpul <Dbtr> se va completa după cum urmează: a) pe primul rând se va trece: nume/denumire plătitor; în cazul în care numele/denumirea depășește spațiul disponibil de 35 de caractere, acesta va fi trunchiat corespunzător;
b) pe rândurile 2 și 3 se va trece: adresa plătitorului; în cazul în care această informație lipsește, dar există informația de pe rândul 4, pe fiecare dintre aceste rânduri se va completa câte un punct; dacă lipsește informația nu numai din rândurile 2 și 3, ci și din rândul 4, aceste rânduri pot fi lăsate libere. În cazul în care adresa completă depășește spațiul disponibil de 70 de caractere, se vor folosi prescurtări;
c) pe ultimul rând (rândul 4) se va trece: codul de înregistrare fiscală al plătitorului sau CNP plătitor, după caz. În cazul în care informația din acest câmp lipsește, acest rând va fi lăsat liber. Completarea acestui câmp este obligatorie în cazul plăților către Trezoreria Statului.
4.
Informațiile despre beneficiar vor fi incluse întotdeauna în <Cdtr> și <CdtrAcct>, atât pentru plățile destinate unui client al unui participant, cât și pentru cele destinate participantului, respectiv unei unități teritoriale a acestuia.
5.
La mențiunea <CdtrAcct> se va completa după cum urmează: a)
IBAN beneficiar, în cazul în care plata este făcută către un client al unui participant; sau
b) codul BIC al centralei participantului beneficiar, precedat de caracterele RO00, sau un cod IBAN alocat de către respectivul participant unui cont intern al centralei proprii, după caz, atunci când plata este făcută către centrala participantului; sau
c) codul IBAN al contului unității teritoriale a participantului către care se face plata, dacă beneficiarul este chiar unitatea teritorială respectivă sau un client al acesteia care nu are cont deschis la aceasta.
6.
Spațiul de 4 x 35 de caractere din câmpul <Cdtr> se va completa după cum urmează: a) pe primul rând se va trece: nume/denumire beneficiar; în cazul în care numele depășește spațiul disponibil de 35 de caractere, acesta va fi trunchiat corespunzător;
b) pe rândurile 2 și 3 se va trece: adresa beneficiarului; în cazul în care această informație lipsește, dar există informația pe rândul 4, pe fiecare dintre aceste rânduri se va completa câte un punct; dacă lipsește informația nu numai din rândurile 2 și 3, ci și din rândul 4, aceste rânduri pot fi lăsate libere. Această informație este obligatorie doar în cazul în care beneficiarul nu deține cont deschis la unitatea teritorială respectivă. În cazul în care adresa completă depășește spațiul disponibil de 70 de caractere, se vor folosi prescurtări;
c) pe ultimul rând (rândul 4) se va trece: codul de înregistrare fiscală al beneficiarului sau CNP-ul beneficiarului, după caz. În cazul în care informația din acest câmp lipsește, acest rând va fi lăsat liber. Completarea acestui câmp este obligatorie în cazul tuturor plăților către Trezoreria Statului. Această informație va fi menționată și în cazul în care plătitorul este și contribuabilul pentru care se plătește obligația.
7.
În câmpul <RmtInf> se vor completa informațiile privind conținutul economic al operațiunii fie cu opțiunea ROC/Informații reprezentând referințe privind conținutul economic al operațiunii și opțional//RFB/Număr ordin de plată, fie, în cazul plăților către Trezoreria Statului, în câmpul <RmtInf> se vor completa obligatoriu următoarele informații: a) pe primul rând: /ROC/Număr de evidență a plății (codul de 23 de caractere alocat de Agenția Națională de Administrare Fiscală, iar în cazurile în care acesta nu există pe documentul de plată, se completează cu un punct);
b) pe al doilea rând: /RFB/Nr. ordin de plată/data emiterii ordinului de plată/data plății ordinului de plată în format de dată yyyymmdd. Cele trei informații vor fi separate prin caracterul „/” (spre exemplu, /RFB/1234/20241103/20241104);
c) pe al treilea rând: Explicații privind conținutul economic al operațiunii. Este obligatoriu de completat în cazul în care nu există informația de pe primul rând. Dacă informația depășește 35 de caractere, se va continua pe rândul următor.
8.
În cazul în care informațiile reprezentând conținutul economic al operațiunii depășesc cele 4 rânduri, se va continua pe rândul următor și se vor folosi aceiași indicatori, respectiv ROC și RFB.
9.
În cazul returnării unei plăți eronate, în câmpul <RmtInf> se va folosi codul /REJT/sau/RETN/, după cum urmează: a) pe primul rând: /REJT/(sau/RETN/) Câmpul din mesajul original datorită căruia are loc returnarea și posibil alte elemente ale mesajului (spre exemplu, opțiunea de câmp sau identificatorul de secvență) ce pot fi utile inițiatorului la determinarea motivului returnării;
b) pe al doilea rând: Cod de eroare;
c) pe al treilea rând:/MREF/Referința mesajului inițial refuzat.
10.
Câmpul <ChrgBr> va fi completat întotdeauna cu opțiunea SHA (shared).
11.
În mesajele XML de tip Core Bulk Large Remittance Credit Transfer, câmpul IBAN plătitor se va completa la mențiunea <IBAN>.../<IBAN> cu una dintre opțiunile următoare: a)
IBAN plătitor, în cazul în care plata este făcută în numele unui client; sau
b) codul BIC al centralei participantului plătitor, precedat de caracterele RO00, sau un cod IBAN alocat de către respectivul participant unui cont intern al centralei proprii, după caz, atunci când plata este făcută de centrala participantului în nume propriu; sau
c) codul IBAN al contului unității teritoriale din care se face plata, în cazul în care plata este ordonată de către o unitate teritorială a participantului în nume propriu sau, în cazul mesajelor XML de tip Core Bulk Large Remittance Credit Transfer, de către un client care nu deține cont deschis la unitatea teritorială respectivă.
12.
În mesajele XML de tip Core Bulk Large Remittance Credit Transfer și Core Bulk Large Remittance Direct Debit Transfer, folosite în relația cu casa de compensare automată, câmpul IBAN beneficiar se va completa la mențiunea <IBAN>.../<IBAN> cu una dintre opțiunile următoare: a)
IBAN-ul beneficiarului, în cazul în care plata este făcută către un client al unui participant; sau
b) codul BIC al centralei participantului beneficiar, precedat de caracterele RO00, sau un cod IBAN alocat de către respectivul participant unui cont intern al centralei proprii, după caz, atunci când plata este făcută către centrala participantului;
c) codul IBAN al contului unității teritoriale a participantului către care se face plata, dacă beneficiarul este chiar unitatea teritorială respectivă sau, în cazul mesajelor XML de tip Core Bulk Large Remittance Credit Transfer, un client al acesteia care nu are cont deschis la aceasta.
13.
În mesajele XML de tip Core Bulk Large Remittance Credit Transfer, informațiile reprezentând referințe privind conținutul economic al operațiunii, inclusiv informațiile solicitate de către Ministerul Finanțelor în cazul plăților către Trezoreria Statului sau referința unei plăți returnate, vor fi completate în câmpul Remittance Information.
-------
