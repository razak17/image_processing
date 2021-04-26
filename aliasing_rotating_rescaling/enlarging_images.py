from skimage import data
from skimage.transform import resize
from utils import show_image

rocket_img = data.rocket()
# show_image(rocket_img)

# Enlarge the image so it is 3 times bigger
height = int(rocket_img.shape[0] / 3)
width = int(rocket_img.shape[1] / 3)

# print(rocket_img.shape[0] / 3)
# print(rocket_img.shape[1] / 3)

enlarged_rocket_image = resize(rocket_img, (height, width), anti_aliasing=True)
show_image(enlarged_rocket_image)
