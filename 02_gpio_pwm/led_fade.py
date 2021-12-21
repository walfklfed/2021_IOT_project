import Rpi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0)

try:
    while True:
        for i in range(0, 101, 5): 
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)

        for i in range(100, 1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)        
finally:
    pwm.stop()
    GPIO.cleanup()
    printf("cleanup and exit")    