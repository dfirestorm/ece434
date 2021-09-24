#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""


import curses
import Adafruit_BBIO.GPIO as GPIO
import time


def main():
    curses.wrapper(play())
    curses.echo()
    
    
class EtchASketch:
    def __init__(self, window):
        self.window = window
        self.maxX = 0
        self.maxY = 0
        self.x = 0
        self.y = 0
        self.baseArray = list()
        self.status = []
        self.setup()
        self.button_setup()
        self.render()
        self.ended = 0
        self.guessed = ""

    def setup(self):
        self.window.addstr("press w to move up, a to move left, s to move down, and d to move right.")
        self.window.move(1, 0)
        self.window.addstr("e will shake and o will ask to exit")
        self.window.move(2, 0)
        self.window.addstr("How wide should the grid be? (1-9) ")
        self.window.refresh()
        self.maxX = self.window.getch()-48 # correct for ascii values
        self.window.move(3, 0)
        self.window.addstr("How tall should the grid be? (1-9) ")
        self.window.refresh()
        self.maxY = self.window.getch()-48 # correct for ascii values
        curses.noecho()
        self.array_setup()
        self.render()
        self.window.move(1, 1)

    def array_setup(self):
        printString = " "
        for i in range(self.maxX):
            printString += str(i)
        self.baseArray.append(printString)
        for k in range(self.maxY):
            append_string = str(k)
            self.baseArray.append(append_string)
        self.window.clear()
        
    def button_setup(self):
        self.button1="P8_11"
        self.button2="P8_12"
        self.button3="P8_15"
        self.button4="P8_16"

        self.LEDr   ="P9_12"
        self.LEDy   ="P9_15"
        self.LEDg   ="P9_23"
        self.LEDb   ="P8_26"

        # Set the GPIO pins:
        GPIO.setup(self.LEDr,    GPIO.OUT)
        GPIO.setup(self.LEDy,    GPIO.OUT)
        GPIO.setup(self.LEDg,    GPIO.OUT)
        GPIO.setup(self.LEDb,    GPIO.OUT)
        GPIO.setup(self.button1, GPIO.IN)
        GPIO.setup(self.button2, GPIO.IN)
        GPIO.setup(self.button3, GPIO.IN)
        GPIO.setup(self.button4, GPIO.IN)

        # Turn on both LEDs
        GPIO.output(self.LEDr, 1)
        GPIO.output(self.LEDy, 1)
        GPIO.output(self.LEDg, 1)
        GPIO.output(self.LEDb, 1)
        # Map buttons to LEDs
        self.map = {self.button1: self.LEDr, self.button2: self.LEDy, self.button3: self.LEDg, self.button4: self.LEDb}
        
    def write_cursor(self):
        xy = self.window.getyx()
        self.window.addch('X')
        self.window.move(xy[0], xy[1])
    
    def button_input(self):
        GPIO.add_event_detect(self.button1, GPIO.BOTH, callback=self.get_input) 
        # RISING, FALLING or BOTH
        GPIO.add_event_detect(self.button2, GPIO.BOTH, callback=self.get_input)
        GPIO.add_event_detect(self.button3, GPIO.BOTH, callback=self.get_input)
        GPIO.add_event_detect(self.button4, GPIO.BOTH, callback=self.get_input)
    
    def get_input(self, channel):
        if channel != None:
            state = GPIO.input(channel)
            GPIO.output(self.map[channel], state)
            if state == False:
                return
        xy = self.window.getyx()
        input_char = None
        if input_char == 119 or channel == self.button2: # w key in ascii
            if xy[0] > 1:
                self.window.move(xy[0]-1, xy[1])
            self.write_cursor()
        elif input_char == 97 or channel == self.button1: # a key in ascii
            if xy[1] > 1:
                self.window.move(xy[0], xy[1]-1) 
            self.write_cursor()
        elif input_char == 115 or channel == self.button3: # s key in ascii
            if xy[0] < self.maxY:
                self.window.move(xy[0] + 1, xy[1])
            self.write_cursor()
        elif input_char == 100 or channel == self.button4:  # d key in ascii
            if xy[1] < self.maxX:
                self.window.move(xy[0], xy[1] + 1)
            self.write_cursor()
        elif input_char == 101: # e key in ascii
            self.window.clear()
            self.window.move(xy[0], xy[1])
        elif input_char == (111 or curses.KEY_BACKSPACE): # o or backspace
            self.window.move(self.maxY + 1, 0)
            self.window.addstr("Would you like to exit or change board size? y/n ")
            self.window.refresh()
            response = self.window.getch()
            if response == 121: # y
                self.ended = True
            else:
                self.window.move(xy[0], xy[1])
        self.render()

    def render(self):
        orig_pos = self.window.getyx()
        for k in range(len(self.baseArray)):
            self.window.addstr(k, 0, self.baseArray[k])
        self.window.move(orig_pos[0], orig_pos[1])
        self.window.refresh()

    def run(self):
        self.button_input()
        while self.ended == 0:
            # input_char = self.window.getch()
            # get_input(None)
            time.sleep(50)


def play():
    window = curses.initscr()
    curses.cbreak()
    s = ""
    while s != "n":
        game = EtchASketch(window)
        game.run()
        window.move(window.getyx()[0] + 1, 0)
        window.addstr("Would you like to change board size? y/n ")
        window.refresh()
        response = window.getch()
        if response != 121: # y
            s = "n"
    curses.nocbreak()
    curses.echo()
    curses.endwin()
    GPIO.cleanup()


main()