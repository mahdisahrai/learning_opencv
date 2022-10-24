import cv2

video = cv2.VideoCapture('vtest.avi')
kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
subtraction = cv2.bgsegm.createBackgroundSubtractorCNT()
# subtraction = cv2.createBackgroundSubtractorKNN()

while (True):
    ret, frame = video.read()
    color = cv2.cvtColor(frame, cv2.COLOR_YCrCb2RGB)
    if frame is None:  # is: it's the address of the frame
        break
    outcome = subtraction.apply(color)
    final = cv2.morphologyEx(outcome, cv2.MORPH_OPEN, kernal) #are some simple operations based on the image shape. It is normally performed on binary images

    cv2.imshow('main', frame)
    cv2.imshow('subtraction', final)

    if cv2.waitKey(31) & 0xFF == ord('a'):
        break

video.release()
cv2.destroyAllWindows()
