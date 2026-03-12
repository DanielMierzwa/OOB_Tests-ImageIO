import imageio.v3 as iio

def test_placeholder():
    read_img = iio.imread('imageio:chelsea.png')
    assert read_img.shape is not None
