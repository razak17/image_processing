from matplotlib import pyplot as plt
from skimage.restoration import inpaint
from utils import show_image, get_mask

image = plt.imread('images/damaged_astronaut.png')

mask = get_mask(image)

restored_image = inpaint.inpaint_biharmonic(image, mask, multichannel=True)

# Show the defective image
show_image(image, 'Image to restore')
show_image(restored_image)
