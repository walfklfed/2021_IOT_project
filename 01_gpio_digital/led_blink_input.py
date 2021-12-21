import RPi.GPIO as GPIO

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        val = input("0:off, 1:on, 9:exit >")
        if val == '0':
            GPIO.output(LED, GPIO.LOW)
            print('Led Off')
        elif val == '1':
            GPIO.output(LED, GPIO.HIGH)
            print('Led On')
        elif val == '9':
            break

finally:
    GPIO.cleanup()
    print('Finished!')