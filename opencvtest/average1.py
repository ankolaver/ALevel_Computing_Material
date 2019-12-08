from PIL import Image
import glob, os
import time

currimg = 0
numimg = int(input("How many images to average from: "))

while currimg<numimg:
    for infileimg in glob.glob("*.jpg"):
        print(infileimg)
        print("This is the image data", end='\n')
        #read time value of key:value format
        #print(infileimg.getexif()[36867])
        with Image.open(infileimg) as img:
            #read image data of original img
            #img_data = Image.frombytes('RGBA', size, data, "raw", stride, orientation)
            print("Working on curr img number: ", currimg)
            img.putalpha(round(256/(currimg+1))) #half alpha value
            os.chdir("C:\\Users\\Kenneth\\Desktop\\night\\averaged")
            print("Entering averaged directory")
            old_mode = img.mode
            
            if old_mode == 'RGBA':
                background = Image.new(old_mode[:-1], img.size, 'white')
                background.paste(img, img.getchannel('A'))
                img = background
                #old_mode = img.mode
                img.save("averaged"+str(currimg)+".jpg")
        currimg+=1

    

    

