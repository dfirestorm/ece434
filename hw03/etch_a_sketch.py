#!/usr/bin/env python3
"""
Etch A Sketch.

Authors Donald Hau.

"""

import smbus
import time





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
        left_counter = '/dev/bone/counter/1/count0'
        right_counter = '/dev/bone/counter/2/count0'
        maxCount = "1000000" # set max counter
        # with auto-closes files when done
        with open(f'{left_counter}/ceiling', 'w') as f:
            f.write(maxCount)
        with open(f'{right_counter}/ceiling', 'w') as f:
            f.write(maxCount)
        # enable both counters
        with open(f'{left_counter}/enable', 'w') as f:
            f.write('1')
        with open(f'{right_counter}/enable', 'w') as f:
            f.write('1')
        # open and store encoder positions
        self.left_file = open(f'{left_counter}/count', 'r')
        self.right_file = open(f'{right_counter}/count', 'r')
        self.get_enc_position()
        # initial position
        self.output[1+(2*self.x)] = self.output[1+(2*self.x)] ^ (1 << self.y)

    def get_enc_position(self):
        self.left_pos = read_data(self.left_file)
        self.right_pos = read_data(self.right_file)

    def get_input(self):
        #determine direction to move here
        left = read_data(self.left_file)
        right = read_data(self.right_file)
        # print(f'left {left} from {self.left_pos} right {right} from {self.right_pos} ')

        if left > self.left_pos and self.left_pos > 3: # left encoder rotated right
            self.use_input(3)
        elif left < self.left_pos or (self.left_pos < 4 and left > 1000):# left encoder rotated left
            self.use_input(0)
        if right > self.right_pos and self.right_pos > 3:# right encoder rotated right
            self.use_input(2)
        elif right < self.right_pos or (self.right_pos < 4 and right > 1000):# right encoder rotated left
            self.use_input(1)
        


    def use_input(self, button_number): 
        # print(f'moving with button {button_number}')
        if button_number == 1: # up
            self.move_cursor(-1,0)
            self.write_cursor()
        elif button_number == 0: # left
            self.move_cursor(0,-1)
            self.write_cursor()
        elif button_number == 2: # down
            self.move_cursor(1,0)
            self.write_cursor()
        elif button_number == 3: # right
            self.move_cursor(0,1)
            self.write_cursor()
        time.sleep(0.05)
        self.get_enc_position()
    
    def move_cursor(self,y_off,x_off):
        # disable old pos indicator
        self.output[1+(2*self.x)] = self.output[1+(2*self.x)] ^ (1 << self.y)
        # limit to bounds of display
        new_y = constrain(self.y + y_off, 0, self.maxY)
        new_x = constrain(self.x + x_off, 0, self.maxX)
        self.y = new_y
        self.x = new_x
        # enable new pos indicator
        self.output[1+(2*self.x)] = self.output[1+(2*self.x)] ^ (1 << self.y)

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

def read_data(file):
    file.seek(0)
    data = file.read()[:-1]
    return int(data)

def main():
    try:
        game = EtchASketch()
        game.run()
    except KeyboardInterrupt:
        return 1


main()
