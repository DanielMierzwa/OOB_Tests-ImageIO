import warnings
from pathlib import Path
from PIL import Image
import imageio.v3 as iio
import time
def test_load_time():
    Image.MAX_IMAGE_PIXELS = None
    # Ukrycie warningów DecompressionBombWarning
    warnings.simplefilter('ignore', Image.DecompressionBombWarning)

    image_path = str(Path(__file__).parent) +"\\test_load_time_source.jpg"
    repeats = 50

    times = []
    print(image_path)
    for _ in range(repeats):
        start = time.perf_counter()
        img = iio.imread(image_path)
        end = time.perf_counter()

        times.append(end - start)

    avg_time = sum(times) / repeats

    assert avg_time < 0.7
if __name__ == "__main__":
    test_load_time()