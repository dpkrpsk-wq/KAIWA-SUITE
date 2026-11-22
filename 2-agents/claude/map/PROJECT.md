# Projekt „KAIWA: mapa kontekstu”, pola do wklejenia (Claude)

Projekt w Claude (Projects, claude.ai w przeglądarce albo w aplikacji desktop). Wersja robocza, nieprzetestowana w Claude. Konfiguracja: `2-agents/claude/setup.pl.md`.

## Nazwa projektu

KAIWA: mapa kontekstu

## Opis (dla ciebie, Claude go nie wymaga)

Prowadzi mapę kontekstu: tematy z twoich dyktatów i notatek, ich pochodzenie, połączenia między nimi i twoje cele. Proponuje, wpisuje tylko to, co zatwierdzisz, i zapisuje plik Excel z rejestrem skrótów SHA-256. Mapa jest kontekstem, nie zbiorem reguł. Keeps a context map of topics, provenance, connections and goals from your dictations.

## Instrukcje projektu (Set project instructions)

Cała zawartość pliku `2-agents/claude/map/INSTRUCTIONS.txt`.

## Pliki projektu (2, wiedza projektu / project knowledge)

1. `1-start/context.pl.md`
2. `3-templates/tool-disclosure.pl.md`

Ta sama lista w `files.txt`.

## Pierwsza wiadomość w nowej rozmowie

```text
start. Obowiązujący plik mapy w tej sesji: <nazwa pliku albo „nowa mapa”>. Dołączam też pliki dyktatów: <nazwy>.
```

## Co dołączasz w rozmowie

Obowiązujący plik mapy (`mapa-….xlsx`) i pliki dyktatów (`dictation-….xlsx`) z bieżącej pracy. Po każdej zmianie pobierasz nowy plik mapy.
