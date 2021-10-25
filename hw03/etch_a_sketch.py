#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""


import curses
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time


def main():
    play()


class EtchASketch:
    def __init__(self):
        self.maxX = 15
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

    def setup(self):
        self.bus = smbus.SMBus(2)  # Use i2c bus 1
        self.matrix = 0x70         # Use address 0x70
        
        self.bus.write_byte_data(self.matrix, 0x21, 0)   # Start oscillator (p10)
        self.bus.write_byte_data(self.matrix, 0x81, 0)   # Disp on, blink off (p11)
        self.bus.write_byte_data(self.matrix, 0xe7, 0)   # Full brightness (page 15)
        self.array_setup()

    def array_setup(self):
        self.output = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

    def write_cursor(self):
        self.output[self.x] =self.output[self.x] | 2**(self.y)
        print(self.x, self.y)
        print(self.output)
    
        

    def get_input(self):
        input_str = str(input("Input here"))[0]
        print("success")
        input_char = input_str.lower()
        if input_char == 'w':
            if self.y > 0:
                self.y -= 1
            self.write_cursor()
        elif input_char == 'a':
            if self.x > 0:
                self.x -= 2
            self.write_cursor()
        elif input_char == 's':
            if self.y < self.maxY:
                self.y += 1
            self.write_cursor()
        elif input_char == 'd':
            if self.x < self.maxX:
                self.x += 2
            self.write_cursor()
        elif input_char == 'e':
            self.array_setup()
        elif input_char == 'o':
            response = str(input("Would you like to exit? y/n "))[0]
            if response == 'y':
                self.ended = 1
        else:
            print("press w to move up, a to move left, s to move down, and d to move right.")
            print("e will shake and o will let you exit or change board size")

    def render(self):
        self.bus.write_i2c_block_data(self.matrix, 0, self.output)

    def run(self):
        self.get_input()
        while self.ended == 0:
            self.render()
            self.get_input()

def play():
    s = ""
    while s != "n":
        game = EtchASketch()
        game.run()
        s = str(input("Would you like to change board size? y/n"))[0]


main()
