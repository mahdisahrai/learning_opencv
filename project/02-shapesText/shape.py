import cv2
import numpy as np

img = cv2.imread('cards.png', 0)
# img = np.zeros([512,512,3],np.uint8) #black background

font = cv2.FONT_ITALIC

img = cv2.line(img, (0, 0), (383, 304), (147, 96, 44,), 10)
img = cv2.arrowedLine(img, (0, 304), (383, 304), (147, 96, 44), 10)
img = cv2.rectangle(img, (400, 150), (298, 200), (147, 96, 44), 5)
img = cv2.circle(img, (490, 244), 50, (0, 250, 0), -1)
img = cv2.putText(img,'working with shapes',(232,31),font,1,(147, 96, 44),2,cv2.LINE_AA)

cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()

