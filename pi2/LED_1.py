import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode( GPIO.BOARD )  
  
GPIO.setup(3, GPIO.OUT)  
  
pwm = GPIO.PWM(3,50) #50hz  
pwm.start(0)  
while True:  
    pwm.ChangeDutyCycle(20) 
    #pwm.stop() 
GPIO.cleanup()  
