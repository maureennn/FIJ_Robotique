#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print()
# and the integer division
# mind your parentheses!

########################################################################
# This library is used for communicating with the FIJ SpyTank
# History
# ------------------------------------------------
# Author	Date      		Comments
# M. Osee	07 Nov   18  	Creation, based on Gopigo lib
#
########################################################################

import sys
import time

if sys.platform == 'uwp':
	import winrt_smbus as smbus
	bus = smbus.SMBus(1)
else:
	import RPi.GPIO as GPIO
	import smbus

	# for RPI version 1, use "bus = smbus.SMBus(0)"
	rev = GPIO.RPI_REVISION
	if rev == 2 or rev == 3:
		bus = smbus.SMBus(1)
	else:
		bus = smbus.SMBus(0)


# This is the address for the SpyTank arduino
address = 0x08

def sendCmd(cmd, param1=0, param2=0, param3=0):
    writeBlock(address, [cmd, param1, param2, param3])


#Write a byte to the GoPiGo
def writeNumber(value):
	try:
		bus.write_byte(address, value)
		time.sleep(.005)
	except IOError:
		return -1
	return 1

#Read a byte from the GoPiGo
def readByte():
	try:
		number = bus.read_byte(address)
		time.sleep(.005)
	except IOError:
		return -1
	return number


# TODO : decider si cette fonction est encore utile

#Write I2C block
def writeBlock(address, block):
	try:
		op = bus.write_i2c_block_data(address, block[0], block[1:len(block)])
		time.sleep(.005)
		return op
	except IOError:
		return -1
	return 1
