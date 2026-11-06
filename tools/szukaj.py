"""Szukanie literatury w otwartych katalogach: OpenAlex, Crossref, DOAJ. Tylko biblioteka standardowa Pythona.

Czesc pakietu KAIWA (Denis Pokropski, student, Uniwersytet Wroclawski, nr indeksu 285421,
kontakt 285421@student.uwr.edu.pl). Wersja robocza, nie wydana.

Uzycie:  python tools/szukaj.py "zapytanie" [--zrodla openalex,crossref,doaj] [--ile 10] [--csv wynik.csv]
Zasady (source-protocol.md):
  - Trafienie z katalogu to tylko metadane: poziom weryfikacji "aggregator-only", nic nie jest nosne,
    dopoki nie przeczytasz pelnego tekstu.
  - Brak trafien to nie dowod braku: wynik mowi, w ktorym katalogu, z jakim zapytaniem i kiedy nic nie znaleziono.
  - Kazde zrodlo ma wlasny status (ok, limit, robots, blad). Nic nie znika po cichu.
  - robots.txt: wyraznie zabroniona sciezka jest pomijana. Nieczytelny robots.txt nie blokuje.
  - Zaden adres e-mail w zapytaniu. OpenAlex: wlasny darmowy klucz w zmiennej OPENALEX_API_KEY (opcjonalnie).
Plik CSV ma kolumny arkusza "zrodla" z office/rejestry.xlsx.
Wynik 0 = co najmniej jedno zrodlo odpowiedzialo, 1 = zadne nie odpowiedzialo, 2 = bledne wywolanie.
"""
import argparse
import csv
import datetime
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

UA = "KAIWA-szukaj/0.1 (student research package)"
KOLUMNY = ["Źródło (autor, tytuł, rok)", "Link albo DOI", "Rodzaj źródła", "Poziom weryfikacji", "Sprawdzony atrybut",
           "Data sprawdzenia", "Cytat dosłowny", "Nośne w argumencie", "Uwagi"]


def adres(zrodlo, q, ile):
    s = urllib.parse.quote(q)
    if zrodlo == "openalex":
        u = "https://api.openalex.org/works?search=%s&per-page=%d" % (s, ile)
        key = os.environ.get("OPENALEX_API_KEY")
        return u + ("&api_key=" + urllib.parse.quote(key) if key else "")
    if zrodlo == "crossref":
        return "https://api.crossref.org/works?query=%s&rows=%d" % (s, ile)
    if zrodlo == "doaj":
        return "https://doaj.org/api/search/articles/%s?pageSize=%d" % (s, ile)
    raise ValueError(zrodlo)


def rekord(autorzy, tytul, rok, doi, link, zrodlo, oa=None):
    doi = (doi or "").lower().replace("https://doi.org/", "").strip() or None
    return {"autorzy": [a for a in autorzy if a][:3], "tytul": " ".join((tytul or "").split()), "rok": rok,
            "doi": doi, "link": link, "zrodlo": zrodlo, "oa": oa}


def z_openalex(d):
    out = []
    for w in d.get("results", []):
        oa = w.get("open_access") or {}
        out.append(rekord([(a.get("author") or {}).get("display_name") for a in w.get("authorships", [])],
                          w.get("display_name"), w.get("publication_year"), w.get("doi"),
                          oa.get("oa_url") or (w.get("primary_location") or {}).get("landing_page_url"),
                          "openalex", oa.get("is_oa")))
    return out


def z_crossref(d):
    out = []
    for w in (d.get("message") or {}).get("items", []):
        rok = ((w.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        autorzy = [" ".join(x for x in (a.get("given"), a.get("family")) if x) for a in w.get("author", [])]
        out.append(rekord(autorzy, (w.get("title") or [""])[0], rok, w.get("DOI"), w.get("URL"), "crossref"))
    return out


def z_doaj(d):
    out = []
    for r in d.get("results", []):
        b = r.get("bibjson") or {}
        doi = next((i.get("id") for i in b.get("identifier", []) if i.get("type") == "doi"), None)
        link = next((l.get("url") for l in b.get("link", []) if l.get("url")), None)
        rok = int(b["year"]) if str(b.get("year", "")).isdigit() else b.get("year")
        out.append(rekord([a.get("name", "").strip() for a in b.get("author", [])], b.get("title"), rok, doi, link,
                          "doaj", True))
    return out


PARSERY = {"openalex": z_openalex, "crossref": z_crossref, "doaj": z_doaj}


def robots_pozwala(url, pobierz):
    u = urllib.parse.urlsplit(url)
    try:
        tekst = pobierz("%s://%s/robots.txt" % (u.scheme, u.netloc))
    except Exception:
        return True                      # nieczytelny robots.txt nie blokuje
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(tekst.splitlines())
    return rp.can_fetch(UA, url)


def pobierz_http(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8")


def szukaj(zrodlo, q, ile, pobierz=pobierz_http, czekaj=time.sleep):
    url = adres(zrodlo, q, ile)
    if not robots_pozwala(url, pobierz):
        return [], "robots: ścieżka zabroniona w robots.txt"
    for proba in (1, 2):
        try:
            return PARSERY[zrodlo](json.loads(pobierz(url))), "ok"
        except urllib.error.HTTPError as e:
            if e.code == 429 and proba == 1:
                czekaj(min(15, int(e.headers.get("Retry-After") or 10) if e.headers else 10))
                continue
            return [], "limit (HTTP 429)" if e.code == 429 else "błąd HTTP %d" % e.code
        except Exception as e:
            return [], "błąd: %s" % type(e).__name__
    return [], "limit (HTTP 429)"


def bez_powtorzen(rekordy):
    widziane, out = set(), []
    for r in rekordy:
        k = r["doi"] or (re.sub(r"\W+", " ", r["tytul"].lower()).strip(), r["rok"])
        if k in widziane:
            continue
        widziane.add(k)
        out.append(r)
    return out


def wiersz_csv(r, q, dzien):
    opis = "%s, %s, %s" % ("; ".join(r["autorzy"]) or "brak autora", r["tytul"] or "brak tytułu", r["rok"] or "b.r.")
    link = ("https://doi.org/" + r["doi"]) if r["doi"] else (r["link"] or "")
    uwagi = "znalezione w %s, zapytanie „%s”, %s" % (r["zrodlo"], q, dzien) + (", otwarty dostęp" if r["oa"] else "")
    return [opis, link, "", "aggregator-only", "", dzien, "", "nie", uwagi]


def main(argv=None, pobierz=pobierz_http, czekaj=time.sleep, dzien=None):
    ap = argparse.ArgumentParser(description="Szukanie w OpenAlex, Crossref i DOAJ")
    ap.add_argument("zapytanie")
    ap.add_argument("--zrodla", default="openalex,crossref,doaj")
    ap.add_argument("--ile", type=int, default=10)
    ap.add_argument("--csv")
    a = ap.parse_args(argv)
    zrodla = [z.strip() for z in a.zrodla.split(",") if z.strip()]
    if any(z not in PARSERY for z in zrodla) or not 1 <= a.ile <= 50:
        print("znane źródła: openalex, crossref, doaj, --ile od 1 do 50")
        return 2
    dzien = dzien or datetime.date.today().isoformat()
    wszystkie, odpowiedzialo = [], 0
    for z in zrodla:
        rek, status = szukaj(z, a.zapytanie, a.ile, pobierz, czekaj)
        if status == "ok":
            odpowiedzialo += 1
            if not rek:
                status = "ok, w %s z zapytaniem „%s” dnia %s nic nie znaleziono" % (z, a.zapytanie, dzien)
        print("%s: %s, %d trafień" % (z, status, len(rek)))
        wszystkie += rek
    wynik = bez_powtorzen(wszystkie)
    for i, r in enumerate(wynik, 1):
        print("%2d. %s" % (i, wiersz_csv(r, a.zapytanie, dzien)[0]))
    if a.csv:
        with open(a.csv, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(KOLUMNY)
            for r in wynik:
                w.writerow(wiersz_csv(r, a.zapytanie, dzien))
        print("zapisano: %s (%d wierszy, poziom weryfikacji aggregator-only)" % (a.csv, len(wynik)))
    return 0 if odpowiedzialo else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
