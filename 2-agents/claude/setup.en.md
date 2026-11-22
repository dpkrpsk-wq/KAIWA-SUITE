# KAIWA: setup guide (Claude)

<img src="../../design/logo/kaiwa-logo.svg" alt="KAIWA" width="96">

Product 26.01, version 0.2.0 (draft), 22 November 2026. Not released. Publisher: Denis Pokropski, BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (Kolegium Międzydziedzinowych Studiów Indywidualnych, KMSI), University of Wrocław.

Status: draft, untested in Claude. This guide covers two ways: projects in claude.ai (in the browser, the Claude desktop app is untested) and skills in Claude Code. The instructions were derived from the ChatGPT way of this package.

## Get the package

Open the package page https://dpkrpsk-wq.github.io/KAIWA-SUITE/, choose the vendor "Claude" and press the download button. Unpack the ZIP file into a folder of your choice. All paths in this guide start in that folder.

Which way fits you: way A needs only a browser and suits most users. Way B is for people who already use Claude Code, a program that runs Claude in a terminal on your own computer.

## What you need

1. Way A, claude.ai: a Claude account. Projects exist on all plans, a free account can create up to five projects. The setting "Code execution and file creation" (called "Create and edit files" in the newer settings layout) must be on (Settings, Capabilities), otherwise the Excel files cannot be created.
2. Way B, Claude Code: Claude Code on your computer, Python 3.8 or newer and the Python package openpyxl (`pip install openpyxl`).
3. About ten minutes for the four modules.

## Four modules

| Module | Way A: project folder | Way B: skill | Project files | Status |
|---|---|---|---|---|
| KAIWA: stream of consciousness (`strumień świadomości`) | `2-agents/claude/stream/` | `2-agents/claude/code/kaiwa-stream/` | 1 | draft, untested in Claude |
| KAIWA: context map (`mapa kontekstu`) | `2-agents/claude/map/` | `2-agents/claude/code/kaiwa-map/` | 3 | draft, untested in Claude |
| KAIWA: analysis (`analiza`) | `2-agents/claude/analysis/` | `2-agents/claude/code/kaiwa-analysis/` | 6 | draft, untested in Claude |
| KAIWA: sources (`źródła`) | `2-agents/claude/sources/` | `2-agents/claude/code/kaiwa-sources/` | 2 | draft, untested in Claude |

Each project folder holds `PROJECT.md` (name, description, first message, in Polish), `INSTRUCTIONS.txt` (project instructions) and `files.txt` (project files). Each skill folder holds one `SKILL.md` with the same instructions and a short preface for Claude Code. A skill is a folder with instructions that Claude Code loads when you call it. The project knowledge of a claude.ai project is the set of files that Claude reads in every chat of that project.

## Way A: set up one project in claude.ai

1. In claude.ai create a new project and give it the name from `PROJECT.md`. The desktop app should offer the same projects, this is unverified.
2. Choose "Set project instructions" and paste the whole content of `INSTRUCTIONS.txt`. The stream of consciousness instructions (`stream/INSTRUCTIONS.txt`) are in English and stay so, because they are text for the model (a prompt), not for the reader.
3. Add the files listed in `files.txt` to the project knowledge ("+" in the knowledge area of the project).
4. Start a new chat in the project with the first message from `PROJECT.md`.

In the help pages checked we found no length limit for project instructions. The instructions in this folder stay within 8,000 characters, the limit of Copilot.

## Way B: install the skills in Claude Code

1. Open a terminal in the folder of the KAIWA package (the folder with `README.md`).
2. Copy the four folders from `2-agents/claude/code/` into the folder `.claude/skills/` of the package folder, so that for example `.claude/skills/kaiwa-stream/SKILL.md` exists. A folder whose name starts with a dot may be hidden in your file manager. On Windows (PowerShell): `New-Item -ItemType Directory -Force .claude/skills; Copy-Item -Recurse 2-agents/claude/code/* .claude/skills/`. On macOS and Linux: `mkdir -p .claude/skills && cp -r 2-agents/claude/code/* .claude/skills/`.
3. Start Claude Code in the package folder and write for example `/kaiwa-stream` or "start" with a short note which module you want.

The skills read the project files from the package folder and save the Excel files in the current folder. They do not install anything. If openpyxl is missing, the skill says so.

The skills are written for Claude Code. In claude.ai use the projects of way A.

## First test

1. In the module "stream of consciousness" write "start". Claude should run a short piece of Python code and show "OK". The "OK" alone does not prove that the code runs, so check the file after the session.
2. Enter two test sentences, then write "koniec". Check the file `dictation-YYYY-MM-DD-HHMM.xlsx` and its sheets "entries", "register" and "tool".

## Files between sessions

1. Way A: download the files Claude creates in a chat right away. Do not assume they stay available after the chat ends (unverified in Claude).
2. Context map: at the start of each session agree with Claude which map file applies in this session. In claude.ai attach it to the chat, in Claude Code name its path. Keep the new file after every change.
3. What Claude remembers from earlier chats is no proof of provenance. Provenance stands only in the columns of the map file.

## Usage warnings

1. A message dictated by voice counts as your original words. The transcription can still differ from what you said, so read the file after the session.
2. The SHA-256 hash shows whether the text in the file matches the hash. It does not show that the model copied your words exactly. The hash "sha256" is computed after Unicode normalisation (NFC) and collapsing whitespace and line breaks. The second hash "sha256_raw" is computed from the exact bytes of the text.
3. Keep the "tool" row (sheet "tool", line "Narzędzie") separately for each chat or session. The model name comes from the chat and is no independent proof.
4. The block "Kontrola kulturowa" in the analysis is the model's self-report, not an independent check.
5. The open access sites in the sources module are a search preference, not a technical restriction. Web search in claude.ai depends on the account and its settings (unverified for this package).
6. Run the script `tools/search.py` on your own computer. It is only in the full package, a release without scripts leaves it out.

## Sources on the platform

Checked on 22 November 2026:

1. "What are projects?", https://support.claude.com/en/articles/9517075-what-are-projects: projects on all plans, free accounts up to five projects.
2. "How can I create and manage projects?", https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects: project instructions and project knowledge.
3. "Create and edit files with Claude", https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude: code execution and file creation, on web and desktop, Settings, Capabilities.
4. Claude Code documentation, https://code.claude.com/docs/en/skills: skills in `.claude/skills/<name>/SKILL.md` and `~/.claude/skills/`.

The help pages describe the desktop app only for code execution and file creation. That projects work the same there is unverified.

## University rules

Before using recorded texts in coursework, check the rules of your university and instructor on the use of AI.

## Feedback

Contact: Denis Pokropski, 285421@student.uwr.edu.pl.

KAIWA SUITE · 26.01 · wersja 0.2.0 · wersja robocza / draft
