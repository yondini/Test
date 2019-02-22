import dc_motor
import servo_motor
import Encoder
import camera
import LED
from threading import Thread
from time import sleep
import cv2

def encoder():
        while True:
           _encoder.printEncoder()
           #print("ss")
           sleep(1)
def motor():
    while True:
        #frame = _camera.readImage()
        #cv2.imshow('webcam',frame)
        #_encoder.printEncoder()
        #sleep(1)
        a=input()
        _servo.Control(float(a))
        a=input()
        _dc.Control(float(a))
def camera_detection():
    while True:
        img = _camera.readImage()
        index = 0
        for i in range(100):
            for j in range(100):
                if img[j,i,0] < 30 and img[j,i,1] < 30 and img[j,i,2]<30:
                    index = index + 1
                if index > 30:
                    print("@@@@@@@@@@@@@@@@@@@@@STOP@@@@@@@@@@@@@@@@@@")
                    _dc.Control(0)
                    return
                    #t2.stop()
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
    #t1=Thread(target=encoder)
    #t2=Thread(target=motor)
    #t3=Thread(target=camera_detection)
    #t1.start()
    #t2.start()
    _servo.Control(6.4)
    _dc.Control(7.7)
    sleep(3)
    _servo.Control(5.6)
    sleep(3)
    _servo.Control(7.2)
    sleep(3)
    _servo.Control(5.6)
    sleep(3)
    _servo.Control(7.2)
    sleep(3)
    _servo.Control(5.6)
    sleep(3)
    _servo.Control(7.2)
    sleep(3)
    _servo.Control(5.6)
    sleep(3)
    _servo.Control(7.2)
    sleep(3)
    _dc.Control(0)
