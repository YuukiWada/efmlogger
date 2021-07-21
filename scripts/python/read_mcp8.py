#!/usr/bin/env python
import spidev
import time

Vref = 5.0
ch0 = [0x01,0x80,0x00]
ch1 = [0x01,0xC0,0x00]

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 100000
spi.mode = 0

try:
    while True:
        adc = spi.xfer2(ch0)
        print(adc)
        time.sleep(1)

except KeyboardInterrupt:
    print()

