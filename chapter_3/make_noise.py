from matplotlib import pyplot as plt
from skimage.util import random_noise
from utils import show_image

image = plt.imread('images/fruits_image.jpg')

noisy_image = random_noise(image)

show_image(image)
show_image(noisy_image, "Noisy Image")
