from matplotlib import pyplot as plt
from skimage import morphology
from utils import show_image

r_img = plt.imread('images/r.png')

eroded_r_img_shape = morphology.binary_erosion(r_img)

show_image(r_img, 'Original')
show_image(eroded_r_img_shape, 'Eroded image')
