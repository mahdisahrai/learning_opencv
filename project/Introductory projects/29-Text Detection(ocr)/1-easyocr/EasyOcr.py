import cv2
import easyocr

plate_img = cv2.imread('plate2.jpg')

read = easyocr.Reader(['en']) #persian: fa
read_box = read.readtext(plate_img)

obtained_text = read_box[0][-2]

print(read_box)
print(obtained_text)