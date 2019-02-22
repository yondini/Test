import dc_motor
import servo_motor
import Encoder
import camera
import LED
from threading import Thread
from time import sleep
import cv2

def encoder():
        _encoder.printEncoder()
        while _encoder.printEncoder()!=None:
                _LED.RED_ON()
        #if _encoder.printEncoder()!=None:
        #        print(_encoder.printEncoder()
        #        _LED.RED_ON()
        #else:
        #        _LED.RED_OFF()
        sleep(1)
  
def motor():
        #frame = _camera.readImage()
        #cv2.imshow('webcam',frame)
        #_encoder.printEncoder()
        #sleep(1)
        a=input()
        _servo.Control(float(a))
        a=input()
        _dc.Control(float(a))

if __name__ == '__main__':
    _dc = dc_motor.dc()
    _servo = servo_motor.servo()
    _encoder = Encoder.encoder()
    _encoder.startEncoder()
    _camera = camera.camera()
    _LED = LED.LED_Control()
    t1=Thread(target=encoder)
    t2=Thread(target=motor)
    t1.start()
    t2.start()
    
