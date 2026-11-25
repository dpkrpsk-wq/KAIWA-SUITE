# Release of KAIWA SUITE / Wydanie

`sets.json` is the single source for the file set of every release ZIP (and for the package page). `tools/release.py` builds the ZIPs from it. / `sets.json` to jedyne źródło zestawu plików każdego ZIP.

## Build locally / Budowa lokalna

```
python -I tools/release.py pruefen --ausgabe dist/release
```

`pruefen` builds twice from the commit `HEAD`, compares both builds byte for byte and checks each ZIP against its sources. `bauen` only builds. `--stand <commit>` builds from another commit, `--arbeitsbaum` reads the files from the disk (used by the tests). The output goes to `dist/release/` (not in Git). / `pruefen` buduje dwa razy i porównuje wyniki.

## What it builds / Co powstaje

- `KAIWA-SUITE-<vendor>-<version>.zip` for copilot, gemini, chatgpt, claude and any, one root folder each, with `ZIP-CONTENTS.md`.
- `KAIWA-SUITE-copilot-skill-<version>.zip` (one `SKILL.md` in the root) and `KAIWA-SUITE-copilot-plugin-<version>.zip` (`manifest.json`, two icons, four skills), sources in `2-agents/copilot/skill/` and `2-agents/copilot/plugin/`, references taken from `method/` at build time.
- `KAIWA-SUITE-chatgpt-plugin-<version>.zip` (`plugin.json`, `.codex-plugin/plugin.json`, four skills with their references), sources in `2-agents/chatgpt/plugin/`, references taken from `2-agents/chatgpt/` and `method/` at build time. `tools/chatgpt_plugin.py` builds the same files.
- `KAIWA-SUITE-chatgpt-project-kit-<version>.zip` (flat: `INSTRUCTIONS.txt`, `PROJECT.md`, `registers.xlsx`, `kaiwa-template.docx`, `README.pl.md`, licences), sources in `2-agents/chatgpt/project-kit/` and `4-without-ai/`. `tools/chatgpt_plugin.py --kit` builds the same files.
- `KAIWA-SUITE-gemini-skill-<version>.zip` (flat, `SKILL.md` in the root, the four module instructions, `method/` prompts and protocols, licences), source `2-agents/gemini/skill/SKILL.md`.
- The same files without the version in the name, `SHA256SUMS.txt` and `release-manifest.json`.

## Publish / Publikacja

Pushing a tag `v<version>` (the version from `product.json`) starts `.github/workflows/release.yml`. It runs the tests, builds the ZIPs and creates the release with `release/release-notes.md`. Nothing is published before the tag is pushed.

After the release is created, copy `release-manifest.json` from the release files to `release/manifest.json` in the repository, commit and push. The package page reads this file to show the download buttons, without it the page shows the fallback. / Po utworzeniu wydania skopiuj `release-manifest.json` z plików wydania do `release/manifest.json`, zatwierdź i wypchnij. Strona pakietu czyta ten plik.
