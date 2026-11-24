Der Dokumentkopf eröffnet jede Seite eines Produkts der KAIWA SUITE mit Logo, Produktname, Produktnummer, Version, Stand und Entwurfsmarke.

## Aufbau

- Eine volle Kopfplatte in `text` (im Theme hell dunkel, im Theme dunkel hell) mit hartem Versatz `schatten-hart`. Links das Icon ohne Beschriftung (80 px, `kaiwa-icon-hell` auf der dunklen Platte, `kaiwa-icon-dunkel` auf der hellen), daneben die Wortmarke in Versalien, zwei Zeilen: KAIWA über SUITE, Stil `titel` mit Gewicht 700.
- Rechts über Signalbändern im 35-Grad-Winkel (`signal`, harte Streifen) die Entwurfsmarke als Aufkleber: Fläche `signal`, Text `tinte`, 3px Rand, leicht gekippt (3 Grad).
- Darunter unter einer 6px-Linie in `text` drei Felder mit `etikett` über dem Wert in `nummer` (32px, Gewicht 700): Numer produktu / Product no., Wersja / Version, Stan / Status. Zwischen Kopf und Inhalt steht `space-6`.

## Was das Produkt liefert

Name, Nummer, Version und Stand aus `produkt.json`. Der Kopf übernimmt sie unverändert. Fehlt ein Wert, bleibt das Feld leer und zeigt `do uzupełnienia / to fill in` in `entwurf`. Es wird nichts erfunden.

## Regeln

- Die Entwurfsmarke steht, solange das Produkt auf `0.x` ist oder das Dokument ungeprüft. Sie fällt erst weg, wenn der Test dokumentiert ist, auf den die Version verweist.
- Die Marke trägt immer das Wort. Die Farbe allein sagt nichts.
- Der Kopf nennt keine Herkunft von Textanteilen. Das gehört ins `Begleitblatt`.
- Ziffern in Tabellenbreite (`font-variant-numeric: tabular-nums`), damit Nummern untereinander fluchten.
- Die Bänder sind harte Streifen mit festen Stufen, keine weichen Verläufe. Sie enden vor der Wortmarke, nichts Wichtiges liegt auf ihnen außer dem Aufkleber.
