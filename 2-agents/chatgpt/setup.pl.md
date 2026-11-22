# KAIWA: instrukcja konfiguracji (ChatGPT)

<img src="../../design/logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Produkt 26.01, wersja 0.2.0 (robocza), 22.11.2026. Nie wydana. Wydawca: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo, kontakt: 285421@student.uwr.edu.pl. Pakiet przenosi metodę KAIWA do ChatGPT. Każdy z czterech agentów to osobny projekt (Projects), czyli folder w ChatGPT z własnymi instrukcjami, plikami i rozmowami.

Stan: wersja robocza, nieprzetestowana w ChatGPT. Opis dotyczy konta ChatGPT Go. Własnych GPT (Custom GPTs) pakiet nie używa.

## Czego potrzebujesz

1. Konto ChatGPT Go z dostępem do projektów (Projects).
2. Około dziesięciu minut na cztery projekty.
3. Python 3.8 lub nowszy tylko wtedy, gdy chcesz sprawdzać pliki na własnym komputerze. To jest opcjonalne.

## Cztery projekty

| Projekt | Folder | Pliki projektu | Stan |
|---|---|---|---|
| KAIWA: strumień świadomości | `2-agents/chatgpt/stream/` | 1 | roboczy, nieprzetestowany w ChatGPT |
| KAIWA: mapa kontekstu | `2-agents/chatgpt/map/` | 3 | roboczy, nieprzetestowany w ChatGPT |
| KAIWA: analiza | `2-agents/chatgpt/analysis/` | 8 | roboczy, nieprzetestowany w ChatGPT |
| KAIWA: źródła | `2-agents/chatgpt/sources/` | 2 | roboczy, nieprzetestowany w ChatGPT |

W każdym folderze: `PROJECT.md` (nazwa, opis, pierwsza wiadomość), `INSTRUCTIONS.txt` (instrukcje projektu) i `files.txt` (pliki projektu).

## Konfiguracja jednego projektu

1. W ChatGPT utwórz nowy projekt i nadaj mu nazwę z `PROJECT.md`.
2. W menu projektu (•••) wybierz „Project settings” i wklej do instrukcji całą zawartość `INSTRUCTIONS.txt`. Instrukcja strumienia świadomości (`stream/INSTRUCTIONS.txt`) jest po angielsku i tak zostaje, bo to tekst dla modelu (prompt), nie dla czytelnika. Powstała z instrukcji Copilot i na tej platformie nie była testowana. Instrukcja każe agentowi odpowiadać w języku użytkownika, ale jej stałe krótkie odpowiedzi są po angielsku.
3. Dodaj do projektu pliki z `files.txt`. Każda lista ma najwyżej 10 plików, więc wystarczy jedno wgranie.
4. Zacznij nową rozmowę w projekcie od pierwszej wiadomości z `PROJECT.md`.

Długość instrukcji: pomoc OpenAI „Projects in ChatGPT” (sprawdzona 22.11.2026) nie podaje granicy. Użytkownicy piszą o około 8000 znaków (niesprawdzone), taką granicę ma Copilot. Instrukcje w tym folderze mają: strumień 6356, mapa 7466, analiza 7285 i źródła 4159 znaków, najwyżej 7466. Po zapisaniu sprawdź, czy instrukcje są całe (niesprawdzone w ChatGPT).

## Menu startowe (analiza)

W projekcie „KAIWA: analiza” dołącz plik i napisz „start” (także po angielsku albo niemiecku, lista w `analysis/SUIT-START-MENU.md`). ChatGPT powinien najpierw pokazać obraz `kaiwa-start-menu.png` i menu tekstowe: triaż, analiza ramą, problem badawczy, inne moduły. Przed twoim wyborem nie powinien analizować pliku. Nieprzetestowane w ChatGPT.

## Pierwszy test

1. W projekcie „strumień świadomości” napisz „start”. Agent powinien uruchomić krótki kod w Pythonie i pokazać „OK”. Samo „OK” nie dowodzi, że kod działa, dlatego po sesji sprawdź plik.
2. Napisz dwa zdania testowe, potem „koniec”. Pobierz plik `dictation-RRRR-MM-DD-GGMM.xlsx` i sprawdź arkusze „entries”, „register” i „tool”.

## Pliki między sesjami

1. Pliki, które agent tworzy w rozmowie, pobierasz od razu. Nie zakładaj, że zostaną dostępne po zakończeniu rozmowy (niesprawdzone w ChatGPT).
2. Mapa kontekstu: na początku każdej sesji ustalasz z agentem, który plik mapy obowiązuje w tej sesji, i dołączasz go do rozmowy. Po każdej zmianie pobierasz nowy plik.
3. Projekt może korzystać z wcześniejszych rozmów jako kontekstu. To nie jest dowód pochodzenia. Pochodzenie stoi tylko w kolumnach pliku mapy.

## Ostrzeżenia dotyczące użycia

1. Wiadomość podyktowana głosem liczy się jako twoje oryginalne słowa. Transkrypcja może jednak różnić się od tego, co powiedziałeś, dlatego przeczytaj plik po sesji.
2. Skrót SHA-256 pokazuje, czy tekst w pliku zgadza się ze skrótem. Nie pokazuje, że model przepisał twoje słowa dokładnie. Skrót „sha256” liczony jest po ujednoliceniu znaków (NFC), odstępów i podziałów wierszy, więc nie wykrywa zmian samych odstępów ani podziałów wierszy. Drugi skrót „sha256_raw” liczony jest z dokładnych bajtów tekstu. Porównany ręcznie z tekstem pokazuje także takie zmiany, sprawdzenie w agencie porównuje tylko „sha256”.
3. Wiersz „Narzędzie” (arkusz „tool”) prowadzisz osobno dla każdej rozmowy. Nazwa modelu pochodzi z czatu i nie jest niezależnym dowodem.
4. Blok „Kontrola kulturowa” w analizie to samoocena modelu, nie niezależne sprawdzenie.
5. Strony otwartego dostępu w agencie źródeł to preferencja wyszukiwania, nie techniczne ograniczenie.
6. Skrypt `tools/search.py` uruchamiasz na własnym komputerze, nie w rozmowie z ChatGPT. Jest tylko w pełnym pakiecie, w wydaniu bez skryptów go nie ma.

## Źródła informacji o platformie

Sprawdzone 22.11.2026 w pomocy OpenAI „Projects in ChatGPT”, https://help.openai.com/en/articles/10169521-projects-in-chatgpt:

1. Konta Go i Plus: do 25 plików w projekcie. Jednocześnie można wgrać 10 plików.
2. Instrukcje projektu ustawia się w menu projektu (•••), „Project settings”. Działają tylko w tym projekcie.
3. Projekty mogą używać swoich rozmów i plików jako kontekstu kolejnych odpowiedzi.

Pozostałe uwagi o ChatGPT pochodzą z raportu zgodności z 21.11.2026, który ChatGPT napisał sam o sobie, i są oznaczone jako niesprawdzone.

## Zasady uczelni

Zanim użyjesz zapisanych tekstów w pracy zaliczeniowej, sprawdź zasady swojej uczelni i prowadzącego dotyczące korzystania z AI.

## Uwagi do testu

Kontakt do zgłaszania uwag: Denis Pokropski, 285421@student.uwr.edu.pl.

KAIWA SUITE · 26.01 · wersja 0.2.0 · wersja robocza / draft
