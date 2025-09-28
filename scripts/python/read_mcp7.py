#!/usr/bin/env python

# MCP3202.py

import time
import pigpio # http://abyz.co.uk/rpi/pigpio/python.html

pi = pigpio.pi()

if not pi.connected:
   exit(0)

h = pi.spi_open(0, 50000) # SPI channel 1 (CE1, GPIO 7)

for i in range(100):

   (b, d) = pi.spi_xfer(h, [1,128,0])

   if b == 3:
      c1 = d[1] & 0x0F
      c2 = d[2]
      print((c1*256)+c2)
   else:
      print("Bad reading")

   time.sleep(0.2)

pi.spi_close(h)

pi.stop()
