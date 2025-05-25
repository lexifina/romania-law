REGULAMENTUL DELEGAT (UE) 2025/855 AL COMISIEI
din 28 ianuarie 2025
de modificare a standardelor tehnice de reglementare prevăzute în Regulamentul delegat (UE) 2021/931 în ceea ce privește precizarea formulei pentru a calcula delta reglementat al opțiunilor call și put încadrate în categoria de risc de marfă
(Text cu relevanță pentru SEE)
COMISIA EUROPEANĂ,
având în vedere Tratatul privind funcționarea Uniunii Europene,
având în vedere Regulamentul (UE) nr. 575/2013 al Parlamentului European și al Consiliului din 26 iunie 2013 privind cerințele prudențiale pentru instituțiile de credit și de modificare a Regulamentului (UE) nr. 648/2012 (1), în special articolul 279a alineatul (3) al treilea paragraf,
întrucât:
(1) În conformitate cu articolul 279a alineatul (3) litera (a) din Regulamentul (UE) nr. 575/2013, formula pe care instituțiile trebuie să o utilizeze pentru a calcula delta reglementat al opțiunilor call și put încadrate în categoria de risc de marfă compatibilă cu condițiile de piață în care prețurile mărfurilor pot fi negative ar trebui, de asemenea, să fie specificată în conformitate cu evoluțiile internaționale în materie de reglementare, completând formula similară pentru opțiunile call și put încadrate în categoria de risc de rată a dobânzii.
(2) Capitolul CRE52 din Cadrul de la Basel, adoptat de Comitetul de la Basel pentru supraveghere bancară (BCBS) (2), stabilește abordarea standardizată pentru riscul de credit al contrapărții (SA-CCR). În capitolul respectiv, punctul 52.40 specifică formula pe care instituțiile trebuie să o utilizeze pentru a calcula delta reglementat al opțiunilor call și put încadrate într-o categorie de risc specifică. Întrebarea 2 de la acest punct 52.40 ridică problema modului în care trebuie calculat delta reglementat pentru opțiuni atunci când termenul P/K este zero sau negativ, astfel încât termenul ln(P/K) nu poate fi calculat, de exemplu într-un mediu cu rate negative ale dobânzii. În răspunsul BCBS la această întrebare se arată că, în astfel de cazuri, instituțiile de credit trebuie să utilizeze o formulă ușor diferită pentru a calcula delta reglementat al opțiunilor call și put, și anume ar trebui să includă în această formulă un factor de decalare a valorii de preț și a valorii de exercitare a opțiunilor în cauză prin adăugarea lambda („λ”), unde λ ar trebui să reprezinte cea mai mică măsură posibilă în care ratele dobânzii în moneda respectivă pot deveni negative. O abordare similară ar trebui urmată în cazul delta reglementat al opțiunilor call și put încadrate în categoria de risc de marfă, în situațiile în care prețurile mărfurilor pot fi negative. Factorul de decalare λ ar trebui să fie destul de mare pentru a permite instituțiilor de credit să calculeze delta reglementat al unei opțiuni încadrate în categoria de risc de marfă în conformitate cu formula prevăzută la articolul 279a alineatul (1) din Regulamentul (UE) nr. 575/2013, dar, în același timp, ar trebui să fie destul de mic pentru a nu introduce un element de subiectivitate inutil în rezultatul calculului delta reglementat.
(3) În concordanță cu abordarea prevăzută în Regulamentul delegat (UE) 2021/931 al Comisiei (3) pentru opțiunile încadrate în categoria de risc de rată a dobânzii, ar trebui utilizată valoarea volatilității reglementate pentru opțiunile put și call din categoria de risc de marfă, astfel cum este determinată în standardele internaționale adoptate de BCBS, deoarece este considerată adecvată pentru utilizarea sa în temeiul dreptului Uniunii.
(4) Prin urmare, Regulamentul delegat (UE) 2021/931 trebuie modificat în consecință.
(5) Prezentul regulament se bazează pe proiectele de standarde tehnice de reglementare prezentate Comisiei de Autoritatea Bancară Europeană.
(6) Autoritatea Bancară Europeană a organizat consultări publice deschise cu privire la proiectele de standarde tehnice de reglementare pe care se bazează prezentul regulament, a analizat costurile și beneficiile potențiale aferente și a solicitat avizul Grupului părților interesate din domeniul bancar instituit în conformitate cu articolul 37 din Regulamentul (UE) nr. 1093/2010 al Parlamentului European și al Consiliului (4),
ADOPTĂ PREZENTUL REGULAMENT:
Articolul 1
Regulamentul delegat (UE) 2021/931 se modifică după cum urmează:
1. La articolul 4 alineatul (4), teza introductivă se înlocuiește cu următorul text:
„4. Instituțiile care fie îndeplinesc condițiile prevăzute la articolul 94 alineatul (1) din Regulamentul (UE) nr. 575/2013, fie îndeplinesc condițiile prevăzute la articolul 325a alineatul (1) din regulamentul respectiv pot identifica cel mai semnificativ determinant de risc prin aplicarea următoarelor etape la inițierea tranzacției și, ulterior, cel puțin trimestrial:”.
2. Articolul 5 se modifică după cum urmează:
(a) la alineatul (1), teza introductivă se înlocuiește cu următorul text:
„(1) Instituțiile calculează delta reglementat (δ) al opțiunilor call și put, atunci când sunt încadrate în categoria de risc de rată a dobânzii sau în categoria de risc de marfă care este compatibilă cu condiții de piață în care ratele dobânzii sau prețurile mărfurilor pot fi negative, după cum urmează:”;
(b) alineatul (2) se înlocuiește cu următorul text:
„(2) În sensul alineatului (1), instituțiile calculează factorul de decalare (λ) pentru orice opțiune call și put după cum urmează:
λ j= | max{pragul j – min{P j, K j}, 0} dacă opțiunea j este încadrată în categoria de risc de rată a dobânzii;
max{ – (1 + pragul j)■min{P j, K j}, 0} dacă opțiunea j este încadrată în categoria de risc de marfă.
unde:
P j | = | prețul la vedere sau la termen al instrumentului-suport al opțiunii j;
K j | = | prețul de exercitare a opțiunii j;
pragul j= | 0,10 %, dacă opțiunea j este încadrată în categoria de risc de rată a dobânzii;
0,1, dacă opțiunea j este încadrată în categoria de risc de marfă.
”;
(c) la alineatul (3), tabelul se înlocuiește cu următorul text:
„Tabel
Categorie de risc | Instrumentul-suport | Volatilitatea reglementată
Rata dobânzii | Toate | 50 %
Marfă | Energia electrică | 150 %
Alte mărfuri (mai puțin energia electrică) | 70 %”
Articolul 2
Prezentul regulament intră în vigoare în a douăzecea zi de la data publicării în Jurnalul Oficial al Uniunii Europene.
Prezentul regulament este obligatoriu în toate elementele sale și se aplică direct în toate statele membre.
Adoptat la Bruxelles, 28 ianuarie 2025.
Pentru Comisie
Președinta
Ursula VON DER LEYEN
(1) JO L 176, 27.6.2013, p. 1, ELI: http://data.europa.eu/eli/reg/2013/575/oj.
(2) https://www.bis.org/basel_framework/chapter/CRE/52.htm?inforce=20230101&published=20200605.
(3) Regulamentul delegat (UE) 2021/931 al Comisiei din 1 martie 2021 de completare a Regulamentului (UE) nr. 575/2013 al Parlamentului European și al Consiliului în ceea ce privește standardele tehnice de reglementare care specifică metoda de identificare a tranzacțiilor cu instrumente financiare derivate cu unul sau mai mulți determinanți de risc semnificativi în sensul articolului 277 alineatul (5), formula pentru a calcula delta reglementat al opțiunilor call și put încadrate în categoria de risc de rată a dobânzii și metoda pentru a stabili dacă o tranzacție este o poziție lungă sau scurtă pe determinantul de risc principal sau pe cel mai semnificativ determinant de risc într-o anumită categorie de risc în sensul articolului 279a alineatul (3) literele (a) și (b) în cadrul abordării standardizate pentru riscul de credit al contrapărții (JO L 204, 10.6.2021, p. 7, ELI: http://data.europa.eu/eli/reg_del/2021/931/oj).
(4) Regulamentul (UE) nr. 1093/2010 al Parlamentului European și al Consiliului din 24 noiembrie 2010 de instituire a Autorității europene de supraveghere (Autoritatea bancară europeană), de modificare a Deciziei nr. 716/2009/CE și de abrogare a Deciziei 2009/78/CE a Comisiei (JO L 331, 15.12.2010, p. 12, ELI: http://data.europa.eu/eli/reg/2010/1093/oj).
ELI: http://data.europa.eu/eli/reg_del/2025/855/oj
