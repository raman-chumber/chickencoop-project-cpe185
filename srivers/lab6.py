#!/home/pi/Documents/lab6
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

try:
    
# Use BCM GPIO references
# Instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)
# Define GPIO signals to use
# Physical pins 3, 5, 7, and 11
# GPIO2, GPIO3, GPIO4, GPIO17
    StepPins = [2, 3, 4, 17]
    GPIO.setup(StepPins, GPIO.OUT)
    Seq = [[1, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 1]]
    StepCount = len(Seq)
    StepDir = 1       
        
# Read wait time from command line
    if len(sys.argv)>1:
        WaitTime = int(sys.argv[1])/float(1000)
    else:
        WaitTime = 10/float(1000)
        
# Initialize variables
    StepCounter = 0
    LoopCounter = 0
    loopmultiplier = 4500 #approx 1 rev
    TotalLoops = 1*loopmultiplier # gives approx n turns
    Looper = bool(1) # statement to break loop
    print("feeder start")
#start main loop
    while(Looper):
        
        #print(StepCounter),
        #print(Seq[StepCounter])
        
        for pin in range(0,4):
            xpin = StepPins[pin] #Get GPIO

            if Seq[StepCounter][pin]!=0:
                #print("Enable GPIO %i" %(xpin))
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
                
        StepCounter += StepDir
        LoopCounter += StepDir
        # statement to stop motor
        if (LoopCounter==TotalLoops):
            Looper = bool(0)
            print("feeder stop")
        # If the sequence ends
        # start again
        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount+StepDir
            
        # Wait before moving on
        time.sleep(WaitTime)
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    
