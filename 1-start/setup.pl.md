# KAIWA: instrukcja konfiguracji (Microsoft 365 Copilot)

<picture><source media="(prefers-color-scheme: dark)" srcset="../design/logo/kaiwa-logo-hell.svg"><img src="../design/logo/kaiwa-logo.svg" alt="KAIWA" width="240"></picture>

**Languages / języki:** [English](setup.en.md) · [Polski](setup.pl.md)

Produkt 26.01, wersja 0.2.0 (robocza), 22.11.2026. Nie wydana. Wydawca: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo, kontakt: 285421@student.uwr.edu.pl. Pakiet jest propozycją, żeby przetestować metodę: myśli mówione na głos zapisuje się dosłownie, a każdy wpis dostaje skrót SHA-256, który później pokazuje, czy tekst w pliku zgadza się ze skrótem.

## Pobranie pakietu

Otwórz stronę pakietu https://dpkrpsk-wq.github.io/KAIWA-SUITE/, wybierz dostawcę „Microsoft 365 Copilot” i naciśnij przycisk pobierania. Rozpakuj plik ZIP do wybranego folderu. Wszystkie ścieżki w tej instrukcji zaczynają się w tym folderze.

## Czego potrzebujesz

1. Konto uczelniane z dostępem do Microsoft 365 Copilot Chat. Licencja Copilot nie jest potrzebna.
2. Około dziesięciu minut na konfigurację. Zaczynaj rozmowę w polu z nazwą agenta (w teście: „Nachricht an KAIWA SUITE senden”). Jeśli pole nosi tylko nazwę „Copilot”, rozmowa toczy się poza agentem i jego zasady nie działają.
3. Python 3.8 lub nowszy tylko wtedy, gdy chcesz sprawdzać pliki na własnym komputerze. To jest opcjonalne.

## Konfiguracja agenta

Nazwy przycisków mogą się różnić w zależności od języka interfejsu. Poniżej podane są nazwy angielskie z dokumentacji Microsoft.

1. Otwórz Copilot w przeglądarce i wybierz po lewej stronie „Agents“, a potem „New agent“.
2. Wybierz konfigurację ręczną („Configure“, „Skip to configure“).
3. Wklej nazwę, opis i podpowiedzi startowe z pliku `2-agents/copilot/stream/AGENT.md`.
4. Jako ikonę („Icon“, „Upload“) wgraj plik `design/logo/kaiwa-icon-192.png`. Microsoft przyjmuje plik PNG do 192 × 192 pikseli i do 1 MB.
5. Wklej do pola instrukcji całą zawartość pliku `2-agents/copilot/stream/INSTRUCTIONS.txt`. Instrukcja jest po angielsku i tak zostaje, bo to tekst dla modelu (prompt), nie dla czytelnika. Pierwszą wersję przetestowano na koncie UWr 17.10.2026 (bez protokołu), obecna wersja jest od tego czasu zmieniona i nieprzetestowana. Instrukcja każe agentowi odpowiadać w języku użytkownika, ale jej stałe krótkie odpowiedzi są po angielsku.
6. W sekcji wiedzy nic nie dodawaj.
7. Zapisz agenta („Create“).

## Pierwszy test

1. Otwórz agenta i napisz „start“.
2. Agent powinien pokazać krótki kod i wynik „OK“. To wskazuje, że agent wykonuje kod. Samo „OK“ tego nie dowodzi, dlatego po sesji sprawdź plik.
3. Jeśli zamiast tego pojawi się ostrzeżenie, że skróty nie są możliwe, sesja zostanie zapisana bez nich. Agent nie może wtedy wymyślać skrótów.
4. Powiedz albo napisz dwa zdania, potem „koniec“. Agent pokaże listę tematów i nazwę pliku Excel.

## Ostrzeżenia dotyczące użycia

1. Copilot Chat bez licencji ma limity użycia. Microsoft pisze w dokumentacji „Usage limits apply to all included features“ (cytat niesprawdzony) i nie podaje liczb. Agent strumienia uruchamia kod tylko dwa razy na sesję, na początku i na końcu, żeby zużycie było małe. Agent mapy uruchamia go przy starcie, odczycie plików, zapisie i sprawdzaniu, sprawdzenie pliku dyktatu też uruchamia kod.
2. Nie dodawaj plików z OneDrive ani SharePoint jako wiedzy agenta. Bez licencji Copilot to nie działa albo jest rozliczane jako płatne użycie.
3. Długa sesja jest mniej pewna. Po dwudziestu wpisach agent proponuje zakończenie. Zakończ wtedy i zacznij nową sesję.
4. Skrót pokazuje, że tekst w pliku nie zmienił się od końca sesji. Nie pokazuje, że model przepisał twoje słowa dokładnie. Skrót „sha256” liczony jest po ujednoliceniu znaków (NFC), odstępów i podziałów wierszy, więc nie wykrywa zmian samych odstępów ani podziałów wierszy. Drugi skrót „sha256_raw” liczony jest z dokładnych bajtów tekstu. Porównany ręcznie z tekstem pokazuje także takie zmiany, sprawdzenie w agencie porównuje tylko „sha256”. Przeczytaj plik raz po zakończeniu sesji.

## Gdzie są pliki

Każda sesja daje jeden plik `dictation-RRRR-MM-DD-GGMM.xlsx` z trzema arkuszami: „entries“ (wpisy z tekstem), „register“ (skróty, liczba znaków i słów, bez tekstu) i „tool“ (opis niżej). Plik z Copilot ma we właściwościach (autor, ostatnio zmodyfikował) imię i nazwisko właściciela konta (test 22.11.2026). Sprawdź to, zanim go komuś przekażesz. Pliki Excel z interpretera kodu trafiają zwykle same do OneDrive, do folderu Copilot (niesprawdzone w dokumentacji Microsoft). Tak było w teście na koncie UWr 17.10.2026 (bez protokołu w pakiecie), ale Microsoft tego nie gwarantuje. Arkusz „tool“ zapisuje narzędzie, model (tak, jak podaje czat), liczbę uruchomień kodu i nakład, a czego nie wiadomo, oznacza „unknown“. Arkusz nie ma skrótu, więc przeczytaj go raz (`3-templates/tool-disclosure.pl.md`). Agent zawsze proponuje też pobranie pliku. Copilot nie nadpisuje plików (niesprawdzone), dlatego folder działa jak rejestr, do którego się tylko dopisuje. Możesz przenosić pliki do własnego folderu, na przykład „KAIWA“.

## Sprawdzanie

1. W Copilot dołącz plik sesji do rozmowy z agentem i napisz „sprawdź ten plik“. Agent policzy skróty jeszcze raz i poda przy każdym wpisie, czy tekst się zmienił.
2. Na własnym komputerze, jeśli prowadzisz dziennik w plikach Markdown: `python tools/dictation_ledger.py init <folder>`, potem `scan <folder>` i `verify <folder>`. Skrypt czyta pliki `journal/RRRR-MM-DD.md` z wierszami `Dosłownie (dyktowane): „...”`, nie czyta plików `.xlsx` z agenta. Skrypt używa tej samej reguły skrótu co agent.

## Drugi agent: mapa kontekstu

Opcjonalnie. Opis metody: `1-start/context.pl.md`. Ta część nie była testowana w tej postaci (osobni agenci). Wersję z jednym agentem i skillem sprawdzono 24.11.2026, zob. punkt 6 niżej.

1. Utwórz drugiego agenta tak samo jak pierwszego.
2. Nazwę, opis i podpowiedzi startowe weź z pliku `2-agents/copilot/map/AGENT.md`, instrukcje z pliku `2-agents/copilot/map/INSTRUCTIONS.txt`.
3. W sekcji wiedzy nic nie dodawaj. Pliki dołączasz do rozmowy.
4. Napisz „start“. Agent powinien odpowiedzieć „Mapa gotowa. Skróty działają.“
5. Dołącz plik dyktatu z pierwszego agenta i napisz „dodaj dołączone dyktaty do mapy“. Zatwierdź propozycje numerami, potem napisz „zapisz“.
6. Sprawdzenie w Copilot: dołącz plik mapy i plik `2-agents/copilot/map/sprawdz-mape.md`, napisz „sprawdź mapę”. Test 24.11.2026 (wersja z jednym agentem i skillem, nie te instrukcje): agent może napisać własny kod albo go nie uruchomić i wtedy nie wykryje zmiany w mapie. Zaufaj tylko odpowiedzi „MAPA OK” albo liście błędów z uruchomionego kodu (otwórz panel rozumowania w odpowiedzi i sprawdź, że kod z pliku się wykonał). Pewne jest tylko sprawdzenie na własnym komputerze: `python tools/context.py sprawdz <plik mapy>` (wymaga pakietu openpyxl).

## Trzeci agent: analiza

Opcjonalnie. Ta część nie była jeszcze testowana w Copilot.

1. Utwórz agenta z pól w `2-agents/copilot/analysis/AGENT.md` i instrukcji z `2-agents/copilot/analysis/INSTRUCTIONS.txt`.
2. W rozmowie dołącz artefakt oraz pliki `method/prompts/core/artifact-triage.md` i `method/prompts/framework-catalog.md`. Bez pliku triażu agent poprosi o niego i nie zrobi triażu ani nie poleci ram.
3. Po triażu agent pyta o dalszy krok (1 dalej, 2 komentarz albo zlecenie, 3 problem badawczy), potem o język wyniku i o kontekst kulturowy artefaktu. Wynik kończy się blokiem „Kontrola kulturowa“. Przebieg: `3-templates/after-triage.pl.md`, lista kontrolna: `3-templates/cultural-check.pl.md`.
4. Gdy agent poleci ramy, dołącz ich pliki z `method/prompts/cultural-scientific/`, `method/prompts/social-science/` albo `method/prompts/philosophical/`.

## Czwarty agent: źródła

Opcjonalnie. Ta część nie była jeszcze testowana w Copilot.

1. Utwórz agenta z pól w `2-agents/copilot/sources/AGENT.md` i instrukcji z `2-agents/copilot/sources/INSTRUCTIONS.txt`.
2. W sekcji wiedzy dodaj cztery strony z `AGENT.md`. Bez nich agent szuka w całej sieci, a wyniki wymagają ostrożniejszej oceny.
3. Instrukcje zawierają skrót protokołu źródeł. Pełny plik `method/protocols/source-protocol.md` możesz dołączyć do rozmowy.
4. Na własnym komputerze możesz szukać bez Copilot: `python tools/search.py "hasło" --csv wynik.csv`. Plik ma kolumny arkusza „zrodla“ z `4-without-ai/registers.xlsx`.

## Bez Copilot

Te same agenty jako moduły Gemini: `2-agents/gemini/setup.pl.md`, jako projekty ChatGPT: `2-agents/chatgpt/setup.pl.md`. Gdy agenci nie działają: prompty i protokoły działają w każdym asystencie AI, a rejestry w Excel także bez AI. Opis: `4-without-ai/README.pl.md`.

## Zasady uczelni

Zanim użyjesz zapisanych tekstów w pracy zaliczeniowej, sprawdź zasady swojej uczelni i prowadzącego dotyczące korzystania z AI.

## Źródła informacji o platformie

Odczytane 22.11.2026 w dokumentacji Microsoft Learn przez asystenta AI (autor nie sprawdził ich osobno):

1. Pola agenta i ikona (nazwa 30 znaków, opis 1000, instrukcje 8000, PNG do 192 × 192 pikseli i 1 MB): https://learn.microsoft.com/plugins/agent-builder-build-agents
2. Bez licencji Copilot działają agenci z instrukcjami i stronami publicznymi, inni tylko w płatnym rozliczeniu: https://learn.microsoft.com/copilot/plan/copilot-overview
3. W przeszukanych stronach (22.11.2026) nie znaleziono liczbowych limitów użycia: https://learn.microsoft.com/partner-center/announcements/2026-november

Długość instrukcji agentów (znaki, granica 8000): strumień 6223, mapa 7579, analiza 6601, źródła 4282. Wklejaj z pliku bez zmian, edytor z końcami wierszy CRLF może dodać znaki.

## Uwagi do testu

Kontakt do zgłaszania uwag: Denis Pokropski, 285421@student.uwr.edu.pl.
