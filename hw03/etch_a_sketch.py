#!/usr/bin/env python3
"""
Etch A Sketch.

Authors Donald Hau.

"""

import smbus
import time


def main():
    play()


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
    
    def write_cursor(self):
        self.output[self.x] += 1 << self.y

    def control_setup(self):
        left_counter = '/dev/bone/counter/1/count0'
        right_counter = '/dev/bone/counter/2/count0'
        maxCount = 1000000
        with open(f'{left_counter}/ceiling', 'w') as f:
            f.write(maxCount)
        with open(f'{right_counter}/ceiling', 'w') as f:
            f.write(maxCount)
        with open(f'{left_counter}/enable', 'w') as f:
            f.write('1'))
        with open(f'{right_counter}/enable', 'w') as f:
            f.write('1')
        self.left_file = open(f'{left_counter}/count', 'r')
        self.right_file = open(f'{right_counter}/count', 'r')
        self.get_enc_position()

    def get_enc_position(self):
        self.left_pos = read_data(self.left_file)
        self.right_pos = read_data(self.right_file)

    def get_input(self):
        #write code to determine direction to move here
        


    def use_input(self, button_number): 
        if button_number == 1:
            self.move_cursor(-1,0)
            self.write_cursor()
        elif button_number == 0:
            self.move_cursor(0,-1)
            self.write_cursor()
        elif button_number == 2:
            self.move_cursor(1,0)
            self.write_cursor()
        elif button_number == 3:
            self.move_cursor(0,1)
            self.write_cursor()
    
    def move_cursor(self,y_off,x_off):
        new_y = constrain(self.y + y_off, 0, self.maxY)
        new_x = constrain(self.x + x_off, 0, self.maxX)
        self.y = new_y
        self.x = new_x

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

def read_data(file):
    file.seek(0)
    data = file.read()[:-1]
    return data

def play():
    s = ""
    while s != "n":
        game = EtchASketch()
        game.run()
        s = str(input("Would you like to exit? y/n"))[0]


main()
