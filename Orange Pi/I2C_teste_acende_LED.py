#!/usr/bin/env python
#coding: utf8

import smbus
DEVICE_ADDR = 0x04
bus = smbus.SMBus(0)
bus.write_byte_data(DEVICE_ADDR, 0x00, 0x01)
