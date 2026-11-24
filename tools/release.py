"""Release-ZIPs fuer KAIWA SUITE: ein ZIP je Anbieter, dazu die Copilot-Pakete Skill und Plugin.

Teil des Pakets KAIWA (Denis Pokropski, student, Uniwersytet Wroclawski, kontakt 285421@student.uwr.edu.pl). Wersja robocza, nie wydana.

Der Dateisatz steht in release/sets.json (einzige Quelle, auch fuer die Paketseite). Gebaut wird aus dem Git-Baum eines
Commits (Vorgabe HEAD), so nimmt ein Release nie unversionierte Dateien mit. Gleicher Commit ergibt gleiche Bytes.

Aufruf (aus dem Repo, Python 3.8 oder neuer, nur Standardbibliothek):
  python -I tools/release.py bauen [--stand <Commit>] [--ausgabe dist/release]   baut ZIPs, SHA256SUMS.txt, release-manifest.json
  python -I tools/release.py pruefen [--stand <Commit>]                          baut zweimal und vergleicht, prueft Inhalt
  python -I tools/release.py bauen --arbeitsbaum                                 liest die Dateien von der Platte (fuer Tests)
Ausgang 0 = in Ordnung, 1 = Befund, 2 = Aufruf oder Umgebung falsch.
"""
import argparse
import hashlib
import io
import json
import subprocess
import sys
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANBIETER = ("copilot", "gemini", "chatgpt", "claude", "any")
FEST = 1767225600  # 2026-01-01 00:00:00 UTC, Zeitstempel im Arbeitsbaum-Modus
PLATZHALTER = "⟨commit⟩"
STUMM = ("__pycache__/", ".pyc")


class Quelle:
    """Dateien eines Git-Commits oder des Arbeitsbaums."""

    def __init__(self, stand=None):
        self.stand = stand
        if stand:
            self.paths = self._git("ls-tree", "-r", "--name-only", stand).decode("utf-8").split("\n")
            self.paths = [p for p in self.paths if p]
            self.zeit = int(self._git("show", "-s", "--format=%ct", stand).decode().strip())
            self.hash = self._git("rev-parse", "--short=7", stand).decode().strip()
        else:
            pfade = []
            for p in sorted(ROOT.rglob("*")):
                if not p.is_file():
                    continue
                rel = p.relative_to(ROOT).as_posix()
                if rel.startswith((".git/", "dist/")) or any(s in rel for s in STUMM):
                    continue
                pfade.append(rel)
            self.paths = pfade
            self.zeit = FEST
            self.hash = "arbeitsbaum"
        self.set = set(self.paths)

    @staticmethod
    def _git(*args):
        r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
        if r.returncode != 0:
            raise RuntimeError("git " + " ".join(args) + ": " + r.stderr.decode("utf-8", "replace").strip())
        return r.stdout

    def lies(self, pfad):
        if self.stand:
            return self._git("cat-file", "blob", self.stand + ":" + pfad)
        return (ROOT / pfad).read_bytes()

    def unter(self, praefix):
        return sorted(p for p in self.paths if p.startswith(praefix) and not any(s in p for s in STUMM))


def zeitstempel(sekunden):
    t = time.gmtime(max(sekunden, 315532800))  # ZIP kennt nichts vor 1980
    return (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec - t.tm_sec % 2)


def sets(q):
    return json.loads(q.lies("release/sets.json").decode("utf-8"))


def version(q):
    return json.loads(q.lies("product.json").decode("utf-8"))["version"]


def dateisatz(q, s, anbieter):
    """Pfade eines Anbieter-ZIP: immer + Eintraege des Anbieters + Eintraege ohne Anbieter, ohne Ausschluss."""
    aus = set(s.get("ausschluss", []))
    out = set()
    for a in s["immer"]:
        if a.endswith("/"):
            out.update(q.unter(a))
        elif a in q.set:
            out.add(a)
    for e in s["eintraege"]:
        if e["v"] in (anbieter, "any"):
            if e.get("dir"):
                out.update(q.unter(e["p"]))
            elif e["p"] in q.set:
                out.add(e["p"])
    return sorted(out - aus)


def contents(name, files, ver, stand):
    return "\n".join([
        "# KAIWA SUITE: pakiet %s / package for %s" % (name, name), "",
        "Ten plik ZIP zawiera tylko pliki dla dostawcy %s, pliki bez dostawcy, licencje i skrypty. README.md opisuje caly pakiet, foldery innych dostawcow sa w repozytorium https://github.com/dpkrpsk-wq/KAIWA-SUITE." % name, "",
        "This ZIP holds only the files for %s, the files without vendor, the licences and the scripts. README.md describes the whole package, the folders of the other vendors are in the repository https://github.com/dpkrpsk-wq/KAIWA-SUITE." % name, "",
        "Wersja / version: %s, commit %s." % (ver, stand), "",
        "Testy / tests: python tools/test_package.py (pomija czesci, ktorych nie ma w tym pakiecie / skips parts not in this package).", "",
        "tools/pdf.py i tools/logo_status.py potrzebuja plikow z design/, ktore sa tylko w pelnym pakiecie. / tools/pdf.py and tools/logo_status.py need files from design/ that are only in the full package.", "",
        "Liczba plikow bez tego pliku / files without this file: %d" % len(files), "",
        *["- `" + p + "`" for p in files], ""])


def zip_bytes(eintraege, zeit):
    """eintraege: Liste (Name im ZIP, Bytes), schon in Reihenfolge. Feste Zeit, feste Attribute."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in eintraege:
            zi = zipfile.ZipInfo(name, zeitstempel(zeit))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o644 << 16
            zi.create_system = 3
            z.writestr(zi, data)
    return buf.getvalue()


def anbieter_zip(q, s, anbieter, ver):
    files = dateisatz(q, s, anbieter)
    wurzel = "KAIWA-SUITE-%s/" % anbieter
    eintr = []
    for p in files:
        data = q.lies(p)
        if p == "1-start/first-contact.html" and PLATZHALTER.encode("utf-8") in data:
            data = data.replace(PLATZHALTER.encode("utf-8"), q.hash.encode("utf-8"))
        eintr.append((wurzel + p, data))
    name = {"copilot": "Microsoft 365 Copilot", "gemini": "Google Gemini", "chatgpt": "ChatGPT", "claude": "Claude", "any": "bez dostawcy / any"}[anbieter]
    eintr.append((wurzel + "ZIP-CONTENTS.md", contents(name, files, ver, q.hash).encode("utf-8")))
    eintr.sort(key=lambda e: e[0])
    return zip_bytes(eintr, q.zeit), len(files) + 1


def paket_zip(q, paket):
    eintr = []
    for ziel, quelle in paket["dateien"]:
        if isinstance(quelle, dict):
            kopf = json.loads(q.lies(quelle["kopf"]).decode("utf-8"))[quelle["name"]]
            body = q.lies(quelle["koerper"]).decode("utf-8")
            text = "---\nname: %s\ndescription: %s\n---\n\n%s" % (kopf["name"], json.dumps(kopf["description"], ensure_ascii=False), body)
            data = text.encode("utf-8")
        else:
            data = q.lies(quelle)
        eintr.append((ziel, data))
    eintr.sort(key=lambda e: e[0])
    return zip_bytes(eintr, q.zeit), len(eintr)


def baue(q, ausgabe):
    s = sets(q)
    ver = version(q)
    ausgabe.mkdir(parents=True, exist_ok=True)
    dateien = []
    for a in ANBIETER:
        daten, n = anbieter_zip(q, s, a, ver)
        dateien.append(("KAIWA-SUITE-%s" % a, daten, n))
    for key in ("copilot-skill", "copilot-plugin"):
        daten, n = paket_zip(q, s["pakete"][key])
        dateien.append((s["pakete"][key]["zip"], daten, n))
    summen, manifest = [], []
    for basis, daten, n in dateien:
        for name in ("%s-%s.zip" % (basis, ver), "%s.zip" % basis):
            (ausgabe / name).write_bytes(daten)
            h = hashlib.sha256(daten).hexdigest()
            summen.append("%s  %s" % (h, name))
            manifest.append({"name": name, "bytes": len(daten), "sha256": h, "dateien": n})
    (ausgabe / "SHA256SUMS.txt").write_text("\n".join(summen) + "\n", encoding="utf-8", newline="\n")
    m = {"produkt": "KAIWA SUITE", "version": ver, "commit": q.hash, "stand": "robocza / draft", "dateien": manifest}
    (ausgabe / "release-manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    return m


def pruefe(q, ausgabe):
    """Baut zweimal (gleiche Bytes), vergleicht jeden ZIP-Inhalt mit der Quelle und die Zahlen mit dem Manifest."""
    befunde = []
    s = sets(q)
    ver = version(q)
    zweit = ausgabe.parent / (ausgabe.name + "-2")
    m1 = baue(q, ausgabe)
    m2 = baue(q, zweit)
    if m1 != m2:
        befunde.append("zwei Bauten ergeben verschiedene Pruefsummen")
    for e in m1["dateien"]:
        z = zipfile.ZipFile(ausgabe / e["name"])
        namen = z.namelist()
        if len(namen) != e["dateien"]:
            befunde.append("%s: %d Eintraege, Manifest nennt %d" % (e["name"], len(namen), e["dateien"]))
        if len(set(namen)) != len(namen):
            befunde.append(e["name"] + ": doppelter Eintrag")
        if z.testzip() is not None:
            befunde.append(e["name"] + ": beschaedigt")
    for a in ANBIETER:
        z = zipfile.ZipFile(ausgabe / ("KAIWA-SUITE-%s-%s.zip" % (a, ver)))
        erwartet = set("KAIWA-SUITE-%s/%s" % (a, p) for p in dateisatz(q, s, a)) | {"KAIWA-SUITE-%s/ZIP-CONTENTS.md" % a}
        if set(z.namelist()) != erwartet:
            befunde.append("KAIWA-SUITE-%s: Dateimenge weicht vom Satz ab: %s" % (a, sorted(set(z.namelist()) ^ erwartet)[:5]))
        for n in z.namelist():
            p = n.split("/", 1)[1]
            if p != "ZIP-CONTENTS.md" and p != "1-start/first-contact.html" and z.read(n) != q.lies(p):
                befunde.append("%s: %s weicht von der Quelle ab" % (a, p))
    return befunde, m1


def main(argv=None):
    ap = argparse.ArgumentParser(description="KAIWA SUITE: Release-ZIPs bauen und pruefen")
    ap.add_argument("befehl", choices=("bauen", "pruefen"))
    ap.add_argument("--stand", default="HEAD", help="Commit, aus dem gebaut wird (Vorgabe HEAD)")
    ap.add_argument("--arbeitsbaum", action="store_true", help="Dateien von der Platte lesen statt aus Git")
    ap.add_argument("--ausgabe", default="dist/release")
    a = ap.parse_args(argv)
    ausgabe = Path(a.ausgabe)
    if not ausgabe.is_absolute():
        ausgabe = ROOT / ausgabe
    try:
        q = Quelle(None if a.arbeitsbaum else a.stand)
        if a.befehl == "bauen":
            m = baue(q, ausgabe)
            for e in m["dateien"]:
                print("%-52s %9d Byte %3d Dateien  %s" % (e["name"], e["bytes"], e["dateien"], e["sha256"][:12]))
            print("Version %s, Commit %s, Ausgabe %s" % (m["version"], m["commit"], ausgabe))
            return 0
        befunde, m = pruefe(q, ausgabe)
        for b in befunde:
            print("BEFUND:", b)
        print("%d Befunde, %d ZIP-Dateien, Version %s, Commit %s" % (len(befunde), len(m["dateien"]), m["version"], m["commit"]))
        return 1 if befunde else 0
    except (RuntimeError, OSError, KeyError, ValueError) as e:
        print("Fehler:", e)
        return 2


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
