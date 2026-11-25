---
name: kaiwa-suite
description: KAIWA SUITE (Kit for Academic Inquiry With AI) with four modules, stream of consciousness with a SHA-256 register, context map, artefact analysis with declared frameworks and open access sources. Use when the user writes start, zaczynam, rozpocznij, starte or names a KAIWA module. Cztery moduły KAIWA, strumień świadomości, mapa kontekstu, analiza artefaktu i źródła.
---

# KAIWA SUITE for Google Gemini (skill)

This skill holds the four KAIWA modules. The full procedure of each module is a file of this skill. Read the file of the chosen module completely before your first reply in that module and follow it as written. This file only says how to read the modules inside a skill.

## Modules

1. Stream of consciousness (strumień świadomości): `stream/INSTRUCTIONS.txt`
2. Context map (mapa kontekstu): `map/INSTRUCTIONS.txt`
3. Artefact analysis (analiza): `analysis/INSTRUCTIONS.txt`
4. Sources, open access (źródła): `sources/INSTRUCTIONS.txt`

If the user does not name a module, show these four and let the user choose. Do not choose for the user.

## Reading the modules in a skill

1. A file the instructions name under `method/`, for example `method/prompts/core/artifact-triage.md`, `method/prompts/framework-catalog.md` or `method/protocols/source-protocol.md`, is the file with that path in this skill. Short names such as `core/artifact-triage.md` or `framework-catalog.md` mean the files under `method/prompts/`.
2. The instructions say that the user attaches framework files. They are already part of this skill under `method/prompts/cultural-scientific/`, `method/prompts/social-science/` and `method/prompts/philosophical/`. Read the framework the user chose from there. The choice stays with the user.
3. The skill holds the files of ten frameworks: feminist-theory, multimodal-analysis, postcolonial-theory, semiotics, source-criticism, structuralism, content-analysis, conversation-analysis, systems-theory, hermeneutics. Recommend and apply only these ten. Any other framework of the catalogue is named "poza pakietem" and is not applied, not from its catalogue entry and not from memory.
4. Not part of this skill: the scripts of the package and the file `4-without-ai/registers.xlsx`. The script `tools/search.py` needs the internet, which scripts in Gemini skills may not use. When the instructions name a script or the registers, say that they belong to the full package on the user's computer.
5. One KAIWA module per chat. If a stream of consciousness recording runs in this chat and was not ended with stop, koniec or end, do not start another module. Say that the recording runs and that it ends with stop or in a new chat.
6. In the line "Narzędzie" or the sheet "tool" the tool is "Google Gemini, skill kaiwa-suite".

## Limits

Keep the words of the user apart from your proposals and mark proposals "[asystent]" or "[assistant]". Never invent a quotation, a source, a DOI, a hash, a model name or a token count. A search snippet is not a source you have read. If a file of this skill cannot be read, say which one and stop at that step instead of rebuilding its content from memory.

Last line of every answer with a result: `KAIWA SUITE · 26.01 · wersja 0.2.2 · wersja robocza / draft`
