import cv2
import numpy as np

img = cv2.imread('pic3.png')
img = cv2.resize(img, (500, 500))
color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.goodFeaturesToTrack(color,11,0.01,10) #Determines strong corners on an image

print(np.int0(corner))
corner = np.int0(corner)


for i in corner:
    x,y = i.ravel() #ravel returns contiguous array
    cv2.circle(img,(x,y),3,(12,23,255),-1)


cv2.imshow('output', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
