# Ujawnienie narzędzia: platforma, model, nakład

Szablon z pakietu KAIWA, produkt 26.01, wersja 0.2.0 (robocza), 05.11.2026.

Znacznik pochodzenia (`method/protocols/provenance-protocol.md`) mówi, czy myśl pochodzi od człowieka czy od AI. Nie mówi, jakie narzędzie i jaki model brały udział ani jaki był nakład obliczeniowy. Ten szablon dodaje te dane. Jest analogią do Leiden Declaration (Zenodo 20302944, 02.06.2026), rekomendacja „Disclose tool use“ (https://leidendeclaration.ai/, dostęp 22.11.2026). Deklaracja dotyczy matematyki, dla pakietu to tylko wzór.

## Pola

1. **Narzędzie**: platforma i agent, na przykład Microsoft 365 Copilot Chat i agent „KAIWA: analiza“.
2. **Model**: tylko tak, jak podaje czat, albo wpisany przez ciebie.
3. **Skąd nazwa modelu**: „wg czatu“, „wpisane przez osobę“ albo „nieznane“.
4. **Data.**
5. **Uruchomienia kodu**: liczba w rozmowie. Agent strumienia uruchamia kod dwa razy, agent analizy zwykle wcale.
6. **Czas sesji** w minutach, jeśli go znasz.
7. **Nakład obliczeniowy**: tokeny, tylko gdy platforma je pokazuje.

Czego nie wiadomo, zostaje „nieznane“ (po angielsku „unknown“). Pole nie jest wymyślane.

## Gdzie te pola trafiają

1. Agent „strumień świadomości“: arkusz „tool“ w pliku `dictation-RRRR-MM-DD-GGMM.xlsx`, obok arkuszy „entries“ i „register“.
2. Agenci „analiza“ i „źródła“: wiersz „Narzędzie“ na końcu wyniku.
3. Excel bez AI: arkusz „narzedzie“ w `4-without-ai/registers.xlsx`, jeden wiersz na sesję.
4. W pracy zaliczeniowej: zdanie albo krótka sekcja w stylu „Użyłem narzędzia X, model Y (według czatu), dnia Z.“ Zasady uczelni i prowadzącego mają pierwszeństwo przed tym szablonem.

## Jak sprawdzić (lista dla studenta albo prowadzącego)

1. Czy wiersz albo arkusz jest i ma wszystkie pola, w razie braku z „nieznane“?
2. Czy przy modelu stoi, skąd wiadomo, jak się nazywa?
3. Czy liczba uruchomień kodu zgadza się z tym, co widać w rozmowie? Pokazuje to historia czatu.
4. Czy w polu nakładu stoją liczby tylko wtedy, gdy platforma je pokazywała?

## Tekst do wklejenia (droga zapasowa)

```text
At the very end of your answer add one line "Tool": platform and agent, model (only as the chat itself states it, or "entered by user", otherwise "unknown"), date, number of code runs in this conversation, computational effort (tokens, only if the platform shows them, otherwise "unknown"). Never give a model name from your memory of what you are. Never invent a version or a token count.
```

## Granice

1. Copilot i darmowe czaty zwykle nie pokazują tokenów (niesprawdzone). Pole nakładu zostaje wtedy „nieznane“.
2. Model może podać swoją wersję błędnie. Nazwa „wg czatu“ jest informacją o tym, co czat powiedział, nie dowodem.
3. Arkusz „tool“ nie ma skrótu SHA-256. Wpis można zmienić ręcznie i nic tego nie pokaże. Skrót w arkuszu „register“ dotyczy tylko wpisów dyktatu.
4. Czas sesji agent zna tylko wtedy, gdy mu go podasz.
