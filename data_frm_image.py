#! /home/grear4/anaconda3/bin/python

#import cv2
import pytesseract

#opening and using pil is better when the image has clearer words otherwise opencv
from PIL import Image

#You can use the openCV way 
#image = cv2.imread(input("CV2-input the file name:"))

#var = pytesseract.image_to_string(image)

#x=open('Data.text','w+')
#x.write(var)
#x.close()

# Or you can follow the pillow way
img=input("Pillow-Input the file name:")
image2 = Image.open(img)

var1 = pytesseract.image_to_string(image2,lang='eng')

y=open(input("File name you wnat to save in:")+'.txt','w+')
y.write(var1)
y.close()

