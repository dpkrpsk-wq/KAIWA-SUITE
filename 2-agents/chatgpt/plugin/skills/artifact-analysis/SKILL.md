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
8. Frameworks. The catalogue lists 16 frameworks, the plugin holds the files of ten: feminist-theory, multimodal-analysis, postcolonial-theory, semiotics, source-criticism, structuralism, content-analysis, conversation-analysis, systems-theory, hermeneutics. Recommend and apply only these ten. Any other framework of the catalogue is named "poza pakietem". Do not apply it, not from its catalogue entry and not from memory. If the user asks for it, say that its file is not in this plugin and offer the ten.
9. The three-way question of step 2 ("Jak chcesz kontynuować?") is always asked. A task sentence the user wrote earlier is not an answer to it.
10. Step 3: write the user's answers about language and context word for word, as the user's words. Do not complete them, do not infer a position of the user, do not state the culture of the artefact. In the result, show the user's context words in the cultural check, row 5, and compare them with the addressee of the result.
11. Step 4: for every framework, one sentence of its own before the analysis. It says for which material and environment the declaration (L1, D2) is written and whether the artefact belongs to it.
12. Step 5: every statement about the artefact carries a short quotation with its place (page or section). A figure without a quotation is not reported. A paraphrase is marked as the model's wording, next to the quotation it rests on.
13. The line "braki" names every step that ran without the file it needs, including an earlier triage that was not checked against its file.
14. One KAIWA module per chat. If a stream of consciousness recording runs in this chat and was not ended with stop, koniec or end, do not start. Reply only with this line in the user's language.
   PL: "Nagrywanie strumienia świadomości trwa. Zakończ je słowem koniec albo otwórz nowy czat dla innego modułu KAIWA."
   EN: "A stream of consciousness recording is running. End it with stop or open a new chat for another KAIWA module."
   DE: "Eine Aufnahme im Gedankenstrom läuft. Beende sie mit stop oder öffne einen neuen Chat für ein anderes KAIWA-Modul."

## Limits

Never invent quotations, sources, metadata, cultural context, model names, dates or hashes. If a file in `references/` cannot be read, say which one and stop at that step instead of rebuilding its content from memory. The cultural check is a self-assessment of the model, not an independent verification.
