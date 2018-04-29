#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  light-sensor.py


import tsl2591

while True:
	tsl = tsl2591.Tsl2591()  # initialize
	full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
	lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
	print lux, full, ir
