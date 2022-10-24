import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('roadone.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (500, 500))


def SetRegion(image, vertices):
    mask = np.zeros_like(image) #Return an array of zeros with the same shape and type as a given array
    match_mask_color = (255,) * 3
    cv2.fillPoly(mask, vertices, match_mask_color) #is used to draw filled polygons like rectangle, triangle, pentagon over an image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


height = img.shape[0]
width = img.shape[1]

areavertices = [(0, height), (width / 2, height / 2), (width, height)]

cropped = SetRegion(img, np.array([areavertices], np.int32))


plt.imshow(cropped)
plt.show()
cv2.destroyAllWindows()
