import os
import logging
import imageio.v3 as iio
import pytest
import numpy as np

logger = logging.getLogger(__name__)

@pytest.fixture
def source_performance_image():
    """Fixture generujący losową macierz numpy udającą obraz 1920x1080."""
    return np.random.randint(0, 256, (1080, 1920, 3), dtype=np.uint8)

def test_png_compression_high_level(benchmark, source_performance_image, tmp_path):
    """Test kompresji PNG z maksymalnym poziomem."""
    output_path = tmp_path / "test_high_compression.png"

    def compress_png():
        iio.imwrite(output_path, source_performance_image, compress_level=9)
        return output_path

    # Wykonanie benchmarka
    result_path = benchmark(compress_png)

    # Weryfikacja wyniku działania funkcji benchmarkowanej
    assert result_path.exists(), "PNG file was not created"
    assert result_path.stat().st_size > 0, "PNG file is empty"

def test_tiff_lossless_compression(benchmark, source_performance_image, tmp_path):
    """Test kompresji TIFF bez strat."""
    output_path = tmp_path / "test_lossless.tiff"

    def compress_tiff():
        iio.imwrite(output_path, source_performance_image)
        return output_path

    # Wykonanie benchmarka
    result_path = benchmark(compress_tiff)

    # Weryfikacja wyniku działania funkcji benchmarkowanej
    assert result_path.exists(), "TIFF file was not created"
    assert result_path.stat().st_size > 0, "TIFF file is empty"
