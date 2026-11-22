# Projekt „KAIWA: strumień świadomości”, pola do wklejenia (ChatGPT)

Projekt w ChatGPT (Projects). Wersja robocza, nieprzetestowana w ChatGPT. Konfiguracja: `2-agents/chatgpt/setup.pl.md`.

## Nazwa projektu

KAIWA: strumień świadomości

## Opis (dla ciebie, ChatGPT go nie wymaga)

Zapisuje strumień świadomości bez przerywania. Mówisz albo piszesz swobodnie, agent zapisuje każdą myśl dosłownie i nie zadaje pytań. Na koniec zapisuje plik Excel z wpisami i z rejestrem skrótów SHA-256, który pokazuje później, czy tekst się nie zmienił. Records a stream of consciousness without interruption and saves an Excel file with the entries and a SHA-256 register.

## Instrukcje projektu (Project settings)

Cała zawartość pliku `2-agents/chatgpt/stream/INSTRUCTIONS.txt`.

## Pliki projektu (1, jedno wgranie)

1. `3-templates/tool-disclosure.pl.md`

Ta sama lista w `files.txt`.

## Pierwsza wiadomość w nowej rozmowie

```text
start
```

## Co dołączasz w rozmowie

Nic. Agent tworzy plik `dictation-RRRR-MM-DD-GGMM.xlsx`, który pobierasz.
