import smbus
import time

bus = smbus.SMBus(1)

DEVICE = 0x20
IODIRA = 0x00
IODIRB = 0x01
# MCP = 0x14 for OLATA and 0x15 for OLATB but i am using GPIOA/B#                                                                                                                      
GPIOA = 0x12       
GPIOB = 0x13

bus.write_byte_data(DEVICE, IODIRA, 0) #sets GPIOA to all output
bus.write_byte_data(DEVICE, IODIRB, 0) #sets GPIOB to all output
bus.write_byte_data(DEVICE, GPIOA, 0) #sets GPIOA pins to 0
bus.write_byte_data(DEVICE, GPIOB, 0) #sets GPIOB pins to 0

def lightUp(gpio):
	for i in range(0,8):
		bus.write_byte_data(DEVICE,gpio,0b0000000011111111<<i)
		time.sleep(0.05)
		
def lightDown(gpio):
	for i in range(0,8):
		bus.write_byte_data(DEVICE,gpio,0b1111111100000000>>i)
		time.sleep(0.05)


	
try:
	while True:
		lightDown(GPIOA)  #use GPIOA or GPIOB
		lightUp(GPIOA)
except KeyboardInterrupt:
	bus.write_byte_data(DEVICE,GPIOA,0)
	bus.write_byte_data(DEVICE,GPIOB,0)
	

