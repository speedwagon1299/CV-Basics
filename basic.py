import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/group 1.jpg')

# basic functions are return type fucntions

# cvt to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
cv.imshow('gray grp',gray)

# cv.line(img, (img.shape[1],img.shape[0]), (0,0), (0,0,255), thickness=2)
# cv.imshow('dead', img)

# blur

blur = cv.GaussianBlur(img,(1,5),cv.BORDER_DEFAULT)     #second argument kernel size always odd (increases blur)
cv.imshow('blur',blur)

# edge cascade

canny = cv.Canny(blur,125,175)   #pixels over 175 considered edges and below 125 not
cv.imshow('canny',canny)

# dilation

dilate = cv.dilate(canny,(3,3),iterations=3)
cv.imshow('dilated',dilate)

# to undo dilation, erosion (doesnt work that well IN MY EXPERIENCE)

erode = cv.erode(dilate, (3,3), iterations = 5)
cv.imshow('eroded',erode)

# resize

resized = cv.resize(img,(300,300))
cv.imshow('resize',resized)

# cropping

cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)