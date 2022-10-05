import cv2

img = cv2.imread('allshapes.png')

color = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(color, 215, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for i in contours:
    approx = cv2.approxPolyDP(i, 0.01 * cv2.arcLength(i, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 1)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img, 'triangle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (15, 220, 255))

    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectratio = float(w) / h
        print(aspectratio)

        if aspectratio >= 0.95 and aspectratio <= 1.05:
            cv2.putText(img, 'square', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (12, 153, 112))

        else:
            cv2.putText(img, 'rectangle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (20, 5, 227))

    elif len(approx) == 5:
        cv2.putText(img, 'pentagon', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (141, 53, 129))

    elif len(approx) == 10:
        cv2.putText(img, 'star', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (140, 52, 40))

    else:
        cv2.putText(img, 'circle', (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (12, 91, 234))



cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
