#!/usr/bin/env python
#coding: utf8

#Retirado de: https://yaaaas.wordpress.com/2018/04/28/orange-pi-zero-i2c-connected-to-arduino/

import smbus
DEVICE_ADDR = 0x04
bus = smbus.SMBus(0)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
