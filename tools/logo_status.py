"""Baut aus design/logo/kaiwa-icon.svg (Logo „K.“) je Zustand und je Farbmodus eine Fassung des Icons.

Aufruf: python -I tools/logo_status.py   (schreibt nach design/logo/status/, gleiche Eingabe ergibt gleiche Bytes)
Zustände: design/logo/status.json, Farbmodi: design/logo/themes.json.
Zustand = gefärbtes Leuchtquadrat im K. Jeder Zustand hat eine Farbe und eine eigene Form, damit er auch ohne Farbsehen erkennbar ist.
Modus = Kachel aus waagrechten Flaggenstreifen (mit Papier aufgehellt), K und Quadrat in Tinte; das Quadrat zeigt dort keinen Zustand.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUELLE = ROOT / "design/logo/kaiwa-icon.svg"
# Das Leuchtquadrat steht im Icon als Rechteck im skalierten Zeichenraum des K (Kante 57), ein Treffer je Datei.
LED = '<rect fill="#FFED00" x="488" y="353" width="57" height="57"/>'
KACHEL = '<rect width="320" height="320" rx="48" fill="#14171F"/>'
F = 57 / 22  # Die Formen sind auf ein Quadrat der Kante 22 gezeichnet und werden auf 57 skaliert.


def led(farbe, form):
    """Form des Zustands im Raum 0..22, eingesetzt an der Stelle des Leuchtquadrats."""
    if form == "voll":
        innen = f'<rect width="22" height="22" fill="{farbe}"/>'
    elif form == "rahmen":
        innen = f'<rect x="1.5" y="1.5" width="19" height="19" fill="none" stroke="{farbe}" stroke-width="3"/>'
    elif form == "pause":
        innen = f'<rect width="8" height="22" fill="{farbe}"/><rect x="14" width="8" height="22" fill="{farbe}"/>'
    elif form == "kreuz":
        innen = (f'<rect width="22" height="22" fill="{farbe}"/>'
                 f'<path d="M5 5L17 17M17 5L5 17" stroke="#14171F" stroke-width="3" stroke-linecap="square"/>')
    elif form == "haken":
        innen = (f'<rect width="22" height="22" fill="{farbe}"/>'
                 f'<path d="M4.5 11.5L9 16L17.5 5.5" fill="none" stroke="#14171F" stroke-width="3"/>')
    elif form == "punkt":
        innen = (f'<rect x="1.5" y="1.5" width="19" height="19" fill="none" stroke="{farbe}" stroke-width="3"/>'
                 f'<rect x="7" y="7" width="8" height="8" fill="{farbe}"/>')
    elif form == "ausruf":
        innen = (f'<rect width="22" height="22" fill="{farbe}"/>'
                 f'<rect x="9.5" y="3.5" width="3" height="10" fill="#14171F"/><rect x="9.5" y="15.5" width="3" height="3" fill="#14171F"/>')
    else:
        raise ValueError(f"unbekannte Form: {form}")
    return f'<g transform="translate(488 353) scale({F:.4f})">{innen}</g>'


def kontrast(a, b):
    def lum(h):
        r, g, bl = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(bl)
    hell, dunkel = sorted((lum(a), lum(b)), reverse=True)
    return (hell + 0.05) / (dunkel + 0.05)


def bauen():
    daten = json.loads((ROOT / "design/logo" / "status.json").read_text(encoding="utf-8"))
    themen = json.loads((ROOT / "design/logo" / "themes.json").read_text(encoding="utf-8"))
    quelle = QUELLE.read_text(encoding="utf-8")
    assert quelle.count(LED) == 1, "Leuchtquadrat in kaiwa-icon.svg nicht eindeutig"
    assert quelle.count(KACHEL) == 1, "Kachel in kaiwa-icon.svg nicht eindeutig"
    ziel = ROOT / "design/logo" / "status"
    ziel.mkdir(exist_ok=True)
    for alt in ziel.glob("*.svg"):  # alte Fassungen entfernen, damit nur der aktuelle Stand liegt
        alt.unlink()
    geschrieben = []
    for z in daten["zustaende"]:
        text = quelle.replace(LED, led(z["farbe"], z["form"]))
        text = text.replace("<title>KAIWA</title>", f'<title>KAIWA, {z["pl"]} / {z["en"]}</title>')
        datei = ziel / f"kaiwa-icon-{z['id']}.svg"
        datei.write_text(text, encoding="utf-8", newline="\n")
        geschrieben.append(datei.name)
    tinte, papier, k = themen["tinte"], themen["papier"], themen["aufhellung"]

    def hell(h):  # Flaggenfarbe mit Papier mischen, Anteil k Papier
        a = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
        p = [int(papier[i:i + 2], 16) for i in (1, 3, 5)]
        return "#" + "".join(f"{round(x * (1 - k) + y * k):02X}" for x, y in zip(a, p))

    for th in themen["themen"]:
        n = len(th["farben"])
        hoehe = 320 / n
        baender = "".join(f'<rect y="{i * hoehe:.3f}" width="320" height="{hoehe + 0.5:.3f}" fill="{hell(farbe)}"/>'
                          for i, farbe in enumerate(th["farben"]))
        kachel = (f'<defs><clipPath id="k-{th["id"]}"><rect width="320" height="320" rx="48"/></clipPath></defs>'
                  f'<g clip-path="url(#k-{th["id"]})">{baender}</g>')
        text = quelle.replace(KACHEL, kachel).replace(LED, LED.replace("#FFED00", tinte))
        text = text.replace('fill="#F1EFE9"', f'fill="{tinte}"')
        text = text.replace("<title>KAIWA</title>", f'<title>KAIWA, {th["pl"]} / {th["en"]}</title>')
        datei = ziel / f"kaiwa-icon-{th['id']}.svg"
        datei.write_text(text, encoding="utf-8", newline="\n")
        geschrieben.append(datei.name)
    return geschrieben


if __name__ == "__main__":
    for name in bauen():
        print(name)
