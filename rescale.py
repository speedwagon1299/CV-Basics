import cv2 as cv

#rescaling frames
# def rescaleFrame(frame, scale = 0.75):
#     width = int(frame.shape[1]*scale)   #width of matrix is num of columns
#     height = int(frame.shape[0]*scale)  #float converted to int
#     dim = (width,height)    #dimension for some reason stored in opposite order
#     return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

# changing vid resolution ONLY FOR LIVE VIDEO
# def changeRes(width,height):
#    cap.set(3,width)
#    cap.set(4,height)

cap = cv.VideoCapture('/home/speedwagon1299/projects/CV-Basics/opencv-course-master/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = cap.read()
    cv.imshow('dog vid normal', frame)
    frame_new = cv.resize(frame,(frame.shape[1]//2,frame.shape[0]//2),interpolation=cv.INTER_AREA)
    cv.imshow('dog vid scale', frame_new)
    if cv.waitKey(20) & 0xff == ord('d'):       #20ms per frame is golden number
        break
cap.release()
cv.destroyAllWindows()

# interpolation = cv.INTER_     (AREA/default => SHRINKING; LINEAR,CUBIC => ENLARGE)