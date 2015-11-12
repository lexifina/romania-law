# Text
1. Casa Națională de Asigurări de Sănătate transmite Agenției Naționale de Administrare Fiscală informațiile privind lista persoanelor fizice care au accesat sistemul de asigurări sociale de sănătate, înregistrate în Registrul unic de evidență al asiguraților din Platforma informatică din asigurările de sănătate pe categorii de asigurați, în vederea anulării contribuției de asigurări sociale de sănătate datorate de către persoanele fizice exceptate de la plata contribuției de asigurări sociale de sănătate potrivit art. 224 alin. (1) din Legea nr. 95/2006 privind reforma în domeniul sănătății republicată, începând cu data de 1 ianuarie 2012 și până la data intrării în vigoare a prevederilor art. I pct. 17 și 18 din Ordonanța Guvernului nr. 4/2015 pentru modificarea Legii nr. 571/2003 privind Codul fiscal. 2. Casa Națională de Asigurări de Sănătate transmite centralizat Agenției Naționale de Administrare Fiscală lista persoanelor fizice prevăzute la pct. 1, înregistrate în Registrul unic de evidență al asiguraților din Platforma informatică din asigurările de sănătate care se încadrează în categoriile menționate la pct. 1, potrivit structurii fișierului de raportare a informațiilor, prevăzute în anexa nr. 1, după cum urmează:
a) pentru anul 2012, se transmite lista persoanelor înregistrate în Registrul unic de evidență a asiguraților din Platforma informatică din asigurările de sănătate, în termen de 10 zile lucrătoare de la data intrării în vigoare a prezentului ordin;
b) pentru anul 2013 se transmite lista persoanelor înregistrate în Registrul unic de evidență a asiguraților din Platforma informatică din asigurările de sănătate, în termen de 15 zile lucrătoare de la data intrării în vigoare a prezentului ordin;
c) pentru anul 2014 se transmite lista persoanelor înregistrate în Registrul unic de evidență a asiguraților din Platforma informatică din asigurările de sănătate, în termen de 20 de zile lucrătoare de la data intrării în vigoare a prezentului ordin.
3. Lista categoriilor de persoane fizice înregistrate în Registrul unic de evidență al asiguraților din Platforma informatică din asigurările de sănătate, întocmită potrivit prevederilor art. 224 alin. (1) din Legea nr. 95/2006 , republicată, este prevăzută în anexa nr. 2. 4. Structura fișierului de raportare a informațiilor privind categoriile de persoane menționate la pct. 3 este prevăzută în anexa nr. 1. 5. Furnizarea de către Casa Națională de Asigurări de Sănătate a informațiilor prevăzute la pct. 1 se realizează prin mecanisme securizate, folosind aplicația "Schimb masiv de date", pusă la dispoziție de către Agenția Națională de Administrare Fiscală, pentru categoriile de persoane menționate în anexa nr. 2. 6. Agenția Națională de Administrare Fiscală, în vederea anulării contribuției de asigurări sociale de sănătate datorate de către persoanele fizice exceptate de la plata contribuției de asigurări sociale de sănătate prevăzute la pct. 1, gestionează informațiile primite de la Casa Națională de Asigurări de Sănătate pentru îndeplinirea obligațiilor care îi revin potrivit legii. 7. Casa Națională de Asigurări de Sănătate transmite centralizat Agenției Naționale de Administrare Fiscală lista persoanelor fizice menționate la pct. 3, pe categorii de asigurați, potrivit datelor înregistrate în Registrul unic de evidență al asiguraților din Platforma informatică din asigurările de sănătate, începând cu data de 1 ianuarie 2012 și până la data intrării în vigoare a prevederilor art. I pct. 17 și 18 din Ordonanța Guvernului nr. 4/2015 . 8. Agenția Națională de Administrare Fiscală și Casa Națională de Asigurări de Sănătate au obligația respectării prevederilor referitoare la confidențialitatea, utilizarea și păstrarea datelor și informațiilor furnizate, conform prevederilor legale. 9. Anexele nr. 1 și 2 fac parte integrantă din prezenta procedură.
Anexa 1
la procedură STRUCTURA fișierului de raportare a informațiilor
┌────┬──────────────────┬────────────┬─────────────────────────────────────────┐ │Nr. │
│
│
│ │crt.│
Nume
│
Tip
│
Semnificație
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 1 │SURSA
│varchar2(10)│
CNAS
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 2 │JUDET_SURSA
│Varchar2(2) │Cod județul care a transmis datele
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 3 │DATA_RAPORTARE
│
date
│Data când au fost extrase datele de la
│ │
│
│
│sursă
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 4 │AN_RAPORTARE
│number(4)
│Anul pentru care se face raportarea
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 5 │LUNA_ RAPORTARE
│number(2)
│Luna pentru care se face raportarea
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 6 │COD_CATEGORIE
│varchar2(10)│Cod al categoriei în care este încadrată │ │
│
│
│persoana
│ │
│
│
│În luna și anul de apartenență la
│ │
│
│
│categoria menționată
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 7 │AN_APARTENENTA_
│
│Anul în care persoana este încadrată în │ │
│CATEGORIE
│number(4)
│categoria menționată
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 8 │LUNA_ APARTENENTA_│
│Luna în care persoana este încadrată în │ │
│CATEGORIE
│number(2)
│categoria menționată
│ ├────┼──────────────────┼────────────┼─────────────────────────────────────────┤ │ 9 │CNP
│varchar2(13)│
│ └────┴──────────────────┴────────────┴─────────────────────────────────────────┘
Anexa 2
la procedură LISTA categoriilor de persoane fizice înregistrate în Registrul unic de evidență al asiguraților din Platforma informatică din asigurările de sănătate, întocmită potrivit prevederilor art. 224 alin. (1) din
Legea nr. 95/2006 privind reforma în domeniul sănătății, republicată
┌─────┬────────────────────────────────────────────────────────────────────────┐ │ 100 │copil în cadrul familiei
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │ 102 │tineri cu vârsta între 18 și 26 de ani care sunt elevi, inclusiv
│ │
│absolvenți de liceu până la începerea anului universitar, dar nu mai
│ │
│mult de 3 luni, ucenici sau studenți, dacă nu realizează venituri din
│ │
│muncă
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │ 103 │tinerii cu vârsta de până la 26 de ani, care provin din sistemul de
│ │
│protecție a copilului și nu realizează venituri din muncă sau nu sunt
│ │
│beneficiari de ajutor social acordat în temeiul Legii nr. 416/2001
│ │
│privind venitul minim garantat, cu modificările și completările
│ │
│ulterioare
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │ 106 │soț, soție, părinți, fără venituri proprii, aflați în întreținerea unei │ │
│persoane asigurate
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │ 108 │persoane cu handicap, cu vârsta de peste 18 ani, care nu realizează
│ │
│venituri din muncă, pensie sau alte surse
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │ 109 │femei însărcinate sau lăuze, dacă nu au niciun venit sau au venituri sub│ │
│salariul de bază minim brut pe țară
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │ 110 │persoanele incluse în programele naționale de sănătate stabilite de
│ │
│Ministerul Sănătății, până la vindecarea respectivei afecțiuni, dacă nu │ │
│realizează venituri din muncă, pensie sau din alte resurse
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │107.1│persoane ale căror drepturi sunt stabilite prin Decretul-Lege
│ │
│ nr. 118/1990 privind acordarea unor drepturi persoanelor persecutate din│ │
│motive politice de dictatura instaurată cu începere de la 6 martie 1945,│ │
│precum și celor deportate în străinătate ori constituite în prizonieri, │ │
│republicat, cu modificările și completările ulterioare
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │107.2│persoane ale căror drepturi sunt stabilite prin Legea nr. 44/1994
│ │
│privind veteranii de război, precum și unele drepturi ale invalizilor și│ │
│văduvelor de război, republicată, cu modificările și completările
│ │
│ulterioare
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │107.3│persoane prevăzute la art. 3 alin. (1), lit. b) pct. 1 din Legea
│ │
│recunoștinței pentru victoria Revoluției Române din Decembrie 1989 și
│ │
│pentru revolta muncitorească anticomunistă de la Brașov din noiembrie
│ │
│1987 nr. 341/2004 , cu modificările și completările ulterioare
│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │107.4│persoane ale căror drepturi sunt stabilite prin Legea nr. 309/2002
│ │
│privind recunoașterea și acordarea unor drepturi persoanelor care au
│ │
│efectuat stagiul militar în cadrul Direcției Generale a Serviciului
│ │
│Muncii în perioada 1950-1961, cu modificările și completările ulterioare│ ├─────┼────────────────────────────────────────────────────────────────────────┤ │107.5│persoanele ale căror drepturi sunt stabilite prin Legea nr. 51/1993
│ │
│privind acordarea unor drepturi magistraților care au fost înlăturați
│ │
│din justiție pentru considerente politice în perioada anilor 1945-1989, │ │
│cu modificările ulterioare
│ └─────┴────────────────────────────────────────────────────────────────────────┘
-------
