# Scenariusze i Przypadki Testowe – ImageIO

## Nagłówek Projektu

**Nazwa projektu:** Out-of-Box (OOB) Tests for ImageIO  
**Moduł PyPi:** imageio  
**Zespół:** QA Testing  
**Data:** 2026-05-22  

---

## ⦏⦐⦑⦒⦓⦔⦕⦖⦗⦘⦙ Scenariusze Testowe

| ID | Nazwa scenariusza | Opis |
|----|--------------------|------|
| TS_01 | Odczyt Metadanych Obrazów | Test poprawności funkcji `immeta` w odczytywaniu metadanych z różnych formatów obrazów bez wczytywania całej zawartości do pamięci |
| TS_02 | Test Round-Trip (Zapis ↔ Odczyt) | Weryfikacja poprawności działania połączonego zapisu (`imwrite`) i odczytu (`imread`) obrazów poprzez zapisanie tablicy, odczyt i porównanie |
| TS_03 | Obsługa Kanałów Kolorów (RGB, RGBA, Grayscale) | Test poprawności przetwarzania różnych modeli barw i kanału Alpha (przezroczystości) przy zapisie i odczycie |
| TS_04 | Konwersja Formatów Barw (RGB ↔ CMYK) | Test możliwości konwersji między formatami kolorów za pomocą `PillowPlugin` i weryfikacja dokładności kolorów |
| TS_05 | Wydajność Wczytywania (Load Time Profiling) | Pomiar czasu i zasobów wymaganych do wczytania obrazów o dużych rozdzielczościach |
| TS_06 | Wydajność Zapisu (Compression Performance) | Pomiar czasu i złożoności operacji eksportu dla różnych algorytmów kompresji |

---

## ⡈⡉⡊⡋⡌⡍⡎⡏ Przypadki Testowe

### ⦂⦃⦄⦅ TC_01 – Odczyt metadanych z pliku PNG

**Powiązany scenariusz:** TS_01  

**Opis:** Weryfikacja poprawności odczytania metadanych z pliku PNG (wymiary, format, informacje dodatkowe) za pomocą funkcji `imageio.v3.immeta`

**Kroki:**
1. Przygotować testowy plik obrazu w formacie PNG (1920x1080, RGB)
2. Wywołać funkcję `imageio.v3.immeta(path_to_image)`
3. Zweryfikować zwrócone dane metadanych
4. Porównać wymiary i format z oczekiwanymi wartościami

**Dane wejściowe:**  
- Plik: `test_image_1920x1080_RGB.png`
- Format: PNG
- Wymiary: 1920 x 1080 pikseli
- Kanały: RGB (3 kanały)

**Oczekiwany rezultat:**  
Funkcja `immeta` zwraca słownik zawierający:
- `size`: (1920, 1080)
- `shape`: (1080, 1920, 3)
- `format`: 'PNG'
- Bez wczytywania całego pliku do pamięci

**Wynik testu:**
- ☐ PASS
- ☐ FAIL

**Uwagi:**

---

### ⦂⦃⦄⦅ TC_02 – Odczyt metadanych z pliku JPEG

**Powiązany scenariusz:** TS_01  

**Opis:** Weryfikacja poprawności odczytania metadanych z pliku JPEG (wymiary, format, jakość kompresji) za pomocą funkcji `imageio.v3.immeta`

**Kroki:**
1. Przygotować testowy plik obrazu w formacie JPEG (3840x2160, RGB)
2. Wywołać funkcję `imageio.v3.immeta(path_to_image)`
3. Zweryfikować zwrócone metadane
4. Porównać wymiary i format z oczekiwanymi wartościami

**Dane wejściowe:**  
- Plik: `test_image_4K_RGB.jpg`
- Format: JPEG
- Wymiary: 3840 x 2160 pikseli
- Kanały: RGB (3 kanały)

**Oczekiwany rezultat:**  
Funkcja `immeta` zwraca słownik zawierający:
- `size`: (3840, 2160)
- `shape`: (2160, 3840, 3)
- `format`: 'JPEG'
- Prawidłowy odczyt bez załadowania całego obrazu do RAM

**Wynik testu:**
- ☐ PASS
- ☐ FAIL

**Uwagi:**

---

### ⦂⦃⦄⦅ TC_03 – Odczyt metadanych z pliku TIFF

**Powiązany scenariusz:** TS_01  

**Opis:** Weryfikacja poprawności odczytania metadanych z pliku TIFF (wymiary, format, liczba kanałów) za pomocą `immeta` i wtyczki TIFF

**Kroki:**
1. Przygotować testowy plik TIFF (2560x1440, RGBA)
2. Wywołać `imageio.v3.immeta(path_to_image)`
3. Zweryfikować zwrócone metadane
4. Sprawdzić właściwe rozpoznanie kanału Alpha

**Dane wejściowe:**  
- Plik: `test_image_RGBA.tiff`
- Format: TIFF
- Wymiary: 2560 x 1440 pikseli
- Kanały: RGBA (4 kanały)

**Oczekiwany rezultat:**  
Metadane zawierają:
- `size`: (2560, 1440)
- `shape`: (1440, 2560, 4)
- `format`: 'TIFF'
- Prawidłowe rozpoznanie kanału Alpha (czwarty kanał)

**Wynik testu:**
- ☐ PASS
- ☐ FAIL

**Uwagi:**

---

### ⦂⦃⦄⦅ TC_04 – Round-Trip PNG (Array → Write → Read → Array)

**Powiązany scenariusz:** TS_02  

**Opis:** Test pełnego cyklu zapisu i odczytu: wygenerowana w pamięci tablica pikseli → zapis PNG → odczyt → porównanie z oryginałem

**Kroki:**
1. Wygenerować losową tablicę NumPy (512x512x3, dtype=uint8, wartości 0-255)
2. Zapisać tablicę do pliku PNG za pomocą `imageio.v3.imwrite()`
3. Wczytać obraz z pliku za pomocą `imageio.v3.imread()`
4. Porównać wczytaną tablicę z oryginałem (powinny być identyczne)

**Dane wejściowe:**  
```python
import numpy as np
original_array = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)
