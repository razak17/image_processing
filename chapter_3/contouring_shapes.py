from skimage import data, measure
from utils import show_image

horse_image = data.horse()
contours = measure.find_contours(horse_image, 0.8)

show_image(horse_image)
show_image(contours)
