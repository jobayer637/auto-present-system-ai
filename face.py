import cv2
import os

face_classifier = cv2.CascadeClassifier('face.xml')
cap = cv2.VideoCapture(0)

id=int(input("Enter id: "))
key = 0
name=str(input("Enter name: "))
while(True):
    ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(grayImage,1.4,4)

    for x,y,w,h in faces:
        key=key+1
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)
        cv2.imwrite('faces/'+name+"."+ str(id)+"."+str(key)+".jpg",grayImage[y:y+h, x:x+w])


    cv2.imshow('frame',grayImage)
    if cv2.waitKey(200)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
