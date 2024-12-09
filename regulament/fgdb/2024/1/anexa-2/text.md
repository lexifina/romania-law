# Anexa nr. 2
Fondul de garantare a depozitelor bancare
LISTA compensațiilor de plătit
Lista compensațiilor de plătit se transmite de Fond instituțiilor de credit mandatate sub forma următoarelor fișiere în format.txt, cu separator de câmp § (section sign), cu structura de mai jos: 1.
Fișierul conținând informații privind plata persoanelor fizice garantate - LIST_PL_PF_MMMM_BBBB.txt
Descrierea câmpului
Denumirea câmpului
Tipul câmpului
Lungimea câmpului
Explicații
Identificatorul unic al deponentului
Cod_dep
N 15
Cod unic atribuit fiecărui deponent de către instituția de credit
Nume deponent
Nume
C 100
Numele deponentului
Prenume deponent
Prenume
C 100
Prenumele deponentului
Data nașterii
Data_n
D 10
Data nașterii deponentului (zz.ll.aaaa)
Serie și număr act identitate
AI
C 30
Seria și numărul actului de identitate al deponentului (buletin de identitate, carte de identitate, pașaport ori alt act de identitate emis conform legii)
Țara actului de identitate
Tara_AI
C 3
Țara unde a fost emis actul de identitate al deponentului
Cod numeric personal
CNP
C 13
Codul numeric personal al deponentului din actul de identitate
Nerezident
Nerezident
L 1
Se completează „T” pentru cetățenii nerezidenți în România
Țară
Tara
C 3
Țara de rezidență
Județ
Județ
C 100
Județul/Provincia/Statul/Regiunea de domiciliu
Localitate
Localitate
C 100
Localitatea de domiciliu
Adresa
Adresa
C 100
Adresa de domiciliu a deponentului, cu excepția informațiilor din câmpurile: Țară, Județ, Localitate
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
Cod bancă cu depozite indisponibile
Cod_banca_f
C 4
Codul băncii pentru care se plătește compensația
Cod bancă mandatată
Cod_banca_m
C 4
Codul băncii mandatate
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
D 10
Se completează doar pentru listele de corecții și conține data la care se trimit corecțiile (zz.ll.aaaa).
Cod corecție
Cod_cor
C 1
Se completează doar pentru listele de corecții cu: a - pentru adăugare; s - pentru ștergere.
Data plății
Data_pl
D 10
Se completează data la care se efectuează plata (zz.ll.aaaa).
Unitatea plătitoare
Unit_pl
C 4
Codul intern al unității mandatarului care a efectuat plata compensației
Suma plătită prin casierie
Suma_casa
N 19,2
Suma compensației plătite efectiv prin casierie
Suma plătită prin virament
Suma_cont
N 19,2
Suma compensației plătite efectiv prin virament bancar
Cont
Cont
C 35
În cazul plăților prin transfer bancar, mandatarul completează numărul contului curent și unitatea bancară unde acesta este deschis.
Banca
Banca_c
C 30
Banca la care este deschis contul în care se plătește compensația
Unitatea bancară
Unit_c
C 30
Subunitatea la care este deschis contul în care se plătește compensația
Cod unitate bancară
Cod_u_c
C 4
Codul subunității se completează în cazul în care plata se face într-un cont deschis în evidențele mandatarului.
Observații
Obs
C 200
Se înscriu datele de identificare ale titularului în cazul în care acestea diferă de cele din listă.
În cazul în care plata se efectuează către altă persoană decât titularul, se înscriu datele de identificare ale acesteia: numele și prenumele, seria și numărul actului de identitate, codul numeric personal și adresa.
2.
Fișierul conținând informații privind plata persoanelor juridice garantate - LIST_PL_PJ_MMMM_BBBB.txt Lista persoanelor juridice include și persoanele fizice autorizate, persoanele fizice care desfășoară activități economice în mod independent, persoanele fizice având profesii liberale, conform legii, precum și alte persoane fizice a căror activitate economică este reglementată prin legi speciale, întreprinderile individuale și întreprinderile familiale, entitățile fără personalitate juridică.
Descrierea câmpului
Denumirea câmpului
Tipul câmpului
Lungimea câmpului
Explicații
Identificatorul unic al deponentului
Cod_dep
N 15
Cod unic atribuit fiecărui deponent de către instituția de credit
Denumirea persoanei juridice
Nume
C 150
Denumirea persoanei juridice
Identificator fiscal
CUI
C 15
Codul unic de înregistrare/Codul fiscal atribuit persoanei juridice
Numărul de înregistrare la registrul comerțului sau al autorizației de funcționare
RC
C 30
Numărul de înregistrare la registrul comerțului sau alt registru ori numărul autorizației de funcționare a persoanei juridice, după caz
Tipul persoanei juridice
Tip_pj
C 10
Tipul persoanei juridice (detaliat în fișierul TIP_PJ_MMMM_BBBB.txt)
Se completează cu codul tipului de client din evidențele instituției de credit. Descrierea tipului de persoană juridică, precum și disponibilitatea informațiilor despre „CUI” și „RC” pentru tipul respectiv de persoană juridică sunt evidențiate în fișierul TIP_PJ_MMMM_BBBB.txt
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
Adresa sediului deponentului, cu excepția informațiilor din câmpurile: Țară, Județ, Localitate
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
Cod banca cu depozite indisponibile
Cod_banca_f
C 4
Codul băncii pentru care se plătește compensația
Cod bancă mandatată
Cod_banca_m
C 4
Codul băncii mandatate
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
D 10
Se completează doar pentru listele de corecții și conține data la care se trimit corecțiile (zz.ll.aaaa).
Cod corecție
Cod_cor
C 1
Se completează doar pentru listele de corecții cu: a - pentru adăugare; s - pentru ștergere.
Data plății
Data_pl
D 10
Se completează data la care se efectuează plata (zz.ll.aaaa).
Unitatea plătitoare
Unit_pl
C 4
Codul intern al unității mandatarului care a efectuat plata compensației
Suma plătită prin casierie
Suma_casa
N 19,2
Suma compensației plătite efectiv prin casierie
Suma plătită prin virament
Suma_cont
N 19,2
Suma compensației plătite efectiv prin virament bancar
Cont
Cont
C 35
În cazul plăților prin transfer bancar, mandatarul completează numărul contului curent și unitatea bancară unde acesta este deschis.
Banca
Banca_c
C 30
Banca la care este deschis contul în care se plătește compensația
Unitatea bancară
Unit_c
C 30
Subunitatea la care este deschis contul în care se plătește compensația
Cod unitate bancară
Cod_u_c
C 4
Codul subunității se completează în cazul în care plata se face într-un cont deschis în evidențele mandatarului.
Observații
Obs
C 200
Se înscriu datele de identificare ale titularului în cazul în care acestea diferă de cele din listă.
În cazul în care plata se efectuează către altă persoană decât titularul, se înscriu datele de identificare ale acesteia: numele și prenumele, seria și numărul actului de identitate, codul numeric personal și adresa.
3.
Fișierul tipurilor de persoane juridice TIP_PJ_MMMM_BBBB.txt - conține codificarea și descrierea tipului de persoană juridică introdusă în câmpul „Tip_pj”
Descrierea câmpului
Denumirea câmpului
Tipul câmpului
Lungimea câmpului
Explicații
Cod tip persoană juridică
Tip_pj
C 10
Codul folosit de instituția de credit în câmpul Tip_pj din fișierul LIST_PL_PJ_MMMM_BBBB.txt
Descriere tip persoană juridică
Descriere
C 100
Descrierea detaliată a tipului de persoană juridică
Identificator fiscal
CUI
L 1
Se completează cu „T” dacă tipul de persoană juridică trebuie să aibă CUI.
Numărul de înregistrare la registrul comerțului sau al autorizației de funcționare
RC
L 1
Se completează cu „T” dacă tipul de persoană juridică trebuie să aibă RC.
OBSERVAȚII Codurile tipurilor de persoană juridică sunt cele primite de la banca ale cărei depozite au devenit indisponibile și au doar caracter informativ.
4.
Fișierul conținând unitățile plătitoare ale mandatarului - UNIT_PL_MMMM.txt
Descrierea câmpului
Denumirea câmpului
Tipul câmpului
Lungimea câmpului
Explicații
Unitate
Unit_pl
C 4
Codul intern al unității mandatarului
Denumire unitate
Den_unit
C 50
Denumirea unității mandatarului
Țară
Tara
C 3
Țara unde are sediul unitatea mandatarului
Județ
Judet
C 100
Județul/Provincia/Statul/Regiunea unde are sediul unitatea mandatarului
Localitate
Localitate
C 100
Localitatea unde are sediul unitatea mandatarului
Adresa
Adresa
C 100
Adresa unității mandatarului, cu excepția informațiilor din câmpurile: Țară, Județ, Localitate
5.
Fișierul conținând corecții la Lista compensațiilor de plătit - {operatiune}_{pp}_MMMM_BBBB_nnn_zzllaaaa.txt, unde {operațiune} poate fi „adaug” sau „sterg”, iar {pp} poate fi „pf” sau „pj”.
Nr. câmp
Descrierea câmpului
Denumirea câmpului
Tipul câmpului
Lungimea câmpului
Explicații 1
Identificatorul unic al deponentului
Cod_dep
N 15
Cod unic atribuit fiecărui deponent de către instituția de credit 2
Cod bancă cu depozite indisponibile
Cod_banca_f
C 4
Codul băncii pentru care se plătește compensația 3
Numărul listei de plată
Nr_list
C 2
Corespunde cu secvența nnn a fișierului de adăugare/ștergere. 4
Identificatorul unic al înregistrării (numărul curent în listă)
Cod_fond
C 10
Poziția deponentului în lista de corecție 5
Data corecției
Data_cor
D 10
Se completează doar pentru listele de corecții și conține data la care se trimit corecțiile (zz.ll.aaaa). 6
Cod corecție
Cod_cor
C 1
Se completează doar pentru listele de corecții cu: a - pentru adăugare; s - pentru ștergere.
6.
Fișierul de confirmare a corecțiilor de către mandatar - Conf_{operatiune}_{pp}_MMMM_BBBB_nnn_zzllaaaa.txt, unde {operațiune} poate fi „adaug” sau „sterg”, iar {pp} poate fi „pf” sau „pj”.
Nr. câmp
Descrierea câmpului
Denumirea câmpului
Tipul câmpului
Lungimea câmpului
Explicații 1
Identificatorul unic al deponentului
Cod_dep
N 15
Cod unic atribuit fiecărui deponent de către instituția de credit 2
Cod bancă cu depozite indisponibile
Cod_banca_f
C 4
Codul băncii pentru care se plătește compensația 3
Numărul listei de plată
Nr_list
C 2
Corespunde cu secvența nnn a fișierului de adăugare/ștergere. 4
Identificatorul unic al înregistrării (numărul curent în listă)
Cod_fond
C 10
Poziția deponentului în lista de corecție 5
Data corecției
Data_cor
D 10
Se completează doar pentru listele de corecții și conține data la care se trimit corecțiile (zz.ll.aaaa). 6
Cod corecție
Cod_cor
C 1
Se completează doar pentru listele de corecții cu: a - pentru adăugare; s - pentru ștergere. 7
Acceptat
Acceptat
C 1
Se completează „1” pentru modificările acceptate și „0” pentru modificările respinse.
Câmpurile 1-6 reproduc în mod identic aceleași câmpuri transmise în fișierul de corecții de la punctul 5.
7.
Situații recapitulative transmise de Fond către instituțiile de credit mandatate 7.1.
Situație recapitulativă la transmiterea Listei compensațiilor de plătit (lista inițială) - recapitulatie_list_pl_MMMM_BBBB.xls FONDUL DE GARANTARE A DEPOZITELOR BANCARE
SITUAȚIE RECAPITULATIVĂ privind fișierele conținând Lista compensațiilor de plătit pentru instituția de credit BBBB transmise în format electronic la data de zz.ll.aaaa
Descrierea
Fișierul
Dimensiunea fișierului
Data ultimei modificări a fișierului
Ora ultimei modificări a fișierului
Nr. de înregistrări
Total compensații de plătit
Persoane fizice garantate
List_pl_pf_MMMM_BBBB.txt
Persoane juridice garantate
List_pl_pj_MMMM_BBBB.txt
Tipuri persoane juridice
Tip_pj_MMMM_BBBB.txt
TOTAL
Director general,....................................................................... (numele, prenumele, semnătura și ștampila)
Director financiar,..................................................... (numele, prenumele și semnătura)
OBSERVAȚII:
1.
Fișierele prin care instituțiile de credit mandatate confirmă Fondului importul Listei compensațiilor de plătit (lista inițială) au denumirile Conf_list_pl_pf_MMMM_BBBB.txt, respectiv Conf_list_pl_pj_MMMM_BBBB.txt.
2.
Situația recapitulativă poate fi transmisă de Fond și în format digital, cu semnăturile electronice calificate ale reprezentanților autorizați, bazate pe certificate digitale calificate emise conform Regulamentului eIDAS.
7.2.
Situație recapitulativă la transmiterea de corecții la Lista compensațiilor de plătit (pentru fiecare listă de corecții) - recapitulatie_corectii_MMMM_BBBB_nnn_zzllaaaa.xls FONDUL DE GARANTARE A DEPOZITELOR BANCARE
SITUAȚIE RECAPITULATIVĂ privind fișierele conținând corecțiile cu numărul nn la Lista compensațiilor de plătit pentru instituția de credit BBBB, transmise în format electronic la data de zz.ll.aaaa
Descrierea Fișierul Dimensiunea fișierului Data ultimei modificări a fișierului Ora ultimei modificări a fișierului Nr. de înregistrări Total compensații de plătit
Ștergeri
Persoane fizice garantate Sterg_pf_MMMM_BBBB_nnn_zzllaaaa.txt
Persoane juridice garantate Sterg_pj_MMMM_BBBB_nnn_zzllaaaa.txt
Adăugări
Persoane fizice garantate Adaug_pf_MMMM_BBBB_nnn_zzllaaaa.txt
Persoane juridice garantate Adaug_pj_MMMM_BBBB_nnn_zzllaaaa.txt
TOTAL
Director general,....................................................................... (numele, prenumele, semnătura și ștampila)
Director financiar,..................................................... (numele, prenumele și semnătura)
OBSERVAȚII: 1.
Fișierele prin care instituțiile de credit mandatate confirmă Fondului importul corecțiilor la Lista compensațiilor de plătit au denumirile, după caz: conf_sterg_pf_MMMM_BBBB_nnn_zzllaaaa.txt, conf_sterg_pj_MMMM_BBBB_nnn_zzllaaaa.txt, conf_adaug_pf_MMMM_BBBB_nnn_zzllaaaa.txt, conf_adaug_pj_MMMM_BBBB_nnn_zzllaaaa.txt.
2.
Situația recapitulativă poate fi transmisă de Fond și în format digital, cu semnăturile electronice calificate ale reprezentanților autorizați, bazate pe certificate digitale calificate emise conform Regulamentului eIDAS.
8.
Situații recapitulative trimise Fondului de instituțiile de credit mandatate 8.1.
Situație recapitulativă la transmiterea plăților zilnice efectuate de instituția de credit mandatată MMMM - recapitulatie_plati_MMMM_BBBB.zzllaaaa.xls Antet instituție de credit MMMM
SITUAȚIE RECAPITULATIVĂ privind plățile efectuate pentru instituția de credit BBBB în data de zz.ll.aaaa
Descrierea
Fișierul
Dimensiunea fișierului
Data ultimei modificări a fișierului
Ora ultimei modificări a fișierului
Nr. de înregistrări
Total compensații plătite
Persoane fizice garantate
Plati_pf_MMMM_BBBB_zzllaaaa.txt
Persoane juridice garantate
Plati_pj_MMMM_BBBB_zzllaaaa.txt
TOTAL plăți de compensații în data de zz.ll.aaaa
Conducătorul MMMM,.............................................................. (numele, prenumele, funcția și semnătura)
Conducătorul compartimentului financiar-contabilitate,..................................................... (numele, prenumele și semnătura)
OBSERVAȚII: Situația recapitulativă poate fi transmisă și în format digital, cu semnăturile electronice calificate ale reprezentanților autorizați, bazate pe certificate digitale calificate emise conform Regulamentului eIDAS.
8.2.
Situație recapitulativă a plăților efectuate de instituția de credit mandatată MMMM pentru instituția de credit BBBB într-o anumită perioadă (anual sau pe întreaga perioadă de plată, la încheierea plăților) Antet instituție de credit MMMM
SITUAȚIE RECAPITULATIVĂ privind plățile efectuate pentru instituția de credit BBBB în perioada................................
Anual - recapitulatie_plati_aaaa_MMMM_BBBB.zzllaaaa.xls
Descrierea Fișierul Dimensiunea fișierului Data ultimei modificări a fișierului Ora ultimei modificări a fișierului Nr. de înregistrări Total compensații plătite
Persoane fizice garantate Plati_pf_aaaa_MMMM_BBBB.txt
Persoane juridice garantate Plati_pj_aaaa_MMMM_BBBB.txt
TOTAL plăți de compensații în perioada........................
Conducătorul MMMM,.............................................................. (numele, prenumele, funcția și semnătura)
Conducătorului compartimentului financiar-contabilitate,..................................................... (numele, prenumele, funcția și semnătura)
La încheierea plăților de compensații pentru instituția de credit BBBB - recapitulatie_plati_final_MMMM_BBBB.zzllaaaa.xls
Descrierea Fișierul Dimensiunea fișierului Data ultimei modificări a fișierului Ora ultimei modificări a fișierului Nr. de înregistrări Total compensații plătite
Persoane fizice garantate Plati_pf_final_MMMM_BBBB.txt
Persoane juridice garantate Plati_pj_final_MMMM_BBBB.txt
TOTAL plăți de compensații în perioada........................
Conducătorul MMMM,.............................................................. (numele, prenumele, funcția și semnătura)
Conducătorul compartimentului financiar-contabilitate,..................................................... (numele, prenumele, funcția și semnătura)
OBSERVAȚII: Situația recapitulativă poate fi transmisă și în format digital, cu semnăturile electronice calificate ale reprezentanților autorizați, bazate pe certificate digitale calificate emise conform Regulamentului eIDAS.
