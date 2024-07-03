import cv2  # Importing the OpenCV library for image processing
import numpy as np  # Importing the NumPy library for numerical operations

# Function to show the value of the trackbar position (for demonstration purposes)
def show(x):
    print(x)

# Create a black image of size 300x500 with 3 color channels (RGB)
img = np.zeros((300, 500, 3), np.uint8)

# Create a window named 'trackbar'
cv2.namedWindow('trackbar')

# Create three trackbars for Blue, Green, and Red channels with range 0-255
cv2.createTrackbar('B', 'trackbar', 0, 255, show)
cv2.createTrackbar('G', 'trackbar', 0, 255, show)
cv2.createTrackbar('R', 'trackbar', 0, 255, show)

# Infinite loop to keep the window open and update the image based on trackbar positions
while (1):

    # Wait for a key press for 1 ms
    K = cv2.waitKey(1) & 0xFF
    
    # If the key 'Esc' is pressed, break the loop
    if K == 27:  # The ASCII value for the Esc key is 27
        break

    # Get the current positions of the three trackbars
    b = cv2.getTrackbarPos('B', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    r = cv2.getTrackbarPos('R', 'trackbar')
    
    # Set the image to the color specified by the trackbar positions
    img[:] = [b, g, r]

    # Show the image in the 'trackbar' window
    cv2.imshow('trackbar', img)

# Destroy all the OpenCV windows
cv2.destroyAllWindows()
