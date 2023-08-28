import cv2
import numpy as np

# Load the video
capture = cv2.VideoCapture('traffic.mp4')

# Read the first frame
ret, frame = capture.read()

# Initial position and dimensions of the tracking window
x, y, w, h = 300, 200, 100, 50
track = (x, y, w, h)

# Convert the frame to HSV color space
color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Create a mask to detect the object based on its color in HSV space
mask = cv2.inRange(color, np.array((0, 60., 32.)), np.array((180., 255., 255)))

# Calculate the histogram of the object's color
hist = cv2.calcHist([color], [0], mask, [180], [0, 180])

# Normalize the histogram
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

# Criteria for the mean shift algorithm
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 2, 5)

# Main loop for tracking
while True:
    ret, frame = capture.read()
    if ret:
        # Crop the frame to the region of interest (ROI)
        crop = frame[y:y + h, x:x + w]
        cv2.imshow('roi', crop)

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Calculate the back projection of the histogram
        dst = cv2.calcBackProject([hsv], [0], hist, [0, 180], 1)  # Calculate back projection of histogram

        # Apply the mean shift algorithm to locate the object
        ret, track = cv2.meanShift(dst, track, term_crit)  # Apply mean shift algorithm

        # Update the position and dimensions of the tracking window
        x, y, w, h = track

        # Draw a rectangle around the tracked object
        final = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 3)

        # Display the back projection and the final result
        cv2.imshow('dst', dst)  # Show back projected image
        cv2.imshow('final', final)

        # Check for the 'Esc' key to exit the loop
        key = cv2.waitKey(35) & 0xFF
        if key == 27:
            break
    else:
        break

# Release the video capture and close all windows
capture.release()
cv2.destroyAllWindows()
