import time
import tempfile
import os
import logging
import imageio.v3 as iio
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture
def source_performance_image():
    """Pobranie obrazu do testowania kompresji z URL."""
    url = 'https://github.com/DanielMierzwa/OOB_Tests-ImageIO/blob/main/tests/performance/source_performance.png?raw=true'
    image = iio.imread(url)
    return image


@pytest.fixture
def temp_output_dir():
    """Create a temporary directory for output files."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Cleanup
    for file in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    os.rmdir(temp_dir)


def test_png_compression_high_level(source_performance_image, temp_output_dir):
    """Test kompresji PNG z maksymalnym poziomem."""
    output_path = os.path.join(temp_output_dir, "test_high_compression.png")

    start_time = time.perf_counter()
    iio.imwrite(output_path, source_performance_image, compress_level=9)
    with open(output_path, 'rb'):
        pass
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    file_size = os.path.getsize(output_path)

    # logger.info(f"PNG (L9): {elapsed_time:.4f}s, {file_size / (1024**2):.2f}MB")

    assert os.path.exists(output_path), "PNG file was not created"
    assert file_size > 0, "PNG file is empty"


def test_tiff_lossless_compression(source_performance_image, temp_output_dir):
    """Test kompresji TIFF bez strat."""
    output_path = os.path.join(temp_output_dir, "test_lossless.tiff")

    start_time = time.perf_counter()
    iio.imwrite(output_path, source_performance_image)
    with open(output_path, 'rb'):
        pass
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    file_size = os.path.getsize(output_path)

    # logger.info(f"TIFF (bezzstratny): {elapsed_time:.4f}s, {file_size / (1024**2):.2f}MB")

    assert os.path.exists(output_path), "TIFF file was not created"
    assert file_size > 0, "TIFF file is empty"


def test_compression_comparison(source_performance_image, temp_output_dir):
    """Porównanie wydajności PNG vs TIFF."""
    png_path = os.path.join(temp_output_dir, "comparison.png")
    tiff_path = os.path.join(temp_output_dir, "comparison.tiff")

    png_start = time.perf_counter()
    iio.imwrite(png_path, source_performance_image, compress_level=9)
    with open(png_path, 'rb'):
        pass
    png_elapsed = time.perf_counter() - png_start

    tiff_start = time.perf_counter()
    iio.imwrite(tiff_path, source_performance_image)
    with open(tiff_path, 'rb'):
        pass
    tiff_elapsed = time.perf_counter() - tiff_start

    png_size = os.path.getsize(png_path)
    tiff_size = os.path.getsize(tiff_path)

    # logger.info(f"Porównanie: PNG(L9) {png_elapsed:.4f}s ({png_size/(1024**2):.2f}MB) vs TIFF {tiff_elapsed:.4f}s ({tiff_size/(1024**2):.2f}MB) ratio={png_size/tiff_size:.2%}")

    assert os.path.exists(png_path), "PNG file was not created"
    assert os.path.exists(tiff_path), "TIFF file was not created"
