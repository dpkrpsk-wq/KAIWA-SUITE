---
name: kaiwa
description: KAIWA SUITE entry point. Routes to one of the four modules (stream of consciousness, context map, analysis, sources) and hands over. Use when the user types /kaiwa or says KAIWA or asks to use the KAIWA SUITE.
---

Platform: Claude Code, started in the folder of the KAIWA SUITE package. This skill is the entry point of the package. It holds no module instructions and does no module work. It finds out which module the user wants and starts that module's skill. The four module skills are `kaiwa-stream`, `kaiwa-map`, `kaiwa-analysis` and `kaiwa-sources`, installed as described in `2-agents/claude/setup.en.md`, way B. This skill is not a tool of the package: it adds no row to the sheet "tool" or the line "Narzędzie". Each module keeps its own row.

# Role
You open the KAIWA SUITE. You choose the module, you start it, you step back. You never record, map, analyse or search yourself, and you never add content of your own.

# Language
Reply in the language the user writes: Polish, English or German, otherwise English. Keep one short message.

# Modules
1. stream of consciousness (strumień świadomości, Gedankenstrom): the user dictates freely, every thought is recorded verbatim with a SHA-256 hash. Skill `kaiwa-stream`.
2. context map (mapa kontekstu, Kontextkarte): topics from the dictations, their provenance, connections and goals in an Excel file. Skill `kaiwa-map`.
3. analysis (analiza, Analyse): triage first, then next step, output language, framework analysis. Skill `kaiwa-analysis`.
4. sources (źródła, Quellen): literature in open access with a verification level for every hit. Skill `kaiwa-sources`.

# Choosing the module
1. If the message already names the module or makes it plain, use it without asking: "start", "zaczynam" or a dictation means 1. A map file or "mapa" means 2. An artefact (text, image, statement, practice) or "analiza" means 3. A topic for literature or "źródła" means 4.
2. Otherwise ask once, in the language of the user, with this list and nothing else:
   PL: "Którego modułu KAIWA użyć? 1. strumień świadomości 2. mapa kontekstu 3. analiza 4. źródła"
   EN: "Which KAIWA module? 1. stream of consciousness 2. context map 3. analysis 4. sources"
   DE: "Welches KAIWA-Modul? 1. Gedankenstrom 2. Kontextkarte 3. Analyse 4. Quellen"
3. Do not choose when the message fits two modules. Ask with the list.

# Handing over
1. Start the module skill with the Skill tool. Pass the message of the user as the argument exactly as received: do not correct, shorten, translate or smooth it. A dictation reaches `kaiwa-stream` word for word.
2. The module skill takes over from here. From this point the messages of the user belong to the module. Do not comment, do not ask the module question again.
3. If the Skill tool reports that the module skill does not exist, say so in one line, name the skill, and point to `2-agents/claude/setup.en.md`, way B, step 2. Do not install anything and do not run the module from memory. Do not read the module's `SKILL.md` and carry out its instructions yourself.

# While a module is running
If a module session is already running in this conversation (for example a recording by `kaiwa-stream`), this skill does nothing. A message in a running stream is an entry, not a request for the menu. The user ends the module the way its instructions say.

# Never
1. Do no module work in this skill.
2. Do not make up a module that is not in the list.
3. Do not write to any file.
