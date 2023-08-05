import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/cats.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Laplacian
lap = cv.Laplacian(gray,cv.CV_64F)      #computes gradients of the image
lap = np.uint8(np.absolute(lap))        #takes absolute values of gradients and makes it image datatype
cv.imshow('lap',lap)

# Sobel
sobelx = cv.Sobel(gray,cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray,cv.CV_64F, 0, 1)
sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('sobelfinal',sobel)

cv.waitKey(0)