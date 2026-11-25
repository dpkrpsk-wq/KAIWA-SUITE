# Protokoły w Word i Excel, bez AI

Część pakietu KAIWA, produkt 26.01, wersja 0.2.1 (robocza), 22.11.2026.

Protokoły z folderu `method/protocols/` (po angielsku, CC BY-SA 4.0) opisują, jak pracować z AI odpowiedzialnie: skąd pochodzi myśl, jak dobrze sprawdzone jest źródło, co sprawdzić przed publikacją. Ten folder pozwala stosować je także wtedy, gdy agenci Copilot nie działają albo gdy pracujesz bez AI.

## Kolejność dróg

1. **Agenci z pakietu.** Pełna droga, opisana w konfiguracji twojego dostawcy: Copilot `1-start/setup.pl.md`, Gemini `2-agents/gemini/setup.pl.md`, ChatGPT `2-agents/chatgpt/setup.pl.md`, Claude `2-agents/claude/setup.pl.md`.
2. **Dowolny asystent AI.** Prompty i protokoły są niezależne od modelu. Wklej albo dołącz plik i tekst z `3-templates/after-triage.pl.md`.
3. **Word i Excel bez AI.** Rejestry poniżej i protokoły do czytania w `method/protocols/`.

## Plik `registers.xlsx`

Pięć arkuszy przenosi po jednym protokole do tabeli, szósty zapisuje narzędzie. Pola z listą wyboru przyjmują tylko słowa z protokołu.

1. **zrodla** (source-protocol): źródło, link albo DOI, rodzaj (pierwotne, wtórne, trzeciorzędne), poziom weryfikacji (deep-read: przeczytane przez ciebie w całości, abstract: tylko streszczenie, agent-reported: streszczone przez asystenta, aggregator-only: tylko wpis w katalogu), sprawdzony atrybut (istnienie, brzmienie, data, status, liczba), data, cytat dosłowny, czy źródło jest nośne. Przed syntezą wpisy agent-reported i aggregator-only podnosisz do deep-read albo usuwasz z argumentów nośnych.
2. **pochodzenie** (provenance-protocol): pojęcie albo twierdzenie, znacznik [H] (twoje), [AI] (wprowadzone przez AI), [AI+] (twoje, rozwinięte przez AI), [H+AI] (wspólne), miejsce wprowadzenia, czy pojęcie jest już nauczone czy jest rusztowaniem.
3. **decyzje** (interpretive-frame-protocol): dziennik decyzji kodowania, czyli termin, rozważone alternatywy, uzasadnienie, nazwa operacji analitycznej i to, czego ta operacja nie daje.
4. **przed_publikacja** (writing-protocol, actant-self-check): sześć kroków kontroli przed oddaniem tekstu, każdy z datą.
5. **falsyfikacja** (falsification-protocol): dziesięć pytań testowych OT-1 do OT-10. W razie wątpliwości rozstrzyga oryginał w protokole.
6. **narzedzie** (bez protokołu, `3-templates/tool-disclosure.pl.md`): jeden wiersz na sesję z AI, czyli data, narzędzie, model i skąd jego nazwa (wg czatu, wpisane przez osobę, nieznane), uruchomienia kodu, czas sesji, nakład obliczeniowy.

Arkusz tworzy skrypt `tools/office.py`, więc po zmianie protokołu można go zbudować od nowa.

## W Word

1. Znacznik pochodzenia wstaw jako komentarz przy akapicie: [H], [AI], [AI+] albo [H+AI].
2. Zmiany zaproponowane przez asystenta wklejaj w trybie śledzenia zmian. Widać wtedy, co przyjęte.
3. Przed oddaniem przejdź arkusz przed_publikacja, krok „lektura w innym formacie“ zrób na PDF, nie w edytorze.

## Mapa kontekstu bez AI

Plik mapy z agenta jest zwykłym plikiem Excel. Możesz go otwierać i uzupełniać ręcznie. Po ręcznej zmianie rejestr skrótów pokaże zmienione wiersze, dopóki agent nie zapisze mapy na nowo. Pochodzenie tematów w mapie odpowiada znacznikom z protokołu: własne to [H], własne+asystent to [AI+], asystent to [AI], sesja to [H+AI], niejasne traktuj ostrożnie jak [AI].
