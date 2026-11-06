# KAIWA: instrukcja konfiguracji (Microsoft 365 Copilot)

<img src="logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Produkt 26.01, wersja 0.2.0 (robocza), 05.11.2026. Nie wydana. Wydawca: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo, nr indeksu 285421, kontakt: 285421@student.uwr.edu.pl. Pakiet jest propozycją, żeby przetestować metodę: myśli mówione na głos zapisuje się dosłownie, a każdy wpis dostaje skrót SHA-256, który później pokazuje, że tekst się nie zmienił.

## Czego potrzebujesz

1. Konto uczelniane z dostępem do Microsoft 365 Copilot Chat. Licencja Copilot nie jest potrzebna.
2. Około dziesięciu minut na konfigurację.
3. Python 3.8 lub nowszy tylko wtedy, gdy chcesz sprawdzać pliki na własnym komputerze. To jest opcjonalne.

## Konfiguracja agenta

Nazwy przycisków mogą się różnić w zależności od języka interfejsu. Poniżej podane są nazwy angielskie z dokumentacji Microsoft.

1. Otwórz Copilot w przeglądarce i wybierz po lewej stronie „Agents“, a potem „New agent“.
2. Wybierz konfigurację ręczną („Configure“, „Skip to configure“).
3. Wklej nazwę, opis i podpowiedzi startowe z pliku `copilot/strumien/AGENT.md`.
4. Wklej do pola instrukcji całą zawartość pliku `copilot/strumien/INSTRUCTIONS.txt`.
5. W sekcji wiedzy nic nie dodawaj.
6. Zapisz agenta („Create“).

## Pierwszy test

1. Otwórz agenta i napisz „start“.
2. Agent powinien pokazać krótki kod i wynik „OK“. To znaczy, że naprawdę wykonuje kod i potrafi liczyć skróty.
3. Jeśli zamiast tego pojawi się ostrzeżenie, że skróty nie są możliwe, sesja zostanie zapisana bez nich. Agent nie może wtedy wymyślać skrótów.
4. Powiedz albo napisz dwa zdania, potem „koniec“. Agent pokaże listę tematów i nazwę pliku Excel.

## Ostrzeżenia dotyczące użycia

1. Copilot Chat bez licencji ma limity użycia. Microsoft pisze w dokumentacji „Usage limits apply to all included features“ i nie podaje liczb. Agent uruchamia kod tylko dwa razy na sesję, na początku i na końcu, żeby zużycie było małe.
2. Nie dodawaj plików z OneDrive ani SharePoint jako wiedzy agenta. Bez licencji Copilot to nie działa albo jest rozliczane jako płatne użycie.
3. Długa sesja jest mniej pewna. Po dwudziestu wpisach agent proponuje zakończenie. Zakończ wtedy i zacznij nową sesję.
4. Skrót pokazuje, że tekst w pliku nie zmienił się od końca sesji. Nie pokazuje, że model przepisał twoje słowa dokładnie. Przeczytaj plik raz po zakończeniu sesji.

## Gdzie są pliki

Każda sesja daje jeden plik `dictation-RRRR-MM-DD-GGMM.xlsx` z dwoma arkuszami: „entries“ (wpisy z tekstem) i „register“ (skróty, liczba znaków i słów, bez tekstu). Pliki Excel z interpretera kodu trafiają zwykle same do OneDrive, do folderu Copilot. Tak było w teście na koncie UWr 17.10.2026, ale Microsoft tego nie gwarantuje. Trzeci arkusz „tool“ zapisuje narzędzie, model (tak, jak podaje czat), liczbę uruchomień kodu i nakład, a czego nie wiadomo, oznacza „unknown“. Arkusz nie ma skrótu, więc przeczytaj go raz (`szablony/ujawnienie-narzedzia.pl.md`). Agent zawsze proponuje też pobranie pliku. Copilot nie nadpisuje plików, dlatego folder działa jak rejestr, do którego się tylko dopisuje. Możesz przenosić pliki do własnego folderu, na przykład „KAIWA“.

## Sprawdzanie

1. W Copilot dołącz plik sesji do rozmowy z agentem i napisz „sprawdź ten plik“. Agent policzy skróty jeszcze raz i poda przy każdym wpisie, czy tekst się zmienił.
2. Na własnym komputerze, jeśli prowadzisz dziennik w plikach Markdown: `python tools/diktat_ledger.py init <folder>`, potem `scan <folder>` i `verify <folder>`. Skrypt używa tej samej reguły skrótu co agent.

## Drugi agent: mapa kontekstu

Opcjonalnie. Opis metody: `KONTEKST.pl.md`. Ta część nie była jeszcze testowana w Copilot.

1. Utwórz drugiego agenta tak samo jak pierwszego.
2. Nazwę, opis i podpowiedzi startowe weź z pliku `copilot/mapa/AGENT.md`, instrukcje z pliku `copilot/mapa/INSTRUCTIONS.txt`.
3. W sekcji wiedzy nic nie dodawaj. Pliki dołączasz do rozmowy.
4. Napisz „start“. Agent powinien odpowiedzieć „Mapa gotowa. Skróty działają.“
5. Dołącz plik dyktatu z pierwszego agenta i napisz „dodaj dołączone dyktaty do mapy“. Zatwierdź propozycje numerami, potem napisz „zapisz“.
6. Na własnym komputerze możesz sprawdzić plik mapy: `python tools/kontekst.py sprawdz <plik mapy>` (wymaga pakietu openpyxl).

## Trzeci agent: analiza

Opcjonalnie. Ta część nie była jeszcze testowana w Copilot.

1. Utwórz agenta z pól w `copilot/analiza/AGENT.md` i instrukcji z `copilot/analiza/INSTRUCTIONS.txt`.
2. W rozmowie dołącz artefakt oraz pliki `prompts/core/artifact-triage.md` i `prompts/framework-catalog.md`. Bez nich agent użyje triażu minimalnego i nie poleci ram.
3. Po triażu agent pyta o dalszy krok (1 dalej, 2 komentarz albo zlecenie, 3 problem badawczy), potem o język wyniku i o kontekst kulturowy artefaktu. Wynik kończy się blokiem „Kontrola kulturowa“. Przebieg: `szablony/po-triazu.pl.md`, lista kontrolna: `szablony/kontrola-kulturowa.pl.md`.
4. Gdy agent poleci ramy, dołącz ich pliki z `prompts/cultural-scientific/` albo `prompts/social-science/`.

## Czwarty agent: źródła

Opcjonalnie. Ta część nie była jeszcze testowana w Copilot.

1. Utwórz agenta z pól w `copilot/zrodla/AGENT.md` i instrukcji z `copilot/zrodla/INSTRUCTIONS.txt`.
2. W sekcji wiedzy dodaj cztery strony z `AGENT.md`. Bez nich agent szuka w całej sieci, a wyniki wymagają ostrożniejszej oceny.
3. Na własnym komputerze możesz szukać bez Copilot: `python tools/szukaj.py "hasło" --csv wynik.csv`. Plik ma kolumny arkusza „zrodla“ z `office/rejestry.xlsx`.

## Bez Copilot

Gdy agenci nie działają: prompty i protokoły działają w każdym asystencie AI, a rejestry w Excel także bez AI. Opis: `office/README.pl.md`.

## Zasady uczelni

Zanim użyjesz zapisanych tekstów w pracy zaliczeniowej, sprawdź zasady swojej uczelni i prowadzącego dotyczące korzystania z AI.

## Uwagi do testu

Kontakt do zgłaszania uwag: Denis Pokropski, nr indeksu 285421, 285421@student.uwr.edu.pl.
