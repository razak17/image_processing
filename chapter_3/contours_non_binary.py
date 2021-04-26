from matplotlib import pyplot as plt
from skimage import measure, filters
from skimage.color.colorconv import rgba2rgb, rgb2gray
from utils import show_image
import numpy as np

image_dice = plt.imread('images/dices.png')

# Make the image grayscale
image_dice = rgb2gray(rgba2rgb(image_dice))

# Obtain the optimal thresh value
thresh = filters.threshold_otsu(image_dice)

# Apply thresholding
binary = image_dice > thresh

# Find contours at a constant value of 0.8
contours = measure.find_contours(binary, 0.8)

# show_image(image_dice)

# Create list with the shape of each contour
shape_contours = [cnt.shape[0] for cnt in contours]

# Set 50 as the maximum size of the dots shape
max_dots_shape = 50

# Count dots in contours excluding bigger than dots size
dots_contours = [cnt for cnt in contours if np.shape(cnt)[0] < max_dots_shape]

print("Dice's dots number: {}. ".format(len(dots_contours)))
