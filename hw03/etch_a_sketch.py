#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
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
        self.pos1 = 0
        self.pos2 = 0

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
    
    def control_setup(self):
        self.encoder1 = RotaryEncoder(eQEP1)
        self.encoder1.setAbsolute()
        self.encoder1.enable()
        self.encoder1.frequency = 1000
        
        self.encoder2 = RotaryEncoder(eQEP2)
        self.encoder2.setAbsolute()
        self.encoder2.enable()
        self.encoder2.frequency = 1000
        
    def write_cursor(self):
        self.output[1+self.x*2] =self.output[1+self.x*2] | 2**(self.y)
        #print(self.x, self.y)
        #print(self.output)
        
    def get_position(self):
        self.pos1 = self.encoder1.position
        self.pos2 = self.encoder2.position
    
    def get_input(self):
        if self.encoder1.position > self.pos1:
            if self.y != 0:
                self.y -= 1
            self.write_cursor()
        elif self.encoder2.position > self.pos2:
            if self.x != 0:
                self.x -= 1
            self.write_cursor()
        elif self.encoder1.position < self.pos1:
            if self.y != self.maxY:
                self.y += 1
            self.write_cursor()
        elif self.encoder2.position < self.pos2:
            if self.x != self.maxX:
                self.x += 1
            self.write_cursor()
        else:
            return
        self.get_position()

    def render(self):
        self.bus.write_i2c_block_data(self.matrix, 0, self.output)

    def run(self):
        self.render()
        while self.ended == 0:
            self.get_input()
            self.render()
            time.sleep(.05)
            

def play():
    s = ""
    while s != "n":
        game = EtchASketch()
        game.run()
        s = str(input("Would you like to change board size? y/n"))[0]


main()
