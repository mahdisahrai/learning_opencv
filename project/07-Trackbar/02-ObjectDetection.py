import cv2
import numpy as np


def show(x):
    print(x)


# cap = cv2.VideoCapture(0)

cv2.namedWindow('trackbar')
cv2.createTrackbar('lh', 'trackbar', 0, 255, show)
cv2.createTrackbar('ls', 'trackbar', 0, 255, show)
cv2.createTrackbar('lv', 'trackbar', 0, 255, show)
cv2.createTrackbar('uh', 'trackbar', 255, 255, show)
cv2.createTrackbar('us', 'trackbar', 255, 255, show)
cv2.createTrackbar('uv', 'trackbar', 255, 255, show)

while (True):

    key = cv2.waitKey(1)
    if key == 30:
        break

    # ret , img = cap.read()
    cv2.namedWindow('image')
    img = cv2.imread('smarties.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('lh', 'trackbar')
    ls = cv2.getTrackbarPos('ls', 'trackbar')
    lv = cv2.getTrackbarPos('lv', 'trackbar')
    uh = cv2.getTrackbarPos('uh', 'trackbar')
    us = cv2.getTrackbarPos('us', 'trackbar')
    uv = cv2.getTrackbarPos('uv', 'trackbar')

    one = np.array([lh, ls, lv])
    two = np.array([uh, us, uv])

    mask = cv2.inRange(hsv, one, two)
    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)




# cap.release()
cv2.destroyAllWindows()

