from matplotlib import pyplot as plt
import numpy as np

image = plt.imread('images/chinese.jpg')

height = np.shape(image)[0]
width = np.shape(image)[1]
pixels = height * width
print(pixels)
