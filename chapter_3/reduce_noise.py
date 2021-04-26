from matplotlib import pyplot as plt
from skimage.restoration import denoise_tv_chambolle
from utils import show_image

image = plt.imread('images/miny.jpeg')

denoised_image = denoise_tv_chambolle(image, multichannel=True)

show_image(image)
show_image(denoised_image, "Denoised Image")
