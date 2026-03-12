import imageio.v3 as iio
from pathlib import Path
import os

# oczekiwane dane
expected_metadata = {
    "test_immeta_source/test_immeta_source1.jpg": {
        "mode": 'RGB',
        "shape": (6144, 8160),
        "Make": 'OPPO',
        "Model": 'OPPO A96',
        "DateTime": '2026:03:12 17:20:38',
    },
    "test_immeta_source/test_immeta_source2.jpg": {
        "mode": 'RGB',
        "shape": (4608, 3456),
        "Make": 'NIKON',
        "Model": 'COOLPIX B500',
        "DateTime": '2024:06:30 15:35:31',
    },
}

def test_immeta():
    """
    Test of imageio.v3.immeta functionality.
    """
    failed_images=[]
    for image_name, expected in expected_metadata.items():
        script_path=str(Path(__file__).parent)
        meta = iio.immeta(script_path+"\\"+image_name)
        test_passed = True
        #\033[31m - daje kolor czerwony, \033[0m - a to biały
        for key, value in expected.items():
            try:
                assert key in meta, f"{key} does not exist in metadata {image_name}"
                # tu sprawdza czy taka dan w ogóle istnieje
                try:
                    assert meta[key] == value, (
                        f"Wrong value in {image_name}: {key} = {meta[key]}, expected {value}")
                    # a tu czy się zgadza z zapisanymi
                except Exception as e:
                    print("\033[31m", type(e), e, "\033[0m")
                    test_passed = False
            except Exception as e:
                print("\033[31m", type(e),e, "\033[0m")
                test_passed = False


        if not test_passed:
            failed_images.append(image_name)
    if len(failed_images)>0:
        raise ValueError("<test_immeta failed> images:"+str(failed_images))
    else:
        print("\033[32m<test_immeta passed>\033[0m")


def read_meta(filepath):
    """
    Reads metadata from a file and formats it to paste in dictionary.
    """
    script_path = str(Path(__file__).parent)
    meta = iio.immeta(script_path+filepath)
    meta_dict = {
        "mode": meta.get("mode"),
        "shape": meta.get("shape"),
        "Make": meta.get("Make"),
        "Model": meta.get("Model"),
        "DateTime": meta.get("DateTime")
    }

    # Formatowanie jak w Python dict
    print(f'"{filepath}": {{')
    for k, v in meta_dict.items():
        print(f'    "{k}": {v!r},')
    print("},\n")


if __name__ == "__main__":
    test_immeta()