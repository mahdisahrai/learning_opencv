import cv2

img = cv2.imread("apple.jpg", 0)
edge = cv2.Canny(img, 85, 150)


def clicks(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # EVENT_RBUTTONDOWN is left click
        cv2.circle(edge, (x, y), 5, (147, 96, 44), 15)
        cv2.imshow('edge', edge)


cv2.imshow('edge', edge)
cv2.setMouseCallback('edge', clicks)


cv2.waitKey(0)
cv2.destroyAllWindows()

