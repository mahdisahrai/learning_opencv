import cv2
import numpy as np

main_img = cv2.imread('back.jpg')
hsv = cv2.cvtColor(main_img, cv2.COLOR_BGR2HSV)

# bgr value
lower_red = np.array([0, 100, 50]) #Bold color
upper_red = np.array([10, 200, 255]) #light color

mask = cv2.inRange(hsv, lower_red, upper_red) # detecting object

# about inpaint:
# The function reconstructs the selected image area from the pixel near the area boundary.
# The function may be used to remove dust and scratches from a scanned photo,
# or to remove undesirable objects from still images or video
inpaint = cv2.inpaint(main_img, mask, 15, flags=cv2.INPAINT_TELEA)

cv2.imshow('main', main_img)
cv2.imshow('mask', mask)
cv2.imshow('inpaint', inpaint)

cv2.waitKey(0)
cv2.destroyAllWindows()
