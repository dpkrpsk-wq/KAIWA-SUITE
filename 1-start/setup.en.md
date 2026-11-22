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

1. Copilot Chat without a license has usage limits. The Microsoft documentation says "Usage limits apply to all included features" (quote unverified) and gives no numbers. The agent runs code only twice per session, at the start and at the end, to keep usage low.
2. Do not add OneDrive or SharePoint files as knowledge. Without a Copilot license this does not work or is billed as metered usage.
3. A long session is less reliable. After twenty entries the agent suggests ending. End the session then and start a new one.
4. The hash shows that the text in the file has not changed since the end of the session. It does not show that the model copied your words exactly. The hash "sha256" is computed after Unicode normalisation (NFC) and collapsing whitespace and line breaks, so changes in whitespace or line breaks alone go undetected. The second hash "sha256_raw" is computed from the exact bytes of the text. Compared by hand with the text it shows such changes too, the check in the agent compares only "sha256". Read the file once after the session.

## Where the files are

Each session gives one file `dictation-YYYY-MM-DD-HHMM.xlsx` with three sheets: "entries" (the entries with text), "register" (hashes, numbers of characters and words, no text) and "tool" (see below). Excel files from the code interpreter usually land in your OneDrive by themselves, in the Copilot folder (not confirmed in the Microsoft documentation). This happened in a test on a University of Wrocław account on 17 October 2026, but Microsoft does not guarantee it. The sheet "tool" records the tool, the model (as the chat states it), the number of code runs and the computational effort, with "unknown" where nothing is known. It carries no hash, so read it once (`3-templates/tool-disclosure.pl.md`, Polish). The agent always offers the file as a download too. Copilot does not overwrite files (unverified), so the folder works as a register that only grows. You can move the files to a folder of your own, for example "KAIWA".

## Checking

1. In Copilot, attach a session file to a conversation with the agent and write "verify this file". The agent computes the hashes again and reports for each entry whether the text changed.
2. On your own computer, if you keep a journal in Markdown files: `python tools/dictation_ledger.py init <folder>`, then `scan <folder>` and `verify <folder>`. The script uses the same hash rule as the agent.

## Analysis agent: cultural check

The optional analysis agent (set-up in `1-start/setup.pl.md`, "Trzeci agent") asks after the triage for the output language and for the cultural context of the artefact, and ends every result with a fixed block "Kontrola kulturowa" (cultural check) that lists the assumptions the model made. Description and checklist (Polish): `3-templates/cultural-check.pl.md`.

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
