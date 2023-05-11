import cv2
from matplotlib import pyplot as plt

img = cv2.imread('fruits.jpg', 0)


plt.hist(img.ravel(), 256, [0, 256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
