import cv2
from matplotlib import pyplot as plt

img = cv2.imread('home.jpg')

# surf = cv2.xfeatures2d.SURF_create()  # surf method

sift = cv2.SIFT_create()  # sift method
orb = cv2.ORB_create(nfeatures=500)  # (nfeatures: precision)   "  orb method

sift_keypoints, descriptor1 = sift.detectAndCompute(img, None)
orb_keypoints, descriptor2 = orb.detectAndCompute(img, None)

draw1 = cv2.drawKeypoints(img, sift_keypoints, None)
draw2 = cv2.drawKeypoints(img, orb_keypoints, None)

title = ['sift', 'orb']
image = [draw1, draw2]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # coordinate with ruler

plt.show()
