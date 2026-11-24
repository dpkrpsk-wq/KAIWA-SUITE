# KAIWA SUITE: menu startowe / start menu (ChatGPT, analiza)

KAIWA SUITE 26.01, wersja 0.2.0 (robocza / draft), 22.11.2026. Plik projektu „KAIWA: analiza” w ChatGPT. Instrukcje projektu odsyłają do tego pliku. / Project file of “KAIWA: analiza” in ChatGPT. The project instructions refer to this file.

## Kiedy / when

The user uploads or attaches a file and then sends a start word. Start words, also with other capitalisation, punctuation or small spelling variants:

| Język / language | Słowa startu / start words |
|---|---|
| polski | start, rozpocznij, zaczynamy, uruchom KAIWA, przejdź dalej |
| English | start, begin, let's begin, start KAIWA, proceed, let's get started |
| Deutsch | Start, los, beginnen, starte KAIWA, weiter mit KAIWA, lass uns beginnen |

A start word without a file also opens the menu. Then the first line of the menu asks for the file.

## Co robisz / what you do

1. Check that a file of the user is in this chat. Name it by its file name. Do not open, summarise, classify or interpret it.
2. Show the picture `kaiwa-start-menu.png` from the project files. Run Python and display the image (for example with PIL and display). If that fails, leave the picture out and say in one line that the picture could not be shown.
3. Below the picture show the text menu in the language of the start word. Use the labels from the table below exactly, in this order.
4. Wait for the choice. The user types the number or the name.
5. After the choice follow the instructions of the project:
   - 1: Krok 1 (triaż), then Krok 2 to Krok 5.
   - 2: show the list of frameworks of the package (section „Pliki” of the instructions), the user chooses, then Krok 3, Krok 4 and Krok 5 with that framework. Triage is skipped, so name the result „bez triażu / without triage”.
   - 3: the research problem card field by field (Krok 2, option 3), then Krok 1 and the further steps.
   - 4: tell the user which separate project to open (strumień świadomości, mapa kontekstu or źródła) and what to write there first, as in its `PROJECT.md`. Do nothing else in this project.
6. Never invent options, labels or design rules that are not in this file.

## Menu tekstowe / text menu

Plain text with Markdown. Chat cannot show colours, the colours are in the picture only.

| Nr | polski | English | Deutsch |
|---|---|---|---|
| tytuł / title | **KAIWA SUITE · analiza** | **KAIWA SUITE · analysis** | **KAIWA SUITE · Analyse** |
| wstęp / intro | Witaj. Plik „<nazwa>” jest w rozmowie. Nic jeszcze nie analizuję. | Welcome. The file “<name>” is in the chat. Nothing is analysed yet. | Willkommen. Die Datei „<Name>“ ist im Chat. Noch ist nichts analysiert. |
| 1 | **Triaż**: które ramy pasują do artefaktu (zalecany start) | **Triage**: which frameworks fit the artefact (recommended start) | **Triage**: welche Rahmen zum Artefakt passen (empfohlener Start) |
| 2 | **Analiza ramą**: rama z katalogu pakietu | **Framework analysis**: a framework from the package catalogue | **Rahmenanalyse**: ein Rahmen aus dem Katalog des Pakets |
| 3 | **Problem badawczy**: karta problemu badawczego | **Research problem**: research problem card | **Forschungsproblem**: Karte des Forschungsproblems |
| 4 | **Inne moduły KAIWA**: strumień świadomości, mapa kontekstu, źródła (osobne projekty) | **Other KAIWA modules**: stream of consciousness, context map, sources (separate projects) | **Andere KAIWA-Module**: Bewusstseinsstrom, Kontextkarte, Quellen (eigene Projekte) |
| koniec / end | Wpisz numer albo nazwę. | Type the number or the name. | Gib die Nummer oder den Namen ein. |

Przykład / example (polski):

```text
KAIWA SUITE · analiza
Witaj. Plik „ulotka.pdf” jest w rozmowie. Nic jeszcze nie analizuję.

1. Triaż: które ramy pasują do artefaktu (zalecany start)
2. Analiza ramą: rama z katalogu pakietu
3. Problem badawczy: karta problemu badawczego
4. Inne moduły KAIWA: strumień świadomości, mapa kontekstu, źródła (osobne projekty)

Wpisz numer albo nazwę.
```

## Obraz / picture

`kaiwa-start-menu.png` shows the same menu in the KAIWA SUITE visual system: black header with the logo, yellow signal stripes at 35 degrees, cards with a hard shadow, font Space Grotesk. Its source is `start-menu.html` in this folder. It uses only the tokens and components of `design/design-system/` and the mark "K." from `design/design-system/assets/Logos/`. The picture is bilingual, Polish and English. If the picture and this file differ, this file applies.

## Test / acceptance test

Upload a file, then send each start word once: „Start” (Deutsch), „Lass uns beginnen”, „Start” (English), „Let's begin”, „Rozpocznij”, „Zaczynamy”. Expected each time: the picture or the one-line note, the text menu in the language of the start word, no analysis, no summary, waiting for the choice. Status: untested in ChatGPT.
