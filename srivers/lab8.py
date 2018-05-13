# ~/project/srivers/lab8.py
# import required libraries
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
try:
    # set pin for touch sensor
    PadPin1=16
    LedPin1=12
    GPIO.setup(PadPin1, GPIO.IN)
    GPIO.setup(LedPin1, GPIO.OUT)
    pressed1=bool(0)
    
    PadPin2=7
    LedPin2=1
    GPIO.setup(PadPin2, GPIO.IN)
    GPIO.setup(LedPin2, GPIO.OUT)
    pressed2=bool(0)
    
    PadPin3=25
    LedPin3=24
    GPIO.setup(PadPin3, GPIO.IN)
    GPIO.setup(LedPin3, GPIO.OUT)
    pressed3=bool(0)
    
    
    
    while True:
        PadPressed1=GPIO.input(PadPin1)
        PadPressed2=GPIO.input(PadPin2)
        PadPressed3=GPIO.input(PadPin3)

        if pressed1 and not PadPressed1:
            print("Button1 off")
            #print(pressed)
            GPIO.output(LedPin1, GPIO.LOW)
            
        if PadPressed1 and not pressed1:        
            print("Button1 on")
            #print(pressed)
            GPIO.output(LedPin1, GPIO.HIGH)
            
        pressed1=PadPressed1
        
        time.sleep(0.1)

        if pressed2 and not PadPressed2:
            print("Button2 off")
            #print(pressed)
            GPIO.output(LedPin2, GPIO.LOW)
            
        if PadPressed2 and not pressed2:
            print("Button2 on")
            #print(pressed)
            GPIO.output(LedPin2, GPIO.HIGH)
            
        pressed2=PadPressed2
        
        time.sleep(0.1)
        
        if pressed3 and not PadPressed3:
            print("Button3 off")
            #print(pressed)
            GPIO.output(LedPin3, GPIO.LOW)
            
        if PadPressed3 and not pressed3:
            print("Button3 on")
            #print(pressed)
            GPIO.output(LedPin3, GPIO.HIGH)
            
        pressed3=PadPressed3
        
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()