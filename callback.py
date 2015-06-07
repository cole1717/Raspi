import os
from time import sleep
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

def my_callback(channel, word):
	print "Function called: " + word


gpio.add_event_detect(2, gpio.RISING, callback = lambda channel: my_callback(channel, "CRUMPUS"), bouncetime=300)

try:
	while True:
		print "waiting...."
		sleep(0.5)
except:
	gpio.cleanup()
