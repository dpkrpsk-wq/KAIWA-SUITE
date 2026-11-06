# Agent „KAIWA: analiza“, pola do wklejenia

Pola w Agent Builder w Microsoft 365 Copilot. Limity według Microsoft Learn (stan 05.11.2026): nazwa 30 znaków, opis 1000 znaków, instrukcje 8000 znaków. Instrukcje zawierają dosłowną kopię triażu minimalnego z prompt-library (mentalpinG-Ops, CC BY-SA 4.0, zob. `prompts/LICENSE.md`).

## Nazwa (Name)

KAIWA: analiza

## Opis (Description)

Analiza artefaktu metodą deklarowanych ram: najpierw triaż, potem wybór dalszego kroku (dalej, komentarz albo problem badawczy), potem język wyniku i kontekst kulturowy, potem analiza według dołączonych plików ram, na końcu blok „Kontrola kulturowa”. Przetwarza po angielsku, wynik podaje w wybranym języku. Artefact analysis with declared frameworks: triage, next step, output language, then framework analysis.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze.

## Wiedza (Knowledge)

Nic nie dodawaj. Pliki z folderu `prompts/` dołączasz do rozmowy. Pliki z OneDrive lub SharePoint jako wiedza wymagają licencji Copilot albo płatnego rozliczenia za użycie.

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Triaż. Tekst: zrób triaż dołączonego artefaktu
2. Tytuł: Problem badawczy. Tekst: chcę sformułować problem badawczy
3. Tytuł: Lista ram. Tekst: pokaż ramy dostępne w pakiecie
