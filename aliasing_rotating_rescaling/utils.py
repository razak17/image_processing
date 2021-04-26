from matplotlib import pyplot as plt


def show_image(image, title="Image", cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show_histogram(x, title="Histogram of Image", bins=256):
    plt.hist(x, bins=bins)
    plt.title(title)
    plt.show()
