
# Python 2
# Make a LED blink

import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

while True:
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.5)



