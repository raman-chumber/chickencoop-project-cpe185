# ~/project/srivers/lab7.py
# import required libraries
import RPi.GPIO as GPIO
import time
# valve is normally closed, turn on to open
try:
        #Use BCM GPIO references
        # Instead of physical pin numbers
    ValveTime=5 # set time for valve to operate
    GPIO.setmode(GPIO.BCM)
    basepin = 26	#set pin for base 
    GPIO.setup(basepin, GPIO.OUT)
    GPIO.output(basepin, GPIO.LOW)
    on=True # set condition for while
        
    while(on):
    # while on, turn on transistor
        GPIO.output(basepin, GPIO.HIGH)
        print("Valve open")
        # valve leave valve open for set time
        time.sleep(ValveTime)
        GPIO.output(basepin, GPIO.LOW)
        on=False
        print("Valve close")
        
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()