# Anexa 4
Informația se prezintă pe suport magnetic cu următoarele caracteristici: Tip: - CD-R (Compact Disc Recordable) Capacitate: 700 MB Format: ISO/IEC DIS 9660:1999 Sesiune simplă Informația se furnizează structurată pe două tipuri diferite de înregistrări în fișiere ASCII: Tipul 1 conține informație de identificare a agentului plătitor și se va regăsi în fișierul ASCII cu nume fișier: 400_AP_CUI_YYYY_MM_DD, unde CIF=cod de identificare fiscală al agentului plătitor, YYYY_MM_DD data de trimitere a fișierului. Tipul 2 conține informație despre beneficiarii efectivi ai plății sau despre entități (beneficiarii reziduali), [corespunzător art. 124^3 alin. (2)], informații despre plata efectuată conform articolul 124^7 punctul 2 din Legea nr. 571/2003 privind Codul fiscal, cu modificările și completările ulterioare. Nume fișier: 400_ BO_CUI_YYYY_MM_DD, unde CIF=cod de identificare fiscală al agentului plătitor, YYYY_MM_DD data de trimitere a fișierului Setul de caractere folosit pentru reprezentarea informației este UTF-8 Câmpurile alfanumerice sunt intercalate între semnul #, separatorul de câmpuri este virgula Notații folosite: M - câmp obligatoriu O - câmp opțional N - numeric A - alphanumeric TIN - număr de înregistrare fiscală Înregistrarea de tip 1 - identificarea agentului plătitor
```
┌───┬──────────────────┬─────────┬────────────┬────────────────────────────────┐
│   │   Denumirea      │  Tipul  │ Natura și  │      Instrucțiunile            │
│   │    câmpului      │câmpului │ lungimea   │       de completare            │
│   │                  │         │ maximă a   │                                │
│   │                  │         │ câmpului   │                                │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │                  │         │            │                                │
│   │Model declarație  │   M     │     N(3)   │ Constantă numerică 400         │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Anul fiscal       │   M     │     N(4)   │Anul fiscal pentru care se dă   │
│   │                  │         │            │declarația:                     │
│   │                  │         │            │4 cifre sub forma YYYY          │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Tip agent plătitor│   M     │     A(2)   │"01" - persoană fizică          │
│   │                  │         │            │"02" - persoane juridice        │
│   │                  │         │            │"06" - alt tip                  │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Denumire/Nume și  │   M     │     A(100) │Pt. persoane juridice - denumire│
│   │prenume agent     │         │            │Pt. persoane fizice - nume și   │
│   │plătitor          │         │            │prenume                         │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Cod de identi-    │         │            │                                │
│   │ficare fiscală    │   M     │     N(13)  │                                │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Cod tară agent    │         │            │                                │
│   │plătitor          │   M     │     A(2)   │ "RO"                           │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Județ             │   M     │     A(20)  │                                │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Sector            │   O     │     A(2)   │ "S1" : "S6"                    │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Localitate        │   M     │     A(40)  │                                │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│ A │Stradă            │   M     │     A(50)  │                                │
│ D ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│ R │Nr.               │   O     │     A(10)  │                                │
│ E ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│ S │Bloc              │   O     │     A(10)  │                                │
│ A ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Scară             │   O     │     A(10)  │                                │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Ap.               │   O     │     A(10)  │                                │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Etaj              │   O     │     A(10)  │                                │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Cod căsuță poștală│   O     │     A(20)  │                                │
│   ├──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Cod poștal        │   O     │     A(10)  │                                │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Persoană de       │         │            │                                │
│   │contact           │   M     │     A(30)  │Nume și prenume                 │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │E-mail persoană de│         │            │                                │
│   │contact           │   O     │     A(30)  │                                │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Telefon persoană  │         │            │                                │
│   │de contact        │   M     │     N(10)  │                                │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Numărul total al  │         │            │                                │
│   │înregistrărilor   │         │            │                                │
│   │din fișierul cu   │         │            │                                │
│   │înregistrări de   │         │            │                                │
│   │tip 2             │   M     │    N(10)   │                                │
├───┼──────────────────┼─────────┼────────────┼────────────────────────────────┤
│   │Valoarea totală a │         │            │Se adună indiferent de moneda   │
│   │veniturilor din   │   M     │    N(15)   │în care s-a făcut plata.        │
│   │declarație (cores-│         │            │Este o sumă de control          │
│   │punde sumei plăți-│         │            │                                │
│   │lor tuturor bene- │         │            │                                │
│   │ficiarilor din    │         │            │                                │
│   │declarație -      │         │            │                                │
│   │fișierul de Tip   │         │            │                                │
│   │2)....            │         │            │                                │
└───┴──────────────────┴─────────┴────────────┴────────────────────────────────┘
```
Înregistrare de tip 2: informație despre beneficiarul efectiv al plății/entitatea (beneficiarul rezidual) și informații despre plata efectuată
Descrierea
câmpului
Tipul
câmpului
Tipul
datelor
Observații
Instrucțiunile
de completare
ID
M
N(10)
Cheie unică de
identificare a
înregistrării în
cadrul fișierului
Rectificativa-
Marcaj
O
A(1)
Se completează
numai pentru decla-
rația rectificativă
Se completează cu
"X" numai pentru
declarația rectifi-
cativă
Rectificativa-
Ref ID
O
N(10)
Se completează
numai pentru decla-
rația rectificativă
Se preia ID din
fișierul în care a
fost transmisă
declarația care se
rectifică
Rectificativa-
Ref data
O
DATA
Se completează
numai pentru decla-
rația rectificativă
Se preia data din
numele fișierul prin
care s-a transmis
declarația care se
rectifică
Tip beneficiar
M
A(2)
"01" - persoană
fizică
"06" - entitate
Denumire/Nume
M
A(60)
Pentru tip=01 nume,
pentru tip= 06
denumire
Prenume
O/M
A(30)
Câmp obligatoriu
pentru tip=01
Număr de identi-
ficare(TIN)
O/M
A(20)
Câmp obligatoriu
pentru tip=06
Tip adresă
M
A(2)
"A1" - rezidențială
"A2" - de afaceri
"A3" - birou înre-
gistrat
"A4" - domiciliu
fiscal
"A5" - nespecificat
Cod stat de rezi-
dență a benefici-
arului
M
A(2)
Conform tabelului
anexat
Stradă
O
A(50)
Număr
O
A(10)
Bloc
O
A(10)
Apartament
O
A(10)
Etaj
O
A(10)
Localitate
M
A(40)
Sector/județ
O
A(30)
Număr căsuță
poștală
O
A(20)
Cod poștal
O
A(10)
Data nașterii
O/M
yyyy-mm-dd
Data
dacă tip = "01" și
Câmp obligatoriu
nu există numărul
de identificare
fiscală
Statul de naștere
O/M
A(2)
Câmp obligatoriu
dacă tip = "01" și
nu există numărul
de identificare
fiscală
Conform tabelului
anexat
Localitatea de
naștere
O/M
A(50)
Câmp obligatoriu
dacă tip = "01" și
nu există numărul
de identificare
fiscală
Serie pașaport
O
A(10)
Număr pașaport
O
A(10)
Stat emitent
O
A(2)
Cod stat emitent
pașaport
Conform tabelului
anexat
Categoria de venit
M
A(2)
"01"=dobânzi
"02"=venituri din
cesiune, răscumpă-
rare, rambursare
Anul plății
M
N(4)
Format YYYY
Tip cont
M
A(5)
Poate lua una dintre
valorile:
"IBAN",
"OBAN",
"ISIN",
"OSIN",
"OTHER"
Swift
O
A(8)
Codul swift
Număr cont
M
A(30)
Identificarea plă
ții sau creanței
Conform tipului
de cont
Contract incheiat
înainte de 2004
M
A(2)
"01"-true
"02"-false
Moneda în care s-a
efectuat plata
M
A(3)
Conform tabelului 6
(ISO-4217)
Atribut cont
O
A(2)
"01" - un singur
titular
"02" - mai mulți
titulari
"03" -nu se cunoaște
Codul ISO folosit pentru codificarea unei țări este cel corespunzător formatului ISO-3166 Alpha-2 Code. Lista codurilor ISO este dată în tabelul 2, tabelul 3, tabelul 4 și tabelul 5 și poate fi consultată la următoarea adresă web: http://www.iso.org/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/iso_3166-1_decoding_table.html Moneda în care s-a efectuat plata este reprezentată conform standardului din tabelul 6. Tabelul 2 - State membre UE
Numele țării
Codul ISO-3166 Alpha-2
Austria
AT
Belgium
BE
Bulgaria
BG
Cyprus
CY
Czech Republic
CZ
Germany
DE
Denmark
DK
Estonia
EE
Greece
GR
Spain
ES
Finland
FI
France
FR
United Kingdom
GB
Hungary
HU
Ireland
IE
Italy
IT
Lithuania
LT
Luxembourg
LU
Latvia
LV
Malta
MT
The Netherlands
NL
Poland
PL
Portugal
PT
România
RO
Sweden
SE
Slovenia
ȘI
Slovakia
SK
Tabelul 3 - Țări terțe
Numele țării terțe
Codul ISO-3166 Alpha-2
Switzerland
CH
Monaco
MC
Andorra
AD
Liechtenstein
LI
San Marino
SM
Tabelul 4 - Teritorii dependente de Marea Britanie și de Regatul Olandei
Numele
teritoriului
Codul
ISO-3166 Alpha-2
Statul membru la care
teritoriile sunt asociate
Anguilla
AI
GB
Aruba
AW
NL
British Virgin Islands
VG
GB
Cayman Islands
KY
GB
Guernsey
GG
GB
Isle of Man
IM
GB
Jersey
JE
GB
Montserrat
MS
GB
Netherlands Antilles
AN
NL
Turks and Caicos Islands
TC
GB
Tabelul 5 - Coduri țară
Codul
țării
Numele țării
AF
AFGHANISTAN
AL
ALBANIA
AX
ALAND ISLANDS
DZ
ALGERIA
AS
AMERICAN SAMOA
AD
ANDORRA
AO
ANGOLA
AI
ANGUILLA
AQ
ANTARCTICA
AG
ANTIGUA AND BARBUDA
AR
ARGENTINA
AM
ARMENIA
AW
ARUBA
AU
AUSTRALIA
AT
AUSTRIA
AZ
AZERBAIJAN
BS
BAHAMAS
BH
BAHRAIN
BD
BANGLADESH
BB
BARBADOS
BY
BELARUS
BE
BELGIUM
BZ
BELIZE
BJ
BENIN
BM
BERMUDA
BT
BHUTAN
BO
BOLIVIA
BA
BOSNIA AND HERZEGOWINA
BW
BOTSWANA
BV
BOUVET ISLAND
BR
BRAZIL
IO
BRITISH INDIAN OCEAN TERRITORY
BN
BRUNEI DARUSSALAM
BG
BULGARIA
BF
BURKINA FASO
BI
BURUNDI
KH
CAMBODIA
CM
CAMEROON
CA
CANADA
CV
CAPE VERDE
KY
CAYMAN ISLANDS
CF
CENTRAL AFRICAN REPUBLIC
TD
CHAD
CL
CHILE
CN
CHINA
CX
CHRISTMAS ISLAND
CC
COCOS (KEELING) ISLANDS
CO
COLOMBIA
KM
COMOROS
CD
CONGO, DEMOCRATIC REPUBLIC OF (was Zaire)
CG
CONGO, PEOPLE'S REPUBLIC OF
CK
COOK ISLANDS
CR
COSTA RICA
CI
COTE D'IVOIRE
HR
CROATIA (local name: Hrvatska)
CU
CUBA
CY
CYPRUS
CZ
CZECH REPUBLIC
DK
DENMARK
DJ
DJIBOUTI
DM
DOMINICA
DO
DOMINICAN REPUBLIC
TL
EAST TIMOR
EC
ECUADOR
EG
EGYPT
SV
EL SALVADOR
GQ
EQUATORIAL GUINEA
ER
ERITREA
EE
ESTONIA
ET
ETHIOPIA
FK
FALKLAND ISLANDS (MALVINAS)
FO
FAROE ISLANDS
FI
FINLAND
FJ
FIJI
FR
FRANCE
GF
FRENCH GUIANA
PF
FRENCH POLYNESIA
TF
FRENCH SOUTHERN TERRITORIES
GA
GABON
GM
GAMBIA
GE
GEORGIA
DE
GERMANY
GH
GHANA
GI
GIBRALTAR
GR
GREECE
GL
GREENLAND
GD
GRENADA
GP
GUADELOUPE
GU
GUAM
GT
GUATEMALA
GG
GUERNSEY
GN
GUINEA
GW
GUINEA-BISSAU
GY
GUYANA
HT
HAITI
HM
HEARD AND MC DONALD ISLANDS
HN
HONDURAS
HK
HONG KONG
HU
HUNGARY
IS
ICELAND
IN
INDIA
ID
INDONESIA
IR
IRAN (ISLAMIC REPUBLIC OF)
IQ
IRAQ
IE
IRELAND
IL
ISRAEL
IM
ISLE OF MAN
IT
ITALY
JM
JAMAICA
JP
JAPAN
JE
JERSEY
JO
JORDAN
KZ
KAZAKHSTAN
KE
KENYA
KI
KIRIBATI
KP
KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF
KR
KOREA, REPUBLIC OF
XK
KOSOVO
KW
KUWAIT
KG
KYRGYZSTAN
LA
LAO PEOPLE'S DEMOCRATIC REPUBLIC
LV
LATVIA
LB
LEBANON
LS
LESOTHO
LR
LIBERIA
LY
LIBYAN ARAB JAMAHIRIYA
LI
LIECHTENSTEIN
LT
LITHUANIA
LU
LUXEMBOURG
MO
MACAU
MK
MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF
MG
MADAGASCAR
MW
MALAWI
MY
MALAYSIA
MV
MALDIVES
ML
MALI
MT
MALTA
MH
MARSHALL ISLANDS
MQ
MARTINIQUE
MR
MAURITANIA
MU
MAURITIUS
YT
MAYOTTE
MX
MEXICO
FM
MICRONESIA, FEDERATED STATES OF
MD
MOLDOVA, REPUBLIC OF
MC
MONACO
MN
MONGOLIA
XM
MONTENEGRO
MS
MONTSERRAT
MA
MOROCCO
MZ
MOZAMBIQUE
MM
MYANMAR
NA
NAMIBIA
NR
NAURU
NP
NEPAL
NL
NETHERLANDS
AN
NETHERLANDS ANTILLES
NC
NEW CALEDONIA
NZ
NEW ZEALAND
NI
NICARAGUA
NE
NIGER
NG
NIGERIA
NU
NIUE
NF
NORFOLK ISLAND
NP
NORTHERN MARIANA ISLANDS
NO
NORWAY
OM
OMAN
PK
PAKISTAN
PW
PALAU
PS
PALESTINIAN TERRITORY, Occupied
PA
PANAMA
PG
PAPUA NEW GUINEA
PY
PARAGUAY
PE
PERU
PH
PHILIPPINES
PN
PITCAIRN
PL
POLAND
PT
PORTUGAL
PR
PUERTO RICO
QA
QATAR
RE
REUNION
RO
ROMÂNIA
RU
RUSSIAN FEDERATION
RW
RWANDA
KN
SAINT KITTS AND NEVIS
LC
SAINT LUCIA
VC
SAINT VINCENT AND THE GRENADINES
WS
SAMOA
SM
SAN MARINO
ST
SAO TOME AND PRINCIPE
SA
SAUDI ARABIA
SN
SENEGAL
XS
SERBIA
SC
SEYCHELLES
SL
SIERRA LEONE
SG
SINGAPORE
SK
SLOVAKIA (Slovak Republic)
ȘI
SLOVENIA
SB
SOLOMON ISLANDS
SO
SOMALIA
ZA
SOUTH AFRICA
GS
SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS
ES
SPAIN
LK
SRI LANKA
SH
ST. HELENA
PM
ST. PIERRE AND MIQUELON
SD
SUDAN
SR
SURINAME
SJ
SVALBARD AND JAN MAYEN ISLANDS
SZ
SWAZILAND
SE
SWEDEN
CH
SWITZERLAND
SY
SYRIAN ARAB REPUBLIC
TW
TAIWAN
TJ
TAJIKISTAN
TZ
TANZANIA, UNITED REPUBLIC OF
TH
THAILAND
TG
TOGO
TK
TOKELAU
TO
TONGA
TT
TRINIDAD AND TOBAGO
TN
TUNISIA
TR
TURKEY
TM
TURKMENISTAN
TC
TURKS AND CAICOS ISLANDS
TV
TUVALU
UG
UGANDA
UA
UKRAINE
AE
UNITED ARAB EMIRATES
GB
UNITED KINGDOM
US
UNITED STATES
UM
UNITED STATES MINOR OUTLYING ISLANDS
UY
URUGUAY
UZ
UZBEKISTAN
VU
VANUATU
VA
VATICAN CITY STATE (HOLY SEE)
VE
VENEZUELA
VN
VIETNAM
VG
VIRGIN ISLANDS (BRITISH)
VI
VIRGIN ISLANDS (U.S.)
WF
WALLIS AND FUTUNA ISLANDS
EH
WESTERN SAHARA
YE
YEMEN
ZM
ZAMBIA
ZW
ZIMBABWE
Tabelul 6 - Coduri monedă
Codul
monedei
Denumirea monedei
AFA
AFGHANI
ALL
ALBANIAN LEK
DZD
ALGERIAN DINAR
AOK
ANGOLAN KWANZA
ANG
ANTILLEAN GUILDER
ARP
ARGENTINIAN AUSTRAL
AWG
ARUBAN GUILDER
AUD
AUSTRALIAN DOLLAR
BSD
BAHAMIAN DOLLAR
BHD
BAHRAINI DINAR
BDT
BANGLADESH TAKA
BBD
BARBADOS DOLLAR
BZD
BELIZE DOLLAR
BMD
BERMUDIAN DOLLAR
BTN
BHUTAN NGULTRUM
BOB
BOLIVIANO
BWP
BOTSWANA PULA
BRC
BRAZILIAN CRUZADO
BND
BRUNEI DOLLAR
BIF
BURUNDI FRANC
SUR
C.W. OF IND. STATES ROUBLE
KHR
CAMBODIAN RIAL
CAD
CANADIAN DOLLAR
CVE
CAPE VERDE ESCUDO
KYD
CAYMAN ISLAND DOLLAR
XOF
CFA FRANC BCEAO
XAF
CFA FRANC BEAC
XPF
CFP FRANC
CLP
CHILEAN PESO
CNY
CHINA RENMINBI YUAN
COP
COLOMBIAN PESO
KMF
COMORIAN FRANC
CRC
COSTA RICAN COLON
HRD
CROATIAN DINAR
CUP
CUBAN PESO
CYP
CYPRUS POUND
CZK
CZECH KORUNA
DKK
DANISH KRONE
DJF
DJIBOUTI FRANC
DOP
DOMINICAN PESO
XCD
EAST CARIBEAN DOLLAR
ECS
ECUADOR SUCRE
EGP
EGYPTIAN POUND
SVC
EL SALVADOR COLON
EEK
ESTONIAN KORUNA
ETB
ETHIOPIAN BIRR
EUR
EUROPEAN CURRENCY
FKP
FALKLAND ISLANDS POUND
FJD
FIJI DOLLAR
GMD
GAMBIAN DALASI
GHC
GHANA CEDI
GIP
GIBRALTAR POUND
GTQ
GUATEMALAN QUETZAL
GQE
GUINEA EKWELE
GNS
GUINEA FRANC
GWP
GUINEA-BISSAU PESO
GYD
GUYANA DOLLAR
HTG
HAITIAN GOURDE
HNL
HONDURAN LEMPIRA
HKD
HONG KONG DOLLAR
HUF
HUNGARIAN FORINT
ISK
ICELANDIC KRONA
INR
INDIAN RUPEE
IDR
INDONESIAN RUPIAH
IRR
IRANIAN RIAL
IQD
IRAQI DINAR
ILS
ISRAELI SHEKEL
JMD
JAMAICAN DOLLAR
JPY
JAPANESE YEN
JOD
JORDANIAN DINAR
KES
KENYAN SHILLING
KWD
KUWAITI DINAR
KGS
KYRGYZSTAN SOM
LAK
LAOS KIP
LVL
LATVIAN LATS
LBP
LEBANESE POUND
LSM
LESOTHO MALUTI
LRD
LIBERIAN DOLLAR
LYD
LIBYAN DINAR
LTL
LITHUANIAN LITAS
MOP
MACAO PATACA
MKD
MACEDONIAN
MGF
MADAGASCAR FRANC
MWK
MALAWI KWACHA
MYR
MALAYSIAN RINGGIT
MVR
MALDIVES RUFIYAA
MTL
MALTESE POUND
MRO
MAURITANIAN OUGUIYA
MUR
MAURITIUS RUPEE
MXP
MEXICAN PESO
MNT
MONGOLIAN TUGRIK
MAD
MOROCCAN DIRHAM
MZM
MOZAMBIQUE METICAL
MMK
MYANMAR KYAT
NAD
NAMIBIAN DOLLAR
NPR
NEPALESE RUPEE
NZD
NEW ZEALAND DOLLAR
NIC
NICARAGUAN CORDOBA
NGN
NIGERIAN NAIRA
KPW
NORTH KOREAN WON
NOK
NORWEGIAN KRONE
OMR
OMANI RIAL
PKR
PAKISTAN RUPEE
PAB
PANAMANIAN BALBOA
PGK
PAPUA NEW GUINEA KINA
PYG
PARAGUAY GUARANI
PES
PERUVIAN INTI
PHP
PHILIPPINE PESO
PLZ
POLISH ZLOTY
QAR
QATARI RIYAL
ROL
ROMANIAN LEU
RWF
RWANDA FRANC
STD
SAO TOME DOBRA
SAR
SAUDI RIYAL
YUN
SERBIAN + MONTENEG. DINAR
SCR
SEYCHELLES RUPEE
SLL
SIERRA LEONE
SGD
SINGAPORE DOLLAR
SKK
SLOVAKIAN KORUNA
SIT
SLOVENIAN TOLAR
SBD
SOLOMON ISLANDS DOLLAR
SOS
SOMALIA SHILLING
ZAR
SOUTH AFRICAN RAND
KRW
SOUTH KOREAN WON
LKR
SRI LANKA RUPEE
SHP
ST. HELENA POUND
GBP
STERLING
SDP
SUDANESE POUND
SRG
SURINAM
SZL
SWAZILAND LILANGENI
SEK
SWEDISH KRONA
CHF
SWISS FRANC
SYP
SYRIAN POUND
TWD
TAIWAN DOLLAR
TZS
TANZANIAN SHILLING
THB
THAILAND BAHT
TOP
TONGAN PA'ANGA
TTD
TRINIDAD AND TOBAGO DOLLAR
TND
TUNISIAN DINAR
TRL
TURKISH LIRA
AED
UAE DIRHAM
UGS
UGANDA SHILLING
UYP
URUGUAYAN PESO
USD
US DOLLAR
VUV
VANUATU VATU
VEB
VENEZUELAN BOLIVAR
VND
VIETNAMESE DONG
WST
WEST SAMOAN TALA
YDD
YEMENI DINAR
YER
YEMENI RIAL
ZRZ
ZAIRE
ZMK
ZAMBIAN KWACHA
ZWD
ZIMBABWE DOLLAR
