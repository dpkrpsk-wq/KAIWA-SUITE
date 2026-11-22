"""Builds 4-without-ai/registers.xlsx: the protocols of the package as Excel registers, usable without AI.

Part of the KAIWA package by Denis Pokropski (student, University of Wroclaw, contact 285421@student.uwr.edu.pl). Draft, not yet released.

Each sheet operationalises one protocol from method/protocols/ (CC BY-SA 4.0, author Denis Pokropski):
  zrodla          source-protocol.md  sections 2, 3, 5 (source kind, verification level, verified attribute)
  pochodzenie     provenance-protocol.md section 2.1 and 3 (markers [H] [AI] [AI+] [H+AI], learned or scaffolded)
  decyzje         interpretive-frame-protocol.md sections 2.3 and 3 (coding-decision log, operation declaration)
  przed_publikacja writing-protocol.md section 3 and actant-self-check.md section 2 (six re-check steps)
  falsyfikacja    falsification-protocol.md section 3 (operational tests OT-1 to OT-10)
  narzedzie       no protocol of the package. Tool, model and computational effort of each AI-assisted session, by
                  analogy with the Leiden Declaration (Zenodo 20302944, 2 June 2026), the recommendation "Disclose tool use".
                  The Declaration addresses mathematics, for this package it is an analogy only.
Run:  python tools/office.py   (needs openpyxl)
"""
import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "4-without-ai" / "registers.xlsx"
OUT_WORD = ROOT / "4-without-ai" / "kaiwa-template.docx"
# Farben und Schrift aus design/design-system/tokens.css (KAIWA SUITE). Space Grotesk liegt in design/fonts,
# warp steht im Font-Stack, eine Datei dafür gibt es nicht. Ohne installierte Schrift ersetzt Office sie.
TINTE, PAPIER, SIGNAL, GEDAEMPFT, LINIE, HINWEIS, ENTWURF = "14171F", "F1EFE9", "FFED00", "4A4F5A", "7C796F", "E6E2D4", "8A3B12"
SCHRIFT = "Space Grotesk"
FIXED = datetime.datetime(2026, 11, 5, 0, 0, 0)

LISTS = {
    "rodzaj": ["pierwotne", "wtórne", "trzeciorzędne"],
    "poziom": ["deep-read", "abstract", "agent-reported", "aggregator-only"],
    "atrybut": ["istnienie", "brzmienie", "data", "status", "liczba"],
    "tak_nie": ["tak", "nie"],
    "znacznik": ["[H]", "[AI]", "[AI+]", "[H+AI]"],
    "nauka": ["nauczone (learned)", "rusztowanie (scaffolded)", "jeszcze nie oceniono"],
    "model_zrodlo": ["wg czatu", "wpisane przez osobę", "nieznane"],
}

SHEETS = [
    ("zrodla", "Źródła (source-protocol.md, sekcje 2, 3, 5). Przed syntezą każdy wpis agent-reported albo "
               "aggregator-only podnieś do deep-read albo usuń z argumentów nośnych.",
     [("Źródło (autor, tytuł, rok)", None, 36), ("Link albo DOI", None, 30), ("Rodzaj źródła", "rodzaj", 16),
      ("Poziom weryfikacji", "poziom", 18), ("Sprawdzony atrybut", "atrybut", 18), ("Data sprawdzenia", None, 16),
      ("Cytat dosłowny", None, 40), ("Nośne w argumencie", "tak_nie", 14), ("Uwagi", None, 30)], []),
    ("pochodzenie", "Pochodzenie (provenance-protocol.md, sekcje 2.1 i 3). Znacznik przy pierwszym wprowadzeniu i przy "
                    "każdym przepisaniu. W razie wątpliwości ostrożniej: raczej [AI] niż [AI+], raczej [AI+] niż [H].",
     [("Data", None, 12), ("Pojęcie, twierdzenie albo krok metodyczny", None, 44), ("Znacznik", "znacznik", 10),
      ("Gdzie wprowadzone", None, 30), ("Nauczone czy rusztowanie", "nauka", 24), ("Uwagi", None, 30)], []),
    ("decyzje", "Decyzje kodowania (interpretive-frame-protocol.md, sekcje 2.3 i 3). Dla każdej decyzji: termin, "
                "alternatywy, uzasadnienie, nazwa operacji i to, czego operacja nie daje.",
     [("Data", None, 12), ("Element", None, 24), ("Użyty termin", None, 20), ("Rozważone alternatywy", None, 30),
      ("Uzasadnienie", None, 36), ("Operacja", None, 24), ("Czego operacja nie daje", None, 30)], []),
    ("przed_publikacja", "Przed publikacją (writing-protocol.md, sekcja 3, actant-self-check.md, sekcja 2). "
                         "Sześć kroków jako osobny etap, nie jako ogólna korekta.",
     [("Krok", None, 30), ("Co sprawdzasz", None, 44), ("Wobec czego", None, 34), ("Zrobione", "tak_nie", 10),
      ("Data", None, 12), ("Uwagi", None, 30)],
     [["Kontrola źródeł (source re-check)", "każdy cytat i każde przywołane twierdzenie", "oryginał źródła, nie wcześniejszy szkic"],
      ["Kontrola artefaktu (artefact re-check)", "każde twierdzenie „to pokazuje X“", "sam artefakt, nie jego widok w narzędziu"],
      ["Lektura w innym formacie (composition self-read)", "tekst w wersji do publikacji", "świeżo wygenerowana wersja w innym formacie niż edytor"],
      ["Audyt czasowników (verb audit)", "czasowniki, które przypisują działanie albo winę", "to, co aktor rzeczywiście zrobił"],
      ["Audyt adresata (addressee audit)", "do kogo mówi tekst, kto jest „my“, kto „oni“", "zamierzona publiczność"],
      ["Ochrona przed ramą dyskredytującą (discrediting-frame inoculation)", "miejsca, które łatwo odczytać jako atak", "możliwe odczytania krytyków"]]),
    ("falsyfikacja", "Testy falsyfikacji (falsification-protocol.md, sekcja 3). W razie wątpliwości "
                     "rozstrzyga oryginał w protokole.",
     [("Test", None, 10), ("Pytanie", None, 70), ("Odpowiedź", None, 50), ("Data", None, 12)],
     [["OT-1", "Co sfalsyfikowałoby to nośne twierdzenie?"],
      ["OT-2", "Czy twierdzenie ma formę ogólną? Jeśli tak, czy brzmi „sprawdzone w N przypadkach, falsyfikowalne przez Z“?"],
      ["OT-3", "Czy dodana reguła albo poprawka zwiększa to, czego metoda zabrania?"],
      ["OT-4", "Czy wykonano ratunek ad hoc? Jeśli tak, czy sprawdzono cały system, a nie tylko poprawkę?"],
      ["OT-5", "Czy zmiana metody opiera się na jednym błędzie czy na powtarzalnym wzorze?"],
      ["OT-6", "Czy dla każdego nośnego twierdzenia jest odpowiedź na pytanie „jak to jest testowane?“, a nie tylko „na czym to się opiera?“"],
      ["OT-7", "Czy etykiety „stabilne“, „kanoniczne“, „ostateczne“ mają podane warunki falsyfikacji?"],
      ["OT-8", "Czy bramka walidacji (klucz odniesienia, zestaw przeciwny) była ustalona przed obejrzeniem danych?"],
      ["OT-9", "Czy trudność materiału testowego jest zadeklarowana i zróżnicowana (co najmniej 2 poziomy) albo wniosek zawężony?"],
      ["OT-10", "Czy bramka zawiera te same treści z przełączoną tylko badaną cechą (para minimalna)?"]]),
    ("narzedzie", "Narzędzie (bez protokołu, analogia do Leiden Declaration, rekomendacja „Disclose tool use“). Jeden wiersz na sesję "
                  "z AI. Model wpisz tak, jak podaje czat, i zaznacz skąd to wiesz. Czego nie wiesz, zostaje „nieznane“. "
                  "Copilot i darmowe czaty zwykle nie pokazują tokenów, a model może podać swoją wersję błędnie.",
     [("Data", None, 12), ("Narzędzie (platforma i agent)", None, 34), ("Model", None, 24),
      ("Skąd nazwa modelu", "model_zrodlo", 20), ("Uruchomienia kodu", None, 12), ("Czas sesji (min)", None, 12),
      ("Nakład obliczeniowy (tokeny, jeśli widoczne)", None, 24), ("Do czego użyte", None, 30), ("Uwagi", None, 30)], []),
]


def build(path=OUT):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook()
    wb.properties.creator = "KAIWA (Denis Pokropski)"
    wb.properties.created = FIXED
    wb.properties.modified = FIXED
    for name, note, cols, rows in SHEETS:
        ws = wb.create_sheet(name)
        ws.append([note])
        ws["A1"].font = Font(name=SCHRIFT, italic=True, color=GEDAEMPFT, size=10)
        ws.append([c[0] for c in cols])
        for cell in ws[2]:
            cell.font = Font(name=SCHRIFT, bold=True, color=PAPIER, size=10)
            cell.fill = PatternFill("solid", fgColor=TINTE)
            cell.border = Border(bottom=Side(style="thick", color=SIGNAL))
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        for r in rows:
            ws.append(r)
        for i, (_, lst, width) in enumerate(cols):
            letter = ws.cell(row=2, column=i + 1).column_letter
            ws.column_dimensions[letter].width = width
            if lst:
                dv = DataValidation(type="list", formula1='"%s"' % ",".join(LISTS[lst]), allow_blank=True)
                ws.add_data_validation(dv)
                dv.add("%s3:%s500" % (letter, letter))
        for row in ws.iter_rows(min_row=3):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
                cell.font = Font(name=SCHRIFT, color=TINTE, size=10)
                cell.border = Border(bottom=Side(style="thin", color=LINIE))
        ws.sheet_properties.tabColor = TINTE
        ws.freeze_panes = "A3"
    del wb["Sheet"]
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return path


def build_word(path=OUT_WORD):
    """Word-Vorlage mit Formatvorlagen der KAIWA SUITE: Kopfzeile mit Produkt und Entwurfsmarke,
    Fußzeile mit Commit-Platzhalter und Seitenzahl, Absatz- und Tabellenformate in Farben und Schrift des Systems."""
    import json
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Mm, Pt, RGBColor

    produkt = json.loads((ROOT / "product.json").read_text(encoding="utf-8"))
    rgb = lambda h: RGBColor.from_string(h)
    doc = Document()
    cp = doc.core_properties
    cp.author = "KAIWA (Denis Pokropski)"
    cp.title = "KAIWA SUITE %s, wersja %s" % (produkt["nummer"], produkt["version"])
    cp.created = cp.modified = FIXED
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Mm(210), Mm(297)
    sec.left_margin = sec.right_margin = Mm(16)
    sec.top_margin, sec.bottom_margin = Mm(18), Mm(22)

    def schrift(style, groesse, farbe=TINTE, fett=False, versal=False):
        f = style.font
        f.name, f.size, f.bold, f.all_caps = SCHRIFT, Pt(groesse), fett, versal
        f.color.rgb = rgb(farbe)
        rpr = style.element.get_or_add_rPr()
        fonts = rpr.find(qn("w:rFonts"))
        if fonts is None:
            fonts = OxmlElement("w:rFonts")
            rpr.append(fonts)
        for k in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            fonts.set(qn(k), SCHRIFT)

    st = doc.styles
    schrift(st["Normal"], 10.5)
    st["Normal"].paragraph_format.space_after = Pt(6)
    st["Normal"].paragraph_format.line_spacing = 1.3
    schrift(st["Title"], 26, fett=True, versal=True)
    schrift(st["Heading 1"], 16, fett=True)
    schrift(st["Heading 2"], 12.5, fett=True)
    schrift(st["Heading 3"], 11, fett=False)
    schrift(st["Caption"], 8.5, farbe=GEDAEMPFT)
    for name, farbe in (("Hinweis", TINTE), ("Do sprawdzenia", ENTWURF)):
        s_ = st.add_style(name, 1)
        s_.base_style = st["Normal"]
        schrift(s_, 10, farbe=farbe)
        ppr = s_.element.get_or_add_pPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear"), shd.set(qn("w:color"), "auto"), shd.set(qn("w:fill"), HINWEIS)
        ppr.append(shd)

    def feld(run, code):
        for typ, text in (("begin", None), (None, code), ("end", None)):
            if typ:
                e = OxmlElement("w:fldChar")
                e.set(qn("w:fldCharType"), typ)
            else:
                e = OxmlElement("w:instrText")
                e.set(qn("xml:space"), "preserve")
                e.text = text
            run._r.append(e)

    kopf = sec.header.paragraphs[0]
    r = kopf.add_run("%s %s" % (produkt["name"], produkt.get("suite", "")))
    r.bold, r.font.size, r.font.color.rgb = True, Pt(11), rgb(TINTE)
    r = kopf.add_run("   %s · wersja %s   " % (produkt["nummer"], produkt["version"]))
    r.font.size, r.font.color.rgb = Pt(9), rgb(GEDAEMPFT)
    if produkt["version"].startswith("0."):
        r = kopf.add_run(" WERSJA ROBOCZA / DRAFT ")
        r.bold, r.font.size, r.font.color.rgb = True, Pt(8), rgb(TINTE)
        r.font.highlight_color = 7  # gelb, nächster Ton zu signal
    fuss = sec.footer.paragraphs[0]
    r = fuss.add_run("KAIWA · %s · wersja %s · commit ⟨commit⟩ · strona " % (produkt["nummer"], produkt["version"]))
    r.font.size, r.font.color.rgb = Pt(8), rgb(GEDAEMPFT)
    r = fuss.add_run()
    r.font.size = Pt(8)
    feld(r, "PAGE")
    fuss.alignment = WD_ALIGN_PARAGRAPH.LEFT

    doc.add_paragraph("Tytuł dokumentu / document title", style="Title")
    doc.add_paragraph("Nagłówek 1 / heading 1", style="Heading 1")
    doc.add_paragraph("Tekst. Zażółć gęślą jaźń.", style="Normal")
    doc.add_paragraph("Uwaga / note: hinweis.", style="Hinweis")
    doc.add_paragraph("Do sprawdzenia / to be checked.", style="Do sprawdzenia")
    t = doc.add_table(rows=2, cols=3)
    for i, txt in enumerate(("Fragment", "Pochodzenie / provenance", "Sprawdzenie / check")):
        c = t.rows[0].cells[i]
        c.text = txt
        run = c.paragraphs[0].runs[0]
        run.bold, run.font.color.rgb, run.font.size = True, rgb(PAPIER), Pt(9)
        tcpr = c._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear"), shd.set(qn("w:color"), "auto"), shd.set(qn("w:fill"), TINTE)
        tcpr.append(shd)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)
    return path


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(build())
    try:
        print(build_word())
    except ImportError:
        print("python-docx fehlt, Word-Vorlage nicht gebaut")
