import cv2.dnn
import numpy as np

img = cv2.imread('room_ser.jpg')
img = cv2.resize(img, None, fx=0.3, fy=0.2)

height, width, channels = img.shape

#print(height, width)

# yolov4.weights: This file contains the output after the YOLO model is trained
net = cv2.dnn.readNet('yolov4.weights', 'yolov4.cfg')

classes = []
with open("coco.names", "r") as f:  # r: r methods
    classes = [line.strip() for line in
               f.readlines()]  # The strip() method returns a copy of the string in which all chars

# YOLOv3 has 3 output layers (82, 94 and 106) as the figure shows.
layer_names = net.getLayerNames()  # getLayerNames(): Get the name of all layers of the network.
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]  # Get the index of the output layers

# blob: It returns a 4-dimensional array/blob for the input image
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)


net.setInput(blob)
yolo_output = net.forward(output_layers)  # forward() - Runs a forward pass to compute the net output
print(yolo_output[0].shape) #predictions

class_ids = []
confidences = []
boxes = []
for out in yolo_output:
    for detection in out:
        scores = detection[5:] # it considers zero to five for coordinates and five to eighty for Coco file classes
        class_id = np.argmax(scores) # It considers the maximum score that is close to the Coco file classes from the predictions
        confidence = scores[class_id]

        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
            print(confidence)
            cv2.circle(img, (center_x,center_y), 10, (0,255,0), 2)



colors = np.random.uniform(0, 255, size=(len(classes), 3))
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4) # it returns maximum and the best values for box

for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[class_ids[i]]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 1)


cv2.imwrite('tehran1.png', img)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWinedows()

