import imageio.v3 as iio
from pathlib import Path
import os
import numpy as np
import pytest

# W folderze Tests stworzyć plik test_read_img.py. 
# Test ma sprawdzać czy funkcja wczytująca działa, 
# sprawdzić możliwość wczytywania plików z internetu


def test_read_img():
    """Test loading a local bundled image using imageio."""
    im = iio.imread('imageio:chelsea.png')
    assert im is not None
    #Sprawdza czy funkcja działa
    assert isinstance(im, np.ndarray)
    assert im.shape == (300, 451, 3)
    assert im.dtype == np.uint8
    #Sprawdza czy obrazek został odczytany


def test_imread_from_internet():
    """Test loading an image from the internet."""
    # Using a small PNG image from a reliable source
    url = 'https://github.com/DanielMierzwa/OOB_Tests-ImageIO/blob/feature/test_read_img.py/tests/functional/test_immeta_source/test_immeta_source1.jpg?raw=true'

    im = iio.imread(url)
    assert im is not None
    #Sprawdza czy funkcja działa
    assert isinstance(im, np.ndarray)
    assert im.ndim == 3
    assert im.shape[2] == 3  # RGB image
    assert im.dtype == np.uint8
    #Sprawdza czy obrazek został odczytany
