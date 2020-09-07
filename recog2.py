import cv2
import numpy as np
import random
import pymysql
import time
from datetime import date, timedelta,datetime

localtime = time.asctime( time.localtime(time.time()) )
st = localtime.split(' ')
pDate = st[2]+'_'+st[1]+'_'+st[4]

connDb = pymysql.connect(host='localhost', user='root',password='')
cur = connDb.cursor()
if cur.execute("(SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'face')"):
    print("databaseb already exists")
else:
    cur.execute('CREATE DATABASE IF NOT EXISTS face')

con = pymysql.connect(host='localhost', user='root',password='', database='face')
cursor = con.cursor()

if cursor.execute("(SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='atd')"):
    print("table already exists")
else:
    cursor.execute('CREATE TABLE atd (id int, name varchar(20))')
    cursor.execute('INSERT INTO atd (id, name)'
    'VALUES'
    '(01,"shima"),(03,"Anika"),(04,"Onik"),(13,"Farjana"),(21,"Jobayer"),(26,"Raju"),(43,"Mamun"),(46,"Sakhawat"),(214,"Sifat")'
    )

if cursor.execute("(SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME='"+pDate+"')"):
    print("column already exists")
else:
    cursor.execute('ALTER TABLE atd ADD '+pDate+' varchar(20)')
    cursor.execute('UPDATE atd SET '+pDate+'="No"')
cursor.execute('SELECT * FROM atd')

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('recog/trainning.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
#cam = cv2.VideoCapture(1)
cam = cv2.VideoCapture(0)
unknownId = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    #Time checking part
    now = datetime.now()
    h = now.strftime("%H")
    m = now.strftime("%M")
    if int(h)>12:
        h=int(h)%12
    else:
        h=h
    tst = str(h)+':'+str(m)
    if tst=='3:56':
        print 'loass your present'
    #end Time checking part

    #Face detection and recognition part
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        newImage = cv2.rectangle(im,(x,y),(x+w,y+h),(50,60,255),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<=45):
            persentage=100-conf

        #update present if id is match
            if tst=='4:28':
                break
            else:
                cursor.execute('UPDATE atd SET '+pDate+'="Yes" WHERE id=%s',Id)
                con.commit()
                cursor.execute('SELECT * FROM atd')
                all = cursor.fetchall()
                for al in all:
                    if Id==al[0]:
                        Id=al[1]

        else:
            persentage=(100-conf)
            Id="Unknown"

        cv2.putText(im, str(Id)+'-'+str(persentage), (x-15,y-5), font, 1, (0,40,255),2, cv2.LINE_AA)
    resize = cv2.resize(im, (int(im.shape[1]*1.5), int(im.shape[0]*1.5)))
    cv2.imshow('im',resize)
    if cv2.waitKey(001)==ord('q'):
        break

con.close()
cam.release()
cv2.destroyAllWindows()
