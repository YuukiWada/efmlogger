#/usr/bin/env python
from gpiozero import MCP3202
import time

Vref = 5.0

while True:
    #pot0 = MCP3202(channel=0)
    pot1 = MCP3202(channel=0)
    print(pot1.value * Vref)
        
    #print(pot1.value * Vref)
    time.sleep(1.0)
    
