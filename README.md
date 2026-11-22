# KAIWA

<img src="design/logo/kaiwa-logo.svg" alt="KAIWA" width="96">

**Strona pakietu / package page:** [https://dpkrpsk-wq.github.io/KAIWA-SUITE/](https://dpkrpsk-wq.github.io/KAIWA-SUITE/)

**Pierwszy kontakt / first contact:** [https://dpkrpsk-wq.github.io/KAIWA-SUITE/1-start/first-contact.html](https://dpkrpsk-wq.github.io/KAIWA-SUITE/1-start/first-contact.html)

Kit for Academic Inquiry With AI. Po japońsku *kaiwa* znaczy rozmowa. In Japanese, *kaiwa* means conversation.

Produkt 26.01, wersja 0.2.0 (robocza), 22.11.2026, nie wydana. Product 26.01, version 0.2.0 (draft), not released.
Wydawca / publisher: Denis Pokropski, lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo / BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (KMSI), University of Wrocław, leading programme image communication, second discipline cultural studies. Kontakt / contact: 285421@student.uwr.edu.pl.

Pakiet do przetestowania metody pracy z AI w naukach humanistycznych i społecznych: myśli mówione na głos zapisuje się dosłownie ze skrótem SHA-256 (skrót nie dowodzi wierności przepisania, zob. setup), tematy z dyktatów tworzą mapę kontekstu, artefakty analizuje się po triażu (wstępnym rozpoznaniu, czym jest artefakt i które ramy do niego pasują) według deklarowanych ram (opisanych z góry sposobów analizy), literaturę szuka się w otwartym dostępie z poziomem weryfikacji każdego trafienia. A package to test a method of AI-assisted work in the humanities and social sciences: verbatim dictation with SHA-256 hashes, a context map, triage-first framework analysis, and open access search with a verification level for every hit.

## Agenci Copilot / Copilot agents

| Folder | Agent | Stan / status |
|---|---|---|
| `2-agents/copilot/stream/` | KAIWA: strumień świadomości | roboczy, pierwszy test na koncie UWr 17.10.2026 bez protokołu, pełny test w Copilot w toku / draft, first test on a university account on 17 Oct 2026 without a record, full Copilot test pending |
| `2-agents/copilot/map/` | KAIWA: mapa kontekstu | roboczy, nieprzetestowany / draft, untested |
| `2-agents/copilot/analysis/` | KAIWA: analiza (triaż, dalszy krok, język wyniku i kontekst kulturowy, ramy, blok kontroli kulturowej) | roboczy, nieprzetestowany / draft, untested |
| `2-agents/copilot/sources/` | KAIWA: źródła (otwarty dostęp) | roboczy, nieprzetestowany / draft, untested |

Konfiguracja: `1-start/setup.pl.md` (wszyscy agenci) i `1-start/setup.en.md` (strumień świadomości i jedna uwaga o agencie analizy). Setup: `1-start/setup.pl.md` covers all agents, `1-start/setup.en.md` the stream of consciousness agent and one note on the analysis agent.

## Moduły Gemini / Gemini modules

| Folder | Moduł / module | Stan / status |
|---|---|---|
| `2-agents/gemini/` | Te same cztery moduły dla Google Gemini, z `2-agents/gemini/setup.pl.md`, `2-agents/gemini/setup.en.md`, `setup-dialog.md` i `SKILL.md`, stan 22.11.2026 / the same four modules for Google Gemini, as of 22 November 2026 | roboczy, nieprzetestowany w Gemini / draft, untested in Gemini |

## Projekty ChatGPT / ChatGPT projects

| Folder | Projekt / project | Stan / status |
|---|---|---|
| `2-agents/chatgpt/` | Te same cztery moduły jako projekty ChatGPT (konto Go), z `2-agents/chatgpt/setup.pl.md` i `2-agents/chatgpt/setup.en.md`, w każdym folderze `PROJECT.md`, `INSTRUCTIONS.txt` i `files.txt` / the same four modules as ChatGPT projects (Go account) | roboczy, nieprzetestowany w ChatGPT / draft, untested in ChatGPT |

## Projekty Claude i skille / Claude projects and skills

| Folder | Projekt albo skill / project or skill | Stan / status |
|---|---|---|
| `2-agents/claude/` | Te same cztery moduły jako projekty w claude.ai (w przeglądarce, aplikacja desktopowa niesprawdzona) oraz jako skille w Claude Code (`2-agents/claude/code/kaiwa-*/SKILL.md`), z `2-agents/claude/setup.pl.md` i `2-agents/claude/setup.en.md`, w każdym folderze `PROJECT.md`, `INSTRUCTIONS.txt` i `files.txt` / the same four modules as projects in claude.ai (in the browser and in the desktop app) and as skills in Claude Code, with the setup guides in Polish and English | roboczy, nieprzetestowany w Claude / draft, untested in Claude |

## Pozostałe pliki / other files

| Plik albo folder / file or folder | Treść / content |
|---|---|
| `design/logo/` | Logo KAIWA „warp mode”: domyślnie czarno-białe, do wyboru tryby spectrum i SHIFT, wskaźnik stanu w prawym dolnym rogu (`status/`, `tools/logo_status.py`) / logo “warp mode”: black and white by default, spectrum and SHIFT modes as options, status indicator bottom right |
| `design/design-system/` | System wizualny KAIWA SUITE (Claude Design): tokeny i manifest, licencja czcionki warp do wyjaśnienia / visual system: tokens and manifest, licence of the warp font still open |
| `DISCLOSURE.md` | Ujawnienie narzędzi AI użytych przy powstaniu pakietu, wersja robocza / disclosure of the AI tools used to make the package, draft |
| `design/video-prompt.pl.md`, `design/video-prompt.en.md` | Blok do filmów 10 s w Gemini: kolory, opis znaku, ruch warp mode / prompt block for 10 second videos in Gemini |
| `index.html` | Strona pakietu (GitHub Pages) z czterema poziomami i czterema dostawcami, linki do plików / package page for GitHub Pages |
| `1-start/first-contact.html` | Strona pierwszego kontaktu w systemie wizualnym / first-contact page in the visual system |
| `1-start/context.pl.md` | Mapa kontekstu: opis metody / context map: method |
| `3-templates/research-problem-card.pl.md` | Karta problemu badawczego: osiem pól i lista kryteriów / research problem card |
| `3-templates/after-triage.pl.md` | Po triażu: dalszy krok i język wyniku, z tekstem do wklejenia / after triage: next step and output language |
| `3-templates/cultural-check.pl.md` | Kontrola kulturowa: pytanie o kontekst, blok na końcu wyniku, lista kontrolna, tekst do wklejenia / cultural check: context question, closing block, checklist, paste text |
| `3-templates/tool-disclosure.pl.md` | Ujawnienie narzędzia: platforma, model, liczba uruchomień kodu, nakład, z listą kontrolną / tool disclosure: platform, model, code runs, effort, with checklist |
| `method/prompts/` | Triaż, katalog ram, ramy kulturoznawcze i nauk społecznych, kopie z prompt-library (mentalpinG-Ops, CC BY-SA 4.0) / triage, catalogue and frameworks |
| `method/protocols/` | Osiem protokołów humanities-ai-methodology (Denis Pokropski, CC BY-SA 4.0) / eight protocols |
| `4-without-ai/` | Protokoły w Word i Excel bez AI, `registers.xlsx` / the protocols in Word and Excel without AI |
| `tools/` | Skrypty Python, opcjonalne, tylko w pełnym pakiecie. Wydanie bez skryptów ich nie zawiera, wtedy pomiń wszystkie wskazówki do `tools/` / optional Python scripts, only in the full package, a release without scripts leaves them out |
| `tools/dictation_ledger.py` | Rejestr skrótów dla dziennika w Markdown / hash ledger for a Markdown journal |
| `tools/context.py` | Sprawdzenie pliku mapy, wymaga openpyxl / map file check, needs openpyxl |
| `tools/search.py` | Szukanie w OpenAlex, Crossref i DOAJ (otwarte katalogi publikacji naukowych), tylko biblioteka standardowa / search in three open catalogues |
| `tools/office.py` | Buduje `4-without-ai/registers.xlsx` (wymaga openpyxl) i `4-without-ai/kaiwa-template.docx` (wymaga python-docx) / builds the Excel registers |
| `tools/pdf.py` | Buduje PDF dokumentów pakietu (lista w skrypcie) w systemie wizualnym KAIWA SUITE do `dist/pdf/` (nie w repozytorium), wymaga pakietu markdown i przeglądarki Edge albo Chrome / builds a PDF of each document in the KAIWA SUITE design |
| `4-without-ai/kaiwa-template.docx` | Szablon Word z formatami KAIWA SUITE (kolory, czcionka, nagłówek, stopka z ⟨commit⟩), budowany przez `tools/office.py` / Word template with the KAIWA SUITE styles |
| `tools/test_package.py` | Testy pakietu / package tests |

## Gdy coś nie działa / fallbacks

Każdy agent ma w instrukcjach drogi zapasowe. Kolejność: agenci Copilot, potem dowolny asystent AI z plikami pakietu, potem Word i Excel bez AI (`4-without-ai/README.pl.md`). Every agent has fallbacks in its instructions, then any AI assistant with the package files, then Word and Excel without AI.

## Licencje / licences

Treść własna pakietu jest na licencji CC BY-NC-SA 4.0 (Creative Commons Uznanie autorstwa, Użycie niekomercyjne, Na tych samych warunkach). Treść własna ma dwie licencje (dual licence): licencja komercyjna na zapytanie, mentalpingoperator@gmail.com, warunki w [`LICENSE-COMMERCIAL.md`](LICENSE-COMMERCIAL.md). `method/prompts/` i `method/protocols/` pozostają na licencji CC BY-SA 4.0, czcionka w `design/fonts/` na licencji SIL Open Font License 1.1. Zakres według folderów i pełny tekst: `LICENSE`. The package's own content is dual-licensed: CC BY-NC-SA 4.0, and a commercial licence on request, terms in [`LICENSE-COMMERCIAL.md`](LICENSE-COMMERCIAL.md). `method/prompts/` and `method/protocols/` stay CC BY-SA 4.0, the font in `design/fonts/` is under the SIL Open Font License 1.1. Scope by folder and full text: `LICENSE`.

Tryby „sprint“ i „przekład na polski“ dojdą po decyzjach autora. Sprint and transfer into Polish follow after the author's decisions.

Przed wydaniem / before release: sprawdzenie polskiego tekstu przez autora, test agentów w Copilot, kontrola przed publikacją.
