# Anexa 3
Situația sumelor utilizate pentru acoperirea plății compensației către participanți și beneficiari
```
┌──────────┬─────────────┬─────────┬────────────┬─────────────┬─────────────┐
│   Cod    │     Cod     │   Cod   │   CNP      │   Suma      │     Suma    │
│ comandă  │administrator│   fond  │participant/│compensației │compensației │
│          │             │         │beneficiar  │plătite către│plătite către│
│          │             │         │            │participanții│participanții│
│          │             │         │            │ fondurilor  │ fondurilor  │
│          │             │         │            │  de pensii  │  de pensii  │
│          │             │         │            │administrate │ facultative │
│          │             │         │            │   privat    │    (lei)    │
│          │             │         │            │    (lei)    │             │
├──────────┼─────────────┼─────────┼────────────┼─────────────┼─────────────┤
│  Col. 1  │    Col. 2   │ Col. 3  │   Col. 4   │    Col. 5   │    Col. 6   │
├──────────┼─────────────┼─────────┼────────────┼─────────────┼─────────────┤
│          │             │         │            │             │             │
├──────────┼─────────────┼─────────┼────────────┼─────────────┼─────────────┤
│          │             │         │            │             │             │
├──────────┼─────────────┼─────────┼────────────┼─────────────┼─────────────┤
│          │    TOTAL    │    x    │            │             │             │
└──────────┴─────────────┴─────────┴────────────┴─────────────┴─────────────┘
```
Instrucțiuni de completare a anexei nr. 3 la normă 1. Anexa nr. 3 la normă se completează de către Fondul de garantare. 2. Instrucțiunile prezentate în continuare au ca scop standardizarea procesului de raportare a balanței de verificare a conturilor contabile. 3. Câmpurile anexei nr. 3 la normă se completează după cum urmează:
```
┌────┬─────────────────────────────┬───────────────────────────────────────────┐
│Nr. │                             │                                           │
│crt.│       Denumirea câmpului    │         Descrierea câmpului               │
├────┼─────────────────────────────┼───────────────────────────────────────────┤
│  1.│Codul de comandă             │Codul comenzii va avea una dintre          │
│    │                             │următoarele valori: 1 = raportare inițială;│
│    │                             │5 = raportare rectificativă                │
├────┼─────────────────────────────┼───────────────────────────────────────────┤
│  2.│Cod administrator            │Cod administrator înscris în Registrul     │
│    │                             │Autorității                                │
├────┼─────────────────────────────┼───────────────────────────────────────────┤
│  3.│Cod fond                     │Cod fond înscris în Registrul Autorității  │
├────┼─────────────────────────────┼───────────────────────────────────────────┤
│  4.│CNP participant/beneficiar   │CNP participant/beneficiar, conform        │
│    │                             │documentelor justificative                 │
├────┼─────────────────────────────┼───────────────────────────────────────────┤
│  5.│Suma compensației plătite    │Valoarea pentru suma compensației plătite  │
│    │către participanții          │către participanții fondurilor de pensii   │
│    │fondurilor de pensii         │administrate privat (lei)                  │
│    │administrate privat (lei)    │                                           │
├────┼─────────────────────────────┼───────────────────────────────────────────┤
│  6.│Suma compensației plătite    │Valoarea pentru suma compensației plătite  │
│    │către participanții          │către participanții fondurilor de pensii   │
│    │fondurilor de pensii         │facultative (lei)                          │
│    │facultative (lei)            │                                           │
└────┴─────────────────────────────┴───────────────────────────────────────────┘
```
Raportare inițială (cod 1) 4. Metodologia de transmitere electronică a anexei nr. 3 la normă
a) Fișierul obținut este denumit după următoarea sintaxă:
YYYYMMDD_anx3fg_1_GGG.xml.p7s, unde: YYYYMMDD reprezintă ultima zi calendaristică a trimestrului pentru care se întocmește raportul; GGG reprezintă codul Fondului de garantare înregistrat în Registrul Autorității.
b) Fișierele menționate la lit. a) se semnează electronic, cu semnătura electronică extinsă a persoanei responsabile notificate conform art. 4 din normă.
c) Fișierul YYYYMMDD_anx3fg_1_GGG.xml.p7s, semnat electronic, se încarcă în sistemul informatic de raportare, în folderul dedicat "anx3fg".
5. Anexa nr. 3 la normă se întocmește trimestrial și se transmite în termen de 25 de zile calendaristice de la expirarea perioadei pentru care se face raportarea. Perioada pentru care se face raportarea este un trimestru. 6. SIR procesează automat datele prevăzute în anexa nr. 3 la normă. 7. SIR transmite automat mesaje persoanelor responsabile cu activitatea de raportare, acestea având obligația de a analiza aceste mesaje în scopul soluționării eventualelor erori sau avertismente. Pentru a putea fi procesate, este obligatorie respectarea planului de conturi aplicabil (existența conturilor în planul de conturi) și a funcției conturilor din planul de conturi aplicabil. Nerespectarea acestor principii de bază conduce la imposibilitatea procesării informațiilor transmise prin anexa nr. 3 la normă. Raportare rectificativă (cod 5) 8. Orice modificare a unei raportări inițiale sau orice raport transmis după termenul stabilit de depunere se consideră raportare rectificativă. 9. Raportarea rectificativă pentru anexa nr. 3 la normă conține, în mod obligatoriu, două fișiere semnate electronic cu semnătura electronică extinsă a persoanei responsabile notificate conform art. 4 din normă, astfel:
a) un fișier în format XML cu valorile corecte (rectificate), denumit conform sintaxei:
YYYYMMDD_anx3fg_5_GGG.xml.p7s;
b) un fișier în format RTF care conține o notă explicativă detaliată cu privire la valorile corectate și motivele care au generat raportarea eronată, inclusiv înregistrările contabile de corecție care s-au efectuat, denumit conform sintaxei:
YYYYMMDD_anx3fg_5_GGG.rtf.p7s. 10. Lipsa oricărui fișier menționat la pct. 9 determină respingerea raportării rectificative. 11. Raportarea rectificativă pentru anexa nr. 3 la normă se încarcă în SIR, în folderul dedicat "anx3fg".
