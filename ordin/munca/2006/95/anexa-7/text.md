# Anexa 7
------- (Anexa nr. 1.4.1 la norme) -------------------------- Structura anexei 1.3 pentru raportarea Declarațiilor privind evidența nominală a beneficiarilor de indemnizație pentru creșterea copilului și a perioadelor asimilate în sistemul public de pensii conform prevederilor OUG nr. 148/2005 privind susținerea familiei în vederea creșterii copilului Descrierea organizării înregistrărilor din fișier: Fișierul pentru raportarea anexei 1.3 va avea obligatoriu denumirea A13_CF_AA_LL.DBF unde - CF reprezintă codul fiscal al Direcției județene de Muncă, Solidaritate Socială și Familie/municipiului București sau al angajatorilor persoane juridice prevăzute la art. 29 din Ordonanța de urgenta a Guvernului nr. 148/2005) - AA reprezintă ultimele 2 cifre ale anului anul pentru care se întocmește declarația - LL reprezintă luna anului pentru care se întocmește declarația Fișierul conține câte o înregistrare pentru fiecare beneficiar de indemnizație pentru creșterea copilului și a perioadelor asimilate în sistemul public de pensii conform prevederilor Ordonanța de urgenta a Guvernului nr. 148/2005 privind susținerea familiei în vederea creșterii copilului și are următoarea structură:
Denumire câmp Tip câmp Lung. Explicații
Anul AN N 4 Se completează cu anul pentru care se întocmește declarația
Luna LN N 2 Se completează cu luna anului pentru care se întocmește declarația
Cod unic de înregistrare - CF al Direcției județene de Muncă, Solidaritate Socială și Familie/municipiului București sau al angajatorilor persoane juridice prevăzute la art. 29 din OUG nr. 148/2005 CF N 10 Se completează partea numerică a codului fiscal atribuit DMSSF, sau angajatorilor - persoane juridice prevăzute la art. 29 din OUG nr. 148/2005, care raportează beneficiarii de indemnizație pentru creșterea copilului și a perioadelor asimilate în sistemul public de pensii conform prevederilor OUG nr. 148/2005 privind susținerea familiei
Denumire angajator sau asimilați ai acestora care raportează beneficiari de OUG nr. 148/2005 DEN C 29 Conține denumirea DMSSF sau a angajatorilor persoane juridice prevăzute la art. 29 din OUG nr. 148/2005, care raportează beneficiarii de indemnizație pentru creșterea copilului și a perioadelor asimilate în sistemul public de pensii conform prevederilor OUG nr. 148/2005 privind susținerea familiei
Nume și prenume asigurat NUME C 29 Conține numele și prenumele asiguratului beneficiar de indemnizație pentru creșterea copilului și a perioadelor asimilate în sistemul public de pensii conform prevederilor OUG nr. 148/2005 privind susținerea familiei
Cod asigurat CNP N 13 Conține codul numeric personal al asiguratului beneficiar de indemnizație pentru creșterea copilului și a perioadelor asimilate în sistemul public de pensii conform prevederilor OUG nr. 148/2005 privind susținerea familiei
Număr zile lucrătoare PP N 2 Conține numărul total de zile lucrătoare din luna în care asiguratul a beneficiat de indemnizații prevăzute de OUG nr. 148/2005
Județ A_JUD C 3 Cod județ angajator - asimilații acestora, plătitori de indemnizații conform OUG nr. 148/2005
- se completează obligatoriu(
Tipul declarației TIPD C 1 Se completează cu R pentru declarația rectificativă, spațiu în rest. Declarația rectificativă se completează numai pentru pozițiile modificate față de declarația inițială (înregistrările cu modificări față de declarația inițială, înregistrări noi față de declarația inițială)
Tip rectificare TIPR C 1 Se completează cu următoarele caractere:
M - modificare sume, zile, CNP sau nume asigurat pentru asigurații raportați anterior,
A - adăugare asigurat nou
S - ștergere asigurat existent în declarația anterioară
Codurile de județe
Cod județ Denumire județ
011 Alba
021 Arad
031 Argeș
041 Bacău
051 Bihor
061 Bistrița
071 Botoșani
081 Brașov
091 Brăila
101 Buzău
111 Caraș Severin
121 Cluj
131 Constanța
141 Covasna
151 Dâmbovița
161 Dolj
171 Galați
181 Gorj
191 Harghita
201 Hunedoara
211 Ialomița
221 Iași
231 Giurgiu
241 Maramureș
251 Mehedinți
261 Mureș
271 Neamț
281 Olt
291 Prahova
301 Satu Mare
311 Sălaj
321 Sibiu
331 Suceava
341 Teleorman
351 Timiș
361 Tulcea
371 Vaslui
381 Vâlcea
391 Vrancea
401 Călărași
411 București
471 Ilfov
-------
