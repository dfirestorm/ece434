#!/usr/bin/env python3
import smbus
import time
import gpiod
bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x49

CONSUMER='getset'
CHIP='2'
alerts=[23,25] # P8_29, 30

bus.write_byte_data(0x48, 0x02, 25)# set reset temp for sensor 1
bus.write_byte_data(0x48, 0x03, 26)# set high temp for sensor 1
bus.write_byte_data(0x49, 0x02, 26)# set reset temp for sensor 2
bus.write_byte_data(0x49, 0x03, 27)# set high temp for sensor 2



def print_output_1():
    temp = bus.read_byte_data(address1, 0)
    print("Alert: temp 1 is " + str(temp), end="\r")
    
def print_output_2():
    temp = bus.read_byte_data(address2, 0)
    print("Alert: temp 2 is " + str(temp), end="\r")

def print_no_error(vals):
    print(f"Neither temp exceeds limits", end="\r")
    
# Set the GPIO pins:

chip = gpiod.Chip('gpiochip2')
chip = gpiod.Chip(CHIP)

getlines = chip.get_lines(alerts)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)



print("Hit ^C to stop")

try:
    while True:
        ev_lines = getlines.event_wait(sec=1)
        if ev_lines:
            for line in ev_lines:
                event = line.event_read()
                # print_event(event)
        vals = getlines.get_values()
        if vals[0] == 0:
            print_output_1()
        if vals[1] == 0:
            print_output_2()
        if not (vals[0] or vals[1]):
            print_no_error(vals)
        time.sleep(0.25)
        
except KeyboardInterrupt:
    print("Cleaning Up")

