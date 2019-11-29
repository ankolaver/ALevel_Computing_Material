import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

fig, ax = plt.subplots()
linewidth = 2
bins = 256
alpha = 0.5

lineBlue, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', linewidth = linewidth, alpha=alpha, label='Blue')
lineGreen, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', linewidth = linewidth, alpha=alpha, label='Green')
lineRed, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', linewidth = linewidth, alpha=alpha, label='Red')
ax.set_xlim(0, bins-1)
ax.set_ylim(0,0.03)
plt.ion() #interactive mode on
plt.title("RGB Histogram")
plt.show()


while True:
    retrieveval, frame = cap.read() #BGR values
    cv2.imshow("Default Video", frame)

    blue,green,red = cv2.split(frame)
    numpix = (frame.shape[0]*frame.shape[1])
    #single channel source, 16 mins 0-15, 16-32 etc.
    histblue = cv2.calcHist([blue],[0],None,[bins],[0,256])/numpix
    #print(histblue)
    histgreen = cv2.calcHist([green],[0],None,[bins],[0,256])/numpix
    histred = cv2.calcHist([red],[0],None,[bins],[0,256])/numpix

    lineBlue.set_ydata(histblue)
    lineGreen.set_ydata(histgreen)
    lineRed.set_ydata(histred)

    fig.canvas.draw()

    plt.xlabel('Color Ranges, 256')
    plt.ylabel('Occurence')


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



'''
while retrieveval:
    cv2.imwrite("curframe{0}.jpg".format(count), frame)
    time.sleep(0.1)
     #save jpeg
    histojpg = cv2.imread("curframe{0}.jpg".format(count))
    if histojpg is None:
        print("are u sure u chose the right img?")
        sys.exit()

    color = ('blue','green','red')
    for i,column in enumerate(color):
        hist = cv2.calcHist([histojpg],[i],None,[256],[0,256])
        #print(hist, column)
        plt.plot(hist,color=column)
    plt.show()
    time.sleep(0.3)
    plt.clf()
    count+=1
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

    def histocount(img):
        color = ('blue','green','red')
        for i,column in enumerate(color):
            hist = cv2.calcHist([img],[i],None,[256],[0,256])
            print(hist, column)
            plt.plot(hist,color=column)
        #return hist, column
        #return plt.show()
    def animate(i):

        plt.xlabel('color_range')
        plt.ylabel('occurences')
    '''
