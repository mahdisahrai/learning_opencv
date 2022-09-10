import cv2


img = cv2.imread('lena_tmpl.jpg')


layer = img.copy()
arr = [layer]


for i in range(4):
    layer = cv2.pyrDown(layer) #the smallest outcome
    arr.append(layer)
    cv2.imshow(str(i), layer)


for i in range(3, 0, -1):
    gaussian = cv2.pyrUp(arr[i]) #the bigest outcome
    laplacian = cv2.subtract(arr[i - 1], gaussian)
    # bitwize = cv2.bitwise_and(gaussian, laplacian)
    # cv2.imshow('bitwize= ' + str(i), bitwize)
    cv2.imshow('laplacian= ' + str(i), laplacian)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
