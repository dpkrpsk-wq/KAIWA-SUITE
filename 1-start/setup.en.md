# KAIWA: setup guide (Microsoft 365 Copilot)

<img src="../design/logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Product 26.01, version 0.2.0 (draft), 22 November 2026. Not released. Publisher: Denis Pokropski, BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (Kolegium Międzydziedzinowych Studiów Indywidualnych, KMSI), University of Wrocław, leading programme image communication (komunikacja wizerunkowa), second discipline cultural studies, contact: 285421@student.uwr.edu.pl. The package invites you to test a method: thoughts spoken aloud are recorded word for word, and every entry gets a SHA-256 hash that later shows whether the text in the file matches the hash.

## What you need

1. A university account with access to Microsoft 365 Copilot Chat. No Copilot license is needed.
2. About ten minutes for the setup.
3. Python 3.8 or newer, only if you want to check files on your own computer. This is optional.

## Set up the agent

Button labels can differ with the language of the interface. The labels below are the English ones from the Microsoft documentation.

1. Open Copilot in the browser, choose "Agents" on the left, then "New agent".
2. Choose the manual setup ("Configure", "Skip to configure").
3. Paste name, description and starter prompts from `2-agents/copilot/stream/AGENT.md`.
4. As the icon ("Icon", "Upload") upload `design/logo/kaiwa-icon-192.png`. Microsoft accepts a PNG file up to 192 × 192 pixels and 1 MB.
5. Paste the whole content of `2-agents/copilot/stream/INSTRUCTIONS.txt` into the instructions field. The instructions are in English and stay so, because they are text for the model (a prompt), not for the reader. A first version was tested on a university account on 17 Oct 2026 (without a record), the current version has changed since and is untested. The instructions tell the agent to reply in the user's language, but their fixed short replies are in English.
6. Add nothing under knowledge.
7. Save the agent ("Create").

## First test

1. Open the agent and write "start".
2. The agent should show a short piece of code and the result "OK". This suggests that the agent runs code. The "OK" alone does not prove it, so check the file after the session.
3. If you see a warning that hashes are not possible instead, the session is saved without them. The agent must not invent hashes then.
4. Say or type two sentences, then "end". The agent shows a list of topics and the name of the Excel file.

## Usage warnings

1. Copilot Chat without a license has usage limits. The Microsoft documentation says "Usage limits apply to all included features" (quote unverified) and gives no numbers. The stream agent runs code only twice per session, at the start and at the end, to keep usage low. The map agent runs it at the start, when reading files, saving and checking, and checking a dictation file runs code too.
2. Do not add OneDrive or SharePoint files as knowledge. Without a Copilot license this does not work or is billed as metered usage.
3. A long session is less reliable. After twenty entries the agent suggests ending. End the session then and start a new one.
4. The hash shows that the text in the file has not changed since the end of the session. It does not show that the model copied your words exactly. The hash "sha256" is computed after Unicode normalisation (NFC) and collapsing whitespace and line breaks, so changes in whitespace or line breaks alone go undetected. The second hash "sha256_raw" is computed from the exact bytes of the text. Compared by hand with the text it shows such changes too, the check in the agent compares only "sha256". Read the file once after the session.

## Where the files are

Each session gives one file `dictation-YYYY-MM-DD-HHMM.xlsx` with three sheets: "entries" (the entries with text), "register" (hashes, numbers of characters and words, no text) and "tool" (see below). Excel files from the code interpreter usually land in your OneDrive by themselves, in the Copilot folder (not confirmed in the Microsoft documentation). This happened in a test on a University of Wrocław account on 17 October 2026, but Microsoft does not guarantee it. The sheet "tool" records the tool, the model (as the chat states it), the number of code runs and the computational effort, with "unknown" where nothing is known. It carries no hash, so read it once (`3-templates/tool-disclosure.pl.md`, Polish). The agent always offers the file as a download too. Copilot does not overwrite files (unverified), so the folder works as a register that only grows. You can move the files to a folder of your own, for example "KAIWA".

## Checking

1. In Copilot, attach a session file to a conversation with the agent and write "verify this file". The agent computes the hashes again and reports for each entry whether the text changed.
2. On your own computer, if you keep a journal in Markdown files: `python tools/dictation_ledger.py init <folder>`, then `scan <folder>` and `verify <folder>`. The script uses the same hash rule as the agent.

## Second agent: context map

Optional. Method: `1-start/context.pl.md` (Polish). This part has not been tested in Copilot yet.

1. Create a second agent the same way as the first.
2. Take name, description and starter prompts from `2-agents/copilot/map/AGENT.md`, the instructions from `2-agents/copilot/map/INSTRUCTIONS.txt`.
3. Add nothing as knowledge. You attach files to the conversation.
4. Write "start". The agent should answer "Mapa gotowa. Skróty działają." (map ready, hashes work).
5. Attach a dictation file from the first agent and write "dodaj dołączone dyktaty do mapy" (add the attached dictations to the map). Approve the proposals by number, then write "zapisz" (save).
6. Check in Copilot: attach the map file and `2-agents/copilot/map/sprawdz-mape.md` and write "sprawdź mapę" (check the map). On your own computer: `python tools/context.py sprawdz <map file>` (needs openpyxl).

## Third agent: analysis

Optional. This part has not been tested in Copilot yet.

1. Create an agent from the fields in `2-agents/copilot/analysis/AGENT.md` and the instructions in `2-agents/copilot/analysis/INSTRUCTIONS.txt`.
2. In the conversation attach the artefact and the files `method/prompts/core/artifact-triage.md` and `method/prompts/framework-catalog.md`. Without the triage file the agent asks for it and neither does the triage nor recommends frameworks.
3. After the triage the agent asks for the next step (1 continue, 2 comment or task, 3 research problem), then for the output language and the cultural context of the artefact. Every result ends with the block "Kontrola kulturowa" (cultural check), which lists the assumptions the model made. Flow: `3-templates/after-triage.pl.md`, checklist: `3-templates/cultural-check.pl.md` (both Polish).
4. When the agent recommends frameworks, attach their files from `method/prompts/cultural-scientific/` or `method/prompts/social-science/`.

## Fourth agent: sources

Optional. This part has not been tested in Copilot yet.

1. Create an agent from the fields in `2-agents/copilot/sources/AGENT.md` and the instructions in `2-agents/copilot/sources/INSTRUCTIONS.txt`.
2. Add the four websites from `AGENT.md` as knowledge. Without them the agent searches the whole web and the results need a more careful assessment.
3. The instructions hold a short form of the source protocol. You can attach the full file `method/protocols/source-protocol.md` to the conversation.
4. On your own computer you can search without Copilot: `python tools/search.py "term" --csv result.csv`. The file has the columns of the sheet "zrodla" in `4-without-ai/registers.xlsx`.

Length of the agent instructions (characters, limit 8,000): stream 6018, map 7495, analysis 6496, sources 4198. Paste them from the file unchanged, an editor with CRLF line endings can add characters.

## Other platforms

The same agents as Gemini modules: `2-agents/gemini/setup.en.md`, as ChatGPT projects: `2-agents/chatgpt/setup.en.md`.

## University rules

Before you use recorded texts in coursework, check the rules of your university and your teacher on the use of AI.

## Sources on the platform

Checked on 22 November 2026 in the Microsoft Learn documentation:

1. Agent fields and icon (name 30 characters, description 1000, instructions 8000, PNG up to 192 × 192 pixels and 1 MB): https://learn.microsoft.com/plugins/agent-builder-build-agents
2. Without a Copilot licence, agents with instructions and public websites are included, others only on pay-as-you-go: https://learn.microsoft.com/copilot/plan/copilot-overview
3. Microsoft does not publish numeric usage limits: https://learn.microsoft.com/partner-center/announcements/2026-november

## Feedback

Contact for feedback: Denis Pokropski, 285421@student.uwr.edu.pl.
