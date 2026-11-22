Die Tabelle ordnet Daten in Zeilen und Spalten mit Kopfzeile in `tinte`, Haarlinien und fluchtenden Ziffern.

## Aufbau

- Kopfzeile: Grund `tinte`, Text `papier`, Stil `etikett`, darunter eine 6px-Kante in `signal`. Polnisch zuerst, Englisch dahinter in Normalschrift. Die ganze Tabelle trägt den harten Versatz `schatten-hart`.
- Zeilen: Stil `tabelle` mit Gewicht 600 bei 16px, 3px Linie in `text` unter jeder Zeile, Polster `space-3`. Kein Zebramuster.
- Zahlen stehen rechtsbündig mit `font-variant-numeric: tabular-nums`.
- Unterschrift unter der Tabelle in `fussnote`, Farbe `text-gedaempft`: `Tabela N.` plus Titel plus Quelle.

## Was die Person liefert

Zeilen mit Werten, einen Titel und die Quelle der Zahlen. Fehlt die Quelle, schreibt die Unterschrift `źródło: do uzupełnienia`.

## Regeln

- Kopfzeile bleibt in `tinte` und `papier` in beiden Themes. Sie ist ein fester Logoton und passt sich nicht an.
- Stand und Entwurf stehen als Wort in `entwurf`, nie als eingefärbte Zeile.
- Eine Tabelle, deren Zahlen aus einer KI-Ausgabe stammen, bekommt ein `Hinweisfeld` zur Prüfung daneben und einen Eintrag im `Begleitblatt`.
- Eckradius `radius-0`, keine senkrechten Linien.
