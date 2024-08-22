# Anexa nr. 4
RAPORT TRANZACȚIONARE
Nr. Denumire Format Descriere
1. Cod tranzacție 4!a Cod tranzacție conform tabelului 1 „Categorii tranzacții raportate și corespondența cu codurile operațiunilor SaFIR”
2. Cod operațiune 3!n Cod operațiune, conform anexei nr. 8 la Regulile de sistem SaFIR
3. Ora tranzacției HHMM Ora și minutul la care s-a încheiat tranzacția
4. Data tranzacției YYYYMMDD Data la care s-a încheiat tranzacția
5. Data scadenței YYYYMMDD Data de decontare intenționată a tranzacției
6. ADEL YYYYMMDD Data-limită pentru decontarea fondurilor pentru tranzacțiile cu titluri denominate în valută
7. Identificatorul emisiunii el2!c [4*35x] Cod ISIN
8. Identificator vânzător 4!a2!a2!c[3!c] Cod BIC
9. Cont vânzător 4!a1!n[13!x]
Simbol cont SaFIR
În cazul în care în tranzacția raportată sunt implicate conturi individuale de clienți, participantul are obligația de a raporta simbolurile conturilor cunoscute.
10. Categorie client 2!n În cazul în care vânzătorul este un client al intermediarului, conform tabelului 2 „Clasificare clienți”
11. Identificator cumpărător 4!a2!a2!c[3!c] Cod BIC
12. Cont cumpărător 4!a1!n[13!x]
Simbol cont SaFIR
În cazul în care în tranzacția raportată sunt implicate conturi individuale de clienți, participantul are obligația de a raporta simbolurile conturilor cunoscute.
13. Categorie client 1!n În cazul în care cumpărătorul este un client al intermediarului, conform tabelului 2 „Clasificare clienți”
14. Randament 15d Pentru tranzacțiile LTR se va specifica rata repo. Pentru tranzacțiile IDR câmpul nu se va completa.
15. Preț net 15d
16. Preț brut 15d
17. Suma de decontat 15d
18. Valoare nominală 15d
19. Cod monedă 3!a Cod monedă în care se efectuează tranzacția: RON, USD, EUR
20. Contract
Acronimul contractului standardizat conform tabelului 3 „Acronim contract standardizat”
21. Nr. contract 16!a Numărul contractului; se aplică pentru tranzacțiile FWD, IDR, LTR, SBB, PLEX.
22. Confirmare 35!a Câmp descriptiv care descrie modul în care s-a derulat confirmarea (tel., poștă electronică etc.)
23. Modul de încheiere a tranzacției 35!a Câmp descriptiv care precizează modalitatea de încheiere a tranzacției: telefonic, Refinitiv etc.
24. Comentarii 35!a Câmp descriptiv care poate conține alte informații
Tabelul 1
Categorii tranzacții raportate și corespondența cu codurile operațiunilor SaFIR
Tip tranzacție Cod tranzacție Cod SaFIR
Vânzări - Cumpărări spot SPOT 802, 872
Vânzări - Cumpărări today TD 802, 872
Vânzări - Cumpărări tomorrow TM 802, 872
Vânzări - Cumpărări forward FWD 802, 872
Repo/Reverse repo în cadrul zilei primul pas IDR1 810
Repo/Reverse repo în cadrul zilei pasul doi IDR2 813
Repo/Reverse repo pe termen lung primul pas LTR1 811, 841, 861
Repo/Reverse repo pe termen lung pasul doi LTR2 814, 844, 862
Sell-buyback/buy-sellback primul pas SBB1 851
Sell-buyback/buy-sellback pasul doi SBB2 854
Executări de gajuri prin vânzare PLEX 823
Tabelul 2
Clasificare clienți
Categorie client Subcategorie client Descriere client 1
Persoane juridice rezidente 11 Companii de asigurare 12 Fonduri de investiții 13 Case de brokeraj 14 ANL 15 Fonduri de garantare 16 Camera de comerț 17 Companii nefinanciare 18 Burse de valori 19 Altele 2
Persoane fizice rezidente 3
Persoane juridice nerezidente 4
Persoane fizice nerezidente
Tabelul 3
Acronim contract standardizat
Contract Acronim Exemple
Contract-cadru standardizat propus sau încheiat cu Banca Națională a României NBR4!a, unde 4!a: reprezintă codificarea tranzacției conform tabelului 1 NBRIDR: contract-cadru pentru tranzacții repo/reverse repo cu decontare în aceeași zi conform Regulamentului nr. 9/2020 privind administrarea riscului de decontare și facilitățile de creditare acordate de Banca Națională a României în scopul fluidizării decontării în sistemul ReGIS
Contract nestandardizat, agreat bilateral de participanții care încheie tranzacția 4!a: reprezintă codificarea tranzacției conform tabelului 1 SBB: contract aferent tranzacțiilor sell-buyback/buy-sellback, agreat bilateral REPO: contract aferent tranzacțiilor repo/reverse repo, agreat bilateral
----
