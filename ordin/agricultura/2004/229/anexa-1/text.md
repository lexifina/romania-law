# Anexa
Formatul electronic al datelor necesare a fi transmise
A. Conținutul înregistrării poziției
Date
Codul
Obligato-
riu opțio-
nal
Observații
Începutul înregistrării
SR
M
Detaliu despre sistem; indică
începutul înregistrării
Adresa
AD
M
Detaliu despre mesaj; destina-
ția; codul Alpha-3 ISO al țării
Mesajul
TM
M
Detaliu despre mesaj; scrierea
mesajului, POS
Indicativul radio
RC
M
Detaliu despre înregistrare a
vasului
Numărul voiajului
TN
O
Detaliu despre activitate; se-
ria numărului voiajului reali-
zat de vas în anul curent
Numele vasului
NA
O
Înregistrarea vasului
Numărul intern
IR
O*1)
Detaliu despre înregistrarea
vasului; numărul unic de înre-
gistrare a vasului format din
codul Alpha-3 ISO al țării,
urmat de un număr
Numărul extern
XR
O
Detaliu despre înregistrarea
vasului; numărul care se vede
pe vas
Latitudine (în decima-
le)
LT
M
Detaliu despre activitate; po-
ziția vasului la data transmi-
terii
Longitudine(în decima-
le)
LG
M
Detaliu despre activitate; po-
ziția vasului la data transmi-
terii
Viteza
SP
M*2)
Viteza vasului în zecimi de
noduri
Direcția
CO
M*2)
Direcția vasului pe scala de
360°
Data
DA
M
Detaliu despre mesaj; data
transmisiei
Ora
TI
M
Detaliu despre mesaj; ora
transmisiei
Terminarea înregis-
trării
ER
M
Detaliu despre sistem; indică
terminarea înregistrării
*1) Obligatoriu pentru navele de pescuit comunitare și românești.
*2) Opțional până la 31 decembrie 2005.
B. Structura înregistrării poziției:
Fiecare transmisie a datelor va fi structurată astfel:
- dublu slash (//) și caracterele SR indică începutul mesajului,
- dublu slash (//) și codul ce indică începutul datelor,
- simplu slash (/) separă codurile datelor,
- perechile de date sunt separate prin spațiu,
- caracterele ER și dublu slash (//) indică sfârșitul înregistrării
C. Definiția datelor
```
┌────────────┬─────────────┬──────┬────────────┬────────────┬─────────────────┐
│ Categoria  │  Date       │Codul │ Tipul      │Conținuturi │  Definiții      │
├────────────┼─────────────┼──────┼────────────┼────────────┼─────────────────┤
│Detalii     │Începutul    │ SR   │            │            │Indică începutul │
│despre      │înregistrări │      │            │            │înregistrării    │
│sistem      ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Sfârșitul    │ ER   │            │            │Indică sfârșitul │
│            │înregistrări │      │            │            │înregistrării    │
├────────────┼─────────────┼──────┼────────────┼────────────┼─────────────────┤
│Detalii     │Adresa       │ AD   │ Char*3     │Adresa ISO- │Adresa celui ce  │
│despre      │destinației  │      │            │3166        │primește mesajul │
│mesaj       ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Mesajul      │ TM   │ Char*3     │Cod         │Primele litere   │
│            │             │      │            │            │ale mesajului    │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Data         │ DA   │ Num*8      │AAAALLZZ    │Anul,luna și ziua│
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Ora          │ TI   │ Num*4      │OOMM        │Ore și minute (  │
│            │             │      │            │            │Universal Time   │
│            │             │      │            │            │Coordinated)(UTC)│
├────────────┼─────────────┼──────┼────────────┼────────────┼─────────────────┤
│Detalii     │Indicativ    │ RC   │ Char*7     │IRCS Code   │Indicativul în-  │
│despre în-  │radio        │      │            │            │ternațional radio│
│registrarea │             │      │            │            │al vasului       │
│vasului     ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Numele       │ NA   │ Char*30    │ISO 8859,1  │Numele vasului   │
│            │vasului      │      │            │            │                 │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Numărul      │ XR   │ Char*14    │ISO 8859,1  │Numărul care se  │
│            │extern       │      │            │            │vede pe vas      │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Numărul      │ IR   │ Char*3     │ISO 3166+   │Numărul unic dat │
│            │intern       │      │ Char*9     │max.9 N     │vasului în urma  │
│            │             │      │            │            │înregistrării în │
│            │             │      │            │            │registrul flotei │
├────────────┼─────────────┼──────┼────────────┼────────────┼─────────────────┤
│Detalii     │Latitudinea  │ LT   │ Char*7     │+/-DD.ddd   │Valoare negativă │
│despre      │(în decimale)│      │            │            │dacă latitudinea │
│activitate  │             │      │            │            │este în emisfera │
│            │             │      │            │            │sudică ^1) (World│
│            │             │      │            │            │Geodetic System  │
│            │             │      │            │            │1984)(WGS84)     │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Longitudinea │ LG   │ Char*8     │+/-DD.ddd   │Valoare negativă │
│            │(în decimale)│      │            │            │dacă longitudinea│
│            │             │      │            │            │este în emisfera │
│            │             │      │            │            │vestică^1) (World│
│            │             │      │            │            │Geodetic System  │
│            │             │      │            │            │1984)(WGS84)     │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Viteza       │ SP   │ Num*3      │Noduri*10   │e.g.//SP/105=    │
│            │(în decimale)│      │            │            │10,5 noduri      │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Direcția     │ CO   │ Num*3      │Scala de 360│e.g.//CO/270=    │
│            │             │      │            │grade       │270°             │
│            ├─────────────┼──────┼────────────┼────────────┼─────────────────┤
│            │Numărul      │ TN   │ Num*3      │001-999     │Seria numărului  │
│            │voiajului    │      │            │            │voiajului reali- │
│            │             │      │            │            │zat de vas în    │
│            │             │      │            │            │anul curent      │
└────────────┴─────────────┴──────┴────────────┴────────────┴─────────────────┘
```
1) semnul plus (+) nu trebuie neapărat să fie transmis. -------------
