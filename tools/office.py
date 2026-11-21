"""Builds office/rejestry.xlsx: the protocols of the package as Excel registers, usable without AI.

Part of the KAIWA package by Denis Pokropski (student, University of Wroclaw, contact 285421@student.uwr.edu.pl). Draft, not yet released.

Each sheet operationalises one protocol from protokoly/ (CC BY-SA 4.0, author Denis Pokropski):
  zrodla          source-protocol.md  sections 2, 3, 5 (source kind, verification level, verified attribute)
  pochodzenie     provenance-protocol.md section 2.1 and 3 (markers [H] [AI] [AI+] [H+AI], learned or scaffolded)
  decyzje         interpretive-frame-protocol.md sections 2.3 and 3 (coding-decision log, operation declaration)
  przed_publikacja writing-protocol.md section 3 and actant-self-check.md section 2 (six re-check steps)
  falsyfikacja    falsification-protocol.md section 3 (operational tests OT-1 to OT-10)
  narzedzie       no protocol of the package. Tool, model and computational effort of each AI-assisted session, by
                  analogy with the Leiden Declaration (Zenodo 20302944, 2 June 2026), Recommendation 01 "Disclose tool use".
                  The Declaration addresses mathematics, for this package it is an analogy only.
Run:  python tools/office.py   (needs openpyxl)
"""
import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "office" / "rejestry.xlsx"
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
    ("narzedzie", "Narzędzie (bez protokołu, analogia do Leiden Declaration, Recommendation 01 „Disclose tool use“). Jeden wiersz na sesję "
                  "z AI. Model wpisz tak, jak podaje czat, i zaznacz skąd to wiesz. Czego nie wiesz, zostaje „nieznane“. "
                  "Copilot i darmowe czaty zwykle nie pokazują tokenów, a model może podać swoją wersję błędnie.",
     [("Data", None, 12), ("Narzędzie (platforma i agent)", None, 34), ("Model", None, 24),
      ("Skąd nazwa modelu", "model_zrodlo", 20), ("Uruchomienia kodu", None, 12), ("Czas sesji (min)", None, 12),
      ("Nakład obliczeniowy (tokeny, jeśli widoczne)", None, 24), ("Do czego użyte", None, 30), ("Uwagi", None, 30)], []),
]


def build(path=OUT):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook()
    wb.properties.creator = "KAIWA (Denis Pokropski)"
    wb.properties.created = FIXED
    wb.properties.modified = FIXED
    for name, note, cols, rows in SHEETS:
        ws = wb.create_sheet(name)
        ws.append([note])
        ws["A1"].font = Font(italic=True)
        ws.append([c[0] for c in cols])
        for cell in ws[2]:
            cell.font = Font(bold=True)
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
        ws.freeze_panes = "A3"
    del wb["Sheet"]
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    return path


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(build())
