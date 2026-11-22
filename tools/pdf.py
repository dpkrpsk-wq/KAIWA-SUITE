"""PDF je Dokument im Gestaltungssystem KAIWA SUITE.

Markdown wird zu HTML mit Dokumentkopf, Entwurfsmarke und Fußzeile (Komponenten
Dokumentkopf und Fusszeile aus design/design-system), danach druckt ein Chromium-Browser
(Edge oder Chrome, headless) das HTML als PDF.

Aufruf: python tools/pdf.py [--browser <Pfad>] [--ziel dist/pdf] [Datei.md ...]
Ohne Dateien: alle Dokumente des Pakets (DOKUMENTE unten).
Benötigt: Python-Paket markdown, einen Chromium-Browser ab Version 131 (Seitenränder mit Zähler).
Name, Nummer, Version und Stand kommen aus product.json, der Commit aus git (7 Zeichen).
Bei Änderungen, die nicht committet sind, bricht das Skript ab: ein Export trägt einen Commit.
Die PDFs gehören nicht ins Repo (dist/ steht in .gitignore), sie gehen als Anlage zum Release.
"""
import argparse
import html
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
DOKUMENTE = ["README.md", "1-start/*.md", "2-agents/copilot/*/AGENT.md", "2-agents/gemini/*.md",
             "2-agents/gemini/*/SKILL.md", "2-agents/chatgpt/*.md", "2-agents/chatgpt/*/PROJECT.md", "3-templates/*.md", "DISCLOSURE.md", "4-without-ai/*.md", "design/video-prompt.*.md"]
BROWSER = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
           r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
           r"C:\Program Files\Google\Chrome\Application\chrome.exe",
           "microsoft-edge", "google-chrome", "chromium", "chromium-browser"]


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout.strip()


def browser(angabe):
    for b in ([angabe] if angabe else BROWSER):
        p = shutil.which(b) or (b if Path(b).is_file() else None)
        if p:
            return p
    sys.exit("Kein Chromium-Browser gefunden. Pfad mit --browser angeben.")


def css():
    tokens = (ROOT / "design/design-system/tokens.css").read_text(encoding="utf-8")
    schrift = (ROOT / "design/fonts/fonts.css").read_text(encoding="utf-8")
    schrift = schrift.replace('url("', 'url("' + (ROOT / "design/fonts").as_uri() + "/")
    return schrift + tokens + """
@page { size: A4; margin: 18mm 16mm 22mm 16mm;
  @bottom-left { content: "__FUSS__"; }
  @bottom-right { content: "strona " counter(page) " z " counter(pages) " / page " counter(page) " of " counter(pages); }
}
@page { @bottom-left { font: 400 8pt/1.4 "Space Grotesk", Arial, sans-serif; color: #4a4f5a; border-top: 2pt solid #14171f; padding-top: 2mm; }
        @bottom-right { font: 400 8pt/1.4 "Space Grotesk", Arial, sans-serif; color: #4a4f5a; border-top: 2pt solid #14171f; padding-top: 2mm; } }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; background: var(--flaeche); color: var(--text); font: 400 10.5pt/1.55 var(--font-text); }
.kopf { position: relative; display: flex; align-items: center; gap: var(--space-6); background: var(--tinte); color: var(--papier);
  padding: 14px 18px; box-shadow: var(--schatten-hart); overflow: hidden; margin-right: 6px; }
.kopf img { width: 64px; height: 64px; }
.kopf .marke { font: 700 28px/28px var(--font-warp); letter-spacing: -1px; text-transform: uppercase; }
.kopf .baender { position: absolute; right: 0; top: 0; bottom: 0; width: 42%;
  background: repeating-linear-gradient(-55deg, var(--signal) 0 12px, var(--tinte) 12px 24px); }
.kopf .aufkleber { position: absolute; right: 22px; top: 50%; transform: translateY(-50%) rotate(-3deg); background: var(--signal);
  color: var(--tinte); border: 3px solid var(--tinte); padding: 4px 10px; font: 500 9pt/1.3 var(--font-kopf); letter-spacing: .06em;
  text-transform: uppercase; }
.felder { display: flex; gap: var(--space-8); border-top: 6px solid var(--text); margin: var(--space-4) 0 var(--space-6); padding-top: var(--space-2); }
.felder div { display: flex; flex-direction: column; }
.etikett { font: 500 7.5pt/1.4 var(--font-kopf); letter-spacing: .06em; text-transform: uppercase; }
.etikett span { color: var(--text-gedaempft); }
.wert { font: 700 16pt/1.2 var(--font-kopf); font-variant-numeric: tabular-nums; }
.wert.entwurf { color: var(--entwurf); }
main h1 { font: 700 20pt/1.2 var(--font-kopf); margin: 0 0 var(--space-4); }
main h2 { font: 700 14pt/1.25 var(--font-kopf); margin: var(--space-6) 0 var(--space-2); border-bottom: 3px solid var(--text); padding-bottom: 2px; }
main h3 { font: 500 11.5pt/1.3 var(--font-kopf); margin: var(--space-4) 0 var(--space-2); }
main a { color: var(--text); }
main code { font-family: Consolas, "Courier New", monospace; font-size: 9pt; background: var(--flaeche-hinweis); padding: 0 3px; }
main pre { background: var(--flaeche-hinweis); border: 1px solid var(--linie); padding: var(--space-3); white-space: pre-wrap; font-size: 8.5pt; }
main pre code { background: none; padding: 0; }
main table { border-collapse: collapse; width: 100%; margin: var(--space-3) 0; font-size: 9pt; box-shadow: var(--schatten-hart); }
main th { background: var(--tinte); color: var(--papier); text-align: left; padding: 4px 8px; border-bottom: 3px solid var(--signal);
  font: 500 8pt/1.3 var(--font-kopf); letter-spacing: .04em; }
main td { padding: 4px 8px; border-bottom: 1px solid var(--linie); vertical-align: top; font-variant-numeric: tabular-nums; }
main img { max-width: 96px; }
main blockquote { margin: var(--space-3) 0; padding: var(--space-3) var(--space-4); background: var(--flaeche-hinweis); border: 1px solid var(--linie); }
"""


def seite(titel, inhalt, produkt, commit):
    entwurf = produkt["version"].startswith("0.")
    fuss = f'KAIWA · {produkt["nummer"]} · wersja {produkt["version"]} · commit {commit}'
    icon = (ROOT / "design/design-system/assets/Logos/kaiwa-icon-hell.svg").as_uri()
    marke = '<div class="baender"></div><div class="aufkleber">wersja robocza / draft</div>' if entwurf else ""
    stand = html.escape(produkt.get("stand", ""))
    return f"""<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>{html.escape(titel)}</title>
<style>{css().replace("__FUSS__", fuss)}</style></head><body>
<header class="kopf"><img src="{icon}" alt="KAIWA"><div class="marke">{html.escape(produkt["name"])}<br>{html.escape(produkt.get("suite", ""))}</div>{marke}</header>
<section class="felder">
<div><span class="etikett">Numer produktu <span>/ Product no.</span></span><span class="wert">{html.escape(produkt["nummer"])}</span></div>
<div><span class="etikett">Wersja <span>/ Version</span></span><span class="wert">{html.escape(produkt["version"])}</span></div>
<div><span class="etikett">Stan <span>/ Status</span></span><span class="wert{' entwurf' if entwurf else ''}">{stand}</span></div>
</section>
<main>{inhalt}</main></body></html>"""


def dokumente(angaben):
    if angaben:
        return [Path(a).resolve() for a in angaben]
    gefunden = []
    for muster in DOKUMENTE:
        gefunden += sorted(ROOT.glob(muster))
    return [p for p in gefunden if p.is_file()]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dateien", nargs="*")
    ap.add_argument("--browser")
    ap.add_argument("--ziel", default=str(ROOT / "dist" / "pdf"))
    a = ap.parse_args()
    if git("status", "--porcelain", "--untracked-files=no"):
        sys.exit("Es gibt Änderungen, die nicht committet sind. Ein Export trägt einen Commit, bitte zuerst committen.")
    commit = git("rev-parse", "--short=7", "HEAD")
    produkt = json.loads((ROOT / "product.json").read_text(encoding="utf-8"))
    exe = browser(a.browser)
    ziel = Path(a.ziel)
    ziel.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for doc in dokumente(a.dateien):
            rel = doc.relative_to(ROOT).as_posix()
            text = doc.read_text(encoding="utf-8")
            inhalt = markdown.markdown(text, extensions=["tables", "fenced_code"])
            basis = doc.parent.as_uri() + "/"
            inhalt = inhalt.replace('src="', 'src="' + basis).replace('src="' + basis + "file:", 'src="file:')
            datei = Path(tmp) / (rel.replace("/", "__") + ".html")
            datei.write_text(seite(rel, inhalt, produkt, commit), encoding="utf-8")
            pdf = ziel / (rel.replace("/", "__").removesuffix(".md") + ".pdf")
            subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                            f"--print-to-pdf={pdf}", datei.as_uri()], capture_output=True, timeout=120)
            print(("OK   " if pdf.is_file() else "FEHLT") + f" {pdf.relative_to(ROOT) if pdf.is_relative_to(ROOT) else pdf}")


if __name__ == "__main__":
    main()
