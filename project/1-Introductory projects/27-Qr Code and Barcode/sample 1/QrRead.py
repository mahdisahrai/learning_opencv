import cv2

qrcode_img = cv2.imread("qr_code1.png")
qrcode_img = cv2.resize(qrcode_img, (300, 300))

detector = cv2.QRCodeDetector()

value, box, _ = detector.detectAndDecode(qrcode_img)
cv2.rectangle(qrcode_img, (int(box[0][0][0]), int(box[0][0][1])), (int(box[0][2][0]), int(box[0][2][1])),
              (255, 255, 0), 2)

print(box)
print(value)

cv2.imshow("result", qrcode_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

