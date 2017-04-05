import RPi.GPIO as GPIO
import time

pins = [11, 12, 13, 15, 16, 18, 22, 7]


	GPIO.setmode(GPIO.BOARD)        
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)   # Setzt alle Pins als Output
		GPIO.output(pin, GPIO.HIGH) 


	while True:
		for pin in pins:
			GPIO.output(pin, GPIO.LOW)	
			time.sleep(0.05)
			GPIO.output(pin, GPIO.HIGH)
		for pin in reversed(pins):
			GPIO.output(pin, GPIO.LOW)
			time.sleep(0.05)
			GPIO.output(pin, GPIO.HIGH)
