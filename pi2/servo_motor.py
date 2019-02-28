import RPi.GPIO as GPIO
import time

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)

try:
    while True:
        a = input()
        p.ChangeDutyCycle(a)
        print("angle : "+str(a))
        # p.ChangeDutyCycle(1.5)
        #print("angle : 1.5")
        #time.sleep(1)
        #p.ChangeDutyCycle(5)
        #print("angle : 5")
        #time.sleep(1)
        #p.ChangeDutyCycle(7.5)
        #print("angle : 7.5")
        #time.sleep(1)

except KeyboardInterrupt:
    p.stop()

GPIO.cleanup()
