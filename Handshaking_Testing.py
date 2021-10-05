# Dylan Peck; Video FX FPGA

import sys
import RPI.GPIO as GPIO
from time import sleep
from time import processing_time

GPIO.setmode(GPIO.BCM)

# Set variables for the GPIO pin numbers
pins = [3, 17, 27, 22, 9, 10, 4, 2]
RTS = 21
RTR = 20
local = 0          #local variable

