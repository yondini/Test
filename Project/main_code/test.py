import dc_motor
import servo_motor
import Encoder
import camera
from threading import Thread
from time import sleep
import cv2

def encoder():
        while True:
           _encoder.printEncoder()
           print("ss")
           sleep(1)

if __name__ == '__main__':
    _dc = dc_motor.dc()
    _servo = servo_motor.servo()
    _encoder = Encoder.encoder()
    _encoder.startEncoder()
    _camera = camera.camera()
    #t= encoder()
    print("AA")
    #t.start()
    while True:
        #frame = _camera.readImage()
        #cv2.imshow('webcam',frame)
        print("ss")
        #_encoder.printEncoder()
        #sleep(1)
        #a=input()
        #_servo.Control(float(a))
        #a=input()
        #_dc.Control(float(a))

    
