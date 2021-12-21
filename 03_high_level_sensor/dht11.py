import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    while True:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print(f'Temperature={t:.1f}*, Hemudity={h:.1f}%')
