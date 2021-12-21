import cv2
import RPi.GPIO as GPIO #RPi.GPIO 라이브러리를 GPIO로 사용
from time import sleep  #time 라이브러리의 sleep함수 사용
from lcd import drivers
import time

GPIO.setmode(GPIO.BCM) 



servoPin_x          = 15   # 서보 핀
SERVO_MAX_DUTY    = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY    = 3   # 서보의 최소(0도) 위치의 주기

servoPin_y          = 14   # 서보 핀
servoPin_shot         = 23   # 서보 핀



GPIO.setup(servoPin_x, GPIO.OUT)  # 서보핀 출력으로 설정
GPIO.setup(servoPin_y, GPIO.OUT)  # 서보핀 출력으로 설정
GPIO.setup(servoPin_shot, GPIO.OUT)  # 서보핀 출력으로 설정

LED = 17
SWITCH = 4
BUZZER_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(LED, 0)


servo_x = GPIO.PWM(servoPin_x, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo_shot = GPIO.PWM(servoPin_shot, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo_y = GPIO.PWM(servoPin_y, 50)  # 서보핀을 PWM 모드 50Hz로 사용하기 (50Hz > 20ms)
servo_x.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.
servo_y.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.
servo_shot.start(0)  # 서보 PWM 시작 duty = 0, duty가 0이면 서보는 동작하지 않는다.


cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('xml/face.xml')

call_x = 0
call_y = 0

def setServoPos(degree):
  # 각도는 180도를 넘을 수 없다.
  if degree > 180:
    degree = 180

  # 각도(degree)를 duty로 변경한다.
  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
  # duty 값 출력


  # 변경된 duty값을 서보 pwm에 적용

  return duty
  







def find_face(x,y):
    find_x = 320-x
    find_y = 240-y


    if find_x > 0:  # 원점보다 왼쪽으로 치우쳤을때
        if find_y > 0: #위로
            return 0
        else:       #아래로
            return 1
    else:           # 원점보다 오른쪽으로 치우쳤을때
        if find_y > 0:
            return 2
        else:
            return 3




if not cap.isOpened():
    print("Camera open failed")
    exit()

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        find_face_val = find_face(x+w/2,y+h/2)

        if find_face_val == 0:
            call_x+=-1
            call_y+=-1


        elif find_face_val == 1:
            call_x+=-1
            call_y+=1
       

        elif find_face_val == 2:
            call_x+=1
            call_y+=-1

        else:
            call_x+=1
            call_y+=1
     



        
        servo_x.ChangeDutyCycle(setServoPos(call_x))
        servo_y.ChangeDutyCycle(setServoPos(call_y))
        
        

    pwm = GPIO.PWM(BUZZER_PIN, 1)
    GPIO.output(LED, 0)

    value = GPIO.input(SWITCH) # 누르지 않은 경우 0, 누른 경우 1
    if value == 1:
        GPIO.output(LED, 1)
        pwm.start(10) # 소리 크기 (전압)
        melody = [262, 294, 330, 349, 440, 494, 523]
        for i in melody:
            pwm.ChangeFrequency(i)
            time.sleep(0.1)
        servo_shot.ChangeDutyCycle(setServoPos(90))
        

    else:
        GPIO.output(LED, 0)
        pwm.stop() 

    
    


    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break


cap.release()
cv2.destroyAllWindows()





   







