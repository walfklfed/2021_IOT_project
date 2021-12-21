import RPi.GPIO as GPIO
import time

LED = 17
SWITCH = 4
BUZZER_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)




try:
    GPIO.output(LED, 0)
    pwm = GPIO.PWM(BUZZER_PIN, 1)
    while True:
        value = GPIO.input(SWITCH) # 누르지 않은 경우 0, 누른 경우 1
        if value == 1:
            GPIO.output(LED, 1)
            pwm.start(10) # 소리 크기 (전압)
            melody = [262, 294, 330, 349, 440, 494, 523]
            for i in melody:
                pwm.ChangeFrequency(i)
                time.sleep(0.1)
        else:
            GPIO.output(LED, 0)
            pwm.stop() 
            time.sleep(1)

        print(value)  

        
  
finally:
     
    GPIO.cleanup()