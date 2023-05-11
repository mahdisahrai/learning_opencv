import cv2
from cv2 import CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH

capture = cv2.VideoCapture(0)  # input
typev = cv2.VideoWriter_fourcc(*'XVID')  # format
out = cv2.VideoWriter('video.avi', typev, 20.0, (640, 480))  # path

while (capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        print(capture.get(CAP_PROP_FRAME_WIDTH))
        print(capture.get(CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        # cvtColor is used for giving filter to video
        color = cv2.cvtColor(frame, cv2.CAP_OPENNI_GRAY_IMAGE)
        cv2.imshow('frame', color)

        # waitKey is used for making slow videos and ord is key for exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


capture.release()
out.release()
cv2.destroyAllWindows()

