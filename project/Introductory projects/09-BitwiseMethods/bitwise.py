import cv2
import numpy as np

img1 = np.zeros((400, 300, 3), np.uint8)
img2 = np.zeros((400, 300, 3), np.uint8)

img1 = cv2.rectangle(img1, (189, 0), (98, 90), (255, 255, 255), -1)
img2 = cv2.rectangle(img2, (299, 0), (146, 399), (255, 255, 255), -1)

bitand = cv2.bitwise_and(img2, img1)
bitor = cv2.bitwise_or(img2, img1)
bitxor = cv2.bitwise_xor(img2, img1)
bitnot = cv2.bitwise_not(bitxor)  # in reverse

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitwise_and', bitand)
cv2.imshow('bitwise_or', bitor)
cv2.imshow('bitwise_xor', bitxor)
cv2.imshow('bitwise_not', bitnot)

cv2.waitKey(0)
cv2.destroyAllWindows()
