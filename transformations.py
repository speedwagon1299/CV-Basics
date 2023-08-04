import cv2 as cv
import numpy as np

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Photos/park.jpg')
cv.imshow('lady',img)

# Translation
def translate(img,x,y): #x = - => shift to left, y => shift down,  etc
    transMat = np.float32([[1,0,x],[0,1,y]])    #mug it up :/
    dim = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dim)  #warpAffine multiplies img with next matrix

translated = translate(img,-100,100)
cv.imshow('translated',translated)


# Rotation

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]  #since last index is for bgr

    if rotPoint == None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    
    dim = (width,height)

    return cv.warpAffine(img,rotMat,dim)

rotated = rotate(img,45)        #rotating one by one leads to loss of parts of the pic so sum the angles
cv.imshow('rotated',rotated)


# Resizing
resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
cv.imshow('resize',resized) 

# Flip
flip = cv.flip(img,0)   #0 is vertflip, 1 is horflip, -1 for both (reversed image)
cv.imshow('flip',flip)

cv.waitKey(0)