import numpy as np
import cv2
import time
import sqlite3
import os.path
import urllib
url="http://192.168.1.3:8080/shot.jpg"

a = 1
face_cascade = cv2.CascadeClassifier(
    '/home/anmolmalhotra97/Desktop/openCV/haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print('file couldnt load, give up!')

datafile = 'FaceBase.db'
datadir = '/home/anmolmalhotra97/Desktop/openCV/IPCAM/'
db = datadir+datafile
print db;
def insertOrUpdate(Id, Name,Age,Gender,Criminal):
    conn = sqlite3.connect("FaceBase.db")
    conn.text_factory = sqlite3.OptimizedUnicode
    cur = conn.cursor()
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE people SET Name=' "+str(name)+" ' WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO people(ID,Name,Age,Gender,Criminal_Record) Values("+str(Id)+","+str(Name)+","+str(Age)+","+str(Gender)+","+str(Criminal)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
id = raw_input('user ID : ')
name = raw_input('user Name : ')
age = raw_input('user Age : ')
gender = raw_input('user Gender : ')
criminal = raw_input('user Criminal Data : ')
insertOrUpdate(id,name,age,gender,criminal)
sampleNumber = 0

while True:
    a = a+1
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        sampleNumber = sampleNumber+1
        cv2.imwrite("/home/anmolmalhotra97/Desktop/openCV/IPCAM/dataset/User." +
                    str(id)+"."+str(sampleNumber)+".jpg", gray[y:y+h, x:x+w])
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        cv2.waitKey(100)
    cv2.imshow('Capturing', frame)
    key = cv2.waitKey(1)
    if(sampleNumber > 50):
        break
cv2.destroyAllWindows()
