import picamera
import time

path = '/home/pi/src4/06_multimedia'
camera = picamera.PiCamera()


try:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.rotation = 180

    while True:
        a = input('photo: 1, video: 2, exit: 9 > ')

        if a == '1':
            nowTime = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/photo_%s.jpg' % (path, nowTime))  
            input('press enter to stop')
            camera.stop_recording() 
   
        elif a == '2':
            nowTime = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('%s/video_%s.h264' % (path, nowTime))
            input('press enter to stop')
            camera.stop_recording()

        elif a == '9':
            break

        else:
            print('Wrong input!')

finally:
    camera.stop_preview()