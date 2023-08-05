import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/cats.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)  #after sending gray image, if pixel is below 150 go to 0 (thresh binary) or if above then 255
# return threshold value back as threshold and thresh as the binarised image
cv.imshow('thresh',thresh)


# Adaptive Thresholding => computer optimises threshold value instead of taking value like simple
adap_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV,11,9) 
cv.imshow('adaptive thresholding mean',adap_thresh)   
#11 is kernel size, 3 is constant to subtract mean from 
adap_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,11,9)    
cv.imshow('adaptive thresholding gauss',adap_thresh)


cv.waitKey(0)