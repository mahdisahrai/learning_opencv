import cv2
import matplotlib.pyplot as plt
import pytesseract
from pytesseract import Output

plate_img = cv2.imread('text.png')
w, h, _ = plate_img.shape

blur = cv2.medianBlur(plate_img, 5)
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

data_image = pytesseract.image_to_data(thresh, output_type=Output.DICT)
print(list(enumerate(data_image['text'])), '\n')
print(data_image)

for index, text in enumerate(data_image['text']):
    if text:
        x1 = int(data_image['left'][index])
        y1 = int(data_image['top'][index])
        x2 = x1 + int(data_image['width'][index])
        y2 = y1 + int(data_image['height'][index])
        cv2.rectangle(thresh, (x1, y1), (x2, y2), (200, 15, 65), 2)

plt.imshow(thresh)
plt.show()
