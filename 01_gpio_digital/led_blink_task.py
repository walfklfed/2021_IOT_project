import RPi.GPIO as GPIO
import time

RED = 17
GREEN = 22
YELL = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELL, GPIO.OUT)
print("Running..")
for i in range(1):
    print("Red light on")
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RED, GPIO.LOW)
    print("Red light off")

    print("Green light on")
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(GREEN, GPIO.LOW)
    print("Green light off")

    print("Yellow light on")
    GPIO.output(YELL, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(YELL, GPIO.LOW)
    print("Yellow light off")

print("Finished!")
GPIO.cleanup()