# Import packages
import time
import math
import RPi.GPIO as GPIO

# Set standard GPIO pinout
GPIO.setmode(GPIO.BCM)

# Set up OUTPUT pins (LEDs)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

# Set up Input Pin (pushbutton)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setwarnings(False)

inputcheck = 0
global winning

def turnOn(led):
	GPIO.output(led, 1)
	return
	
def turnOff(led):
	GPIO.output(led, 0)
	return
	
def butnpress(channel):
	global winning
	if (inputcheck == 1):
		print('Winner!')
		winning = 1

	else:
		print('Loser!')
		if (winning == 1):
			winning == 1
		else:
			winning == 0
		
	return winning
		

try:
	GPIO.add_event_detect(12, GPIO.RISING, callback = butnpress, bouncetime = 300)
	outputs = [18, 19, 21, 22, 23, 25, 26]
	inputs = [12]
	global winning
	winning = 0
	#Gpio.add_event_detect(12, gpio.rising)
	#gpio.add_event_callback(12, buttonPress)
	while (winning == 0):
		for i in outputs:
			
			if (i==22):
				inputcheck = 1
			else:
				inputcheck = 0
					
			turnOn(i)
			count = 0
			count2 = 0	
			while (count2<10):
				
				count2 = count2+1
				while (count < 150000):
					count = count + 1
				turnOff(i)
			
	if (winning):
		while (1):
			GPIO.output(22, 1)
			time.sleep(.5)
			GPIO.output(22, 0)
			time.sleep(.5)

except KeyboardInterrupt:
	GPIO.cleanup()


