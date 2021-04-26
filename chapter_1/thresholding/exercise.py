from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_local, threshold_otsu


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


shapes = plt.imread('images/shapes.jpg')
shapes_gray = rgb2gray(shapes)

block_size = 35

local_thresh = threshold_local(shapes_gray, block_size, offset=10)
global_thresh = threshold_otsu(shapes_gray)

binary_local = shapes_gray > local_thresh
binary_global = shapes_gray > global_thresh

show_image(binary_global)
