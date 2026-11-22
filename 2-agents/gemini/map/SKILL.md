# Moduł „KAIWA: mapa kontekstu”, pola do wklejenia (Google Gemini)

Pola do utworzenia pojedynczego Skillu (Gemini web/app) albo Gemu (Google Workspace). Opis metody: `1-start/context.pl.md`. Wersja robocza 0.2.0 (22.11.2026), nieprzetestowana w Gemini.

## Nazwa (Name)

KAIWA: mapa kontekstu

## Opis (Description)

Prowadzi mapę kontekstu: tematy z twoich dyktatów i notatek, ich pochodzenie, połączenia między nimi i twoje cele. Proponuje, wpisuje tylko to, co zatwierdzisz, i zapisuje plik Excel z rejestrem skrótów SHA-256. Mapa jest kontekstem, nie zbiorem reguł. Keeps a context map of topics, provenance, connections and goals from your dictations.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze (`2-agents/gemini/map/INSTRUCTIONS.txt`).

## Wiedza (Knowledge)

Nic nie dodawaj. Pliki dyktatów (`dictation-*.xlsx`) i istniejącą mapę (`mapa-*.xlsx`) dołączasz bezpośrednio do rozmowy.

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Start. Tekst: start
2. Tytuł: Dodaj dyktaty. Tekst: dodaj dołączone dyktaty do mapy
3. Tytuł: Moje cele. Tekst: chcę zapisać swoje cele
4. Tytuł: Co dalej. Tekst: co dalej
5. Tytuł: Sprawdź mapę. Tekst: sprawdź mapę
