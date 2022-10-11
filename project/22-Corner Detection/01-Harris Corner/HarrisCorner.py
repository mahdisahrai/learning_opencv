import cv2
import numpy as np

img = cv2.imread('chess.png')
img = cv2.resize(img, (500, 500))
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(color)

dst = cv2.cornerHarris(gray, 6, 7, 0.01)  # 2,3
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [100, 0, 155]

cv2.imshow('output', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
