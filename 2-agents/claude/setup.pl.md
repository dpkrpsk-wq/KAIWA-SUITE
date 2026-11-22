# KAIWA: konfiguracja (Claude)

<img src="../../design/logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Produkt 26.01, wersja 0.2.0 (robocza), 22.11.2026. Nie wydana. Wydawca: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski.

Status: wersja robocza, nieprzetestowana w Claude. Instrukcja opisuje dwie drogi: projekty w claude.ai (w przeglądarce, aplikacja desktop Claude niesprawdzona) i skille w Claude Code. Instrukcje powstały na podstawie drogi ChatGPT w tym pakiecie.

## Pobranie pakietu

Otwórz stronę pakietu https://dpkrpsk-wq.github.io/KAIWA-SUITE/, wybierz dostawcę „Claude” i naciśnij przycisk pobierania. Rozpakuj plik ZIP do wybranego folderu. Wszystkie ścieżki w tej instrukcji zaczynają się w tym folderze.

Która droga do ciebie pasuje: droga A wymaga tylko przeglądarki i pasuje większości osób. Droga B jest dla osób, które już używają Claude Code, programu uruchamiającego Claude w terminalu na własnym komputerze.

## Czego potrzebujesz

1. Droga A, claude.ai: konto Claude. Projekty są dostępne we wszystkich planach, konto bezpłatne może utworzyć do pięciu projektów. Ustawienie „Code execution and file creation” (w nowszym układzie ustawień „Create and edit files”) musi być włączone (Settings, Capabilities), inaczej nie powstaną pliki Excel.
2. Droga B, Claude Code: Claude Code na twoim komputerze, Python 3.8 lub nowszy i pakiet Pythona openpyxl (`pip install openpyxl`).
3. Około dziesięciu minut na cztery moduły.

## Cztery moduły

| Moduł | Droga A: folder projektu | Droga B: skill | Pliki projektu | Status |
|---|---|---|---|---|
| KAIWA: strumień świadomości | `2-agents/claude/stream/` | `2-agents/claude/code/kaiwa-stream/` | 1 | wersja robocza, nieprzetestowana w Claude |
| KAIWA: mapa kontekstu | `2-agents/claude/map/` | `2-agents/claude/code/kaiwa-map/` | 3 | wersja robocza, nieprzetestowana w Claude |
| KAIWA: analiza | `2-agents/claude/analysis/` | `2-agents/claude/code/kaiwa-analysis/` | 8 | wersja robocza, nieprzetestowana w Claude |
| KAIWA: źródła | `2-agents/claude/sources/` | `2-agents/claude/code/kaiwa-sources/` | 2 | wersja robocza, nieprzetestowana w Claude |

Każdy folder projektu zawiera `PROJECT.md` (nazwa, opis, pierwsza wiadomość), `INSTRUCTIONS.txt` (instrukcje projektu) i `files.txt` (pliki projektu). Każdy folder skilla zawiera jeden plik `SKILL.md` z tymi samymi instrukcjami i krótkim wstępem dla Claude Code. Skill to folder z instrukcjami, które Claude Code wczytuje, gdy go wywołasz. Wiedza projektu w claude.ai to pliki, które Claude czyta w każdej rozmowie tego projektu.

## Droga A: jeden projekt w claude.ai

1. W claude.ai utwórz nowy projekt i nadaj mu nazwę z `PROJECT.md`. Aplikacja desktop powinna oferować te same projekty, to jest niesprawdzone.
2. Wybierz „Set project instructions” i wklej całą zawartość `INSTRUCTIONS.txt`. Instrukcje strumienia świadomości (`stream/INSTRUCTIONS.txt`) są po angielsku i tak zostają, bo to tekst dla modelu (prompt), nie dla czytelnika.
3. Dodaj pliki z listy `files.txt` do wiedzy projektu („+” w obszarze wiedzy projektu).
4. W projekcie zacznij nową rozmowę pierwszą wiadomością z `PROJECT.md`.

W sprawdzonych stronach pomocy nie znaleźliśmy limitu długości instrukcji projektu. Instrukcje w tym folderze mieszczą się w 8000 znaków, limicie Copilot.

## Droga B: skille w Claude Code

1. Otwórz terminal w folderze pakietu KAIWA (folder z `README.md`).
2. Skopiuj cztery foldery z `2-agents/claude/code/` do folderu `.claude/skills/` w folderze pakietu, tak aby istniał na przykład `.claude/skills/kaiwa-stream/SKILL.md`. Folder, którego nazwa zaczyna się od kropki, może być ukryty w menedżerze plików. W Windows (PowerShell): `New-Item -ItemType Directory -Force .claude/skills; Copy-Item -Recurse 2-agents/claude/code/* .claude/skills/`. W macOS i Linux: `mkdir -p .claude/skills && cp -r 2-agents/claude/code/* .claude/skills/`.
3. Uruchom Claude Code w folderze pakietu i napisz na przykład `/kaiwa-stream` albo „start” z krótką informacją, o który moduł chodzi.

Skille czytają pliki projektu z folderu pakietu i zapisują pliki Excel w bieżącym folderze. Niczego nie instalują. Gdy brakuje openpyxl, skill to mówi.

Skille są napisane dla Claude Code. W claude.ai używaj projektów z drogi A.

## Pierwszy test

1. W module „strumień świadomości” napisz „start”. Claude powinien uruchomić krótki kod w Pythonie i pokazać „OK”. Samo „OK” nie dowodzi, że kod działa, więc po sesji sprawdź plik.
2. Wpisz dwa zdania testowe, potem napisz „koniec”. Sprawdź plik `dictation-RRRR-MM-DD-GGMM.xlsx` i jego arkusze „entries”, „register” i „tool”.

## Pliki między sesjami

1. Droga A: pliki, które Claude tworzy w rozmowie, pobieraj od razu. Nie zakładaj, że zostaną dostępne po zakończeniu rozmowy (niesprawdzone w Claude).
2. Mapa kontekstu: na początku każdej sesji ustal z Claude, który plik mapy obowiązuje w tej sesji. W claude.ai dołącz go do rozmowy, w Claude Code podaj jego ścieżkę. Po każdej zmianie zachowaj nowy plik.
3. To, co Claude pamięta z wcześniejszych rozmów, nie jest dowodem pochodzenia. Pochodzenie stoi tylko w kolumnach pliku mapy.

## Ostrzeżenia

1. Wiadomość podyktowana głosem liczy się jako twoje oryginalne słowa. Transkrypcja może jednak różnić się od tego, co powiedziałeś, więc po sesji przeczytaj plik.
2. Skrót SHA-256 pokazuje, czy tekst w pliku zgadza się ze skrótem. Nie pokazuje, że model przepisał twoje słowa dokładnie. Skrót „sha256” jest liczony po normalizacji Unicode (NFC) i scaleniu spacji i podziałów wiersza. Drugi skrót „sha256_raw” jest liczony z dokładnych bajtów tekstu. Porównany ręcznie z tekstem pokazuje też zmiany odstępów, sprawdzenie w agencie porównuje tylko „sha256”. Oba skróty chronią tekst w postaci przejętej przez model, nie to, co powiedziałeś.
3. Wiersz „tool” (arkusz „tool”, wiersz „Narzędzie”) prowadź osobno dla każdej rozmowy albo sesji. Nazwa modelu pochodzi z rozmowy i nie jest niezależnym dowodem.
4. Blok „Kontrola kulturowa” w analizie to samoopis modelu, nie niezależna kontrola.
5. Strony otwartego dostępu w module źródeł są preferencją wyszukiwania, nie ograniczeniem technicznym. Wyszukiwanie w sieci w claude.ai zależy od konta i jego ustawień (niesprawdzone dla tego pakietu).
6. Skrypt `tools/search.py` uruchamiaj na własnym komputerze. Jest tylko w pełnym pakiecie, wydanie bez skryptów go nie ma.

## Źródła o platformie

Sprawdzone 22.11.2026:

1. „What are projects?”, https://support.claude.com/en/articles/9517075-what-are-projects: projekty we wszystkich planach, konta bezpłatne do pięciu projektów.
2. „How can I create and manage projects?”, https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects: instrukcje projektu i wiedza projektu.
3. „Create and edit files with Claude”, https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude: wykonywanie kodu i tworzenie plików, w przeglądarce i w aplikacji desktop, Settings, Capabilities.
4. Dokumentacja Claude Code, https://code.claude.com/docs/en/skills: skille w `.claude/skills/<nazwa>/SKILL.md` i `~/.claude/skills/`.

Strony pomocy opisują aplikację desktop tylko dla wykonywania kodu i tworzenia plików. To, że projekty działają tam tak samo, jest niesprawdzone.

## Zasady uczelni

Zanim użyjesz zapisanych tekstów w pracy na zajęcia, sprawdź zasady uczelni i prowadzącego dotyczące korzystania z AI.

## Uwagi

Kontakt: Denis Pokropski, 285421@student.uwr.edu.pl.

KAIWA SUITE · 26.01 · wersja 0.2.0 · wersja robocza / draft
