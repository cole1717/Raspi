import os
from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

try:
	while True:
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(40, GPIO.LOW)
		sleep(0.5)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(40, GPIO.HIGH)
		sleep(0.5)
except:
	GPIO.cleanup()


