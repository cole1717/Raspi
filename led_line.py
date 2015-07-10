import smbus
import time

bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRA = 0x00
MCP = 0x14     #OLATA?
GPIOA = 0x12


bus.write_byte_data(DEVICE, MCP, 0)
bus.write_byte_data(DEVICE,MCP,0x00)
time.sleep(1)
'''
next = 0b00000001
for i in range(0,17):
	if i < 7:
		i += 1
		bus.write_byte_data(DEVICE,MCP,next)
		time.sleep(0.1)
		next = next << 1
	else:
		i += 1
		bus.write_byte_data(DEVICE,MCP,next)
		time.sleep(0.1)
		next = next >> 1	
'''

def lightUp():
	next = 0b00000001
	for i in range(0,8):
		i += 1
		bus.write_byte_data(DEVICE,MCP,next)
		time.sleep(0.1)
		next = next << 1
		
def lightDown():
	next = 0b10000000
	for i in range(0,8):
		i += 1
		bus.write_byte_data(DEVICE,MCP,next)
		time.sleep(0.1)
		next = next >> 1
	
	
try:
	while True:
		lightUp()
		lightDown()
except KeyboardInterrupt:
	bus.write_byte_data(DEVICE,OLATA,0)
	
bus.write_byte_data(DEVICE,MCP,0)
