import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("fruits.jpg", cv2.IMREAD_GRAYSCALE)  # Read image

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

canny = cv2.Canny(img, 100, 200)

result = cv2.bitwise_or(sobelX, sobelY)

title = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelcombined', 'canny']
image = [img, lap, sobelX, sobelY, result, canny]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i], 'BrBG_r')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # coordinate with ruler



plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

