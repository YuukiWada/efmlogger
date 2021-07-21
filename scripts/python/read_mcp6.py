#!/usr/bin.env python
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI

CLK  = 23
MISO = 21
MOSI = 19
CS   = 24
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

SPI_PORT   = 0
SPI_DEVICE = 0
#mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#mcp.read_adc(0)

value = mcp.read_adc_difference(0)
value=mcp.read_adc(0)
print(value)
#time.sleep(0.5)
