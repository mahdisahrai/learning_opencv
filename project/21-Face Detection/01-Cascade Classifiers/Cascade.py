import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('messi5.jpg') #or adding video

face = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

