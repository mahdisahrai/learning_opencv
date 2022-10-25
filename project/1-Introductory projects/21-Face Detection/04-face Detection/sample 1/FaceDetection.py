import cv2
from cvzone.FaceDetectionModule import FaceDetector

capture = cv2.VideoCapture(0)
detector = FaceDetector()

while (capture.isOpened()):
    ret, frame = capture.read()
    result, box = detector.findFaces(frame)


    # for example: {'id': 0, 'bbox': (295, 267, 273, 273), 'score': [0.8099899888038635], 'center': (431, 403)}
    if box:
        print(box[0])
        center = box[0]['center']
        cv2.circle(frame, center, 5, (0, 250, 0), 1)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(10) & 0xFF
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
