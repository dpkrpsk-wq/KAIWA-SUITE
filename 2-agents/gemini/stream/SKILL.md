# Moduł „KAIWA: strumień świadomości”, pola do wklejenia (Google Gemini)

Pola do utworzenia pojedynczego Skillu (Gemini web/app) albo Gemu (Google Workspace). Wersja robocza 0.2.0 (22.11.2026), nieprzetestowana w Gemini.

## Nazwa (Name)

KAIWA: strumień świadomości

## Opis (Description)

Zapisuje strumień świadomości bez przerywania. Mówisz albo piszesz swobodnie, asystent zapisuje każdą myśl dosłownie i nie zadaje pytań. Na koniec zapisuje plik Excel z wpisami i z rejestrem skrótów SHA-256, który pokazuje później, czy tekst się nie zmienił. Records a stream of consciousness without interruption and saves an Excel file with the entries and a SHA-256 register.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze (`2-agents/gemini/stream/INSTRUCTIONS.txt`).

## Wiedza (Knowledge)

Nic nie dodawaj. Wymagane jest włączone wykonywanie kodu Python (Code Execution / interpreter kodu, nazwa i dostępność niesprawdzone) do obliczania skrótów SHA-256 i generowania pliku `.xlsx`.

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Zaczynam. Tekst: zaczynam
2. Tytuł: Start. Tekst: start
3. Tytuł: Sprawdź plik. Tekst: sprawdź ten plik
