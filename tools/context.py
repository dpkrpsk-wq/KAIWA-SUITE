"""Mapa kontekstu, format kontekst-1: sprawdza plik mapy z agenta "KAIWA: mapa kontekstu".

Czesc pakietu KAIWA (Denis Pokropski, student, Uniwersytet Wroclawski, kontakt 285421@student.uwr.edu.pl). Wersja robocza, nie wydana.

Uzycie:  python tools/context.py sprawdz <mapa.xlsx>
Wynik 0 = mapa zgodna z regulami i niezmieniona od zapisu, 1 = bledy (lista na ekranie),
2 = brak pliku albo pakietu openpyxl.
Reguly miedzy znacznikami sa slowo w slowo te same co w 2-agents/copilot/map/INSTRUCTIONS.txt.
Test pakietu (tools/test_package.py) pilnuje, zeby sie nie rozjechaly.
"""
import argparse
import hashlib
import sys
import unicodedata
from pathlib import Path


def h(t):
    return hashlib.sha256(" ".join(unicodedata.normalize("NFC", t).split()).encode("utf-8")).hexdigest()


# --- reguły kontekst-1, początek
import re
POCHODZENIE = ("własne", "własne+asystent", "asystent", "sesja", "niejasne")
RODZAJE = ("jawne", "treściowe", "rozmowa")
HORYZONTY = ("krótki", "średni", "długi")
DATA = re.compile(r"\d{4}-\d\d-\d\d")
def _n(rows):
    rows = [["" if v is None else str(v).strip() for v in list(r)[:5]] for r in rows]
    return [tuple(r + [""] * (5 - len(r))) for r in rows if any(r)]
def bledy(tematy, polaczenia, cele):
    T, P, C = _n(tematy), _n(polaczenia), _n(cele)
    ids = [t[0] for t in T] + [c[0] for c in C]
    b = ["%s: identyfikator powtórzony" % x for x in sorted({i for i in ids if ids.count(i) > 1})]
    for i, temat, grupa, zrodlo, poch in T:
        if not re.fullmatch(r"[A-Z]{1,2}\d{1,3}", i):
            b.append("%s: identyfikator tematu ma postać A1" % i)
        if not temat or not zrodlo:
            b.append("%s: brak tematu albo źródła" % i)
        if poch not in POCHODZENIE:
            b.append("%s: pochodzenie spoza listy" % i)
    for i, horyzont, cel, termin, zrodlo in C:
        if not re.fullmatch(r"CEL\d{1,3}", i):
            b.append("%s: identyfikator celu ma postać CEL1" % i)
        if horyzont not in HORYZONTY:
            b.append("%s: horyzont spoza listy" % i)
        if not cel or (termin and not DATA.fullmatch(termin)):
            b.append("%s: brak celu albo termin nie w postaci RRRR-MM-DD" % i)
    pary = set()
    for od, do, rodzaj, uzas, potw in P:
        k = od + ">" + do
        if od not in ids or do not in ids or od == do:
            b.append("%s: nieznany temat albo cel, albo połączenie z samym sobą" % k)
        if rodzaj not in RODZAJE:
            b.append("%s: rodzaj spoza listy" % k)
        if rodzaj == "rozmowa" and not DATA.fullmatch(potw):
            b.append("%s: rozmowa wymaga daty RRRR-MM-DD" % k)
        if (min(od, do), max(od, do), rodzaj) in pary:
            b.append("%s: połączenie powtórzone" % k)
        pary.add((min(od, do), max(od, do), rodzaj))
    return b
def wiersze(tematy, polaczenia, cele):
    w = [("tematy", t[0], t) for t in _n(tematy)]
    w += [("połączenia", ">".join(p[:3]), p) for p in _n(polaczenia)]
    w += [("cele", c[0], c) for c in _n(cele)]
    return [(a, i, "␟".join(r)) for a, i, r in w]
# --- reguły kontekst-1, koniec


def sprawdz(plik):
    """Zwraca liste bledow: reguly kontekst-1 plus zgodnosc z arkuszem rejestr."""
    import openpyxl
    wb = openpyxl.load_workbook(plik)

    def arkusz(n):
        return list(wb[n].iter_rows(min_row=2, values_only=True)) if n in wb.sheetnames else []
    T, P, C = arkusz("tematy"), arkusz("połączenia"), arkusz("cele")
    b = bledy(T, P, C)
    reg = {(str(r[0]), str(r[1])): str(r[2]) for r in arkusz("rejestr") if r and r[0]}
    for a, i, tekst in wiersze(T, P, C):
        if reg.pop((a, i), None) != h(tekst):
            b.append("%s %s: zmieniony od zapisu albo nowy" % (a, i))
    b += ["%s %s: usunięty od zapisu" % k for k in sorted(reg)]
    return b


def main(argv=None):
    ap = argparse.ArgumentParser(description="Mapa kontekstu (kontekst-1): sprawdzenie pliku")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sprawdz").add_argument("plik")
    a = ap.parse_args(argv)
    if not Path(a.plik).is_file():
        print("brak pliku: %s" % a.plik)
        return 2
    try:
        import openpyxl  # noqa: F401
    except ImportError:
        print("brak pakietu openpyxl: pip install openpyxl")
        return 2
    b = sprawdz(a.plik)
    print("\n".join(b) if b else "MAPA OK")
    return 1 if b else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
