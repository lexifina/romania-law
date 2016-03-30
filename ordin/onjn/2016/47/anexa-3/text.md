# Anexa 3
CONȚINUTUL, RAPOARTELE ȘI ACCESUL la informații transmise de către organizatorii de jocuri de noroc la distanță, definite la art. 10 alin. (1) lit. h)-n) din Ordonanța de urgență a Guvernului nr. 77/2009, aprobată cu modificări și completări prin Legea nr. 246/2010, cu modificările și completările ulterioare, către Oficiul Național pentru Jocuri de Noroc ale serverului de siguranță Cerințe generale de raportare 1. Sistemul informatic central autorizat pentru organizatorul de jocuri de noroc la distanță va genera în momentul efectuării unei tranzacții (operațiuni) un raport cu informațiile solicitate. Raportul se va transmite în timp real în serverul de siguranță. 2. Prin tranzacție se înțelege orice înregistrare în sistemul informatic central al organizatorului care se referă la: - datele personale ale participantului la joc; - operațiunile financiare ale acestuia; - fiecare operațiune dintr-o sesiune de joc (include fiecare mână jucată, fiecare pariu plasat); și - aspectele referitoare la protecția jucătorului (autoexcluderea, excluderea etc.) aferente jucătorilor români sau jucătorilor care utilizează IP din România. 3. Organizatorul va asigura identitatea, autenticitatea, confidențialitatea și nonrepudierea datelor din serverul de siguranță. 4. Organizatorul va pune la dispoziția autorității modalitatea de verificare a semnăturii electronice și cheia de decriptare. 5. Organizatorul va pune la dispoziția autorității modalitatea prin care se poate verifica faptul că informația conținută pe acest server este completă și se regăsește în sistemul informatic central. Aceasta, precum și rapoartele stabilite privind funcționarea serverului de siguranță trebuie să poată fi accesibile din terminalul situat la Oficiul Național pentru Jocuri de Noroc. 6. Raportul va fi semnat cu semnătură electronică, conform prevederilor legale în vigoare (Legea nr. 455/2001 privind semnătura electronică, republicată). 7. Raportul generat va fi marcat temporal, conform prevederilor legale în vigoare (Legea nr. 451/2004 privind marca temporală). 8. După transmiterea datelor în serverul de siguranță, organizatorul de jocuri de noroc la distanță nu va mai avea posibilitatea modificării datelor transmise.
```
┌──────────────┬───────────────┬──────────┬─────────┬─────────────────────┬────────────────┬───────┬───────┬─────────────────────────────┬───────────────────┐
│   Tipul de   │               │ Subnivel │ Subnivel│                     │                │ Ocur. │ Ocur. │                             │                   │
│ înregistrare │   Câmpul      │ câmp 1   │  câmp 2 │ Declanșator generare│    Tip date    │  Min. │  Max. │  Descrierea câmpului        │      Exemplu      │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Bază comună   │               │          │         │                     │                │       │       │                             │                   │
│pentru toate  │               │          │         │Depinde de tipul     │                │       │       │                             │                   │
│înregistrările│               │          │         │înregistrării        │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │VersiuneFormat │          │         │                     │Număr întreg    │       │       │Versiunea modelului de date  │                   │
│              │               │          │         │                     │pozitiv         │   1   │   1   │utilizat. Aceasta permite    │                   │
│              │               │          │         │                     │                │       │       │implementarea ușoară a       │                   │
│              │               │          │         │                     │                │       │       │evoluțiilor formatului și    │                   │
│              │               │          │         │                     │                │       │       │coexistența diferitelor      │                   │
│              │               │          │         │                     │                │       │       │versiuni ale modelului în    │                   │
│              │               │          │         │                     │                │       │       │depozitul de date.           │ 1                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │IDÎnregistrare │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic înregistrarea. Două     │                   │
│              │               │          │         │                     │                │       │       │înregistrări din seif nu pot │                   │
│              │               │          │         │                     │                │       │       │avea în comun niciodată      │                   │
│              │               │          │         │                     │                │       │       │același ID de înregistrare.  │                   │
│              │               │          │         │                     │                │       │       │Operatorul va utiliza un     │254a26b5-5194-465d-│
│              │               │          │         │                     │                │       │       │UUID pentru acest câmp.      │b1c5-063231490d60  │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID operator    │          │         │                     │Șir de caractere│   1   │   1   │Acesta este ID-ul operato-   │                   │
│              │               │          │         │                     │                │       │       │rului care generează         │                   │
│              │               │          │         │                     │                │       │       │înregistrarea. Dacă un       │                   │
│              │               │          │         │                     │                │       │       │furnizor generează           │                   │
│              │               │          │         │                     │                │       │       │înregistrarea în numele unui │                   │
│              │               │          │         │                     │                │       │       │operator, este utilizat      │                   │
│              │               │          │         │                     │                │       │       │ID-ul operatorului. Acest ID │                   │
│              │               │          │         │                     │                │       │       │este oferit de autoritatea   │                   │
│              │               │          │         │                     │                │       │       │care a acordat o licență     │French_Operator    │
│              │               │          │         │                     │                │       │       │acestui operator.            │(operator francez) │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID Generator   │          │         │                     │                │       │       │Dacă operatorul a generat    │                   │
│              │Înregistrare   │          │         │                     │Șir de caractere│   0   │   1   │înregistrarea, acest câmp    │                   │
│              │               │          │         │                     │                │       │       │este absent. În caz contrar, │                   │
│              │               │          │         │                     │                │       │       │acesta este ID-ul furnizo-   │                   │
│              │               │          │         │                     │                │       │       │rului care generează         │                   │
│              │               │          │         │                     │                │       │       │înregistrarea. Valoarea      │                   │
│              │               │          │         │                     │                │       │       │acestui ID este aleasă de    │Network_Operator   │
│              │               │          │         │                     │                │       │       │furnizor.                    │(operator rețea)   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Dată extracție │          │         │                     │Dată oră        │   1   │   1   │Aceasta este ora la care a   │                   │
│              │               │          │         │                     │                │       │       │fost creată înregistrarea    │                   │
│              │               │          │         │                     │                │       │       │(adică ora la care a fost    │                   │
│              │               │          │         │                     │                │       │       │extrasă din sistemul         │                   │
│              │               │          │         │                     │                │       │       │informatic). Aceasta NU este │                   │
│              │               │          │         │                     │                │       │       │ora la care înregistrarea    │                   │
│              │               │          │         │                     │                │       │       │este trimisă sau înregistrată│                   │
│              │               │          │         │                     │                │       │       │în seif. Se va utiliza UTC   │                   │
│              │               │          │         │                     │                │       │       │pentru a preveni DST și alte │2011-10-           │
│              │               │          │         │                     │                │       │       │probleme.                    │04T19:53:51.346Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Marcaj         │          │         │                     │                │       │       │Acest câmp opțional este     │                   │
│              │corectare      │          │         │                     │Bool            │   0   │   1   │utilizat numai atunci când   │                   │
│              │               │          │         │                     │                │       │       │înregistrarea curentă        │                   │
│              │               │          │         │                     │                │       │       │înlocuiește sau anulează o   │                   │
│              │               │          │         │                     │                │       │       │înregistrare anterioară      │                   │
│              │               │          │         │                     │                │       │       │trimisă incorect. În acest   │                   │
│              │               │          │         │                     │                │       │       │caz, înregistrarea nouă      │                   │
│              │               │          │         │                     │                │       │       │corectă utilizează același   │                   │
│              │               │          │         │                     │                │       │       │ID înregistrare și acest     │                   │
│              │               │          │         │                     │                │       │       │câmp este setat ca fiind     │                   │
│              │               │          │         │                     │                │       │       │"adevărat". Aceasta este     │                   │
│              │               │          │         │                     │                │       │       │singura excepție când poate  │                   │
│              │               │          │         │                     │                │       │       │fi reutilizat ID             │                   │
│              │               │          │         │                     │                │       │       │înregistrare.                │                   │
│              │               │          │         │                     │                │       │       │Fișierul poate fi identificat│                   │
│              │               │          │         │                     │                │       │       │în continuare în mod unic    │                   │
│              │               │          │         │                     │                │       │       │prin intermediul perechii    │                   │
│              │               │          │         │                     │                │       │       │ID înregistrare și Dată      │                   │
│              │               │          │         │                     │                │       │       │extracție. Pentru a anula o  │                   │
│              │               │          │         │                     │                │       │       │înregistrare este trimisă o  │                   │
│              │               │          │         │                     │                │       │       │înregistrare "goală", care   │                   │
│              │               │          │         │                     │                │       │       │conține numai elementele din │                   │
│              │               │          │         │                     │                │       │       │această secțiune (bază comună│                   │
│              │               │          │         │                     │                │       │       │pentru toate înregistrările).│fals               │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Detalii       │               │          │         │La înregistrarea     │                │       │       │                             │                   │
│jucător       │               │          │         │jucătorului și când  │                │       │       │                             │                   │
│              │               │          │         │se modifică          │                │       │       │                             │                   │
│              │               │          │         │informații           │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Prenume        │          │         │Înregistrare         │Șir de caractere│   1   │   1   │Prenumele jucătorului în curs│                   │
│              │               │          │         │                     │                │       │       │de înregistrare. Dacă        │                   │
│              │               │          │         │                     │                │       │       │prenumele jucătorului este   │                   │
│              │               │          │         │                     │                │       │       │compus, prenumele vor fi     │                   │
│              │               │          │         │                     │                │       │       │separate prin "-" (cratimă). │                   │
│              │               │          │         │                     │                │       │       │Dacă jucătorul are un al     │                   │
│              │               │          │         │                     │                │       │       │doilea prenume sau mai multe │                   │
│              │               │          │         │                     │                │       │       │prenume, toate trebuie       │                   │
│              │               │          │         │                     │                │       │       │indicate și separate prin    │                   │
│              │               │          │         │                     │                │       │       │" " (spațiu unic).           │Ion Marian Popescu │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Nume           │          │         │Înregistrare         │Șir de caractere│   1   │   1   │Acest câmp conține numele de │                   │
│              │               │          │         │                     │                │       │       │familie al jucătorului. Dacă │                   │
│              │               │          │         │                     │                │       │       │jucătorul are mai multe nume │                   │
│              │               │          │         │                     │                │       │       │de familie, toate trebuie    │                   │
│              │               │          │         │                     │                │       │       │indicate și separate prin    │                   │
│              │               │          │         │                     │                │       │       │" " (spațiu unic). Numele de │                   │
│              │               │          │         │                     │                │       │       │familie este cel utilizat în │                   │
│              │               │          │         │                     │                │       │       │mod curent în documentele    │                   │
│              │               │          │         │                     │                │       │       │oficiale de identitate și    │                   │
│              │               │          │         │                     │                │       │       │poate fi diferit de numele de│                   │
│              │               │          │         │                     │                │       │       │la data nașterii.            │Ion Barbu          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data nașterii  │          │         │Înregistrare         │Data            │   1   │   1   │Data nașterii jucătorului    │1895-03-18         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │CNP            │          │         │Înregistrare         │Număr           │   1   │   1   │Acest câmp conține codul     │                   │
│              │               │          │         │                     │                │       │       │numeric personal pentru      │                   │
│              │               │          │         │                     │                │       │       │cetățenii români.            │1900806182888      │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Rezidență      │          │         │                     │                │       │       │Rezidență fiscală a          │                   │
│              │fiscală        │          │         │Înregistrare         │Șir de caractere│   1   │   1   │jucătorului                  │România            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Stradă/număr   │          │         │Înregistrarea și     │                │       │       │Aceasta este strada și       │                   │
│              │               │          │         │schimbarea adresei   │Șir de caractere│   1   │   1   │numărul clădirii principa-   │                   │
│              │               │          │         │                     │                │       │       │lului domiciliu al           │                   │
│              │               │          │         │                     │                │       │       │jucătorului, așa cum apare   │                   │
│              │               │          │         │                     │                │       │       │în documentele sale de       │Strada Narciselor  │
│              │               │          │         │                     │                │       │       │identitate.                  │nr. 3              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Cod poștal     │          │         │Înregistrarea și     │                │       │       │Acesta este codul poștal al  │                   │
│              │               │          │         │schimbarea adresei   │Număr           │   1   │   1   │principalului domiciliu al   │                   │
│              │               │          │         │                     │                │       │       │jucătorului, așa cum apare în│                   │
│              │               │          │         │                     │                │       │       │documentele sale de          │                   │
│              │               │          │         │                     │                │       │       │identitate. Codul poate să   │                   │
│              │               │          │         │                     │                │       │       │conțină litere și alte       │                   │
│              │               │          │         │                     │                │       │       │caractere (deoarece jucătorul│                   │
│              │               │          │         │                     │                │       │       │poate locui în altă țară).   │96541              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Localitate     │          │         │Înregistrarea și     │                │       │       │Aceasta este localitatea     │                   │
│              │               │          │         │schimbarea adresei   │Șir de caractere│   1   │   1   │principalului domiciliu al   │                   │
│              │               │          │         │                     │                │       │       │jucătorului, așa cum apare în│                   │
│              │               │          │         │                     │                │       │       │documentele sale de          │                   │
│              │               │          │         │                     │                │       │       │identitate.                  │București          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Țara           │          │         │Înregistrarea și     │                │       │       │Acesta este codul ISO 3166-1 │                   │
│              │               │          │         │schimbarea adresei   │Șir de caractere│   0   │   1   │(ALPHA-2) al țării principa- │                   │
│              │               │          │         │                     │                │       │       │lului domiciliu al           │                   │
│              │               │          │         │                     │                │       │       │jucătorului, așa cum apare în│                   │
│              │               │          │         │                     │                │       │       │documentele sale de          │                   │
│              │               │          │         │                     │                │       │       │identitate. Acest câmp este  │                   │
│              │               │          │         │                     │                │       │       │obligatoriu dacă jucătorul   │                   │
│              │               │          │         │                     │                │       │       │nu locuiește în țară.        │RO                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID jucător     │          │         │Înregistrare         │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │                   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │personale.                   │9965-facbcc23542   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data creării   │          │         │                     │                │       │       │Acestea sunt data și ora     │2011-10-04T19:     │
│              │contului       │          │         │                     │DatăOră         │   1   │   1   │creării contului jucătorului.│44:51.346Z         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Stare internă  │          │         │                     │                │       │       │                             │                   │
│              │cont           │          │         │                     │                │   1   │   1   │                             │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Situație  │         │                     │Șir de caractere│       │       │Aceasta este situația        │                   │
│              │               │          │         │                     │(enumerare)     │   1   │   1   │contului de jucător în       │                   │
│              │               │          │         │                     │                │       │       │sistemul informatic al       │                   │
│              │               │          │         │                     │                │       │       │operatorului. Poate avea una │                   │
│              │               │          │         │                     │                │       │       │din următoarele valori:      │                   │
│              │               │          │         │                     │                │       │       │- "preliminar": jucătorul a  │                   │
│              │               │          │         │                     │                │       │       │înregistrat un cont temporar,│                   │
│              │               │          │         │                     │                │       │       │însă încă nu a fost verificat│                   │
│              │               │          │         │                     │                │       │       │complet;                     │                   │
│              │               │          │         │                     │                │       │       │- "activ": jucătorul a fost  │                   │
│              │               │          │         │                     │                │       │       │confirmat și poate retrage   │                   │
│              │               │          │         │                     │                │       │       │bani din contul de jucător;  │                   │
│              │               │          │         │                     │                │       │       │- "suspendat": jucătorul nu  │                   │
│              │               │          │         │                     │                │       │       │are temporar permisiunea de a│                   │
│              │               │          │         │                     │                │       │       │juca și de a retrage bani (de│                   │
│              │               │          │         │                     │                │       │       │obicei, în timpul unei       │                   │
│              │               │          │         │                     │                │       │       │anchete);                    │                   │
│              │               │          │         │                     │                │       │       │- "închis": jucătorul a      │                   │
│              │               │          │         │                     │                │       │       │solicitat închiderea contului│                   │
│              │               │          │         │                     │                │       │       │său sau în prezent se află pe│                   │
│              │               │          │         │                     │                │       │       │lista de excluderi. Este     │                   │
│              │               │          │         │                     │                │       │       │posibil, de asemenea, ca     │                   │
│              │               │          │         │                     │                │       │       │operatorul să fi hotărât să  │                   │
│              │               │          │         │                     │                │       │       │închidă contul.              │activ              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Data      │         │                     │DatăOră         │   1   │   1   │Data și ora celei mai recente│                   │
│              │               │          │         │                     │                │       │       │modificări a situației       │2011-10-           │
│              │               │          │         │                     │                │       │       │jucătorului. UTC             │04T19:44:51.346Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Soldul        │               │          │         │O dată pe săptămână  │                │       │       │                             │                   │
│contului de   │               │          │         │sau o dată pe lună   │                │       │       │                             │                   │
│jucător       │               │          │         │pentru toate         │                │       │       │                             │                   │
│              │               │          │         │conturile de jucători│                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID jucător     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │                   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat   │                   │
│              │               │          │         │                     │                │       │       │în toate evidențele care     │                   │
│              │               │          │         │                     │                │       │       │țin de jucător și nu este    │                   │
│              │               │          │         │                     │                │       │       │modificat niciodată în timpul│                   │
│              │               │          │         │                     │                │       │       │vieții utile a contului.     │                   │
│              │               │          │         │                     │                │       │       │IDJucător nu se modifică,    │                   │
│              │               │          │         │                     │                │       │       │indiferent dacă jucătorul    │                   │
│              │               │          │         │                     │                │       │       │își schimbă pseudonimul      │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │sau datele personale.        │9965-facbcc23542   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Cont           │          │         │                     │                │   1   │neaso- │Lista tuturor conturilor și  │                   │
│              │               │          │         │                     │                │       │ciat   │portofelelor deținute de un  │                   │
│              │               │          │         │                     │                │       │       │jucător prin operatorul său. │                   │
│              │               │          │         │                     │                │       │       │Dacă sunt utilizate, "bani   │                   │
│              │               │          │         │                     │                │       │       │reali", "bani bonus" și      │                   │
│              │               │          │         │                     │                │       │       │"puncte revendicabile" sunt  │                   │
│              │               │          │         │                     │                │       │       │urmărite în calitate de      │                   │
│              │               │          │         │                     │                │       │       │conturi separate. Dacă un    │                   │
│              │               │          │         │                     │                │       │       │operator utilizează alte     │                   │
│              │               │          │         │                     │                │       │       │tipuri de portofele, acestea │                   │
│              │               │          │         │                     │                │       │       │vor fi urmărite, de asemenea │                   │
│              │               │          │         │                     │                │       │       │(de exemplu, bani care pot   │                   │
│              │               │          │         │                     │                │       │       │fi utilizați numai pentru    │                   │
│              │               │          │         │                     │                │       │       │sloturi).                    │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │                │       │       │Descrierea contului/         │                   │
│              │               │contului  │         │                     │Șir de caractere│   1   │   1   │portofelului Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│Cont bonus         │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │(Nu poate fi       │
│              │               │          │         │                     │                │       │       │descriere.                   │retras.)           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte existente în │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale             │36.231             │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Plafon    │         │                     │Zecimal         │   1   │   1   │Sumă totală de bani reali pe │                   │
│              │               │          │         │                     │                │       │       │care un jucător îi poate avea│                   │
│              │               │          │         │                     │                │       │       │în cont, cu o precizie de cel│                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale.            │36.231             │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │bonus COP          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Rezumat la    │               │          │         │O dată pe zi, pentru │                │       │       │                             │                   │
│sfârșitul     │               │          │         │fiecare tip de joc și│                │       │       │                             │                   │
│zilei         │               │          │         │monedă oferită de    │                │       │       │                             │                   │
│              │               │          │         │operator (chiar dacă │                │       │       │                             │                   │
│              │               │          │         │nimeni nu a jucat    │                │       │       │                             │                   │
│              │               │          │         │jocul în ziua        │                │       │       │                             │                   │
│              │               │          │         │respectivă). Pot     │                │       │       │                             │                   │
│              │               │          │         │exista câteva        │                │       │       │                             │                   │
│              │               │          │         │rezumate zilnice     │                │       │       │                             │                   │
│              │               │          │         │pentru aceeași       │                │       │       │                             │                   │
│              │               │          │         │categorie și monedă, │                │       │       │                             │                   │
│              │               │          │         │astfel încât         │                │       │       │                             │                   │
│              │               │          │         │furnizorii pot oferi │                │       │       │                             │                   │
│              │               │          │         │această înregistrare │                │       │       │                             │                   │
│              │               │          │         │în numele            │                │       │       │                             │                   │
│              │               │          │         │operatorului.        │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Categoria      │          │         │                     │Șir de caractere│       │       │Aceasta este categoria sau   │                   │
│              │jocului        │          │         │                     │(enumerare)     │   1   │   1   │tipul jocului, conform       │                   │
│              │               │          │         │                     │                │       │       │descrierii și autorizării    │                   │
│              │               │          │         │                     │                │       │       │prin lege (de exemplu,       │                   │
│              │               │          │         │                     │                │       │       │"poker", "blackjack",        │                   │
│              │               │          │         │                     │                │       │       │"pariu", "altele" etc.)      │                   │
│              │               │          │         │                     │                │       │       │Valoarea depinde exclusiv de │                   │
│              │               │          │         │                     │                │       │       │setările predefinite.        │poker              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Monedă         │          │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │EUR                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Numărul de     │          │         │                     │Număr întreg    │       │       │Număr de jucători care au    │                   │
│              │jucători       │          │         │                     │pozitiv         │   1   │   1   │jucat cel puțin un joc de    │                   │
│              │               │          │         │                     │                │       │       │acest tip în timpul          │                   │
│              │               │          │         │                     │                │       │       │perioadei. Poate fi "0".     │74                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Numărul de     │          │         │                     │Număr întreg    │       │       │Număr de runde/mâini/        │                   │
│              │jocuri         │          │         │                     │pozitiv         │   1   │   1   │învârtiri sau sesiuni jucate │                   │
│              │               │          │         │                     │                │       │       │în cadrul perioadei          │36521              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Bani pariați   │          │         │                     │Zecimal         │   1   │   1   │Sumă totală de bani pariați  │                   │
│              │               │          │         │                     │                │       │       │de jucători pentru tipul de  │                   │
│              │               │          │         │                     │                │       │       │joc din perioadă (excluzând  │                   │
│              │               │          │         │                     │                │       │       │contribuțiile la jackpoturi).│                   │
│              │               │          │         │                     │                │       │       │Poate fi "0". Aceasta nu este│                   │
│              │               │          │         │                     │                │       │       │suma pierdută de jucători.   │                   │
│              │               │          │         │                     │                │       │       │Pentru pariuri descrie suma  │                   │
│              │               │          │         │                     │                │       │       │tuturor pariurilor plasate,  │                   │
│              │               │          │         │                     │                │       │       │chiar dacă nu au fost decise.│56412354           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Contribuții la │          │         │                     │                │       │       │Sumă totală de bani cu care  │                   │
│              │jackpoturi     │          │         │                     │Zecimal         │   1   │   1   │jucătorii contribuie la      │                   │
│              │               │          │         │                     │                │       │       │jackpoturi pentru tipul de   │                   │
│              │               │          │         │                     │                │       │       │joc din perioadă. Poate fi   │                   │
│              │               │          │         │                     │                │       │       │"0". Nu descrie câștigurile  │                   │
│              │               │          │         │                     │                │       │       │din jackpoturi, ci numai     │                   │
│              │               │          │         │                     │                │       │       │contribuțiile.               │23651              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Câștiguri      │          │         │                     │Zecimal         │   1   │   1   │Sumă totală de bani câștigați│                   │
│              │               │          │         │                     │                │       │       │de jucători pentru tipul de  │                   │
│              │               │          │         │                     │                │       │       │joc din perioadă. Poate fi   │                   │
│              │               │          │         │                     │                │       │       │"0". Pentru pariuri descrie  │                   │
│              │               │          │         │                     │                │       │       │suma tuturor pariurilor      │                   │
│              │               │          │         │                     │                │       │       │câștigate în cadrul          │                   │
│              │               │          │         │                     │                │       │       │perioadei, chiar dacă au fost│                   │
│              │               │          │         │                     │                │       │       │plasate înainte de începerea │                   │
│              │               │          │         │                     │                │       │       │perioadei.                   │1235465            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │GGR            │          │         │                     │Zecimal         │   1   │   1   │Suma totală a banilor primiți│                   │
│              │               │          │         │                     │                │       │       │de operator din acest tip de │                   │
│              │               │          │         │                     │                │       │       │joc în cadrul perioadei.     │                   │
│              │               │          │         │                     │                │       │       │Poate fi negativă            │5434556            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Soldul        │               │          │         │                     │                │       │       │                             │                   │
│contului      │               │          │         │O dată pe lună pentru│                │       │       │                             │                   │
│jackpot       │               │          │         │fiecare jackpot      │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Descriere      │          │         │                     │                │       │       │Aceasta este o descriere a   │                   │
│              │jackpot        │          │         │                     │Șir de caractere│    1  │   1   │jackpotului, așa cum este    │                   │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │                   │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│                   │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │                   │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │                   │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │Jackpot de poker   │
│              │               │          │         │                     │                │       │       │are descrierea sa.           │"bad beat"         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data resetării │          │         │                     │DatăOră         │   1   │   1   │Data și ora la care a început│                   │
│              │               │          │         │                     │                │       │       │jackpotul sau la care s-a    │2011-10-           │
│              │               │          │         │                     │                │       │       │declanșat ultima oară        │04T19:44:51.346Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Cont           │          │         │                     │                │   1   │neaso- │Lista tuturor conturilor     │                   │
│              │               │          │         │                     │                │       │ciat   │jackpotului. De exemplu,     │                   │
│              │               │          │         │                     │                │       │       │jackpotul poate avea un cont │                   │
│              │               │          │         │                     │                │       │       │pe "bani reali" și un cont pe│                   │
│              │               │          │         │                     │                │       │       │"bani bonus", care sunt      │                   │
│              │               │          │         │                     │                │       │       │transferate ambele           │                   │
│              │               │          │         │                     │                │       │       │jucătorului care declanșează │                   │
│              │               │          │         │                     │                │       │       │jackpotul.                   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │                │       │       │Descrierea contului          │                   │
│              │               │contului  │         │                     │Șir de caractere│   1   │   1   │jackpotului                  │Cont pe bani reali │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte existente în │                   │
│              │               │          │         │                     │                │       │       │contul de jackpot, cu o      │                   │
│              │               │          │         │                     │                │       │       │precizie de cel puțin 2      │                   │
│              │               │          │         │                     │                │       │       │zecimale                     │36.231             │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │bonus COP          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Tranzacție    │               │          │         │Aproape în timp real,│                │       │       │                             │                   │
│care nu ține  │               │          │         │când are loc o       │                │       │       │                             │                   │
│de jocurile   │               │          │         │tranzacție           │                │       │       │                             │                   │
│de noroc      │               │          │         │neimplicată în cadrul│                │       │       │                             │                   │
│              │               │          │         │jocului (atribuirea  │                │       │       │                             │                   │
│              │               │          │         │unui bonus,          │                │       │       │                             │                   │
│              │               │          │         │transformarea unui   │                │       │       │                             │                   │
│              │               │          │         │bonus etc.)          │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID tranzacție  │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic tranzacția neimplicată  │                   │
│              │               │          │         │                     │                │       │       │în cadrul jocului. Două      │                   │
│              │               │          │         │                     │                │       │       │tranzacții din seif nu pot   │                   │
│              │               │          │         │                     │                │       │       │avea în comun niciodată      │                   │
│              │               │          │         │                     │                │       │       │același IDTranzacție.        │                   │
│              │               │          │         │                     │                │       │       │Operatorul va utiliza un UUID│254a26b5-5194-465d-│
│              │               │          │         │                     │                │       │       │pentru acest câmp.           │b1c5-063231490d60  │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Descrierea     │          │         │                     │                │       │       │Aceasta este o descriere a   │                   │
│              │tranzacției    │          │         │                     │Șir de caractere│   1   │   1   │tranzacției neimplicate în   │                   │
│              │               │          │         │                     │                │       │       │cadrul unui joc (de exemplu, │                   │
│              │               │          │         │                     │                │       │       │"retragere", "depunere",     │                   │
│              │               │          │         │                     │                │       │       │"conversie de bani bonus în  │                   │
│              │               │          │         │                     │                │       │       │bani reali"). Aceasta poate  │                   │
│              │               │          │         │                     │                │       │       │fi și o încasare automată    │                   │
│              │               │          │         │                     │                │       │       │declanșată de operator,      │                   │
│              │               │          │         │                     │                │       │       │deoarece contul de bani reali│                   │
│              │               │          │         │                     │                │       │       │al jucătorului a depășit un  │                   │
│              │               │          │         │                     │                │       │       │anumit plafon.               │depunere           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data           │          │         │                     │DatăOră         │   1   │   1   │Data și ora la care a avut   │2011-10-           │
│              │               │          │         │                     │                │       │       │loc tranzacția               │04T19:44:51.346Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Cont debitat   │          │         │                     │                │   1   │   1   │Contul care a fost debitat   │                   │
│              │               │          │         │                     │                │       │       │în timpul tranzacției        │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID jucător│         │                     │Șir de caractere│   0   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │                   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │                   │
│              │               │          │         │                     │                │       │       │personale. Acest câmp este   │                   │
│              │               │          │         │                     │                │       │       │opțional, deoarece contul    │                   │
│              │               │          │         │                     │                │       │       │debitat poate fi un cont     │                   │
│              │               │          │         │                     │                │       │       │(virtual) al operatorului,   │                   │
│              │               │          │         │                     │                │       │       │de exemplu, atunci când      │                   │
│              │               │          │         │                     │                │       │       │operatorul atribuie bani     │                   │
│              │               │          │         │                     │                │       │       │bonus sau puncte de          │                   │
│              │               │          │         │                     │                │       │       │loialitate. Trebuie          │                   │
│              │               │          │         │                     │                │       │       │furnizat fie IDJucător, fie  │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │IDOperator.                  │9965-facbcc23542   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID        │         │                     │Șir de caractere│   0   │    1  │Acest câmp identifică în mod │French_Operator    │
│              │               │operator  │         │                     │                │       │       │unic operatorul al cărui cont│(operator francez) │
│              │               │          │         │                     │                │       │       │(virtual) este debitat, de   │                   │
│              │               │          │         │                     │                │       │       │exemplu, când operatorul     │                   │
│              │               │          │         │                     │                │       │       │atribuie puncte bonus.       │                   │
│              │               │          │         │                     │                │       │       │Acesta este utilizat, de     │                   │
│              │               │          │         │                     │                │       │       │asemenea, în cadrul jocurilor│                   │
│              │               │          │         │                     │                │       │       │în rețea, când portofelul    │                   │
│              │               │          │         │                     │                │       │       │unui jucător este transferat │                   │
│              │               │          │         │                     │                │       │       │către și de la operatorul de │                   │
│              │               │          │         │                     │                │       │       │rețea. Trebuie furnizat fie  │                   │
│              │               │          │         │                     │                │       │       │IDJucător, fie IDOperator.   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Jurisdic- │         │                     │Șir de caractere│   0   │    1  │Aceasta este jurisdicția în  │România            │
│              │               │ția opera-│         │                     │                │       │       │care activează operatorul al │                   │
│              │               │torului   │         │                     │                │       │       │cărui cont (virtual) este    │                   │
│              │               │          │         │                     │                │       │       │debitat.                     │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │    1  │Descrierea contului/         │Moneybookers       │
│              │               │contului  │         │                     │                │       │       │portofelului. Aceasta este   │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. În timpul unei    │                   │
│              │               │          │         │                     │                │       │       │depuneri, acesta poate fi    │                   │
│              │               │          │         │                     │                │       │       │contul bancar al jucătorului.│                   │
│              │               │          │         │                     │                │       │       │Când sunt utilizați furnizori│                   │
│              │               │          │         │                     │                │       │       │de bani virtuali sau carduri │                   │
│              │               │          │         │                     │                │       │       │preplătite, este inclusă și  │                   │
│              │               │          │         │                     │                │       │       │denumirea sistemului.        │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale             │10,00              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │USD                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Cont creditat  │          │         │                     │                │   1   │   1   │Contul care a fost creditat  │                   │
│              │               │          │         │                     │                │       │       │în timpul tranzacției        │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID jucător│         │                     │Șir de caractere│   0   │   1   │Acest câmp identifică în mod │328ad861-25cb-6437 │
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │-9965-facbcc23542  │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat   │                   │
│              │               │          │         │                     │                │       │       │în toate evidențele care țin │                   │
│              │               │          │         │                     │                │       │       │de jucător și nu este        │                   │
│              │               │          │         │                     │                │       │       │modificat niciodată în timpul│                   │
│              │               │          │         │                     │                │       │       │vieții utile a contului.     │                   │
│              │               │          │         │                     │                │       │       │IDJucător nu se modifică,    │                   │
│              │               │          │         │                     │                │       │       │indiferent dacă jucătorul își│                   │
│              │               │          │         │                     │                │       │       │schimbă pseudonimul sau      │                   │
│              │               │          │         │                     │                │       │       │datele personale.            │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional,    │                   │
│              │               │          │         │                     │                │       │       │deoarece contul creditat     │                   │
│              │               │          │         │                     │                │       │       │poate fi un cont (virtual) al│                   │
│              │               │          │         │                     │                │       │       │operatorului, de exemplu,    │                   │
│              │               │          │         │                     │                │       │       │atunci când jucătorul cumpără│                   │
│              │               │          │         │                     │                │       │       │un tricou din magazinul      │                   │
│              │               │          │         │                     │                │       │       │operatorului. Dacă nu este   │                   │
│              │               │          │         │                     │                │       │       │furnizat IDJucător, este     │                   │
│              │               │          │         │                     │                │       │       │obligatorie furnizarea       │                   │
│              │               │          │         │                     │                │       │       │IDOperator.                  │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID        │         │                     │Șir de caractere│   0   │   1   │Acest câmp identifică în mod │French_Operator    │
│              │               │operator  │         │                     │                │       │       │unic operatorul al cărui cont│(operator francez) │
│              │               │          │         │                     │                │       │       │(virtual) este creditat, de  │                   │
│              │               │          │         │                     │                │       │       │exemplu, când operatorul     │                   │
│              │               │          │         │                     │                │       │       │primește un portofel de      │                   │
│              │               │          │         │                     │                │       │       │jucător de la alt operator.  │                   │
│              │               │          │         │                     │                │       │       │Dacă IDJucător este deținut  │                   │
│              │               │          │         │                     │                │       │       │de alt operator, acest câmp  │                   │
│              │               │          │         │                     │                │       │       │trebuie completat, de        │                   │
│              │               │          │         │                     │                │       │       │asemenea.                    │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Jurisdic- │         │                     │Șir de caractere│   0   │   1   │Dacă operatorul nu deține    │România            │
│              │               │ția opera-│         │                     │                │       │       │licență în această           │                   │
│              │               │torului   │         │                     │                │       │       │jurisdicție, acest câmp      │                   │
│              │               │          │         │                     │                │       │       │conține jurisdicția în care  │                   │
│              │               │          │         │                     │                │       │       │activează operatorul al cărui│                   │
│              │               │          │         │                     │                │       │       │cont (virtual) este creditat.│                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │cont pe bani reali │
│              │               │contului  │         │                     │                │       │       │portofelului. Aceasta este   │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. În timpul unei    │                   │
│              │               │          │         │                     │                │       │       │retrageri, acesta este contul│                   │
│              │               │          │         │                     │                │       │       │bancar al jucătorului. Când  │                   │
│              │               │          │         │                     │                │       │       │sunt utilizați furnizori de  │                   │
│              │               │          │         │                     │                │       │       │bani virtuali sau carduri    │                   │
│              │               │          │         │                     │                │       │       │preplătite, este inclusă și  │                   │
│              │               │          │         │                     │                │       │       │denumirea sistemului.        │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate în │25321,02           │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. Suma poate │                   │
│              │               │          │         │                     │                │       │       │fi diferită din contul       │                   │
│              │               │          │         │                     │                │       │       │debitat, dacă operațiunea    │                   │
│              │               │          │         │                     │                │       │       │este o conversie între două  │                   │
│              │               │          │         │                     │                │       │       │tipuri de unități (dintr-o   │                   │
│              │               │          │         │                     │                │       │       │monedă în alta, de puncte de │                   │
│              │               │          │         │                     │                │       │       │fidelitate în puncte bonus). │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│COP                │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu,      │                   │
│              │               │          │         │                     │                │       │       │"bani bonus"). Acest câmp    │                   │
│              │               │          │         │                     │                │       │       │este opțional dacă contul    │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Joc de ring   │               │          │         │Aproape în timp real │                │       │       │                             │                   │
│(de exemplu,  │               │          │         │după fiecare rundă   │                │       │       │                             │                   │
│joc de poker  │               │          │         │(de exemplu, după    │                │       │       │                             │                   │
│pe numerar)   │               │          │         │fiecare mână în cazul│                │       │       │                             │                   │
│              │               │          │         │jocului de poker)    │                │       │       │                             │                   │
│              │               │          │         │sau după fiecare     │                │       │       │                             │                   │
│              │               │          │         │sesiune              │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID sesiune     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │254a26b5-5194-465d-│
│              │               │          │         │                     │                │       │       │unic runda sau sesiunea      │b1c5-063231490d60  │
│              │               │          │         │                     │                │       │       │jocului. Două runde/sesiuni  │                   │
│              │               │          │         │                     │                │       │       │din seif nu pot avea         │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDRundă    │                   │
│              │               │          │         │                     │                │       │       │(chiar și pentru tipuri de   │                   │
│              │               │          │         │                     │                │       │       │jocuri diferite). Operatorul │                   │
│              │               │          │         │                     │                │       │       │va utiliza un UUID pentru    │                   │
│              │               │          │         │                     │                │       │       │acest câmp.                  │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Categoria      │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este categoria sau   │poker              │
│              │jocului        │          │         │                     │(enumerare)     │       │       │tipul jocului, conform       │                   │
│              │               │          │         │                     │                │       │       │descrierii și autorizării    │                   │
│              │               │          │         │                     │                │       │       │prin lege (de exemplu,       │                   │
│              │               │          │         │                     │                │       │       │"poker", "blackjack",        │                   │
│              │               │          │         │                     │                │       │       │"pariu", "altele" etc.)      │                   │
│              │               │          │         │                     │                │       │       │Valoarea depinde exclusiv de │                   │
│              │               │          │         │                     │                │       │       │setările predefinite.        │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Denumire       │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Poker Texas Hold'em│
│              │comercială a   │          │         │                     │                │       │       │jocului, așa cum este afișată│no limit           │
│              │jocului        │          │         │                     │                │       │       │pentru jucător. Pentru acest │                   │
│              │               │          │         │                     │                │       │       │joc specific este utilizat un│                   │
│              │               │          │         │                     │                │       │       │ID, care este comun pentru   │                   │
│              │               │          │         │                     │                │       │       │toți jucătorii care joacă    │                   │
│              │               │          │         │                     │                │       │       │jocul respectiv.             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jucători       │          │         │                     │                │   1   │neaso- │Toți jucătorii care participă│                   │
│              │               │          │         │                     │                │       │ciat   │la această rundă de joc sunt │       -           │
│              │               │          │         │                     │                │       │       │enumerați aici.              │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID jucător│         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │9965-facbcc23542   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │                   │
│              │               │          │         │                     │                │       │       │personale.                   │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional,    │                   │
│              │               │          │         │                     │                │       │       │deoarece contul creditat     │                   │
│              │               │          │         │                     │                │       │       │poate fi un cont (virtual)   │                   │
│              │               │          │         │                     │                │       │       │al operatorului, de exemplu, │                   │
│              │               │          │         │                     │                │       │       │atunci când jucătorul        │                   │
│              │               │          │         │                     │                │       │       │cumpără un tricou din        │                   │
│              │               │          │         │                     │                │       │       │magazinul operatorului.      │                   │
│              │               │          │         │                     │                │       │       │Dacă nu este furnizat        │                   │
│              │               │          │         │                     │                │       │       │IDJucător, este obligatorie  │                   │
│              │               │          │         │                     │                │       │       │furnizarea IDOperator.       │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID        │         │                     │Șir de caractere│   0   │   1   │Acest câmp identifică în mod │French_Operator    │
│              │               │operator  │         │                     │                │       │       │unic operatorul al cărui cont│(operator francez) │
│              │               │          │         │                     │                │       │       │(virtual) este creditat, de  │                   │
│              │               │          │         │                     │                │       │       │exemplu, când operatorul     │                   │
│              │               │          │         │                     │                │       │       │primește un portofel de      │                   │
│              │               │          │         │                     │                │       │       │jucător de la alt operator.  │                   │
│              │               │          │         │                     │                │       │       │Dacă IDJucător este deținut  │                   │
│              │               │          │         │                     │                │       │       │de alt operator, acest câmp  │                   │
│              │               │          │         │                     │                │       │       │trebuie completat, de        │                   │
│              │               │          │         │                     │                │       │       │asemenea.                    │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Jurisdic- │         │                     │Șir de caractere│   0   │   1   │Dacă operatorul nu deține    │România            │
│              │               │ția opera-│         │                     │                │       │       │licență în această           │                   │
│              │               │torului   │         │                     │                │       │       │jurisdicție, acest câmp      │                   │
│              │               │          │         │                     │                │       │       │conține jurisdicția în care  │                   │
│              │               │          │         │                     │                │       │       │activează operatorul al cărui│                   │
│              │               │          │         │                     │                │       │       │cont (virtual) este creditat.│                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Bani      │         │                     │                │   1   │neaso- │Listă a tuturor sumelor      │                   │
│              │               │pariați   │         │                     │                │       │ciat   │pariate de jucător în timpul │ -                 │
│              │               │          │         │                     │                │       │       │rundei. Dacă o sumă pariată  │                   │
│              │               │          │         │                     │                │       │       │unică este debitată din      │                   │
│              │               │          │         │                     │                │       │       │conturi diferite (de exemplu,│                   │
│              │               │          │         │                     │                │       │       │din contul de bani reali și  │                   │
│              │               │          │         │                     │                │       │       │din contul de bani bonus, se │                   │
│              │               │          │         │                     │                │       │       │consideră că s-au pariat     │                   │
│              │               │          │         │                     │                │       │       │două sume diferite).         │                   │
│              │               │          │         │                     │                │       │       │Aceasta include și rake-ul   │                   │
│              │               │          │         │                     │                │       │       │posibil.                     │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descrie- │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │bani bonus         │
│              │               │          │rea      │                     │                │       │       │portofelului. Aceasta este   │                   │
│              │               │          │contului │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere.                   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Sumă     │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │10,00              │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. Aceasta nu │                   │
│              │               │          │         │                     │                │       │       │include contribuțiile la     │                   │
│              │               │          │         │                     │                │       │       │jackpot.                     │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Monedă   │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│USD                │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu,      │                   │
│              │               │          │         │                     │                │       │       │"bani bonus"). Acest câmp    │                   │
│              │               │          │         │                     │                │       │       │este opțional dacă contul    │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Câștiguri │         │                     │                │   0   │neaso- │Listă a tuturor câștigurilor │                   │
│              │               │          │         │                     │                │       │ciat   │jucătorului în timpul rundei.│                   │
│              │               │          │         │                     │                │       │       │O rundă poate conduce la mai │                   │
│              │               │          │         │                     │                │       │       │multe câștiguri, deoarece    │                   │
│              │               │          │         │                     │                │       │       │premiul este împărțit în bani│                   │
│              │               │          │         │                     │                │       │       │reali și bani bonus, de      │                   │
│              │               │          │         │                     │                │       │       │exemplu.                     │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descriere│                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │Bilete și cazare la│
│              │               │          │ÎnNatură │                     │                │       │       │numai atunci când jucătorul  │hotel pentru un    │
│              │               │          │         │                     │                │       │       │câștiga un premiu în natură. │week-end în Las    │
│              │               │          │         │                     │                │       │       │În acest caz, câmpul descrie │Vegas              │
│              │               │          │         │                     │                │       │       │ce fel de cadou a câștigat   │                   │
│              │               │          │         │                     │                │       │       │jucătorul. Trebuie furnizată │                   │
│              │               │          │         │                     │                │       │       │fie DescriereÎnNatură,       │                   │
│              │               │          │         │                     │                │       │       │fie Descriere cont.          │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descrie- │                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │cont pe bani reali │
│              │               │          │rea      │                     │                │       │       │numai când se creditează bani│                   │
│              │               │          │contului │                     │                │       │       │(virtuali) într-un cont, nu  │                   │
│              │               │          │         │                     │                │       │       │în cazul premiilor în natură.│                   │
│              │               │          │         │                     │                │       │       │Descrierea contului/         │                   │
│              │               │          │         │                     │                │       │       │portofelului în care se      │                   │
│              │               │          │         │                     │                │       │       │creditează câștigurile.      │                   │
│              │               │          │         │                     │                │       │       │Aceasta este utilizată drept │                   │
│              │               │          │         │                     │                │       │       │identificare pentru acest    │                   │
│              │               │          │         │                     │                │       │       │tip de cont. Toți jucătorii  │                   │
│              │               │          │         │                     │                │       │       │cu același tip de cont au în │                   │
│              │               │          │         │                     │                │       │       │comun aceeași descriere.     │                   │
│              │               │          │         │                     │                │       │       │Trebuie furnizată fie        │                   │
│              │               │          │         │                     │                │       │       │DescriereÎnNatură, fie       │                   │
│              │               │          │         │                     │                │       │       │Descriere cont.              │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Sumă     │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate în │25321,02           │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. În cazul   │                   │
│              │               │          │         │                     │                │       │       │unui premiu în natură,       │                   │
│              │               │          │         │                     │                │       │       │aceasta este valoarea        │                   │
│              │               │          │         │                     │                │       │       │estimată a premiului.        │                   │
│              │               │          │         │                     │                │       │       │Aceasta nu include           │                   │
│              │               │          │         │                     │                │       │       │câștigurile din jackpoturi.  │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Monedă   │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │COP                │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu,      │                   │
│              │               │          │         │                     │                │       │       │"bani bonus").               │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional dacă│                   │
│              │               │          │         │                     │                │       │       │contul utilizează moneda     │                   │
│              │               │          │         │                     │                │       │       │locală.                      │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Jackpot   │         │                     │                │   0   │neaso- │Aceasta este o listă a       │                   │
│              │               │          │         │                     │                │       │ciat   │tuturor jackpoturilor, dacă  │       -           │
│              │               │          │         │                     │                │       │       │este cazul, asociate         │                   │
│              │               │          │         │                     │                │       │       │jucătorului în această rundă.│                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descriere│                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Jackpot de poker   │
│              │               │          │jackpot  │                     │                │       │       │jackpotului, așa cum este    │"bad beat"         │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │                   │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│                   │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │                   │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │                   │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │                   │
│              │               │          │         │                     │                │       │       │are descrierea sa.           │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descrie- │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │bani bonus         │
│              │               │          │rea      │                     │                │       │       │portofelului de jucător      │                   │
│              │               │          │contului │                     │                │       │       │implicat în tranzacția       │                   │
│              │               │          │         │                     │                │       │       │jackpotului. Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același    │                   │
│              │               │          │         │                     │                │       │       │tip de cont au în comun      │                   │
│              │               │          │         │                     │                │       │       │aceeași descriere.           │                   │
│              │               │          │         │                     │                │       │       │Aceasta nu este o descriere  │                   │
│              │               │          │         │                     │                │       │       │a contului unde se află banii│                   │
│              │               │          │         │                     │                │       │       │aferenți jackpotului înainte │                   │
│              │               │          │         │                     │                │       │       │de declanșarea acestuia.     │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Sumă     │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate sau│25321,02           │
│              │               │          │         │                     │                │       │       │debitate din cont, cu o      │                   │
│              │               │          │         │                     │                │       │       │precizie de cel puțin 2      │                   │
│              │               │          │         │                     │                │       │       │zecimale.                    │                   │
│              │               │          │         │                     │                │       │       │Suma este negativă în cazul  │                   │
│              │               │          │         │                     │                │       │       │în care contul a fost debitat│                   │
│              │               │          │         │                     │                │       │       │în timpul unei contribuții la│                   │
│              │               │          │         │                     │                │       │       │jackpot. Suma este pozitivă  │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul a câștigat    │                   │
│              │               │          │         │                     │                │       │       │jackpotul.                   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Monedă   │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │COP                │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu,      │                   │
│              │               │          │         │                     │                │       │       │"bani bonus").               │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional dacă│                   │
│              │               │          │         │                     │                │       │       │contul utilizează moneda     │                   │
│              │               │          │         │                     │                │       │       │locală.                      │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Ora începerii  │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora la  │2011-10-           │
│              │               │          │         │                     │                │       │       │care a început runda.        │04T19:44:51.346Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Ora terminării │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora     │2011-10-           │
│              │               │          │         │                     │                │       │       │terminării rundei (rezultatul│04T19:45:32.265Z   │
│              │               │          │         │                     │                │       │       │este cunoscut).              │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Joc cu jucător│               │          │         │Aproape în timp real │                │       │       │                             │                   │
│unic (de      │               │          │         │după fiecare rundă   │                │       │       │                             │                   │
│exemplu,      │               │          │         │sau sesiune de joc   │                │       │       │                             │                   │
│sloturi)      │               │          │         │                     │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID sesiune     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │254a26b5-5194-465d-│
│              │               │          │         │                     │                │       │       │unic runda jocului. Două     │b1c5-063231490d60  │
│              │               │          │         │                     │                │       │       │runde din seif nu pot avea   │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDRundă    │                   │
│              │               │          │         │                     │                │       │       │(chiar și pentru tipuri de   │                   │
│              │               │          │         │                     │                │       │       │jocuri diferite). Operatorul │                   │
│              │               │          │         │                     │                │       │       │va utiliza un UUID pentru    │                   │
│              │               │          │         │                     │                │       │       │acest câmp. Deoarece numai   │                   │
│              │               │          │         │                     │                │       │       │un jucător este implicat     │                   │
│              │               │          │         │                     │                │       │       │într-un "joc cu jucător      │                   │
│              │               │          │         │                     │                │       │       │unic", operatorul poate opta │                   │
│              │               │          │         │                     │                │       │       │să înregistreze rundele      │                   │
│              │               │          │         │                     │                │       │       │jucătorului împreună într-o  │                   │
│              │               │          │         │                     │                │       │       │sesiune, în locul            │                   │
│              │               │          │         │                     │                │       │       │înregistrării tuturor        │                   │
│              │               │          │         │                     │                │       │       │rundelor în mod independent. │                   │
│              │               │          │         │                     │                │       │       │O sesiune cu jucător unic    │                   │
│              │               │          │         │                     │                │       │       │este durata petrecută de un  │                   │
│              │               │          │         │                     │                │       │       │jucător la același joc. Pot  │                   │
│              │               │          │         │                     │                │       │       │exista mai multe sesiuni cu  │                   │
│              │               │          │         │                     │                │       │       │jucător unic în paralel, la  │                   │
│              │               │          │         │                     │                │       │       │jocuri diferite sau la       │                   │
│              │               │          │         │                     │                │       │       │același joc.                 │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Categoria      │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este categoria sau   │sloturi            │
│              │jocului        │          │         │                     │(enumerare)     │       │       │tipul jocului, conform       │                   │
│              │               │          │         │                     │                │       │       │descrierii și autorizării    │                   │
│              │               │          │         │                     │                │       │       │prin lege (de exemplu,       │                   │
│              │               │          │         │                     │                │       │       │"video poker", "sloturi",    │                   │
│              │               │          │         │                     │                │       │       │"altele" etc.). Valoarea     │                   │
│              │               │          │         │                     │                │       │       │depinde exclusiv de setările │                   │
│              │               │          │         │                     │                │       │       │predefinite.                 │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Denumire       │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Sloturi Tomb       │
│              │comercială a   │          │         │                     │                │       │       │jocului, așa cum este afișată│Raider 2013        │
│              │jocului        │          │         │                     │                │       │       │pentru jucător. Pentru acest │                   │
│              │               │          │         │                     │                │       │       │joc specific este utilizat   │                   │
│              │               │          │         │                     │                │       │       │un ID, care este comun       │                   │
│              │               │          │         │                     │                │       │       │pentru toți jucătorii care   │                   │
│              │               │          │         │                     │                │       │       │joacă jocul respectiv.       │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID jucător     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │9965-facbcc23542   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat   │                   │
│              │               │          │         │                     │                │       │       │în toate evidențele care țin │                   │
│              │               │          │         │                     │                │       │       │de jucător și nu este        │                   │
│              │               │          │         │                     │                │       │       │modificat niciodată în timpul│                   │
│              │               │          │         │                     │                │       │       │vieții utile a contului.     │                   │
│              │               │          │         │                     │                │       │       │IDJucător nu se modifică,    │                   │
│              │               │          │         │                     │                │       │       │indiferent dacă jucătorul    │                   │
│              │               │          │         │                     │                │       │       │își schimbă pseudonimul sau  │                   │
│              │               │          │         │                     │                │       │       │datele personale.            │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID operator    │          │         │                     │Șir de caractere│   0   │   1   │Acesta este ID-ul            │French_Operator    │
│              │               │          │         │                     │                │       │       │operatorului care "deține"   │(operator francez) │
│              │               │          │         │                     │                │       │       │jucătorul. Operatorul        │                   │
│              │               │          │         │                     │                │       │       │deținător poate fi diferit de│                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea în caz de      │                   │
│              │               │          │         │                     │                │       │       │lichidități în comun sau     │                   │
│              │               │          │         │                     │                │       │       │jocuri în rețea. Acest ID    │                   │
│              │               │          │         │                     │                │       │       │este oferit de autoritatea   │                   │
│              │               │          │         │                     │                │       │       │care a acordat o licență     │                   │
│              │               │          │         │                     │                │       │       │acestui operator. Acest câmp │                   │
│              │               │          │         │                     │                │       │       │este opțional, dacă          │                   │
│              │               │          │         │                     │                │       │       │operatorul este același cu   │                   │
│              │               │          │         │                     │                │       │       │operatorul care creează      │                   │
│              │               │          │         │                     │                │       │       │înregistrarea.               │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jurisdicția    │          │         │                     │Șir de caractere│   0   │   1   │Aceasta este jurisdicția în  │România            │
│              │operatorului   │          │         │                     │                │       │       │care activează operatorul    │                   │
│              │               │          │         │                     │                │       │       │care "deține" jucătorul.     │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea. Acest   │                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea și deținătorul │                   │
│              │               │          │         │                     │                │       │       │jucătorului se află în       │                   │
│              │               │          │         │                     │                │       │       │aceeași jurisdicție.         │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Bani pariați   │          │         │                     │                │   1   │neaso- │Listă a tuturor sumelor      │                   │
│              │               │          │         │                     │                │       │ciat   │pariate de jucător în timpul │ -                 │
│              │               │          │         │                     │                │       │       │rundei. Pot exista mai multe │                   │
│              │               │          │         │                     │                │       │       │sume pariate în timpul unei  │                   │
│              │               │          │         │                     │                │       │       │mâini de poker, de exemplu.  │                   │
│              │               │          │         │                     │                │       │       │Dacă o sumă pariată unică    │                   │
│              │               │          │         │                     │                │       │       │este debitată din conturi    │                   │
│              │               │          │         │                     │                │       │       │diferite (de exemplu, din    │                   │
│              │               │          │         │                     │                │       │       │contul de bani reali și din  │                   │
│              │               │          │         │                     │                │       │       │contul de bani bonus, se     │                   │
│              │               │          │         │                     │                │       │       │consideră că s-au pariat două│                   │
│              │               │          │         │                     │                │       │       │sume diferite).              │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului                 │                   │
│              │               │          │         │                     │                │       │       │Aceasta este utilizată drept │                   │
│              │               │          │         │                     │                │       │       │identificare pentru acest tip│                   │
│              │               │          │         │                     │                │       │       │de cont. Toți jucătorii cu   │                   │
│              │               │          │         │                     │                │       │       │același tip de cont au în    │                   │
│              │               │          │         │                     │                │       │       │comun aceeași descriere.     │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. Aceasta nu │                   │
│              │               │          │         │                     │                │       │       │include contribuțiile la     │                   │
│              │               │          │         │                     │                │       │       │jackpot                      │10,00              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │USD                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Câștiguri      │          │         │                     │                │   1   │neaso- │Listă a tuturor câștigurilor │                   │
│              │               │          │         │                     │                │       │ciat   │jucătorului în timpul rundei.│                   │
│              │               │          │         │                     │                │       │       │Un premiu poate conduce la   │                   │
│              │               │          │         │                     │                │       │       │mai multe câștiguri, deoarece│                   │
│              │               │          │         │                     │                │       │       │premiul este împărțit în bani│                   │
│              │               │          │         │                     │                │       │       │reali și bani bonus, de      │                   │
│              │               │          │         │                     │                │       │       │exemplu.                     │         -         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descriere │         │                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │Bilete și cazare la│
│              │               │ÎnNatură  │         │                     │                │       │       │numai atunci când jucătorul  │hotel pentru un    │
│              │               │          │         │                     │                │       │       │câștiga un premiu în natură. │week-end în Las    │
│              │               │          │         │                     │                │       │       │În acest caz, câmpul descrie │Vegas              │
│              │               │          │         │                     │                │       │       │ce fel de cadou a câștigat   │                   │
│              │               │          │         │                     │                │       │       │jucătorul. Trebuie furnizată │                   │
│              │               │          │         │                     │                │       │       │fie DescriereÎnNatură, fie   │                   │
│              │               │          │         │                     │                │       │       │Descriere cont.              │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │                   │
│              │               │contului  │         │                     │                │       │       │numai când se creditează bani│                   │
│              │               │          │         │                     │                │       │       │(virtuali) într-un cont, nu  │                   │
│              │               │          │         │                     │                │       │       │în cazul premiilor în natură.│                   │
│              │               │          │         │                     │                │       │       │Descrierea contului/         │                   │
│              │               │          │         │                     │                │       │       │portofelului în care se      │                   │
│              │               │          │         │                     │                │       │       │creditează câștigurile.      │                   │
│              │               │          │         │                     │                │       │       │Aceasta este utilizată drept │                   │
│              │               │          │         │                     │                │       │       │identificare pentru acest tip│                   │
│              │               │          │         │                     │                │       │       │de cont. Toți jucătorii cu   │                   │
│              │               │          │         │                     │                │       │       │același tip de cont au în    │                   │
│              │               │          │         │                     │                │       │       │comun aceeași descriere.     │                   │
│              │               │          │         │                     │                │       │       │Trebuie furnizată fie        │                   │
│              │               │          │         │                     │                │       │       │DescriereÎnNatură, fie       │                   │
│              │               │          │         │                     │                │       │       │Descriere cont.              │cont pe bani reali │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate în │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. În cazul   │                   │
│              │               │          │         │                     │                │       │       │unui premiu în natură,       │                   │
│              │               │          │         │                     │                │       │       │aceasta este valoarea        │                   │
│              │               │          │         │                     │                │       │       │estimată a premiului. Aceasta│                   │
│              │               │          │         │                     │                │       │       │nu include câștigurile din   │                   │
│              │               │          │         │                     │                │       │       │jackpoturi.                  │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.).         │                   │
│              │               │          │         │                     │                │       │       │Dacă este virtuală, este     │                   │
│              │               │          │         │                     │                │       │       │utilizată descrierea (de     │                   │
│              │               │          │         │                     │                │       │       │exemplu, "bani bonus"). Acest│                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │contul utilizează moneda     │                   │
│              │               │          │         │                     │                │       │       │locală.                      │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jackpot        │          │         │                     │                │   0   │neaso- │Aceasta este o listă a       │                   │
│              │               │          │         │                     │                │       │ciat   │tuturor jackpoturilor, dacă  │                   │
│              │               │          │         │                     │                │       │       │este cazul, asociate         │                   │
│              │               │          │         │                     │                │       │       │jucătorului în această rundă.│ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descriere │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Jackpot de poker   │
│              │               │jackpot   │         │                     │                │       │       │jackpotului, așa cum este    │"bad beat"         │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │                   │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│                   │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │                   │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │                   │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │                   │
│              │               │          │         │                     │                │       │       │are descrierea sa.           │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului de jucător      │                   │
│              │               │          │         │                     │                │       │       │implicat în tranzacția       │                   │
│              │               │          │         │                     │                │       │       │jackpotului. Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. Aceasta nu este o │                   │
│              │               │          │         │                     │                │       │       │descriere a contului unde se │                   │
│              │               │          │         │                     │                │       │       │află banii aferenți          │                   │
│              │               │          │         │                     │                │       │       │jackpotului înainte de       │                   │
│              │               │          │         │                     │                │       │       │declanșarea acestuia.        │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate sau│                   │
│              │               │          │         │                     │                │       │       │debitate din cont, cu o      │                   │
│              │               │          │         │                     │                │       │       │precizie de cel puțin 2      │                   │
│              │               │          │         │                     │                │       │       │zecimale. Suma este negativă │                   │
│              │               │          │         │                     │                │       │       │în cazul în care contul a    │                   │
│              │               │          │         │                     │                │       │       │fost debitat în timpul unei  │                   │
│              │               │          │         │                     │                │       │       │contribuții la jackpot. Suma │                   │
│              │               │          │         │                     │                │       │       │este pozitivă dacă jucătorul │                   │
│              │               │          │         │                     │                │       │       │a câștigat jackpotul.        │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.).         │                   │
│              │               │          │         │                     │                │       │       │Dacă este virtuală, este     │                   │
│              │               │          │         │                     │                │       │       │utilizată descrierea (de     │                   │
│              │               │          │         │                     │                │       │       │exemplu, "bani bonus"). Acest│                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │contul utilizează moneda     │                   │
│              │               │          │         │                     │                │       │       │locală.                      │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Ora începerii  │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora la  │2011-10-           │
│              │               │          │         │                     │                │       │       │care a început runda sau     │04T19:44:51.346Z   │
│              │               │          │         │                     │                │       │       │sesiunea.                    │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Ora terminării │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora     │2011-10-           │
│              │               │          │         │                     │                │       │       │terminării rundei (rezultatul│04T19:45:32.265Z   │
│              │               │          │         │                     │                │       │       │este cunoscut) sau a         │                   │
│              │               │          │         │                     │                │       │       │terminării sesiunii          │                   │
│              │               │          │         │                     │                │       │       │(jucătorul a părăsit jocul). │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Tranzacție în │               │          │         │Aproape în timp real │                │       │       │                             │                   │
│turneu (de    │               │          │         │la buy-in            │                │       │       │                             │                   │
│exemplu,      │               │          │         │                     │                │       │       │                             │                   │
│buy-in, rebuy │               │          │         │                     │                │       │       │                             │                   │
│la poker)     │               │          │         │                     │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID tranzacție  │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │unic tranzacția asociată     │9965-facbcc23542   │
│              │               │          │         │                     │                │       │       │jucătorului respectiv în     │                   │
│              │               │          │         │                     │                │       │       │turneu. Două tranzacții din  │                   │
│              │               │          │         │                     │                │       │       │seif nu pot avea în comun    │                   │
│              │               │          │         │                     │                │       │       │niciodată același            │                   │
│              │               │          │         │                     │                │       │       │IDTranzacție. Operatorul va  │                   │
│              │               │          │         │                     │                │       │       │utiliza un UUID pentru acest │                   │
│              │               │          │         │                     │                │       │       │câmp.                        │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID turneu      │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │254a26b5-5194-465d-│
│              │               │          │         │                     │                │       │       │unic turneul. Două turnee din│b1c5-063231490d60  │
│              │               │          │         │                     │                │       │       │seif nu pot avea niciodată   │                   │
│              │               │          │         │                     │                │       │       │același IDTurneu (deși pot   │                   │
│              │               │          │         │                     │                │       │       │avea în comun aceeași        │                   │
│              │               │          │         │                     │                │       │       │denumire comercială a        │                   │
│              │               │          │         │                     │                │       │       │jocului). Operatorul va      │                   │
│              │               │          │         │                     │                │       │       │utiliza un UUID pentru acest │                   │
│              │               │          │         │                     │                │       │       │câmp. Toate tranzacțiile     │                   │
│              │               │          │         │                     │                │       │       │aferente turneului vor avea  │                   │
│              │               │          │         │                     │                │       │       │același IDTurneu.            │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Categoria      │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este categoria sau   │                   │
│              │jocului        │          │         │                     │(enumerare)     │       │       │tipul jocului, conform       │                   │
│              │               │          │         │                     │                │       │       │descrierii și autorizării    │                   │
│              │               │          │         │                     │                │       │       │prin lege (de exemplu,       │                   │
│              │               │          │         │                     │                │       │       │"poker", "blackjack", "pariu"│                   │
│              │               │          │         │                     │                │       │       │"altele" etc.). Valoarea     │                   │
│              │               │          │         │                     │                │       │       │depinde exclusiv de setările │                   │
│              │               │          │         │                     │                │       │       │predefinite.                 │                   │
│              │               │          │         │                     │                │       │       │Turneele nu se limitează la  │                   │
│              │               │          │         │                     │                │       │       │poker.                       │poker              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Denumire       │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Turneu de Poker    │
│              │comercială a   │          │         │                     │                │       │       │jocului, așa cum este afișată│Hold'em            │
│              │jocului        │          │         │                     │                │       │       │pentru jucător. Pentru acest │                   │
│              │               │          │         │                     │                │       │       │joc specific este utilizat un│                   │
│              │               │          │         │                     │                │       │       │ID, care este comun pentru   │                   │
│              │               │          │         │                     │                │       │       │toți jucătorii care joacă    │                   │
│              │               │          │         │                     │                │       │       │jocul respectiv.             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID jucător     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │9965-facbcc23542   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │                   │
│              │               │          │         │                     │                │       │       │personale.                   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID operator    │          │         │                     │Șir de caractere│   0   │   1   │Acesta este ID-ul            │French_Operator    │
│              │               │          │         │                     │                │       │       │operatorului care "deține"   │(operator francez) │
│              │               │          │         │                     │                │       │       │jucătorul.                   │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea. Acest ID│                   │
│              │               │          │         │                     │                │       │       │este oferit de autoritatea   │                   │
│              │               │          │         │                     │                │       │       │care a acordat o licență     │                   │
│              │               │          │         │                     │                │       │       │acestui operator. Acest câmp │                   │
│              │               │          │         │                     │                │       │       │este opțional, dacă          │                   │
│              │               │          │         │                     │                │       │       │operatorul este același cu   │                   │
│              │               │          │         │                     │                │       │       │operatorul care creează      │                   │
│              │               │          │         │                     │                │       │       │înregistrarea.               │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jurisdicția    │          │         │                     │Șir de caractere│   0   │   1   │Aceasta este jurisdicția în  │                   │
│              │operatorului   │          │         │                     │                │       │       │care activează operatorul    │                   │
│              │               │          │         │                     │                │       │       │care "deține" jucătorul.     │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea. Acest   │                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea și deținătorul │                   │
│              │               │          │         │                     │                │       │       │jucătorului se află în       │                   │
│              │               │          │         │                     │                │       │       │aceeași jurisdicție.         │România            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Tip tranzacție │          │         │                     │Șir de caractere│   1   │   1   │Acesta furnizează categoria  │                   │
│              │               │          │         │                     │                │       │       │tranzacției. De exemplu,     │                   │
│              │               │          │         │                     │                │       │       │într-un turneu de poker,     │                   │
│              │               │          │         │                     │                │       │       │acestea sunt "buy-in",       │                   │
│              │               │          │         │                     │                │       │       │"rebuy", "addon".            │                   │
│              │               │          │         │                     │                │       │       │Turneele care nu sunt de     │                   │
│              │               │          │         │                     │                │       │       │poker pot utiliza diferite   │                   │
│              │               │          │         │                     │                │       │       │tipuri de tranzacții.        │rebuy              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data           │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora     │2011-10-           │
│              │               │          │         │                     │                │       │       │tranzacției.                 │04T19:45:32.265Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Bani pariați   │          │         │                     │                │   1   │neaso- │Listă a tuturor sumelor de   │                   │
│              │               │          │         │                     │                │       │ciat   │bani angajate de jucător     │                   │
│              │               │          │         │                     │                │       │       │pentru această tranzacție.   │                   │
│              │               │          │         │                     │                │       │       │Pot exista mai multe sume    │                   │
│              │               │          │         │                     │                │       │       │pariate în timpul unei       │                   │
│              │               │          │         │                     │                │       │       │tranzacții, dacă banii sunt  │                   │
│              │               │          │         │                     │                │       │       │debitați din conturi diferite│                   │
│              │               │          │         │                     │                │       │       │(de exemplu, din contul de   │                   │
│              │               │          │         │                     │                │       │       │bani reali și din contul de  │                   │
│              │               │          │         │                     │                │       │       │bani bonus, se consideră că  │                   │
│              │               │          │         │                     │                │       │       │s-au pariat două sume        │                   │
│              │               │          │         │                     │                │       │       │diferite).                   │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere.                   │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. Aceasta nu │                   │
│              │               │          │         │                     │                │       │       │include contribuțiile la     │                   │
│              │               │          │         │                     │                │       │       │jackpot.                     │10,00              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu,:     │                   │
│              │               │          │         │                     │                │       │       │"bani bonus"). Acest câmp    │                   │
│              │               │          │         │                     │                │       │       │este opțional dacă contul    │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │USD                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jackpot        │          │         │                     │                │   0   │neaso- │Aceasta este o listă a       │                   │
│              │               │          │         │                     │                │       │ciat   │tuturor jackpoturilor, dacă  │                   │
│              │               │          │         │                     │                │       │       │este cazul, la care jucătorul│                   │
│              │               │          │         │                     │                │       │       │a contribuit cu această      │                   │
│              │               │          │         │                     │                │       │       │tranzacție.                  │  -                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descriere │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Câștigătorul       │
│              │               │jackpot   │         │                     │                │       │       │jackpotului, așa cum este    │jackpotului        │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │"jucătorul         │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│înregistrat cu     │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │numărul un milion" │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │                   │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │                   │
│              │               │          │         │                     │                │       │       │are descrierea sa.           │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului de jucător      │                   │
│              │               │          │         │                     │                │       │       │implicat în tranzacția       │                   │
│              │               │          │         │                     │                │       │       │jackpotului. Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. Aceasta nu este o │                   │
│              │               │          │         │                     │                │       │       │descriere a contului unde se │                   │
│              │               │          │         │                     │                │       │       │află banii aferenți          │                   │
│              │               │          │         │                     │                │       │       │jackpotului înainte de       │                   │
│              │               │          │         │                     │                │       │       │declanșarea acestuia.        │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. Suma este  │                   │
│              │               │          │         │                     │                │       │       │negativă, deoarece contul a  │                   │
│              │               │          │         │                     │                │       │       │fost debitat pentru o        │                   │
│              │               │          │         │                     │                │       │       │contribuție la jackpot.      │362,20             │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.).         │                   │
│              │               │          │         │                     │                │       │       │Dacă este virtuală, este     │                   │
│              │               │          │         │                     │                │       │       │utilizată descrierea (de     │                   │
│              │               │          │         │                     │                │       │       │exemplu, "bani bonus"). Acest│                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │contul utilizează moneda     │                   │
│              │               │          │         │                     │                │       │       │locală.                      │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Câștiguri     │               │          │         │Aproape în timp real │                │       │       │                             │                   │
│turneu (de    │               │          │         │la sfârșitul         │                │       │       │                             │                   │
│exemplu,      │               │          │         │turneului            │                │       │       │                             │                   │
│turneu de     │               │          │         │                     │                │       │       │                             │                   │
│poker)        │               │          │         │                     │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID turneu      │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │254a26b5-5194-465d-│
│              │               │          │         │                     │                │       │       │unic turneul. Două turnee din│b1c5-063231490d60  │
│              │               │          │         │                     │                │       │       │seif nu pot avea niciodată   │                   │
│              │               │          │         │                     │                │       │       │același IDTurneu (chiar și   │                   │
│              │               │          │         │                     │                │       │       │pentru tipuri de jocuri      │                   │
│              │               │          │         │                     │                │       │       │diferite). Operatorul va     │                   │
│              │               │          │         │                     │                │       │       │utiliza un UUID pentru acest │                   │
│              │               │          │         │                     │                │       │       │câmp. Aceasta este aceeași   │                   │
│              │               │          │         │                     │                │       │       │valoare cu cea utilizată     │                   │
│              │               │          │         │                     │                │       │       │pentru toate tranzacțiile    │                   │
│              │               │          │         │                     │                │       │       │care implică acest turneu.   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Categoria      │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este categoria sau   │                   │
│              │jocului        │          │         │                     │(enumerare)     │       │       │tipul jocului, conform       │                   │
│              │               │          │         │                     │                │       │       │descrierii și autorizării    │                   │
│              │               │          │         │                     │                │       │       │prin lege (de exemplu,       │                   │
│              │               │          │         │                     │                │       │       │"poker", "blackjack",        │                   │
│              │               │          │         │                     │                │       │       │"pariu", "altele" etc.).     │                   │
│              │               │          │         │                     │                │       │       │Valoarea depinde exclusiv de │                   │
│              │               │          │         │                     │                │       │       │setările predefinite.        │                   │
│              │               │          │         │                     │                │       │       │Turneele nu se limitează la  │                   │
│              │               │          │         │                     │                │       │       │poker.                       │poker              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Denumire       │          │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │Turneu de Poker    │
│              │comercială a   │          │         │                     │                │       │       │jocului, așa cum este afișată│Hold'em            │
│              │jocului        │          │         │                     │                │       │       │pentru jucător. Pentru acest │                   │
│              │               │          │         │                     │                │       │       │joc specific este utilizat un│                   │
│              │               │          │         │                     │                │       │       │ID, care este comun pentru   │                   │
│              │               │          │         │                     │                │       │       │toți jucătorii care joacă    │                   │
│              │               │          │         │                     │                │       │       │jocul respectiv.             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Dată sfârșit   │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora     │2011-10-           │
│              │               │          │         │                     │                │       │       │terminării turneului         │04T19:45:32.265Z   │
│              │               │          │         │                     │                │       │       │(rezultatul este cunoscut)   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Câștigători    │          │         │                     │                │   1   │neaso- │Aceasta este lista tuturor   │                   │
│              │               │          │         │                     │                │       │ciat   │câștigătorilor turneului.    │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID jucător│         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │9965-facbcc23542   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │                   │
│              │               │          │         │                     │                │       │       │personale.                   │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ID        │         │                     │Șir de caractere│   0   │   1   │Acesta este ID-ul            │French_Operator    │
│              │               │operator  │         │                     │                │       │       │operatorului care "deține"   │(operator francez) │
│              │               │          │         │                     │                │       │       │jucătorul.                   │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea. Acest ID│                   │
│              │               │          │         │                     │                │       │       │este oferit de autoritatea   │                   │
│              │               │          │         │                     │                │       │       │care a acordat o licență     │                   │
│              │               │          │         │                     │                │       │       │acestui operator. Acest câmp │                   │
│              │               │          │         │                     │                │       │       │este opțional, dacă          │                   │
│              │               │          │         │                     │                │       │       │operatorul este același cu   │                   │
│              │               │          │         │                     │                │       │       │operatorul care creează      │                   │
│              │               │          │         │                     │                │       │       │înregistrarea.               │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Jurisdic- │         │                     │Șir de caractere│   0   │   1   │Aceasta este jurisdicția în  │                   │
│              │               │ția opera-│         │                     │                │       │       │care activează operatorul    │                   │
│              │               │torului   │         │                     │                │       │       │care "deține" jucătorul.     │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea. Acest   │                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea și deținătorul │                   │
│              │               │          │         │                     │                │       │       │jucătorului se află în       │                   │
│              │               │          │         │                     │                │       │       │aceeași jurisdicție.         │România            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Câștiguri │         │                     │                │   1   │neaso- │Listă a tuturor câștigurilor │                   │
│              │               │          │         │                     │                │       │ciat   │jucătorului în timpul        │                   │
│              │               │          │         │                     │                │       │       │turneului. Un premiu poate   │                   │
│              │               │          │         │                     │                │       │       │conduce la mai multe         │                   │
│              │               │          │         │                     │                │       │       │câștiguri, deoarece premiul  │                   │
│              │               │          │         │                     │                │       │       │este împărțit în bani reali  │                   │
│              │               │          │         │                     │                │       │       │și bani bonus, de exemplu.   │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descriere│                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │Bilete și cazare la│
│              │               │          │ÎnNatură │                     │                │       │       │numai atunci când jucătorul  │hotel pentru un    │
│              │               │          │         │                     │                │       │       │câștiga un premiu în natură. │week-end în Las    │
│              │               │          │         │                     │                │       │       │În acest caz, câmpul descrie │Vegas              │
│              │               │          │         │                     │                │       │       │ce fel de cadou a câștigat   │                   │
│              │               │          │         │                     │                │       │       │jucătorul. Trebuie furnizată │                   │
│              │               │          │         │                     │                │       │       │fie DescriereÎnNatură, fie   │                   │
│              │               │          │         │                     │                │       │       │Descriere cont.              │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descrie- │                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │                   │
│              │               │          │rea      │                     │                │       │       │numai când se creditează bani│                   │
│              │               │          │contului │                     │                │       │       │(virtuali) într-un cont, nu  │                   │
│              │               │          │         │                     │                │       │       │în cazul premiilor în natură.│                   │
│              │               │          │         │                     │                │       │       │Descrierea contului/         │                   │
│              │               │          │         │                     │                │       │       │portofelului în care se      │                   │
│              │               │          │         │                     │                │       │       │creditează câștigurile.      │                   │
│              │               │          │         │                     │                │       │       │Aceasta este utilizată drept │                   │
│              │               │          │         │                     │                │       │       │identificare pentru acest tip│                   │
│              │               │          │         │                     │                │       │       │de cont. Toți jucătorii cu   │                   │
│              │               │          │         │                     │                │       │       │același tip de cont au în    │                   │
│              │               │          │         │                     │                │       │       │comun aceeași descriere.     │                   │
│              │               │          │         │                     │                │       │       │Trebuie furnizată fie        │                   │
│              │               │          │         │                     │                │       │       │DescriereÎnNatură, fie       │                   │
│              │               │          │         │                     │                │       │       │Descriere cont.              │cont pe bani reali │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Sumă     │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate în │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale. În cazul   │                   │
│              │               │          │         │                     │                │       │       │unui premiu în natură,       │                   │
│              │               │          │         │                     │                │       │       │aceasta este valoarea        │                   │
│              │               │          │         │                     │                │       │       │estimată a premiului. Aceasta│                   │
│              │               │          │         │                     │                │       │       │nu include câștigurile din   │                   │
│              │               │          │         │                     │                │       │       │jackpoturi.                  │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Monedă   │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │ COP               │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │ Jackpot  │         │                     │                │   0   │neaso- │Aceasta este o listă a       │                   │
│              │               │          │         │                     │                │       │ciat   │tuturor jackpoturilor, dacă  │                   │
│              │               │          │         │                     │                │       │       │este cazul, din acest turneu │                   │
│              │               │          │         │                     │                │       │       │asociate jucătorului.        │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descriere│                     │Șir de caractere│   1   │   1   │Aceasta este o descriere     │                   │
│              │               │          │jackpot  │                     │                │       │       │a jackpotului, așa cum este  │                   │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │                   │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│                   │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │                   │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │                   │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │Jackpot de poker   │
│              │               │          │         │                     │                │       │       │are descrierea sa.           │"bad beat"         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Descrie- │                     │Șir de          │   1   │   1   │Descrierea contului/         │                   │
│              │               │          │rea      │                     │caractere       │       │       │portofelului de jucător      │                   │
│              │               │          │contului │                     │                │       │       │implicat în tranzacția       │                   │
│              │               │          │         │                     │                │       │       │jackpotului. Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. Aceasta nu este o │                   │
│              │               │          │         │                     │                │       │       │descriere a contului unde se │                   │
│              │               │          │         │                     │                │       │       │află banii aferenți          │                   │
│              │               │          │         │                     │                │       │       │jackpotului înainte de       │                   │
│              │               │          │         │                     │                │       │       │declanșarea acestuia.        │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Sumă     │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate sau│                   │
│              │               │          │         │                     │                │       │       │debitate din cont, cu o      │                   │
│              │               │          │         │                     │                │       │       │precizie de cel puțin 2      │                   │
│              │               │          │         │                     │                │       │       │zecimale. Suma este negativă │                   │
│              │               │          │         │                     │                │       │       │în cazul în care contul a    │                   │
│              │               │          │         │                     │                │       │       │fost debitat în timpul unei  │                   │
│              │               │          │         │                     │                │       │       │contribuții la jackpot. Suma │                   │
│              │               │          │         │                     │                │       │       │este pozitivă dacă jucătorul │                   │
│              │               │          │         │                     │                │       │       │a câștigat jackpotul.        │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │          │Monedă   │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Plasarea      │               │          │         │Aproape în timp real │                │       │       │                             │                   │
│pariurilor    │               │          │         │atunci când pariul   │                │       │       │                             │                   │
│              │               │          │         │este plasat cu cote  │                │       │       │                             │                   │
│              │               │          │         │fixe sau când pariul │                │       │       │                             │                   │
│              │               │          │         │este acceptat în     │                │       │       │                             │                   │
│              │               │          │         │cazul bursei         │                │       │       │                             │                   │
│              │               │          │         │pariurilor           │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID pariu       │          │         │                     │Șir de caractere│   1   │   1   │ID unic al pariului. Dacă pe │                   │
│              │               │          │         │                     │                │       │       │același bilet apar mai multe │                   │
│              │               │          │         │                     │                │       │       │pariuri, fiecare pariu       │                   │
│              │               │          │         │                     │                │       │       │individual are propriul ID.  │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID jucător     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │                   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │personale.                   │9965-facbcc23542   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID operator    │          │         │                     │Șir de caractere│   0   │   1   │Acesta este ID-ul            │                   │
│              │               │          │         │                     │                │       │       │operatorului care "deține"   │                   │
│              │               │          │         │                     │                │       │       │jucătorul. Operatorul        │                   │
│              │               │          │         │                     │                │       │       │deținător poate fi diferit de│                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea în caz de      │                   │
│              │               │          │         │                     │                │       │       │lichidități în comun sau     │                   │
│              │               │          │         │                     │                │       │       │jocuri în rețea. Acest ID    │                   │
│              │               │          │         │                     │                │       │       │este oferit de autoritatea   │                   │
│              │               │          │         │                     │                │       │       │care a acordat o licență     │                   │
│              │               │          │         │                     │                │       │       │acestui operator. Acest câmp │                   │
│              │               │          │         │                     │                │       │       │este opțional, dacă          │                   │
│              │               │          │         │                     │                │       │       │operatorul este același cu   │                   │
│              │               │          │         │                     │                │       │       │operatorul care creează      │French_Operator    │
│              │               │          │         │                     │                │       │       │înregistrarea.               │(operator francez) │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jurisdicția    │          │         │                     │Șir de caractere│   0   │   1   │Aceasta este jurisdicția în  │                   │
│              │operatorului   │          │         │                     │                │       │       │care activează operatorul    │                   │
│              │               │          │         │                     │                │       │       │care "deține" jucătorul.     │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea. Acest   │                   │
│              │               │          │         │                     │                │       │       │câmp este opțional dacă      │                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea și deținătorul │                   │
│              │               │          │         │                     │                │       │       │jucătorului se află în       │                   │
│              │               │          │         │                     │                │       │       │aceeași jurisdicție.         │România            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Descriere pariu│          │         │                     │Șir de caractere│   1   │   1   │Aceasta descrie pariul plasat│2014/02/13 -       │
│              │               │          │         │                     │                │       │       │de jucător, așa cum i-a fost │Barca/PSG - 1N2 -  │
│              │               │          │         │                     │                │       │       │afișat.                      │câștigător Barca   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Descriere      │          │         │                     │Șir de caractere│   1   │neaso- │Aceasta cuprinde toate       │                   │
│              │eveniment      │          │         │                     │                │       │ciat   │evenimentele/jocurile/       │2014/02/13 - meci  │
│              │               │          │         │                     │                │       │       │competițiile implicate în    │de fotbal -        │
│              │               │          │         │                     │                │       │       │determinarea rezultatului.   │Barca/PSG          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Cote agreate   │          │         │                     │Zecimal         │   0   │   1   │Dacă pariul plasat este unul │                   │
│              │               │          │         │                     │                │       │       │cu cote fixe, cotele sunt    │                   │
│              │               │          │         │                     │                │       │       │descrise aici.               │1,25               │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data           │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora la  │2011-10-           │
│              │               │          │         │                     │                │       │       │care a fost plasat pariul.   │04T19:45:32.265Z   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Bani pariați   │          │         │                     │                │   1   │neaso- │Listă a tuturor sumelor      │                   │
│              │               │          │         │                     │                │       │ciat   │pariate de jucător în cadrul │                   │
│              │               │          │         │                     │                │       │       │acestui pariu. Pot exista mai│                   │
│              │               │          │         │                     │                │       │       │multe sume pariate în cadrul │                   │
│              │               │          │         │                     │                │       │       │unui pariu. Dacă banii sunt  │                   │
│              │               │          │         │                     │                │       │       │debitați din conturi diferite│                   │
│              │               │          │         │                     │                │       │       │(de exemplu, din contul de   │                   │
│              │               │          │         │                     │                │       │       │bani reali și din contul de  │                   │
│              │               │          │         │                     │                │       │       │bani bonus, se consideră că  │                   │
│              │               │          │         │                     │                │       │       │s-au pariat două sume        │                   │
│              │               │          │         │                     │                │       │       │diferite).                   │         -         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere.                   │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale             │10,00              │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   1   │   1   │Monedă utilizată pentru cont.│                   │
│              │               │          │         │                     │                │       │       │Dacă este o monedă reală,    │                   │
│              │               │          │         │                     │                │       │       │este utilizat codul ISO 4217 │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │USD                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jackpot        │          │         │                     │                │   0   │neaso- │Aceasta este o listă a       │                   │
│              │               │          │         │                     │                │       │ciat   │tuturor jackpoturilor, dacă  │                   │
│              │               │          │         │                     │                │       │       │este cazul, la care jucătorul│                   │
│              │               │          │         │                     │                │       │       │a contribuit cu pariul.      │                   │
│              │               │          │         │                     │                │       │       │Probabil neutilizat          │         -         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descriere │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │                   │
│              │               │jackpot   │         │                     │                │       │       │jackpotului, așa cum este    │                   │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │                   │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│                   │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │                   │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │Câștigătorul       │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │pariului cu numărul│
│              │               │          │         │                     │                │       │       │are descrierea sa.           │un milion plasat   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului de jucător      │                   │
│              │               │          │         │                     │                │       │       │implicat în tranzacția       │                   │
│              │               │          │         │                     │                │       │       │jackpotului. Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. Aceasta nu este o │                   │
│              │               │          │         │                     │                │       │       │descriere a contului unde se │                   │
│              │               │          │         │                     │                │       │       │află banii aferenți          │                   │
│              │               │          │         │                     │                │       │       │jackpotului înainte de       │                   │
│              │               │          │         │                     │                │       │       │declanșarea acestuia.        │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte debitate din │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale             │                   │
│              │               │          │         │                     │                │       │       │Suma este negativă, deoarece │                   │
│              │               │          │         │                     │                │       │       │contul a fost debitat pentru │                   │
│              │               │          │         │                     │                │       │       │o contribuție la jackpot.    │362,20             │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   1   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│Deciderea     │               │          │         │Aproape în timp real │                │       │       │                             │                   │
│pariului (și  │               │          │         │pentru deciderea și  │                │       │       │                             │                   │
│redeciderea)  │               │          │         │redeciderea pariului │                │       │       │                             │                   │
│              │               │          │         │Se trimite chiar dacă│                │       │       │                             │                   │
│              │               │          │         │jucătorul a pierdut. │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID pariu       │          │         │                     │Șir de caractere│   1   │   1   │ID unic al pariului. Dacă pe │                   │
│              │               │          │         │                     │                │       │       │același bilet apar mai multe │                   │
│              │               │          │         │                     │                │       │       │pariuri, fiecare pariu       │                   │
│              │               │          │         │                     │                │       │       │individual are propriul ID.  │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID jucător     │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │               │          │         │                     │                │       │       │unic jucătorul relevant      │                   │
│              │               │          │         │                     │                │       │       │pentru această înregistrare. │                   │
│              │               │          │         │                     │                │       │       │Doi jucători nu pot avea     │                   │
│              │               │          │         │                     │                │       │       │niciodată același IDJucător. │                   │
│              │               │          │         │                     │                │       │       │IDJucător este asociat       │                   │
│              │               │          │         │                     │                │       │       │contului jucătorului         │                   │
│              │               │          │         │                     │                │       │       │înregistrat, este utilizat în│                   │
│              │               │          │         │                     │                │       │       │toate evidențele care țin de │                   │
│              │               │          │         │                     │                │       │       │jucător și nu este modificat │                   │
│              │               │          │         │                     │                │       │       │niciodată în timpul vieții   │                   │
│              │               │          │         │                     │                │       │       │utile a contului. IDJucător  │                   │
│              │               │          │         │                     │                │       │       │nu se modifică, indiferent   │                   │
│              │               │          │         │                     │                │       │       │dacă jucătorul își schimbă   │                   │
│              │               │          │         │                     │                │       │       │pseudonimul sau datele       │328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │personale.                   │9965-facbcc23542   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID operator    │          │         │                     │Șir de caractere│   0   │   1   │Acesta este ID-ul            │                   │
│              │               │          │         │                     │                │       │       │operatorului care "deține"   │                   │
│              │               │          │         │                     │                │       │       │jucătorul. Operatorul        │                   │
│              │               │          │         │                     │                │       │       │deținător poate fi diferit de│                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea în caz de      │                   │
│              │               │          │         │                     │                │       │       │lichidități în comun sau     │                   │
│              │               │          │         │                     │                │       │       │jocuri în rețea. Acest ID    │                   │
│              │               │          │         │                     │                │       │       │este oferit de autoritatea   │                   │
│              │               │          │         │                     │                │       │       │care a acordat o licență     │                   │
│              │               │          │         │                     │                │       │       │acestui operator.            │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional,    │                   │
│              │               │          │         │                     │                │       │       │dacă operatorul este același │                   │
│              │               │          │         │                     │                │       │       │cu operatorul care creează   │French_Operator    │
│              │               │          │         │                     │                │       │       │înregistrarea.               │(operator francez) │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jurisdicția    │          │         │                     │Șir de caractere│   0   │   1   │Aceasta este jurisdicția în  │                   │
│              │operatorului   │          │         │                     │                │       │       │care activează operatorul    │                   │
│              │               │          │         │                     │                │       │       │care "deține" jucătorul.     │                   │
│              │               │          │         │                     │                │       │       │Operatorul deținător poate fi│                   │
│              │               │          │         │                     │                │       │       │diferit de operatorul care   │                   │
│              │               │          │         │                     │                │       │       │generează înregistrarea în   │                   │
│              │               │          │         │                     │                │       │       │caz de lichidități în comun  │                   │
│              │               │          │         │                     │                │       │       │sau jocuri în rețea.         │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional dacă│                   │
│              │               │          │         │                     │                │       │       │operatorul care generează    │                   │
│              │               │          │         │                     │                │       │       │înregistrarea și deținătorul │                   │
│              │               │          │         │                     │                │       │       │jucătorului se află în       │                   │
│              │               │          │         │                     │                │       │       │aceeași jurisdicție.         │România            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Descrierea     │          │         │                     │Șir de caractere│   1   │neaso- │Această listă conține        │                   │
│              │deciderii      │          │         │                     │                │       │ciat   │rezultatele tuturor          │                   │
│              │               │          │         │                     │                │       │       │evenimentelor care au condus │                   │
│              │               │          │         │                     │                │       │       │la această decidere. Această │                   │
│              │               │          │         │                     │                │       │       │listă poate fi mai scurtă    │                   │
│              │               │          │         │                     │                │       │       │decât lista cu descrierea    │                   │
│              │               │          │         │                     │                │       │       │evenimentelor, deoarece un   │                   │
│              │               │          │         │                     │                │       │       │pariu poate fi decis chiar   │                   │
│              │               │          │         │                     │                │       │       │dacă nu au avut loc toate    │                   │
│              │               │          │         │                     │                │       │       │evenimentele aferente.       │Barca a câștigat   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Descriere      │          │         │                     │Șir de caractere│   1   │neaso- │Aceasta cuprinde toate       │                   │
│              │eveniment      │          │         │                     │                │       │ciat   │evenimentele/jocurile/       │                   │
│              │               │          │         │                     │                │       │       │competițiile implicate în    │                   │
│              │               │          │         │                     │                │       │       │determinarea rezultatului.   │                   │
│              │               │          │         │                     │                │       │       │Această listă trebuie să fie │2014/02/13 - meci  │
│              │               │          │         │                     │                │       │       │aceeași cu cea utilizată în  │de fotbal -        │
│              │               │          │         │                     │                │       │       │timpul plasării pariurilor.  │Barca/PSG          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Data           │          │         │                     │DatăOră         │   1   │   1   │Aceasta este data și ora la  │                   │
│              │               │          │         │                     │                │       │       │care s-a decis pariul        │2011-10-04T19: 45: │
│              │               │          │         │                     │                │       │       │(rezultatul este cunoscut)   │32.265Z            │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Câștiguri      │          │         │                     │                │   1   │neaso- │Listă a tuturor câștigurilor │                   │
│              │               │          │         │                     │                │       │ciat   │jucătorului în timpul        │                   │
│              │               │          │         │                     │                │       │       │turneului. Un premiu poate   │                   │
│              │               │          │         │                     │                │       │       │conduce la mai multe         │                   │
│              │               │          │         │                     │                │       │       │câștiguri, deoarece premiul  │                   │
│              │               │          │         │                     │                │       │       │este împărțit în bani reali  │                   │
│              │               │          │         │                     │                │       │       │și bani bonus, de exemplu.   │  -                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descriere │         │                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │                   │
│              │               │ÎnNatură  │         │                     │                │       │       │numai atunci când jucătorul  │                   │
│              │               │          │         │                     │                │       │       │câștiga un premiu în natură. │                   │
│              │               │          │         │                     │                │       │       │În acest caz, câmpul descrie │                   │
│              │               │          │         │                     │                │       │       │ce fel de cadou a câștigat   │Bilete și cazare la│
│              │               │          │         │                     │                │       │       │jucătorul. Trebuie furnizată │hotel pentru un    │
│              │               │          │         │                     │                │       │       │fie DescriereÎnNatură, fie   │week-end în        │
│              │               │          │         │                     │                │       │       │Descriere cont.              │Las Vegas          │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   0   │   1   │Acest câmp este utilizat     │                   │
│              │               │contului  │         │                     │                │       │       │numai când se creditează bani│                   │
│              │               │          │         │                     │                │       │       │(virtuali) într-un cont, nu  │                   │
│              │               │          │         │                     │                │       │       │în cazul premiilor în natură.│                   │
│              │               │          │         │                     │                │       │       │Descrierea contului/         │                   │
│              │               │          │         │                     │                │       │       │portofelului în care se      │                   │
│              │               │          │         │                     │                │       │       │creditează câștigurile.      │                   │
│              │               │          │         │                     │                │       │       │Aceasta este utilizată drept │                   │
│              │               │          │         │                     │                │       │       │identificare pentru acest tip│                   │
│              │               │          │         │                     │                │       │       │de cont. Toți jucătorii cu   │                   │
│              │               │          │         │                     │                │       │       │același tip de cont au în    │                   │
│              │               │          │         │                     │                │       │       │comun aceeași descriere.     │                   │
│              │               │          │         │                     │                │       │       │Trebuie furnizată fie        │                   │
│              │               │          │         │                     │                │       │       │DescriereÎnNatură, fie       │                   │
│              │               │          │         │                     │                │       │       │Descriere cont.              │cont pe bani reali │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate în │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale             │                   │
│              │               │          │         │                     │                │       │       │În cazul unui premiu în      │                   │
│              │               │          │         │                     │                │       │       │natură, aceasta este valoarea│                   │
│              │               │          │         │                     │                │       │       │estimată a premiului.        │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │Jackpot        │          │         │                     │                │   0   │neaso- │Aceasta este o listă a       │                   │
│              │               │          │         │                     │                │       │ciat   │tuturor jackpoturilor, dacă  │                   │
│              │               │          │         │                     │                │       │       │este cazul, pe care jucătorul│                   │
│              │               │          │         │                     │                │       │       │le-a declanșat și le-a       │                   │
│              │               │          │         │                     │                │       │       │câștigat. Probabil           │                   │
│              │               │          │         │                     │                │       │       │neutilizat                   │ -                 │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descriere │         │                     │Șir de caractere│   1   │   1   │Aceasta este o descriere a   │                   │
│              │               │jackpot   │         │                     │                │       │       │jackpotului, așa cum este    │                   │
│              │               │          │         │                     │                │       │       │afișată pentru jucător.      │                   │
│              │               │          │         │                     │                │       │       │Pentru acest jackpot specific│                   │
│              │               │          │         │                     │                │       │       │este utilizat un ID, care    │                   │
│              │               │          │         │                     │                │       │       │este comun pentru toți       │                   │
│              │               │          │         │                     │                │       │       │jucătorii. Fiecare jackpot   │Jackpot de poker   │
│              │               │          │         │                     │                │       │       │are descrierea sa.           │"bad beat"         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Descrierea│         │                     │Șir de caractere│   1   │   1   │Descrierea contului/         │                   │
│              │               │contului  │         │                     │                │       │       │portofelului de jucător      │                   │
│              │               │          │         │                     │                │       │       │implicat în tranzacția       │                   │
│              │               │          │         │                     │                │       │       │jackpotului. Aceasta este    │                   │
│              │               │          │         │                     │                │       │       │utilizată drept identificare │                   │
│              │               │          │         │                     │                │       │       │pentru acest tip de cont.    │                   │
│              │               │          │         │                     │                │       │       │Toți jucătorii cu același tip│                   │
│              │               │          │         │                     │                │       │       │de cont au în comun aceeași  │                   │
│              │               │          │         │                     │                │       │       │descriere. Aceasta nu este o │                   │
│              │               │          │         │                     │                │       │       │descriere a contului unde se │                   │
│              │               │          │         │                     │                │       │       │află banii aferenți          │                   │
│              │               │          │         │                     │                │       │       │jackpotului înainte de       │                   │
│              │               │          │         │                     │                │       │       │declanșarea acestuia.        │bani bonus         │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Bani sau puncte creditate în │                   │
│              │               │          │         │                     │                │       │       │cont, cu o precizie de cel   │                   │
│              │               │          │         │                     │                │       │       │puțin 2 zecimale             │                   │
│              │               │          │         │                     │                │       │       │Suma este pozitivă, deoarece │                   │
│              │               │          │         │                     │                │       │       │jucătorul a câștigat         │                   │
│              │               │          │         │                     │                │       │       │jackpotul.                   │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Moneda utilizată pentru cont │                   │
│              │               │          │         │                     │                │       │       │sau valoarea estimată. Dacă  │                   │
│              │               │          │         │                     │                │       │       │este o monedă reală, este    │                   │
│              │               │          │         │                     │                │       │       │utilizat codul ISO 4217      │                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.). Dacă    │                   │
│              │               │          │         │                     │                │       │       │este virtuală, este utilizată│                   │
│              │               │          │         │                     │                │       │       │descrierea (de exemplu, "bani│                   │
│              │               │          │         │                     │                │       │       │bonus"). Acest câmp este     │                   │
│              │               │          │         │                     │                │       │       │opțional dacă contul         │                   │
│              │               │          │         │                     │                │       │       │utilizează moneda locală.    │COP                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│GGR           │               │          │         │Aproape în timp real,│                │       │       │                             │                   │
│              │               │          │         │de fiecare dată când │                │       │       │                             │                   │
│              │               │          │         │este decis un pariu, │                │       │       │                             │                   │
│              │               │          │         │se termină un joc sau│                │       │       │                             │                   │
│              │               │          │         │are loc o tranzacție │                │       │       │                             │                   │
│              │               │          │         │de pe urma căreia    │                │       │       │                             │                   │
│              │               │          │         │operatorul percepe un│                │       │       │                             │                   │
│              │               │          │         │comision. Practic, de│                │       │       │                             │                   │
│              │               │          │         │fiecare dată când    │                │       │       │                             │                   │
│              │               │          │         │este afectat GGR-ul  │                │       │       │                             │                   │
│              │               │          │         │operatorului.        │                │       │       │                             │                   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │ID tranzacție/ │          │         │                     │Șir de caractere│   1   │   1   │Acest câmp identifică în mod │                   │
│              │ID sesiune/ID  │          │         │                     │                │       │       │unic tranzacția, sesiunea sau│                   │
│              │pariu          │          │         │                     │                │       │       │pariul. Două tranzacții,     │                   │
│              │               │          │         │                     │                │       │       │sesiuni sau pariuri din seif │                   │
│              │               │          │         │                     │                │       │       │nu pot avea în comun         │                   │
│              │               │          │         │                     │                │       │       │niciodată acest câmp.        │                   │
│              │               │          │         │                     │                │       │       │Operatorul va utiliza un UUID│328ad861-25cb-6437-│
│              │               │          │         │                     │                │       │       │pentru acest câmp.           │9965-facbcc23542   │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │GGR            │          │         │                     │                │   1   │   1   │Bani primiți de operator     │                   │
│              │               │          │         │                     │                │       │       │drept comision pentru        │                   │
│              │               │          │         │                     │                │       │       │tranzacție sau mizele        │                   │
│              │               │          │         │                     │                │       │       │jucătorilor, în cazul în care│                   │
│              │               │          │         │                     │                │       │       │au pierdut.                  │  -                │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Sumă      │         │                     │Zecimal         │   1   │   1   │Sumă primită de operator     │                   │
│              │               │          │         │                     │                │       │       │Suma poate fi negativă în    │                   │
│              │               │          │         │                     │                │       │       │cazul în care jucătorul a    │                   │
│              │               │          │         │                     │                │       │       │câștigat sau în cazul unei   │                   │
│              │               │          │         │                     │                │       │       │redecideri.                  │25321,02           │
├──────────────┼───────────────┼──────────┼─────────┼─────────────────────┼────────────────┼───────┼───────┼─────────────────────────────┼───────────────────┤
│              │               │Monedă    │         │                     │Monedă          │   0   │   1   │Codul ISO 4217 al monedei GGR│                   │
│              │               │          │         │                     │                │       │       │("EUR", "GBP" etc.)          │                   │
│              │               │          │         │                     │                │       │       │Acest câmp este opțional în  │                   │
│              │               │          │         │                     │                │       │       │cazul în care GGR utilizează │                   │
│              │               │          │         │                     │                │       │       │moneda locală.               │COP                │
└──────────────┴───────────────┴──────────┴─────────┴─────────────────────┴────────────────┴───────┴───────┴─────────────────────────────┴───────────────────┘
```
-------
