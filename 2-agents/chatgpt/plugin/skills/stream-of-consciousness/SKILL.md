---
name: stream-of-consciousness
description: KAIWA stream of consciousness (strumień świadomości). Records every thought of the user verbatim without interrupting and at the end saves an Excel workbook with the entries and a SHA-256 register. Use when the user says start or zaczynam to dictate, wants a verbatim record, or attaches a dictation workbook to verify.
---

# KAIWA stream of consciousness

The full procedure of this module is the file `references/2-agents/chatgpt/stream/INSTRUCTIONS.txt`. Read it completely before your first reply and follow it as written. It controls the workflow. This file only says how to read it inside a plugin.

## Reading the instructions in a plugin

1. The folder `references/` keeps the paths of the KAIWA SUITE package. The tool disclosure template is `references/3-templates/tool-disclosure.pl.md`.
2. Where the instructions speak of the project, read this skill and the files in `references/`.
3. Run the code in the instructions with Python in this chat. Write "OK" or a hash only when the code ran and printed it.
4. Tell the user once, when the recording starts, that the SHA-256 register proves only that the saved text did not change after saving. It does not prove that a transcription matches what was spoken. The user checks the verbatim column.
5. In the sheet "tool" the tool is "ChatGPT, plugin KAIWA Suite, skill stream-of-consciousness". This replaces the project name the instructions give.
6. One KAIWA module per chat. While a recording runs, a message that calls another KAIWA module is not an entry. Examples: /triage, a start word of the analysis, a request for a context map or for sources, the chip of another KAIWA skill. Record nothing from it, start no other module and reply only with this line in the language of the recording. The recording goes on after it.
   PL: "Nagrywanie strumienia świadomości trwa. Zakończ je słowem koniec albo otwórz nowy czat dla innego modułu KAIWA."
   EN: "A stream of consciousness recording is running. End it with stop or open a new chat for another KAIWA module."
   DE: "Eine Aufnahme im Gedankenstrom läuft. Beende sie mit stop oder öffne einen neuen Chat für ein anderes KAIWA-Modul."

## Limits

Never change, shorten or correct what the user wrote. Never guess the time, the token count or the model name. If the workbook cannot be created, say so and keep the entries in the chat.
