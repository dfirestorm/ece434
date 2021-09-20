#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""


import curses


def main():
    curses.wrapper(play())


class EtchASketch:
    def __init__(self, window):
        self.window = window
        self.printString = "  "
        self.maxX = 0
        self.maxY = 0
        self.x = 0
        self.y = 0
        self.workingArray = list()
        self.baseArray = list()
        self.status = []
        self.setup()
        self.render()
        self.ended = 0
        self.guessed = ""

    def setup(self):
        self.window.addstr("press w to move up, a to move left, s to move down, and d to move right.")
        self.window.move(1, 0)
        self.window.addstr("e will shake and o will ask to exit")
        self.window.move(2, 0)
        self.window.addstr("How wide should the grid be? ")
        self.window.refresh()
        self.maxX = self.window.getch()-48 # correct for ascii values
        self.window.move(3, 0)
        self.window.addstr("How tall should the grid be? ")
        self.window.refresh()
        self.maxY = self.window.getch()-48 # correct for ascii values
        curses.noecho()
        self.array_setup()
        self.render()
        self.window.move(1, 1)

    def array_setup(self):
        self.printString = " "
        for i in range(self.maxX):
            self.printString += str(i)
        self.workingArray.append(self.printString)
        self.baseArray = self.workingArray
        for k in range(self.maxY):
            append_string = str(k)
            self.baseArray.append(append_string)
            append_string = str(k) + self.maxX * " "
            self.workingArray.append(append_string)
        self.window.clear()
        

    def write_cursor(self):
        xy = self.window.getyx()
        # very long line to effectively just replace the character at the cursor x and y value with an X
        # not used since taking advantage of curses not rewriting screen
        # self.workingArray[xy[1] + 1] = self.workingArray[xy[1] + 1][0:xy[0] + 1] + "X" + self.workingArray[xy[0] + 1][xy[1] + 2:]
        self.window.addch('X')
        self.window.move(xy[0], xy[1]-1)

    def get_input(self):
        input_char = self.window.getch()
        xy = self.window.getyx()
        if input_char == 119: # w key in ascii
            if xy[0] > 1:
                self.window.move(xy[0]-1, xy[1])
            self.write_cursor()
        elif input_char == 97: # a key in ascii
            if xy[1] > 1:
                # self.window.move(xy[0], xy[1]-1) for if you are using smaller scale
                self.window.move(xy[0], xy[1]-2) 
            self.write_cursor()
        elif input_char == 115: # s key in ascii
            if xy[0]+1 < self.maxY:
                self.window.move(xy[0] + 1, xy[1])
            self.write_cursor()
        elif input_char == 100: # d key in ascii
            if xy[1]+1 < self.maxX * 2:
                # self.window.move(xy[0], xy[1]-2) for if you are using smaller scale
                self.window.move(xy[0], xy[1] + 2)
            self.write_cursor()
        elif input_char == 101: # e key in ascii
            self.window.clear()
            self.workingArray = self.baseArray
            self.window.move(1,1)
        elif input_char == (111 or curses.KEY_BACKSPACE): # o or backspace
            self.window.move(self.maxY + 1, 0)
            self.window.addstr("Would you like to exit or change board size? y/n ")
            self.window.refresh()
            response = self.window.getch()
            if response == 121: # y
                self.ended = True
            else:
                self.window.move(xy[0], xy[1])

    def render(self):
        orig_pos = self.window.getyx()
        print_string = ""
        self.window.move(0, 0)
        for k in range(len(self.baseArray)):
            xy = self.window.getyx()
            for j in range(len(self.baseArray[k])):
                print_string += self.baseArray[k][j]
            self.window.addstr(print_string)
            print_string = ""
            self.window.move(xy[0] + 1, 0)
        self.window.move(orig_pos[0], orig_pos[1])
        self.window.refresh()

    def run(self):
        self.get_input()
        while self.ended == 0:
            self.render()
            self.get_input()


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


main()