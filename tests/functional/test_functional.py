import imageio.v3 as iio

# Do usunięcia w dalszych iteracjach projektu
def test_placeholder():
    read_img = iio.imread('imageio:chelsea.png')
    assert read_img.shape is not None
