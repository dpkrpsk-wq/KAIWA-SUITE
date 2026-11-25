"""Builds the KAIWA ChatGPT plugin archive from the package files. Standard library only.

The plugin texts written for the plugin are in 2-agents/chatgpt/plugin/ (plugin.json, .codex-plugin/plugin.json,
README.md, skills/*/SKILL.md). Everything under skills/*/references/ is an unchanged copy of a package file at its
package path: the module's INSTRUCTIONS.txt, the files of the module's files.txt and of the skill's extra.txt.
Same package state, same ZIP bytes (sorted entries, fixed date, fixed mode).
Layout after the plugin ChatGPT itself exported on 24.11.2026 (plugin.json, .codex-plugin/plugin.json, skills/).

Run:  python tools/chatgpt_plugin.py                  writes dist/KAIWA-SUITE-chatgpt-plugin.zip
      python tools/chatgpt_plugin.py --check PLIK.zip  compares an archive with the package
"""
import argparse
import hashlib
import io
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "2-agents/chatgpt/plugin"
OUT = ROOT / "dist/KAIWA-SUITE-chatgpt-plugin.zip"
# skill name in the plugin -> module folder under 2-agents/chatgpt
SKILLS = {
    "artifact-analysis": "analysis",
    "context-map": "map",
    "research-sources": "sources",
    "stream-of-consciousness": "stream",
}
PLUGIN_FILES = ("plugin.json", ".codex-plugin/plugin.json", "README.md")
LICENCES = ("LICENSE", "LICENSE-COMMERCIAL.md", "DISCLOSURE.md", "method/prompts/LICENSE.md", "method/protocols/LICENSE.md")
# Plugin icon (X1 25.11.2026): the agent icon of the design system KAIWA SUITE, dark tile, K in papier, square in signal
ASSETS = {
    "assets/kaiwa-icon-512.png": "design/logo/kaiwa-icon-512.png",
    "assets/kaiwa-icon-192.png": "design/logo/kaiwa-icon-192.png",
}
DATE = (1980, 1, 1, 0, 0, 0)


def _list(path):
    if not path.is_file():
        return []
    return [l.strip() for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def references(skill):
    """Package paths copied into skills/<skill>/references/, without duplicates, in a fixed order."""
    module = SKILLS[skill]
    paths = ["2-agents/chatgpt/%s/INSTRUCTIONS.txt" % module]
    paths += _list(ROOT / "2-agents/chatgpt" / module / "files.txt")
    paths += _list(PLUGIN / "skills" / skill / "extra.txt")
    return list(dict.fromkeys(paths))


def entries():
    """Archive path -> package file. Raises if a package file is missing."""
    out = {}
    for name in PLUGIN_FILES:
        out[name] = PLUGIN / name
    for name in LICENCES:
        out[name] = ROOT / name
    for name, src in ASSETS.items():
        out[name] = ROOT / src
    for skill in SKILLS:
        out["skills/%s/SKILL.md" % skill] = PLUGIN / "skills" / skill / "SKILL.md"
        for p in references(skill):
            out["skills/%s/references/%s" % (skill, p)] = ROOT / p
    missing = [str(f.relative_to(ROOT)) for f in out.values() if not f.is_file()]
    if missing:
        raise FileNotFoundError("missing package files: " + ", ".join(missing))
    return dict(sorted(out.items()))


def build():
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, src in entries().items():
            info = zipfile.ZipInfo(name, DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            info.create_system = 3  # Unix, auch unter Windows: ChatGPT lehnte "Neue Version hochladen" mit 0 ab (Test X1 25.11.2026), mit 3 nahm es die Datei an
            z.writestr(info, src.read_bytes(), compresslevel=9)
    return buf.getvalue()


def check(path):
    """Compares an archive entry by entry with the package. Returns (same, different, missing, extra)."""
    want = {n: f.read_bytes() for n, f in entries().items()}
    with zipfile.ZipFile(path) as z:
        have = {i.filename: z.read(i) for i in z.infolist() if not i.is_dir()}
    same = sorted(n for n in want if n in have and have[n] == want[n])
    different = sorted(n for n in want if n in have and have[n] != want[n])
    missing = sorted(n for n in want if n not in have)
    extra = sorted(n for n in have if n not in want)
    return same, different, missing, extra


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", metavar="ZIP")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args(argv)
    if a.check:
        same, different, missing, extra = check(a.check)
        print("identical: %d" % len(same))
        for label, items in (("different", different), ("missing", missing), ("extra", extra)):
            print("%s: %d" % (label, len(items)))
            for n in items:
                print("  " + n)
        return 0 if not (different or missing or extra) else 1
    data = build()
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print("%s  %d files  sha256 %s" % (out, len(entries()), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
