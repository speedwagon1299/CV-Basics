import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/park.jpg')


# BGfR TO GRAY
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# BGR TO HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR TO LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# BGR TO RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# plt.imshow(rgb)       # since mptplt takes rgb not bgr images
# plt.show()

cv.waitKey(0)