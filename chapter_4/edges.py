from skimage.feature import canny, corner_harris
from skimage.color import rgb2gray
from matplotlib import pyplot as plt
from utils import show_image

image = plt.imread('images/grape_fruit.jpg')
grayscale_image = rgb2gray(image)
canny_edges = canny(grayscale_image)

show_image(image)
show_image(grayscale_image)
show_image(canny_edges, "Edges with Canny")
