import os
import numpy as np
import cv2
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()
path = '/home/anmolmalhotra97/Desktop/openCV/IPCAM/dataset'


def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg, 'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv2.imshow("training", faceNp)
        #cv2.waitKey(100)
    return np.array(IDs), faces


Ids, faces = getImagesWithID(path)
recognizer.train(faces, Ids)
recognizer.save('/home/anmolmalhotra97/Desktop/openCV/IPCAM/recognizer/trainingData.yml')
cv2.destroyAllWindows()
