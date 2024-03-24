import cv2
import cvzone
import numpy as np
from cvzone.FaceMeshModule import FaceMeshDetector

# camera access and video camera (0 is the which cam "if multiple cam have by default 0 ") open
cap = cv2.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=1)

# sensitivity
sen=10

while True:
    # read the image
    success, img = cap.read()
    # create an empty text image
    imageText = np.zeros_like(img)
    # detach the face
    img, faces = detector.findFaceMesh(img, draw=False)
    text_list=['Radhe Radhe','Ram Ram','Hare krishna','Krishna Krishna']

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        # to measure distance between the two eyes(in images pixel)
        w, _ = detector.findDistance(pointLeft, pointRight)
        # in the real life avg distance the eyes distance is 6.3 cm(male), and 6.1 or 6.2 cm (female)
        W = 6.3

        # find distance
        f = 600
        d = (W * f) / w
        print(d)

        # distance show on face
        cvzone.putTextRect(img, f"Depth:{int(int(d/sen)*sen)}cm",
                           (face[10][0] - 75, face[10][1] - 50),
                           scale=2)

        for i,text in enumerate(text_list):
            SingleHight=20 +int((int(d/sen)*sen)/4)
            Scale=.4+(int(d/sen)*sen)/75
            cv2.putText(imageText,text,(50,50+(i*SingleHight)),cv2.FONT_ITALIC,Scale,(255,255,255),2)
        imageStack = cvzone.stackImages([img, imageText], 2, 1)

    cv2.imshow('image', imageStack )
    cv2.waitKey(1)
