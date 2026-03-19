# 1.Opis projektu
Projekt OOB_Tests-ImageIO ma na celu testowanie biblioteki ImageIO, szczególnie w kontekście testów Out-of-Box (OOB) - czyli testów sprawdzających zachowanie systemu przy dostępie do pamięci poza dozwolonymi granicami. Celem jest:

Identyfikacja błędów i luk w zabezpieczeniach

Weryfikacja stabilności biblioteki ImageIO

Testowanie granic i warunków brzegowych

Zapewnienie bezpieczeństwa aplikacji korzystających z ImageIO

# 2. Podział Ról
Szymon Rospondek -- Tech Lead, DevOps,Developer

Daniel Mierzwa -- Product Owner,Developer

Filip Walczak -- Tester, Dokumentacja,Developer

# 3. Kanał Komunikacji

![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)


# 4. Strategia Testowania

## § Plan zakłada przetestowanie działania 5 modułów : 

### 1. imageio.v3.immeta
   
Funkcja służąca do odczytywania metadanych obrazu bez wczytywania całego pliku do pamięci. Zwraca informacje takie jak np. rozmiar obrazu, format czy inne dane zapisane w pliku.

### 2. imageio.v3.imread

Funkcja używana do wczytywania obrazu z pliku (np. PNG, JPG) do tablicy NumPy. Dzięki temu obraz można dalej analizować lub przetwarzać w Pythonie.

### 3. imageio.plugins.pillow.PillowPlugin

Plugin biblioteki ImageIO oparty na bibliotece Pillow. Odpowiada za obsługę wielu popularnych formatów obrazów (np. JPEG, PNG, GIF) podczas ich wczytywania i zapisywania.

### 4. imageio.v3.imwrite

Funkcja służąca do zapisywania obrazu do pliku. Przyjmuje dane obrazu (np. tablicę NumPy) i zapisuje je w wybranym formacie graficznym.

### 5. imageio.v3.imwrite

Funkcja służąca do zapisywania obrazu do pliku. Przyjmuje dane obrazu (najczęściej tablicę NumPy) i zapisuje je w wybranym formacie graficznym, np. PNG, JPG lub TIFF. Umożliwia także ustawienie różnych parametrów zapisu zależnych od formatu pliku.
## § Rodzaje Testów

  Testy funkcjonalne
  
  Testy wydajnościowe
  
  Testy akceptacyjne
# 5. Struktura Projektu
```
OOB_Tests-ImageIO/
│
├──  README.md
├──  README_TASK.md
├──  Pipeline.py
│
├──  .github/
│
├── AcceptanceTests/
│
├── Results/
│
├──  scripts/
│
└──  tests/
```
# 6. Harmonogram
1.Stworzyć pipeline (zrobione)

2.Stworzyć testy funkcjonalne i dokumuntacje(Marzec)

3. Stworzyć testy wydajnościowe i dokumentacje
   
4. Sprawdzenie i poprawki kodu
   
5. Stworzyć testy akceptacyjne i dokumentacje
   
6. Stworzyć reszte dokumentacji i przygotować finalną wersje finalnej wersji
