import RPi.GPIO as IO
import time

encPinA = 6
encPinB = 13

IO.setmode(IO.BCM)
IO.setwarnings(False)
IO.setup(encPinA, IO.IN, pull_up_down=IO.PUD_UP)
IO.setup(encPinB, IO.IN, pull_up_down=IO.PUD_UP)

encoderPos = 0
_pinA = 0
A_pos = 0
def encoderA(channel):
    global encoderPos
    global _pinA
    global A_pos
    if IO.input(encPinA) == IO.input(encPinB):
        encoderPos += 1
    else:
        encoderPos -= 1
    _pinA = channel
    A_pos = encoderPos
    #print('PinA : %d, encoder : %d' %(channel, encoderPos))
    
def encoderB(channel):
    global encoderPos
    if IO.input(encPinA) == IO.input(encPinB):
        encoderPos -= 1
    else:
        encoderPos += 1
    #print('PinB : %d, encoder : %d' %(channel, encoderPos))

IO.add_event_detect(encPinA, IO.BOTH, callback=encoderA)
#IO.add_event_detect(encPinB, IO.BOTH, callback=encoderB)

while True:
    print('PinA : %d, encoder : %d' %(_pinA, A_pos))
    time.sleep(1)  
