Die Fußzeile trägt auf jeder Seite Produktname, Nummer, Version, Commit und Seitenzahl.

## Aufbau

- Linie oben (6px `text`), darunter eine Zeile in `fussnote`, Farbe `text-gedaempft`.
- Links: Produktname in Space Grotesk 500 und `text`, dann Nummer, `wersja <Version>`, `commit <Hash>`. Getrennt durch ` · `.
- Rechts: `strona N z M / page N of M`.

## Was das Produkt liefert

Nummer und Version aus `produkt.json`, den Kurz-Hash (7 Zeichen) aus dem Git-Stand des Exports, Seitenzahlen aus dem Ausgabeformat.

## Regeln

- In Vorlagen steht der Platzhalter `⟨commit⟩` auf einer `signal`-Fläche mit gestricheltem Rand in `tinte`. Der Export ersetzt ihn. Ein Dokument, das mit Platzhalter hinausgeht, gilt als nicht exportiert.
- Kein Logo in der Fußzeile, damit der Kopf das einzige Markenelement der Seite bleibt.
- Kleinste Schrift des Systems (11px). Darunter nicht gehen.
- Herkunft von Textanteilen steht hier nicht, sondern im `Begleitblatt`.
