from matplotlib import pyplot as plt
from skimage.transform import resize
from utils import show_image

dogs_banner = plt.imread('images/dogs.jpg')

# Set proportional height so its half its size
height = int(dogs_banner.shape[0] / 2)
width = int(dogs_banner.shape[1] / 2)

image_resized = resize(dogs_banner, (height, width), anti_aliasing=True)

# Show the original and rotated image
show_image(dogs_banner, 'Original')
show_image(image_resized, 'Resized image')
