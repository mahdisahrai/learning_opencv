import cv2
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt


img = cv2.imread("fruits.jpg", cv2.IMREAD_GRAYSCALE)  # Read image
canny = cv2.Canny(img, 100, 200)
title = ['canny']
image = [canny]



for i in range(1):
    plt.subplot(1, 1, i + 1), plt.imshow(image[i], 'BrBG_r')
    plt.title(title[i])
    # plt.xticks([]), plt.yticks([])  # coordinate with ruler



def on_click(event):
    if event.button is MouseButton.LEFT:
        x = event.x
        y = event.y
        print(x,y)



plt.connect('button_press_event', on_click)
plt.show()

