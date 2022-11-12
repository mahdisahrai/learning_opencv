import cv2
import numpy as np

main_img = cv2.imread('back.jpg')

gray_mask = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
mask = np.zeros((gray_mask.shape), dtype=np.uint8)


mask[88:139,613:705] = 255    # [y1:y2, x1:x2]  #255: color


masked_bitwise = cv2.bitwise_and(gray_mask,gray_mask,mask=mask)


# about inpaint:
#The function reconstructs the selected image area from the pixel near the area boundary. 
#The function may be used to remove dust and scratches from a scanned photo, 
# or to remove undesirable objects from still images or video
inpaint = cv2.inpaint(main_img, masked_bitwise, 7, flags=cv2.INPAINT_TELEA)


cv2.imshow('main', main_img)
cv2.imshow('mask',  mask)
cv2.imshow('bitwise', masked_bitwise)
cv2.imshow('inpaint', inpaint)

cv2.waitKey(0)
cv2.destroyAllWindows()
