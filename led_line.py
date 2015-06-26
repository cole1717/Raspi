import smbus
import time

bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRA = 0x00
MCP = 0x14
GPIOA = 0x12
#############################SOMETHING IS WRONG WITH GPIOA7 #########################
bus.write_byte_data(DEVICE, MCP, 0)
bus.write_byte_data(DEVICE,MCP,11000000)
time.sleep(1)
'''
next = 0b0000000001
for i in range(0,8):
	i += 1
	bus.write_byte_data(DEVICE,MCP,next)
	time.sleep(0.1)
	print next
	next = next << 1
	'''
bus.write_byte_data(DEVICE,MCP,0)

	
	

'''
try:
	while True:
		line()
except KeyboardInterrupt:
	bus.write_byte_data(DEVICE,OLATA,0)
'''
