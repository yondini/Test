#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import numpy as np
import cv2
import random
import os, sys

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    print(frame.shape[:2])
    #frame = cv2.resize(frame,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
    #height, width = frame.shape[:2]

    """

    if frame.shape[0] !=540: # resizing for challenge video
        frame = cv2.resize(frame, None, fx=3/4, fy=3/4, interpolation=cv2.INTER_AREA)
    """        
    cv2.imshow('result',frame)

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
     
