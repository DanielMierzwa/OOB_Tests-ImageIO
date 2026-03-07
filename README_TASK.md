# OOB_Tests-ImageIO
Testy na lekcję Testowania i Dokumentacji Aplikacji.

Obiektem testów będzie biblioteka ImageIO: https://pypi.org/project/ImageIO/

## Członkowie zespołu
1. Daniel Mierzwa 
1. Szymon Rospondek
1. Filip Walczak

## Cele
### Zakres podstawowy (obowiązkowy)
Projekt obejmuje testowanie najnowszej stabilnej wersji wybranego modułu z PyPI.
Wymagania minimalne:
#### 1. Repozytorium
  Repozytorium powinno zawierać:
  * README z opisem projektu i strategii testowej
  * opis podziału ról w zespole
  * strukturę katalogów projektu
  * dokument z opisem scenariuszy testów akceptacyjnych
  * Pipeline (GitHub Actions)
#### 2. Pipeline powinna:
  * być uruchamiana manualnie
  * instalować wskazany moduł z PyPI
  * uruchamiać testy jednostkowe biblioteki (jeśli są dostępne)
  * uruchamiać Wasze testy funkcjonalne  
  * uruchamiać Wasze testy wydajnościowe
  * wyświetlać czytelne podsumowanie wyników
  Pipeline ma być prosta i przejrzysta. Nie wymagamy Dockerów, matrix buildów ani wielosystemowych
  konfiguracji.
#### 3. Testy funkcjonalne
  Każdy zespół przygotowuje:
  * 3–5 testów funkcjonalnych
  Testy powinny:
  * sprawdzać realne użycie modułu
  * mieć uzasadnienie (dlaczego akurat te scenariusze)
  * być czytelne i dobrze nazwane
#### 4. Testy wydajnościowe
  Każdy zespół przygotowuje:
  * 1–2 proste testy wydajnościowe
  Nie wymagamy profesjonalnych benchmarków. Wystarczy:
  * pomiar czasu wykonania wybranej operacji
  * zapis wyniku do loga
  * proste porównanie wyników
#### 5. Scenariusze testów akceptacyjnych
  Należy przygotować dokument zawierający:
  * co najmniej 3 scenariusze testów akceptacyjnych
  * opis celu testu
  * opis oczekiwanego rezultatu
  * kryterium zaliczenia
  Nie muszą być one automatyzowane.
### 🏆 Opcja dla grup celujących w ocenę celującą
Dla zespołów ambitnych przewidziana jest możliwość rozszerzenia projektu:

#### 🔧 Budowanie modułu z wybranego commita na GitHubie

Zamiast instalować wersję z PyPI, zespół może:
  * pobrać wybrany commit z oficjalnego repozytorium GitHub modułu
  * zbudować go lokalnie
  * przetestować go przy użyciu swojej pipeline
Wymaga to:
  * zrozumienia zależności
  * rozwiązania ewentualnych problemów buildowych
  * udokumentowania procesu
To rozszerzenie jest dobrowolne i przewidziane dla zespołów chcących celować w ocenę najwyższą.

Tesdsdsd
