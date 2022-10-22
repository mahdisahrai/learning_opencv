import datetime
import cv2


capture = cv2.VideoCapture(0)
capture.set(3,720)
capture.set(4,450)


while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:

        date = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        coordinate = 'width: ' + str(capture.get(3)) + '    height: ' + str(capture.get(4))
        frame = cv2.putText(frame, date, (62, 58), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, coordinate, (62, 430), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        color = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

        cv2.imshow('frame', color)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



capture.release()
cv2.destroyAllWindows()
