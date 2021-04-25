from matplotlib import pyplot as plt
from skimage import exposure
from utils import show_image, show_histogram

chest_xray_img = plt.imread('images/chest_xray.png')

show_image(chest_xray_img, "Chest x-ray")
show_histogram(chest_xray_img.ravel())

chest_xray_img_eq = exposure.equalize_hist(chest_xray_img)
show_image(chest_xray_img_eq, 'Resulting image')
