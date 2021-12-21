import RPI.GPIO as GPIO
import time

TRIGGER_PIN = 4
ECHO_PIN = 14
LED_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time()

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()

        duration_time = stop - start
        distance = 17160 * duration_time

        print(f'Distance : {distance:.1f}cm')

        if distance <= 20:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led on')
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led off')
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
    
