import cv2
import os
import numpy
from PIL import Image


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier  = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
id=0

#recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('recog/trainningData.yml')
print(recognizer.load('recog/trainningData.yml'))

font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(grayImage)

    for x,y,w,h in faces:

        cv2.rectangle(grayImage, (x,y), (x+w, y+h), (255,0,0),2)
        id,conf = recognizer.predict(grayImage[y:y+h, x:x+w])

        cv2.putText(grayImage, str(id), (x,y), font, 1, (255,0,255),3, cv2.LINE_AA)


        cv2.imshow('ima',grayImage)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
