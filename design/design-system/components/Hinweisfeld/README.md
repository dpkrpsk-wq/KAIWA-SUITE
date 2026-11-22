Das Hinweisfeld hebt eine Aussage über das Dokument hervor: einen Hinweis, eine Stelle zur Prüfung oder den Entwurfsstand.

## Varianten

- **Uwaga / Note.** Grund `flaeche-hinweis`, 3px Rand in `text`, harter Versatz `schatten-hart`, Etikett in `text`. Für neutrale Angaben.
- **Do sprawdzenia / To be checked.** Fläche `signal`, Text und Etikett in `tinte`, 3px Rand, harter Versatz. Das lauteste Feld, darum selten. Für Stellen, die niemand extern geprüft hat (Zitate, Zahlen, Fundstellen, KI-Anteile).
- **Wersja robocza / Draft.** Wie Hinweis, aber 3px gestrichelter Rand in `entwurf`, Etikett in `entwurf`, ohne Versatz. Für den Entwurfsstand des Dokuments.

## Was die Person liefert

Ein kurzer Text, polnisch zuerst und englisch dahinter in `text-gedaempft`. Bei der Variante zur Prüfung nennt der Text, was zu prüfen ist und womit.

## Regeln

- Das Etikett trägt immer das Wort der Variante. Die Variante ist nie nur an Farbe oder Randstil zu erkennen.
- Innenabstand `space-4`, Eckradius `radius-0`, Rand 3px rundum, harter Versatz nach unten rechts (außer beim Entwurf).
- Ein Hinweisfeld nennt keine Herkunft („von KI geschrieben“). Das Etikett `Do sprawdzenia` markiert Unsicherheit und behauptet nichts über den Urheber.
- Nicht mehr als drei Felder je Seite. Ein Feld je Aussage.
- Ein Feld zur Prüfung bleibt stehen, bis die Prüfung dokumentiert ist, und wird dann durch einen Hinweis mit Prüfer und Datum ersetzt.
