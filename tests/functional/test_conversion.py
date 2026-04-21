from pathlib import Path
import imageio.v3 as iio
import numpy as np
import pytest

# DEBUG_DIR = Path(__file__).parent
# odkomentuj tą linijkę i linie 47-49 oraz 76-78
# jeśli potrzebujesz zobaczyć efekty konwersji
def _rgb(img):
    if img.ndim == 2:
        return np.stack([img, img, img], axis=-1)
    if img.shape[2] == 4:
        return img[:, :, :3]
    return img


def _alpha(img):
    if img.ndim == 3 and img.shape[2] == 4:
        return img[:, :, 3]
    return np.full(img.shape[:2], 255, dtype=np.uint8)


@pytest.fixture
def source_images():
    """
    Wskazuje pliki wejściowe (tylko read-only)
    """
    base = Path(__file__).parent / "test_conversion_source"
    return {
        "png": base / "source.png",
        "jpg": base / "source.jpg",
    }


def test_png_to_jpg_conversion(tmp_path, source_images):
    src = source_images["png"]

    out_file = tmp_path / "out.jpg"

    img = iio.imread(src)

    if img.shape[-1] == 4:
        img = img[..., :3]
    # usunięcie kanału alfa

    iio.imwrite(out_file, img, format="jpeg", quality=95)

    # DEBUG_DIR.mkdir(exist_ok=True)
    # debug_copy = DEBUG_DIR / "png_to_jpg_result.jpg"
    # iio.imwrite(debug_copy, img, format="JPEG", quality=95)

    assert out_file.exists()

    orig = iio.imread(src)
    conv = iio.imread(out_file)

    orig_rgb = _rgb(orig)
    conv_rgb = _rgb(conv)

    assert orig_rgb.shape == conv_rgb.shape

    diff = np.mean(np.abs(orig_rgb.astype(int) - conv_rgb.astype(int)))#wyliczenie średniego odchylenia
    assert diff <= 1, f"Zbyt duże różnice kolorów: {diff}"

    # JPG nie ma alpha
    assert np.all(_alpha(conv) == 255)


def test_jpg_to_png_conversion(tmp_path, source_images):
    src = source_images["jpg"]

    out_file = tmp_path / "out.png"

    img = iio.imread(src)
    iio.imwrite(out_file, img)

    # DEBUG_DIR.mkdir(exist_ok=True)
    # debug_copy = DEBUG_DIR / "jpg_to_png_result.png"
    # iio.imwrite(debug_copy, img)

    assert out_file.exists()

    orig = iio.imread(src)
    conv = iio.imread(out_file)

    orig_rgb = _rgb(orig)
    conv_rgb = _rgb(conv)

    assert orig_rgb.shape == conv_rgb.shape

    diff = np.abs(orig_rgb.astype(int) - conv_rgb.astype(int)).max()
    assert diff <= 2, f"Zbyt duże różnice kolorów: {diff}"

    assert np.all(_alpha(conv) == 255)