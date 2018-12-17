import numpy as np
import cv2
import urllib
import time
url="http://192.168.1.3:8080/shot.jpg"
# while True:
#     imgResp=urllib.urlopen(url)
#     imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
#     img=cv2.imdecode(imgNp,-1)
#     cv2.imshow("test",img)
#     if ord('q')==cv2.waitKey(10):
#         exit()
a = 1
face_cascade = cv2.CascadeClassifier('/home/anmolmalhotra97/Desktop/openCV/haarcascade_frontalface_default.xml')
if face_cascade.empty():
   print('file couldnt load, give up!')
while True:
    a=a+1  
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)
    for x, y, w, h in faces:
        frame=cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow('Capturing',img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
cv2.destroyAllWindows()