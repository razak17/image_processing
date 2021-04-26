import numpy as np
from matplotlib import pyplot as plt


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


# Load image
seville_img = plt.imread('sevilleup.jpg')

# Flip the image vertically
seville_vertical_flip = np.flipud(seville_img)
# Flip the image horizontally
seville_horzontal_flip = np.fliplr(seville_vertical_flip)

show_image(seville_img, 'Original image')
show_image(seville_vertical_flip, 'Vertically flipped image')
show_image(seville_horzontal_flip, 'Corrected image')
