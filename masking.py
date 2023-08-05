import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/cats.jpg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2], dtype='uint8')  # grayscale mask only
cv.imshow('blank',blank)

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
cv.imshow('mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)  #remember the mask is put on top of the normal image
cv.imshow('masked',masked)

cv.waitKey(0)