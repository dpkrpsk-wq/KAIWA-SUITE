---
name: Entwurfsnotiz Onboarding-Seite KAIWA
status: draft
last_changed: 2026-11-06
audience: Denis Pokropski (Entscheidung über Veröffentlichung)
---

# Entwurfsnotiz: Onboarding-Seite KAIWA

`docs/index.html` ist eine statische Seite ohne Build-Werkzeug. Assets liegen in `docs/assets/`. Die Seite ist lokal gebaut und nicht veröffentlicht. GitHub Pages ist nicht eingeschaltet, nichts ist gepusht, nichts ist committet.

## Vergleich mit Repo A und Begründung

Repo A (`humanities-ai-methodology/docs/index.html`) funktioniert dort, wo es Entscheidungen abnimmt: die vierstufige Leiter als Hauptbild, die Paste-Karte als greifbares Objekt mit Kopieren-Knopf, die sichtbaren Ehrlichkeitsmarken (Entwurfsstand, „illustrativ“) und die Regel, dass alles in einer Datei ohne Telemetrie liegt. Diese Haltung ist übernommen: Entwurfsmarke im Kopf, Hinweisfelder „do sprawdzenia“ an den Stellen, die nicht getestet sind, und eine Seite ohne Skripte von Dritten.

Besser machen wir drei Dinge. Erstens trägt die Seite SUITE statt einer eigenen Palette und folgt dem Systemthema hell oder dunkel, während Repo A trotz der Vorgabe „beide Schemata“ ein festes Marineblau erzwingt, eine nicht geladene Schrift (IBM Plex) nennt und mit Perlenringen und Hintergrundbild dekoriert. Zweitens ist sie dreisprachig (Polnisch voreingestellt, Englisch, Deutsch) mit Umschalter und `lang`-Attribut an jedem Textknoten, Tastaturbedienung, Sprunglink, Navigation und geprüftem Kontrast, wo Repo A nur Englisch und keine Navigation hat. Deutsch ist seit der Änderung vom 2026-11-06 01:22 dabei, mit denselben Quellenregeln, und der deutsche Essay dient als Quelle. Drittens ersetzt sie das Quiz durch Schritte nach Plattform, denn KAIWA hat bisher eine Anleitung (Copilot), und ein Quiz würde zu Stufen führen, die es noch nicht gibt.

## Aufbau und Quelle jeder Aussage

| Abschnitt | Quelle im Paket |
| --- | --- |
| Kopf, Stand, Fußzeile | `produkt.json`, `README.md`, SUITE-Komponenten Dokumentkopf und Fusszeile |
| Do czego (Zweck, Annahmen, Testfragen) | `esej/uzasadnienie-metody.de.md`, `README.md` (deutscher Text folgt dem Essay) |
| Cztery moduły | `README.md`, `SETUP.pl.md`, `KONTEKST.pl.md`, Essay |
| Jak zacząć | `SETUP.pl.md`, `SETUP.en.md`, `office/rejestry.xlsx` (fünf Register, Blätter geprüft) |
| Granice | `SETUP.pl.md`, `SETUP.en.md`, `KONTEKST.pl.md`, Essay |
| Zasady uczelni | `SETUP.pl.md`, `SETUP.en.md`, Essay |
| Stan, licencja, kontakt | `README.md`, `SETUP.*`, `logo/status.json`, `logo/themen.json` |

Wirkungsaussagen des Essays („Vorteile für die Lehre“) stehen als „Założenia autora, nie wyniki badań“. Die Lizenz steht nur als geplant, weil im Repo keine Lizenzdatei für das Gesamtpaket liegt. Die Seite enthält keinen Bezug zu Geschäft, mentalpinG-Ops, AI-Lens oder bizdev und keine Herkunftsangabe zum Text.

## Personalisierung

Modus (schwarzweiß, spectrum, SHIFT) und Statusfelder (sieben Zustände mit Form, Farbe und Name) liegen in einem eingeklappten Feld „Personalizacja“. Schwarzweiß ist voreingestellt. Die Wahl ändert Logo und Tab-Icon und wird in `localStorage` gemerkt, ohne Cookie. Der Status zeigt sich am Kopf-Logo nur im Schwarzweiß-Modus, weil es keine Dateien für Modus und Status zusammen gibt. Im dunklen Theme nimmt die Seite die helle Kachel (SUITE: helle Kachel auf dunklem Grund), bei den Status-Icons bleibt die dunkle Kachel mit Haarlinie.

## Mechanisch geprüft (2026-11-06)

1. Kein Semikolon, kein Gedankenstrich und kein Halbgeviertstrich in allen Textknoten aller drei Sprachen und Attributtexten (Skript, Ergebnis 0 Verstöße, auch 0 Treffer im ganzen Dateitext für die Striche).
2. Alle 669 Textknoten liegen unter einem `lang`-Attribut (`pl`, `en`, `de`). Die Dokumentsprache und der Titel folgen dem Umschalter.
3. Kontrast nach WCAG, Tokenpaare: Text 13,1 bis 15,6 zu 1, gedämpfter Text 6,3 bis 8,8 zu 1, Entwurfsfarbe 6,0 bis 8,5 zu 1, Linie 3,8 zu 1 (hell und dunkel, auf `flaeche` und `flaeche-hinweis`).
4. Browser-Pane (Chromium): alle drei Sprachen (Umschalter, `html lang` und Titel wechseln mit), Umschalter, Modus und Status, dunkles Theme und mobile Breite 375 px ohne horizontales Scrollen. Schriften Space Grotesk und Source Serif 4 laden, polnische Zeichen erscheinen.

## Offene Punkte

1. Der polnische Text ist nicht vom Autor geprüft. Das steht auch im README als Punkt vor der Veröffentlichung. Der englische Text ist nach SETUP.en gebaut, der deutsche nach dem Essay und SETUP.pl. Beide sind ebenfalls ungeprüft.
2. Alle Links zeigen auf das private Repo `dpkrpsk-wq/KAIWA-SUITE` (Zweig `main`). Sie laufen ins Leere, solange es privat ist. Dateipfade im Text sind kein Link, weil relative Pfade unter `docs/` als Pages-Wurzel nicht ins Repo führen.
3. Google Fonts: Das Laden überträgt die IP-Adresse an Google. SUITE sieht Google Fonts vor, Repo A verzichtet auf Fremdquellen. Alternative: die zwei Schriften als Dateien in `docs/assets/` ablegen. Entscheidung offen.
4. Die Uni-Adresse steht auf der Seite, wie in den Paketdateien. Sie enthält die Matrikelnummer. Die Nummer selbst steht auf der Seite nicht. Ob die Adresse öffentlich erscheinen soll, ist zu entscheiden.
5. `noindex` ist gesetzt, solange das Paket nicht veröffentlicht ist. Vor der Veröffentlichung entfernen.
6. Die Fußzeile trägt den Platzhalter `⟨commit⟩` (SUITE-Regel: Export mit Platzhalter ist kein Export). Der Kurz-Hash kommt nach dem Commit.
7. Sobald eine Lizenzdatei im Repo liegt, ist der Lizenzabschnitt anzupassen (Feld „Planowane“ entfällt oder ändert sich).
8. `docs/assets/kaiwa-icon-hell.svg` ist per Farbtausch aus dem Neutral-Icon erzeugt, nicht aus SUITE übernommen (die SUITE-Logodateien liegen als Blobs und sind nicht gelesen). Abgleich mit dem SUITE-Asset steht aus.
9. Mehrsprachigkeit: SUITE setzt „Polnisch, dahinter Englisch“. Die Seite zeigt eine Sprache auf einmal und folgt SUITE nur bei den Statusnamen und Feldetiketten. In englischen und deutschen Stücken steht als Gegenbezeichnung das polnische Wort.
10. Stand der Modulangaben ist der 05.11.2026 (README). Wenn der Copilot-Test abgeschlossen ist, sind Modulstatus und Hinweisfelder anzupassen.
11. Nicht geprüft: Bildschirmleser, Firefox und Safari, Druckansicht (nur eine Minimalregel).
12. Veröffentlichung später: GitHub Pages mit Quelle `main` und Ordner `/docs` einschalten. Das ist nicht geschehen.
13. Deutsche Fachwörter sind Wahl der Übersetzung, nicht aus einer Paketdatei: „Prüfwert“ und „Einordnung (Triage)“ stehen im Essay, „Kulturkontrolle“ für „Kontrola kulturowa“ und „Strom der Gedanken“ für „strumień świadomości“ sind gesetzt. Das Schlusswort für den Strom-Agenten nennt die deutsche Seite „koniec“ (polnisch) und „end“ (englisch), weil SETUP nur diese beiden kennt.
