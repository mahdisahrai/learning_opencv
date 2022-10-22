import cv2
from tracker import *

tracker = EuclideanDistTracker()  # Creating tracker object
capture = cv2.VideoCapture('highway.mp4')  # input
detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40) # setting subtraction

while (capture.isOpened()):

    arr = []

    ret, frame = capture.read()
    crop = frame[340:720, 500:800]  # [y1:y2, x1:x2]
    mask = detector.apply(crop)
    _, mask = cv2.threshold(mask, 150, 200, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Calculating areas and removing small elements
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            x, y, w, h = cv2.boundingRect(contour)
            # cv2.drawContours(crop, [contour], -1, (0, 0, 90), 2)
            arr.append([x, y, w, h])

    # Object Tracking
    boxes_ids = tracker.update(arr)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(crop, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (157, 0, 0), 2)
        cv2.rectangle(crop, (x, y), (x + w, y + h), (0, 255, 0), 3)


    cv2.imshow('crop', crop)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        break

cv2.destroyAllWindows()
