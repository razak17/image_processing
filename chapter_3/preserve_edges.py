from matplotlib import pyplot as plt
from skimage.restoration import denoise_bilateral
from utils import show_image

image = plt.imread('images/noise-noisy-nature.jpg')

denoised_image = denoise_bilateral(image, multichannel=True)

show_image(image)
show_image(denoised_image, "Denoised Image")
