import cv2
import numpy as np
from time import sleep

cap = cv2.VideoCapture(0)

while True:
    retrieveval, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #row,cols = frame.shape
    #print("Cols:",cols)
    #range for red color
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, retrieveval = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x:cv2.contourArea(x), reverse=True)

    cv2.line(frame, (320, 0), (320, 480), (255, 0, 0), 2)

    if len(contours)>0:
        (x,y,w,h) = cv2.boundingRect(contours[0])
        print("X_mid:",x+w/2,"Y_mid:",y+h/2)

        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),2)
        cv2.line(frame, (int(x+w/2), 0), (int(x+w/2), 480), (0, 255, 0), 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Mask over", red_mask)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
