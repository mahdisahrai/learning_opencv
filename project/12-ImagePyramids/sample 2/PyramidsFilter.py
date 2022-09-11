import cv2
import numpy as np


apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
kernal = np.ones((5, 5), np.float32) / 25
filter = cv2.filter2D(orange, -1, kernal)

combine = np.hstack((apple[:, :230], filter[:, 256:]))

layer = combine.copy()


for i in range(4):
    layer = cv2.pyrDown(layer)
    cv2.imshow(str(i), layer)


print(apple.shape)
print(orange.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
