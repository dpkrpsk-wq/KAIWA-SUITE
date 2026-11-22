"""Baut aus design/logo/kaiwa-icon.svg und design/logo/kaiwa-logo.svg je Zustand eine Fassung mit gefärbtem Leuchtquadrat.

Aufruf: python -I tools/logo_status.py   (schreibt nach design/logo/status/, gleiche Eingabe ergibt gleiche Bytes)
Die Zustände stehen in design/logo/status.json. Jeder Zustand hat eine Farbe und eine Form, damit er auch ohne Farbsehen erkennbar ist.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LED = '<rect x="254" y="254" width="22" height="22" fill="#F1EFE9"/>'


def led(farbe, form):
    if form == "voll":
        return f'<rect x="254" y="254" width="22" height="22" fill="{farbe}"/>'
    if form == "rahmen":
        return f'<rect x="255.5" y="255.5" width="19" height="19" fill="none" stroke="{farbe}" stroke-width="3"/>'
    if form == "pause":
        return (f'<rect x="254" y="254" width="8" height="22" fill="{farbe}"/>'
                f'<rect x="268" y="254" width="8" height="22" fill="{farbe}"/>')
    if form == "kreuz":
        return (f'<rect x="254" y="254" width="22" height="22" fill="{farbe}"/>'
                f'<path d="M259 259L271 271M271 259L259 271" stroke="#14171F" stroke-width="3" stroke-linecap="square"/>')
    if form == "haken":
        return (f'<rect x="254" y="254" width="22" height="22" fill="{farbe}"/>'
                f'<path d="M258.5 265.5L263 270L271.5 259.5" fill="none" stroke="#14171F" stroke-width="3"/>')
    if form == "punkt":
        return (f'<rect x="255.5" y="255.5" width="19" height="19" fill="none" stroke="{farbe}" stroke-width="3"/>'
                f'<rect x="261" y="261" width="8" height="8" fill="{farbe}"/>')
    if form == "ausruf":
        return (f'<rect x="254" y="254" width="22" height="22" fill="{farbe}"/>'
                f'<rect x="263.5" y="257.5" width="3" height="10" fill="#14171F"/><rect x="263.5" y="269.5" width="3" height="3" fill="#14171F"/>')
    raise ValueError(f"unbekannte Form: {form}")


def kontrast(a, b):
    def lum(h):
        r, g, bl = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(bl)
    hell, dunkel = sorted((lum(a), lum(b)), reverse=True)
    return (hell + 0.05) / (dunkel + 0.05)


def bauen():
    daten = json.loads((ROOT / "design/logo" / "status.json").read_text(encoding="utf-8"))
    ziel = ROOT / "design/logo" / "status"
    ziel.mkdir(exist_ok=True)
    for alt in ziel.glob("*.svg"):  # alte Fassungen entfernen, damit nur der aktuelle Stand liegt
        alt.unlink()
    geschrieben = []
    for basis in ("kaiwa-icon", "kaiwa-logo"):
        quelle = (ROOT / "design/logo" / f"{basis}.svg").read_text(encoding="utf-8")
        assert quelle.count(LED) == 1, f"Leuchtquadrat in {basis}.svg nicht eindeutig"
        for z in daten["zustaende"]:
            text = quelle.replace(LED, led(z["farbe"], z["form"]))
            text = text.replace("<title>KAIWA</title>", f'<title>KAIWA, {z["pl"]} / {z["en"]}</title>')
            datei = ziel / f"{basis}-{z['id']}.svg"
            datei.write_text(text, encoding="utf-8", newline="\n")
            geschrieben.append(datei.name)
    themen = json.loads((ROOT / "design/logo" / "themes.json").read_text(encoding="utf-8"))
    tinte, papier, k = themen["tinte"], themen["papier"], themen["aufhellung"]

    def hell(h):  # Flaggenfarbe mit Papier mischen, Anteil k Papier
        a = [int(h[i:i + 2], 16) for i in (1, 3, 5)]
        p = [int(papier[i:i + 2], 16) for i in (1, 3, 5)]
        return "#" + "".join(f"{round(x * (1 - k) + y * k):02X}" for x, y in zip(a, p))

    for basis in ("kaiwa-icon", "kaiwa-logo"):
        quelle = (ROOT / "design/logo" / f"{basis}.svg").read_text(encoding="utf-8")
        for th in themen["themen"]:
            n = len(th["farben"])
            hoehe = 446 / n
            baender = "".join(
                f'<rect x="-200" y="{-63 + i * hoehe:.2f}" width="720" height="{hoehe + 0.6:.2f}" fill="{hell(farbe)}"/>'
                for i, farbe in enumerate(th["farben"]))
            hintergrund = (f'<defs><clipPath id="taste"><rect width="320" height="320" rx="48"/></clipPath></defs>'
                           f'<g clip-path="url(#taste)"><g transform="rotate(-35 160 160)">{baender}</g></g>')
            text = quelle.replace('<rect width="320" height="320" rx="48" fill="#14171F"/>', hintergrund)
            zeilen = text.splitlines()
            ri = ei = 0
            for j, z in enumerate(zeilen):
                if z.startswith("<ellipse") and 'fill="none"' in z:
                    z = z.replace('stroke="#F1EFE9"', f'stroke="{th["ringe"][ri]}"')
                    z = re.sub(r'opacity="[0-9.]+"', 'opacity="1"', z)
                    z = re.sub(r'stroke-width="([0-9.]+)"', lambda m: f'stroke-width="{max(2.0, float(m.group(1)))}"', z)
                    ri += 1
                elif z.startswith("<g transform=") and 'fill-opacity="0.' in z:
                    # beide Echo-Kopien stehen in einer Zeile: jede bekommt ihre eigene Farbe und Deckkraft
                    deckkraft = ["0.16", "0.30"]
                    zaehler = [0]

                    def echo_ersetzen(m):
                        k = zaehler[0]
                        zaehler[0] += 1
                        return f'fill="{th["echo"][k]}" fill-opacity="{deckkraft[k]}"'
                    z = re.sub(r'fill="#F1EFE9" fill-opacity="0\.[0-9]+"', echo_ersetzen, z)
                zeilen[j] = z
            text = "\n".join(zeilen) + "\n"
            text = text.replace('fill="#F1EFE9"', f'fill="{tinte}"').replace('stroke="#F1EFE9"', f'stroke="{tinte}"')
            text = text.replace("<title>KAIWA</title>", f'<title>KAIWA, {th["pl"]} / {th["en"]}</title>')
            datei = ziel / f"{basis}-{th['id']}.svg"
            datei.write_text(text, encoding="utf-8", newline="\n")
            geschrieben.append(datei.name)
    return geschrieben


if __name__ == "__main__":
    for name in bauen():
        print(name)
