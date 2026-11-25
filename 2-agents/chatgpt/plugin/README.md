# KAIWA SUITE: ChatGPT plugin

Wtyczka ChatGPT z czterema skillami KAIWA, dostępnymi w każdym czacie konta, bez projektów. / A ChatGPT plugin with the four KAIWA skills, available in every chat of the account, without projects.

| Skill | Moduł / module | Procedura / procedure |
|---|---|---|
| `artifact-analysis` | analiza / analysis | `2-agents/chatgpt/analysis/INSTRUCTIONS.txt` |
| `context-map` | mapa kontekstu / context map | `2-agents/chatgpt/map/INSTRUCTIONS.txt` |
| `research-sources` | źródła / sources | `2-agents/chatgpt/sources/INSTRUCTIONS.txt` |
| `stream-of-consciousness` | strumień świadomości / stream of consciousness | `2-agents/chatgpt/stream/INSTRUCTIONS.txt` |

## Budowa / build

`python tools/chatgpt_plugin.py` tworzy / creates `dist/KAIWA-SUITE-chatgpt-plugin.zip`. Pliki w `references/` każdego skilla są niezmienionymi kopiami plików pakietu: instrukcja modułu, pliki z jego `files.txt` i z `extra.txt` skilla. Ten sam stan pakietu daje te same bajty ZIP. / The files under each skill's `references/` are unchanged copies of package files: the module's instructions, the files of its `files.txt` and of the skill's `extra.txt`. The same package state gives the same ZIP bytes.

`python tools/chatgpt_plugin.py --check PLIK.zip` porównuje ZIP z pakietem / compares a ZIP with the package.

## Instalacja / installation

W ChatGPT: Plugins, przycisk dodawania, przesłanie archiwum wtyczki, plik `dist/KAIWA-SUITE-chatgpt-plugin.zip`. W niemieckim interfejsie 24.11.2026: „Hinzufügen”, „Plugin-Archiv hochladen”, inne języki niesprawdzone. / In ChatGPT: Plugins, the add button, upload a plugin archive, file `dist/KAIWA-SUITE-chatgpt-plugin.zip`. Labels seen in the German interface on 24 November 2026, other languages unverified. Starszą wtyczkę `kaiwa-suite` z wyższym numerem wersji usuń najpierw / remove an older `kaiwa-suite` plugin with a higher version number first.

## Stan / status

Wersja `0.2.0-chatgpt.6`, robocza, nieprzetestowana w ChatGPT. Bez narzędzi MCP i bez skryptów lokalnych. / Version `0.2.0-chatgpt.6`, draft, untested in ChatGPT. No MCP tools and no local scripts.
