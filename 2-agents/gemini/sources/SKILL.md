# Moduł „KAIWA: źródła”, pola do wklejenia (Google Gemini)

Pola do utworzenia pojedynczego Skillu (Gemini web/app) albo Gemu (Google Workspace). Wersja robocza 0.2.2 (22.11.2026), nieprzetestowana w Gemini.

## Nazwa (Name)

KAIWA: źródła

## Opis (Description)

Szuka literatury naukowej w otwartym dostępie według protokołu źródeł: każde trafienie z poziomem weryfikacji, brak trafień zapisany jako brak w danym wyszukiwaniu, agent ma niczego nie wymyślać. Tabela pasuje do arkusza „zrodla” w Excel. Finds open access literature with a verification level for every hit.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze (`2-agents/gemini/sources/INSTRUCTIONS.txt`).

## Wiedza (Knowledge)

Katalogi otwartego dostępu (do przeszukania w sieci lub przez adresy zapytań):
1. https://doaj.org
2. https://bibliotekanauki.pl
3. https://core.ac.uk
4. https://zenodo.org

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Szukaj. Tekst: szukam literatury do tematu
2. Tytuł: Z karty. Tekst: szukaj do dołączonej karty problemu badawczego
3. Tytuł: Do Excela. Tekst: zapisz tabelę jako plik Excel
