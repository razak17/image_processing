from matplotlib import pyplot as plt
from skimage.segmentation import slic
from skimage.color import label2rgb
from utils import show_image

image = plt.imread('images/chinese.jpg')

# Obtain the segmentation with 400 regions
segments = slic(image, start_label=1, n_segments=400)

# Put segments on top of original image to compare
segmented_image = label2rgb(segments, image, kind='avg', bg_label=0)

# Show the segmented image
# show_image(image)
show_image(segmented_image, "Segmented image, 400 superpixels")
