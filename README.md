# KAIWA

<img src="logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Kit for Academic Inquiry With AI. Po japońsku *kaiwa* znaczy rozmowa. In Japanese, *kaiwa* means conversation.

Produkt 26.01, wersja 0.2.0 (robocza), 05.11.2026, nie wydana. Product 26.01, version 0.2.0 (draft), not released.
Wydawca / publisher: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo / BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (KMSI), University of Wrocław, leading programme image communication, second discipline cultural studies. Kontakt / contact: 285421@student.uwr.edu.pl.

Pakiet do przetestowania metody pracy z AI w naukach humanistycznych i społecznych: myśli mówione na głos zapisuje się dosłownie ze skrótem SHA-256, tematy z dyktatów tworzą mapę kontekstu, artefakty analizuje się po triażu według deklarowanych ram, literaturę szuka się w otwartym dostępie z poziomem weryfikacji każdego trafienia. A package to test a method of AI-assisted work in the humanities and social sciences: verbatim dictation with SHA-256 hashes, a context map, triage-first framework analysis, and open access search with a verification level for every hit.

## Agenci Copilot / Copilot agents

| Folder | Agent | Stan / status |
|---|---|---|
| `copilot/strumien/` | KAIWA: strumień świadomości | gotowy, test w Copilot w toku / ready, Copilot test pending |
| `copilot/mapa/` | KAIWA: mapa kontekstu | roboczy, nieprzetestowany / draft, untested |
| `copilot/analiza/` | KAIWA: analiza (triaż, dalszy krok, język wyniku i kontekst kulturowy, ramy, blok kontroli kulturowej) | roboczy, nieprzetestowany / draft, untested |
| `copilot/zrodla/` | KAIWA: źródła (otwarty dostęp) | roboczy, nieprzetestowany / draft, untested |

Konfiguracja: `SETUP.pl.md` (wszyscy agenci) i `SETUP.en.md` (strumień świadomości i jedna uwaga o agencie analizy). Setup: `SETUP.pl.md` covers all agents, `SETUP.en.md` the stream agent and one note on the analysis agent.

## Pozostałe pliki / other files

| Plik albo folder / file or folder | Treść / content |
|---|---|
| `esej/uzasadnienie-metody.de.md` | Esej: dlaczego ta metoda, motywacja, problem, powstanie koncepcji, realizacja (po niemiecku) / essay on motivation, problem, concept and implementation (German) |
| `logo/` | Logo KAIWA „warp mode”: domyślnie czarno-białe, do wyboru tryby spectrum i SHIFT, wskaźnik stanu w prawym dolnym rogu (`status/`, `tools/logo_status.py`) / logo “warp mode”: black and white by default, spectrum and SHIFT modes as options, status indicator bottom right |
| `KONTEKST.pl.md` | Mapa kontekstu: opis metody / context map: method |
| `szablony/karta-problemu-badawczego.pl.md` | Karta problemu badawczego: osiem pól i lista kryteriów / research problem card |
| `szablony/po-triazu.pl.md` | Po triażu: dalszy krok i język wyniku, z tekstem do wklejenia / after triage: next step and output language |
| `szablony/kontrola-kulturowa.pl.md` | Kontrola kulturowa: pytanie o kontekst, blok na końcu wyniku, lista kontrolna, tekst do wklejenia / cultural check: context question, closing block, checklist, paste text |
| `szablony/ujawnienie-narzedzia.pl.md` | Ujawnienie narzędzia: platforma, model, liczba uruchomień kodu, nakład, z listą kontrolną / tool disclosure: platform, model, code runs, effort, with checklist |
| `prompts/` | Triaż, katalog ram, ramy kulturoznawcze i nauk społecznych, kopie z prompt-library (mentalpinG-Ops, CC BY-SA 4.0) / triage, catalogue and frameworks |
| `protokoly/` | Osiem protokołów humanities-ai-methodology (Denis Pokropski, CC BY-SA 4.0) / eight protocols |
| `office/` | Protokoły w Word i Excel bez AI, `rejestry.xlsx` / the protocols in Word and Excel without AI |
| `tools/diktat_ledger.py` | Rejestr skrótów dla dziennika w Markdown / hash ledger for a Markdown journal |
| `tools/kontekst.py` | Sprawdzenie pliku mapy, wymaga openpyxl / map file check, needs openpyxl |
| `tools/szukaj.py` | Szukanie w OpenAlex, Crossref i DOAJ, tylko biblioteka standardowa / search in three open catalogues |
| `tools/office.py` | Buduje `office/rejestry.xlsx`, wymaga openpyxl / builds the Excel registers |
| `tools/test_paket.py` | Testy pakietu / package tests |

## Gdy coś nie działa / fallbacks

Każdy agent ma w instrukcjach drogi zapasowe. Kolejność: agenci Copilot, potem dowolny asystent AI z plikami pakietu, potem Word i Excel bez AI (`office/README.pl.md`). Every agent has fallbacks in its instructions, then any AI assistant with the package files, then Word and Excel without AI.

## Licencje / licences

`prompts/` i `protokoly/` są na licencji CC BY-SA 4.0, szczegóły w `LICENSE.md` w każdym z tych folderów. Licencja reszty pakietu zostanie ustalona przed wydaniem. The folders `prompts/` and `protokoly/` are CC BY-SA 4.0. The licence of the rest is set before release.

Tryby „sprint“ i „przekład na polski“ dojdą po decyzjach autora. Sprint and transfer into Polish follow after the author's decisions.

Przed wydaniem / before release: sprawdzenie polskiego tekstu przez autora, test agentów w Copilot, licencja reszty pakietu, kontrola przed publikacją.
