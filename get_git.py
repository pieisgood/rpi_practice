import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

input_pin = 23

GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	while True:
		if GPIO.input(input_pin) == False:
			print("Pulling most recent code!!")
			subprocess.call(['./pull_projects.sh'])
			while GPIO.input(input_pin) == False:
				time.sleep(0.1)
finally:
	print("cleaning up")
	GPIO.cleanup()