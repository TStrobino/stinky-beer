
DEBUG = True

### GPIO PORT NUMBERS
RED_PORT = 17
GREEN_PORT = 27
BLUE_PORT = 22

import sys
import time
import RPi.GPIO as GPIO
import config
def setup_GPIO():
    GPIO.cleanup()
    if ~DEBUG:
        GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RED_PORT, GPIO.OUT)
    GPIO.setup(GREEN_PORT, GPIO.OUT)
    GPIO.setup(BLUE_PORT, GPIO.OUT)

def stop_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()


def setRed(value):
    GPIO.PWM(RED_PORT, value/255)
    if DEBUG:
        print(f"[PhotoActivation setRed: {value}]")

def setGreen(value):
    GPIO.PWM(GREEN_PORT, value/255)
    if DEBUG:
        print(f"[PhotoActivation setGreen: {value}]")
def setBlue(value):
    GPIO.PWM(BLUE_PORT, value/255)
    if DEBUG:
        print(f"[PhotoActivation setBlue: {value}]")


