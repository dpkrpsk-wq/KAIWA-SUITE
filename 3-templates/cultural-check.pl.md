# Kontrola kulturowa: kontekst przed analizą i blok po niej

Szablon z pakietu KAIWA, produkt 26.01, wersja 0.2.0 (robocza), 05.11.2026.

Model ma domyślne spojrzenie, którego sam nie zawsze widzi: co uznaje za normę, kogo za odbiorcę, jakie instytucje, święta, role i konwencje zakłada. Ten szablon robi z tego jawny krok. Agent „KAIWA: analiza“ wykonuje go sam. Ten plik służy jako droga zapasowa dla dowolnego asystenta AI i jako lista kontrolna dla studenta albo prowadzącego.

## Gdzie krok działa

1. Po triażu i wyborze dalszego kroku asystent pyta o kontekst, razem z pytaniem o język wyniku (`3-templates/after-triage.pl.md`, krok 2).
2. Przy każdej ramie asystent pisze jedno zdanie o tym, dla jakiego materiału ją opisano.
3. Wynik kończy się stałym blokiem „Kontrola kulturowa“.

## Pytanie o kontekst

Asystent pyta jednym tekstem:

> Kontekst: w jakim języku i środowisku (kraj, krąg, czas) powstał artefakt, dla kogo go zrobiono, kim jesteś wobec tego środowiska (swój, obcy, pomiędzy) i dla kogo jest wynik? Odpowiedz tylko to, co wiesz.

Odpowiedzi trafiają do analizy dosłownie jako twoje słowa. Czego nie wiesz, zostaje jako „brak informacji“. Asystent nie dopowiada kultury ani odbiorcy.

## Blok na końcu wyniku

Pięć wierszy. Każdy jest wypełniony albo ma postać „nie dotyczy: powód“.

1. **Założenia modelu.** Każde założenie o normie, odbiorcy, kraju, instytucjach, religii, płci, czasie albo języku, które wpłynęło na wynik. Z oznaczeniem **[założenie modelu]** i podstawą: cytat z artefaktu, twoje słowa albo „brak podstawy“.
2. **Rama a materiał.** Jedno zdanie na ramę: dla jakiego materiału i środowiska opisuje ją jej deklaracja (L1: założenia ontologiczne ramy, D2: pozycja obserwatora, obok D1: skala i D3: czas, według deklaracji w `method/prompts/framework-catalog.md`) i czy artefakt do niego należy. Gdy deklaracja o tym milczy: „deklaracja nie mówi“.
3. **Odczytania alternatywne.** Przy każdym kodzie konotacji (znaczeniu dodatkowym, które znak niesie poza dosłownym, wg Barthes'a) dwa do trzech odczytań. Wybrany jest oznaczony „wybrany przeciw: …“ (protokół ram interpretacyjnych, `method/protocols/interpretive-frame-protocol.md`, § 2.2).
4. **Terminy bez odpowiednika.** Gdy język wyniku różni się od języka artefaktu: glosa w języku wyniku, termin źródłowy kursywą w nawiasie przy pierwszym użyciu (nawias Cassin, czyli termin oryginalny w nawiasie obok przekładu, ten sam protokół, § 2.1).
5. **Adresat wyniku.** Kto jest „my“, kto „oni“ w tekście wyniku i czy to zgadza się z odbiorcą, którego podałeś (`method/protocols/actant-self-check.md`, § 2.2).

## Jak sprawdzić (lista dla studenta albo prowadzącego)

1. Czy blok jest na końcu wyniku i ma pięć wierszy?
2. Czy każdy wiersz jest wypełniony albo ma powód przy „nie dotyczy“?
3. Czy każde **[założenie modelu]** ma podstawę? Przy „brak podstawy“ to ty rozstrzygasz, czy założenie jest trafne. Odpowiedź wpisz do wyniku.
4. Czy wiersz 2 wymienia każdą użytą ramę?
5. Czy odczytania w wierszu 3 są naprawdę różne, czy to jedno odczytanie w trzech słowach?
6. Czy „my“ i „oni“ w wierszu 5 są takimi osobami, jakimi chcesz je widzieć?
7. Czy w tekście wyniku jest założenie, którego nie ma w bloku? Jeśli tak, dopisz je do bloku sam. Blok pokazuje tylko to, co model sam nazwał. Resztę widzi tylko czytelnik.

Drugi przebieg: wklej wynik, artefakt i swoje odpowiedzi o kontekst do nowej rozmowy i zapytaj, jakich założeń w bloku brakuje. To drugi głos, nie dowód.

## Tekst do wklejenia (droga zapasowa)

```text
After the triage and the choice of next step, ask me in one message, in my language: (1) in which language the result should be (Polish, English, German or other), (2) "Context: in which language and milieu (country, circle, time) was the artefact made, for whom, who am I in relation to that milieu (insider, outsider, in between), and who is the result for? Answer only what you know." Record my answers verbatim as my words. Mark what I do not give as "no information". Do not fill in a culture or an audience for me.
For every framework you apply, add one sentence: for which material and milieu its declaration (L1, D2) describes it, and whether the artefact belongs there. If the declaration is silent, write "declaration does not say". For every connotation code, give two or three readings and mark the chosen one "chosen against: ...".
End the result with a block "Cultural check" of five lines, each filled or "not applicable: reason":
1. Assumptions about norm, audience, country, institutions, religion, gender, time or language that shaped the result. Mark each [model assumption] with its basis: a quote from the artefact, my words, or "no basis".
2. Framework and material, one sentence per framework.
3. Alternative readings and the one chosen against.
4. Terms without equivalent, when the result language differs from the artefact language: gloss in the result language, source term in italics in brackets at first use.
5. Addressee of the result: who is "we" and who is "they" in the text, and whether this fits the audience I named.
Never assign a culture to the artefact or to me that I did not state.
```

## Granice

1. Blok pokazuje, co model sam nazwał. Założenia, których model nie rozpoznaje, w nim się nie pojawią. Punkt 7 listy i drugi przebieg to jedyne sposoby, żeby je wychwycić.
2. Pakiet nie rozstrzyga, czy krok zmienia wyniki. To wymagałoby próby z tym samym artefaktem z krokiem i bez niego.
3. Wiersz 2 opiera się na deklaracjach ram w `method/prompts/`. Gdy deklaracja milczy, blok mówi to wprost i niczego nie dopowiada.
