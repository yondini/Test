import dc_motor
import servo_motor
import Encoder
import camera
import LED
from threading import Thread
from time import sleep
import cv2
import numpy as np
#cam=cv2.VideoCapture(0)
#sleep(2)

def encoder():
    speed = 0
    while True:
       #value = _encoder.printEncoder()
       #if int(value) < 20: 
       #    _dc.Control(7.45)
       #else:
       #    _dc.Control(0)
       #print("회전 수 : "+value)      
       #sleep(1)
       a = input()
       _Servo.Control(float(a))
def camera_detection():
    angle = 6.4
    past_x1 = 0
    past_x2 = 640
    while True:
        try:
            img = _camera.readImage()
            height, width, channels = img.shape
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #print(width)
            x = [[0]*2 for i in range(2)]
            x1 = 0
            x2 = 640
            state = 0
            #blur = cv2.bilateralFilter(gray,9,100,100)
            #edges = cv2.Canny(blur,50,150,apertureSize=3)
            for i in range(width):
                #print(gray[height/2,i])
                
                if gray[int(height/3),i] < 100:
                    if gray[int(height/3),i-1] < 100:
                        x[state][0] = x[state][0] + i
                        x[state][1] = x[state][1] + 1
                else:
                    if x[state][1] > 5:
                        if state == 0: 
                            x1 = int(x[state][0] / x[state][1])
                        elif state == 1:
                            x2 = int(x[state][0] / x[state][1])
                        state = 1
                    else:
                        x[state][0] = 0
                        x[state][1] = 0
        except:
            x1 = past_x1
            x2 = past_x2
                   # state = 
        #img = cv2.imread(r'images\chessboard\frame01.jpg')
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
        #img_original = img.copy()
        #blur2 = cv2.bilateralFilter(blur,9,100,100)
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #blur = cv2.bilateralFilter(gray,9,100,100)
        #edges = cv2.Canny(blur,50,150,apertureSize=3)

        #lines = cv2.HoughLines(edges,1,np.pi/180,70)
        #resultline=[0]*3
        #try:
        #    for i in range(len(lines)):
        #        if resultline[1]<lines[i][0][1]:
        #            resultline[0]=lines[i][0][0]
        #            resultline[1]=lines[i][0][1]
        #    rho=resultline[0]
        #    theta=resultline[1]
        #    print(theta)
            #if (theta >= 0 and theta <1.2) or (theta >1.9 and theta <=3.14):
            #    _servo.Control(6.4)
            #    angle = 6.4
            #elif theta > 1.57:
            #    if angle <= 7.5:
            #        angle = angle + 0.2
            #        _servo.Control(angle)
            #else:
            #    if angle >= 5.5:
            #        angle = angle - 0.2
            #        _servo.Control(angle) 
        #    a = np.cos(theta)
        #    b = np.sin(theta)
        #    x0 = a*rho
        #    y0 = b*rho
        #    x1 = int(x0 + 1000*(-b))
        #    y1 = int(y0+1000*(a))
        #    x2 = int(x0 - 1000*(-b))
        #    y2 = int(y0 -1000*(a))
        #    if y1<y2:
        #        print(y2)
        #    else:
        #        print(y1)
        try:
            if x2 == 0 or x2 == 640:
                print("lost 1 line")
                if abs(x1 - past_x1) < abs(x1 - past_x2):
                    print("line 1")
                    _x1 = x1
                    past_x1 = x1
                    _x2 = 640
                    past_x2 = 640 
            #        _servo.Control(angle)
                else:
                    print("line 2")
                    _x2 = x1
                    past_x2 = x1
                    _x1 = 0
                    past_x1 = 0
            else:
                _x1 = x1
                past_x1 = x1
                _x2 = x2
                past_x2 = x2
 
            cv2.line(img,(_x1,int(height/3)-10),(_x1,int(height/4)+10),(0,0,255),2)
            cv2.line(img,(_x2,int(height/3)-10),(_x2,int(height/4)+10),(0,255,0),2)
            print("X1 : ",_x1)
            print("X2 : ",_x2)
            print("Center : ",320-(_x2+_x1)/2)
            cv2.line(img,(int((_x2+_x1)/2),int(height/3)),(320,480),(255,0,0),2) 
        except:
            print("can't find line")
        #res = np.vstack((img_original,img))
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
        cv2.imshow('img',img)
    
        print("----------------------------------------------")
if __name__ == '__main__':
    _dc = dc_motor.dc()
    _servo = servo_motor.servo()
    _encoder = Encoder.encoder()
    _encoder.startEncoder()
    _camera = camera.camera()
    
    _LED = LED.LED_Control()
    _LED.RED_ON()
    _LED.GREEN_ON()
    _LED.YELLOW_ON()
    t1=Thread(target=encoder)
    t2=Thread(target=camera_detection)
    t1.start()
    t2.start()

cv2.destroyAllWindows()
