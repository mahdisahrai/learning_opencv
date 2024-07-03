import cv2  # Importing the OpenCV library for image processing
import numpy as np  # Importing the NumPy library for numerical operations

# Read the image 'smarties.png'
img = cv2.imread('smarties.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a median blur to the grayscale image to reduce noise
gray = cv2.medianBlur(gray, 5)

# Detect circles in the grayscale image using the Hough Circle Transform
houghcircle = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 30,
                               param1=50, param2=35, minRadius=0, maxRadius=0)

# Convert the (x, y, radius) values to integers
circle = np.uint16(np.around(houghcircle))

# Draw each detected circle on the original image
for (x, y, r) in circle[0, :]:
    cv2.circle(img, (x, y), r, (0, 255, 0), 3)  # Drawing the circle in green with a thickness of 3

# Display the image with detected circles
cv2.imshow('image', img)

# Wait for a key press indefinitely or for a specified amount of time in milliseconds
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()
