import cv2

img = cv2.imread('smarties.png')
img = cv2.resize(img, (400, 400))



#FindContours supports only CV_8UC1 images when mode != CV_RETR_FLOODFILL
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(color, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


print(len(contours))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
