#/usr/bin/env python
from gpiozero import MCP3202
import time

while True:
    pot = MCP3202(channel=0)
    print(str(pot.value))
    time.sleep(0.1)
    
