from matplotlib import pyplot as plt
from skimage import exposure
from utils import show_image

image_coffee = plt.imread('images/coffee.png')
show_image(image_coffee)

adapthist_img = exposure.equalize_adapthist(image_coffee, clip_limit=0.03)

show_image(adapthist_img, "adapthist_img")
