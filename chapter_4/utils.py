from matplotlib import pyplot as plt
from matplotlib import patches
import numpy as np


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_image_with_corners(image, coords, title="Corners detected"):
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title(title)
    plt.plot(coords[:, 1], coords[:, 0], '+r', markersize=15)
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


def show_detected_face(result, detected, title="Face image"):
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_cmap('gray')
    plt.title(title)
    plt.axis('off')
    for patch in detected:
        img_desc.add_patch(
            patches.Rectangle((patch['c'], patch['r']),
                              patch['width'],
                              patch['height'],
                              fill=False,
                              color='r',
                              linewidth=2))
    plt.show()


def getFace(d, image):
    ''' Extracts the face rectangle from the image using the coordinates of the detected.'''
    # X and Y starting points of the face rectangle
    x, y = d['r'], d['c']
    # The width and height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']
    # Extract the detected face
    face = image[x:width, y:height]
    return face


def mergeBlurryFace(original, gaussian_image, d):
    # X and Y starting points of the face rectangle
    x, y = d['r'], d['c']
    # The width and height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']
    original[x:width, y:height] = gaussian_image
    return original
