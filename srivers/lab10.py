#!/home/pi/project/project/srivers/lab10.py

# LCD pinouts
# 1 : VSS (5V)
# 2 : VDD (GND)
# 3 : Contrast (GND)
# 4 : Register Set
# 5 : Read / Write
# 6 : Enable
# 7 : Data Bit 0 (Not Used)
# 8 : Data Bit 1 (Not Used)
# 9 : Data Bit 2 (Not Used)
# 10: Data Bit 3 (Not Used)
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD backlight (5v)
# 16: LCD backlight (GND)

import RPi.GPIO as GPIO
import time
# define GPIO pins
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 21
LCD_D5 = 20
LCD_D6 = 13
LCD_D7 = 16

#display constants
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 #write to line 1
LCD_LINE_2 = 0x0C #write to line 2

#timing constants
E_PULSE = 0.0001
E_DELAY = 0.0001

def main():

        
    #initialize display
    lcd_init()
    
    while True:
        #display this text
        lcd_byte(LCD_LINE_1, LCD_CMD)
        lcd_string("I really hope", 1)
        lcd_byte(LCD_LINE_2, LCD_CMD)
        lcd_string("this works...", 1)
        time.sleep(3)
        
        lcd_byte(LCD_LINE_1, LCD_CMD)
        lcd_string("my life depends", 1)
        lcd_byte(LCD_LINE_2, LCD_CMD)
        lcd_string("on this working.", 1)
        time.sleep(3)
            
    def lcd_init():
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(LCD_RS, GPIO.OUT)
            GPIO.setup(LCD_E, GPIO.OUT)
            GPIO.setup(LCD_D4, GPIO.OUT)
            GPIO.setup(LCD_D5, GPIO.OUT)
            GPIO.setup(LCD_D6, GPIO.OUT)
            GPIO.setup(LCD_D7, GPIO.OUT)
            
            lcd_byte(0x33, LCD_CMD) #110011 initialise
            lcd_byte(0x32, LCD_CMD) #110010 initialise
            lcd_byte(0x28, LCD_CMD) #101000 data length, number of lines, font size
            lcd_byte(0x0C, LCD_CMD) #001100 display on, cursor off, blink off
            lcd_byte(0x06, LCD_CMD) #000110 cursor move direction
            lcd_byte(0x01, LCD_CMD) #000001 clear display
            time.sleep(E_DELAY)
            
    def lcd_byte(bits, mode):
        #send byte to data pin
        #mode = true for character
        #     = false for command
        GPIO.output(LCD_RS, mode)
            
        #high bits
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        if bits&0x10==0x10:
            GPIO.output(LCD_D4, True)
        if bits&0x20==0x20:
            GPIO.output(LCD_D5, True)
        if bits&0x40==0x40:
            GPIO.output(LCD_D6, True)
        if bits&0x80==0x80:
            GPIO.output(LCD_D7, True)
                
         #toggle enable pin
        lcd_toggle_enable()
            
        #low bits
        GPIO.output(LCD_D4, False)
        GPIO.output(LCD_D5, False)
        GPIO.output(LCD_D6, False)
        GPIO.output(LCD_D7, False)
        if bits&0x10==0x10:
            GPIO.output(LCD_D4, True)
        if bits&0x20==0x20:
            GPIO.output(LCD_D5, True)
        if bits&0x40==0x40:
            GPIO.output(LCD_D6, True)
        if bits&0x80==0x80:
            GPIO.output(LCD_D7, True)
                
        lcd_toggle_enable()
            
    def lcd_toggle_enable():
        #toggle enable
        time.sleep(E_DELAY)
        GPIO.output(LCD_E, True)
        time.sleep(E_PULSE)
        GPIO.output(LCD_E, False)
        time.sleep(E_DELAY)
        
    def lcd_string(message):
        #send string to display
        #style = left justified
        message = message.ljust(LCD_WIDTH," ")
        print(message)
        
        for i in range(LCD_WIDTH):
                lcd_byte(ord(message[i]), LCD_CHR)
                
    if __name__ == '__main__':
        
        try:
            main()
            print(message)
        except KeyboardInterrupt:
            pass
        finally:
            lcd_byte(0x01, LCD_CMD)
            lcd_string("Goodbye!", LCD_LINE_1)
            GPIO.cleanup()

# the origional author of this code is Matt Hawkins
# www.raspberrypi-spy.co.uk