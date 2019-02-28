import cv2
import numpy as np
import time

class camera():
    def __init__(self):
        self.cam = cv2.VideoCapture("line_640x480.mp4")
        #cam.set(3,320)
        #cam.set(4,240)
        time.sleep(2)
    #while True:
    def readImage(self):
        ret,frame = self.cam.read()
        return frame
    #if cv2.waitKey(1)&0xFF == ord('q'):
    #    break
    #cv2.imshow('webcam', frame)
    #print("1")
    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()
