# Strategia Testowania

## § Moduły imageio, które przetestujemy

### 1. imageio.v3.immeta
Funkcja służąca do odczytywania metadanych obrazu bez wczytywania całego pliku do pamięci. Zwraca informacje takie jak np. rozmiar obrazu, format czy inne dane zapisane w pliku.

### 2. imageio.v3.imread
Funkcja używana do wczytywania obrazu z pliku (np. PNG, JPG) do tablicy NumPy. Dzięki temu obraz można dalej analizować lub przetwarzać w Pythonie.

### 3. imageio.v3.imwrite
Funkcja służąca do zapisywania obrazu do pliku. Przyjmuje dane obrazu (najczęściej tablicę NumPy) i zapisuje je w wybranym formacie graficznym, np. PNG, JPG lub TIFF. Umożliwia także ustawienie różnych parametrów zapisu zależnych od formatu pliku.

### 4. imageio.plugins.pillow.PillowPlugin
Plugin biblioteki ImageIO oparty na bibliotece Pillow. Odpowiada za obsługę wielu popularnych formatów obrazów (np. JPEG, PNG, GIF) podczas ich wczytywania i zapisywania.

### 5. imageio.plugins.tifffile.TifffilePlugin
Plugin biblioteki ImageIO oparty na bibliotece tifffile. Odpowiada za kompleksową obsługę plików TIFF.

## § Testy funkcjonalne

### 1. Analiza metadanych obrazów
Testowanie poprawnego odczytu i weryfikacji metadanych z plików graficznych (np. wymiarów, formatu, informacji dodatkowych) wykorzystując funkcję `immeta` oraz wtyczki (np. `PillowPlugin`, `TifffilePlugin`) bez wczytywania pełnej tablicy pikseli do pamięci RAM.

### 2. Test Round-Trip (Tablica -> Zapis -> Obraz -> Odczyt -> Tablica)
Test weryfikujący poprawność działania połączonego zapisu i odczytu. Polega na zapisaniu wygenerowanej w pamięci tablicy pikseli do pliku za pomocą funkcji `imwrite`, a następnie bezbłędnym odczycie tych samych danych z powrotem przy użyciu `imread`.

### 3. Test obsługi plików wielowarstwowych (Testy wolumetryczne)
Test nakierowany na weryfikację wydajności oraz niezawodności pracy z wtyczką `TifffilePlugin` podczas obsługi plików wielowarstwowych np. TIFF.

### 4. Testy obsługi kanałów (Barwy, Alpha, Grayscale)
Ocena procedury zapisu i odczytu plików powiązanych z różnymi paletami barw oraz kanałem przezroczystości (ang. Alpha channel), sprawdzając poprawne alokowanie w trójwymiarowych tablicach w użyciu z `imread` oraz `imwrite`.

### 5. Testy Round-Trip konwertujące formaty barw (np. RGB -> CMYK -> RGB)
Ocena możliwości `PillowPlugin` w zakresie konwersji formatów barw, np. z CMYK do RGB. Sprawdzić czy kolory po powrocie do RGB są maksymalnie zbliżone.

## § Testy wydajnościowe

### 1. Wydajność wczytywania obrazów o znacznych rozdzielczościach (Load Time Profiling)
Test zbadania narzutu (overhead) podczas dekodowania i wczytywania pikseli. Polega na zmierzeniu czasu, jaki funkcja `imageio.v3.imread` potrzebuje na poprawne wczytanie obrazów o ogromnych wymiarach (np. 8K, 16K, gigapanoramy) bezpośrednio do wolnych zasobów RAM na podstawie tablicy w NumPy.

### 2. Czas kompresji i zapis obrazów (Złożoność Zapisywania)
Test mający na celu obliczenie kosztu operacji eksportu dla skomplikowanych algorytmów kompresji. Polega na ustaleniu czasu wykonywania wywołania `imageio.v3.imwrite` zapisującego obrazy o dużym rozmiarze z wykorzystaniem wysokiego stopnia kompresji PNG lub w bezstratnych formatach typu TIFF, mierząc czas trwania alokacji pliku wynikowego na dysku fizycznym.
