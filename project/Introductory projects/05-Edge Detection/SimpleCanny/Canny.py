import cv2


img = cv2.imread("apple.jpg")  # Read image


t_lower = 90  # Lower Threshold
t_upper = 150  # Upper threshold



edge = cv2.Canny(img, t_lower, t_upper)



cv2.imshow('image', img)
cv2.imshow('edge', edge)



cv2.waitKey(0)
cv2.destroyAllWindows()
