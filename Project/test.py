import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
#cam.set(3,320)
#cam.set(4,240)
time.sleep(2)

while True:
    ret,frame = cam.read()
    #for i in range(320):
     #   for j in range(240):
      #      if frame[j,i,0] < 100 and frame[j,i,1] < 100 and frame[j,i,2]<100 :
       #         frame[j,i] = 0
        #    else:
         #       frame[j,i] = 255
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
    cv2.imshow('webcam', frame)
    #print("1")
cam.release()
cv2.destroyAllWindows()
