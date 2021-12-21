#피에조 부저
# 도음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10) # 소리 크기 (전압)
melody = [262, 294, 330, 349, 440, 494, 523]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
    
finally:
    pwm.stop()
    GPIO.cleanup()