import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/cats.jpg')
cv.imshow('img',img)

# Averaging (intensity of selected pixel is avg of surrounding pixel intensity)
avg = cv.blur(img,(3,3))
cv.imshow('averaging',avg)

# Gaussian blur is weighted avg blur with more precedence to main pixel
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gb',gauss)

# Median Blur (median of surrounding images) - better at reducing noise at times
median = cv.medianBlur(img,3)   #im guessing since its newer it doesnt need to accept square matrix shape dimensions
cv.imshow('median',median)

# Bilater Blurring - unlike traditional, it blurs the image but KEEPS THE EDGES (accepts diameter not kernel)
bi = cv.bilateralFilter(img,5,15,15)  #sigmacolour is to decide bell curve spread for accepting color (idrk), sigma space for influence by outer surrounding pixels
cv.imshow('bilateral',bi)
cv.waitKey(0)