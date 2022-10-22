import cv2
import numpy as np

img = cv2.imread('sudoku.png')
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(color, 50, 100, apertureSize=3)

houghline = cv2.HoughLines(edge, 1, np.pi / 155, 170)

for line in houghline:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x = a * rho
    y = b * rho
    x1 = int(x + 1000 * (-b))
    y1 = int(y + 1000 * (a))
    x2 = int(x - 1000 * (-b))
    y2 = int(y - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 12, 255), 1)

cv2.imshow('edge', edge)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
