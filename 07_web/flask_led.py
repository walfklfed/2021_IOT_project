from flask import Flask

import RPi.GPIO as GPIO
import time


app = Flask(__name__)

RED_PIN = 4
BLUE_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)


@app.route("/")
def hello_world():
    return '''
    <h1>Hello, Flask</h1>
    <a href = "/led/red/on"><h1>RED LED ON</h1></a>
    <a href = "/led/blue/on"><h1>BLUE LED ON</h1></a>
    <a href = "/led/red/off"><h1>RED LED OFF</h1></a>
    <a href = "/led/blue/off"><h1>BLUE LED OFF</h1></a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color, op):
    print(color, op)
    if color == "red":
        if op == "on":
            GPIO.output(RED_PIN, GPIO.HIGH)
            return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
            '''
        elif op == "off":
            GPIO.output(RED_PIN, GPIO.LOW)
            return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
            '''
    elif color == "blue":
        if op == "on":
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
            '''
        elif op == "off":
            GPIO.output(BLUE_PIN, GPIO.LOW)
            return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
            '''
    

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()