import cv2
import qrcode

qrcode_img = cv2.imread("new_qrcode.png")
qrcode_img = cv2.resize(qrcode_img, (300, 300))

detector = cv2.QRCodeDetector()
value, box, _ = detector.detectAndDecode(qrcode_img)

#generating qr code
generated_qrcode = qrcode.make('https://github.com/mahdisahrai')
generated_qrcode.save('new_qrcode.png')


print(value)
cv2.imshow("new_qrcode", qrcode_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

