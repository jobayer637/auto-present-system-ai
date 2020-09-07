import cv2
import numpy as np

cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
cam = cv2.VideoCapture(1)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        newImage = cv2.rectangle(im,(x,y),(x+w,y+h),(0,60,100),2)
    cv2.imshow('im',im)
    if cv2.waitKey(1)==ord('q'):
        break

con.close()
cam.release()
cv2.destroyAllWindows()
