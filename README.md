# KAIWA

<picture><source media="(prefers-color-scheme: dark)" srcset="design/logo/kaiwa-logo-hell.svg"><img src="design/logo/kaiwa-logo.svg" alt="KAIWA" width="240"></picture>

**Package page / strona pakietu:** [https://dpkrpsk-wq.github.io/KAIWA-SUITE/](https://dpkrpsk-wq.github.io/KAIWA-SUITE/)

**First contact / pierwszy kontakt:** [https://dpkrpsk-wq.github.io/KAIWA-SUITE/1-start/first-contact.html](https://dpkrpsk-wq.github.io/KAIWA-SUITE/1-start/first-contact.html)

**Download / pobieranie:** one ZIP per vendor on the [package page](https://dpkrpsk-wq.github.io/KAIWA-SUITE/) and in the [releases](https://github.com/dpkrpsk-wq/KAIWA-SUITE/releases). Steps per assistant: `get/copilot.html`, `get/gemini.html`, `get/chatgpt.html`, `get/claude.html` on the package page. / Jeden ZIP na dostawcę na stronie pakietu i w wydaniach. Kroki dla każdego asystenta na stronie pakietu.

Kit for Academic Inquiry With AI. In Japanese, *kaiwa* means conversation. Po japońsku *kaiwa* znaczy rozmowa.

Product 26.01, version 0.2.0 (draft), 22 November 2026, not released. Produkt 26.01, wersja 0.2.0 (robocza), 22.11.2026, nie wydana.
Publisher / wydawca: Denis Pokropski, BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (KMSI), University of Wrocław, leading programme image communication, second discipline cultural studies / lic. filozofii (Uniwersytet Wrocławski, 2019), student studiów II stopnia, Kolegium Międzydziedzinowych Studiów Indywidualnych (KMSI), Uniwersytet Wrocławski, kierunek wiodący komunikacja wizerunkowa, druga dyscyplina kulturoznawstwo. Contact / kontakt: 285421@student.uwr.edu.pl.

A package to test a method of AI-assisted work in the humanities and social sciences: verbatim dictation with SHA-256 hashes, a context map, triage-first framework analysis, and open access search with a verification level for every hit. Pakiet do przetestowania metody pracy z AI w naukach humanistycznych i społecznych: myśli mówione na głos zapisuje się dosłownie ze skrótem SHA-256 (skrót nie dowodzi wierności przepisania, zob. setup), tematy z dyktatów tworzą mapę kontekstu, artefakty analizuje się po triażu (wstępnym rozpoznaniu, czym jest artefakt i które ramy do niego pasują) według deklarowanych ram (opisanych z góry sposobów analizy), literaturę szuka się w otwartym dostępie z poziomem weryfikacji każdego trafienia.

## Copilot agents / Agenci Copilot

| Folder | Agent | Status / stan |
|---|---|---|
| `2-agents/copilot/stream/` | KAIWA: stream of consciousness / strumień świadomości | draft, first test on a university account on 17 Oct 2026 without a record, full Copilot test pending / roboczy, pierwszy test na koncie UWr 17.10.2026 bez protokołu, pełny test w Copilot w toku |
| `2-agents/copilot/map/` | KAIWA: context map / mapa kontekstu | draft, untested / roboczy, nieprzetestowany |
| `2-agents/copilot/analysis/` | KAIWA: analysis (triage, next step, output language and cultural context, frameworks, cultural check block) / analiza (triaż, dalszy krok, język wyniku i kontekst kulturowy, ramy, blok kontroli kulturowej) | draft, untested / roboczy, nieprzetestowany |
| `2-agents/copilot/sources/` | KAIWA: sources (open access) / źródła (otwarty dostęp) | draft, untested / roboczy, nieprzetestowany |

Setup: `1-start/setup.en.md` covers all four agents, `1-start/setup.pl.md` too. Konfiguracja: `1-start/setup.en.md` i `1-start/setup.pl.md` (wszyscy agenci).

## Gemini modules / Moduły Gemini

| Folder | Module / moduł | Status / stan |
|---|---|---|
| `2-agents/gemini/` | The same four modules for Google Gemini, with `2-agents/gemini/setup.en.md`, `2-agents/gemini/setup.pl.md`, `setup-dialog.md` and `SKILL.md`, as of 22 November 2026 / te same cztery moduły dla Google Gemini, stan 22.11.2026 | draft, untested in Gemini / roboczy, nieprzetestowany w Gemini |

## ChatGPT projects / Projekty ChatGPT

| Folder | Project / projekt | Status / stan |
|---|---|---|
| `2-agents/chatgpt/` | The same four modules as ChatGPT projects (Go account), with `2-agents/chatgpt/setup.en.md` and `2-agents/chatgpt/setup.pl.md`, in each folder `PROJECT.md`, `INSTRUCTIONS.txt` and `files.txt` / te same cztery moduły jako projekty ChatGPT (konto Go) | draft, untested in ChatGPT / roboczy, nieprzetestowany w ChatGPT |
| `2-agents/chatgpt/plugin/` | The same four modules as one ChatGPT plugin with four skills, available in every chat of the account, build: `python tools/chatgpt_plugin.py` / te same cztery moduły jako jedna wtyczka ChatGPT z czterema skillami, dostępna w każdym czacie konta | draft, untested in ChatGPT / roboczy, nieprzetestowany w ChatGPT |

## Claude projects and skills / Projekty Claude i skille

| Folder | Project or skill / projekt albo skill | Status / stan |
|---|---|---|
| `2-agents/claude/` | The same four modules as projects in claude.ai (in the browser, the desktop app is unverified) and as skills in Claude Code (`2-agents/claude/code/kaiwa-*/SKILL.md`), with `2-agents/claude/setup.en.md` and `2-agents/claude/setup.pl.md`, in each folder `PROJECT.md`, `INSTRUCTIONS.txt` and `files.txt` / te same cztery moduły jako projekty w claude.ai (w przeglądarce, aplikacja desktopowa niesprawdzona) oraz jako skille w Claude Code | draft, untested in Claude / roboczy, nieprzetestowany w Claude |

## Other files / Pozostałe pliki

| File or folder / plik albo folder | Content / treść |
|---|---|
| `design/logo/` | Logo KAIWA “K.”: K mark with a square, KAIWA wordmark and tagline, black and white by default, spectrum and SHIFT modes as options, status indicator in the square (`status/`, `tools/logo_status.py`) / logo KAIWA „K.”: znak K z kwadratem, napis KAIWA i podpis, domyślnie czarno-białe, do wyboru tryby spectrum i SHIFT, wskaźnik stanu w kwadracie |
| `design/design-system/` | Visual system KAIWA SUITE (Claude Design): tokens and manifest, licence of the warp font still open / system wizualny KAIWA SUITE: tokeny i manifest, licencja czcionki warp do wyjaśnienia |
| `DISCLOSURE.md` | Disclosure of the AI tools used to make the package, draft / ujawnienie narzędzi AI użytych przy powstaniu pakietu, wersja robocza |
| `design/video-prompt.pl.md`, `design/video-prompt.en.md` | Prompt block for 10 second videos in Gemini: colours, description of the mark, motion / blok do filmów 10 s w Gemini: kolory, opis znaku, ruch |
| `index.html`, `get/` | Package page (GitHub Pages) with one download card per vendor and one page of steps per assistant, English first / strona pakietu z kartą pobierania dla każdego dostawcy i stroną kroków dla każdego asystenta, angielski na pierwszym miejscu |
| `release/`, `tools/release.py` | File set of the release ZIPs (`release/sets.json`) and the script that builds them, see `release/README.md` / zestaw plików ZIP wydania i skrypt, który je buduje |
| `1-start/first-contact.html` | First-contact page in the visual system / strona pierwszego kontaktu w systemie wizualnym |
| `1-start/context.pl.md` | Context map: method / mapa kontekstu: opis metody |
| `3-templates/research-problem-card.pl.md` | Research problem card: eight fields and a list of criteria / karta problemu badawczego: osiem pól i lista kryteriów |
| `3-templates/after-triage.pl.md` | After triage: next step and output language, with paste text / po triażu: dalszy krok i język wyniku, z tekstem do wklejenia |
| `3-templates/cultural-check.pl.md` | Cultural check: context question, closing block, checklist, paste text / kontrola kulturowa: pytanie o kontekst, blok na końcu wyniku, lista kontrolna, tekst do wklejenia |
| `3-templates/tool-disclosure.pl.md` | Tool disclosure: platform, model, code runs, effort, with checklist / ujawnienie narzędzia: platforma, model, liczba uruchomień kodu, nakład, z listą kontrolną |
| `method/prompts/` | Triage, catalogue and frameworks of the cultural and social sciences, copies from prompt-library (mentalpinG-Ops, CC BY-SA 4.0) / triaż, katalog ram, ramy kulturoznawcze i nauk społecznych |
| `method/protocols/` | Eight protocols of humanities-ai-methodology (Denis Pokropski, CC BY-SA 4.0) / osiem protokołów |
| `4-without-ai/` | The protocols in Word and Excel without AI, `registers.xlsx` / protokoły w Word i Excel bez AI |
| `tools/` | Python scripts, optional, only in the full package. A release without scripts leaves them out, then skip every hint to `tools/` / skrypty Python, opcjonalne, tylko w pełnym pakiecie. Wydanie bez skryptów ich nie zawiera, wtedy pomiń wszystkie wskazówki do `tools/` |
| `tools/dictation_ledger.py` | Hash ledger for a Markdown journal / rejestr skrótów dla dziennika w Markdown |
| `tools/context.py` | Map file check, needs openpyxl / sprawdzenie pliku mapy, wymaga openpyxl |
| `tools/search.py` | Search in OpenAlex, Crossref and DOAJ (open catalogues of scholarly publications), standard library only / szukanie w OpenAlex, Crossref i DOAJ, tylko biblioteka standardowa |
| `tools/office.py` | Builds `4-without-ai/registers.xlsx` (needs openpyxl) and `4-without-ai/kaiwa-template.docx` (needs python-docx) / buduje rejestry Excel i szablon Word |
| `tools/pdf.py` | Builds a PDF of the package documents (list in the script) in the KAIWA SUITE design into `dist/pdf/` (not in the repository), needs the package markdown and the Edge or Chrome browser / buduje PDF dokumentów pakietu w systemie wizualnym KAIWA SUITE |
| `4-without-ai/kaiwa-template.docx` | Word template with the KAIWA SUITE styles (colours, font, header, footer with ⟨commit⟩), built by `tools/office.py` / szablon Word z formatami KAIWA SUITE |
| `tools/test_package.py` | Package tests / testy pakietu |

## When something does not work / Gdy coś nie działa

Every agent has fallbacks in its instructions: first the Copilot agents, then any AI assistant with the package files, then Word and Excel without AI (`4-without-ai/README.pl.md`). Każdy agent ma w instrukcjach drogi zapasowe. Kolejność: agenci Copilot, potem dowolny asystent AI z plikami pakietu, potem Word i Excel bez AI.

## Licences / Licencje

The package's own content is dual-licensed: CC BY-NC-SA 4.0, and a commercial licence on request, terms in [`LICENSE-COMMERCIAL.md`](LICENSE-COMMERCIAL.md). `method/prompts/` and `method/protocols/` stay CC BY-SA 4.0, the font in `design/fonts/` is under the SIL Open Font License 1.1. Scope by folder and full text: `LICENSE`. Treść własna pakietu jest na licencji CC BY-NC-SA 4.0 (Creative Commons Uznanie autorstwa, Użycie niekomercyjne, Na tych samych warunkach). Treść własna ma dwie licencje (dual licence): licencja komercyjna na zapytanie, mentalpingoperator@gmail.com, warunki w [`LICENSE-COMMERCIAL.md`](LICENSE-COMMERCIAL.md). `method/prompts/` i `method/protocols/` pozostają na licencji CC BY-SA 4.0, czcionka w `design/fonts/` na licencji SIL Open Font License 1.1. Zakres według folderów i pełny tekst: `LICENSE`.

Sprint and transfer into Polish follow after the author's decisions. Tryby „sprint“ i „przekład na polski“ dojdą po decyzjach autora.

Before release / przed wydaniem: the author checks the Polish text, the agents are tested in Copilot, a check before publication / sprawdzenie polskiego tekstu przez autora, test agentów w Copilot, kontrola przed publikacją.
