import cv2

main_img = cv2.imread('sign.jpg')
gray_mask = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(gray_mask, 170, 255, cv2.THRESH_BINARY)
masked_dilate = cv2.dilate(mask, (12, 12), iterations=3)


# about inpaint:
# The function reconstructs the selected image area from the pixel near the area boundary.
# The function may be used to remove dust and scratches from a scanned photo,
# or to remove undesirable objects from still images or video
inpaint = cv2.inpaint(main_img, masked_dilate, 15, flags=cv2.INPAINT_TELEA)


cv2.imshow('mask', mask)
cv2.imshow('main', inpaint)

cv2.waitKey(0)
cv2.destroyAllWindows()
