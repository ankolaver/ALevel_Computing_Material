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

'''
from itertools import chain
from collections import Counter

#count number of occurences of a certain shade of color
new_blue = list(chain.from_iterable(blue))
new_green = list(chain.from_iterable(green))
new_red = list(chain.from_iterable(red))
print(new_blue)
print(new_green)
print(new_red)

f_blue = Counter(new_blue)
f_green = Counter(new_green)
f_red = Counter(new_red)
print(f_blue)
print(f_green)
print(f_red)

plt.line(list(f_blue.keys()),f_blue.values(),color ='blue')
plt.line(list(f_green.keys()),f_green.values(),color ='green')
plt.line(list(f_red.keys()),f_red.values(),color ='red')
plt.show()

'''
