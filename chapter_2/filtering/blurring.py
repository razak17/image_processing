from matplotlib import pyplot as plt
from skimage.filters import gaussian
from utils import show_image

image = plt.imread('images/sharp.jpg')

gaussian_img = gaussian(image, multichannel=False)

show_image(image, "Original")
show_image(gaussian_img, "Reduced sharpness Gaussian")
