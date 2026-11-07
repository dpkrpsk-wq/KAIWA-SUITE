# Gate-Vorbereitung KAIWA 0.2.0, Stand 2026-11-07

Vorbereitungsnotiz für das Publikations-Gate (Skill `publication-clearance`). Das Gate selbst ist nicht gelaufen und startet erst auf ausdrückliches Go des Herausgebers. Zahlen aus `git ls-files` und `wc -w` am Branch `gestaltung-kaiwa-suite`, Commit 7353dd4, plus die drei Entwürfe dieser Sitzung.

## 1. Umfang des Pakets

Textdateien nach Sprache (Wörter nach `wc -w`, gerundet):

| Sprache | Dateien | Wörter |
|---|---|---|
| Polnisch | `KONTEKST.pl.md`, `SETUP.pl.md`, `office/README.pl.md`, vier Vorlagen in `szablony/`, Agentenfelder und Anweisungen für analiza, mapa, źródła, Agentenfelder für strumień | rund 7 300 |
| Polnisch und Englisch gemischt | `README.md`, `prompts/LICENSE.md`, `protokoly/LICENSE.md` | rund 1 100 |
| Englisch | `SETUP.en.md`, Anweisungen für strumień, elf Dateien in `prompts/` (Triage, Katalog, neun Rahmen), acht Protokolle in `protokoly/` | rund 62 600 |
| Deutsch | `esej/uzasadnienie-metody.de.md`, `docs/design-brief-onboarding.md` | rund 3 100 |
| Dreisprachig im Markup | `docs/index.html` (Onboarding-Seite, wartet auf das Design-System) | rund 8 600 mit Markup |

Neu in dieser Sitzung, noch nicht committet: `esej/uzasadnienie-metody.pl.md` (rund 1 900 Wörter Polnisch), zwei Mailentwürfe unter `docs/` (je rund 450 Wörter Polnisch), diese Notiz.

Ohne Fließtext: `office/rejestry.xlsx`, `produkt.json`, zwei `SHA256SUMS`, sechs Python-Werkzeuge in `tools/`, Logo und zehn Statussymbole als Vektorgrafik.

Rund 84 Prozent des Textes sind unveränderte Kopien aus zwei fremden Repositories unter CC BY-SA 4.0 (`prompts/`, `protokoly/`). Eigene Texte des Pakets sind rund 12 000 Wörter.

## 2. Vorschlag für den Tier: T2

T2 (Operational, substanziell) deckt Material, das unter dem Namen und der Matrikelnummer des Herausgebers an Lehrende der eigenen Hochschule geht und dort als Arbeitsgrundlage dienen soll. Gründe gegen die Nachbarn:

- T1 (Public-informal) lässt Lexicon-Stability, Claim-Prüfung und AI-Provenance optional. Ein Paket, dessen Methode die Herkunft jedes Gedankens verlangt, muss die eigene Herkunft offenlegen können. AI-Provenance (D10) gehört deshalb auf Pflicht, und das gibt erst T2.
- T3 (Scholarly) setzt Source-Attestation (D8) für den gesamten Text auf Pflicht. Für rund 62 000 Wörter fremder Protokolle und Prompts, die nicht zitiert, sondern weitergegeben werden, trägt das nichts bei und blockiert ohne Gewinn. Das Paket ist nicht zitierfähig gemeint.

Geht nur der Essay allein an Dritte, reicht T1 (Essay). Die Tier-Wahl bleibt beim Herausgeber, das Gate flaggt nur einen Mismatch.

Zwei Risiken aus Abschnitt 3 (Marke, Lizenz) prüft keine Dimension der Matrix. Sie sind vor dem Gate zu entscheiden, nicht durch das Gate.

## 3. Bekannte Risiken und was vor dem Gate fehlt

1. **Unionsmarke KAIWA.** Beim Amt der Europäischen Union für geistiges Eigentum ist unter der Nummer 018773497 die Wortmarke KAIWA eingetragen, unter anderem in den Klassen 9 (Software) und 41 (Bildung). Fehlt: eine Entscheidung des Herausgebers, ob der Name für ein nicht kommerzielles Testpaket im Hochschulkontext bleibt oder vor der Weitergabe wechselt, gegebenenfalls nach einer Einschätzung des Kollisionsrisikos.
2. **Namensnennung mentalpinG-Ops.** Der Name steht an 15 Stellen: in `prompts/LICENSE.md` und `protokoly/LICENSE.md` als Lizenzgeber mit Verweis auf Repositories unter diesem Konto, als Fußzeile „© mentalpinG-Ops. Dual-licensed“ in allen zehn Prompt-Dateien, in `README.md` Zeile 34 und zweimal in `copilot/analiza/INSTRUCTIONS.txt`. CC BY-SA 4.0 verlangt die Nennung, die Persona Geschäft erscheint damit in einem Paket der Persona Forschung, und die Fußzeilen der Prompts bieten zusätzlich eine kommerzielle Lizenz an. AI-Lens und XIOM kommen im Paket nicht vor (Grep 2026-11-07). Fehlt: die ausdrückliche Bestätigung, dass die Nennung in dieser Form bleibt, oder eine Entscheidung, die Prompt-Fußzeilen als vermerkte Änderung zu kürzen.
3. **aXIOM in `prompts/core/artifact-triage.md`, Zeile 204.** Die Dimension D1 (Material-Boundary) führt aXIOM als verbotenes Token und läuft auf jedem Tier als Floor. Die Datei ist eine unveränderte Kopie mit Prüfsumme in `SHA256SUMS`, eine Änderung widerspricht dem Satz „Zmiany: brak“ in `prompts/LICENSE.md`. Dazu kommt ein Currency-Problem: die Kopie stammt vom 3. November, die Quelle hat die Triage zwischen dem 3. und 5. November auf einen Kernprompt mit erzeugtem Katalog umgestellt und Artifact Triage außer Betrieb genommen. Fehlt: eine Entscheidung, ob die Triage-Datei neu aus der Quelle kopiert, mit vermerkter Änderung angepasst oder aus dem Paket genommen wird.
4. **Lizenz des übrigen Pakets.** `README.md` sagt, die Lizenz werde vor der Veröffentlichung festgelegt. Gewollt ist eine Doppellizenz nach dem Muster CC BY-SA 4.0 offen plus kommerzielle Nutzung nach Vereinbarung. Fehlt: eine `LICENSE.md` im Repo-Wurzelverzeichnis und der angepasste Satz im README.
5. **Copilot-Test P1 negativ.** Der Tenant der Universität erlaubt kein Hochladen eigener App-Pakete. README, SETUP, Essay und beide Mailentwürfe sagen, das Paket laufe mit dem Konto der Universität in Microsoft 365 Copilot ohne zusätzliche Lizenz. Fehlt: ein Nachweis, dass der Agent Builder im Tenant verfügbar ist (das ist ein anderer Weg als ein App-Paket), sonst müssen diese Sätze vor dem Versand weichen, weil D4 (Data-Fidelity) sie sonst als unbelegt wertet.
6. **Polnische Texte vom Herausgeber ungelesen.** Das betrifft alle polnischen Dateien des Pakets 0.2 und neu den polnischen Essay und die zwei Mailentwürfe. Fehlt: die Lektüre durch den Herausgeber, das README nennt sie selbst als Bedingung vor der Veröffentlichung.
7. **AI-Provenance des Pakets selbst (D10, auf T2 Pflicht).** Die Texte des Pakets stammen nach dem Provenienz-Log aus Claude-Sitzungen auf Vorgaben des Herausgebers, und auf dessen Wort steht das nicht in den Texten. Das Paket enthält die Vorlage `szablony/ujawnienie-narzedzia.pl.md` für genau diese Offenlegung. Fehlt: eine ausgefüllte Offenlegung für das Paket als Begleitnotiz, sonst meldet D10 eine Lücke.
8. **Kürzelregel im deutschen Essay.** Der deutsche Essay schreibt elfmal „KI“, die polnische Fassung schreibt „sztuczna inteligencja“ aus. Fehlt: die Entscheidung, ob der deutsche Text mitzieht.

## 4. Geschätzter Aufwand je Prüfagent

Auf T2 laufen D1, D2, D3 mechanisch in der Hauptsitzung. Urteilsdimensionen mit eigenem Agent: D4, D5, D6, D9, D10 als Pflicht, D7, D8, D11 als Option. Das sind fünf bis acht Agenten.

Die Volllektüre aller Texte des Pakets sind rund 74 000 Wörter Fließtext plus Onboarding-Seite, in Tokens grob 110 000 bis 120 000 je Agent, polnischer und deutscher Text brauchen mehr Tokens je Wort als englischer. Dazu Web-Abrufe (Markenregister, Quell-Repositories, Lizenztexte) und die Ausgabe. Arbeitszahl: 130 000 bis 190 000 Tokens je Agent, bei fünf Agenten rund 650 000 bis 950 000, bei acht rund 1 000 000 bis 1 500 000. Modell nach Token-Regel: sonnet für Urteilsdimensionen, haiku für den Lexicon-Sweep (D3).

Vor dem Lauf: Vorprüfung `preflight.ps1`, Currency-Check (Punkt 3 oben trifft ihn), Risiken 1 bis 5 entschieden.
