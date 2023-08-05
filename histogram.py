import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/cats.jpg')
cv.imshow('img',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


blank = np.zeros(img.shape[:2], dtype = 'uint8')
circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow('mask',mask)

# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])
# [0] is channel that indexes the position of gray that we want, mask = None, histSize = [256] => num of bins for hist wrapped as a list
# range of all possible pixel values [0,256]

gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)