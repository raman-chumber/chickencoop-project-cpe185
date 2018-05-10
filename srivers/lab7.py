# ~/project/srivers/lab7.py
# import required libraries
import RPi.GPIO as GPIO
import time
# valve is normally closed, turn on to open
try:
# Use BCM GPIO references
# Instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	#set pin for base of transistor
	basepin = 27	
	
	GPIO.setup(basepin, GPIO.OUT)
	
	GPIO.output(basepin, GPIO.LOW)
	# set condition for while
	on=bool(1)
	# set time for valve to operate in sec
        ValveTime=10
        
        while(on):
        # while on, turn on transistor
           GPIO.output(basepin, GPIO.HIGH)
           print("Valve open")
           # valve leave valve open for set time
           time.sleep(ValveTime)
           GPIO.output(basepin, GPIO.LOW)
           on=bool(0)
           print("Valve close")
        
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()