import RPi.GPIO as GPIO
import time

LED = 4
GPIO.setmode(GPIO.BCM)      # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED, GPIO.OUT)   # GPIO.OUT or GPIO.IN

for i in range(100):
    GPIO.output(LED, GPIO.HIGH) #1
    print("led on")
    time.sleep(0.02)
    GPIO.output(LED, GPIO.LOW)  #0
    print("led off")
    time.sleep(0.02)

GPIO.cleanup()              # GPIO 핀상태 초기화