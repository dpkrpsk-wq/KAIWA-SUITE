# KAIWA: instrukcja konfiguracji (Google Gemini)

<picture><source media="(prefers-color-scheme: dark)" srcset="../../design/logo/kaiwa-logo-hell.svg"><img src="../../design/logo/kaiwa-logo.svg" alt="KAIWA" width="240"></picture>

**Languages / języki:** [English](setup.en.md) · [Polski](setup.pl.md)

Produkt 26.01, wersja 0.2.1 (robocza), 22.11.2026. Nie wydana. Wydawca: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo, kontakt: 285421@student.uwr.edu.pl. Pakiet przenosi metodę KAIWA do Google Gemini (Skills i Gems to zapisane w Gemini stałe instrukcje, które można wywołać w rozmowie, oraz dowolny czat Gemini z załącznikami).

## Pobranie pakietu

Otwórz stronę pakietu https://mentalping-ops.github.io/KAIWA-SUITE/, wybierz dostawcę „Google Gemini” i naciśnij przycisk pobierania. Rozpakuj plik ZIP do wybranego folderu. Wszystkie ścieżki w tej instrukcji zaczynają się w tym folderze.

## Czego potrzebujesz

1. Konto Google z dostępem do Google Gemini (konto prywatne od 18 lat, konto z subskrypcją Google AI lub konto uczelniane/służbowe Google Workspace, rodzaje kont niesprawdzone).
2. Około pięciu minut na konfigurację (albo jednej minuty w trybie samego czatu z załącznikiem).
3. Python 3.8 lub nowszy tylko wtedy, gdy chcesz sprawdzać pliki na własnym komputerze. To jest opcjonalne.

## Wybór drogi (według praktyki i rodzaju konta)

Google Gemini obsługuje cztery drogi użycia, dopasowane do ustawień włączonych na koncie:

1. **Droga 1, czat z załącznikiem (bez konfiguracji, niesprawdzone w Gemini):** Dołączasz do nowej rozmowy plik `2-agents/gemini/setup-dialog.md` i piszesz „start”. Asystent prowadzi cię przez wybór modułu i daje gotowy tekst do wklejenia.
2. **Droga 2, Skill lub Gem (stała konfiguracja bez powtarzania instrukcji):**
   - **Konta prywatne od 18 lat (Gemini web/app):** W lewym menu wybierz **Dostosuj / Skills** (po angielsku „Customize“, polska nazwa niesprawdzona), kliknij **Utwórz** (niesprawdzone) i utwórz Skills z plików w `2-agents/gemini/stream/`, `2-agents/gemini/map/`, `2-agents/gemini/analysis/`, `2-agents/gemini/sources/`.
   - **Konta uczelniane i służbowe Google Workspace (tam, gdzie działają Gems):** Wybierz **Eksploruj Gems** (nazwa menu niesprawdzona), kliknij **Nowy Gem** (polska nazwa niesprawdzona, po angielsku „New Gem“), wklej nazwę, opis i instrukcje z wybranego folderu (`2-agents/gemini/stream/`, `2-agents/gemini/map/`, `2-agents/gemini/analysis/`, `2-agents/gemini/sources/`).
3. **Droga 3, podłączenie folderu Google Drive (Workspace / połączone aplikacje):** Jeśli na koncie masz włączone rozszerzenie Google Workspace, możesz trzymać `method/protocols/` i `method/prompts/` na Dysku Google i odwoływać się do nich w rozmowie bez ponownego wgrywania (niesprawdzone).
4. **Droga 4, praca lokalna bez AI lub weryfikacja skrótów:** Te same skrypty z folderu `tools/` (`dictation_ledger.py`, `context.py`, `search.py`) oraz arkusze w `4-without-ai/registers.xlsx` sprawdzają wyniki poza Gemini.

## Szybka konfiguracja Skill / Gem (cztery moduły)

Każdy moduł ma własny podfolder w `2-agents/gemini/` z dwoma plikami: `SKILL.md` z polami konfiguracyjnymi oraz `INSTRUCTIONS.txt` z pełną instrukcją.

Czy Gemini wykonuje kod na twoim koncie, pokazuje dopiero pierwszy test (niesprawdzone).

| Moduł | Folder | Wymagany interpreter kodu | Stan / status |
|---|---|---|---|
| KAIWA: strumień świadomości | `2-agents/gemini/stream/` | tak (do skrótów SHA-256 i pliku `.xlsx`) | wersja robocza, nieprzetestowana w Gemini |
| KAIWA: mapa kontekstu | `2-agents/gemini/map/` | tak (do walidacji `kontekst-1`, układu pliku mapy z `1-start/context.pl.md`, i `.xlsx`) | wersja robocza, nieprzetestowana w Gemini |
| KAIWA: analiza | `2-agents/gemini/analysis/` | nie | wersja robocza, nieprzetestowana w Gemini |
| KAIWA: źródła | `2-agents/gemini/sources/` | opcjonalnie (do eksportu `.xlsx`) | wersja robocza, nieprzetestowana w Gemini |

### Kroki dla jednego modułu (Skill lub Gem)

1. Otwórz Gemini w przeglądarce (`gemini.google.com`).
2. W sekcji **Skills** (konta prywatne) albo **Gems** (konta Workspace) utwórz nowy wpis.
3. Skopiuj nazwę i opis z pliku `SKILL.md` w wybranym podfolderze. Jeśli Gemini pozwala ustawić ikonę, użyj pliku `design/logo/kaiwa-icon-192.png` (nie sprawdzono w Gemini).
4. Wklej całą treść pliku `INSTRUCTIONS.txt` do pola instrukcji. Instrukcja strumienia świadomości (`stream/INSTRUCTIONS.txt`) jest po angielsku i tak zostaje, bo to tekst dla modelu (prompt), nie dla czytelnika. Powstała z instrukcji Copilot i na tej platformie nie była testowana. Instrukcja każe agentowi odpowiadać w języku użytkownika, ale jej stałe krótkie odpowiedzi są po angielsku.
5. W wiedzy (Knowledge) nie musisz nic dodawać na stałe: pliki z `method/prompts/`, dyktaty i mapę dołączasz bezpośrednio do konkretnej rozmowy.
6. Zapisz konfigurację.

## Pierwszy test

1. Otwórz skonfigurowany Skill/Gem (albo nowy czat z dołączonym `2-agents/gemini/setup-dialog.md`) i napisz „start”.
2. W modułach **strumień świadomości** i **mapa kontekstu** Gemini powinien uruchomić krótki kod Python i wypisać „OK”, a następnie potwierdzić aktywność skrótów SHA-256.
3. Jeśli w twoim kraju lub na koncie uczelnianym wykonywanie kodu jest wyłączone, Gemini wyświetli ostrzeżenie i zapisze sesję bez skrótów. Nie wolno mu wtedy wymyślać skrótów.
4. Napisz dwa zdania testowe, a potem „koniec”. Sprawdź, czy pojawia się lista tematów, plik `.xlsx` do pobrania oraz wiersz „Narzędzie” i stopka wersji.

## Ostrzeżenia dotyczące użycia i ograniczenia platformy

1. **Dostępność funkcji według kraju i rodzaju konta:** W części krajów (m.in. w EOG/UE) oraz na wybranych kontach uczelnianych Google Workspace niektóre funkcje Gemini (np. Skills, udostępnianie Skills, połączenie z Dyskiem Google lub wykonywanie kodu) mogą być wyłączone z powodów regulacyjnych lub administracyjnych (niesprawdzone). Wtedy użyj drogi 1 (załącznik w czacie) lub drogi zapasowej w `4-without-ai/README.pl.md`.
2. **Rozdzielenie Gemini web i panelu bocznego Workspace:** Instrukcje zapisane w aplikacji Gemini i personalizacja w panelu bocznym Dokumentów/Dysku Google nie synchronizują się automatycznie (niesprawdzone).
3. **Brak automatycznego zapisu na Dysk Google z interpretera kodu:** W odróżnieniu od testowanego konta Microsoft 365 Copilot, pliki `.xlsx` wygenerowane kodem w Gemini są dostępne bezpośrednio do pobrania w oknie rozmowy (niesprawdzone). Zapisz je ręcznie w swoim folderze roboczym (np. `KAIWA/`).
4. **Długa sesja:** Po dwudziestu wpisach w strumieniu świadomości zakończ sesję i rozpocznij nową, aby uniknąć utraty dosłowności.
5. **Skrót SHA-256 nie dowodzi wierności przepisania:** Skrót potwierdza tylko, że tekst w pliku `.xlsx` nie zmienił się po zapisie. Skrót „sha256” liczony jest po ujednoliceniu znaków (NFC), odstępów i podziałów wierszy, więc nie wykrywa zmian samych odstępów ani podziałów wierszy. Drugi skrót „sha256_raw” liczony jest z dokładnych bajtów tekstu. Porównany ręcznie z tekstem pokazuje także takie zmiany, sprawdzenie w agencie porównuje tylko „sha256”. Przeczytaj wygenerowany plik raz po zakończeniu sesji.

## Sprawdzanie na własnym komputerze

- Dziennik w Markdown: `python tools/dictation_ledger.py init <folder>`, `scan <folder>`, `verify <folder>`.
- Mapa kontekstu: `python tools/context.py sprawdz <plik mapy>` (wymaga `openpyxl`).
- Wyszukiwanie otwarte: `python tools/search.py "hasło" --csv wynik.csv`.

## Zasady uczelni

Zanim użyjesz zapisanych tekstów w pracy zaliczeniowej, sprawdź zasady swojej uczelni i prowadzącego dotyczące korzystania z AI.

## Uwagi do testu

Kontakt do zgłaszania uwag: Denis Pokropski, 285421@student.uwr.edu.pl.

KAIWA SUITE · 26.01 · wersja 0.2.1 · wersja robocza / draft
