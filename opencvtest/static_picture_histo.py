import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

img = cv2.imread('test2.jpg')

#checking for image
if img is None:
    print("are u sure u chose the right img?")
    sys.exit()

#print(img)
#check the amount of (rows,columns,(bgr))
print(img.shape)

color = ('b','g','r')
for i,column in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=column)
    plt.xlabel('')
plt.show()

