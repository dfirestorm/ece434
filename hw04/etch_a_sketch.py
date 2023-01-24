#!/usr/bin/env python3
"""
Etch A Sketch.

Authors Donald Hau.

"""



import curses, os
import gpiod,time

# init paramaters
CHIP = '1'
buttons=[13,12,15,14] # P8_11, P8_12, P8_15, P8_16

def main():
    # os.system("& (python3 ~/ece434/hw04/flask_gpio.py)")
    curses.wrapper(play)

def play(window):
    curses.echo()
    s = ""
    while s != "q":
        game = EtchASketch(window)
        game.run()
        window.erase()
        window.addstr(0,0, "q to exit or b to change board size")
        s = chr(window.getch())
        window.addstr(s)

class EtchASketch:
    def __init__(self, window):
        self.window = window
        self.printString = "  "
        self.maxX = 0
        self.maxY = 0
        self.x = 0
        self.y = 0
        self.status = []
        self.setup()
        self.ended = 0

    def setup(self):
        self.window.addstr(0,0,"Use the buttons to control the cursor")
        self.window.addstr(1,0,"cannot erase and use ^C to exit")
        self.window.addstr(2,0,"How wide should the grid be? ")
        self.maxX = int(self.window.getstr())
        self.window.addstr(3,0,"How tall should the grid be? ")
        self.maxY = int(self.window.getstr())
        self.window.move(0, 0)
        curses.noecho()
        self.button_setup()
        self.array_setup()

    def button_setup(self):     
        chip = gpiod.Chip(CHIP)
        self.lines = chip.get_lines(buttons)
        self.lines.request(consumer='getset', type=gpiod.LINE_REQ_EV_RISING_EDGE)
        self.last_vals = self.lines.get_values()
    
    def array_setup(self, y:int=1, x:int=3):
        self.window.clear()
        printString = "   "
        for i in range(self.maxX):
            printString += str(i)+' ' 
        self.window.addstr(printString)
        self.window.move(self.window.getyx()[0]+1,0)
        for k in range(self.maxY):
            append_string = str(k)+": "
            self.window.addstr(append_string)
            self.window.move(self.window.getyx()[0]+1,0)
        self.window.move(y,x)
        self.write_cursor()
    
    def write_cursor(self):
        self.window.addch('X')
        self.move_cursor(0,-1)

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
        if button_number == 1:
            self.move_grid(-1,0)
            self.write_cursor()
        elif button_number == 0:
            self.move_grid(0,-1)
            self.write_cursor()
        elif button_number == 2:
            self.move_grid(1,0)
            self.write_cursor()
        elif button_number == 3:
            self.move_grid(0,1)
            self.write_cursor()

    def move_grid(self,y_off,x_off):
        self.move_cursor(y_off, x_off*2)
    
    def move_cursor(self,y_off,x_off):
        y = self.window.getyx()[0]
        x = self.window.getyx()[1]
        new_y = constrain(y + y_off, 1, self.maxY)
        new_x = constrain(x + x_off, 3, self.maxX*2+1)
        self.window.move(new_y,new_x)
    def run(self):
        while self.ended == 0:
            self.get_input()
            self.window.refresh()


def constrain(val, min_val, max_val):
    return(min(max_val, max(min_val, val)))



main()
