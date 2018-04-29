#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  allsensors.py

#sensor libraries from Adafruit
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


#constants
SHUNT_OHMS = 0.1


def readlight():
	tsl = tsl2591.Tsl2591()  # initialize
	full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
	lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
	print ("Brightness: %.2f lux" % lux)
	print ("Full spectrum: %.2f" % full) 
	print ("Infrared: %.2f" % ir)
	return True

def readvoltage():
	ina = INA219(SHUNT_OHMS)
	ina.configure()
	
	print("Bus Voltage: %.3f V" % ina.voltage())
	try:
		print("Bus Current: %.3f mA" % ina.current())
		print("Power: %.3f mW" % ina.power())
		print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
		print("\n")
	except DeviceRangeError as e:
		# Current out of device range with specified shunt resister
		print(e)
	return True

while True:
	readlight()
	readvoltage()
	sleep(0.6)
	
