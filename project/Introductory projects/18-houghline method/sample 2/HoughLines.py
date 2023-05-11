import cv2
import numpy as np

img = cv2.imread('sudoku.png')
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(color, 50, 100, apertureSize=3)

houghline = cv2.HoughLinesP(edge, 1, np.pi / 150, 100, minLineLength=100, maxLineGap=20)

for line in houghline:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 12, 255), 2)

cv2.imshow('edge', edge)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
