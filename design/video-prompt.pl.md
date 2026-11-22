# KAIWA SUITE: blok do filmów 10 s (Gemini)

Ten tekst wklejasz do Gemini przy każdym filmie z serii. Część stała trzyma wygląd serii. Pole odcinka opisuje, co dzieje się w danym filmie. Wartości pochodzą z `design/design-system/tokens.css`, `design/logo/themes.json` i opisu logo w systemie KAIWA SUITE (Claude Design).

## Część stała (do wklejenia)

```text
Film 10 sekund, jedno ujęcie bez cięć, bez dźwięku mowy.
Format: 16:9, 1920 x 1080. Wariant pionowy: 9:16, 1080 x 1920.

Styl: płaska grafika, ostre krawędzie, twarde kształty. Bez gradientów, bez rozmycia, bez miękkich cieni, bez efektów świetlnych, bez faktury. Cień tylko jako twarde przesunięcie 6 px w prawo w dół, w kolorze tekstu.

Kolory (hex), tylko te:
tło #F1EFE9 (papier) albo #14171F (tinte),
kształty i linie #14171F na jasnym tle, #F1EFE9 na ciemnym tle,
sygnał #FFED00 (żółty) tylko jako pasy i plamy, nigdy jako tło całego kadru,
rdzeń tunelu #07080C,
zielony stan #3FB97A tylko w małym kwadracie w prawym dolnym rogu.

Znak KAIWA, warp mode: ciemna kafelka z zaokrąglonymi rogami (promień 15 procent boku). Na niej tunel z sześciu zagnieżdżonych elips o nierównych odstępach i zmiennej grubości linii, z ciemnym rdzeniem. Do tunelu płynie ośmiornica: ciało z płetwami skierowanymi ku tunelowi, z tyłu sześć ramion z okrągłymi końcami, jedno oko. Za ośmiornicą dwie blade kopie jako echo. W prawym dolnym rogu kafelki mały kwadrat (wskaźnik stanu).

Ruch warp mode: ośmiornica płynie po prostej linii pod kątem 35 stopni w górę w prawo, w stronę tunelu. Echo podąża za nim w stałych odstępach. Elipsy tunelu przybliżają się skokami, bez płynnego rozmycia. Na końcu ośmiornica wchodzi w ciemny rdzeń. W ostatniej sekundzie kadr zatrzymuje się na nieruchomym znaku na środku, z wolnym miejscem dookoła (co najmniej jedna czwarta boku znaku).

Pasy sygnałowe: równoległe pasy #FFED00 pod kątem 35 stopni, twarde krawędzie, stałe szerokości.

Nie pokazuj liter ani napisów w obrazie. Nie obracaj, nie rozciągaj i nie przebarwiaj znaku.
```

## Pole odcinka

```text
Temat odcinka: [jedno zdanie, co pokazuje ten film]
Tło: [papier #F1EFE9 | tinte #14171F]
Tryb kolorów znaku: [czarno-biały (domyślny) | spectrum | SHIFT]
```

Tryby spectrum i SHIFT mają własne kolory pasów, pierścieni i echa. Lista: `design/logo/themes.json`. Kwadrat w trybach spectrum i SHIFT ma kolor #14171F i nie pokazuje stanu.

## Po wygenerowaniu

- Napis KAIWA SUITE (wersaliki) i numer odcinka dodaj w montażu, nie w generatorze. Tak litery zgadzają się z systemem.
- Sprawdź każdy kolor z listy na pierwszej i ostatniej klatce.
- Porównaj znak na ostatniej klatce z `design/logo/kaiwa-icon.svg`. Jeśli kształt się różni, wygeneruj film jeszcze raz albo zakończ go plikiem znaku.

| Nazwa | Hex | Użycie w filmie |
|---|---|---|
| `tinte` | #14171F | ciemne tło, kształty na jasnym tle |
| `papier` | #F1EFE9 | jasne tło, kształty na ciemnym tle |
| `signal` | #FFED00 | pasy pod kątem 35 stopni |
| rdzeń | #07080C | środek tunelu |
| `status-aktiv` | #3FB97A | kwadrat stanu, tylko w trybie czarno-białym |
