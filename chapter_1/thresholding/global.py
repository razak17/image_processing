from skimage.filters import threshold_otsu, threshold_local
from skimage.color import rgb2gray, rgba2rgb
from matplotlib import pyplot as plt


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


# Load image
image = plt.imread('images/tw.png')

# Convert two grayscale
image_gray = rgb2gray(rgba2rgb(image))

block_size = 35

local_thresh = threshold_local(image_gray, block_size, offset=10)
global_thresh = threshold_otsu(image_gray)

binary_local = image_gray > local_thresh
binary_global = image_gray > global_thresh

show_image(image)
show_image(binary_local, title="Local Thresholding")
show_image(binary_global, title="Global Thresholding")
