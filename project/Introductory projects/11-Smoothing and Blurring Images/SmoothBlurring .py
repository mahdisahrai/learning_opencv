import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('home.jpg', 0)
kernal = np.ones((5, 5), np.float32) / 25


filter = cv2.filter2D(img, -1, kernal)
blur = cv2.blur(img, (20, 20))
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
median = cv2.medianBlur(img, 5)


title = ['image', '2D convolution', 'blur', 'GaussianBlur', 'bilateralFilter', 'medianBlur']
image = [img, filter, blur, gaussian_blur, bilateral, median]


for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # coordinate with ruler



plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
