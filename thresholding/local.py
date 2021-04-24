from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
from matplotlib import pyplot as plt

chess_pieces = plt.imread('images/bw.jpg')
chess_pieces_gray = rgb2gray(chess_pieces)

thresh = threshold_otsu(chess_pieces_gray)
binary = chess_pieces_gray > thresh

plt.imshow(chess_pieces, cmap="gray")
plt.show()

plt.imshow(chess_pieces_gray, cmap="gray")
plt.show()

plt.imshow(binary, cmap="gray")
plt.show()
