import face_recognition
from PIL import Image, ImageDraw
import cv2
import dlib
import numpy as np
import os

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX

#name = "Unknown Person"


path='faces'
known_face_encodings = []
known_face_names = []
images = [os.path.join(path, f) for f in os.listdir(path)]
for image in images:
     im = face_recognition.load_image_file(image)
     faec_encode = face_recognition.face_encodings(im)[0]
     known_face_encodings.append(faec_encode)

     nm = image.split()[0].split('\\')[1].split('.')[0]
     known_face_names.append(nm)

#----------------------

while(True):
    ret, frame = cap.read()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(grayImage,1.4,4)

    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)



    test_image = frame
    pil_image = Image.fromarray(frame)
    face_locations = face_recognition.face_locations(frame)



#----------------------

    face_encodings = face_recognition.face_encodings(test_image, face_locations)



    # Convert to PIL format
    pil_image = Image.fromarray(test_image)

    # Create a ImageDraw instance
    draw = ImageDraw.Draw(pil_image)

    # Loop through faces in test image
    for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
      matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

      name = "Unknown Person"

      # If match
      if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]


      # Draw box
      draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

      # Draw label
      text_width, text_height = draw.textsize(name)
      draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
      draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

    del draw

    # Display image
    pil_image.show()

#-----------------------
    if cv2.waitKey(20)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
