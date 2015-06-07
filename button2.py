import os
from time import sleep
import RPi.GPIO as gpio

#prev_state = 0

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

def alternateLED(channel):
	global prev_state
	
	if not prev_state:
		prev_state = 1
		'''try:
			while True:                         ################  INFINITE ALT STATE WITHOUT while loop or put listener inside it?????  ############
				gpio.output(20, gpio.HIGH)
				gpio.output(21, gpio.LOW)
				sleep(0.5)
				gpio.output(20, gpio.LOW)
				gpio.output(21, gpio.HIGH)
				sleep(0.5)
		except:
			#gpio.output(20, gpio.LOW)
			#gpio.output(21, gpio.LOW)
			gpio.cleanup()'''
	elif prev_state:
		prev_state = 0
		'''print "button already on, you butt"
		gpio.cleanup()'''
		
		

prev_state=0  
gpio.add_event_detect(2, gpio.RISING, callback = lambda channel: alternateLED(channel), bouncetime=300)	
try:
	while True:
		sleep(0.4)
		print prev_state
except:
	gpio.cleanup()

'''
def alternateLED(channel):
	global prev_state
	
	if not prev_state:
		prev_state = 1
		try:
			while true:
				gpio.output(20, gpio.HIGH)
				gpio.output(21, gpio.LOW)
				sleep(0.5)
				gpio.output(20, gpio.LOW)
				gpio.output(21, gpio.HIGH)
				sleep(0.5)
		except:
			gpio.output(20, gpio.LOW)
			gpio.output(21, gpio.LOW)
			gpio.cleanup()    #return
	elif prev_state:
		prev_state = 0
		gpio.cleanup() #return

def main():
	print "main called"
	gpio.add_event_detect(2, gpio.RISING, callback = lambda channel: alternateLED(channel), bouncetime=300)	
	print "event detector"
	while True:
		print "poo"
		sleep(0.5)
	print "PASSED TEST"	

try:
	main()
except:
	gpio.cleanup()


'''
