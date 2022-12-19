#!/usr/bin/env python3
import smbus
import time
import Adafruit_BBIO.GPIO as GPIO
bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a
bus.write_byte_data(0x48, 0x02, 26)
bus.write_byte_data(0x48, 0x03, 27)
bus.write_byte_data(0x4a, 0x02, 24)
bus.write_byte_data(0x4a, 0x03, 25)

alert="P9_12"
alert2="P9_15"

def print_output_1(channel):
    temp = bus.read_byte_data(address1, 0)
    print("Alert: temp 1 is " + str(temp), end = "\r")
    time.sleep(0.25)
    
def print_output_2(channel):
    temp = bus.read_byte_data(address2, 0)
    print("Alert: temp 2 is " + str(temp), end = "\r")
    time.sleep(0.25)
    
# Set the GPIO pins:
GPIO.setup(alert, GPIO.IN)
GPIO.setup(alert2, GPIO.IN)
GPIO.add_event_detect(alert, GPIO.BOTH, callback=print_output_1) 
GPIO.add_event_detect(alert2, GPIO.BOTH, callback=print_output_2) 
        
        

try:
    while True:
        time.sleep(100)   # Let other processes run

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()