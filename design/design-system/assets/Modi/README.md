Wählbare Farbmodi für das KAIWA-Icon „K.“. Die Voreinstellung ist der Schwarzweiß-Modus (Gruppe `Logos`). Wer das Logo personalisiert, wählt einen der beiden Modi **spectrum** oder **SHIFT**. Ohne Wahl gilt der Schwarzweiß-Modus. Jeder Modus liegt als ein Icon vor.

## Dateien

- `kaiwa-icon-spectrum.svg`: Modus spectrum (Flagge tęcza / rainbow). Sechs waagrechte Streifen von Rot oben bis Violett unten.
- `kaiwa-icon-shift.svg`: Modus SHIFT (Flagge trans). Fünf waagrechte Streifen Hellblau, Rosa, Weiß, Rosa, Hellblau.

## Aufbau

- Die Kachel besteht aus den Flaggenstreifen, waagrecht wie in der Flagge, je 55 Prozent mit `papier` aufgehellt. Werte aus `design/logo/themes.json` im Repo.
- spectrum: `#EB8582`, `#F7C280`, `#F7EE80`, `#85BD91`, `#95A0C0`, `#B896BB` (aus `#E40303`, `#FF8C00`, `#FFED00`, `#008026`, `#24408E`, `#732982`).
- SHIFT: `#AEE0F1`, `#F3D0D3`, `#F7F6F3`, `#F3D0D3`, `#AEE0F1` (aus `#5BCEFA`, `#F5A9B8`, `#FFFFFF`, `#F5A9B8`, `#5BCEFA`).
- K und Quadrat stehen in `tinte` (#14171F). Kachelradius `radius-logo`, Lage des Zeichens wie im Icon der Gruppe `Logos`.

## Regeln

- Die Modi sind eine Wahl der Person, die das Dokument verantwortet, kein Zustand des Dokuments. Sie ändern keine Bedeutung.
- Die Kachel ist selbst farbig. Eine helle oder dunkle Fassung gibt es nicht. Sie steht auf hellem und auf dunklem Grund.
- Das Quadrat ist in den Modi `tinte` und zeigt keinen Status. Zustände (`Status`) gelten nur im Schwarzweiß-Modus auf der dunklen Kachel.
- Ein Logo mit Wortmarke gibt es in den Modi nicht. Neben dem Modus-Icon steht die Wortmarke aus `Logos`.

## Hinweise

- Die Flaggenfarben sind gängige Hex-Werte ohne Primärquelle.
- `tinte` erreicht auf den aufgehellten Streifen mindestens 6,9 zu 1 (spectrum, violetter Streifen) und 12,6 zu 1 (SHIFT).
