# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 08:48:17 2020

@author: Souichirou Kikuchi
"""

import spidev
from time import sleep

V_REF = 5.0 # input Voltage
CHN = 0 # channel

spi = spidev.SpiDev()
spi.open(0, 0) # 0：SPI0、0：CE0
spi.max_speed_hz = 1000000 

def get_voltage():
    dout = spi.xfer2([((0b1000+CHN)>>2)+0b100,((0b1000+CHN)&0b0011)<<6,0]) # Din(RasPi MCP3208
    bit12 = ((dout[1]&0b1111) << 8) + dout[2] # Dout
    volts = round((bit12 * V_REF) / float(4095),4) 
    return volts

try:
    print('--- start program ---')
    while True:
        volts = get_voltage()
        print('volts= {:3.2f}'.format(volts))
        sleep(1)

except KeyboardInterrupt:
    pass
finally:
    spi.close()
    print('--- stop program ---')
