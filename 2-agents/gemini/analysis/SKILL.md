# Moduł „KAIWA: analiza”, pola do wklejenia (Google Gemini)

Pola do utworzenia pojedynczego Skillu (Gemini web/app) albo Gemu (Google Workspace). Instrukcje odsyłają do triażu w `method/prompts/core/artifact-triage.md` (prompt-library, mentalpinG-Ops, CC BY-SA 4.0, zob. `method/prompts/LICENSE.md`). Ten plik dołączasz do rozmowy. Wersja robocza 0.2.0 (22.11.2026), nieprzetestowana w Gemini.

## Nazwa (Name)

KAIWA: analiza

## Opis (Description)

Analiza artefaktu metodą deklarowanych ram: najpierw triaż, potem wybór dalszego kroku (dalej, komentarz albo problem badawczy), potem język wyniku i kontekst kulturowy, potem analiza według dołączonych plików ram, na końcu blok „Kontrola kulturowa”. Przetwarza po angielsku, wynik podaje w wybranym języku. Artefact analysis with declared frameworks: triage, next step, output language, then framework analysis.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze (`2-agents/gemini/analysis/INSTRUCTIONS.txt`).

## Wiedza (Knowledge)

Pliki z folderu `method/prompts/` (`core/artifact-triage.md`, `framework-catalog.md`, wybrane ramy z `cultural-scientific/` i `social-science/`) dołączasz do rozmowy albo odwołujesz się do nich przez podłączony Dysk Google (niesprawdzone).

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Triaż. Tekst: zrób triaż dołączonego artefaktu
2. Tytuł: Problem badawczy. Tekst: chcę sformułować problem badawczy
3. Tytuł: Lista ram. Tekst: pokaż ramy dostępne w pakiecie
