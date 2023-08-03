import cv2 as cv

# reading an image

img = cv.imread("opencv-course-master/Resources/Photos/cat.jpg")
cv.imshow('cat image',img)
cv.waitKey(0) #0 is for any key on the keyboard

# reading a video
vid = cv.VideoCapture('opencv-course-master/Resources/Videos/dog.mp4')

while True:     #while frame is availabe show the video
    isTrue, frame = vid.read()  #read method to take frame by frame
    cv.imshow('dog video', frame)
    if cv.waitKey(20) & 0xff == ord('d'):   #after 20 ns if the user hits 'd' then exit
        break

vid.release()
cv.destroyAllWindows()