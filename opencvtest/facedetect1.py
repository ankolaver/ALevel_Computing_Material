import numpy as np
import cv2
import matplotlib.pyplot as plt

#testing responsiveness
print("hi")

#capturing from the main laptop webcam
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

#from system
face_cascade = cv2.CascadeClassifier('C:\\Users\\Kenneth\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Kenneth\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('C:\\Users\\Kenneth\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_smile.xml')

while True:
    ret, img = cap.read()
    #img = cv2.flip(img, -1)
    img = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.imread('happy.jpg')

    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        #syntax
        #cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.5,
            minNeighbors=15,
            minSize=(25, 25)
            )
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(87,100,100),3)

    cv2.imshow('facedetecting',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
