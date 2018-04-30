# ~/project/srivers/lab8.py
# import required libraries
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
try:
    # set pin for touch sensor
    PadPin=22
    LedPin=10
    GPIO.setup(PadPin, GPIO.IN)
    GPIO.setup(LedPin, GPIO.OUT)
    
    pressed=bool(0)
    
    while True:
        PadPressed=GPIO.input(PadPin)

        if PadPressed and not pressed:
            print("Touch sensor off")
            #print(pressed)
            GPIO.output(LedPin, GPIO.LOW)
            
        if pressed and not PadPressed:
            print("Touch sensor on")
            #print(pressed)
            GPIO.output(LedPin, GPIO.HIGH)
            
        pressed=PadPressed
        
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()