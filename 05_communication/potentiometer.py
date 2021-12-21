import RPi.GPIO as GPIO
import spidev
import time

# SPI 인스턴스 생성
spi = spidev.SpiDev()
LED = 21
GPIO.setmode(GPIO.BCM)      # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED, GPIO.OUT)

# SPI 통신 시작
spi.open(0, 0) #bus : 0, device: 0

# SPI 통신 속도 설정
spi.max_speed_hz = 100000

# 채널에서 SPI 데이터 읽기 (0~1023)
def analog_read(channel):
    # [byte1, byte2, byte3]
    # byte2 = : channel config (channel 0) (+8) -> 0000 1000 << 4 = 1000 0000
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8)  + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0) # reading(0~1023)
        if(reading > 800):
            GPIO.output(LED, GPIO.LOW)
        else:
            GPIO.output(LED, GPIO.HIGH)
        print("Reading = %d, Voltage = %f" % (reading,reading*3.3/1024))
        time.sleep(0.5)
finally : 
    spi.close()