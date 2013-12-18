# Anexa nr. 2
Anexa 2 (Anexa nr. 3 la Ordinul nr. 892/2012) INSTRUCȚIUNI pentru transmiterea în format electronic a Declarației informative privind impozitul pe veniturile din transferul proprietăților imobiliare din patrimoniul personal, cod 14.13.01.13/10i Structura fișier XML pentru Declarația informativă privind impozitul pe veniturile din transferul proprietăților imobiliare din patrimoniul personal (formular 208)
Nr. crt. Elemente/atribute Denumire câmp Tip și lungime câmp Câmp obligatoriu Câmp calculat Formule șirestricții Erori
1. [declarație208]< strong="" style="box-sizing: border-box;"><>
2. luna Perioada de raportare -Luna N(2) DA
- luna în (06,12)pt. an > 2013 ERR - luna raportare
3. an Perioada de raportare -An N(4) DA
an ≥ 2013 ERR - an raportare
4. d_rec Declarație rectificativă N(1) DA
d_rec = (0-inițială, 1-rectificativă)
5. nume_declar Nume declarant C(75) DA
ERR - nume declarantnecompletat
6. prenume_declar Prenume declarant C(75) DA
ERR - prenume declarant necompletat
7. funcție_declar Funcție declarant C(50) DA
ERR - funcție declarant necompletată
8.
Notar public
9. cui Cod de înregistrarefiscală N(13) DA
Verificare cui ERR - CIF notar invalid saunecompletat
10. den Denumire/Nume șiPrenume C(200) DA
ERR - denumire notarnecompletată
11. adresa Adresă domiciliu fiscal C(1000) DA
ERR - adresă notarnecompletată
12. telefon Telefon domiciliu fiscal C(15)
13. fax Fax domiciliu fiscal C(15)
14. mail E-mail domiciliu fiscal C(200)
15. nrben Nr. beneficiari de venit N(15) DA DA nrben =suma(op1) ERR - mod de calcul eronat pentru Nr. beneficiari de venit
16. Tvalt Total valoare înscrisă în documentul de transfer (lei) N(15) DA DA Tvalt = suma(ival_bv) ERR - mod de calcul eronat pentru Total valoare înscrisă în documentul de transfer
17. Tbază Total bază de calcul aimpozitului (lei) N(15) DA DA Tbaza = suma(baza_bv) ERR - mod de calcul eronat pentru Total bază de calcul aimpozitului
18. Timp Total impozit pe venitul din transferul proprietăților imobiliare N(15) DA DA Timp = suma(imp_bv) ERR - mod de calcul eronat pentru Total impozit pe venitul din transferul proprietăților imobiliare
19. totalPlată_A Suma de control N(15) DA DA totalPlată_A =suma (imp_bv) ERR - mod de calcul eronat pentru suma de control
20. [op1] 1-n apariții
21.
Beneficiar de venit
22. cif_bv 1. CNP/NIF N(13)
Verificare cif (la străini nu se cere CNP/NIF) ERR - CIF beneficiarinvalid
23. den_bv 2. Nume, Prenume C(100) DA
ERR - denumire beneficiarnecompletată
24. mod_tr 6. Modalitatea de transfer a dreptului de proprietate N(1) DA
mod_tr =(1,2,3,4) 1 - (V) prin acte de vânzare-cumpărare 2 - (M) prinmoștenire 3 - (D) prin donație 4 - (A) altele ERR - modalitatea de transfer necompletată
25. per_DI 7. Perioadă deținereimobil N(1)
per_DI = (1,2) 1 - sub 3 ani,inclusiv 2 - peste 3 ani ERR - Perioadă deținereimobil
26. explicație Explicație modalitatea de transfer C(200)
dacă mod_tr = 4 atunci explicație<>null ERR - mod_tr = 4 și explicație nu e completată
27. val_bv 8. Valoarea înscrisă îndocumentul de transfer(lei) N(15) DA
28. baza_bv 9. Baza de calcul a impozitului (lei) N(15) DA
ERR - bază de calculnecompletată
29. imp_bv 10. Impozitul pe venitul din transferul proprietăților imobiliare din patrimoniul personal (lei) N(15) DA
Formule de calcul propuse ERR - impozit necompletat
30. taxe_bv 11. Taxele notariale aferente transferului (lei) N(15)
31. [op11]< strong="" style="box-sizing: border-box;"><> 0-n apariții
32.
Cealaltă partecontractantă
33. den_cc 3. Denumire/Nume șiprenume C(200)
dacă mod_tr =(1,3,4) atunciden_cc [] null ERR - denumire cealaltă parte contractantă necompletată
34. cif_cc 4. Cod de identificare fiscală (CF/CNP/NIF) N(13)
Verificare cif ERR - CIF cealaltă parte contractantă invalid
35. cota_cc 5. Cota parte N(3.2) 3 întregi 2 zecim.
cota_cc ≤ 100 suma (cota_cc) = 100 din toți op11 ai unui op1 ERR - suma cote parte pebeneficiar
36. [/op11]
37. [/op1]
38. [declarație208]
Calcul pentru coloana 10 "Impozitul pe venitul din transferul proprietăților imobiliare din patrimoniul personal" (formule de calcul propuse)
imp_bv = x + y%* (baza_bv-z)
x y%
mod_tr = 2 (M) (la finalizare în mai mult de 2 ani) → imp_bv = 0 +1%*(baza_bv -0)
mod_tr = 2 (M) (la finalizare în maximum 2 ani) → imp_bv = 0
mod_tr[]2 (V, D, A) și per_DI = 1 (≤ 3 ani) și baza_bv ≤ 200000 → imp_bv = 0 +3%*(baza_bv -0)
mod_tr[]2 (V, D, A) și per_DI = 1 (≤ 3 ani) și baza_bv > 200000 → imp_bv = 6000 +2%*(baza_bv -200000)
mod_tr[]2 (V, D, A) și per_DI = 2 (> 3 ani) și baza_bv ≤ 200000 → imp_bv = 0 +2%*(baza_bv -0)
mod_tr[]2 (V, D, A) și per_DI = 2 (> 3 ani) și baza_bv > 200000 → imp_bv = 4000 +1%*(baza_bv -200000)
-------
