import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

GPIO.cleanup()	
#os.system('clear')

while True:
	GPIO.output(21, GPIO.HIGH)
	


'''
while True:
	GPIO.output(21,True)
	time.sleep(1)
	GPIO.output(21,False)
	time.sleep(.5)
'''

