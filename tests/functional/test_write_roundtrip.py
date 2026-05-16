import numpy as np
import imageio.v3 as iio
from pathlib import Path
import os

def test_imwrite_imread_roundtrip():
    """
    Test poprawności połączonego zapisu i odczytu obrazu:
    - generuje tablicę pikseli w pamięci,
    - zapisuje ją do pliku przy użyciu imwrite,
    - odczytuje z powrotem przy użyciu imread,
    - weryfikuje zgodność danych.
    """
    tmp_path=Path(__file__).parent
    # Wygenerowanie przykładowego obrazu RGB 64x64
    original = np.random.randint(
        0, 256, size=(64, 64, 3), dtype=np.uint8
    )

    # Ścieżka do pliku tymczasowego
    file_path = tmp_path / "roundtrip_test.png"

    # Zapis obrazu
    iio.imwrite(file_path, original)

    # Odczyt obrazu
    loaded = iio.imread(file_path)

    print(f"scieak:{file_path}")
    print("xd")
    # Usunięcie niepotrzebnego pliku
    if os.path.isfile(file_path):
        os.unlink(file_path)

    # Weryfikacja kształtu i typu danych
    assert loaded.shape == original.shape
    assert loaded.dtype == original.dtype

    # Weryfikacja identyczności pikseli
    np.testing.assert_array_equal(loaded, original)
