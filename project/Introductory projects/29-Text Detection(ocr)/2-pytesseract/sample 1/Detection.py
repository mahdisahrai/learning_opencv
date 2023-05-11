import cv2
import matplotlib.pyplot as plt
import pytesseract

plate_img = cv2.imread('text.png')
w, h, _ = plate_img.shape

blur = cv2.medianBlur(plate_img, 5)
_, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

text_image = pytesseract.image_to_string(thresh)
box_image = pytesseract.image_to_boxes(thresh)
list = box_image.split('\n')

print('------------------------------')
print(text_image)
print('------------------------------')
print(pytesseract.get_languages())
print('------------------------------')
print(list)
print('------------------------------')


for box in list:
    boxes = box.split(' ')
    if boxes[0]:
        x1 = int(boxes[1])
        y1 = int(boxes[2])
        x2 = int(boxes[3])
        y2 = int(boxes[4])
        cv2.rectangle(thresh, (x1, w - y1), (x2, w - y2), (255, 15, 45), 2)
        print(boxes)


plt.imshow(thresh)
plt.show()

