import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.FaceMeshModule import FaceMeshDetector

face_img = cv.imread('face_hd.jpg')
face_img = cv.resize(face_img, (512, 512))

detector = FaceDetector()
meshdetector = FaceMeshDetector(maxFaces=1)  # maxFaces num of face

face_img, bbox = detector.findFaces(face_img)  # face
face_img, faces = meshdetector.findFaceMesh(face_img)  # landmarks

#finding points and displaying
if faces:
    for i in range(0, len(faces[0])):
        cv.putText(face_img, str(i), (faces[0][i][0], faces[0][i][1]), cv.FONT_HERSHEY_PLAIN, 0.5, (0, 0, 255), 1)


cv.imshow('outcome', face_img)
cv.waitKey(0)
cv.destroyAllWindows()
