import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector


# Initialize video capture from the default camera (index 0)
capture = cv2.VideoCapture(0)

# Create a FaceDetector instance for face detection
detector = FaceDetector()

# Create a FaceMeshDetector instance for face mesh detection with a maximum of 1 face
mesh_detector = FaceMeshDetector(maxFaces=1)

# Start a loop to process frames from the camera
while capture.isOpened():
    # Read a frame from the camera
    ret, frame = capture.read()

    # Perform face detection using the FaceDetector
    result, box = detector.findFaces(frame)

    # Perform face mesh detection using the FaceMeshDetector
    result, faces = mesh_detector.findFaceMesh(frame)

    # Check if any faces were detected
    if box:
        # Print information about the first detected face
        print(box[0])
        center = box[0]['center']  # Extract the center of the detected face
        cv2.circle(frame, center, 5, (0, 250, 0), 1)  # Draw a green circle at the center of the detected face

    # Display the current frame with any detected faces and face mesh
    cv2.imshow('frame', frame)

    # Check for key presses and exit the loop if the 'Esc' key (27) is pressed
    key = cv2.waitKey(10) & 0xFF
    if key == 27:
        break

# Release the video capture object and close OpenCV windows
capture.release()
cv2.destroyAllWindows()
