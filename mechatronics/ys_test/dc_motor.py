import RPi.GPIO as GPIO
import time

class dc():
    def __init__(self):
        pin = 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.p = GPIO.PWM(pin, 50)
        self.p.start(0)
        print("dd1")
    def Control(self,value):
        try:
            self.p.ChangeDutyCycle(value)
            print("angle : "+str(value))
        except KeyboardInterrupt:
            self.p.stop()
            print("dd2")
    def __del__(self):
        print("dd3")
        self.p.stop()
        GPIO.cleanup()

