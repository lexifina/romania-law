# Anexa nr. 1
Anexă (Anexa nr. 3 la procedură) FORMATUL DE INTEROGARE a datelor de către personalul poliției rutiere din cadrul Poliției Române și al Poliției de Frontieră Române
```
┌─────────────────────────┬───┬─────────┬──────────────────────────────────────────────────┐
│Elementul interogării    │O/F│Tip/Număr│                                                  │
│                         │   │   de    │            Descriere/Observații                  │
│                         │   │caractere│                                                  │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Date privind vehiculul   │ O │ AN 1-50 │Se completează automat de către aplicația         │
│                         │   │         │informatică.                                      │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Statul membru de         │ O │   Enum  │Selectabil dintr-o listă, care conține codul de   │
│înmatriculare            │   │         │stat și denumirea în clar.                        │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Identificator unic al    │ O │ AN 1-36 │Editabil sau generat de sistem prin bifarea în    │
│căutării                 │   │         │ecran a căsuței "Generare identificator căutare"  │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Numărul de înmatriculare │ O │ AN 1-15 │Cod armonizat (A), potrivit abrevierii prevăzute  │
│                         │   │         │de Directiva 1999/37/CE a Consiliului din         │
│                         │   │         │29 aprilie 1999 privind documentele de            │
│                         │   │         │înmatriculare pentru vehicule                     │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Numărul de înmatriculare,│ F │ AN 1-15 │Aplicabil doar când statul selectat este Germania,│
│partea a doua            │   │         │caz în care completarea este obligatorie          │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Date privind încălcarea  │ O │ AN 1-50 │Se completează automat de către aplicația         │
│                         │   │         │informatică.                                      │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Statul membru în care s-a│ O │   Enum  │Se completează automat de către aplicația         │
│săvârșit încălcarea      │   │         │informatică.                                      │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Data de referință a      │ O │   Dată  │Format "AAAA-LL-ZZ" sau dată cu denominarea       │
│încălcării               │   │         │fusului orar, de exemplu UTC "CCYY-MM-DDZ", sau   │
│                         │   │         │data locală la care se adaugă diferența orară față│
│                         │   │         │de UTC: "CCYY-MM-DD±nn.nn"                        │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Ora de referință a       │ O │   Timp  │Format UTC: "hh:mm:ssZ" sau "hh:mm:ss±00.00"      │
│încălcării               │   │         │                                                  │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Scopul căutării          │ O │   Enum  │Codul încălcării selectabil dintr-o listă, în     │
│                         │   │         │funcție de tipul acesteia.                        │
│                         │   │         │Valorile permise sunt:                            │
│                         │   │         │1 = exces de viteză;                              │
│                         │   │         │2 = conducerea sub influența alcoolului;          │
│                         │   │         │3 = nefolosirea centurii de siguranță;            │
│                         │   │         │4 = nerespectarea semnificației culorii roșii a   │
│                         │   │         │semaforului;                                      │
│                         │   │         │5 = utilizarea unei benzi interzise;              │
│                         │   │         │10 = conducerea sub influența substanțelor        │
│                         │   │         │psihoactive;                                      │
│                         │   │         │11 = nefolosirea căștii de protecție;             │
│                         │   │         │12 = utilizarea ilegală a unui telefon mobil sau a│
│                         │   │         │altui dispozitiv de comunicare în timpul          │
│                         │   │         │conducerii.                                       │
├─────────────────────────┼───┼─────────┼──────────────────────────────────────────────────┤
│Denumirea autorității    │ O │ AN 1-50 │Se completează automat în funcție de setările     │
│competente               │   │         │utilizatorului. În caz contrar se introduce din   │
│                         │   │         │tastatură.                                        │
└─────────────────────────┴───┴─────────┴──────────────────────────────────────────────────┘
```
Abrevieri: O = obligatoriu, în cazul în care informația este disponibilă în sistemul de evidență aparținând statului membru, altul decât România; F = facultativ; AN = alfanumeric; Enum = listă de valori selectabile.
-----
