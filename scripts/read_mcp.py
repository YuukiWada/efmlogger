#/usr/bin/env python
from gpiozero import MCP3202

pot = MCP3202(channel=0)
print(str(pot.value))
