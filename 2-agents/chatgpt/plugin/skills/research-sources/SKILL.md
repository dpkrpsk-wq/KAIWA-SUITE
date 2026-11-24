---
name: research-sources
description: KAIWA sources (źródła). Finds scholarly open access literature for a research question, proposes search terms in several languages first and records the verification level of every source. Use when the user asks for KAIWA literature research, search terms, a source table or the verification level of a source.
---

# KAIWA sources

The full procedure of this module is the file `references/2-agents/chatgpt/sources/INSTRUCTIONS.txt`. Read it completely before your first reply and follow it as written. It controls the workflow. This file only says how to read it inside a plugin.

## Reading the instructions in a plugin

1. The folder `references/` keeps the paths of the KAIWA SUITE package. `method/protocols/source-protocol.md` is `references/method/protocols/source-protocol.md`, the templates are in `references/3-templates/`.
2. Where the instructions speak of the project or the project files, read the files in `references/`.
3. Search with the web search of this chat. The script `tools/search.py` the instructions mention is not part of this plugin and does not run here. Under the table name the route you used for every search: web search, with query and date.
4. Propose the search terms and wait for the user's acceptance before the first search, as the instructions say.
5. In the line "Narzędzie" the platform and agent are "ChatGPT, plugin KAIWA Suite, skill research-sources".

## Limits

Never invent authors, titles, years, DOIs, links or quotations. A search snippet is not a source you have read. No result means no result for that query on that date, not that no literature exists. If a file in `references/` cannot be read, say which one and stop at that step.
