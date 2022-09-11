import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')

b, g, r = cv2.split(img)

calchist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])


plt.plot(calchist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
