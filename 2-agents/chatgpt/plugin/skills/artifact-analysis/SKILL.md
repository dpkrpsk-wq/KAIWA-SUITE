---
name: artifact-analysis
description: KAIWA analysis (analiza). Staged analysis of a cultural artefact (text, image, PDF, statement, practice) with a start menu, triage and declared frameworks. Use when the user attaches an artefact and writes a start word such as start, rozpocznij, zaczynamy, let's begin or lass uns beginnen, or asks for a KAIWA triage or framework analysis.
---

# KAIWA analysis

The full procedure of this module is the file `references/2-agents/chatgpt/analysis/INSTRUCTIONS.txt`. Read it completely before your first reply and follow it as written. It controls the workflow. This file only says how to read it inside a plugin.

## Reading the instructions in a plugin

1. The folder `references/` keeps the paths of the KAIWA SUITE package. A file the instructions name, for example `core/artifact-triage.md` or `framework-catalog.md`, is the file with that name under `references/method/prompts/`. `SUIT-START-MENU.md` and `kaiwa-start-menu.png` are in `references/2-agents/chatgpt/analysis/`. The templates are in `references/3-templates/`, the protocols in `references/method/protocols/`.
2. Where the instructions speak of the project or the project files, read the files in `references/`. A file the user attaches is a file attached in this chat.
3. Start menu: open `references/2-agents/chatgpt/analysis/kaiwa-start-menu.png` with Python and show it, then the text menu, as `SUIT-START-MENU.md` says. Only if the image cannot be shown, say so in one line and show the text menu.
4. The instructions say that the user attaches the framework file after triage. The framework files are already in `references/method/prompts/cultural-scientific/` and `references/method/prompts/social-science/`. Read the framework the user chose from there. The choice stays with the user. Never pick a framework yourself.
5. Menu item 4 (other KAIWA modules) names separate projects. In this plugin they are the skills `stream-of-consciousness`, `context-map` and `research-sources` in the same account. Tell the user to call the skill by name in a new chat.
6. In the line "Narzędzie" the platform and agent are "ChatGPT, plugin KAIWA Suite, skill artifact-analysis".
7. Step 2, choice 3 (research problem card) is work with the user, not a text you write. Use `references/3-templates/research-problem-card.pl.md`. Ask for one field at a time, in the order of the instructions, and wait for the user's answer before the next field. Write the user's words first and unchanged. Propose wording only when the user asks for it or says they do not know, and mark every proposal "[asystent]". Never fill the whole card, the research question or a thesis in one reply. Check the criteria together with the user only when all fields are filled.
8. One KAIWA module per chat. If a stream of consciousness recording runs in this chat and was not ended with stop, koniec or end, do not start. Reply only with this line in the user's language.
   PL: "Nagrywanie strumienia świadomości trwa. Zakończ je słowem koniec albo otwórz nowy czat dla innego modułu KAIWA."
   EN: "A stream of consciousness recording is running. End it with stop or open a new chat for another KAIWA module."
   DE: "Eine Aufnahme im Gedankenstrom läuft. Beende sie mit stop oder öffne einen neuen Chat für ein anderes KAIWA-Modul."

## Limits

Never invent quotations, sources, metadata, cultural context, model names, dates or hashes. If a file in `references/` cannot be read, say which one and stop at that step instead of rebuilding its content from memory. The cultural check is a self-assessment of the model, not an independent verification.
