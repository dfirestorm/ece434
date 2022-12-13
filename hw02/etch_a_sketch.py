#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""



import curses
import Adafruit_BBIO.GPIO as GPIO

def main():
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
        self.guessed = ""

    def setup(self):
        self.window.addstr(0,0,"press w to move up, a to move left, s to move down, and d to move right. ")
        self.window.addstr(1,0,"e will shake and o will ask to exit")
        self.window.addstr(2,0,"How wide should the grid be? ")
        self.maxX = int(self.window.getstr())
        self.window.addstr(3,0,"How tall should the grid be? ")
        self.maxY = int(self.window.getstr())
        self.window.move(0, 0)
        curses.noecho()
        self.button_setup()
        self.array_setup()

    def button_setup
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


    def key_pressed(self,key):
        print("channel = " + channel)
        state = GPIO.input(channel)
        GPIO.output(map[channel], state)
        print(map[channel] + " Toggled")

    def get_input(self):        
        input_char = chr(self.window.getch())
        
        y = self.window.getyx()[0]
        x = self.window.getyx()[1]
        self.window.addstr(self.maxY+3,0,input_char)
        self.window.move(y,x)
        match input_char:
            case 'w':
                self.move_grid(-1,0)
                self.write_cursor()
            case 'a':
                self.move_grid(0,-1)
                self.write_cursor()
            case 's':
                self.move_grid(1,0)
                self.write_cursor()
            case 'd':
                self.move_grid(0,1)
                self.write_cursor()
            case 'e':
                self.array_setup(y,x)
            case 'q':
                curses.echo()
                self.window.addstr(self.maxY+3,0, "Would you like to exit or change board size? y/n ")
                response = chr(self.window.getch())
                if response == 'y':
                    self.ended = True
                else:
                    curses.noecho()
                    self.window.move(y,x)
            case _:
                y = self.window.getyx()[0]
                x = self.window.getyx()[1]
                self.window.addstr(self.maxY+1,0,"press w to move up, a to move left, s to move down, and d to move right.")
                self.window.addstr(self.maxY+2,0,"e will shake and q will let you exit or change board size")
                self.window.move(y,x)

    def move_grid(self,y_off,x_off):
        self.move_cursor(y_off, x_off*2)
    
    def move_cursor(self,y_off,x_off):
        y = self.window.getyx()[0]
        x = self.window.getyx()[1]
        new_y = constrain(y + y_off, 1, self.maxY+1)
        new_x = constrain(x + x_off, 3, self.maxX*2+1)
        self.window.move(new_y,new_x)
    def run(self):
        self.get_input()
        while self.ended == 0:
            self.get_input()
            self.window.refresh()


def constrain(val, min_val, max_val):
    return(min(max_val, max(min_val, val)))



main()
