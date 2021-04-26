from matplotlib import pyplot as plt
import numpy as np
from skimage.restoration import inpaint
from utils import show_image

image = plt.imread('images/image_with_logo.png')

mask = np.zeros(image.shape[:-1])

# Set the pixels where the logo is to 1
mask[210:290, 360:425] = 1

logo_removed = inpaint.inpaint_biharmonic(image, mask, multichannel=True)

# Show the original and logo removed images
show_image(image, 'Image with logo')
show_image(logo_removed, 'Image with logo removed')
