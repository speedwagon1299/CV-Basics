import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/group 1.jpg')
cv.imshow('lady',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('front_face_default.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)  
#minNeigh is a parameter specifying how many neighbors each candidate rectangle should have to retain it. 
print(f'{len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h),(0,0,255),thickness = 2)

cv.imshow('faces',img)

cv.waitKey(0)