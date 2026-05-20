import time
import tempfile
import os
import numpy as np
import imageio.v3 as iio
import pytest


@pytest.fixture
def large_rgb_image():
    """Generate a large RGB image (4096x4096 px) for compression testing."""
    np.random.seed(42)
    image = np.random.randint(0, 256, (4096, 4096, 3), dtype=np.uint8)
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


def test_png_compression_high_level(large_rgb_image, temp_output_dir):
    """
    Test imageio.v3.imwrite performance writing large RGB image to PNG with maximum compression.
    
    Measures time from function call to return (not including image generation or file read verification).
    PNG compression level: 9 (maximum)
    Image size: 4096x4096 px RGB
    """
    output_path = os.path.join(temp_output_dir, "test_high_compression.png")
    
    # Measure time for PNG writing with maximum compression
    start_time = time.perf_counter()
    iio.imwrite(output_path, large_rgb_image, compress_level=9)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    file_size = os.path.getsize(output_path)
    
    # Print diagnostic information
    print(f"\nPNG Compression Test (Level 9):")
    print(f"  Elapsed time: {elapsed_time:.4f} seconds")
    print(f"  File size: {file_size / (1024**2):.2f} MB")
    
    # Verify file was created
    assert os.path.exists(output_path), "PNG file was not created"
    assert file_size > 0, "PNG file is empty"


def test_tiff_lossless_compression(large_rgb_image, temp_output_dir):
    """
    Test imageio.v3.imwrite performance writing large RGB image to lossless TIFF format.
    
    Measures time from function call to return (not including image generation or file read verification).
    TIFF format: lossless (no compression codec specified - default is no compression)
    Image size: 4096x4096 px RGB
    """
    output_path = os.path.join(temp_output_dir, "test_lossless.tiff")
    
    # Measure time for TIFF writing (lossless format)
    start_time = time.perf_counter()
    iio.imwrite(output_path, large_rgb_image)
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    file_size = os.path.getsize(output_path)
    
    # Print diagnostic information
    print(f"\nTIFF Lossless Compression Test:")
    print(f"  Elapsed time: {elapsed_time:.4f} seconds")
    print(f"  File size: {file_size / (1024**2):.2f} MB")
    
    # Verify file was created
    assert os.path.exists(output_path), "TIFF file was not created"
    assert file_size > 0, "TIFF file is empty"


def test_compression_comparison(large_rgb_image, temp_output_dir):
    """
    Compare performance and file sizes between PNG (compressed) and TIFF (lossless).
    
    This test runs both formats and provides a comparison report.
    """
    png_path = os.path.join(temp_output_dir, "comparison.png")
    tiff_path = os.path.join(temp_output_dir, "comparison.tiff")
    
    # PNG with maximum compression
    png_start = time.perf_counter()
    iio.imwrite(png_path, large_rgb_image, compress_level=9)
    png_elapsed = time.perf_counter() - png_start
    
    # TIFF lossless
    tiff_start = time.perf_counter()
    iio.imwrite(tiff_path, large_rgb_image)
    tiff_elapsed = time.perf_counter() - tiff_start
    
    png_size = os.path.getsize(png_path)
    tiff_size = os.path.getsize(tiff_path)
    
    # Print comparison report
    print(f"\nCompression Comparison Report:")
    print(f"{'Format':<15} {'Time (s)':<12} {'Size (MB)':<12} {'Ratio':<10}")
    print(f"{'-'*49}")
    print(f"{'PNG (L9)':<15} {png_elapsed:<12.4f} {png_size/(1024**2):<12.2f} {png_size/tiff_size:<10.2%}")
    print(f"{'TIFF (raw)':<15} {tiff_elapsed:<12.4f} {tiff_size/(1024**2):<12.2f} {'1.00':<10}")
    
    # Verify both files were created
    assert os.path.exists(png_path), "PNG file was not created"
    assert os.path.exists(tiff_path), "TIFF file was not created"
