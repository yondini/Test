import RPi.GPIO as GPIO
import time

class LED_Control():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        input_value = True
    
    def RED_ON(self):
        print("RED ON")
        GPIO.output(12, True)
        GPIO.setup(12, GPIO.OUT)
    
    def RED_OFF(self):
        print("RED OFF")
        GPIO.output(12, False)   
    
    def GREEN_ON(self):
        print("GREEN ON")
        GPIO.output(20, True)
   
    def GREEN_OFF(self):
        print("GREEN OFF")
        GPIO.output(20, False)

    def YELLOW_ON(self):
        print("YELLOW ON")
        GPIO.output(16, True)

    def YELLOW_OFF(self):
        print("YELLOW OFF")
        GPIO.output(16, False)
    
    def __del__(self):
        self.RED_OFF()
        self.GREEN_OFF()
        self.YELLOW_OFF()
        GPIO.cleanup()
