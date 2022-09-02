import cv2
import cv2 as cv


img = cv2.imread('starry_night.jpg',0)

_, th1 = cv.threshold(img,150,200,cv.THRESH_BINARY)
_, th2 = cv.threshold(img,150,200,cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img,150,200,cv.THRESH_TRUNC)
_, th4 = cv.threshold(img,150,200,cv.THRESH_TOZERO)


cv2.imshow('image',img)

cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)


cv2.waitKey(0)
cv2.destroyAllWindows()
