#Dylan Peck Senior Project

import sys
import RPi.GPIO as GPIO
from time import sleep
from time import process_time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Set variable names for GPIO pin numbers
test_data = [0, 1, 0, 1, 0, 0, 0, 0]
data_pins = [7, 11, 13, 15, 12, 16, 18, 22]
RTS_pin = 29
RTR_pin = 32

#Local variable
CURRENT_RTS = 0

#Set up pins as input or output
GPIO.setup(data_pins, GPIO.OUT)
GPIO.setup(RTS_pin, GPIO.OUT)
GPIO.setup(RTR_pin, GPIO.IN)

#In a while loop
#updating the data pins
def send_byte(new_data):
    GPIO.output(data_pins, new_data)
    GPIO.input(data_pins)

#assert RTS
while(test_data is not None):
    GPIO.output(RTS_pin, 1)
    print("RTS asserted")
    break

#wait until RTR is asserted
while(1):
    if(GPIO.input(RTR_pin) == 1):
        print("RTR asserted")
        break
#    print("RTR asserted")
#    break

#deassert RTS
GPIO.output(RTS_pin, 0)
print("RTS deasserted")

#wait until RTR is deassserted
while(1):     #was set equal to 1 but wouldnt get deasserted unless set to 0
    if(GPIO.input(RTR_pin) == 0):
        print("RTR deasserted")
        break
