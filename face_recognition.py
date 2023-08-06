import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('front_face_default.xml')

ppl = []
for p in os.listdir('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Faces/train'):
    ppl.append(p)

# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer.create()
face_recognizer.read('face_trained.yml')

img = cv.imread('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Faces/val/elton_john/3.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h,x:x+w]
    label, conf = face_recognizer.predict(face_roi)
    print(f'{ppl[label]} with a confidence of {conf}')
    cv.putText(img,str(ppl[label]),(30,30),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv.imshow('Detected Face',img)
cv.waitKey(0)