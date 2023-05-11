import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp

capture = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)

while (capture.isOpened()):
    ret, frame = capture.read()

    hand, img = detector.findHands(frame)

    cv.imshow('frame', frame)

    key = cv.waitKey(2) & 0xFF
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()
