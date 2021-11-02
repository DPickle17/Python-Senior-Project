#Dylan Peck Senior Project

import sys
import RPi.GPIO as GPIO
from time import sleep
from time import process_time

GPIO.setmode(GPIO.BCM)

# Set variable names for GPIO pin numbers
data_pins = [3, 17, 27, 22, 9, 10, 4, 2]
RTS_pin = 21
RTR_pin = 20

#Local variable
CURRENT_RTS = 0      

# Set up pins as input or output
GPIO.setup(data_pins, GPIO.OUT)
GPIO.setup(RTS_pin, GPIO.OUT)
GPIO.setup(RTR_pin, GPIO.IN)


# IN A WHILE LOOP
#updating the data pins
GPIO.ouput(data_pins,new_data)
GPIO.input(data_pins)

#assert RTS
GPIO.output(RTS_pin, 1)   

#wait until RTR is asserted
while(GPIO.input(RTR_pin) == 0):

#deassert RTS
GPIO.output(RTS_pin, 0)

#wait until RTR is deasserted
while(GPIO.input(RTR_pin) == 1):

