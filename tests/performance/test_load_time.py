import warnings
from pathlib import Path
from PIL import Image
import imageio.v3 as iio
import pytest
import numpy as np

@pytest.fixture
def sample_image_path(tmp_path):
    """Fixture generujący losowy obraz 1920x1080 do testów wczytywania."""
    image_path = tmp_path / "test_load_time_source.jpg"
    # Generowanie losowej macierzy numpy udającej obraz RGB 1920x1080
    random_image = np.random.randint(0, 256, (1080, 1920, 3), dtype=np.uint8)
    iio.imwrite(image_path, random_image)
    return image_path

def test_load_time(benchmark, sample_image_path):
    Image.MAX_IMAGE_PIXELS = None
    # Ukrycie warningów DecompressionBombWarning
    warnings.simplefilter('ignore', Image.DecompressionBombWarning)

    # Funkcja, która będzie mierzona (tylko wczytanie)
    def load_image():
        return iio.imread(sample_image_path)

    # Uruchomienie benchmarka
    img = benchmark(load_image)

    # Weryfikacja wyniku działania funkcji benchmarkowanej
    assert img is not None
    assert img.size > 0
    assert img.shape == (1080, 1920, 3)
