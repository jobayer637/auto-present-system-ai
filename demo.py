import cv2
import os

cam = cv2.VideoCapture('all.mp4')
detector=cv2.CascadeClassifier("face.xml");
i=0
name=raw_input('enter your id')
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray,1.4,5)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("grayImage/face-"+name +'.'+ str(i) + ".jpg", gray[y:y+h,x:x+w])
        cv2.rectangle(gray,(x-10,y-10),(x+w+10,y+h+10),(225,0,0),2)
        cv2.imshow('im',gray)
    cv2.imshow('im',gray)
    cv2.waitKey(10)
    if i>600:
        break
cam.release()
cv2.destroyAllWindows()
