import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

GPIO.setup(2, GPIO.OUT)

GPIO.setup(3, GPIO.OUT)

GPIO.output(4, GPIO.LOW)

GPIO.output(2, GPIO.LOW)

GPIO.output(3, GPIO.LOW)


GPIO.setup(18, GPIO.OUT)

GPIO.setup(23, GPIO.OUT)

GPIO.setup(24, GPIO.OUT)

GPIO.output(18, GPIO.LOW)

GPIO.output(24, GPIO.LOW)

GPIO.output(23, GPIO.LOW)
