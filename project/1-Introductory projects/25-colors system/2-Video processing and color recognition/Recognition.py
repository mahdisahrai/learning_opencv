import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while (True):
    rec, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # https://www.w3schools.com/colors/colors_rgb.asp  *  website RGB Calculator
    lower_red = np.array([50, 50, 100])
    upper_red = np.array([253, 191, 255])

    mask_detect = cv.inRange(hsv, lower_red, upper_red)  # detecting object
    bitwise_and = cv.bitwise_and(frame, frame, mask=mask_detect)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask_detect)
    cv.imshow('separate', bitwise_and)

    keyexit = cv.waitKey(2) & 0xFF
    if keyexit == 27:
        break

cv.destroyAllWindows()
cap.release()
