import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('smarties.png', 0)
kernal = np.ones((5, 5), np.uint8)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

dilation = cv2.dilate(mask, kernal, iterations=2)  # dilation rate
erosion = cv2.erode(mask, kernal, iterations=2)  # Erosion rate
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)


title = ['image', 'mask', 'dilation', 'erosion', 'gradient', 'opening']
image = [img, mask, dilation, erosion, gradient, opening]


for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # coordinate with ruler


plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
