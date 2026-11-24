KAIWA-Logo „K.“: das Zeichen K mit Quadrat, daneben die Wortmarke KAIWA und die Unterzeile „KIT FOR ACADEMIC INQUIRY WITH AI“. Nachgezeichnet nach der Vorlage `Minimalistisches_KAIWA-Logo-Branding.png` von Denis Pokropski (2026-11-24), Farben aus den Tokens. Es ersetzt das Logo „KAIWA, warp mode“ mit Flugzeug und Tunnel.

## Dateien

- `kaiwa-logo-dunkel.svg`: Zeichen, Wortmarke und Unterzeile in `tinte` (#14171F), Quadrat in `tinte`. Auf hellem Grund (`flaeche` im Theme hell).
- `kaiwa-logo-hell.svg`: dasselbe in `papier` (#F1EFE9), Quadrat in `signal` (#FFED00). Auf dunklem Grund (`flaeche` im Theme dunkel).
- `kaiwa-icon-dunkel.svg`: Kachel `tinte`, K in `papier`, Quadrat in `signal`. Auf hellem Grund, für Favicon, Agenten-Icon und Dokumentkopf.
- `kaiwa-icon-hell.svg`: Kachel `papier`, K und Quadrat in `tinte`. Auf dunklem Grund.

Die Töne stehen fest in den Dateien. `currentColor` wirkt in `<img>` nicht.

## Aufbau

- Das K besteht aus Stamm, Arm und Bein. Das Bein endet senkrecht vor dem Quadrat. Das Quadrat steht auf der Grundlinie, seine Kante ist 0,24 der Zeichenhöhe.
- Wortmarke KAIWA: fünf Buchstaben aus geraden Linien, nachgezeichnet, keine Schrift.
- Unterzeile: Montserrat 500 (SIL Open Font License), gesperrt, als Pfade. Sie hängt an keiner geladenen Schrift und sieht in `<img>` überall gleich aus.
- Kachel: Radius `radius-logo` (15 Prozent). Das Zeichen nimmt 0,6 der Kachelbreite ein.

## Farbe des Quadrats

- Auf `tinte` steht das Quadrat in `signal` (14,8 zu 1). Nur dort trägt es Farbe.
- Auf `papier` steht das Quadrat in `tinte`. `signal` erreicht auf `papier` nur 1,1 zu 1 und wäre unsichtbar.
- Das Quadrat ist das Leuchtquadrat. Zustände (`Status`) zeigt es nur auf der dunklen Kachel.

## Regeln

- Logo mit Unterzeile ab 400 px Breite. Darunter wird die Unterzeile kleiner als 8 px Versalhöhe, dann steht das Icon.
- Icon ab 32 px Kantenlänge (Favicon). Im Dokumentkopf steht es mit 64 px.
- Schutzraum ringsum mindestens die Kante des Quadrats, beim Icon ein Viertel der Kantenlänge.
- Nicht drehen, nicht strecken, nicht umfärben, keine Schatten, kein Verlauf. Das Quadrat nicht durch eine andere Form ersetzen.

## Offen

- Die Schrift der Unterzeile in der Vorlage ist nicht bestimmt. Montserrat 500 deckt sich in der Überlagerung mit der Vorlage.
