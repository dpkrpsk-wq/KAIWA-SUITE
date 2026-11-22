# Projekt „KAIWA: analiza”, pola do wklejenia (Claude)

Projekt w Claude (Projects, claude.ai, aplikacja desktop niesprawdzona). Wersja robocza, nieprzetestowana w Claude. Konfiguracja: `2-agents/claude/setup.pl.md`.

## Nazwa projektu

KAIWA: analiza

## Opis (dla ciebie, Claude go nie wymaga)

Analiza artefaktu metodą deklarowanych ram: najpierw triaż, potem wybór dalszego kroku (dalej, komentarz albo problem badawczy), potem język wyniku i kontekst kulturowy, potem analiza według dołączonych plików ram, na końcu blok „Kontrola kulturowa”. Przetwarza po angielsku, wynik podaje w wybranym języku. Artefact analysis with declared frameworks: triage, next step, output language, then framework analysis.

## Instrukcje projektu (Set project instructions)

Cała zawartość pliku `2-agents/claude/analysis/INSTRUCTIONS.txt`.

## Pliki projektu (8, wiedza projektu / project knowledge)

1. `method/prompts/core/artifact-triage.md`
2. `method/prompts/framework-catalog.md`
3. `3-templates/after-triage.pl.md`
4. `3-templates/cultural-check.pl.md`
5. `3-templates/research-problem-card.pl.md`
6. `3-templates/tool-disclosure.pl.md`
7. `method/protocols/interpretive-frame-protocol.md` (do kontroli kulturowej / for the cultural check)
8. `method/protocols/actant-self-check.md` (do kontroli kulturowej / for the cultural check)

Ta sama lista w `files.txt`.

## Pierwsza wiadomość w nowej rozmowie

```text
start. Dołączam artefakt: <plik albo tekst>.
```

## Co dołączasz w rozmowie

Artefakt oraz po triażu pliki ram z `method/prompts/cultural-scientific/` albo `method/prompts/social-science/`, które poleca triaż.
