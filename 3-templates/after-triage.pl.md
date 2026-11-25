# Po triażu: dalszy krok i język wyniku

Szablon z pakietu KAIWA, produkt 26.01, wersja 0.2.1 (robocza), 22.11.2026.

Triaż klasyfikuje artefakt (rodzaj, modalność, twierdzenia jawne i ukryte, skala) i proponuje ramy analizy. Zanim analiza się zacznie, asystent pyta o dwie rzeczy. Agent „KAIWA: analiza“ robi to sam. Ten plik służy jako zapasowa droga: tekst poniżej możesz wkleić do dowolnego asystenta AI razem z wynikiem triażu.

## Krok 1: jak kontynuować

Asystent pokazuje wynik triażu i pyta:

> Jak chcesz kontynuować?
> 1. Dalej bez dodatkowych informacji.
> 2. Ogólny komentarz albo zlecenie.
> 3. Sformułowanie problemu badawczego.

1. **Dalej bez dodatkowych informacji.** Asystent stosuje ramy zaproponowane w triażu, bez dalszych pytań.
2. **Ogólny komentarz albo zlecenie.** Piszesz albo mówisz, na co asystent ma zwrócić uwagę albo co ma zrobić. Asystent zapisuje twoje słowa dosłownie i traktuje je jako zlecenie dla całej analizy.
3. **Sformułowanie problemu badawczego.** Asystent prowadzi cię pole po polu przez kartę problemu badawczego (`3-templates/research-problem-card.pl.md`). Do każdego pola wpisuje najpierw twoje słowa. Własne propozycje oznacza jako **[asystent]**. Na końcu razem sprawdzacie pięć kryteriów. Gotowa karta staje się ramą całej analizy.

## Krok 2: język wyniku

Po kroku 1, przy każdej z trzech dróg, asystent pyta:

> W jakim języku ma być wynik? polski, English, Deutsch albo inny.

Język przetwarzania pozostaje angielski: triaż i ramy analizy pracują po angielsku, bo w tym języku zostały napisane i przetestowane w repozytorium prompt-library (protokołów tych testów nie ma w pakiecie). Dopiero wynik asystent podaje w wybranym języku. Kluczowe terminy zostają przy pierwszym użyciu w nawiasie w wersji angielskiej, żeby było widać, którego pojęcia ramy dotyczą.

Razem z pytaniem o język asystent pyta o kontekst kulturowy artefaktu, twoją pozycję wobec niego i adresata wyniku. Wynik kończy się blokiem „Kontrola kulturowa“. Opis i lista kontrolna: `3-templates/cultural-check.pl.md`.

## Tekst do wklejenia (droga zapasowa)

```text
After the triage above, do not start the analysis yet. Ask me in my language:
"How do you want to continue? 1. Continue without further input. 2. General comment or task. 3. Formulate a research problem."
Option 1: apply the frameworks recommended by the triage.
Option 2: record my words verbatim and treat them as the task for the whole analysis.
Option 3: guide me field by field through: topic, research problem, cognitive and practical aim ("what for?"), main thesis or hypothesis, secondary hypotheses, main question, auxiliary questions. Put my words first. Mark every suggestion of yours as [assistant]. At the end check with me: clear and understandable, refers to reality, empirically researchable, does not suggest the answer, contains a dependency (X affects Y). Use the finished card as the frame of the analysis.
Then ask: "In which language should the result be?" Keep processing in English. Give the result in the chosen language, with key terms in English in brackets at first use.
```
