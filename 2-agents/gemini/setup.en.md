# KAIWA: setup guide (Google Gemini)

<picture><source media="(prefers-color-scheme: dark)" srcset="../../design/logo/kaiwa-logo-hell.svg"><img src="../../design/logo/kaiwa-logo.svg" alt="KAIWA" width="240"></picture>

**Languages / języki:** [English](setup.en.md) · [Polski](setup.pl.md)

Product 26.01, version 0.2.2 (draft), 22 November 2026. Not released. Publisher: Denis Pokropski, BA in philosophy (University of Wrocław, 2019), master's student, College of Interdisciplinary Individual Studies (Kolegium Międzydziedzinowych Studiów Indywidualnych, KMSI), University of Wrocław, leading programme image communication (komunikacja wizerunkowa), second discipline cultural studies, contact: 285421@student.uwr.edu.pl. This package adapts the KAIWA method for Google Gemini (Skills and Gems are saved standing instructions in Gemini that you call up in a chat, plus plain Gemini chats with file attachments).

## Get the package

Open the package page https://mentalping-ops.github.io/KAIWA-SUITE/, choose the vendor "Google Gemini" and press the download button. Unpack the ZIP file into a folder of your choice. All paths in this guide start in that folder.

## What you need

1. A Google account with access to Google Gemini (personal account 18+, Google AI subscription, or Google Workspace education/work account, account types unverified).
2. About five minutes for setup (or one minute in plain chat mode with an attachment).
3. Python 3.8 or newer, only if you want to verify files on your own computer. This is optional.

## Choosing your setup route (by workflow and account type)

1. **Route 1, plain chat with attachment (zero setup, untested in Gemini):** Attach `2-agents/gemini/setup-dialog.md` to a new Gemini chat and write "start". The assistant guides you through module selection and provides ready-to-paste instructions.
2. **Route 2, Skill or Gem (persistent setup):**
   - **Personal accounts 18+ (Gemini web/app):** Download `KAIWA-SUITE-gemini-skill-<version>.zip` from the package page. In the Gemini web app open **Skills**, choose **Create** and **Upload**, select the ZIP and finish with **Create**. Google accepts a `SKILL.md` file, a folder or a ZIP with `SKILL.md` in the main folder, up to 100 MB (Google help page on Skills, read on 25 November 2026). The skill holds the four modules, ten frameworks and the protocols, no scripts. Untested in Gemini.
   - **Google Workspace education/work accounts (where Gems are active):** Open **Explore Gems** (menu name unverified), choose **New Gem**, and paste name, description and instructions from the chosen module folder.
3. **Route 3, connected Google Drive folder (Workspace integration):** When the Google Workspace extension is enabled on your account, keep `method/protocols/` and `method/prompts/` in Google Drive (unverified) and reference them directly in chat.
4. **Route 4, local verification without AI:** Run the scripts in `tools/` (`dictation_ledger.py`, `context.py`, `search.py`) or use `4-without-ai/registers.xlsx`.

## Quick setup for the four modules

If Gemini lets you set an icon, use `design/logo/kaiwa-icon-192.png` (not checked in Gemini).

Whether Gemini runs code: in a test on a Google Pro account on 25 November 2026 Gemini itself said that it has no Python interpreter in the chat with the skill. That is a statement of the model, not checked independently. It may differ by account, model and setting. Your first test shows what your account does.

| Module | Folder | Code interpreter needed | Status |
|---|---|---|---|
| KAIWA: stream of consciousness (`strumień świadomości`) | `2-agents/gemini/stream/` | yes for SHA-256 hashes and `.xlsx`, but Gemini reported no interpreter (model statement, not checked) | skill uploaded and called, a session started, end of session without code fixed in `stream/INSTRUCTIONS.txt` and not retested, otherwise draft |
| KAIWA: context map (`mapa kontekstu`) | `2-agents/gemini/map/` | yes for `kontekst-1` validation and `.xlsx`, but Gemini reported no interpreter (model statement, not checked) | draft, untested in Gemini, case without code added to `map/INSTRUCTIONS.txt` |
| KAIWA: analysis (`analiza`) | `2-agents/gemini/analysis/` | no | draft, untested in Gemini |
| KAIWA: sources (`źródła`) | `2-agents/gemini/sources/` | optional (for `.xlsx` export) | draft, untested in Gemini |

The stream of consciousness instructions (`stream/INSTRUCTIONS.txt`) are in English and stay so, because they are text for the model (a prompt), not for the reader. They were derived from the Copilot instructions and are untested on this platform. They tell the agent to reply in the user's language, but their fixed short replies are in English.

## First test

1. Open the configured Skill/Gem (or start a chat with `2-agents/gemini/setup-dialog.md` attached) and write "start".
2. For **stream of consciousness** and **context map** the instructions ask Gemini to run a short Python check and print "OK". If Gemini has no interpreter, as it reported on 25 November 2026 (a statement of the model, not checked independently), it must say that this chat computes no hashes. It must not print "OK" and must not invent a hash.
3. If code execution is disabled in your region or institutional tenant, Gemini must warn you and save without hashes. It must never fabricate a hash.
4. Enter two test sentences and write "end". With code, check that the topic list, downloadable `.xlsx` file, "Tool" disclosure line, and version footer appear. Without code there is no file: the stream gives a Markdown table with the verbatim texts and a line that no file and no hash exist, the map saves nothing.

## Usage warnings and platform boundaries

1. **Regional and institutional feature limits:** In some regions (including parts of the EEA/EU) and managed Google Workspace tenants, Skills, Skill sharing, Drive extensions, or code execution may be disabled for privacy or administrative reasons (unverified). Use Route 1 (chat attachment) or `4-without-ai/README.pl.md` as fallback.
2. **Separate memory stores:** Instructions in the Gemini web app and Workspace side-panel personalization do not sync automatically (unverified).
3. **Manual file download:** Files generated by the code interpreter in Gemini must be downloaded directly from the chat response (unverified) and saved to your working folder.
4. **Session length:** End stream-of-consciousness sessions after twenty entries to keep verbatim recording reliable.
5. **Hashes verify file integrity only:** Read the generated `.xlsx` file once after each session to verify exact wording. The hash "sha256" is computed after Unicode normalisation (NFC) and collapsing whitespace and line breaks, so changes in whitespace or line breaks alone go undetected. The second hash "sha256_raw" is computed from the exact bytes of the text. Compared by hand with the text it shows such changes too, the check in the agent compares only "sha256".
6. **No interpreter reported, behaviour of the skill:** In the test of 25 November 2026 (Google Pro account) Gemini said that it has no Python interpreter in the chat with the skill (a statement of the model, not checked independently). At the end of a stream session it then wrote pseudocode and said that export and register are kept in Google Drive. The instructions forbid that. Since then the stream and the map name the case without code (a table with the verbatim texts or no save, one line that no file and no hash exist, never a claim that anything is saved). This is fixed in the text and not retested in Gemini.

## University rules

Before using recorded texts in coursework, check the rules of your university and instructor on the use of AI.

## Feedback

Contact: Denis Pokropski, 285421@student.uwr.edu.pl.

KAIWA SUITE · 26.01 · wersja 0.2.2 · wersja robocza / draft
