import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('book1.png')
img2 = cv2.imread('book2.png')

orb = cv2.ORB_create(nfeatures=500)  # (nfeatures: precision)   "  orb method

# descriptor describe elementary characteristics such as the shape, the color, the texture or the motion
orb_keypoints1, descriptor1 = orb.detectAndCompute(img1, None)
orb_keypoints2, descriptor2 = orb.detectAndCompute(img2, None)

# bf: Brute-force descriptor matcher.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) #is used for matching the features of the first image with another image
matches = bf.match(descriptor1, descriptor2)

matches = sorted(matches, key=lambda x: x.distance) #sorting
image_matches = cv2.drawMatches(img1, orb_keypoints1, img2, orb_keypoints2, matches[:20], None, flags=2)

plt.imshow(image_matches)
plt.show()
