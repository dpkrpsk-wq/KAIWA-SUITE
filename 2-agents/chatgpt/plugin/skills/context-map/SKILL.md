---
name: context-map
description: KAIWA context map (mapa kontekstu). Builds, updates and checks a map of topics, connections, provenance and user goals in an Excel workbook, with the user's approval before every change. Use when the user wants to start or continue a KAIWA context map, attaches a map workbook or writes "sprawdź mapę" or "check the map".
---

# KAIWA context map

The full procedure of this module is the file `references/2-agents/chatgpt/map/INSTRUCTIONS.txt`. Read it completely before your first reply and follow it as written. It controls the workflow. This file only says how to read it inside a plugin.

## Reading the instructions in a plugin

1. The folder `references/` keeps the paths of the KAIWA SUITE package. The method text is `references/1-start/context.pl.md`, the map check is `references/2-agents/chatgpt/map/sprawdz-mape.md`, the tool disclosure template is `references/3-templates/tool-disclosure.pl.md`.
2. Where the instructions speak of the project or the project files, read the files in `references/`. A map file is a workbook the user attaches in this chat. Ask which attached file is the map for this session, as the instructions say. A plugin keeps nothing between chats, so the user attaches the latest map in every new chat.
3. For "sprawdź mapę" run the code from `references/2-agents/chatgpt/map/sprawdz-mape.md` with Python on the attached map. Report "verified" only when that code ran and printed its result.
4. Before you offer a new map file that replaces an existing one, compare the row counts of every sheet in the old and the new workbook and show them to the user.
5. In the sheet "tool" or the line "Narzędzie" the platform and agent are "ChatGPT, plugin KAIWA Suite, skill context-map".

## Limits

Never invent topics, connections, goals, provenance, dates or hashes. Compute hashes only by running code. If a file in `references/` cannot be read, say which one and stop at that step.
