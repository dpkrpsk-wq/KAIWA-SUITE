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
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import dictation_ledger as L  # noqa: E402

INSTRUCTIONS = ROOT / "2-agents/copilot" / "stream" / "INSTRUCTIONS.txt"
CODE = re.compile(r"```python\n(.*?)```", re.S)
VERB = ["Freiheit ist   die Bedingung der Kritik.", "Wolność jest warunkiem krytyki.", "Freiheit ist die Bedingung der Kritik."]


def code_blocks():
    return CODE.findall(INSTRUCTIONS.read_text(encoding="utf-8"))


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
        start, write, verify = mapa_blocks()
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

    def test_errors_save_nothing(self):
        start, write, _ = mapa_blocks()
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
            agent = (ROOT / "2-agents" / platform / "analysis" / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
            self.assertIn("method/prompts/core/artifact-triage.md", agent, platform)
            self.assertNotIn("You are an artifact triage analyst", agent, platform)
        self.assertNotIn("Wyjątek / exception", (ROOT / "LICENSE").read_text(encoding="utf-8"))


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
                  "structuralism", "content-analysis", "conversation-analysis", "systems-theory"):
            self.assertIn(f, t)
            self.assertTrue(list((ROOT / "method/prompts").rglob(f + ".md")), f)


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
            text = (ROOT / name).read_text(encoding="utf-8")
            with self.subTest(datei=name):
                self.assertIn(data["nummer"], text)
                self.assertIn(data["version"], text)

    def test_logo_present(self):
        self.assertTrue((ROOT / "design/logo" / "kaiwa-logo.svg").exists())
        for name in ("README.md", "1-start/setup.pl.md", "1-start/setup.en.md"):
            with self.subTest(datei=name):
                self.assertIn("design/logo/kaiwa-logo.svg", (ROOT / name).read_text(encoding="utf-8"))


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
        self.assertEqual(len(erster), 2 * (len(daten["zustaende"]) + len(themen["themen"])))
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
            if p.is_file():
                t = p.read_text(encoding="utf-8").lower()
                for w in ("onedrive", "sharepoint", "agent builder"):
                    self.assertNotIn(w, t, "%s: %s" % (p.name, w))

    def test_instruction_length(self):
        for a in self.AGENTS:
            t = (self.BASE / a / "INSTRUCTIONS.txt").read_text(encoding="utf-8")
            self.assertLessEqual(len(t), 8000, a)  # Copilot-Grenze als tragbare Obergrenze, ChatGPT nennt keine

    def test_project_files_complete(self):
        for a in self.AGENTS:
            for n in ("PROJECT.md", "INSTRUCTIONS.txt", "files.txt"):
                self.assertTrue((self.BASE / a / n).is_file(), "%s/%s" % (a, n))


if __name__ == "__main__":
    unittest.main()
