import cv2
import numpy as np

# input
capture = cv2.VideoCapture('traffic.mp4')

ret, frame = capture.read()

x, y, w, h = 300, 200, 100, 50
track = (x, y, w, h)
color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(color, np.array((0, 60., 32.)), np.array((180., 255., 255))) #Detect an object based on the range of pixel values in the HSV colorspace
hist = cv2.calcHist([color], [0], mask, [180], [0, 180]) #calcHist() function to calculate the image histograms
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX) #The normalize() function returns the normalized image as the output
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 3, 1) #for locating the maxima of a density function

while (True):

    ret, frame = capture.read()
    if ret == True:
        crop = frame[y:y + h, x: x + w]  # [y1:y2, x1:x2]
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], hist, [0, 180], 1) # calcBackProject calculates the back project of the histogram

        ret, track = cv2.CamShift(dst, track,term_crit) #CamShift is a object tracking algorithm

        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        final = cv2.polylines(frame,[pts],True,(0,255,0),1)

        cv2.imshow('dst', dst) # dst: depth of the destination image
        cv2.imshow('roi', crop)
        cv2.imshow('final', final)

        key = cv2.waitKey(32) & 0xFF
        if key == 27:
            break
    else:
        break
        
        
        
cv2.destroyAllWindows()
