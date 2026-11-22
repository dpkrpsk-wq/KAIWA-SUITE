# Mapa kontekstu

Dodatek roboczy do pakietu KAIWA (Kit for Academic Inquiry With AI), 22.11.2026. Nie wydany. Wydawca: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo, kontakt: 285421@student.uwr.edu.pl.

## Po co

Kto dyktuje swoje myśli codziennie, po kilku tygodniach ma setki wpisów. Mapa kontekstu zbiera z nich tematy, zapisuje, skąd każdy temat pochodzi, i pokazuje, jak tematy łączą się ze sobą i z celami. Daje trzy rzeczy:

1. Ma oddzielać własne myśli od tego, co dopowiedział asystent AI (agent nieprzetestowany). To ważne przy każdej pracy zaliczeniowej.
2. Pokazuje luki: tematy bez połączeń i grupy tematów, które się ze sobą nie stykają. Luka jest pytaniem do ciebie, nie zadaniem dla asystenta.
3. Pomaga ustalić kolejność pracy: co łączy się z twoimi celami, a co jest drobną sprawą bez wpływu na całość.

## Kontekst, nie reguły

Mapa mówi, nad czym myślisz i jak tematy się łączą. Nie mówi, co masz robić. Asystent, który z niej korzysta, łączy swoje odpowiedzi z twoimi tematami i mówi wprost, kiedy jakaś propozycja nie ma z nimi połączenia. Nie ocenia twoich tematów i nie dopisuje ich sam.

## Co jest w mapie

Plik Excel w formacie kontekst-1 (stały układ arkuszy i kolumn, który sprawdza `tools/context.py`) z czterema arkuszami:

1. „tematy“: identyfikator (na przykład A1), temat twoimi słowami, grupa, źródło (na przykład plik dyktatu i numer wpisu), pochodzenie.
2. „połączenia“: od, do, rodzaj, uzasadnienie, data potwierdzenia.
3. „cele“: identyfikator (na przykład CEL1), horyzont, cel, termin, źródło.
4. „rejestr“: skrót SHA-256 każdego wiersza. Pokazuje później, czy wiersz zmienił się od zapisu.

Pochodzenie tematu:

1. własne: myśl z twoich słów, asystent ją tylko zapisał
2. własne+asystent: treść twoja, układ albo dopowiedzenie od asystenta
3. asystent: propozycja asystenta, której nie było w twoich słowach
4. sesja: temat powstał w rozmowie z AI i udziałów nie da się rozdzielić
5. niejasne: brak informacji o pochodzeniu

Te kategorie odpowiadają znacznikom z protokołu pochodzenia (`method/protocols/provenance-protocol.md`): własne to [H], własne+asystent to [AI+], asystent to [AI], sesja to [H+AI]. Niejasne traktuj ostrożnie jak [AI], bo protokół każe w razie wątpliwości przypisywać raczej AI niż sobie.

Rodzaj połączenia:

1. jawne: notatka sama nazywa ten związek
2. treściowe: asystent widzi związek, notatki go nie nazywają
3. rozmowa: związek potwierdzony przez ciebie w rozmowie, z datą potwierdzenia

Horyzont celu: krótki, średni albo długi, według twojej oceny. Połączenie może prowadzić od tematu do celu. Tak mapa pokazuje, które tematy pracują na który cel.

## Jak to działa z agentami

1. Agent „KAIWA: strumień świadomości“ zapisuje dyktaty w plikach Excel.
2. Agent „KAIWA: mapa kontekstu“ czyta te pliki, proponuje tematy i połączenia i wpisuje tylko to, co zatwierdzisz numerami.
3. Na pytanie „co dalej“ agent porządkuje zadania, które wymienisz, najpierw według celów, z którymi się łączą, potem według liczby połączeń ich tematu. Zadanie bez połączenia z mapą stoi na końcu, z takim opisem. Bez arkusza celów agent nie ustala kolejności.
4. Plik mapy możesz dołączyć także do innych rozmów z asystentem AI jako kontekst.

Konfiguracja drugiego agenta: dla Copilot `1-start/setup.pl.md`, część „Drugi agent: mapa kontekstu“. Inni dostawcy: moduł „mapa kontekstu” w konfiguracji dostawcy (Copilot `1-start/setup.pl.md`, Gemini `2-agents/gemini/setup.pl.md`, ChatGPT `2-agents/chatgpt/setup.pl.md`, Claude `2-agents/claude/setup.pl.md`).

## Sprawdzanie

W Copilot dołącz plik mapy i napisz „sprawdź mapę“. Na własnym komputerze: `python tools/context.py sprawdz <plik mapy>` (wymaga pakietu openpyxl). Oba sposoby używają tych samych reguł, test pakietu pilnuje, żeby się nie rozjechały.

## Granice

1. Mapa zawiera twoje myśli i cele. Zostaje tam, gdzie zapisujesz swoje pliki. Nie udostępniaj jej bez namysłu.
2. Nie dodawaj mapy jako wiedzy agenta. Bez licencji Copilot agent korzysta tylko z instrukcji i stron publicznych, inne źródła wiedzy wymagają licencji albo płatnego rozliczenia za użycie (Microsoft Learn, Copilot overview, sprawdzone 22.11.2026). Dołączaj plik do rozmowy.
3. Skrót pokazuje tylko, że wiersz nie zmienił się od zapisu. Nie pokazuje, że temat jest dobrze nazwany ani że pochodzenie jest prawdziwe. Pochodzenie ustalasz ty.

## Skąd pomysł

Autor prowadzi taką mapę dla własnych notatek badawczych i używa jej jako kontekstu w pracy z asystentem AI. Ten dodatek przenosi sposób, nie treść.

## Stan

Wersja robocza. Agent mapy nie był jeszcze testowany w Copilot. Uwagi: Denis Pokropski, 285421@student.uwr.edu.pl.
