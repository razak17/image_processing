import numpy as np
from matplotlib import pyplot as plt


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_histogram(x, title="Image", bins=256):
    plt.hist(x, bins=bins)
    plt.title(title)
    plt.show()


image = plt.imread('woman.jpg')

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

show_image(red, "Red Image")
show_image(green, "Green Image")
show_image(blue, "Blue Image")

show_histogram(red.ravel(), "Red Histogram")
show_histogram(green.ravel(), "Green Histogram")
show_histogram(blue.ravel(), "Blue Histogram")
