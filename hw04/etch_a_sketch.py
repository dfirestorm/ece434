#!/usr/bin/env python3
"""
Etch A Sketch.

Authors Donald Hau.

"""

import smbus
import time,gpiod

# init paramaters
CHIP = '1'
buttons=[13,12,15,14] # P8_11, P8_12, P8_15, P8_16 are LEFT, UP, DOWN, RIGHT



class EtchASketch:
    def __init__(self):
        self.maxX = 7
        self.maxY = 7
        self.x = 0
        self.y = 0
        # The first byte is GREEN, the second is RED.
        self.output = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.status = []
        self.setup()
        self.render()
        self.ended = 0
        self.left_pos = 0
        self.right_pos = 0

    def setup(self):
        self.bus = smbus.SMBus(2)  # Use i2c bus 1
        self.matrix = 0x70         # Use address 0x70
        
        self.bus.write_byte_data(self.matrix, 0x21, 0)   # Start oscillator (p10)
        self.bus.write_byte_data(self.matrix, 0x81, 0)   # Disp on, blink off (p11)
        self.bus.write_byte_data(self.matrix, 0xe7, 0)   # Full brightness (page 15)
        self.array_setup()
        self.control_setup()

    def array_setup(self):
        self.output = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_cursor()

    def control_setup(self):     
        chip = gpiod.Chip(CHIP)
        self.lines = chip.get_lines(buttons)
        self.lines.request(consumer='getset', type=gpiod.LINE_REQ_EV_RISING_EDGE)
        self.last_vals = self.lines.get_values()
    

    def get_input(self):
        input = self.lines.event_wait(sec=1)
        if input:
            vals = self.lines.get_values()
            for k in range(4):
                if vals[k] != self.last_vals[k]:
                    if vals[k] != 0:
                        self.use_input(k)
                    self.last_vals = vals
                    # time.sleep(0.1)
        # else:
        #     self.last_vals = vals

    def use_input(self, button_number): 
        # print(f'moving with button {button_number}')
        if button_number == 1: # up
            self.move_cursor(-1,0)
            self.write_cursor()
        elif button_number == 0: # left
            self.move_cursor(0,1)
            self.write_cursor()
        elif button_number == 2: # down
            self.move_cursor(1,0)
            self.write_cursor()
        elif button_number == 3: # right
            self.move_cursor(0,-1)
            self.write_cursor()
        time.sleep(0.05)
        
   
    def move_cursor(self,y_off,x_off):
        # disable old pos indicator
        self.output[1+(2*self.x)] = self.output[1+(2*self.x)] & (0 << self.y)
        # limit to bounds of display
        new_y = constrain(self.y + y_off, 0, self.maxY)
        new_x = constrain(self.x + x_off, 0, self.maxX)
        self.y = new_y
        self.x = new_x
        # enable new pos indicator
        self.output[1+(2*self.x)] = self.output[1+(2*self.x)] | (1 << self.y)

    def write_cursor(self):
        self.output[(2*self.x)] = self.output[(2*self.x)] | (1 << self.y)

    def render(self):
        self.bus.write_i2c_block_data(self.matrix, 0, self.output)

    def run(self):
        self.render()
        while self.ended == 0:
            self.get_input()
            self.render()
            time.sleep(.05)
            
def constrain(val, min_val, max_val):
    return(min(max_val, max(min_val, val)))


def main():
    try:
        game = EtchASketch()
        game.run()
    except KeyboardInterrupt:
        return 1


main()
