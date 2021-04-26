from matplotlib import pyplot as plt
import numpy as np


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_histogram(x, title="Histogram of Image", bins=256):
    plt.hist(x, bins=bins)
    plt.title(title)
    plt.show()


def get_mask(image):
    mask = np.zeros(image.shape[:-1])
    mask[101:106, 0:240] = 1

    mask[152:154, 0:60] = 1
    mask[153:155, 60:100] = 1
    mask[154:156, 100:120] = 1
    mask[155:156, 120:140] = 1
    mask[212:217, 0:150] = 1
    mask[217:222, 150:256] = 1
    return mask
