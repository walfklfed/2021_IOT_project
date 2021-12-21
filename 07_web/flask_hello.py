from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

default_return = '''
    <p><h1>LED ON/OFF</h1></p><a href='/led/RED/on'><button type="button">RED LED ON</button></a> <a href='/led/RED/off'><button type="button">RED LED OFF</button></a>
    <a href='/led/BLUE/on'><button type="button">BLUE LED ON</button></a> <a href='/led/BLUE/off'><button type="button">BLUE LED OFF</button></a>
    ''' 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('led2.html')

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == 'RED':
        LED_PIN = RED_LED_PIN
    else:
        LED_PIN = BLUE_LED_PIN
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return default_return + "<p><h1>" + color + " LED ON</h1></p>"
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return default_return + "<p><h1>" + color + " LED OFF</h1></p>"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()