import cv2

image1 = cv2.imread('messi5.jpg')
image2 = cv2.imread('opencv-logo.png')

b, r, g = cv2.split(image1)
image1 = cv2.merge((b, r, g))

crop = image1[243:294, 413:464]  # [y1:y2, x1:x2]
image1[155:206, 183:234] = crop  # moving the cropped part

image1 = cv2.resize(image1, (512, 512))
image2 = cv2.resize(image2, (512, 512))

outcome1 = cv2.addWeighted(image1, .2, image2, .8, 0)
outcome2 = cv2.add(image1, image2)

cv2.imshow('crop', crop)
cv2.imshow('addWeighted', outcome1)
cv2.imshow('add', outcome2)

print(image1.shape)
print(image1.size)
print(image1.dtype)

cv2.waitKey(0)
cv2.destroyAllWindows()
