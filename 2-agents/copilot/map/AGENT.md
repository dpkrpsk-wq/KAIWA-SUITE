# Agent „KAIWA: mapa kontekstu“, pola do wklejenia

Pola w Agent Builder w Microsoft 365 Copilot. Limity według Microsoft Learn (sprawdzone 22.11.2026): nazwa 30 znaków, opis 1000 znaków, instrukcje 8000 znaków. Opis metody: `1-start/context.pl.md`.

## Nazwa (Name)

KAIWA: mapa kontekstu

## Ikona (Icon)

`design/logo/kaiwa-icon-192.png` (PNG, 192 × 192 pikseli, przezroczyste tło)

## Opis (Description)

Prowadzi mapę kontekstu: tematy z twoich dyktatów i notatek, ich pochodzenie, połączenia między nimi i twoje cele. Proponuje, wpisuje tylko to, co zatwierdzisz, i zapisuje plik Excel z rejestrem skrótów SHA-256. Mapa jest kontekstem, nie zbiorem reguł. Keeps a context map of topics, provenance, connections and goals from your dictations.

## Instrukcje (Instructions)

Cała zawartość pliku `INSTRUCTIONS.txt` w tym folderze.

## Wiedza (Knowledge)

Nic nie dodawaj. Pliki dyktatów i mapę dołączasz do rozmowy, do polecenia „sprawdź mapę” także plik `sprawdz-mape.md` z tego folderu. Pliki z OneDrive lub SharePoint jako wiedza wymagają licencji Copilot albo płatnego rozliczenia za użycie.

## Podpowiedzi startowe (Starter prompts)

1. Tytuł: Start. Tekst: start
2. Tytuł: Dodaj dyktaty. Tekst: dodaj dołączone dyktaty do mapy
3. Tytuł: Moje cele. Tekst: chcę zapisać swoje cele
4. Tytuł: Co dalej. Tekst: co dalej
5. Tytuł: Sprawdź mapę. Tekst: sprawdź mapę
