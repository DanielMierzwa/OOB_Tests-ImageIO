from pathlib import Path

import imageio.v3 as iio
import numpy as np
from PIL import Image


# Funkcja pomocnicza, która zapewnia, że obraz jest w formacie RGB (3 kanały).
def _ensure_rgb(image: np.ndarray) -> np.ndarray:
    if image.ndim == 2:
        return np.stack([image, image, image], axis=-1)
    if image.ndim == 3 and image.shape[2] == 4:
        return image[:, :, :3]
    return image


# Tworzy zestaw kontrolnych próbek kolorów, który obejmuje podstawowe kolory.
def _build_color_chart() -> np.ndarray:
    color_chart = np.array(
        [
            [0, 0, 0],         # black
            [255, 255, 255],   # white
            [255, 0, 0],       # red
            [0, 255, 0],       # green
            [0, 0, 255],       # blue
            [0, 255, 255],     # cyan
            [255, 0, 255],     # magenta
            [255, 255, 0],     # yellow
            [64, 64, 64],      # gray64
            [128, 128, 128],   # gray128
            [192, 192, 192],   # gray192
            [255, 165, 0],     # orange
            [50, 205, 50],     # lime
            [0, 127, 255],     # azure
            [138, 43, 226],    # violet
            [255, 105, 180],   # pink
        ],
        dtype=np.uint8
    ).reshape((4, 4, 3))

    return np.repeat(np.repeat(color_chart, 32, axis=0), 32, axis=1)


# Oblicza maksymalną bezwzględną różnicę między dwoma obrazami.
# Potrzebne do oceny odchylenia kolorów po konwersji.
def _max_abs_diff(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.abs(a.astype(np.int16) - b.astype(np.int16)).max())


# Oblicza średnią bezwzględną różnicę między dwoma obrazami.
# Potrzebne do oceny odchylenia kolorów po konwersji.
def _mean_abs_diff(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.abs(a.astype(np.int16) - b.astype(np.int16)).mean())


# Wykonuje konwersję RGB -> CMYK -> RGB z TIFF jako formatem pośrednim.
def _roundtrip_rgb_via_cmyk_tiff(rgb: np.ndarray, tmp_path: Path) -> np.ndarray:
    rgb = _ensure_rgb(rgb).astype(np.uint8)

    cmyk_image = Image.fromarray(rgb, mode='RGB').convert('CMYK')
    cmyk_array = np.asarray(cmyk_image, dtype=np.uint8)

    out_file = tmp_path / 'roundtrip_cmyk.tif'

    iio.imwrite(
        out_file,
        cmyk_array,
        plugin='pillow',
        format='TIFF',
        mode="CMYK",
    )

    assert out_file.exists(), "Output file was not created."

    with Image.open(out_file) as saved_img:
        assert saved_img.mode == "CMYK", f"Oczekiwany tryb obrazu zapisanego to CMYK, ale otrzymano {saved_img.mode}"

    return iio.imread(out_file, plugin='pillow', mode="RGB")


# Sprawdza, że konwersja RGB -> CMYK -> RGB dla zestawu kontrolnych próbek kolorów zachowuje kolory w granicach dopuszczalnego odchylenia.
def test_rgb_cmyk_roundtrip_preserves_reference_swatches(tmp_path):
    original = _build_color_chart()
    roundtrip = _roundtrip_rgb_via_cmyk_tiff(original, tmp_path)

    assert roundtrip.shape == original.shape, f"Kształt obrazu po konwersji {roundtrip.shape} nie zgadza się z oczekiwanym {original.shape}"
    assert roundtrip.dtype == np.uint8, f"Dtype obrazu po konwersji {roundtrip.dtype} nie zgadza się z oczekiwanym uint8"

    max_diff = _max_abs_diff(original, roundtrip)
    mean_diff = _mean_abs_diff(original, roundtrip)

    assert max_diff <= 1, f"Maksymalna różnica bezwzględna {max_diff} przekracza próg 1"
    assert mean_diff <= 0.5, f"Średnia różnica bezwzględna {mean_diff} przekracza próg 0.5"



# Sprawdza konwersje RGB -> CMYK -> RGB dla rzeczywistego obrazu w granicach dopuszczalnego odchylenia barw.
# Porównuje wynik z konwersją wykonaną w pamięci przez Pillow, aby upewnić się, że proces zapisu i odczytu TIFF nie wprowadza dodatkowych błędów.
def test_rgb_cmyk_rgb_roundtrip_matches_in_memory_pillow_conversion(tmp_path):
    source = Path(__file__).parent / 'test_conversion_source' / 'source.jpg'

    original = _ensure_rgb(iio.imread(source, plugin='pillow')).astype(np.uint8)

    expected_rgb = np.asarray(
        Image.fromarray(original, mode='RGB').convert('CMYK').convert('RGB'),
        dtype=np.uint8
    )

    roundtrip = _roundtrip_rgb_via_cmyk_tiff(original, tmp_path)

    assert roundtrip.shape == expected_rgb.shape, f"Kształt obrazu po konwersji {roundtrip.shape} nie zgadza się z oczekiwanym {expected_rgb.shape}"
    assert roundtrip.dtype == expected_rgb.dtype == np.uint8, f"Dtype obrazu po konwersji {roundtrip.dtype} nie zgadza się z oczekiwanym uint8"

    max_diff = _max_abs_diff(expected_rgb, roundtrip)
    assert max_diff <= 1, f"Maksymalna różnica bezwzględna {max_diff} przekracza próg 1"

