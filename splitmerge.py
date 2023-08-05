import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/group 1.jpg')
cv.imshow('img',img)

b,g,r = cv.split(img)   #to split colours into three by unpacking tuple but storing intensity as GRAYSCALE

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)


merged = cv.merge([b,g,r])
cv.imshow('merge',merged)


# to show plain blue or green or red

blank = np.zeros(img.shape[:2],dtype='uint8')       #since grayscale images dont have a third dimension
red = cv.merge([blank,blank,r])     
blue = cv.merge([b,blank,blank])     
green = cv.merge([blank,g,blank])    
cv.imshow('blue',blue)
cv.imshow('green',green) 
cv.imshow('red',red)  

cv.waitKey(0)