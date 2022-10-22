import cv2

eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

img = cv2.imread('face.jpeg') #or adding video

eye = eye_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in eye:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
