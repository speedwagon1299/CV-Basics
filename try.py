import cv2 as cv
import numpy as np

vid = cv.VideoCapture('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Videos/ball.mp4')



lower_yellow = np.array([0.11*256, 0.60*256, 0.20*256])
upper_yellow = np.array([0.14*256, 1.00*256, 1.00*256])

def track(frame):
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    blur = cv.GaussianBlur(hsv,(7,7),4)
    mask = cv.inRange(blur,lower_yellow,upper_yellow)
    contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if (area > 300):
            x,y,w,h = cv.boundingRect(contour)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),thickness=2)


while True:
    isTrue, frame = vid.read()
    track(frame)
    cv.imshow('tennis',frame)
    if cv.waitKey(25) & 0xff==ord('d'):
        break
vid.release()
cv.destroyAllWindows()
