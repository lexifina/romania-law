# Anexa nr. 3
CONVENȚIA
Actual/Actual (ICMA) - descriere și exemple
Determinarea datei cuponului
Există două abordări care tratează diferit modul în care se determină datele de cupon: ICMA (Normal) și ICMA Ultimo.
I.1.
ICMA (Normal) - această metodă presupune că data cuponului se stabilește la exact aceeași zi a lunii ca și cuponul precedent, la intervale egale. Ex. 1: emisiune cu cupon semestrial:
Nr. cupon Dată cupon
1. 01/01/2004
2. 01/07/2004
3. Etc.
Ex. 2: emisiune cu cupon semestrial:
Nr. cupon Dată cupon Notă
1. 30/06/2004 30 este ultima zi a lunii iunie. ICMA Normal prevede că data următorului cupon va fi exact în aceeași zi (și nu ultima zi) a lunii decembrie.
2. 30/12/2004 31 este ultima zi a lunii decembrie.
3. Etc.
Excepție: dacă ziua următorului cupon nu există ca dată, atunci data cuponului se stabilește ca fiind ultima zi a respectivei luni.
Ex. 3: emisiune cu cupon semestrial:
Nr. cupon Dată cupon Notă
1. 30/07/2003
2. 29/02/2004 Pentru luna februarie nu există data de 30, prin urmare, data cuponului este precedenta zi a lunii.
3. Etc.
I.2.
ICMA Ultimo - această metodă se poate aplica numai atunci când datele de cupon coincid cu ultima zi a lunii. Această metodă presupune că data cuponului se stabilește întotdeauna în ultima zi a lunii, la intervale egale. Ex. 4: emisiune cu cupon semestrial:
Nr. cupon Dată cupon Notă
1. 30/06/2004 30 este ultima zi a lunii iunie. ICMA Ultimo prevede că data următorului cupon va fi ultima zi (și nu aceeași zi) a lunii decembrie.
2. 31/12/2004 31 este ultima zi a lunii decembrie.
3. Etc.
Perioade de cupon regulate și neregulate
Metodele ICMA Actual/Actual fac o distincție între perioadele de cupon regulate și cele neregulate. O perioadă de cupon regulată reprezintă un multiplu exact al unei luni și este rezultat al frecvenței plăților de cupon.
Ex. 5: Pentru o emisiune cu plata de cupon semestrială, perioada 01/01/2004-01/07/2004 este o perioadă de cupon regulată pentru că reprezintă un multiplu exact: 6 x 1 lună. De asemenea, este rezultatul exact al frecvenței de plată a cuponului: 12 luni/2 (2 reprezintă frecvența semestrială).
Perioadele de cupon neregulate nu respectă regula enunțată mai sus. Pentru aceste cazuri este necesar să se construiască „perioade de cupon nominale” care să se încadreze în regulile descrise mai sus.
Ex. 6: Pentru o emisiune cu plata de cupon semestrială, dar a cărei primă plată de cupon are loc la data de 01/03/2004, aceasta nu mai reprezintă o plată regulată de cupon, ci una neregulată, deoarece, chiar dacă este un multiplu exact (3 x 1 lună), nu mai este rezultat al frecvenței cuponului (12 luni/2).
II.1.
Calculul dobânzii acumulate și al cuponului pentru perioadele regulate A = (rata anuală a cuponului/F)*(N/C) și reprezintă dobânda acumulată exprimată procentual (în engleză accrued interest)
P = (rata anuală a cuponului/F) și reprezintă rata (%) la care se calculează suma de plată, unde: C = numărul de zile între D1/M1/Y1 și D3/M3/Y3;
N = numărul de zile între D1/M1/Y1 și D2/M2/Y2;
F = frecvența (1 pentru plata de cupon anuală, 2 pentru plata semestrială etc.);
D1/M1/Y1 = data de la care se calculează dobânda acumulată;
D2/M2/Y2 = data până la care se calculează dobânda acumulată;
D3/M3/Y3 = următoarea dată de cupon.
Ex. 7: emisiune cu plata de cupon semestrială, perioadele de cupon regulate: D1/M1/Y1 = 22/10/2003;
D2/M2/Y2 = 15/01/2004;
D3/M3/Y3 = 22/04/2004.
Rata anuală a cuponului = 10%;
F = 2;
P = rata anuală a cuponului/F = 10%/2;
A = (rata anuală a cuponului/F)*(N/C) = (10%/2)*(85/183).
II.2.
Calculul dobânzii acumulate A (accrued interest) și al cuponului pentru perioadele neregulate Dacă perioada dintre D1/M1/Y1 și D3/M3/Y3 nu respectă criteriile perioadelor regulate, atunci este considerată perioadă neregulată și este necesară construirea unei perioade de cupon nominale.
Perioade de cupon neregulate pot fi perioada primului cupon și perioada ultimului cupon. Motivația acestui fapt este aceea că celelalte date de cupon se determină folosind una din convențiile ICMA (Normal) sau Ultimo, iar perioadele aferente următoarelor cupoane vor fi regulate.
Perioada nominală pentru primul cupon (când D1/M1/Y1 coincide cu data emisiunii) se generează numărând înapoi „o perioadă regulată” de la data plății următorului cupon (D3/M3/Y3).
Perioada nominală pentru ultimul cupon (când D3/M3/Y3 coincide cu scadența emisiunii) se generează numărând înainte „o perioadă regulată” de la data penultimului cupon.
Atunci când se generează perioadele de cupon nominale: • dacă se aplică ICMA Normal se folosește aceeași zi a lunii; • dacă se aplică ICMA Ultimo se folosește ultima zi a lunii.
Pentru perioadele neregulate, cuponul și dobânda acumulată se obțin astfel: A = (rata anuală a cuponului/F')*Sumă(Ni/Ci);
P = (rata anuală a cuponului/F')*Sumă(Ni/Ci), unde: F' = partea întreagă [12/F];
D1/M1/Y1 = data de la care se calculează dobânda acumulată;
D2/M2/Y2 = data până la care se calculează dobânda acumulată;
D3/M3/Y3 = următoarea dată de cupon;
C = numărul de zile între D1/M1/Y1 și D3/M3/Y3;
N = numărul de zile între D1/M1/Y1 și D2/M2/Y2;
F = frecvența (1 pentru plata de cupon anuală, 2 pentru plata semestrială etc.);
P = rata la care se calculează suma de plată.
Ex. 8: emisiune cu plata de cupon semestrială, perioade de cupon neregulate D1/M1/Y1 = 15/08/2003
D2/M2/Y2 = 15/03/2004
D3/M3/Y3 = 15/07/2004
Ci = numărul de zile pentru dobânda acumulată;
Ni = numărul de zile aferente perioadelor de cupon nominale;
F = frecvența (1 pentru plata de cupon anuală, 2 pentru plata semestrială etc.);
P = rata la care se calculează suma de plată;
Rata anuală a cuponului = 4%;
F = 2.
Prima perioadă de cupon (15/08/2003 și 15/07/2004) nu respectă criteriile unei perioade regulate, prin urmare este necesară construirea perioadelor nominale. Întrucât este vorba de primul cupon, determinarea datelor perioadelor nominale se realizează numărând înapoi de la data celui de-al doilea cupon, dar respectând convenția ICMA Normal.
Prima perioadă nominală: 15/01/2004-15/07/2004: 182 de zile
Cea de-a doua perioadă nominală: 15/07/2003-15/01/2004: 184 de zile
P = (rata anuală a cuponului/F')*Sumă(Ni/Ci) = 4%/2*[(153/184)+(182/182)]
A = (rata anuală a cuponului/F')*Sumă(Ni/Ci) = (4%/2)*[(153/184)+(60/182)]
