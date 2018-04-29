#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  allsensors.py

# sensor libraries from Adafruit
#==============================

#1. light sensor
import tsl2591

#2 voltage sensor INA219
from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep

#3. real time clock DS3231  
import smbus
import os
import time

# Release RTC 3231
os.system('sudo rmmod rtc_ds1307')

# Setup RTC 3231 for temperature reading
bus = smbus.SMBus(1)
address = 0x68
CONV = 32

# constants
SHUNT_OHMS = 0.1

# Function to Read light sensor data
def readlight():
	tsl = tsl2591.Tsl2591()  # initialize
	full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
	lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
	print ("Brightness: %.2f lux" % lux)
	print ("Full spectrum: %.2f" % full) 
	print ("Infrared: %.2f" % ir)
	return True

# Function to read voltage data
def readvoltage():
	ina = INA219(SHUNT_OHMS)
	ina.configure()
	
	print("Bus Voltage: %.3f V" % ina.voltage())
	try:
		print("Bus Current: %.3f mA" % ina.current())
		print("Power: %.3f mW" % ina.power())
		print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
	except DeviceRangeError as e:
		# Current out of device range with specified shunt resister
		print(e)
	return True

# Force a conversion and wait until it completes
def convTemp(address):
    byte_control = bus.read_byte_data(address,0x0E)
    if byte_control&CONV == 0:
        bus.write_byte_data(address, 0x0E, byte_control|CONV)
    byte_control = bus.read_byte_data(address,0x0E)
    while byte_control&CONV != 0:
        time.sleep(1)
        byte_control = bus.read_byte_data(address,0x0E)
    return True

# Get temperature in degrees C
def getTemp(address):
    convTemp(address)
    byte_tmsb = bus.read_byte_data(address,0x11)
    byte_tlsb = bus.read_byte_data(address,0x12)
    tinteger = (byte_tmsb & 0x7f) + ((byte_tmsb & 0x80) >> 7) * -2**8
    tdecimal = (byte_tmsb >> 7) * 2**(-1) + ((byte_tmsb & 0x40) >> 6) * 2**(-2)
    return tinteger + tdecimal
# Convert and output temperature data
def readtemperature():
	Celsius = getTemp(address)
	Fahrenheit = 9.0/5.0 * Celsius + 32
	print ("Fahrenheit: %.1f *F" % Fahrenheit)
	print ("Celsius: %.1f *C" % Celsius)
	return True

# loop to call functions one by one
while True:
	readlight() 			# Call light sensor function
	readvoltage()			# Call voltage sensor 
	readtemperature()		# Call temperature sensor
	print("\n")
	sleep(0.6)
	
