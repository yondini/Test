import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode( GPIO.BOARD )  
  
GPIO.setup(3, GPIO.OUT)  
  
pwm = GPIO.PWM(3,50) #50hz  
pwm.start(0)  
  
for i in range(0,3):  
  
    for dc in range(0,101,10):  
        pwm.ChangeDutyCycle(dc)  
        time.sleep(0.1)  

    for dc in range(100,-1,-10):  
        pwm.ChangeDutyCycle(dc)  
        time.sleep(0.1)  
  
pwm.stop()  
GPIO.cleanup()  
