from flask import Flask,render_template

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
    return render_template("led.html")

@app.route("/led/<color>/<op>")
def led_op(color, op):
    print(color, op)
    if color == "red":
        if op == "on":
            GPIO.output(RED_PIN, GPIO.HIGH)
            return '''
            <p>RED LED ON</p>
            '''
        elif op == "off":
            GPIO.output(RED_PIN, GPIO.LOW)
            return '''
            <p>RED LED OFF</p>
            '''
    elif color == "blue":
        if op == "on":
            GPIO.output(BLUE_PIN, GPIO.HIGH)
            return '''
            <p>BLUE LED ON</p>
            '''
        elif op == "off":
            GPIO.output(BLUE_PIN, GPIO.LOW)
            return '''
            <p>BLUE LED OFF</p>
            '''
    

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()