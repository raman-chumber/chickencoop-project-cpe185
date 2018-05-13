# ~/project/srivers/lab9.py
import RPi.GPIO as GPIO
import time

try:
    
    forward = 20 #GPio pin 
    backward = 21 #GPio pin
    sleeptime=1/2 #wait timer
    ftime = 1 #forward timer
    rtime = 1 #reverse timer
    loopcount = 5 #loop counter
    
    GPIO.setmode(GPIO.BCM) # sets GPIO pin mode
    GPIO.setup(forward, GPIO.OUT) # assign pin as output
    GPIO.setup(backward, GPIO.OUT) # assign pin as output
    
    def Forward(): #define function forward
        print("forward") # print forward
        GPIO.output(forward, GPIO.HIGH) # set pin assigned to forward high
        time.sleep(ftime) # leave pin high for some set time
        GPIO.output(forward, GPIO.LOW) # set pin low
        
    def Reverse(): # define function reverse
        print("reverse") # print reverse
        GPIO.output(backward, GPIO.HIGH) # set in assigned to reverse high
        time.sleep(rtime) # leave pin high for some set time
        GPIO.output(backward, GPIO.LOW) # set pin low
        
    for x in range(0,loopcount):
        
        x += 1
        
        Forward() # turn motor in forward direction
        
        time.sleep(sleeptime) # wait
         
        Reverse() # turn motor in reverese direction
        
        time.sleep(sleeptime) # wait
        
        
except KeyboardInterrupt:
    pass
    print("exit...")

finally:
    GPIO.cleanup()
    
    