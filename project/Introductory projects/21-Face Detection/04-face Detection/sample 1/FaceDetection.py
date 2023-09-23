# Import necessary libraries
import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Initialize the video capture and face detector
capture = cv2.VideoCapture(0)
detector = FaceDetector()

# Main loop for capturing and processing frames
while (capture.isOpened()):
    # Read a frame from the camera
    ret, frame = capture.read()
    
    # Detect faces in the frame
    result, box = detector.findFaces(frame)

    # If faces are detected, process them
    if box:
        # Print the bounding box information of the first detected face
        print(box[0])
        center = box[0]['center']
        # Draw a green circle at the center of the detected face
        cv2.circle(frame, center, 5, (0, 250, 0), 1)

    # Display the frame with detected faces
    cv2.imshow('frame', frame)

    # Check for the 'Esc' key to exit the loop
    key = cv2.waitKey(10) & 0xFF
    if key == 27:
        break

# Release the video capture and close all windows
capture.release()
cv2.destroyAllWindows()
