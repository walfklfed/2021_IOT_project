#피에조 부저
# 도음 출력하기
import RPi.GPIO as GPIO
import time


BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 262 주파수 = 4옥타브 도음
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # 소리 크기

time.sleep(2)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()