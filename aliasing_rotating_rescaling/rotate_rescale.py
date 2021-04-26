from skimage import data
from skimage.transform import rotate, rescale
from utils import show_image

image = data.cat()
show_image(image)

# Rotate the image 90 degrees clockwise
rotated_img = rotate(image, -90)
show_image(rotated_img, 'rotated_img')

# Rescale with anti aliasing
rescaled_with_aa = rescale(rotated_img,
                           1 / 4,
                           anti_aliasing=True,
                           multichannel=True)

# Rescale without anti aliasing
rescaled_without_aa = rescale(rotated_img, 1 / 4)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")
