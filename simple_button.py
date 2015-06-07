import os
from time import sleep
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)


while True:
	if not gpio.input(2):
		print "pressed"
		break
	elif gpio.input(2):
		print "waiting"
		sleep(1)

print "done."
gpio.cleanup()
