# Sprawdzenie mapy / map check (KAIWA, mapa kontekstu)

KAIWA SUITE 26.01, wersja 0.2.2 (robocza / draft), 22.11.2026. Plik projektu „KAIWA: mapa kontekstu” (Claude). Kod dla polecenia „sprawdź mapę”. Używa funkcji h, bledy i wiersze z bloku startowego instrukcji projektu. W PLIK wpisz ścieżkę dołączonego pliku mapy. / Code for the command “sprawdź mapę”. It uses the functions h, bledy and wiersze from the start block of the project instructions. Put the path of the attached map file into PLIK.

```python
import openpyxl
PLIK = "mapa.xlsx"
wb = openpyxl.load_workbook(PLIK)
def arkusz(n):
    return list(wb[n].iter_rows(min_row=2, values_only=True)) if n in wb.sheetnames else []
T, P, C = arkusz("tematy"), arkusz("połączenia"), arkusz("cele")
b = bledy(T, P, C)
b += ["brak arkusza: " + n for n in ("tematy", "połączenia", "cele", "rejestr") if n not in wb.sheetnames]
reg = {(str(r[0]), str(r[1])): str(r[2]) for r in arkusz("rejestr") if r and r[0]}
for a, i, tekst in wiersze(T, P, C):
    if reg.pop((a, i), None) != h(tekst):
        b.append("%s %s: zmieniony od zapisu albo nowy" % (a, i))
b += ["%s %s: usunięty od zapisu" % k for k in sorted(reg)]
print("\n".join(b) if b else "MAPA OK")
```
