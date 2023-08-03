import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')  # uint8 is dtype of an image and 3 signifies red green blue
cv.imshow('blank',blank)

# to get blank green
# blank[:] = 0,255,0    #convention blue green red (bgr)
# cv.imshow('green',blank)

blank[200:300,300:400] = 0,0,255  #red square 
cv.imshow('red square',blank)       #(0,0) is top left

#to draw rectangle
cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness = 2)     #as seen before, eventhough convention is (row,column), (width,height) is used instead
cv.imshow('rect', blank)    
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//4), thickness = -1)#thickness = -1 => filled rectangle
# cv.imshow('new rects', blank)   #double / used (//) for floor division while (/) for float divison    

#to draw a circle
cv.circle(blank, (250,250), 50, (0,0,255), thickness = 3)
cv.imshow('circle',blank)

#to draw a line
cv.line(blank, (500,500), (0,0), (255,0,0), thickness = 1)
cv.imshow('line',blank)

#to write text
cv.putText(blank, 'Hello World', (250,250), cv.FONT_HERSHEY_PLAIN, 1.3, (0,255,0), thickness = 2) #loc is starting of bottom left of text
cv.imshow('text',blank)

cv.waitKey(0)