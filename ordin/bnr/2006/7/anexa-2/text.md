# Anexa 2
RAPORT DE TRANZACTIONARE
```
┌──┬─────────────────┬───────────────┬─────────────────────────────────────────┐
│NR│ Denumire        │   Format      │              Descriere                  │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│1 │Cod tranzactie   │4!a            │Cod tranzactie conform tabel 1 "Categorii│
│  │                 │               │tranzactii și corespondenta cu codurile  │
│  │                 │               │operațiunilor SaFIR"                     │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│2 │Cod operațiune   │3!n            │Cod operațiune, conform regulilor        │
│  │                 │               │sistemului SaFIR, Anexa 8                │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│3 │Ora tranzactiei  │HHMM           │Ora și minutul la care s-a incheiat      │
│  │                 │               │tranzactia                               │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│4 │Data tranzactiei │YYYYMMDD       │Data la care s-a incheiat tranzactia     │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│5 │Data scadentei   │YYYYMMDD       │Data la care se va initia decontarea     │
│  │                 │               │tranzactiei                              │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│6 │ADEL             │YYYYMMDD       │Data limita pentru decontarea fondurilor │
│  │                 │               │pentru tranzactiile cu titluri denominate│
│  │                 │               │în valuta                                │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│7 │Identificatorul  │e12!că4*35x]   │Cod ISIN                                 │
│  │emisiunii        │               │                                         │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│8 │Identificator    │4!a2!a2!că3!c] │Cod BIC                                  │
│  │vânzător         │               │                                         │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│9 │Cont vânzător    │4!a1!n         │Simbol cont SaFIR                        │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│10│Identificator    │4!a2!a2!că3!c] │Cod BIC                                  │
│  │cumparator       │               │                                         │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│11│Cont cumparator  │4!a1!n         │Simbol cont SaFIR                        │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│12│Randament        │15d            │Pentru tranzactiile LTR se va specifică  │
│  │                 │               │rata repo                                │
│  │                 │               │Pentru tranzactiile IDR campul nu se va  │
│  │                 │               │completa                                 │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│13│Pret net         │15d            │                                         │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│14│Pret brut        │15d            │                                         │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│15│Suma de decontat │15d            │                                         │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│16│Cod moneda       │3!a            │Cod moneda în care se efectueaza         │
│  │                 │               │tranzactia: RON                          │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│17│Contract         │               │Acronimul contractului standardizat      │
│  │standardizat     │               │conform tabelului 2, "Acronim contract   │
│  │                 │               │standardizat";                           │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│18│Nr. contract     │16!a           │Numărul contractului; se aplică pentru   │
│  │                 │               │tranzactiile FWD, IDR, LTR, SBB, PLEX    │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│19│Confirmare       │35!a           │Camp descriptiv care descrie modul în    │
│  │                 │               │care s-a derulat confirmarea (tel.,      │
│  │                 │               │posta electronică etc.)                  │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│20│Modul de         │               │Camp descriptiv care precizeaza modali-  │
│  │încheiere a      │               │tatea de încheiere a tranzactiei:        │
│  │tranzactiei      │35!a           │telefonic, Reuters, etc.                 │
├──┼─────────────────┼───────────────┼─────────────────────────────────────────┤
│21│Comentarii       │35!a           │Camp descriptiv care poate contine alte  │
│  │                 │               │informații                               │
└──┴─────────────────┴───────────────┴─────────────────────────────────────────┘
```
Tabel 1 - Categorii tranzactii raportare și corespondenta cu codurile operațiunilor SaFIR
```
┌──────────────────────────────────┬──────────────────┬───────────────────┐
│      Tip tranzactie              │ Cod tranzactie   │   Cod SaFIR       │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Vanzari - Cumparari spot          │    SPOT          │       802         │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Vanzari - Cumparari tody          │    TD            │       802         │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Vanzari - Cumparari tomorrow      │    TM            │       802         │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Vanzari - Cumparari forward       │    FWD           │       802         │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Repo/Reverse repo în cadrul zilei │    IDR1          │       810         │
│primul pas                        │                  │                   │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Repo/Reverse repo în cadrul zilei │    IDR2          │       813         │
│pasul doi                         │                  │                   │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Repo/Reverse repo pe termen       │    LTR1          │       811         │
│lung primul pas                   │                  │                   │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Repo/Reverse repo pe termen       │    LTR2          │       814         │
│lung pasul doi                    │                  │                   │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Sell-buyback/buy-sellback primul  │    SBB1          │       802         │
│pas                               │                  │                   │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Sell-buyback/buy-sellback pasul   │    SBB2          │       802         │
│doi                               │                  │                   │
├──────────────────────────────────┼──────────────────┼───────────────────┤
│Executari gajuri prin vanzare     │    PLEX          │       823         │
│                                  │                  │                   │
└──────────────────────────────────┴──────────────────┴───────────────────┘
```
Tabelul 2 - Acronim contract standardizat
```
┌────────────────────┬────────────────────┬────────────────────────────────────┐
│Contract            │Acronim             │Exemple                             │
├────────────────────┼────────────────────┼────────────────────────────────────┤
│Contract cadru      │NBR4!a, unde        │NBRIDR:contract cadru aferent       │
│standardizat propus │4!a: reprezinta     │tranzactiilor repo/reverse repo cu  │
│sau incheiat cu     │codificarea tranzac-│decontare în aceeasi zi conform     │
│Banca Naționala a   │tiei conform        │Regulamentului nr. 10/2005 privind  │
│României            │tabelului 1         │facilitatile acordate de Banca      │
│                    │                    │Naționala a României în scopul      │
│                    │                    │fluidizarii decontarilor în sistemul│
│                    │                    │ReGIS                               │
├────────────────────┼────────────────────┼────────────────────────────────────┤
│Contract nestandar- │4!a: reprezinta     │SBB: contract aferent tranzactiilor │
│dizat, agreat bila- │codificarea tranzac-│sell-buyback/buy-sellback, agreat   │
│teral de partici-   │tiei conform        │bilateral                           │
│pantii care incheie │tabelului 1         │REPO: contract aferent tranzactiilor│
│tranzactia          │                    │repo/reverse repo, agreat bilateral │
└────────────────────┴────────────────────┴────────────────────────────────────┘
```
____________
