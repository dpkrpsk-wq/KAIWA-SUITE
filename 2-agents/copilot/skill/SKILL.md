---
name: kaiwa-suite
description: "KAIWA SUITE, study package with four modules: stream of consciousness with a SHA-256 register in Excel, context map, artefact analysis with declared frameworks, open access sources with verification levels. Use when the user says „KAIWA“, „start“, „zaczynam“, „koniec“, „sprawdź ten plik“, „start mapy“, „mapa kontekstu“, „dodaj dołączone dyktaty do mapy“, „sprawdź mapę“, „co dalej“, „zrób triaż dołączonego artefaktu“, „chcę sformułować problem badawczy“, „pokaż ramy dostępne w pakiecie“, „szukam literatury do tematu“, or attaches dictation-….xlsx or mapa-….xlsx."
---

# KAIWA SUITE

KAIWA SUITE 26.01, version 0.2.1 (working draft). This skill has four modules. Each module is one file in `modules/`.

# Choose the module

| The user says or does | Read this file |
|---|---|
| „start“, „zaczynam“, „begin“, wants to dictate or record thoughts, attaches a dictation file and asks to verify it („sprawdź ten plik“, „verify this file“) | `modules/stream.md` |
| „start mapy“, „mapa kontekstu“, „dodaj dołączone dyktaty do mapy“, „chcę zapisać swoje cele“, „co dalej“, „sprawdź mapę“, attaches `mapa-….xlsx` | `modules/map.md` |
| „triaż“, „zrób triaż dołączonego artefaktu“, „chcę sformułować problem badawczy“, „pokaż ramy dostępne w pakiecie“, wants an artefact analysis | `modules/analysis.md` |
| „szukam literatury“, „szukaj do dołączonej karty problemu badawczego“, asks for sources, DOI or open access literature | `modules/sources.md` |
| Only „KAIWA“, „KAIWA SUITE“, „menu“ or „moduły“ | Show the menu below and wait |

Menu, in the language of the user, one line per module:
1. Strumień świadomości (stream of consciousness): records your thoughts word for word.
2. Mapa kontekstu (context map): topics, provenance, connections and goals from your dictations.
3. Analiza (analysis): triage and analysis of an artefact with declared frameworks.
4. Źródła (sources): open access literature with a verification level for every hit.

# Rules

1. Open the chosen module file and read all of it before your first reply. Then follow it exactly. It replaces this file for the rest of the module.
2. Paths such as `references/...` in a module are relative to the root of this skill.
3. One module is active at a time. Change it only when the user asks for another module by name. During a recording session in the stream module every message is an entry, also when it contains words from the table above. Only the end words of that module end it.
4. If you cannot open a module file, say so and stop. Never work from memory of a module.
