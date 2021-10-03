#Dylan Peck; Video FX FPGA

import RPi.GPIO as GPIO
from time import sleep

# Using actual pin numbers rather than BCM
GPIO.setmode(GPIO.BCM)

# Set data pins to be used for output, connected to
# PMOD ports on Nexys 4 DDR FPGA
data_pins = [3, 17, 27, 22, 9, 10, 4, 2]
GPIO.setup(pins, GPIO.OUT)

try:
    # For num runs, switch the output pins from 
    # high to low every 2 seconds, outputting to screen for
    # verification
    num_runs = 2
    for x in range(num_runs):
        GPIO.output(pins, [0, 0, 0, 0, 0, 0, 0, 0])
        print('LED OFF')
        sleep(2)
        GPIO.output(pins, [1, 1, 1, 1, 1, 1, 1, 1])
        print('LED ON')
        sleep(2)

except KeyboardInterrupt:
    print("\nUser exited with CTRL+C")

finally:
    GPIO.cleanup()                          # Clear GPIO pins so other programs can use them
