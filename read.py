import cv2 as cv
img = cv.imread("opencv-course-master/Resources/Photos/cat.jpg")
cv.imshow('cat image',img)
cv.waitKey(0)