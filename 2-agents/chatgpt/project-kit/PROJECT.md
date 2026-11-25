# Projekt-Set dla ChatGPT: KAIWA w każdym projekcie tematycznym / project kit for ChatGPT

Część pakietu KAIWA, produkt 26.01, wersja 0.2.1 (robocza), 25.11.2026. Wersja robocza, nieprzetestowana w ChatGPT.

Wtyczka KAIWA Suite działa w każdym czacie konta, także w projektach. Projekt-Set dodaje to, czego wtyczka nie niesie: stały stan tematu. Każdy projekt tematyczny (na przykład „Konie” i „Misie żelki”) dostaje te same pliki i te same instrukcje, ale ma własny stan, własne mapy i własne rozmowy. / The plugin works in every chat of the account, also in projects. The kit adds the lasting state of a topic. Each topic project gets the same files and instructions and keeps its own state.

## Przed pierwszym użyciem

1. Zainstaluj wtyczkę `KAIWA-SUITE-chatgpt-plugin-<wersja>.zip` jednorazowo dla konta (Plugins, dodaj, prześlij archiwum wtyczki).
2. Rozpakuj `KAIWA-SUITE-chatgpt-project-kit-<wersja>.zip`. Powstają pliki obok siebie, bez podfolderów.

## Dla każdego nowego projektu tematycznego

1. W ChatGPT: nowy projekt, nazwa twojego tematu.
2. W ustawieniach projektu (Project settings, Instructions) wklej całą zawartość pliku `INSTRUCTIONS.txt`.
3. Wgraj jednym wgraniem trzy pliki: `registers.xlsx`, `kaiwa-template.docx`, `README.pl.md`.
4. Nowa rozmowa w projekcie. Wybierz KAIWA Suite w polu rozmowy (znak plus albo @) i napisz słowo startu.

## Pierwsza wiadomość w rozmowie

```text
start. Moduł: <analiza, mapa kontekstu, źródła albo strumień świadomości>. Obowiązujący plik mapy: <nazwa pliku albo „nowa mapa”>.
```

## Zapis stanu

ChatGPT nie zmienia plików projektu. Po rozmowie z mapą, dyktatem albo rejestrem pobierz nowy plik i podmień go w projekcie ręcznie: usuń stary plik, wgraj nowy. Stan tematu to pliki projektu. Dwa projekty nie dzielą stanu. / ChatGPT does not change project files. Download the new file and replace the old one by hand.

## Drugi temat

Utwórz drugi projekt i powtórz cztery kroki z tymi samymi plikami. Nic z pierwszego projektu nie przechodzi do drugiego, poza wtyczką, która jest w koncie.

## Czego Projekt-Set nie zawiera

Skryptów z folderu `tools/`: wyszukiwanie `search.py` potrzebuje sieci, której Python w ChatGPT nie ma, archiwum dyktatów `dictation_ledger.py` prowadzi archiwum na twoim komputerze. Używasz ich lokalnie z pełnym pakietem. Sprawdzenie mapy i skrót SHA-256 dyktatu są w skillach wtyczki. / The scripts need your own computer, see the full package.

## Lista plików projektu

Ta sama lista w `files.txt` (ścieżki w pełnym pakiecie). W ZIP pliki leżą obok siebie:

1. `registers.xlsx`
2. `kaiwa-template.docx`
3. `README.pl.md`
