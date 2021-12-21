from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 5

try:
    while True:
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        display.lcd_display_string(now.strftime("%x%X"), 1)
        display.lcd_display_string(f'{t:.1f}*, {h:.1f}%', 2)


finally:
    display.lcd_clear()