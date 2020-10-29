import imutils
import cv2
from imutils.video import VideoStream


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(2)
    

    def __del__(self):
        self.video.release()


    def get_frame(self):
        success,image = self.video.read()
        frame_flip = cv2.flip(image,1)
        ret,jpeg = cv2.imencode(".jpg",frame_flip)
        return jpeg.tobytes()