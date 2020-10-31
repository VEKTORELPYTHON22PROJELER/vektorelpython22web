import imutils
import cv2
from imutils.video import VideoStream
import json

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    

    def __del__(self):
        self.video.release()


    def get_frame(self):
        tani = cv2.face.LBPHFaceRecognizer_create()
        tani.read('cascades\trainer.yml')
        detector = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")
        font = cv2.FONT_HERSHEY_SIMPLEX
        id = 0

        dictionary = {}
        names = []
        dosya = open('cascades\ids.json',"r")
        dictionary = json.load(dosya)
        for key,values in dictionary.items():
            names.append(key)

        success,image = self.video.read()
        frame_flip = cv2.flip(image,1)
        gri = cv2.cvtColor(frame_flip,cv2.COLOR_BGR2GRAY)
        try:
            faces = detector.detectMultiScale(gri,scaleFactor=1.3,minNeighbors=5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame_flip,(x,y),(x+w,y+h),(0,255,0),2)
                id,oran = tani.predict(gri[y:y+h,x:x+w])
                if oran>70:
                    id = names[id]
                cv2.putText(frame_flip,str(id)+str(round(oran,2))+"%",(x+5,y-5),font,1,(255,255,255),2)
        except:
            pass
        ret,jpeg = cv2.imencode(".jpg",frame_flip)
        return jpeg.tobytes()