from skimage import morphology
from matplotlib import pyplot as plt
from utils import show_image

world_img = plt.imread('images/world_image.jpg')

dilated_img = morphology.binary_dilation(world_img)
show_image(world_img, 'Original')
show_image(dilated_img, 'Dilated image')
