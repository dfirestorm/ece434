#!/usr/bin/env python3
"""
Switches and Lights.

Authors Donald Hau.

"""
import gpiod
import sys
import time


chip = gpiod.Chip('gpiochip1')
buttons=[13,12,15,14] # P8_11, P8_12, P8_15, P8_16
leds = [18,16,19,17] # P9_14, P9_15, P9_16, P9_23


CONSUMER='getset'
CHIP='1'
buttons=[13,12,15,14] # P8_11, P8_12, P8_15, P8_16
leds = [18,16,19,17] # P9_14, P9_15, P9_16, P9_23

def print_event(event):
    if event.type == gpiod.LineEvent.RISING_EDGE:
        evstr = ' RISING EDGE'
    elif event.type == gpiod.LineEvent.FALLING_EDGE:
        evstr = 'FALLING EDGE'
    else:
        raise TypeError('Invalid event type')

    print('event: {} offset: {} timestamp: [{}.{}]'.format(evstr,
                                                           event.source.offset(),
                                                           event.sec, event.nsec))

chip = gpiod.Chip(CHIP)

getlines = chip.get_lines(buttons)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

setlines = chip.get_lines(leds)
setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

print("Hit ^C to stop")

while True:
    ev_lines = getlines.event_wait(sec=1)
    if ev_lines:
        for line in ev_lines:
            event = line.event_read()
            # print_event(event)
    vals = getlines.get_values()
    
    # for val in vals:
    #     print(val, end=' ')
    # print('\r', end='')

    setlines.set_values(vals)

