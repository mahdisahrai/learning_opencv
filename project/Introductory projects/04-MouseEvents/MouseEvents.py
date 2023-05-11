import cv2
import numpy as np



img = np.zeros([512, 512, 3], np.uint8)



def clicks(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN: #EVENT_RBUTTONDOWN is left click
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_DUPLEX
        res = str(x) + ', ' + str((y))
        cv2.putText(img, res, (x, y), font, 1, (255, 255, 0), 2, cv2.CV_32F)
        cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN: #EVENT_RBUTTONDOWN is right click
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_DUPLEX
        res = str(x) + ', ' + str((y))
        cv2.putText(img, res, (x, y), font, 1, (255, 255, 255), 2, cv2.CV_32F)
        cv2.imshow('image', img)



cv2.imshow('image', img)
cv2.setMouseCallback('image', clicks)


cv2.waitKey(0)
cv2.destroyAllWindows()
