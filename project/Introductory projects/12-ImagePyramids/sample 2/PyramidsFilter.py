import cv2  # Importing the OpenCV library for image processing
import numpy as np  # Importing the NumPy library for numerical operations

# Read the images of apple and orange
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

# Create a kernel for the filter
kernal = np.ones((5, 5), np.float32) / 25

# Apply the filter to the orange image
filter = cv2.filter2D(orange, -1, kernal)

# Combine the left half of the apple image and the right half of the filtered orange image
combine = np.hstack((apple[:, :230], filter[:, 256:]))

# Make a copy of the combined image for pyramid down sampling
layer = combine.copy()

# Apply Gaussian pyramid down-sampling 4 times and display each level
for i in range(4):
    layer = cv2.pyrDown(layer)
    cv2.imshow(str(i), layer)

# Print the shapes of the original apple and orange images
print(apple.shape)
print(orange.shape)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
