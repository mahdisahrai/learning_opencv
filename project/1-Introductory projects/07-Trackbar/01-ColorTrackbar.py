import cv2
import numpy as np


def show(x):
    print(x)


img = np.zeros((300, 500, 3), np.uint8)
cv2.namedWindow('trackbar')

cv2.createTrackbar('B', 'trackbar', 0, 255, show)
cv2.createTrackbar('G', 'trackbar', 0, 255, show)
cv2.createTrackbar('R', 'trackbar', 0, 255, show)


while (1):

    K = cv2.waitKey(1) & 0xFF
    if K == 30:
        break

    b = cv2.getTrackbarPos('B', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    r = cv2.getTrackbarPos('R', 'trackbar')
    img[:] = [b, g, r]

    cv2.imshow('trackbar', img)




cv2.destroyAllWindows()
