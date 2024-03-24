import cv2
import  cvzone
from  cvzone.FaceMeshModule import FaceMeshDetector
#camera access and video cam (0 is the which cam "if mulipale cam have by defult 0 ") open
cap= cv2.VideoCapture(0)

decetoor=FaceMeshDetector(maxFaces=1)

while True:
    success,img=cap.read()
    #detech the face
    img,faces=decetoor.findFaceMesh(img,draw=False)

    if faces:
        face=faces[0]
        pointleft=face[145]
        pointRight=face[374]

        # drawing
        # # to put a point on the left eye
        # cv2.circle(img,pointleft,5,(255,0,255),cv2.FILLED)
        # # to put a point on the right eye
        # cv2.circle(img,pointRight,5,(255,0,255),cv2.FILLED)
        # # to do line between the point
        # cv2.line(img,pointleft,pointRight,(0,200,0),3)


#to mesure distance between the two eyes(in images pixcel)
        w,_=decetoor.findDistance(pointleft,pointRight)
        # in the real life avg distance the eyes distance is 6.3 cm(male), and 6.1 or 6.2 cm (female)
        W=6.3
       # print(w)
        # # distance between face and camera
        # d = 42
        #
        # # finding focale length if camera
        # f = (w * d) / W
#find distance
        f=600
        d=(W*f)/w
        print(d)
        cvzone.putTextRect(img,f"Depth:{int(d)}cm",
                           (face[10][0]-75,face[10][1]-50),
                           scale=2

                           )


    cv2.imshow('image',img)
    cv2.waitKey(1)