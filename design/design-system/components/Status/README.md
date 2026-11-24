Das Status-Zeichen ist das Leuchtquadrat unten rechts im KAIWA-Logo. Es zeigt einen von sieben Zuständen an.

**Farbe allein bedeutet nichts.** Der Zustand steht immer als Wort daneben (Polnisch zuerst, Englisch dahinter). Die Form trägt die Bedeutung mit, wo sie sich unterscheidet.

## Zustände

| Polnisch | English | Form | Farbe | Token | Kontrast zu `tinte` |
| --- | --- | --- | --- | --- | --- |
| aktywny | active | Quadrat mit Haken | `#3FB97A` | `status-aktiv` | 7,2 zu 1 |
| w toku | running | Rahmen mit Punkt | `#5B9BF0` | `status-laeuft` | 6,3 zu 1 |
| wstrzymany | paused | zwei Balken | `#E6B84A` | `status-pausiert` | 9,7 zu 1 |
| ostrzeżenie | warning | Quadrat mit Ausrufezeichen | `#F0883E` | `status-warnung` | 7,1 zu 1 |
| błąd | error | Quadrat mit Kreuz | `#EF5A52` | `status-fehler` | 5,3 zu 1 |
| wyłączony | off | nur Rahmen | `#8A919B` | `status-aus` | 5,6 zu 1 |
| neutralny | neutral | volles Quadrat | `#F1EFE9` | `status-neutral` | 15,6 zu 1 |

## Regeln

- Die Zustandsfarben stehen nur im Leuchtquadrat auf der dunklen Kachel (`tinte`). Alle erreichen dort mindestens 5 zu 1.
- Nicht als Text- oder Flächenfarbe auf `flaeche` im Theme hell verwenden. Auf `papier` liegen sie zwischen 1,6 und 2,9 zu 1.
- Die Marken auf dem Quadrat (Haken, Ausrufezeichen, Kreuz) und der Punkt im Rahmen sind `tinte` bzw. die Zustandsfarbe. Jeder der sieben Zustände hat eine eigene Form, keine teilt sich eine.
- Die Form ist nach Augenmaß ab einem Quadrat von rund 9 px lesbar. Im Icon „K.“ ist das Quadrat 0,127 der Kantenlänge, die Grenze liegt also bei etwa 72 px. Darunter trägt nur noch die Farbe, dort muss das Wort daneben stehen.
- Die Zustände wechseln nur am Leuchtquadrat. Das K bleibt.
- Eine Status-Anzeige ersetzt keine Prüfung. Sie meldet, was das Programm zählt, und nicht, ob es stimmt.

## Hinweise

- Die Farbbedeutung lehnt sich an die übliche Ampel-Logik für Anzeigeleuchten an (grün normal, gelb Abweichung, rot Fehler, blau Hinweis oder laufend, grau aus). Sie ist nicht an einer Norm geprüft.
- Die Form trägt die Bedeutung mit (WCAG 1.4.1), aber nur dort, wo das Quadrat groß genug zu erkennen ist. In der Praxis steht das Wort daneben.
- Quelle: `output/kaiwa/logo/status.json`. Die Zustands-SVG im Repo zeigen noch das alte Zeichen mit Flugzeug und gelten nicht mehr.
