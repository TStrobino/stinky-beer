
### GPIO PORT NUMBERS
RED_PORT = 17
GREEN_PORT = 27
BLUE_PORT = 22

import sys
import time
import RPi.GPIO as GPIO
def setup_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RED_PORT, GPIO.OUT)
    GPIO.setup(GREEN_PORT, GPIO.OUT)
    GPIO.setup(BLUE_PORT, GPIO.OUT)

def setRed(value):
    GPIO.PWM(RED_PORT, value)

def setGreen(value):
    GPIO.PWM(GREEN_PORT, value)
    
def setBlue(value):
    GPIO.PWM(BLUE_PORT, value)



