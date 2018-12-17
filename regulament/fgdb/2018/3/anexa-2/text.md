# Anexa nr. 2
Fondul de garantare a depozitelor bancare
LISTA COMPENSAȚIILOR DE PLĂTIT
Lista compensațiilor de plătit se transmite de Fond instituțiilor de credit mandatate sub forma următoarelor fișiere în format txt, cu separator de câmp § (section sign), cu structura de mai jos: 1.
Fișierul conținând informații privind plata persoanelor fizice garantate - LIST_PL_PF_BBBB.txt
Denumire câmp
Tip câmp
Lungime câmp
Explicații
Identificatorul unic al deponentului
Cod_dep
N 15
Cod unic atribuit fiecărui deponent de către instituția de credit
Nume deponent
Nume
C 100
Conține numele deponentului.
Prenume deponent
Prenume
C 100
Conține prenumele deponentului.
Data nașterii
Data_n
D 8
Data nașterii deponentului
Serie și număr act identitate
AI
C 30
Conține seria și numărul actului de identitate al deponentului (care poate fi buletin de identitate, carte de identitate, pașaport ori alt act de identitate emis conform legii).
Țara actului de identitate
Tara_AI
C 3
Conține țara unde a fost emis actul de identitate al deponentului.
Cod numeric personal
CNP
C 13
Conține codul numeric personal al deponentului din actul de identitate.
Nerezident
Nerezident
L 1
Se completează „T” pentru cetățenii nerezidenți în România.
Țară
Tara
C 3
Țara de rezidență
Județ
Judet
C 100
Județul/Provincia/Statul/Regiunea de domiciliu
Localitate
Localitate
C 100
Localitatea de domiciliu
Adresa
Adresa
C 100
Conține adresa de domiciliu a deponentului, cu excepția informațiilor din câmpurile: Țară, Județ, Localitate.
Cod poștal
Cod_p
C 30
Codul poștal aferent adresei deponentului
Compensația
Compensatie
N 19,2
Compensația
Valuta
Valuta
C 3
Valuta în care este exprimată compensația
Cod bancă în faliment
Cod_banca_f
C 4
Codul băncii pentru care se plătește compensația
Numărul listei de plată
Nr_list
C 2
În cazul listei inițiale de plată se completează cu valoarea „01”, iar în cazul listelor cu modificări și adăugări ulterioare acestui câmp i se atribuie în continuare numere începând cu „02”.
Identificatorul unic al înregistrării (numărul curent în listă)
Cod_fond
C 10
Poziția deponentului în listă
Data corecției
Data_cor
D 8
Se completează doar pentru listele de corecții și conține data la care se trimit corecțiile (zz.ll.aa).
Cod corecție
Cod_cor
C 1
Se completează doar pentru listele de corecții cu: a - pentru adăugare; s - pentru ștergere.
Data plății
Data_pl
D 8
Unitatea plătitoare a mandatarului. Se completează data la care se efectuează plata (zz.ll.aa).
Unitatea plătitoare
Unit_pl
C 4
Codul intern al unității mandatarului care a efectuat plata
Suma plătită prin casierie
Suma_casa
N 19,2
Suma compensației plătite efectiv titularului de depozit sau reprezentantului acestuia prin casierie
Suma plătită prin virament în cont
Suma_cont
N 19,2
Suma compensației plătite efectiv titularului de depozit sau reprezentantului acestuia prin virament în cont bancar
Cont
Cont
C 35
În cazul plăților prin transfer bancar, mandatarul completează numărul contului curent și unitatea bancară unde acesta este deschis.
Banca
Banca_c
C 30
Banca la care este deschis contul în care se plătește
Unitatea bancară
Unit_c
C 30
Subunitatea la care este deschis contul în care se plătește
Cod unitate bancară
Cod_u_c
C 4
Codul unității se completează în cazul în care plata se face într-un cont al mandatarului.
Observații
Obs
C 200
Se înscriu datele de identificare ale titularului în cazul în care acestea diferă de cele din listă.
În cazul în care plata se efectuează către altă persoană decât titularul, se înscriu datele de identificare ale acesteia - numele și prenumele, seria și numărul actului de identitate, codul numeric personal și adresa.
2.
Fișierul conținând informații privind plata persoanelor juridice garantate - LIST_PL_PJ_BBBB.txt Lista persoanelor juridice include și persoanele fizice autorizate, persoanele fizice care desfășoară activități economice în mod independent, persoanele fizice având profesii liberale, conform legii, precum și alte persoane fizice a căror activitate economică este reglementată prin legi speciale, întreprinderile individuale și întreprinderile familiale, entitățile fără personalitate juridică.
Denumire câmp
Tip câmp
Lungime câmp
Explicații
Identificatorul unic al deponentului
Cod_dep
N 15
Cod unic atribuit fiecărui deponent de către instituția de credit
Denumirea persoanei juridice
Nume
C 150
Conține denumirea persoanei juridice.
Identificator fiscal
CUI
C 15
Conține codul unic de înregistrare/codul fiscal atribuit persoanei juridice.
Numărul de înregistrare la registrul comerțului sau al autorizației de funcționare
RC
C 30
Numărul de înregistrare la registrul comerțului sau alt registru ori numărul autorizației de funcționare a persoanei juridice, după caz
Tipul persoanei juridice
Tip_pj
C 10
Conține tipul persoanei juridice (detaliat în fișierul TIP_PJ_BBBB.txt). Se completează cu codul tipului de client din evidențele instituției de credit. Descrierea tipului de persoană juridică, precum și disponibilitatea informațiilor despre „CUI” și „RC” pentru tipul respectiv de persoană juridică sunt evidențiate în fișierul TIP_PJ_BBBB.txt.
Nerezident
Nerezident
L 1
Se completează „T” pentru persoanele juridice străine nerezidente în România.
Țară
Tara
C 3
Țara unde se află sediul
Județ
Judet
C 100
Județul/Provincia/Statul/Regiunea unde se află sediul
Localitate
Localitate
C 100
Localitatea unde se află sediul
Sediul
Adresa
C 100
Conține adresa sediului deponentului, cu excepția informațiilor din câmpurile: Țară, Județ, Localitate.
Cod poștal
Cod_p
C 30
Codul poștal aferent sediului deponentului
Compensația
Compensatie
N 19,2
Compensația
Valuta
Valuta
C 3
Valuta în care este exprimată compensația
Cod banca în faliment
Cod_banca_f
C 4
Codul băncii pentru care se plătește compensația
Numărul listei de plată
Nr_list
C 2
În cazul listei inițiale de plată se completează cu valoarea „01”, iar în cazul listelor cu modificări și adăugări ulterioare acestui câmp i se atribuie în continuare numere începând cu „02”.
Identificatorul unic al înregistrării (numărul curent în listă)
Cod_fond
C 10
Poziția deponentului în listă
Data corecției
Data_cor
D 8
Se completează doar pentru listele de corecții și conține data la care se trimit corecțiile (zz.ll.aa).
Cod corecție
Cod_cor
C 1
Se completează doar pentru listele de corecții cu: a - pentru adăugare s - pentru ștergere
Data plății
Data_pl
D 8
Unitatea plătitoare a mandatarului. Se completează data la care se efectuează plata (zz.ll.aa).
Unitatea plătitoare
Unit_pl
C 4
Codul intern al unității mandatarului care a efectuat plata
Suma plătită prin casierie
Suma_casa
N 19,2
Suma compensației plătite efectiv titularului de depozit sau reprezentantului acestuia prin casierie
Suma plătită prin virament în cont
Suma_cont
N 19,2
Suma compensației plătite efectiv titularului de depozit sau reprezentantului acestuia prin virament în cont bancar
Cont
Cont
C 35
În cazul plăților prin transfer bancar, mandatarul completează numărul contului curent și unitatea bancară unde acesta este deschis
Banca
Banca_c
C 30
Subunitatea la care este deschis contul în care se plătește
Unitatea bancară
Unit_c
C 30
Subunitatea la care este deschis contul în care se plătește
Cod unitate bancară
Cod_u_c
C 4
Codul unității se completează în cazul în care plata se face într-un cont al mandatarului.
Observații
Obs
C 200
Se înscriu datele de identificare ale titularului în cazul în care acestea diferă de cele din listă.
În cazul în care plata se efectuează către altă persoană decât titularul, se înscriu datele de identificare ale acesteia - numele și prenumele, seria și numărul actului de identitate, codul numeric personal și adresa.
3.
Fișierul tipurilor de persoane juridice TIP_PJ_BBBB.txt - conține codificarea și descrierea tipului de persoană juridică introdusă în câmpul „Tip_pj”
Denumire câmp Tip câmp Lungime câmp Explicații
Cod tip persoană juridică Tip_pj C 10 Conține codul folosit de instituția de credit în câmpul Tip_pj din fișierul LIST_PL_PJ_BBBB.txt.
Descriere tip persoană juridică Descriere C 100 Conține descrierea detaliată a tipului de persoană juridică.
Identificator fiscal CUI L 1 Se completează cu „T” dacă tipul de persoană juridică trebuie să aibă CUI.
Numărul de înregistrare la registrul comerțului sau al autorizației de funcționare RC L 1 Se completează cu „T” dacă tipul de persoană juridică trebuie să aibă RC.
OBSERVAȚII CODURILE TIPURILOR DE PERSOANĂ JURIDICĂ SUNT CELE PRIMITE DE LA BANCA ALE CĂREI DEPOZITE AU DEVENIT INDISPONIBILE ȘI AU DOAR CARACTER INFORMATIV.
4.
FIȘIERUL CONȚINÂND UNITĂȚILE PLĂTITOARE ALE MANDATARULUI - UNIT_PL.TXT
Denumire câmp Tip câmp Lungime câmp Explicații
Unitate Unit_pl C 4 Conține codul intern al unității mandatarului.
Denumire unitate Den_unit C 50 Conține denumirea unității mandatarului.
Țară Tara C 3 Țara unde are sediul unitatea mandatarului.
Județ Judet C 100 Județul/Provincia/Statul/Regiunea unde are sediul unitatea mandatarului
Localitate Localitate C 100 Localitatea unde are sediul unitatea mandatarului
Adresa Adresa C 100 Conține adresa unității mandatarului, cu excepția informațiilor din câmpurile: Țară, Județ, Localitate.
