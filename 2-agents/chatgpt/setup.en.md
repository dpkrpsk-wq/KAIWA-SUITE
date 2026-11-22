# KAIWA: setup guide (ChatGPT)

<img src="../../design/logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Product 26.01, version 0.2.0 (draft), 5 November 2026. Not released. Publisher: Denis Pokropski, BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (Kolegium Międzydziedzinowych Studiów Indywidualnych, KMSI), University of Wrocław, leading programme image communication (komunikacja wizerunkowa), second discipline cultural studies, contact: 285421@student.uwr.edu.pl. The package brings the KAIWA method to ChatGPT. Each of the four agents is a separate project (Projects), a folder in ChatGPT with its own instructions, files and chats.

Status: draft, untested in ChatGPT. This guide covers a ChatGPT Go account. The package does not use Custom GPTs.

## What you need

1. A ChatGPT Go account with access to projects (Projects).
2. About ten minutes for the four projects.
3. Python 3.8 or newer, only if you want to verify files on your own computer. This is optional.

## Four projects

| Project | Folder | Project files | Status |
|---|---|---|---|
| KAIWA: stream of consciousness (`strumień świadomości`) | `2-agents/chatgpt/stream/` | 1 | draft, untested in ChatGPT |
| KAIWA: context map (`mapa kontekstu`) | `2-agents/chatgpt/map/` | 2 | draft, untested in ChatGPT |
| KAIWA: analysis (`analiza`) | `2-agents/chatgpt/analysis/` | 6 | draft, untested in ChatGPT |
| KAIWA: sources (`źródła`) | `2-agents/chatgpt/sources/` | 2 | draft, untested in ChatGPT |

Each folder holds `PROJECT.md` (name, description, first message, in Polish), `INSTRUCTIONS.txt` (project instructions) and `files.txt` (project files).

## Set up one project

1. In ChatGPT create a new project and give it the name from `PROJECT.md`.
2. In the project menu (•••) choose "Project settings" and paste the whole content of `INSTRUCTIONS.txt` into the instructions. The stream of consciousness instructions (`stream/INSTRUCTIONS.txt`) are in English and stay so, because they are text for the model (a prompt), not for the reader. They were derived from the Copilot instructions and are untested on this platform. They tell the agent to reply in the user's language, but their fixed short replies are in English.
3. Add the files listed in `files.txt` to the project. Each list has at most 10 files, so one upload is enough.
4. Start a new chat in the project with the first message from `PROJECT.md`.

Length of the instructions: the OpenAI help "Projects in ChatGPT" (checked 22 November 2026) states no limit, the limit of 8,000 characters comes from Copilot. The instructions in this folder stay within it. After saving, check that the instructions are complete (unverified in ChatGPT).

## First test

1. In the project "stream of consciousness" write "start". The agent should run a short piece of Python code and show "OK". The "OK" alone does not prove that the code runs, so check the file after the session.
2. Enter two test sentences, then write "koniec". Download the file `dictation-YYYY-MM-DD-HHMM.xlsx` and check the sheets "entries", "register" and "tool".

## Files between sessions

1. Download the files the agent creates in a chat right away. Do not assume they stay available after the chat ends (unverified in ChatGPT).
2. Context map: at the start of each session agree with the agent which map file applies in this session and attach it to the chat. Download the new file after every change.
3. A project can use earlier chats as context. That is no proof of provenance. Provenance stands only in the columns of the map file.

## Usage warnings

1. A message dictated by voice counts as your original words. The transcription can still differ from what you said, so read the file after the session.
2. The SHA-256 hash shows whether the text in the file matches the hash. It does not show that the model copied your words exactly. The hash "sha256" is computed after Unicode normalisation (NFC) and collapsing whitespace and line breaks, so changes in whitespace or line breaks alone go undetected. The second hash "sha256_raw" is computed from the exact bytes of the text. Compared by hand with the text it shows such changes too, the check in the agent compares only "sha256".
3. Keep the "tool" row (sheet "tool", line "Narzędzie") separately for each chat. The model name comes from the chat and is no independent proof.
4. The block "Kontrola kulturowa" in the analysis is the model's self-report, not an independent check.
5. The open access sites in the sources agent are a search preference, not a technical restriction.
6. Run the script `tools/search.py` on your own computer, not in a ChatGPT chat. It is only in the full package, a release without scripts leaves it out.

## Sources on the platform

Checked on 22 November 2026 in the OpenAI help article "Projects in ChatGPT", https://help.openai.com/en/articles/10169521-projects-in-chatgpt:

1. Go and Plus accounts: up to 25 files per project. 10 files can be uploaded at the same time.
2. Project instructions are set in the project menu (•••), "Project settings". They apply only within that project.
3. Projects can use their chats and files as context for later answers.

The other notes on ChatGPT come from a compatibility report of 21 November 2026 that ChatGPT wrote about itself, and are marked as unverified.

## University rules

Before using recorded texts in coursework, check the rules of your university and instructor on the use of AI.

## Feedback

Contact: Denis Pokropski, 285421@student.uwr.edu.pl.

KAIWA SUITE · 26.01 · wersja 0.2.0 · wersja robocza / draft
