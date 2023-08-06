import os
import numpy as np
import cv2 as cv

ppl = []
DIR = '/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Faces/train'
haar_cascade = cv.CascadeClassifier('front_face_default.xml')
for i in os.listdir('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Faces/train'):
    ppl.append(i)

features = []   # image arrays of faces
labels = []     # corresponding name to the face

def create_train():
    for p in ppl:                       #creating training set of grayscales
        path = os.path.join(DIR, p)     #literally add the / and path
        label = ppl.index(p)            #0 for first person, 1 for second person, etc
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
    
create_train()

face_recognizer = cv.face.LBPHFaceRecognizer_create()       #opencv built in face recognizer

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)

