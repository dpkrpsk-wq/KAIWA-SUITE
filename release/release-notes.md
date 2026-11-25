KAIWA SUITE 26.01, version 0.2.0 (working draft / wersja robocza)

This is a draft. It has not been reviewed externally and most modules are untested in the assistants named below. / To wersja robocza, nie przeszła zewnętrznego sprawdzenia, a większość modułów nie była testowana w wymienionych asystentach.

## Download / Pobierz

One ZIP per vendor, unpack it into a folder and follow `1-start/setup.en.md` (Polish: `setup.pl.md`) or the guide of your vendor in `2-agents/<vendor>/`. / Jeden ZIP na dostawcę, rozpakuj do folderu i postępuj według instrukcji.

| File | For |
|---|---|
| `KAIWA-SUITE-copilot-<version>.zip` | Microsoft 365 Copilot, Agent Builder (copy name, description and instructions from the files) |
| `KAIWA-SUITE-copilot-skill-<version>.zip` | Copilot dialog "Upload skill", one `SKILL.md` in the root. Not tested in Copilot yet. |
| `KAIWA-SUITE-copilot-plugin-<version>.zip` | Copilot plugin package (Cowork, Admin Center). Not verified. It needs a licence or an administrator. |
| `KAIWA-SUITE-gemini-<version>.zip` | Google Gemini |
| `KAIWA-SUITE-chatgpt-<version>.zip` | ChatGPT (Go account, Projects) |
| `KAIWA-SUITE-chatgpt-plugin-<version>.zip` | ChatGPT plugin with four skills for every chat of the account (Plugins, add, upload plugin archive). Draft, untested in ChatGPT beyond the first runs. |
| `KAIWA-SUITE-claude-<version>.zip` | Claude (claude.ai projects, Claude Code skills) |
| `KAIWA-SUITE-any-<version>.zip` | Without a vendor: templates, protocols, scripts, Word and Excel |
| `SHA256SUMS.txt`, `release-manifest.json` | Checksums and file list |

The same files without the version in the name are the stable links. / Te same pliki bez wersji w nazwie to stałe linki.

## Note / Uwaga

- Do not drag a ZIP file into the Copilot chat window, it is not accepted as an attachment. Unpack it first. / Nie przeciągaj ZIP do czatu Copilot, nie jest przyjmowany jako załącznik. Najpierw rozpakuj.
- Excel files that Copilot creates carry the account owner's name in the file properties. Check them before you share them. / Pliki Excel z Copilot mają we właściwościach imię i nazwisko właściciela konta.
- A hash in the register shows that a text did not change after it was recorded, not that it was copied correctly. / Skrót w rejestrze pokazuje, że tekst nie zmienił się po zapisie, nie że przepisano go wiernie.

## Licence / Licencja

Own content CC BY-NC-SA 4.0, copies in `method/` CC BY-SA 4.0, font under OFL. Commercial use needs a separate licence, see `LICENSE-COMMERCIAL.md`. AI involvement is listed in `DISCLOSURE.md`. Feedback: Denis Pokropski, 285421@student.uwr.edu.pl.
