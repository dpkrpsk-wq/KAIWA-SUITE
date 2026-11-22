KAIWA, warp mode: das KAIWA-Logo (Produktnummer 26.01) in zwei Formen und zwei Fassungen, übernommen unverändert aus `design/logo/`. Ein Krake schwimmt auf den Tunnel zu. Kraken gelten als sehr intelligent, und das Flugzeug passte nicht zum Zeichen. Der Übergang durch den Tunnel ist der warp mode. Dunkle Kachel, sechs verschachtelte Ellipsen als Tunnel mit ungleichen Abständen und wechselnder Strichstärke, dunkler Kern, Krake (Körper mit Flossen zum Tunnel, sechs Arme mit runden Spitzen, ein Auge) mit zwei blassen Kopien als Echo dahinter, Leuchtquadrat. Die Beschriftung „warp mode“ steht zweizeilig oben links, nach vorn geneigt.

## Dateien

- `kaiwa-logo-dunkel.svg`: Logo mit Beschriftung. Kachel `tinte` (#14171F), Zeichen und Schrift `papier` (#F1EFE9), Kern #07080C. Original. Auf hellem Grund (`flaeche` im Theme hell).
- `kaiwa-logo-hell.svg`: gleiche Geometrie, Töne von Kachel und Zeichen vertauscht. Kachel `papier`, Zeichen `tinte`, Kern bleibt #07080C. Auf dunklem Grund (`flaeche` im Theme dunkel).
- `kaiwa-icon-dunkel.svg` und `kaiwa-icon-hell.svg`: dieselben Fassungen ohne Beschriftung. Für kleine Größen, Agenten-Icon, Favicon, Dokumentkopf.

Die Töne stehen fest in den Dateien. `currentColor` wirkt in `<img>` nicht. Eine dunkle Kachel auf dunklem Grund verschwindet, darum gibt es die helle Fassung.

## Voreinstellung, Status und Modi

Das Leuchtquadrat zeigt in der Komponente `Status` einen von sieben Zuständen. Diese Gruppe ist der Schwarzweiß-Modus und die Voreinstellung des Logos. Wer personalisiert, wählt einen der beiden Farbmodi spectrum oder SHIFT aus der Gruppe `Modi`.

## Regeln

- Das Logo mit Beschriftung steht ab 128 px Kantenlänge am Bildschirm (im Druck ab 34 mm). Darunter ist die Schrift kleiner als 11 px und nicht mehr sicher lesbar.
- Das Icon ohne Beschriftung gilt unter 128 px. Mindestgröße 32 px (Favicon), dort erkennt man Krake und Tunnel als Fleck. Bei 24 px bleibt nur noch ein Umriss, nicht verwenden. Das Echo hinter dem Kraken und die einzelnen Ringe erscheinen ab etwa 64 px. Im Dokumentkopf steht das Icon mit 64 px.
- Schutzraum ringsum mindestens ein Viertel der Kantenlänge (bei 128 px also 32 px). Nichts steht in diesem Raum.
- Eckradius 48 auf 320, also `radius-logo` (15 Prozent). Beim Skalieren nicht ändern.
- Nicht drehen, nicht strecken, nicht umfärben, keine Schatten, kein Verlauf. Das Echo und die Ringe nicht zu Flächen füllen.
- Der Name „KAIWA“ steht daneben als Text in `titel`.

## Offen

Die Beschriftung „warp mode“ ist SVG-Text in Space Grotesk 500. In `<img>`-Darstellung (Assets-Ansicht, andere Seiten) fällt sie auf Arial zurück, weil SVG in `<img>` keine Webschrift nachlädt. Die Vorschauen der Komponenten binden das Logo inline ein, dort greift Space Grotesk. Für Druck und Weitergabe fehlt eine Fassung mit Umrissen für die Beschriftung. Das Icon hat keinen Text und ist davon frei.
