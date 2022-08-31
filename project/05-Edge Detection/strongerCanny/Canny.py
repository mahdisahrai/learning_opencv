import cv2
from matplotlib import pyplot as plt


img = cv2.imread("apple.jpg",0)  # Read image
canny1 = cv2.Canny(img, 90, 150)
canny2 = cv2.Canny(img, 100, 200)


title = ['image','canny1','canny2']
image = [img,canny1,canny2]


for i in range(3): #2-3
    plt.subplot(2,3,i+1), plt.imshow(image[i],'BrBG_r')
    plt.title(title[i])
    # plt.xticks([]),plt.yticks([]) #coordinate with ruler



plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
