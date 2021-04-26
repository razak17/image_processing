from skimage import color
from skimage.filters import sobel
from matplotlib import pyplot as plt


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


soaps = plt.imread('images/soaps.jpg')
soaps_gray = color.rgb2gray(soaps)

edge_sobel = sobel(soaps_gray)

show_image(soaps, "Original")
show_image(edge_sobel, "Edges with Sobel")
