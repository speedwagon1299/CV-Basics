import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/lady.jpg')
cv.imshow('lady',img)

# Translation
def translate(img,x,y): #x = - => shift to left, y => shift down,  etc
    transMat = np.float32([[1,0,x],[0,1,y]])    #mug it up :/
    dim = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dim)

translated = translate(img,-100,100)
cv.imshow('translated',translated)


# Rotation

def rotate(img, angle, rotpoint = None):
    (height,width) = img.shape[:2]

cv.waitKey(0)