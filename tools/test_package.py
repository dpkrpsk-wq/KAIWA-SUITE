"""Tests for the KAIWA package. Standard library plus openpyxl (only for the Copilot file test).

Checks: the Copilot instructions fit the 8,000 character limit of Agent Builder, both code blocks in them run,
the Excel file they write carries the same hashes and ids as dictation_ledger.py computes from a journal, the ledger
commands work, and the package texts contain no semicolon and no dash outside code.
Context map (2-agents/copilot/map, tools/context.py): the agent's rule block is the same text as in context.py, its code
blocks run, a written map passes the local check, a changed cell is found, and a map with errors is not saved.
Run:  python tools/test_package.py
"""
import contextlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import dictation_ledger as L  # noqa: E402

INSTRUCTIONS = ROOT / "2-agents/copilot" / "stream" / "INSTRUCTIONS.txt"
# Ein ZIP je Anbieter von der Paketseite ist ein Teilpaket: es traegt ZIP-CONTENTS.md und enthaelt nur die Ordner eines Anbieters.
# Dort werden Tests fuer fehlende Teile uebersprungen, im vollen Repo bleibt jeder Test streng (Review 22.11.2026, P0).
TEILPAKET = (ROOT / "ZIP-CONTENTS.md").exists()


def fehlt(name):
    return TEILPAKET and not (ROOT / name).exists()


def braucht(*pfade):
    weg = [p for p in pfade if fehlt(p)]
    return unittest.skipIf(bool(weg), "nie w tym pakiecie / not in this package: " + ", ".join(weg))
CODE = re.compile(r"```python\n(.*?)```", re.S)
VERB = ["Freiheit ist   die Bedingung der Kritik.", "Wolność jest warunkiem krytyki.", "Freiheit ist die Bedingung der Kritik."]


def code_blocks():
    return CODE.findall(INSTRUCTIONS.read_text(encoding="utf-8"))


@braucht("2-agents/copilot")
class InstructionsTest(unittest.TestCase):
    def test_limit(self):
        self.assertLessEqual(len(INSTRUCTIONS.read_text(encoding="utf-8")), 8000)

    def test_probe_block(self):
        out = subprocess.run([sys.executable, "-I", "-c", code_blocks()[0]], capture_output=True, text=True)
        self.assertEqual(out.stdout.strip(), "OK")

    def test_end_block_matches_ledger(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl missing")
        entries = "ENTRIES = [\n" + "".join(
            "    (%d, 'verbatim', 't', 'p', %r, 'prov', False),\n" % (i + 1, v) for i, v in enumerate(VERB)) + "]\n"
        code = code_blocks()[1].replace("ENTRIES = [\n    # (number, form \"verbatim\" or \"addendum\", title, paraphrase, verbatim, provenance, assistant_content True/False)\n]\n", entries)
        self.assertIn("'Wolność", code)
        with tempfile.TemporaryDirectory() as tmp:
            out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=tmp)
            self.assertEqual(out.returncode, 0, out.stderr)
            name = out.stdout.split()[0]
            wb = openpyxl.load_workbook(os.path.join(tmp, name))
            reg = list(wb["register"].iter_rows(values_only=True))[1:]
            day = reg[0][1]
            journal = "".join("**t (x)**\n\nVerbatim (dictated): “%s”\n\n" % v for v in VERB)
            found, _ = L.read_day(day, journal, "journal/%s.md" % day)
            # read_day numbers repeats only across a journal, so apply the same rule here
            seen = {}
            for c in found:
                seen[c["id"]] = seen.get(c["id"], 0) + 1
                if seen[c["id"]] > 1:
                    c["id"] = "%s-%d" % (c["id"], seen[c["id"]])
            self.assertEqual([r[4] for r in reg], [c["sha256"] for c in found])
            self.assertEqual([r[0] for r in reg], [c["id"] for c in found])
            self.assertTrue(reg[2][0].endswith("-2"))   # same sentence after whitespace collapse gets a repeat number
            self.assertEqual(list(wb["entries"].iter_rows(values_only=True))[2][4], VERB[1])


class LedgerTest(unittest.TestCase):
    def test_scan_verify_probe(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(L.main(["init", tmp]), 0)
            day = Path(tmp, "journal", "2026-11-05.md")
            day.write_text("### Dictation Stream of Consciousness 08:00, 10 min, goal essay-x, session abc12345\n\n"
                           "**Freedom (08:01)**\n\nVerbatim (dictated): “Freedom first.”\n\n"
                           "Addendum (08:05)\n\nVerbatim (dictated): “And always.”\n\n"
                           "**Wolność (08:07)**\n\nDosłownie (dyktowane): „Wolność jest warunkiem.”\n\n"
                           "**Offen (08:09)**\n\nWortlaut (diktiert): „ohne Schluss\n", encoding="utf-8")
            self.assertEqual(L.main(["scan", tmp, "--now", "2026-11-05T08:10:00Z"]), 0)
            recs = L.read_ledger(tmp)
            self.assertEqual([(r["form"], r["time"]) for r in recs],
                             [("verbatim", "08:01"), ("addendum", "08:05"), ("verbatim", "08:07")])
            self.assertEqual((recs[0]["mode"], recs[0]["minutes"], recs[0]["goal"], recs[0]["session"]),
                             ("stream-of-consciousness", 10, "essay-x", "abc12345"))
            self.assertNotIn("Freedom", Path(tmp, "ledger.jsonl").read_text(encoding="utf-8"))
            self.assertEqual(L.main(["scan", tmp, "--now", "2026-11-05T08:11:00Z"]), 0)
            self.assertEqual(len(L.read_ledger(tmp)), 3)          # nothing added twice
            self.assertEqual(L.main(["verify", tmp]), 0)
            day.write_text(day.read_text(encoding="utf-8").replace("And always.", "And sometimes."), encoding="utf-8")
            self.assertEqual(L.main(["verify", tmp]), 1)
            self.assertEqual(L.main(["probe"]), 0)

    def test_mode_names_old_and_new(self):
        """Headings before 2026-11-08 (stream, strumień, Strom) read as the same mode as the full name."""
        for heading, mode in (("### Dictation Stream of Consciousness 08:00", "stream-of-consciousness"),
                              ("### Dyktowanie strumień świadomości 08:00", "stream-of-consciousness"),
                              ("### Dictation stream 08:00", "stream-of-consciousness"),
                              ("### Dyktowanie strumień 08:00", "stream-of-consciousness"),
                              ("### Diktat-Strom 08:00, Sitzung abc12345", "stream-of-consciousness"),
                              ("### Dictation sprint 08:00, 10 min", "sprint")):
            found, _ = L.read_day("2026-11-05", heading + "\n\n**a (08:01)**\n\nVerbatim (dictated): \"x\"\n", "d.md")
            self.assertEqual((found[0]["mode"], found[0]["session_start"]), (mode, "08:00"), heading)

    def test_same_bytes(self):
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                L.main(["init", tmp])
                Path(tmp, "journal", "2026-11-05.md").write_text("**a (09:00)**\nVerbatim (dictated): \"x y\"\n", encoding="utf-8")
                L.main(["scan", tmp, "--now", "2026-11-05T09:00:00Z"])
                outs.append(Path(tmp, "ledger.jsonl").read_bytes())
        self.assertEqual(outs[0], outs[1])


MAPA = ROOT / "2-agents/copilot" / "map" / "INSTRUCTIONS.txt"
RULES = re.compile(r"# --- reguły kontekst-1, początek\n.*?# --- reguły kontekst-1, koniec\n", re.S)
TEMATY_F = [("A1", "Pisanie jako myślenie", "Metoda", "dictation-2026-11-05-0810.xlsx 1", "własne"),
            ("A2", "Ślad pochodzenia myśli", "Metoda", "dictation-2026-11-05-0810.xlsx 2", "własne+asystent"),
            ("B1", "Granice modelu", "AI", "propozycja asystenta", "asystent")]
POL_F = [("A1", "A2", "jawne", "wpis 2 nazywa związek", ""),
         ("A2", "B1", "rozmowa", "potwierdzone w rozmowie", "2026-11-05"),
         ("A1", "CEL1", "treściowe", "pisanie służy esejowi", "")]
CELE_F = [("CEL1", "krótki", "Esej na zajęcia", "2026-11-20", "rozmowa 05.11.")]
UTF8 = dict(os.environ, PYTHONIOENCODING="utf-8")


def mapa_blocks():
    return CODE.findall(MAPA.read_text(encoding="utf-8"))


def fill(block, tematy, pol, cele):
    for name, rows in (("TEMATY", tematy), ("POLACZENIA", pol), ("CELE", cele)):
        block = re.sub(r"%s = \[\n.*?\n\]" % name, lambda m, n=name, r=rows: "%s = %r" % (n, r), block, count=1, flags=re.S)
    return block


def run(code, cwd=None):
    return subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, encoding="utf-8",
                          env=UTF8, cwd=cwd)


@braucht("2-agents/copilot")
class MapaTest(unittest.TestCase):
    def test_limit(self):
        self.assertLessEqual(len(MAPA.read_text(encoding="utf-8")), 8000)

    def test_rules_same_as_local_tool(self):
        a = RULES.search(MAPA.read_text(encoding="utf-8")).group(0)
        b = RULES.search((HERE / "context.py").read_text(encoding="utf-8")).group(0)
        self.assertEqual(a, b)

    def test_probe(self):
        out = run(mapa_blocks()[0])
        self.assertEqual(out.stdout.strip(), "OK", out.stderr)

    def test_rules(self):
        import context as K
        T = TEMATY_F + [("A1", "dubel", "", "s", "własne"), ("a9", "x", "", "s", "moje"), (None, None, None)]
        P = [("A1", "A2", "jawne", "", ""), ("A2", "A1", "jawne", "", ""), ("A1", "A1", "jawne", "", ""),
             ("A1", "Z9", "inne", "", ""), ("A2", "B1", "rozmowa", "", "05.11.2026")]
        C = [("CEL1", "pilny", "", "11.11.2026", "")]
        self.assertEqual(sorted(K.bledy(T, P, C)), sorted([
            "A1: identyfikator powtórzony",
            "a9: identyfikator tematu ma postać A1",
            "a9: pochodzenie spoza listy",
            "CEL1: horyzont spoza listy",
            "CEL1: brak celu albo termin nie w postaci RRRR-MM-DD",
            "A2>A1: połączenie powtórzone",
            "A1>A1: nieznany temat albo cel, albo połączenie z samym sobą",
            "A1>Z9: nieznany temat albo cel, albo połączenie z samym sobą",
            "A1>Z9: rodzaj spoza listy",
            "A2>B1: rozmowa wymaga daty RRRR-MM-DD",
        ]))
        self.assertEqual(K.bledy(TEMATY_F, POL_F, CELE_F), [])

    def test_write_verify_tamper(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl missing")
        import context as K
        start, write = mapa_blocks()[:2]
        # Pruefcode liegt seit 22.11.2026 in sprawdz-mape.md (Laengenreserve der Anweisung, Befund V1)
        verify = CODE.findall((MAPA.parent / "sprawdz-mape.md").read_text(encoding="utf-8"))[0]
        with tempfile.TemporaryDirectory() as tmp:
            out = run(start + "\n" + fill(write, TEMATY_F, POL_F, CELE_F), tmp)
            self.assertEqual(out.returncode, 0, out.stderr)
            name = out.stdout.strip().splitlines()[-1].split()[0]
            path = os.path.join(tmp, name)
            self.assertTrue(name.startswith("mapa-") and name.endswith(".xlsx"), out.stdout)
            self.assertEqual(K.sprawdz(path), [])
            check = start + "\n" + verify.replace('PLIK = "mapa.xlsx"', "PLIK = %r" % path)
            self.assertEqual(run(check, tmp).stdout.strip().splitlines()[-1], "MAPA OK")
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(K.main(["sprawdz", path]), 0)
            wb = openpyxl.load_workbook(path)
            wb["tematy"]["B3"] = "Ślad pochodzenia"   # row 3 is topic A2
            wb.save(path)
            self.assertEqual(K.sprawdz(path), ["tematy A2: zmieniony od zapisu albo nowy"])
            self.assertIn("tematy A2: zmieniony", run(check, tmp).stdout)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(K.main(["sprawdz", path]), 1)

    def test_file_without_map_sheets_is_not_ok(self):
        """Befund V13: eine Datei ohne Kartenblaetter darf nicht als MAPA OK gelten."""
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl missing")
        import context as K
        start = mapa_blocks()[0]
        verify = CODE.findall((MAPA.parent / "sprawdz-mape.md").read_text(encoding="utf-8"))[0]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "bez-mapy.xlsx")
            wb = openpyxl.Workbook()
            wb.active.title = "entries"
            wb.save(path)
            self.assertIn("brak arkusza: tematy", K.sprawdz(path))
            check = start + "\n" + verify.replace('PLIK = "mapa.xlsx"', "PLIK = %r" % path)
            out = run(check, tmp).stdout
            self.assertIn("brak arkusza: tematy", out)
            self.assertNotIn("MAPA OK", out)

    def test_errors_save_nothing(self):
        start, write = mapa_blocks()[:2]
        with tempfile.TemporaryDirectory() as tmp:
            out = run(start + "\n" + fill(write, TEMATY_F, [("A1", "A2", "rozmowa", "bez daty", "")], CELE_F), tmp)
            self.assertIn("BŁĘDY", out.stdout, out.stderr)
            self.assertIn("A1>A2: rozmowa wymaga daty RRRR-MM-DD", out.stdout)
            self.assertEqual(list(Path(tmp).glob("*.xlsx")), [])


COPIES = ("method/prompts", "method/protocols")          # unchanged third-party copies, checked by hash instead of style
FENCE = re.compile(r"```[a-z]*\n.*?```", re.S)


class CopiesTest(unittest.TestCase):
    def test_hashes_match(self):
        import hashlib
        for folder in COPIES:
            base = ROOT / folder
            listed = {}
            for line in (base / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
                h, name = line.split(" *", 1)
                listed[name] = h
            files = sorted(p.relative_to(base).as_posix() for p in base.rglob("*.md") if p.name != "LICENSE.md")
            self.assertEqual(sorted(listed), files, folder)
            for name, h in listed.items():
                self.assertEqual(hashlib.sha256((base / name).read_bytes()).hexdigest(), h, name)
            self.assertIn("CC BY-SA 4.0", (base / "LICENSE.md").read_text(encoding="utf-8"))

    def test_minimal_triage_by_reference(self):
        # F-0038 (X1 22.11.2026): kein woertlicher Auszug mehr, nur Verweis auf die Kopie in method/prompts
        src = (ROOT / "method/prompts" / "core" / "artifact-triage.md").read_text(encoding="utf-8")
        self.assertIn("### 2. Artifact Triage", src)
        for platform in ("copilot", "gemini"):
            if fehlt("2-agents/" + platform):
                continue
            agent = (ROOT / "2-agents" / platform / "analysis" / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
            self.assertIn("method/prompts/core/artifact-triage.md", agent, platform)
            self.assertNotIn("You are an artifact triage analyst", agent, platform)
        self.assertNotIn("Wyjątek / exception", (ROOT / "LICENSE").read_text(encoding="utf-8"))


@braucht("2-agents/copilot")
class AgentsTest(unittest.TestCase):
    def test_limits_and_fields(self):
        for name in ("stream", "map", "analysis", "sources"):
            d = ROOT / "2-agents/copilot" / name
            self.assertLessEqual(len((d / "INSTRUCTIONS.txt").read_text(encoding="utf-8")), 8000, name)
            agent = (d / "AGENT.md").read_text(encoding="utf-8")
            title = re.search(r"## Nazwa \(Name\)\n\n(.+)\n", agent).group(1)
            self.assertLessEqual(len(title), 30, name)
            desc = re.search(r"## Opis \(Description\)\n\n(.+)\n", agent).group(1)
            self.assertLessEqual(len(desc), 1000, name)

    def test_analiza_menu_and_language(self):
        t = (ROOT / "2-agents/copilot" / "analysis" / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
        for s in ("1. Dalej bez dodatkowych informacji.", "2. Ogólny komentarz albo zlecenie.",
                  "3. Sformułowanie problemu badawczego.", "W jakim języku ma być wynik?"):
            self.assertIn(s, t)
        self.assertLess(t.index("# Krok 2"), t.index("# Krok 3"))
        for f in ("feminist-theory", "multimodal-analysis", "postcolonial-theory", "semiotics", "source-criticism",
                  "structuralism", "content-analysis", "conversation-analysis", "systems-theory", "hermeneutics"):
            self.assertIn(f, t)
            self.assertTrue(list((ROOT / "method/prompts").rglob(f + ".md")), f)


@braucht("2-agents/copilot")
class InterculturalTest(unittest.TestCase):
    """The cultural check is a step in the analysis agent, not only a wish: the instructions, the template and the
    files that point to it must carry the same marks. The test reads the text of the instructions. It cannot show
    that a model follows them, that is what the checklist in the template is for."""
    MARKS = ("Kontekst:", "brak informacji", "[założenie modelu]", "brak podstawy", "deklaracja nie mówi",
             "wybrany przeciw", "Kontrola kulturowa")

    def agent(self):
        return (ROOT / "2-agents/copilot" / "analysis" / "INSTRUCTIONS.txt").read_text(encoding="utf-8")

    def test_steps_in_order(self):
        t = self.agent()
        heads = [t.index(h) for h in ("# Krok 3: język wyniku i kontekst kulturowy", "# Krok 4", "# Krok 5")]
        self.assertEqual(heads, sorted(heads))
        step3, step4, step5 = t[heads[0]:heads[1]], t[heads[1]:heads[2]], t[heads[2]:]
        for s in ("W jakim języku ma być wynik?", "Kontekst:", "brak informacji"):
            self.assertIn(s, step3)
        for s in ("deklaracja nie mówi", "wybrany przeciw"):
            self.assertIn(s, step4)
        block = step5[step5.index("blok „Kontrola kulturowa”"):]
        self.assertIn("[założenie modelu]", block)
        self.assertIn("brak podstawy", block)
        self.assertIn("nie dotyczy: powód", block)
        self.assertEqual(len(re.findall(r"^[1-5]\. ", block[:block.index("# Gdy coś nie działa")], re.M)), 5)

    def test_never_rules(self):
        t = self.agent()
        never = t[t.index("# Nigdy"):t.index("# Triaż minimalny")]
        self.assertIn("kultury, której nie podał", never)
        self.assertIn("Nie pomijaj bloku „Kontrola kulturowa”", never)

    def test_template_carries_same_marks(self):
        tpl = (ROOT / "3-templates" / "cultural-check.pl.md").read_text(encoding="utf-8")
        for m in self.MARKS:
            self.assertIn(m, tpl, m)
        for m in ("[model assumption]", "chosen against", "declaration does not say", "Cultural check"):
            self.assertIn(m, tpl, m)       # the English paste text for any assistant
        for ref in ("interpretive-frame-protocol.md", "actant-self-check.md"):
            self.assertTrue((ROOT / "method/protocols" / ref).is_file(), ref)
            self.assertIn(ref, tpl)

    def test_sources_agent_and_pointers(self):
        z = (ROOT / "2-agents/copilot" / "sources" / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
        self.assertIn("w języku artefaktu", z)
        self.assertIn("Kontrola kulturowa", (ROOT / "2-agents/copilot" / "analysis" / "AGENT.md").read_text(encoding="utf-8"))
        for name in ("README.md", "1-start/setup.pl.md", "1-start/setup.en.md"):
            self.assertIn("cultural-check.pl.md", (ROOT / name).read_text(encoding="utf-8"), name)
        self.assertIn("cultural-check.pl.md", (ROOT / "3-templates" / "after-triage.pl.md").read_text(encoding="utf-8"))


@braucht("2-agents/copilot", "1-start/setup.pl.md")
class ToolDisclosureTest(unittest.TestCase):
    """Tool, model and effort are recorded where the work is recorded: a sheet "tool" in the stream of consciousness file, a line
    "Narzędzie" at the end of the analysis and source results, a sheet "narzedzie" in the Excel register. The test
    reads the instructions and runs the stream of consciousness code. It cannot show that a model reports its own version truly."""
    TOOL_HEAD = ["date", "tool", "model", "model_source", "code_runs", "session_minutes", "compute"]

    def read(self, *parts):
        return (ROOT.joinpath(*parts)).read_text(encoding="utf-8")

    def test_stream_sheet_tool(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl missing")
        text = self.read("2-agents/copilot", "stream", "INSTRUCTIONS.txt")
        for s in ("TOOL = (", "never from your memory", "stated by chat", "entered by user", "is not hashed"):
            self.assertIn(s, text, s)
        stub = "ENTRIES = [\n    # (number, form \"verbatim\" or \"addendum\", title, paraphrase, verbatim, provenance, assistant_content True/False)\n]\n"
        code = code_blocks()[1].replace(stub, "ENTRIES = [(1, 'verbatim', 't', 'p', 'Hallo', 'prov', False)]\n")
        with tempfile.TemporaryDirectory() as tmp:
            out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=tmp)
            self.assertEqual(out.returncode, 0, out.stderr)
            wb = openpyxl.load_workbook(os.path.join(tmp, out.stdout.split()[0]))
            self.assertEqual(wb.sheetnames, ["entries", "register", "tool"])
            rows = list(wb["tool"].iter_rows(values_only=True))
            self.assertEqual(list(rows[0]), self.TOOL_HEAD)
            self.assertEqual(rows[1][1:4], ("unknown", "unknown", "unknown"))      # nothing is invented by default
            self.assertEqual(rows[1][4], 2)
            self.assertEqual(rows[1][0], list(wb["register"].iter_rows(values_only=True))[1][1])   # same date as the register
            reg = list(wb["register"].iter_rows(values_only=True))[0]
            self.assertEqual(len(reg), 11)                                         # hashed register with sha256_raw (F-0049)
            import hashlib
            row = list(wb["register"].iter_rows(values_only=True))[1]
            self.assertEqual(reg[5], "sha256_raw")
            self.assertEqual(row[5], hashlib.sha256("Hallo".encode("utf-8")).hexdigest())   # exact bytes

    def test_result_line_in_analysis_and_sources(self):
        for name in ("analysis", "sources"):
            t = self.read("2-agents/copilot", name, "INSTRUCTIONS.txt")
            for s in ("wiersz „Narzędzie”", "tak, jak podaje czat", "„nieznane”", "tokeny", "Nie podawaj modelu z pamięci o sobie"):
                self.assertIn(s, t, (name, s))
        a = self.read("2-agents/copilot", "analysis", "INSTRUCTIONS.txt")
        self.assertGreater(a.index("wiersz „Narzędzie”"), a.index("blok „Kontrola kulturowa”"))   # last thing in step 5
        self.assertLess(a.index("wiersz „Narzędzie”"), a.index("# Gdy coś nie działa"))

    def test_excel_sheet_and_template(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl missing")
        import office as O
        with tempfile.TemporaryDirectory() as tmp:
            wb = openpyxl.load_workbook(O.build(Path(tmp, "r.xlsx")))
            ws = wb["narzedzie"]
            head = [c.value for c in ws[2]]
            self.assertEqual(head[:5], ["Data", "Narzędzie (platforma i agent)", "Model", "Skąd nazwa modelu", "Uruchomienia kodu"])
            self.assertIn("Nakład obliczeniowy (tokeny, jeśli widoczne)", head)
            lists = [dv.formula1 for dv in ws.data_validations.dataValidation]
            self.assertIn('"wg czatu,wpisane przez osobę,nieznane"', lists)
        tpl = self.read("3-templates", "tool-disclosure.pl.md")
        for s in ("Skąd nazwa modelu", "nieznane", "Granice", "Disclose tool use", "Never give a model name from your memory",
                  "nie ma skrótu SHA-256", "tokenów"):
            self.assertIn(s, tpl, s)
        for name in ("README.md", "1-start/setup.pl.md", "1-start/setup.en.md"):
            self.assertIn("tool-disclosure.pl.md", self.read(name), name)
        self.assertIn("narzedzie", self.read("4-without-ai", "README.pl.md"))


class ProductIdentityTest(unittest.TestCase):
    """Produktnummer und Version stehen in product.json und gleich in jedem Dokumentkopf (X1 2026-11-06)."""

    KOEPFE = ["README.md", "1-start/setup.pl.md", "1-start/setup.en.md", "4-without-ai/README.pl.md",
              "3-templates/research-problem-card.pl.md", "3-templates/cultural-check.pl.md",
              "3-templates/after-triage.pl.md", "3-templates/tool-disclosure.pl.md"]

    def test_product_file(self):
        data = json.loads((ROOT / "product.json").read_text(encoding="utf-8"))
        self.assertRegex(data["nummer"], r"^\d{2}\.\d{2}$")
        self.assertRegex(data["version"], r"^\d+\.\d+\.\d+$")

    def test_heads_match_product_file(self):
        data = json.loads((ROOT / "product.json").read_text(encoding="utf-8"))
        for name in self.KOEPFE:
            if fehlt(name):
                continue
            text = (ROOT / name).read_text(encoding="utf-8")
            with self.subTest(datei=name):
                self.assertIn(data["nummer"], text)
                self.assertIn(data["version"], text)

    def test_logo_present(self):
        self.assertTrue((ROOT / "design/logo" / "kaiwa-logo.svg").exists())
        for name in ("README.md", "1-start/setup.pl.md", "1-start/setup.en.md"):
            if fehlt(name):
                continue
            with self.subTest(datei=name):
                self.assertIn("design/logo/kaiwa-logo.svg", (ROOT / name).read_text(encoding="utf-8"))


@braucht("design/logo/status.json", "tools/logo_status.py")
class LogoStatusTest(unittest.TestCase):
    """Statusfassungen und Farbthemen des Logos: vollständig, gleiche Bytes bei erneutem Bau, Kontrast mindestens 3:1."""

    def test_states_and_themes(self):
        sys.path.insert(0, str(HERE))
        import logo_status as s
        erster = {n: (ROOT / "design/logo" / "status" / n).read_bytes() for n in s.bauen()}
        zweiter = {n: (ROOT / "design/logo" / "status" / n).read_bytes() for n in s.bauen()}
        self.assertEqual(erster, zweiter)
        daten = json.loads((ROOT / "design/logo" / "status.json").read_text(encoding="utf-8"))
        themen = json.loads((ROOT / "design/logo" / "themes.json").read_text(encoding="utf-8"))
        self.assertEqual(len(erster), len(daten["zustaende"]) + len(themen["themen"]))  # nur das Icon, je Zustand und je Modus eine Datei
        for z in daten["zustaende"]:
            with self.subTest(zustand=z["id"]):
                self.assertGreaterEqual(s.kontrast(z["farbe"], daten["hintergrund"]), 3.0)
        formen = {z["form"] for z in daten["zustaende"]}
        self.assertGreaterEqual(len(formen), 4, "Zustände dürfen sich nicht nur durch die Farbe unterscheiden")


class SzukajTest(unittest.TestCase):
    OA = {"results": [{"display_name": "Semiotics  of ads", "publication_year": 2020, "doi": "https://doi.org/10.1/AB",
                       "authorships": [{"author": {"display_name": "A. Nowak"}}],
                       "open_access": {"is_oa": True, "oa_url": "https://x.org/a.pdf"}}]}
    CR = {"message": {"items": [{"title": ["Semiotics of ads"], "DOI": "10.1/ab", "URL": "https://doi.org/10.1/ab",
                                 "issued": {"date-parts": [[2020]]}, "author": [{"given": "A.", "family": "Nowak"}]},
                                {"title": ["Other"], "DOI": "10.2/cd", "issued": {"date-parts": [[2019]]}}]}}
    DJ = {"results": [{"bibjson": {"title": "Znaki w reklamie", "year": "2024", "author": [{"name": "B. Kowal "}],
                                   "identifier": [{"type": "doi", "id": "10.3/EF"}], "link": [{"url": "https://j.pl/1"}]}}]}

    def fake(self, robots=""):
        data = {"api.openalex.org": self.OA, "api.crossref.org": self.CR, "doaj.org": self.DJ}

        def pobierz(url):
            host = url.split("/")[2]
            if url.endswith("/robots.txt"):
                if robots:
                    return robots
                raise OSError("no robots")
            return json.dumps(data[host])
        return pobierz

    def test_parse_dedup_csv(self):
        import search as S
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp, "w.csv")
            with contextlib.redirect_stdout(io.StringIO()) as buf:
                rc = S.main(["semiotyka", "--csv", str(out)], pobierz=self.fake(), dzien="2026-11-05")
            self.assertEqual(rc, 0)
            rows = list(csv_reader(out))
            self.assertEqual(rows[0], S.KOLUMNY)
            self.assertEqual(len(rows) - 1, 3)                      # same DOI from OpenAlex and Crossref counted once
            self.assertTrue(all(r[3] == "aggregator-only" and r[7] == "nie" for r in rows[1:]))
            self.assertIn("https://doi.org/10.1/ab", [r[1] for r in rows])
            self.assertIn("doaj: ok, 1 trafień", buf.getvalue())

    def test_columns_match_excel_register(self):
        import search as S
        import office as O
        cols = [c[0] for c in next(s for s in O.SHEETS if s[0] == "zrodla")[2]]
        self.assertEqual(S.KOLUMNY, cols)

    def test_robots_and_rate_limit(self):
        import urllib.error
        import search as S
        rec, status = S.szukaj("doaj", "x", 5, pobierz=self.fake("User-agent: *\nDisallow: /api/\n"))
        self.assertEqual((rec, status), ([], "robots: ścieżka zabroniona w robots.txt"))
        calls = []

        def limited(url):
            if url.endswith("/robots.txt"):
                raise OSError
            calls.append(url)
            raise urllib.error.HTTPError(url, 429, "Too Many", None, None)
        rec, status = S.szukaj("crossref", "x", 5, pobierz=limited, czekaj=lambda s: None)
        self.assertEqual((rec, status, len(calls)), ([], "limit (HTTP 429)", 2))

    def test_empty_result_is_named(self):
        import search as S

        def empty(url):
            if url.endswith("/robots.txt"):
                raise OSError
            return json.dumps({"results": []})
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            S.main(["xyz", "--zrodla", "doaj"], pobierz=empty, dzien="2026-11-05")
        self.assertIn("w doaj z zapytaniem „xyz” dnia 2026-11-05 nic nie znaleziono", buf.getvalue())


def csv_reader(path):
    import csv
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.reader(f))


class OfficeTest(unittest.TestCase):
    def test_build(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl missing")
        import office as O
        with tempfile.TemporaryDirectory() as tmp:
            p = O.build(Path(tmp, "r.xlsx"))
            wb = openpyxl.load_workbook(p)
            self.assertEqual(wb.sheetnames, ["zrodla", "pochodzenie", "decyzje", "przed_publikacja", "falsyfikacja", "narzedzie"])
            self.assertEqual(wb["falsyfikacja"].max_row, 12)
            lists = [dv.formula1 for dv in wb["zrodla"].data_validations.dataValidation]
            self.assertIn('"deep-read,abstract,agent-reported,aggregator-only"', lists)
        src = (ROOT / "method/protocols" / "source-protocol.md").read_text(encoding="utf-8")
        for level in O.LISTS["poziom"]:
            self.assertIn("**%s**" % level, src)                 # levels are the protocol's own words
        prov = (ROOT / "method/protocols" / "provenance-protocol.md").read_text(encoding="utf-8")
        for m in O.LISTS["znacznik"]:
            self.assertIn("`%s`" % m, prov)


class MapRulesTest(unittest.TestCase):
    """Eine Regelquelle fuer die Kontextkarte: der Block in tools/context.py, woertlich in jeder Map-Anweisung (Bericht 22.11.2026, P0 4)."""

    def test_every_vendor_same_rules(self):
        lokal = RULES.search((HERE / "context.py").read_text(encoding="utf-8")).group(0)
        orte = [ROOT / "2-agents" / v / "map" / "INSTRUCTIONS.txt" for v in ("copilot", "gemini", "chatgpt", "claude")]
        orte.append(ROOT / "2-agents/claude/code/kaiwa-map/SKILL.md")
        geprueft = 0
        for p in orte:
            if fehlt(str(p.relative_to(ROOT))):
                continue
            with self.subTest(datei=str(p.relative_to(ROOT))):
                m = RULES.search(p.read_text(encoding="utf-8"))
                self.assertIsNotNone(m)
                self.assertEqual(m.group(0), lokal)
                geprueft += 1
        if not TEILPAKET:
            self.assertGreater(geprueft, 0)


class TextTest(unittest.TestCase):
    def test_no_semicolon_or_dash_in_prose(self):
        findings = []
        for p in sorted(ROOT.rglob("*")):
            if p.suffix not in (".md", ".txt") or not p.is_file():
                continue
            if "/".join(p.relative_to(ROOT).parts[:2]) in COPIES and p.name != "LICENSE.md":
                continue
            if p.relative_to(ROOT).parts[0].startswith("."):  # lokale Werkzeugordner wie .remember, nicht Teil des Pakets
                continue
            text = FENCE.sub("", p.read_text(encoding="utf-8"))
            text = re.sub(r"`[^`]*`", "", text)
            for nr, line in enumerate(text.splitlines(), 1):
                if re.search("[;—–]", line):
                    findings.append("%s:%d" % (p.relative_to(ROOT), nr))
        self.assertEqual(findings, [])


@braucht("2-agents/chatgpt/project-kit")
class ChatGPTProjectKitTest(unittest.TestCase):
    """Projekt-Set fuer ChatGPT (X1 25.11.2026): Plugin im ganzen Konto, dazu pro Themenprojekt dieselben Dateien und
    Anweisungen mit eigenem Stand. Das Plugin ist im Projekt-Chat nutzbar (X1 sah KAIWA Suite im Projekt Master studies)."""
    BASE = ROOT / "2-agents/chatgpt/project-kit"

    def test_instruction_length(self):
        t = (self.BASE / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
        self.assertLessEqual(len(t), 7500)
        self.assertLessEqual(len(t.encode("utf-8")), 8000)

    def test_instruction_names_every_project_file_and_the_rules(self):
        t = (self.BASE / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
        for name in ("registers.xlsx", "kaiwa-template.docx", "README.pl.md", "mapa-", "dictation-"):
            self.assertIn(name, t, name)
        for s in ("read only for you", "replace the project file by hand", "One KAIWA module per chat", "of other projects"):
            self.assertIn(s, t, s)
        for sheet in ("zrodla", "pochodzenie", "decyzje", "przed_publikacja", "falsyfikacja", "narzedzie"):
            self.assertIn(sheet, t, sheet)

    def test_file_list_matches_the_zip_and_exists(self):
        import chatgpt_plugin as P
        files = [l.strip() for l in (self.BASE / "files.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertLessEqual(len(files), 10)  # one upload
        for p in files:
            self.assertTrue((ROOT / p).is_file(), p)
            self.assertIn(Path(p).name, P.kit_entries(), p)

    def test_kit_has_no_scripts_and_project_md_names_the_files(self):
        import chatgpt_plugin as P
        names = set(P.kit_entries())
        self.assertFalse([n for n in names if n.endswith(".py")])
        text = (self.BASE / "PROJECT.md").read_text(encoding="utf-8")
        for n in ("INSTRUCTIONS.txt", "registers.xlsx", "kaiwa-template.docx", "README.pl.md"):
            self.assertIn(n, text, n)

    def test_registers_workbook_has_the_sheets_the_instruction_names(self):
        import openpyxl
        wb = openpyxl.load_workbook(ROOT / "4-without-ai/registers.xlsx")
        self.assertEqual(wb.sheetnames, ["zrodla", "pochodzenie", "decyzje", "przed_publikacja", "falsyfikacja", "narzedzie"])


@braucht("2-agents/chatgpt")
class ChatGPTTest(unittest.TestCase):
    """ChatGPT-Weg (F-0045, F-0021): Projects auf einem Go-Konto, 25 Dateien je Project, 10 je Upload
    (OpenAI-Hilfe „Projects in ChatGPT“, geprüft 22.11.2026). Kein OneDrive, kein Agent Builder."""
    BASE = ROOT / "2-agents/chatgpt"
    AGENTS = ("stream", "map", "analysis", "sources")

    def test_file_lists(self):
        for a in self.AGENTS:
            files = [l.strip() for l in (self.BASE / a / "files.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
            self.assertLessEqual(len(files), 25, a)
            self.assertLessEqual(len(files), 10, a)  # eine Liste, ein Upload
            for p in files:
                self.assertTrue((ROOT / p).is_file(), p)

    def test_no_copilot_platform(self):
        for p in self.BASE.rglob("*"):
            if p.is_file() and p.suffix != ".png":
                t = p.read_text(encoding="utf-8").lower()
                for w in ("onedrive", "sharepoint", "agent builder"):
                    self.assertNotIn(w, t, "%s: %s" % (p.name, w))

    def test_instruction_length(self):
        for a in self.AGENTS:
            t = (self.BASE / a / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
            self.assertLessEqual(len(t), 8000, a)  # Copilot-Grenze als tragbare Obergrenze, ChatGPT nennt keine
            # Abstand zur gemeldeten Grenze, auch wenn ein Feld Bytes statt Zeichen zaehlt (Bericht 22.11.2026)
            self.assertLessEqual(len(t), 7500, a)
            self.assertLessEqual(len(t.encode("utf-8")), 8000, a)

    def test_start_menu(self):
        """Start-Protokoll (studium F-0071): Menue vor jeder Analyse, Spezifikation und Bild als Projektdateien."""
        d = self.BASE / "analysis"
        files = (d / "files.txt").read_text(encoding="utf-8")
        for n in ("SUIT-START-MENU.md", "kaiwa-start-menu.png"):
            self.assertIn("2-agents/chatgpt/analysis/" + n, files)
            self.assertTrue((d / n).is_file(), n)
        t = (d / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
        self.assertLess(t.index("# Start: menu"), t.index("# Krok 1"))
        spec = (d / "SUIT-START-MENU.md").read_text(encoding="utf-8")
        for w in ("rozpocznij", "zaczynamy", "let's begin", "lass uns beginnen", "Triaż", "Analiza ramą", "Problem badawczy", "Inne moduły KAIWA"):
            self.assertIn(w, spec)
        self.assertLess((d / "kaiwa-start-menu.png").stat().st_size, 600 * 1024)

    def test_project_files_complete(self):
        for a in self.AGENTS:
            for n in ("PROJECT.md", "INSTRUCTIONS.txt", "files.txt"):
                self.assertTrue((self.BASE / a / n).is_file(), "%s/%s" % (a, n))


@braucht("2-agents/chatgpt/plugin")
class ChatGPTPluginTest(unittest.TestCase):
    """ChatGPT-Wtyczka (X1 24.11.2026): vier Skills kontoweit statt vier Projekten. Aufbau nach dem Plugin,
    das ChatGPT am 24.11.2026 selbst exportiert hat. Die Referenzen sind unveraenderte Paketdateien."""
    import chatgpt_plugin as P  # noqa: E402

    def test_same_bytes_twice(self):
        self.assertEqual(self.P.build(), self.P.build())

    def test_archive_matches_package(self):
        with tempfile.TemporaryDirectory() as d:
            z = Path(d) / "p.zip"
            z.write_bytes(self.P.build())
            same, different, missing, extra = self.P.check(z)
        self.assertEqual((different, missing, extra), ([], [], []))
        self.assertEqual(len(same), len(self.P.entries()))

    def test_zip_header_says_unix(self):
        """Test in ChatGPT 25.11.2026: 'Neue Version hochladen' lehnte das ZIP mit Erzeugersystem 0 (Windows) ab und nahm
        dasselbe mit Erzeugersystem 3 (Unix) an. Das Skript schreibt immer 3."""
        z = zipfile.ZipFile(io.BytesIO(self.P.build()))
        self.assertEqual({i.create_system for i in z.infolist()}, {3})

    def test_module_files_in_skill(self):
        names = set(self.P.entries())
        for skill, module in self.P.SKILLS.items():
            need = ["2-agents/chatgpt/%s/INSTRUCTIONS.txt" % module]
            need += [l.strip() for l in (ROOT / "2-agents/chatgpt" / module / "files.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
            for p in need:
                self.assertIn("skills/%s/references/%s" % (skill, p), names)

    def test_paths_named_in_skills_exist(self):
        names = set(self.P.entries())
        for skill in self.P.SKILLS:
            text = (self.P.PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            for p in re.findall(r"`(references/[^`]+)`", text):
                if p.endswith("/"):
                    self.assertTrue(any(n.startswith("skills/%s/%s" % (skill, p)) for n in names), p)
                else:
                    self.assertIn("skills/%s/%s" % (skill, p), names)

    def test_skill_heads(self):
        for skill in self.P.SKILLS:
            lines = (self.P.PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8").splitlines()
            self.assertEqual(lines[0], "---", skill)
            end = lines.index("---", 1)
            fields = dict((k.strip(), v.strip()) for k, _, v in (l.partition(":") for l in lines[1:end]))
            self.assertEqual(sorted(fields), ["description", "name"], skill)
            self.assertEqual(fields["name"], skill)
            self.assertRegex(skill, r"^[a-z0-9-]{1,64}$")
            self.assertTrue(0 < len(fields["description"]) <= 1024, skill)

    def test_manifests(self):
        a = json.loads((self.P.PLUGIN / "plugin.json").read_text(encoding="utf-8"))
        b = json.loads((self.P.PLUGIN / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        product = json.loads((ROOT / "product.json").read_text(encoding="utf-8"))
        for k in ("name", "version", "license", "author", "repository"):
            self.assertEqual(a[k], b[k], k)
        self.assertEqual(a["extensions"]["com.openai"]["interface"], b["interface"])
        self.assertTrue(a["version"].startswith(product["version"] + "-chatgpt."), a["version"])
        self.assertEqual(a["license"], "CC-BY-NC-SA-4.0")
        self.assertIn("Użycie niekomercyjne", (ROOT / "LICENSE").read_text(encoding="utf-8"))
        self.assertEqual(b["skills"], "./skills")
        # X1 25.11.2026: unter "Website" im ChatGPT-Plugin steht die Organisation mentalpinG-Ops (Feld interface.websiteURL,
        # nach Drittquellen, die offizielle Seite von OpenAI wurde nicht gelesen)
        self.assertEqual(b["interface"]["websiteURL"], "https://github.com/mentalpinG-Ops")

    def test_icon_is_the_design_system_agent_icon(self):
        """X1 25.11.2026: das Plugin-Icon ist das Agenten-Icon des Design-Systems (Kachel tinte, K papier, Quadrat signal).
        logo und composerIcon zeigen auf PNG-Dateien, die im Archiv liegen."""
        import struct
        names = self.P.entries()
        for p in ("plugin.json", ".codex-plugin/plugin.json"):
            m = json.loads((self.P.PLUGIN / p).read_text(encoding="utf-8"))
            i = m["extensions"]["com.openai"]["interface"] if "extensions" in m else m["interface"]
            for key, size in (("logo", 512), ("composerIcon", 192)):
                ziel = i[key][2:] if i[key].startswith("./") else i[key]
                self.assertIn(ziel, names, p + ": " + key)
                kopf = names[ziel].read_bytes()[:24]
                self.assertEqual(kopf[:8], b"\x89PNG\r\n\x1a\n", ziel)
                self.assertEqual(struct.unpack(">II", kopf[16:24]), (size, size), ziel)
        svg = (ROOT / "design/logo/kaiwa-icon.svg").read_text(encoding="utf-8")
        for farbe in ("#14171F", "#F1EFE9", "#FFED00"):
            self.assertIn(farbe, svg)

    def test_one_module_per_chat(self):
        """Test in ChatGPT 24.11.2026: /triage waehrend einer Aufnahme wurde als Notiz aufgenommen.
        X1 25.11.2026: sperren mit Hinweis. Jeder Skill traegt dieselben drei Hinweiszeilen."""
        lines = None
        for skill in self.P.SKILLS:
            text = (self.P.PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("One KAIWA module per chat.", text, skill)
            found = [l.strip() for l in text.splitlines() if l.strip().startswith(("PL: \"Nagrywanie", "EN: \"A stream", "DE: \"Eine Aufnahme"))]
            self.assertEqual(len(found), 3, skill)
            if lines is None:
                lines = found
            self.assertEqual(found, lines, skill)

    def test_ten_frameworks_named(self):
        """Test in ChatGPT 25.11.2026: die Analyse wandte Hermeneutik an, deren Datei nicht im Paket war.
        X1 25.11.2026: Hermeneutik aufgenommen (zehn Rahmen). Die SKILL.md nennt genau die Rahmen, deren Dateien
        in references liegen, und sagt, was mit allen anderen geschieht."""
        text = (self.P.PLUGIN / "skills/artifact-analysis/SKILL.md").read_text(encoding="utf-8")
        files = sorted(Path(n).stem for n in self.P.entries()
                       if n.startswith("skills/artifact-analysis/references/method/prompts/")
                       and ("/cultural-scientific/" in n or "/social-science/" in n or "/philosophical/" in n))
        self.assertEqual(len(files), 10)
        self.assertIn("hermeneutics", files)
        for f in files:
            self.assertIn(f, text, f)
        self.assertIn("poza pakietem", text)
        self.assertIn("holds the files of ten", text)

    def test_instruction_names_hermeneutics(self):
        """Die Projekt-Anweisung der Analyse nennt die zehn Rahmen des Ordners method/prompts."""
        t = (ROOT / "2-agents/chatgpt/analysis/INSTRUCTIONS.txt").read_text(encoding="utf-8")
        self.assertIn("philosophical (hermeneutics)", t)
        for p in (ROOT / "method/prompts").rglob("*.md"):
            if p.parent.name in ("cultural-scientific", "social-science", "philosophical"):
                self.assertIn(p.stem, t, p.name)


@braucht("2-agents/gemini")
class GeminiTest(unittest.TestCase):
    """Gemini (X1 25.11.2026, Phase A): Test im Skill auf einem Pro-Konto. Gemini meldete keinen Python-Interpreter, das ist
    eine Aussage des Modells und nicht unabhaengig geprueft. Die Anleitung sagt es so, die Module nennen den Fall ohne Code."""
    BASE = ROOT / "2-agents/gemini"

    def test_setup_does_not_promise_code_and_names_the_finding(self):
        for name, key, alt in (("setup.en.md", "no interpreter", "| yes (for SHA-256 hashes and `.xlsx`) |"),
                               ("setup.pl.md", "brak interpretera", "| tak (do skrótów SHA-256 i pliku `.xlsx`) |")):
            text = (self.BASE / name).read_text(encoding="utf-8")
            self.assertIn(key, text, name)
            self.assertNotIn(alt, text, name)
            self.assertIn("25", text)
        en = (self.BASE / "setup.en.md").read_text(encoding="utf-8")
        for s in ("a statement of the model, not checked independently", "No interpreter reported, behaviour of the skill", "must not invent a hash"):
            self.assertIn(s, en, s)

    def test_stream_and_map_name_the_case_without_code(self):
        stream = (self.BASE / "stream/INSTRUCTIONS.txt").read_text(encoding="utf-8")
        self.assertIn("0. If code cannot run", stream)
        self.assertIn("not in Google Drive", stream)
        karte = (self.BASE / "map/INSTRUCTIONS.txt").read_text(encoding="utf-8")
        self.assertIn("0. Bez kodu", karte)
        self.assertIn("także nie w Google Drive", karte)
        self.assertIn("sprawdzenie nie jest możliwe", karte)

    def test_analysis_carries_the_rules_of_the_plugin_test(self):
        for vendor in ("chatgpt", "gemini"):
            text = (ROOT / "2-agents" / vendor / "analysis/INSTRUCTIONS.txt").read_text(encoding="utf-8")
            for s in ("Takiej ramy nie stosuj", "Jedno pole na wiadomość", "nie zastępuje pytania z kroku 2",
                      "Nie wnioskuj o stanowisku użytkownika", "liczby bez cytatu nie podawaj", "także kroki bez wymaganego pliku"):
                self.assertIn(s, text, vendor + ": " + s)

    def test_chatgpt_setup_names_the_three_ways_and_the_tested_state(self):
        for name, keys in (("setup.en.md", ("Three ways", "Tested state", "chatgpt-plugin", "project-kit", "websiteURL", "Never tried")),
                           ("setup.pl.md", ("Trzy drogi", "Przetestowany stan", "chatgpt-plugin", "project-kit", "websiteURL", "Nigdy nie sprawdzono"))):
            text = (ROOT / "2-agents/chatgpt" / name).read_text(encoding="utf-8")
            for s in keys:
                self.assertIn(s, text, name + ": " + s)
            self.assertNotRegex(text, r"\bT[0-9]{1,3}\b", name)  # Befundnummern gehoeren nur in Commit-Texte
        self.assertLessEqual(len((ROOT / "2-agents/chatgpt/analysis/INSTRUCTIONS.txt").read_text(encoding="utf-8")), 7500)


@braucht("2-agents/claude")
class ClaudeTest(unittest.TestCase):
    """Claude-Weg (studium F-0069): Projekte in claude.ai (Browser, Desktop-App) und Skills in Claude Code.
    Skill-Regeln nach platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
    (name: höchstens 64 Zeichen, nur a-z, 0-9 und Bindestrich, ohne „claude“ und „anthropic“;
    description: nicht leer, höchstens 1024 Zeichen) und code.claude.com/docs/en/skills
    (SKILL.md unter 500 Zeilen), geprüft 22.11.2026."""
    BASE = ROOT / "2-agents/claude"
    AGENTS = ("stream", "map", "analysis", "sources")

    def test_project_files_complete(self):
        for a in self.AGENTS:
            for n in ("PROJECT.md", "INSTRUCTIONS.txt", "files.txt"):
                self.assertTrue((self.BASE / a / n).is_file(), "%s/%s" % (a, n))

    def test_file_lists(self):
        for a in self.AGENTS:
            files = [l.strip() for l in (self.BASE / a / "files.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
            self.assertTrue(files, a)
            for p in files:
                self.assertTrue((ROOT / p).is_file(), p)

    def test_instruction_length(self):
        for a in self.AGENTS:
            t = (self.BASE / a / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
            self.assertLessEqual(len(t), 8000, a)  # gleiche Obergrenze wie bei ChatGPT und Copilot
            # Abstand zur gemeldeten Grenze, auch wenn ein Feld Bytes statt Zeichen zaehlt (Bericht 22.11.2026)
            self.assertLessEqual(len(t), 7500, a)
            self.assertLessEqual(len(t.encode("utf-8")), 8000, a)

    def test_no_other_vendor(self):
        # Die Setup-Texte nennen die Herkunft aus dem ChatGPT-Weg, geprüft werden die Texte für das Modell.
        for p in self.BASE.rglob("*"):
            if p.is_file() and not p.name.startswith("setup."):
                t = p.read_text(encoding="utf-8").lower()
                for w in ("chatgpt", "openai"):
                    self.assertNotIn(w, t, "%s: %s" % (p.relative_to(self.BASE), w))

    def test_skills(self):
        skills = sorted((self.BASE / "code").glob("kaiwa-*/SKILL.md"))
        self.assertEqual([p.parent.name for p in skills], ["kaiwa-analysis", "kaiwa-map", "kaiwa-sources", "kaiwa-stream"])
        for p in skills:
            text = p.read_text(encoding="utf-8")
            lines = text.splitlines()
            self.assertEqual(lines[0], "---", p.parent.name)
            end = lines.index("---", 1)
            fields = {}
            for l in lines[1:end]:
                key, _, value = l.partition(":")
                fields[key.strip()] = value.strip()
            self.assertEqual(sorted(fields), ["description", "name"], p.parent.name)
            self.assertEqual(fields["name"], p.parent.name)
            self.assertRegex(fields["name"], r"^[a-z0-9-]{1,64}$")
            for w in ("claude", "anthropic"):
                self.assertNotIn(w, fields["name"])
            self.assertTrue(fields["description"], p.parent.name)
            self.assertLessEqual(len(fields["description"]), 1024, p.parent.name)
            self.assertLess(len(lines), 500, p.parent.name)


@braucht("release/sets.json", "tools/release.py")
class ReleaseSetsTest(unittest.TestCase):
    """Dateisatz der Release-ZIPs (release/sets.json, einzige Quelle, F-0086): jeder Pfad existiert, Verweise loesen sich auf."""

    @classmethod
    def setUpClass(cls):
        import release as REL
        cls.REL = REL
        cls.q = REL.Quelle(None)
        cls.s = REL.sets(cls.q)

    def test_every_path_exists(self):
        for a in self.s["immer"]:
            self.assertTrue(a in self.q.set or self.q.unter(a), a)
        for e in self.s["eintraege"]:
            self.assertTrue(e["p"] in self.q.set or self.q.unter(e["p"]), e["p"])
        for name, paket in self.s["pakete"].items():
            for ziel, quelle in paket["dateien"]:
                pfade = [quelle] if isinstance(quelle, str) else [quelle["kopf"], quelle["koerper"]]
                for p in pfade:
                    self.assertIn(p, self.q.set, name + ": " + ziel)

    def test_files_referenced_by_licences_and_readme_are_in_every_zip(self):
        # Befund 24.11.2026: LICENSE-COMMERCIAL.md verweist auf design/fonts/OFL.txt, README.md und DISCLOSURE.md auf first-contact.html
        for a in self.REL.ANBIETER:
            satz = set(self.REL.dateisatz(self.q, self.s, a))
            for p in ("design/fonts/OFL.txt", "1-start/first-contact.html", "LICENSE", "LICENSE-COMMERCIAL.md", "DISCLOSURE.md", "README.md", "product.json"):
                self.assertIn(p, satz, a + ": " + p)

    def test_files_txt_entries_are_in_the_vendor_zip(self):
        for a in ("chatgpt", "claude"):
            satz = set(self.REL.dateisatz(self.q, self.s, a))
            for f in sorted(x for x in self.q.set if x.startswith("2-agents/%s/" % a) and x.endswith("/files.txt")):
                for zeile in self.q.lies(f).decode("utf-8").splitlines():
                    zeile = zeile.strip()
                    if zeile:
                        self.assertIn(zeile, satz, a + ": " + f + " nennt " + zeile)

    def test_release_script_is_not_shipped(self):
        for a in self.REL.ANBIETER:
            self.assertNotIn("tools/release.py", self.REL.dateisatz(self.q, self.s, a))

    def test_plugin_version_matches_product(self):
        manifest = json.loads(self.q.lies("2-agents/copilot/plugin/manifest.json").decode("utf-8"))
        self.assertEqual(manifest["version"], self.REL.version(self.q))


@braucht("release/sets.json", "tools/release.py")
class ReleaseBuildTest(unittest.TestCase):
    """Die gebauten ZIPs: reproduzierbar, Inhalt gleich Quelle, Copilot-Pakete nach den Regeln aus Microsoft Learn (Meta, 24.11.2026)."""

    @classmethod
    def setUpClass(cls):
        import release as REL
        cls.REL = REL
        cls.tmp = tempfile.TemporaryDirectory()
        cls.q = REL.Quelle(None)
        cls.s = REL.sets(cls.q)
        cls.ver = REL.version(cls.q)
        cls.out = Path(cls.tmp.name) / "release"
        cls.befunde, cls.m = REL.pruefe(cls.q, cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_build_is_reproducible_and_matches_sources(self):
        self.assertEqual(self.befunde, [])

    def test_names_carry_the_version_and_sums_match(self):
        import hashlib
        namen = {e["name"] for e in self.m["dateien"]}
        for basis in ["KAIWA-SUITE-" + a for a in self.REL.ANBIETER] + ["KAIWA-SUITE-copilot-skill", "KAIWA-SUITE-copilot-plugin", "KAIWA-SUITE-chatgpt-plugin", "KAIWA-SUITE-chatgpt-project-kit", "KAIWA-SUITE-gemini-skill"]:
            self.assertIn("%s-%s.zip" % (basis, self.ver), namen)
            self.assertIn(basis + ".zip", namen)
        zeilen = (self.out / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(zeilen), len(namen))
        for z in zeilen:
            h, n = z.split("  ")
            self.assertEqual(hashlib.sha256((self.out / n).read_bytes()).hexdigest(), h, n)

    def test_vendor_zip_has_one_root_folder_and_contents_file(self):
        for a in self.REL.ANBIETER:
            z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-%s-%s.zip" % (a, self.ver)))
            wurzeln = {n.split("/")[0] for n in z.namelist()}
            self.assertEqual(wurzeln, {"KAIWA-SUITE-" + a}, a)
            self.assertIn("KAIWA-SUITE-%s/ZIP-CONTENTS.md" % a, z.namelist())

    def test_copilot_skill_zip_has_exactly_one_skill_md_in_the_root(self):
        z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-copilot-skill-%s.zip" % self.ver))
        namen = z.namelist()
        self.assertEqual([n for n in namen if n.endswith("SKILL.md")], ["SKILL.md"])
        self.assertLessEqual(len(namen), 100)
        self.assertLess(sum(i.compress_size for i in z.infolist()), 10 * 1024 * 1024)
        kopf = re.match(r'---\nname: (.+)\ndescription: (".*")\n---\n', z.read("SKILL.md").decode("utf-8"))
        self.assertIsNotNone(kopf)
        self.assertEqual(kopf.group(1), "kaiwa-suite")

    def test_copilot_plugin_zip_follows_the_package_rules(self):
        import struct
        z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-copilot-plugin-%s.zip" % self.ver))
        namen = z.namelist()
        for n in ("manifest.json", "color.png", "outline.png"):
            self.assertIn(n, namen)
        for n, groesse in (("color.png", 192), ("outline.png", 32)):
            kopf = z.read(n)
            self.assertEqual(kopf[:8], b"\x89PNG\r\n\x1a\n")
            self.assertEqual(struct.unpack(">II", kopf[16:24]), (groesse, groesse), n)
        m = json.loads(z.read("manifest.json").decode("utf-8"))
        self.assertEqual(m["version"], self.ver)
        self.assertLessEqual(len(m["name"]["short"]), 30)
        self.assertLessEqual(len(m["name"]["full"]), 100)
        self.assertLessEqual(len(m["description"]["short"]), 80)
        self.assertLessEqual(len(m["description"]["full"]), 4000)
        ordner = [a["folder"].replace("./", "") for a in m["agentSkills"]]
        self.assertEqual(len(ordner), 4)
        for o in ordner:
            self.assertIn(o + "/SKILL.md", namen)
        self.assertEqual(sorted(n for n in namen if n.endswith("SKILL.md")), sorted(o + "/SKILL.md" for o in ordner))
        self.assertLessEqual(len(namen), 100)

    def test_chatgpt_plugin_zip_equals_the_plugin_builder(self):
        """X1 25.11.2026: das ChatGPT-Plugin steht auf der Downloadseite. Das Release-ZIP hat dieselben Dateien mit denselben
        Bytes wie tools/chatgpt_plugin.py."""
        import chatgpt_plugin as P
        z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-chatgpt-plugin-%s.zip" % self.ver))
        gebaut = zipfile.ZipFile(io.BytesIO(P.build()))
        self.assertEqual(sorted(z.namelist()), sorted(gebaut.namelist()))
        for n in gebaut.namelist():
            self.assertEqual(z.read(n), gebaut.read(n), n)
        m = json.loads(z.read("plugin.json").decode("utf-8"))
        self.assertTrue(m["version"].startswith(self.ver + "-chatgpt."), m["version"])

    def test_chatgpt_project_kit_zip_equals_the_builder(self):
        """X1 25.11.2026: Projekt-Set fuer Themenprojekte. Das Release-ZIP hat dieselben Dateien mit denselben Bytes wie
        tools/chatgpt_plugin.py --kit und liegt flach, ohne Unterordner."""
        import chatgpt_plugin as P
        z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-chatgpt-project-kit-%s.zip" % self.ver))
        gebaut = zipfile.ZipFile(io.BytesIO(P.build(P.kit_entries())))
        self.assertEqual(sorted(z.namelist()), sorted(gebaut.namelist()))
        for n in gebaut.namelist():
            self.assertEqual(z.read(n), gebaut.read(n), n)
            self.assertNotIn("/", n)

    def test_gemini_skill_zip_follows_the_upload_rules(self):
        """Google-Hilfe "Skills fuer Gemini-Apps erstellen und verwalten" und der Dialog "Skill hochladen" (X1 25.11.2026):
        SKILL.md im Hauptordner, Name in Kleinbuchstaben mit Bindestrich, nur unterstuetzte Dateitypen (der Dialog nennt
        CSV, PY, TXT, MD, das Paket nimmt nur .md und .txt), hoechstens 100 MB, keine Skripte, keine versteckten Dateien,
        jede Datei, auf die SKILL.md und die Modulanweisungen verweisen, liegt im Skill."""
        z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-gemini-skill-%s.zip" % self.ver))
        namen = z.namelist()
        self.assertEqual([n for n in namen if n.lower().endswith("skill.md")], ["SKILL.md"])
        kopf = re.match(r"---\n(.*?)\n---\n", z.read("SKILL.md").decode("utf-8"), re.S)
        self.assertIsNotNone(kopf)
        felder = dict((k.strip(), v.strip()) for k, _, v in (l.partition(":") for l in kopf.group(1).splitlines()))
        self.assertEqual(sorted(felder), ["description", "name"])
        self.assertEqual(felder["name"], "kaiwa-suite")
        self.assertRegex(felder["name"], r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertTrue(0 < len(felder["description"]) <= 1024)
        self.assertEqual({os.path.splitext(n)[1] for n in namen}, {".md", ".txt"})
        self.assertLess(sum(i.file_size for i in z.infolist()), 100 * 1024 * 1024)
        self.assertFalse([n for n in namen if n.startswith(".") or "/." in n or "__pycache__" in n])
        skill = z.read("SKILL.md").decode("utf-8")
        for m in ("stream", "map", "analysis", "sources"):
            self.assertIn("%s/INSTRUCTIONS.txt" % m, skill)
            self.assertIn("%s/INSTRUCTIONS.txt" % m, namen)
            self.assertEqual(z.read("%s/INSTRUCTIONS.txt" % m), self.q.lies("2-agents/gemini/%s/INSTRUCTIONS.txt" % m))
        for p in ("method/prompts/core/artifact-triage.md", "method/prompts/framework-catalog.md", "method/protocols/source-protocol.md"):
            self.assertIn(p, namen)
        rahmen = sorted(n.rsplit("/", 1)[1][:-3] for n in namen
                        if n.startswith("method/prompts/") and n.split("/")[2] in ("cultural-scientific", "social-science", "philosophical"))
        self.assertEqual(len(rahmen), 10)
        for r in rahmen:
            self.assertIn(r, skill)

    def test_plugin_skills_carry_the_module_text(self):
        z = zipfile.ZipFile(self.out / ("KAIWA-SUITE-copilot-plugin-%s.zip" % self.ver))
        for m in ("stream", "map", "analysis", "sources"):
            text = z.read("skills/kaiwa-%s/SKILL.md" % m).decode("utf-8")
            kopf = re.match(r'---\nname: (kaiwa-%s)\ndescription: (".*")\n---\n\n' % m, text)
            self.assertIsNotNone(kopf, m)
            self.assertLessEqual(len(json.loads(kopf.group(2))), 1024, m)
            body = self.q.lies("2-agents/copilot/skill/modules/%s.md" % m).decode("utf-8")
            self.assertEqual(text[kopf.end():], body, m)


class _PageParser(__import__("html.parser", fromlist=["HTMLParser"]).HTMLParser):
    """Sammelt aus einer Seite: Links, data-pkg, Absaetze ohne zweite Sprache, sichtbaren Text ohne Script und Style."""
    TARGET = ("p", "h1", "h2", "h3", "li", "summary")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.pkgs, self.unpaired, self.text = [], [], [], []
        self.stack, self.skip, self.steps_li = [], 0, 0
        self.list_depth, self.steps_level = 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        for k in ("href", "src"):
            if a.get(k):
                self.links.append(a[k])
        if a.get("data-pkg"):
            self.pkgs.append(a["data-pkg"])
        if tag in ("ol", "ul"):
            self.list_depth += 1
            if tag == "ol" and "steps" in (a.get("class") or "").split():
                self.steps_level = self.list_depth
        if tag == "li" and self.steps_level and self.list_depth == self.steps_level:
            self.steps_li += 1
        if tag in self.TARGET:
            self.stack.append({"tag": tag, "alt": False, "nolang": "data-nolang" in a, "text": ""})
        if "alt" in (a.get("class") or "").split():
            for s in self.stack:
                s["alt"] = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag in ("ol", "ul"):
            if self.list_depth == self.steps_level:
                self.steps_level = 0
            self.list_depth -= 1
        if tag in self.TARGET and self.stack and self.stack[-1]["tag"] == tag:
            s = self.stack.pop()
            if s["text"].strip() and not s["alt"] and not s["nolang"]:
                self.unpaired.append(s["text"].strip()[:60])

    def handle_data(self, data):
        if self.skip:
            return
        self.text.append(data)
        for s in self.stack:
            s["text"] += data


@braucht("index.html", "get/pages.js")
class PagesTest(unittest.TestCase):
    """Paketseite und Anbieterseiten (F-0086 bis F-0095): kein JSZip, kein GitHub-API-Abruf, Englisch mit Polnisch, Links loesen sich auf."""
    VENDOR_PAGES = ("get/copilot.html", "get/gemini.html", "get/chatgpt.html", "get/claude.html")
    PAGES = ("index.html",) + VENDOR_PAGES
    PAGES_URL = "https://mentalping-ops.github.io/KAIWA-SUITE/"
    REPO_URL = "https://github.com/mentalpinG-Ops/KAIWA-SUITE/"

    def parse(self, rel):
        p = _PageParser()
        p.feed((ROOT / rel).read_text(encoding="utf-8"))
        return p

    def test_no_jszip_no_github_api_no_placeholder(self):
        for rel in self.PAGES + ("get/pages.js", "get/pages.css"):
            t = (ROOT / rel).read_text(encoding="utf-8").lower()
            for w in ("jszip", "api.github.com", "⟨commit⟩"):
                self.assertNotIn(w, t, rel + ": " + w)

    def test_every_text_block_has_both_languages(self):
        for rel in self.PAGES:
            self.assertEqual(self.parse(rel).unpaired, [], rel)

    def test_visible_text_has_no_semicolon_or_dash(self):
        for rel in self.PAGES:
            text = "".join(self.parse(rel).text)
            self.assertEqual(re.findall(r"[;—–]", text), [], rel)

    def test_links_resolve(self):
        for rel in self.PAGES + ("1-start/first-contact.html",):
            for link in self.parse(rel).links:
                if link.startswith(("#", "mailto:", "data:")):
                    continue
                if link.startswith(self.PAGES_URL):
                    ziel = link[len(self.PAGES_URL):].split("#")[0]
                    self.assertTrue(ziel == "" or (ROOT / ziel).exists(), rel + ": " + link)
                elif link.startswith(self.REPO_URL):
                    rest = link[len(self.REPO_URL):]
                    for pre in ("blob/main/", "tree/main/"):
                        if rest.startswith(pre):
                            self.assertTrue((ROOT / rest[len(pre):]).exists(), rel + ": " + link)
                elif link.startswith("http"):
                    continue
                else:
                    ziel = (ROOT / rel).parent / link.split("#")[0].split("?")[0]
                    self.assertTrue(ziel.exists(), rel + ": " + link)

    def test_download_boxes_name_real_packages(self):
        import release as REL
        gueltig = set(REL.ANBIETER) | {"copilot-skill", "copilot-plugin", "chatgpt-plugin", "chatgpt-project-kit", "gemini-skill"}
        for rel in self.PAGES:
            for pkg in self.parse(rel).pkgs:
                self.assertIn(pkg, gueltig, rel)
        for rel, v in zip(self.VENDOR_PAGES, ("copilot", "gemini", "chatgpt", "claude")):
            self.assertIn(v, self.parse(rel).pkgs, rel)
        self.assertEqual({p for p in self.parse("index.html").pkgs},
                         set(REL.ANBIETER) | {"chatgpt-plugin", "chatgpt-project-kit", "gemini-skill"})

    def test_chatgpt_page_offers_the_plugin_zip(self):
        t = (ROOT / "get/chatgpt.html").read_text(encoding="utf-8")
        self.assertRegex(t, r'data-pkg="chatgpt-plugin" data-label="Plugin ZIP \(every chat\)"')
        # X1 lud das Projektpaket in "Neue Version hochladen" (25.11.2026): der obere Knopf nennt seinen Zweck
        self.assertIn('data-pkg="chatgpt" data-label="Bundle for four projects (not for plugin upload)"', t)
        self.assertIn('href="#plg"', t)
        for s in ("Plugin-Archiv hochladen", "Hinzufügen", "higher version number", "one KAIWA module per chat"):
            self.assertIn(s.lower(), t.lower(), s)
        import chatgpt_plugin as P
        self.assertIn(json.loads((P.PLUGIN / "plugin.json").read_text(encoding="utf-8"))["version"], t)

    def test_gemini_page_offers_the_skill_zip(self):
        t = (ROOT / "get/gemini.html").read_text(encoding="utf-8")
        self.assertIn('data-pkg="gemini-skill" data-label="Skill ZIP (for Skills &gt; Upload)"', t)
        self.assertIn('data-pkg="gemini" data-label="Bundle to unpack (not for skill upload)"', t)
        self.assertIn('href="#skl"', t)

    def test_chatgpt_page_states_the_tested_state_and_the_three_ways(self):
        # Seitenauftrag 25.11.2026: getesteter Stand und bekannte Befunde, Quelle 2-agents/chatgpt/setup.en.md
        t = (ROOT / "get/chatgpt.html").read_text(encoding="utf-8")
        for s in ('id="tst"', 'href="#tst"', "Way 1, plugin", "Way 2, project kit", "Way 3, four projects", "never uploaded",
                  "0.2.0-chatgpt.4", "menu picture was not shown", "step 2 was skipped", "not taken word for word",
                  "a framework without a file in the package", "not run live again", "<code>websiteURL</code>",
                  "refused an earlier local build", "Way 3: create the four projects"):
            self.assertIn(s.lower(), t.lower(), s)
        self.assertNotIn("All four projects are drafts", t)
        kopf = t[t.index('<section class="stack">'):t.index('<ol class="steps"')]
        self.assertIn("Three ways", kopf)

    def test_gemini_page_states_the_tested_state_and_the_missing_interpreter(self):
        t = (ROOT / "get/gemini.html").read_text(encoding="utf-8")
        for s in ('id="tst"', 'href="#tst"', "Google Pro account", "<code>kaiwa-suite</code>", "stream session started",
                  "no Python interpreter", "a statement of the model, not checked independently", "pseudocode",
                  "not tested again", "never tried"):
            self.assertIn(s.lower(), t.lower(), s)
        self.assertNotIn("All four modules are drafts", t)
        # der Schritt "First test" darf den Python-Check nicht mehr als sicher voraussetzen
        test = t[t.index("<h2>First test"):t.index("<h2>Known limits")]
        self.assertIn("no Python interpreter", test)
        self.assertIn("must not print", test)

    def test_pages_name_no_internal_test_numbers(self):
        for rel in self.PAGES + ("get/pages.js",):
            t = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"\bT[0-9]{2}\b", re.sub(r"<[^>]+>", " ", t)), rel)

    def test_index_cards_for_plugin_kit_and_skill_say_what_they_are_for(self):
        t = (ROOT / "index.html").read_text(encoding="utf-8")
        for pkg, label in (("chatgpt", "Bundle for four projects (not for plugin upload)"),
                           ("chatgpt-plugin", "Plugin ZIP (every chat)"),
                           ("chatgpt-project-kit", "Project kit ZIP (for topic projects)"),
                           ("gemini", "Bundle to unpack (not for skill upload)"),
                           ("gemini-skill", "Skill ZIP (for Skills &gt; Upload)")):
            self.assertRegex(t, r'data-pkg="%s" data-label="%s"' % (re.escape(pkg), re.escape(label)))
        for s in ("Never uploaded", "Gemini reported no Python interpreter", "Tried only in part"):
            self.assertIn(s, t, s)

    def test_script_says_when_a_file_is_not_in_the_release_yet(self):
        # gemini-skill steht erst mit dem naechsten Tag im Manifest: die Karte zeigt dann Text statt eines toten Knopfs
        t = (ROOT / "get/pages.js").read_text(encoding="utf-8")
        self.assertIn("This file is not in release", t)
        self.assertIn("Tego pliku nie ma w wydaniu", t)

    def test_vendor_pages_have_the_six_steps(self):
        for rel in self.VENDOR_PAGES:
            self.assertEqual(self.parse(rel).steps_li, 6, rel)

    def test_copilot_page_names_the_upload_ways_and_their_status(self):
        t = (ROOT / "get/copilot.html").read_text(encoding="utf-8")
        for s in ("Which upload goes where", "Hochladen", "copilot-skill", "“Plug-Ins” &gt; “Add” (Hinzufügen) &gt; “Upload” (Hochladen)",
                  "Neue Fähigkeit", "not verified", "Form tested, this ZIP not uploaded", "lost 7 of 10 hits", "Format wird nicht unterstützt", "unverified in this account", "TAR", "Do not</strong> drag a ZIP",
                  "The uploaded package must contain a 'SKILL.md' file.", "exactly one 'SKILL.md' file, but found 4"):
            self.assertIn(s.lower(), t.lower(), s)

    def test_copilot_download_buttons_say_what_they_are_for(self):
        # X1 lud das Buendel im Dialog "Skill hochladen" hoch (25.11.2026): die Knoepfe nennen ihren Zweck
        t = (ROOT / "get/copilot.html").read_text(encoding="utf-8")
        for pkg, label in (("copilot", "Bundle to unpack (not for Upload)"), ("copilot-skill", "Skill ZIP (for Plug-Ins &gt; Upload)"),
                           ("copilot-plugin", "Plugin ZIP (not verified)")):
            self.assertRegex(t, r'data-pkg="%s" data-label="%s"' % (re.escape(pkg), re.escape(label)))
        self.assertIn('data-pkg="copilot" data-label="Bundle to unpack (not for Upload)"', (ROOT / "index.html").read_text(encoding="utf-8"))
        self.assertIn('data-label', (ROOT / "get/pages.js").read_text(encoding="utf-8"))

    def test_script_reads_only_its_own_manifest_and_has_a_fallback(self):
        t = (ROOT / "get/pages.js").read_text(encoding="utf-8")
        self.assertIn("release/manifest.json", t)
        self.assertIn("archive/refs/heads/main.zip", t)
        self.assertEqual(re.findall(r"fetch\(([^)]*)\)", t), ['base + "release/manifest.json", { cache: "no-cache" }', 'base + "release/sets.json"'])

    def test_first_contact_links_the_vendor_pages(self):
        t = (ROOT / "1-start/first-contact.html").read_text(encoding="utf-8")
        for v in ("copilot", "gemini", "chatgpt", "claude"):
            self.assertIn(self.PAGES_URL + "get/%s.html" % v, t)

    def test_contact_is_only_the_university_address(self):
        for rel in self.PAGES:
            t = (ROOT / rel).read_text(encoding="utf-8").lower()
            # Seit dem Umzug des Repos in die Organisation (X1 25.11.2026) steht der Organisationsname in den Adressen
            # (github.com/mentalping-ops/..., mentalping-ops.github.io). Nur Adressen sind ausgenommen, nie Text oder Kontakt (F-0091).
            t = t.replace("github.com/mentalping-ops/", "").replace("mentalping-ops.github.io", "")
            self.assertNotIn("mentalping", t, rel)
            self.assertNotIn("gmail", t, rel)


if __name__ == "__main__":
    unittest.main()
