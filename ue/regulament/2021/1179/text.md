REGULAMENTUL DE PUNERE ÎN APLICARE (UE) 2021/1179 AL COMISIEI
din 16 iulie 2021
de modificare a Regulamentului de punere în aplicare (UE) nr. 1051/2011 în ceea ce privește tabelele agregate și fișierele cu microdate pentru transmiterea datelor
(Text cu relevanță pentru SEE)
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) nr. 692/2011 al Parlamentului European și al Consiliului din 6 iulie 2011 privind statisticile europene referitoare la turism și de abrogare a Directivei 95/57/CE (1), în special articolul 9 alineatele (2) și (3),
întrucât:
(1) Regulamentul de punere în aplicare (UE) nr. 1051/2011 al Comisiei (2) stabilește standardul de schimb pentru tabelele agregate și fișierele cu microdate.
(2) Ca urmare a intrării în vigoare a Regulamentului delegat (UE) 2019/1681 al Comisiei (3) prin care se stabilesc modificările tehnice ale formatului de transmitere a datelor anuale care trebuie transmise Comisiei, este necesară adaptarea anexelor II și III la Regulamentul de punere în aplicare (UE) nr. 1051/2011 în ceea ce privește tabelele agregate și fișierele de transmitere a datelor.
(3) Prin urmare, Regulamentul de punere în aplicare (UE) nr. 1051/2011 trebuie să fie modificat în consecință.
(4) Măsurile prevăzute în prezentul regulament sunt conforme cu avizul Comitetului Sistemului Statistic European instituit prin articolul 7 din Regulamentul (CE) nr. 223/2009 al Parlamentului European și al Consiliului (4),
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Regulamentul de punere în aplicare (UE) nr. 1051/2011 se modifică după cum urmează:
1. Anexa II se modifică după cum urmează:
La rubrica „Capul de tabel”, seturile de date enumerate la a treia liniuță se modifică după cum urmează:
(1) „int_cap_annual” se înlocuiește cu „TOUR_CAP_A”;
(2) „int_occ_annual” se înlocuiește cu „TOUR_OCC_A”;
(3) „int_occ_mnight” se înlocuiește cu „TOUR_NIGHTS_M”;
(4) „int_occ_marrno” se înlocuiește cu „TOUR_ARRNOCC_M”;
(5) „int_non_rented” se înlocuiește cu „TOUR_NONRENT_A”;
(6) „nat_dem_partic” se înlocuiește cu „TOUR_PARTIC_A”;
(7) „nat_dem_sdvout” se înlocuiește cu „TOUR_SDVOUT_Q”;
(8) „nat_dem_sdvdom” se înlocuiește cu „TOUR_SDVDOM_Q”.
2. Anexa III se înlocuiește cu textul din anexa la prezentul regulament.
Articolul 2
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 16 iulie 2021.
Pentru Comisie
Președintele
Ursula VON DER LEYEN
(1) JO L 192, 22.7.2011, p. 17.
(2) Regulamentul de punere în aplicare (UE) nr. 1051/2011 al Comisiei din 20 octombrie 2011 de punere în aplicare a Regulamentului (UE) nr. 692/2011 al Parlamentului European și al Consiliului privind statisticile europene referitoare la turism în ceea ce privește structura rapoartelor de calitate și transmiterea datelor (JO L 276, 21.10.2011, p. 13).
(3) Regulamentul delegat (UE) 2019/1681 al Comisiei din 1 august 2019 de modificare a Regulamentului (UE) nr. 692/2011 al Parlamentului European și al Consiliului privind statisticile europene referitoare la turism, în ceea ce privește termenele de transmitere și adaptarea anexelor I și II (JO L 258, 9.10.2019, p. 1).
(4) Regulamentul (CE) nr. 223/2009 al Parlamentului European și al Consiliului din 11 martie 2009 privind statisticile europene și de abrogare a Regulamentului (CE, Euratom) nr. 1101/2008 al Parlamentului European și al Consiliului privind transmiterea de date statistice confidențiale Biroului Statistic al Comunităților Europene, a Regulamentului (CE) nr. 322/97 al Consiliului privind statisticile comunitare și a Deciziei 89/382/CEE, Euratom a Consiliului de constituire a Comitetului pentru programele statistice ale Comunităților Europene (JO L 87, 31.3.2009, p. 164).
ANEXĂ
„ANEXA III
Fișierele cu microdate pentru transmiterea datelor incluse în secțiunea 2 a anexei II la Regulamentul (UE) nr. 692/2011
Structura fișierului și codificarea: aspecte practice
Fiecare călătorie se înregistrează individual în fișierul cu microdate transmis. Acest fișier cu microdate este verificat și editat în totalitate și, dacă este necesar, este imputat și respectă structura și codificarea descrise în tabelul de mai jos. Comisia (Eurostat) va furniza orientări suplimentare cu privire la formatul de transmitere.
Datele care nu respectă standardul de schimb prevăzut în prezenta anexă se consideră că nu au fost transmise.
Capul de tabel
Scopul capului de tabel este de a identifica seriile de date transmise. El constă în patru câmpuri:
— Perioada de referință este formată din șapte caractere, primele patru caractere identificând anul, iar ultimele trei identificând perioada din an (A00).
— Codul țării este format din două caractere, conținând codul de țară format din două caractere al statului membru care transmite datele. Exemple: BE (Belgia), BG (Bulgaria), …
— Subiectul constă în identificatorul setului de date: nat_dem_microdata.
— Moneda identifică moneda în care sunt raportate cheltuielile (EUR sau NAC). În timp ce statele membre din zona euro transmit datele exprimate în euro (codul EUR), statele membre din afara zonei euro transmit datele exprimate fie în euro, fie în moneda lor națională (codul NAC). Totuși, toate cheltuielile trebuie raportate în aceeași monedă în cadrul aceluiași fișier.
Date
Numele coloanei | Identificator | Descriere | Filtru/observații
ID | 000001-999999 | Numărul secvențial al călătoriei |
CARACTERISTICILE CĂLĂTORIEI
Câmpul 1 | | Luna plecării |
| 01-24 | Numărul lunii (luna ianuarie a anului de referință = 01, luna decembrie a anului de referință = 12; luna ianuarie a anului calendaristic anterior = 13, luna decembrie a anului calendaristic anterior = 24) |
Câmpul 2 | | Durata călătoriei, în număr de înnoptări |
| 001-366 | Număr de înnoptări (maximum 3 cifre) |
Câmpul 3 | | Duratei călătoriei: număr de înnoptări efectuate pe teritoriul național | Numai pentru călătorii în străinătate Variabilă trienală, în anii opționali: cod = gol
| 000-183 | Număr de înnoptări (maximum 3 cifre) |
Câmpul 4 | | Țara principală de destinație |
Codificare conform listei de țări din manualul metodologic realizat în temeiul articolului 10 din Regulamentul (UE) nr. 692/2011
Câmpul 5 | | Obiectivul principal al călătoriei |
| 1 | Scop privat/personal: divertisment, activități recreative și concediu |
| 2 | Scop privat/personal: vizitarea rudelor și prietenilor |
| 3 | Scop privat/personal: altele (de exemplu: tratament medical, pelerinaj) |
| 4 | Scop profesional/afaceri |
| | Tipul destinației | Variabilă trienală, în anii opționali: cod = gol
Câmpul 6 | 1 | Oraș = da |
| 2 | Oraș = nu |
| 9 | Oraș = nu se aplică (Câmpul 5 = 4) |
Câmpul 7 | 1 | Litoral = da |
| 2 | Litoral = nu |
| 9 | Litoral = nu se aplică (Câmpul 5 = 4) |
Câmpul 8 | 1 | Cadru natural (inclusiv malul lacurilor, râurilor etc.) = da |
| 2 | Cadru natural (inclusiv malul lacurilor, râurilor etc.) = nu |
| 9 | Cadru natural (inclusiv malul lacurilor, râurilor etc.) = nu se aplică (Câmpul 5 = 4) |
Câmpul 9 | 1 | Vas de croazieră = da |
| 2 | Vas de croazieră = nu |
| 9 | Vas de croazieră = nu se aplică (Câmpul 5 = 4) |
Câmpul 10 | 1 | Munte (ținuturi muntoase, dealuri etc.) = da |
| 2 | Munte (ținuturi muntoase, dealuri etc.) = nu |
| 9 | Munte (ținuturi muntoase, dealuri etc.) = nu se aplică (Câmpul 5 = 4) |
Câmpul 11 | 1 | Altele = da |
| 2 | Altele = nu |
| 9 | Oraș = nu se aplică (Câmpul 5 = 4) |
Câmpul 12 | | Participarea copiilor | Variabilă trienală, în anii opționali: cod = gol
| 1 | Da |
| 2 | Nu |
| 9 | Nu se aplică (Câmpul 5 = 4) |
Câmpul 13 | | Mijloace de transport principale |
| 1 | Transport aerian (zboruri, regulate sau pe bază de charter, sau alte servicii aeriene) |
| 2 | Cale maritimă (linii pentru pasageri și navete, croaziere, nave de recreare, vase închiriate etc.) |
| 3 | Cale ferată |
| 4 | Autobuz, autocar (regulat/planificat sau ocazional/neplanificat) |
| 5 | Autobuz sau autocar regulat/planificat | Defalcare opțională
| 6 | Autobuz sau autocar ocazional/neplanificat | Defalcare opțională
| 7 | Autovehicul privat (propriu sau în leasing, inclusiv autoturism al prietenilor/rudelor) |
| 8 | Autovehicul închiriat [inclusiv platforme de co-voiajare (car-sharing sau ride-sharing)] |
| 9 | Altul (de exemplu: bicicletă) |
Câmpul 14 | | Mijloace de cazare principale |
| 1 | Cazare închiriată: hoteluri sau unități de cazare similare |
| 2 | Cazare închiriată: terenuri de camping, caravane sau locuri pentru rulote (nerezidențial) |
| 3 | Cazare închiriată: cum ar fi casă, vilă, apartament; cameră (camere) închiriată (închiriate) într-o locuință |
| 4 | Cazare închiriată: altă cazare închiriată (cum ar fi pensiuni pentru tineret, porturi de agrement, unități medicale) |
| 5 | Cazare neînchiriată: casă de vacanță proprie |
| 6 | Cazare neînchiriată: cazare oferită fără plată de către rude sau prieteni |
| 7 | Cazare neînchiriată: altă cazare neînchiriată |
Câmpul 15 | | Rezervarea călătoriei: rezervarea pe internet a mijloacelor de cazare principale | Variabilă trienală, în anii opționali: cod = gol
| 1 | Da |
| 2 | Nu |
Câmpul 16 | | Rezervarea călătoriei: canal de rezervare pentru mijloacele de cazare principale | Variabilă trienală, în anii opționali: cod = gol
| 1 | Direct la furnizorul de servicii de cazare |
| 2 | Prin intermediul unei agenții de voiaj, al unui operator turistic, al unui portal sau sistem de închiriere de locuințe pentru scurtă durată sau al unei agenții de închiriere de locuințe de vacanță, care oferă o listă cu mai mulți furnizori de servicii de cazare |
| 3 | Nicio rezervare nu a fost necesară |
Câmpul 17 | | Rezervarea mijloacelor de cazare principale prin intermediul unui site web sau al unei aplicații, cum ar fi Airbnb, Booking.com, Expedia, HomeAway | Variabilă trienală, în anii opționali: cod = gol
| 1 | Da |
| 2 | Nu |
| 9 | Nu se aplică (Câmpul 14 ≠ 3 sau Câmpul 15 ≠ 1 sau Câmpul 16 ≠ 2) |
Câmpul 18 | | Rezervarea călătoriei: rezervarea pe internet a mijloacelor de transport principale | Variabilă trienală, în anii opționali: cod = gol
| 1 | Da |
| 2 | Nu |
Câmpul 19 | | Rezervarea călătoriei: canal de rezervare pentru mijloacele de transport principale | Variabilă trienală, în anii opționali: cod = gol
| 1 | Direct la furnizorul de servicii de transport |
| 2 | Prin intermediul unei agenții de voiaj, al unui operator turistic, al unui portal |
| 3 | Nicio rezervare nu a fost necesară |
Câmpul 20 | | Rezervarea mijloacelor de transport principale prin intermediul unui site web sau al unei aplicații, cum ar fi BlaBlaCar | Variabilă opțională, dacă nu este transmisă: cod = gol
| 1 | Da |
| 2 | Nu |
| 9 | Nu se aplică (Câmpul 18 ≠ 1 sau Câmpul 19 ≠ 2) |
Câmpul 21 | | Rezervarea călătoriei: pachet de călătorie | Variabilă trienală, în anii opționali: cod = gol
| 1 | Da |
| 2 | Nu |
Câmpul 22 | | Rezervarea călătoriei: rezervarea pachetului pe internet | Variabilă trienală, în anii opționali: cod = gol
| 1 | Da |
| 2 | Nu |
Câmpul 23 | | Cheltuielile legate de călătorie efectuate de turistul individual pentru pachete |
| 00000000-99999998 | Suma exprimată în euro (sau în moneda națională, pentru statele membre din afara zonei euro) (maximum 8 cifre) |
Câmpul 24 | | Cheltuielile legate de călătorie efectuate de turistul individual pentru transport |
| 00000000-99999998 | Suma exprimată în euro (sau în moneda națională, pentru statele membre din afara zonei euro) (maximum 8 cifre) |
Câmpul 25 | | Cheltuielile legate de călătorie efectuate de turistul individual pentru cazare |
| 00000000-99999998 | Suma exprimată în euro (sau în moneda națională, pentru statele membre din afara zonei euro) (maximum 8 cifre) |
Câmpul 26 | | Cheltuielile legate de călătorie efectuate de turistul individual pentru alimente și băutură în cafenele și restaurante | Variabilă opțională, dacă nu este transmisă: cod = gol
| 00000000-99999998 | Suma exprimată în euro (sau în moneda națională, pentru statele membre din afara zonei euro) (maximum 8 cifre) |
Câmpul 27 | | Alte cheltuieli legate de călătorie efectuate de turistul individual (totalul altor cheltuieli, inclusiv pentru bunuri de consum de folosință îndelungată și bunuri de valoare) |
| 00000000-99999998 | Suma exprimată în euro (sau în moneda națională, pentru statele membre din afara zonei euro) (maximum 8 cifre) |
Câmpul 28 | | Bunuri de consum de folosință îndelungată și bunuri de valoare (subcategorie a categoriei «Alte cheltuieli legate de călătorie efectuate de turistul individual») |
| 00000000-99999998 | Suma exprimată în euro (sau în moneda națională, pentru statele membre din afara zonei euro) (maximum 8 cifre) |
Profilul vizitatorului
Câmpul 29 | | Gen |
| 1 | Masculin |
| 2 | Feminin |
Câmpul 30 | | Vârstă |
| 000-198 | Număr de ani împliniți (3 cifre) |
Câmpul 31 | | Țară de reședință |
Codul țării, cu două caractere (Belgia = BE, Bulgaria = BG, ...)
Câmpul 32 | | Nivel de instruire | Variabilă opțională, dacă nu este transmisă: cod = gol
| 1 | Cel mult învățământ secundar inferior (ISCED 2011, nivelurile 0-2) |
| 2 | Secundar superior și postsecundar (neterțiar) (ISCED 2011, nivelurile 3 și 4) |
| 3 | Terțiar (ISCED 2011, nivelurile 5-8) |
Câmpul 33 | | Situația profesională | Variabilă opțională, dacă nu este transmisă: cod = gol
| 1 | Salariat (angajat sau angajat independent) |
| 2 | Șomer |
| 3 | Student (sau elev) |
| 4 | Altul în afara câmpului muncii |
Câmpul 34 | | Venit pe gospodărie, pe cuartile | Variabilă opțională, dacă nu este transmisă: cod = gol
| 1 | Cuartila 1 |
| 2 | Cuartila 2 |
| 3 | Cuartila 3 |
| 4 | Cuartila 4 |
Coeficient de extrapolare
Coeficientul de extrapolare de la eșantion la populație
Câmpul 35 | 000000-999999 | Câmpul 35 conține numere întregi |
Câmpul 36 | 000-999 | Câmpul 36 conține zecimale |
”
