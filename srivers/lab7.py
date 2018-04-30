import RPi.GPIO as GPIO
import time
try:
# Use BCM GPIO references
# Instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	
	basepin = 27	
	
	GPIO.setup(basepin, GPIO.OUT)
	
	GPIO.output(basepin, GPIO.LOW)
	
	on=bool(1)

	while(on):
           GPIO.output(basepin, GPIO.HIGH)
           print("valve open")
           time.sleep(10)
           GPIO.output(basepin, GPIO.LOW)
           on=bool(0)
           print("Valve close")
        
except keyboardinterrupt:
    pass
finally:
    GPIO.cleanup()
           
           
           
           
