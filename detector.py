import numpy as np
import cv2
import urllib
import time
url="http://192.168.1.3:8080/shot.jpg"
import sqlite3
def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    print(cmd);
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

a = 1
face_cascade = cv2.CascadeClassifier('/home/anmolmalhotra97/Desktop/openCV/haarcascade_frontalface_default.xml')
if face_cascade.empty():
    print('file couldnt load, give up!')

rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('/home/anmolmalhotra97/Desktop/openCV/IPCAM/recognizer/trainingData.yml')
id = 0
#font =(FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.25
fontColor = (0, 0, 255)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
while True:
    a = a+1
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgNp,-1)
    #print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        if(conf<60):
            profile=getProfile(id)
            if(profile!=None):
                    cv2.putText(frame, str(profile[1]), (x, y+h+30),fontFace, fontScale, fontColor, 2)
                    cv2.putText(frame, str(profile[2]), (x, y+h+60),fontFace, fontScale, fontColor, 2)
                    cv2.putText(frame, str(profile[3]), (x, y+h+90),fontFace, fontScale, fontColor, 2)
                    cv2.putText(frame, str(profile[4]), (x, y+h+120),fontFace, fontScale, fontColor, 2)
        else:
            cv2.putText(frame, "UNKNOWN", (x, y+h),fontFace, fontScale, fontColor, 2)
    cv2.imshow('Capturing', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
