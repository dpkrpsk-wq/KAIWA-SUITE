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
sygnał #FFED00 (żółty) tylko jako pasy, plamy i kwadrat w znaku, nigdy jako tło całego kadru,
zielony stan #3FB97A tylko w małym kwadracie znaku i tylko wtedy, gdy pokazany jest stan.

Znak KAIWA „K.”: ciemna kafelka z zaokrąglonymi rogami (promień 15 procent boku). Na niej duża litera K o prostych, twardych krawędziach w kolorze #F1EFE9, a u stopy K, na prawo od jego nogi, mały żółty kwadrat #FFED00 (wskaźnik stanu). Nic więcej nie leży na kafelce.

Ruch: K stoi nieruchomo. Kwadrat pojawia się twardym cięciem, potem dwa razy włącza się i wyłącza twardym cięciem, bez zanikania. Pasy pod kątem 35 stopni przebiegają raz przez kadr od lewej do prawej skokami, bez płynnego rozmycia. W ostatniej sekundzie kadr zatrzymuje się na nieruchomym znaku na środku, z wolnym miejscem dookoła (co najmniej jedna czwarta boku znaku).

Pasy sygnałowe: równoległe pasy #FFED00 pod kątem 35 stopni, twarde krawędzie, stałe szerokości.

Nie pokazuj liter ani napisów w obrazie. Nie obracaj, nie rozciągaj i nie przebarwiaj znaku.
```

## Pole odcinka

```text
Temat odcinka: [jedno zdanie, co pokazuje ten film]
Tło: [papier #F1EFE9 | tinte #14171F]
Tryb kolorów znaku: [czarno-biały (domyślny) | spectrum | SHIFT]
```

Tryby spectrum i SHIFT mają własne kolory poziomych pasów kafelki. Lista: `design/logo/themes.json`. K i kwadrat w trybach spectrum i SHIFT mają kolor #14171F, a kwadrat nie pokazuje stanu.

## Po wygenerowaniu

- Napis KAIWA SUITE (wersaliki) i numer odcinka dodaj w montażu, nie w generatorze. Tak litery zgadzają się z systemem.
- Sprawdź każdy kolor z listy na pierwszej i ostatniej klatce.
- Porównaj znak na ostatniej klatce z `design/logo/kaiwa-icon.svg`. Jeśli kształt się różni, wygeneruj film jeszcze raz albo zakończ go plikiem znaku.

| Nazwa | Hex | Użycie w filmie |
|---|---|---|
| `tinte` | #14171F | ciemne tło, kształty na jasnym tle |
| `papier` | #F1EFE9 | jasne tło, kształty na ciemnym tle |
| `signal` | #FFED00 | pasy pod kątem 35 stopni |
| `status-aktiv` | #3FB97A | kwadrat stanu, tylko w trybie czarno-białym i tylko gdy pokazany jest stan |
