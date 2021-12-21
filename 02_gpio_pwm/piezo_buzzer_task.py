#피에조 부저
# 도음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(70) # 소리 크기 (전압)
melody = [262, 294, 330, 349, 440, 494, 523]
music = [4, 4, 5, 5, 4, 4, 2, 4, 4, 2, 2, 1, 4, 4, 5, 5, 4, 4, 2, 4, 2, 1, 2, 0]
beat =  [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3]

try:
    for i in range(len(music)):
        pwm.ChangeFrequency(melody[music[i]])
        time.sleep(beat[i]*0.5)

    
finally:
    pwm.stop()
    GPIO.cleanup()

    import RPi.GPIO as GPIO
