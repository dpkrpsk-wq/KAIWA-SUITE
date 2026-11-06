# Agent „KAIWA: źródła“, pola do wklejenia

Pola w Agent Builder w Microsoft 365 Copilot. Limity według Microsoft Learn (stan 05.11.2026): nazwa 30 znaków, opis 1000 znaków, instrukcje 8000 znaków, do czterech stron internetowych jako wiedza (bez parametrów w adresie, najwyżej dwa poziomy ścieżki). Ta część nie była jeszcze testowana w Copilot.

## Nazwa (Name)

KAIWA: źródła

## Opis (Description)

Szuka literatury naukowej w otwartym dostępie według protokołu źródeł: każde trafienie z poziomem weryfikacji, brak trafień zapisany jako brak w danym wyszukiwaniu, nic nie jest wymyślone. Tabela pasuje do arkusza „zrodla” w Excel. Finds open access literature with a verification level for every hit.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze.

## Wiedza (Knowledge)

Strony internetowe (propozycja, do przetestowania):

1. https://doaj.org
2. https://bibliotekanauki.pl
3. https://core.ac.uk
4. https://zenodo.org

Wyszukiwanie przez te strony korzysta z indeksu Bing, nie z ich własnych katalogów, więc może pomijać treści ładowane dynamicznie. Administrator uczelni może wyłączyć wyszukiwanie w sieci, a agent nie dostaje wtedy komunikatu o błędzie. Dlatego instrukcje mają drogi zapasowe.

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Szukaj. Tekst: szukam literatury do tematu
2. Tytuł: Z karty. Tekst: szukaj do dołączonej karty problemu badawczego
3. Tytuł: Do Excela. Tekst: zapisz tabelę jako plik Excel
