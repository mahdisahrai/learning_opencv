import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('roadone.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img = cv2.resize(img, (500, 500))


def SetRegion(image, vertices):
    mask = np.zeros_like(image)  # Return an array of zeros with the same shape and type as a given array
    match_mask_color = (255,) * 3 #it replicates 255 for two times in an arr like it (255,255,255)
    cv2.fillPoly(mask, vertices,
                 match_mask_color)  # is used to draw filled polygons like rectangle, triangle, pentagon over an image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def DrawingLines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        x1, y1, x2, y2 = line[0] # or   for x1, y1, x2, y2 in line

        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)

    # gamma is scaler added to each sum
    img = cv2.addWeighted(img, 1, blank_image, 1, 0.5) #addWeighted() helps in transition of the image to another.  in order to blend image 
    return img


height = img.shape[0]
width = img.shape[1]

areavertices = [(0, height), (width / 2, height / 2), (width, height)]

color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(color, 100, 155)
cropped = SetRegion(canny, np.array([areavertices], np.int32))

#rho is measured in pixels and theta is measured in radians 
houghline = cv2.HoughLinesP(cropped, rho=6, theta=np.pi / 180, threshold=160, lines=np.array([]),
                            minLineLength=100, maxLineGap=80)

final_lines = DrawingLines(img, houghline)

plt.imshow(final_lines)
plt.show()
cv2.destroyAllWindows()
