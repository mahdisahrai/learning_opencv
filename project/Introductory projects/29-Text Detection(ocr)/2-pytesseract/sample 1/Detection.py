# Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import pytesseract

# Load the image ('text.png') using OpenCV
plate_img = cv2.imread('text.png')

# Get the width, height, and number of channels of the image
w, h, _ = plate_img.shape

# Apply median blur to reduce noise in the image
blur = cv2.medianBlur(plate_img, 5)

# Apply binary thresholding to create a binary image
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

# Use pytesseract to extract text from the binary image
text_image = pytesseract.image_to_string(thresh)

# Use pytesseract to extract boxes around characters in the image
box_image = pytesseract.image_to_boxes(thresh)

# Split the box image information into a list of lines
list = box_image.split('\n')

# Print a separator line
print('------------------------------')

# Print the extracted text
print(text_image)

# Print a separator line
print('------------------------------')

# Print the available languages for pytesseract
print(pytesseract.get_languages())

# Print a separator line
print('------------------------------')

# Print the list of character boxes
print(list)

# Print a separator line
print('------------------------------')

# Loop through the list of character boxes and draw rectangles around them
for box in list:
    boxes = box.split(' ')
    if boxes[0]:
        x1 = int(boxes[1])
        y1 = int(boxes[2])
        x2 = int(boxes[3])
        y2 = int(boxes[4])
        cv2.rectangle(thresh, (x1, w - y1), (x2, w - y2), (255, 15, 45), 2)
        print(boxes)

# Display the image with character boxes
plt.imshow(thresh)
plt.show()
