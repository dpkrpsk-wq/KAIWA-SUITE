# Projekt „KAIWA: analiza”, pola do wklejenia (ChatGPT)

Projekt w ChatGPT (Projects). Wersja robocza, nieprzetestowana w ChatGPT. Konfiguracja: `2-agents/chatgpt/setup.pl.md`.

## Nazwa projektu

KAIWA: analiza

## Opis (dla ciebie, ChatGPT go nie wymaga)

Analiza artefaktu metodą deklarowanych ram: najpierw triaż, potem wybór dalszego kroku (dalej, komentarz albo problem badawczy), potem język wyniku i kontekst kulturowy, potem analiza według dołączonych plików ram, na końcu blok „Kontrola kulturowa”. Przetwarza po angielsku, wynik podaje w wybranym języku. Artefact analysis with declared frameworks: triage, next step, output language, then framework analysis.

## Instrukcje projektu (Project settings)

Cała zawartość pliku `2-agents/chatgpt/analysis/INSTRUCTIONS.txt`.

## Pliki projektu (8, jedno wgranie)

1. `method/prompts/core/artifact-triage.md`
2. `method/prompts/framework-catalog.md`
3. `3-templates/after-triage.pl.md`
4. `3-templates/cultural-check.pl.md`
5. `3-templates/research-problem-card.pl.md`
6. `3-templates/tool-disclosure.pl.md`
7. `2-agents/chatgpt/analysis/SUIT-START-MENU.md` (menu startowe / start menu)
8. `2-agents/chatgpt/analysis/kaiwa-start-menu.png` (obraz menu / menu picture)

Ta sama lista w `files.txt`.

## Pierwsza wiadomość w nowej rozmowie

Dołącz artefakt (plik) i napisz:

```text
start
```

ChatGPT pokazuje najpierw menu startowe (obraz i menu tekstowe) i czeka na twój wybór. Słowa startu po polsku, angielsku i niemiecku: `SUIT-START-MENU.md`.

## Co dołączasz w rozmowie

Artefakt oraz po triażu pliki ram z `method/prompts/cultural-scientific/` albo `method/prompts/social-science/`, które poleca triaż.
