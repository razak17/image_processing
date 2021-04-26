from matplotlib import pyplot as plt
from skimage import exposure
from utils import show_image

image_aerial = plt.imread('images/city.png')
show_image(image_aerial)

image_aerial_eq = exposure.equalize_hist(image_aerial)
show_image(image_aerial_eq)
