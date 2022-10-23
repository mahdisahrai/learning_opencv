import cv2

img = cv2.imread('room_ser.jpg')

# blob: It returns a 4-dimensional array/blob for the input image
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

for b in blob:
    for n, blob1 in enumerate(b):
        cv2.imshow(str(n), blob1)


cv2.waitKey(0)
cv2.destroyAllWinedows()
