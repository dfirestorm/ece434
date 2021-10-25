#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""

import Adafruit_BBIO.GPIO as GPIO
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

    def setup(self):
        self.bus = smbus.SMBus(2)  # Use i2c bus 1
        self.matrix = 0x70         # Use address 0x70
        
        self.bus.write_byte_data(self.matrix, 0x21, 0)   # Start oscillator (p10)
        self.bus.write_byte_data(self.matrix, 0x81, 0)   # Disp on, blink off (p11)
        self.bus.write_byte_data(self.matrix, 0xe7, 0)   # Full brightness (page 15)
        self.array_setup()
        self.button_setup()

    def array_setup(self):
        self.output = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    
    def button_setup(self):
        self.button1="P8_11"
        self.button2="P8_12"
        self.button3="P8_15"
        self.button4="P8_16"

        GPIO.setup(self.button1, GPIO.IN)
        GPIO.setup(self.button2, GPIO.IN)
        GPIO.setup(self.button3, GPIO.IN)
        GPIO.setup(self.button4, GPIO.IN)
        
    def button_input(self):
        GPIO.add_event_detect(self.button1, GPIO.BOTH, callback=self.get_input) 
        # RISING, FALLING or BOTH
        GPIO.add_event_detect(self.button2, GPIO.BOTH, callback=self.get_input)
        GPIO.add_event_detect(self.button3, GPIO.BOTH, callback=self.get_input)
        GPIO.add_event_detect(self.button4, GPIO.BOTH, callback=self.get_input)
        
    def write_cursor(self):
        self.output[self.x*2] =self.output[self.x*2] | 2**(self.y)
        print(self.x, self.y)
        print(self.output)
    
    def get_input(self, channel):
        if channel != None:
            state = GPIO.input(channel)
            if state == False:
                return
        print("success")
        if channel == self.button2:
            if self.y != 0:
                self.y -= 1
            self.write_cursor()
        elif channel == self.button1:
            if self.x != 0:
                self.x -= 1
            self.write_cursor()
        elif channel == self.button3:
            if self.y != self.maxY:
                self.y += 1
            self.write_cursor()
        elif channel == self.button4:
            if self.x != self.maxX:
                self.x += 1
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
        self.render()

    def render(self):
        self.bus.write_i2c_block_data(self.matrix, 0, self.output)

    def run(self):
        self.button_input()
        while self.ended == 0:
            # get_input(None)
            time.sleep(1/10)
            

def play():
    s = ""
    while s != "n":
        game = EtchASketch()
        game.run()
        s = str(input("Would you like to change board size? y/n"))[0]


main()
