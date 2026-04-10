# Strategia Testowania

## § Plan zakłada przetestowanie działania 5 modułów : 

### 1. imageio.v3.immeta
   
Funkcja służąca do odczytywania metadanych obrazu bez wczytywania całego pliku do pamięci. Zwraca informacje takie jak np. rozmiar obrazu, format czy inne dane zapisane w pliku.

### 2. imageio.v3.imread

Funkcja używana do wczytywania obrazu z pliku (np. PNG, JPG) do tablicy NumPy. Dzięki temu obraz można dalej analizować lub przetwarzać w Pythonie.

### 3. imageio.v3.imwrite

Funkcja służąca do zapisywania obrazu do pliku. Przyjmuje dane obrazu (najczęściej tablicę NumPy) i zapisuje je w wybranym formacie graficznym, np. PNG, JPG lub TIFF. Umożliwia także ustawienie różnych parametrów zapisu zależnych od formatu pliku.

### 4. imageio.plugins.pillow.PillowPlugin

Plugin biblioteki ImageIO oparty na bibliotece Pillow. Odpowiada za obsługę wielu popularnych formatów obrazów (np. JPEG, PNG, GIF) podczas ich wczytywania i zapisywania.

> Testy obejmują:
> 1. Analizę metadanych obrazów.
> 2. Test *Round-Trip* - Tablica -*Zapis*-> Obraz -*Odczyt*-> Tablica
> 3. Test obsługi plików wielowarstwowych. Tzw. *Testy wolumetrzyczne*
> 4. Testy obsługi kanałów. (Barwy, Alpha, Grayscale)
> 5. Testy konewrtujące formaty barw. Np. CMYK -> RGB

## § Rodzaje Testów

  Testy funkcjonalne
  
  Testy wydajnościowe
  
  Testy akceptacyjne
