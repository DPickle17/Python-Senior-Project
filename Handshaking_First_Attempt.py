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

#Set up GPIO pins as inputs or outputs
GPIO.setup(pins, GPIO.OUT)
GPIO.setup(RTS, GPIO.OUT)
GPIO.setup(RTR, GPIO.IN)

#Send a single byte of data to the FPGA
def send_byte(output_byte)
    GPIO.output(pins, output_byte)

try:
    #Control to be updated by the incoming data, then passed to the send_byte
    #function to be outputted to the pins
    control = [0, 0, 0, 0, 0, 0, 0, 0]
    count = 1

    start = processing_time()
    for data in sys.stdin.buffer.read(65536)

        data = data - 128
        data_bin = bin(data & 0b11111111)
        data_bin = data_bin[2:0].zfill(8)

        #Fill in control with data
        for i in range(len(control)):
            control[i-1] = int(data_bin[i-1])

        #Recieve handshaking signals
        if data:
            print("Byte: " + str(count))
            count = count + 1
            send_byte(control)
            GPIO.output(RTS, 1)
            print("Pi sent data")
            while True:                                               #Wait for the FPGA to recieve
                print("Waiting for FPGA to recieve")
                if GPIO.input(RTR)
                    print("FPGA recieved")
                    GPIO.output(RTS, 0)
                    break
                while True:                                           #Wait for the FPGA to acknowledge 
                    print("Waiting for FPGA to acknowledge")
                    if not GPIO.inptu(RTR)
                        print{"Pi sees that FPGA acknowledged")
                        break
                    print("Handshake completed!")

                print(GPIO.input(RTR))

    except KeyboardInterrupt
        print("User exited with CTRL+C")

    finally:
        stop = processing_time()
        print("Elapsed time in seconds: " + stop - start)
        GPIO.cleanup()                                              #Clears GPIO pins so they can be used for other programs
