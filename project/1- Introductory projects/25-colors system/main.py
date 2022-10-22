import cv2

img = cv2.imread('shapes.png') # opencv(bgr) , plt(rgb)
blue, green, red = cv2.split(img) # RGB(Red,Green,Blue)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # HSV is a good choice of color space for segmenting by color


cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.imshow('hsv', hsv)
cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()
