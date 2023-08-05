import cv2 as cv
import numpy as np

# img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/group 1.jpg')
# cv.imshow('img',img)

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370), 255, -1)   #for drawing functions, create buffer copy of image and also assign to a new variable
cv.imshow('rect',rectangle)                       #plain 255 for colour means white, -1 thickness is fill

circle = cv.circle(blank.copy(),(blank.shape[1]//2,blank.shape[0]//2),200,255,-1)
cv.imshow('circle',circle)

bit_and = cv.bitwise_and(rectangle,circle)  #intersection
bit_or = cv.bitwise_or(rectangle,circle)    #union
bit_xor = cv.bitwise_xor(rectangle,circle)  #exclusive 
bit_not = cv.bitwise_not(rectangle)         #inverts pixel colours (prob self complements pixel intensity)
cv.imshow('and',bit_and)
cv.imshow('or',bit_or)
cv.imshow('xor',bit_xor)
cv.imshow('not',bit_not)


cv.waitKey(0)