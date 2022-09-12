import cv2

img1 = cv2.imread('src1.jpg')
img2 = cv2.imread('src2.jpg')

img3 = cv2.imread('apple.jpg')
img4 = cv2.imread('orange.jpg')

#difference between two arrays when they have the same size and type
diff1 = cv2.absdiff(img1, img2)
diff2 = cv2.absdiff(img3, img4)

cv2.imshow('output1', diff1)
cv2.imshow('output2', diff2)

cv2.waitKey(0)
cv2.destroyAllWindows()

