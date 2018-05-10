# ~/project/srivers/lab9.py
import RPi.GPIO as GPIO
import time

try:
    
    forward = 20
    backward = 21
    sleeptime=2
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(forward, GPIO.OUT)
    GPIO.setup(backward, GPIO.OUT)
    
    def Forward(x):
        GPIO.output(forward, GPIO.HIGH)
        print("forward")
        time.sleep(sleeptime)
        GPIO.output(forward, GPIO.LOW)
        
    def Reverse(x):
        GPIO.output(backward, GPIO.HIGH)
        print("backward")
        time.sleep(sleeptime)
        GPIO.output(backward, GPIO.LOW)
        
    while (1):
        
        Forward(5)
        
        time.sleep(sleeptime)
        
        Reverse(5)
        
except KeyboardInterrupt:
    pass
    print("Forced exit...")

finally:
    GPIO.cleanup()