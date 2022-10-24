import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

capture = cv.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)

while (capture.isOpened()):
    ret, frame = capture.read()
    hand, img = detector.findHands(frame)

    if hand:
        first_hand = hand[0]
        imlist = first_hand["lmList"]  # lmList is landmark list
        length, info, frame = detector.findDistance(imlist[4][:-1], imlist[5][:-1], frame) #[:-1] = The first two arguments

        print(length)
        cv.imshow('frame', frame)

    key = cv.waitKey(10) & 0xFF
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()
