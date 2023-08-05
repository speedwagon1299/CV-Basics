import cv2 as cv
import numpy as np

img = cv.imread("opencv-course-master/Resources/Photos/cats.jpg")
cv.imshow('cats',img)

# blur = cv.blur(img,(5,5), cv.BORDER_DEFAULT)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

canny = cv.Canny(gray,125,175)
cv.imshow('canny',canny)

# to find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countours')
# retr_list for all contours, retr_tree for the hierarchical, retr_external for external contours
# chain_approx_none for ignoring no lines and simple for slight grouping

# threshold
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)   #ret is to take the first return type of retVal (idrk)
#if density of pixel is below 125, its taken as black, density more than 255 its taken as white
cv.imshow('thresh',thresh)
contours2, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)} countours')

blank = np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('blank',blank)


#recommended to canny --> contour --> drawContour (simple thresholding has many disadvantages at times)

cv.waitKey(0)