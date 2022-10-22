import cv2
import numpy as np

img = cv2.imread('smarties.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
houghcircle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 30,
                               param1=50, param2=35, minRadius=0, maxRadius=0)

circle = np.uint16(np.around(houghcircle))

for (x, y, r) in circle[0, :]:
    cv2.circle(img, (x, y), r, (0, 52, 0), 3)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
