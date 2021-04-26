from skimage.filters import try_all_threshold
from skimage.color import rgb2gray
from matplotlib import pyplot as plt

fruits = plt.imread('images/fruits.jpg')
fruits_gray = rgb2gray(fruits)

fig, ax = try_all_threshold(fruits_gray, verbose=False)

plt.show()
