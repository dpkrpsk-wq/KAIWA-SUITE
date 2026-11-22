# Projekt „KAIWA: źródła”, pola do wklejenia (ChatGPT)

Projekt w ChatGPT (Projects). Wersja robocza, nieprzetestowana w ChatGPT. Konfiguracja: `2-agents/chatgpt/setup.pl.md`.

## Nazwa projektu

KAIWA: źródła

## Opis (dla ciebie, ChatGPT go nie wymaga)

Szuka literatury naukowej w otwartym dostępie według protokołu źródeł: każde trafienie z poziomem weryfikacji, brak trafień zapisany jako brak w danym wyszukiwaniu, agent ma niczego nie wymyślać. Tabela pasuje do arkusza „zrodla” w Excel. Finds open access literature with a verification level for every hit.

## Instrukcje projektu (Project settings)

Cała zawartość pliku `2-agents/chatgpt/sources/INSTRUCTIONS.txt`.

## Pliki projektu (2, jedno wgranie)

1. `method/protocols/source-protocol.md`
2. `3-templates/tool-disclosure.pl.md`

Ta sama lista w `files.txt`.

## Pierwsza wiadomość w nowej rozmowie

```text
start. Temat poszukiwań: <temat w jednym zdaniu>.
```

## Co dołączasz w rozmowie

Nic na stałe. Tabelę trafień możesz przenieść do arkusza „zrodla” w `4-without-ai/registers.xlsx`.
