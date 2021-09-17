#!/usr/bin/env python3
"""
Etch A Sketch.`

Authors Donald Hau.

"""


import curses


def main():
    play()


class EtchASketch:
    def __init__(self, window):
        self.window = window
        self.printString = "  "
        self.maxX = 0
        self.maxY = 0
        self.x = 0
        self.y = 0
        self.workingArray = list()
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
        self.maxX = self.window.getch()
        self.window.move(3, 0)
        self.window.addstr("How tall should the grid be? ")
        self.window.refresh()
        self.maxY = self.window.getch()
        curses.noecho()
        self.window.move(1, 1)
        self.array_setup()
        self.render()

    def array_setup(self):
        self.printString = "  "
        for i in range(self.maxX):
            self.printString += str(i)
        self.workingArray.append(self.printString)
        for k in range(self.maxY):
            append_string = str(k)
            self.workingArray.append(append_string)

    def write_cursor(self):
        self.window.addch('X')

    def get_input(self):
        input_char = self.window.getch()
        xy = self.window.getyx()
        if input_char == 'w':
            if xy[0] > 1:
                self.window.move(xy[0]-1, xy[1])
            self.write_cursor()
        elif input_char == 'a':
            if xy[1] > 1:
                self.window.move(xy[0], xy[1]-1)
            self.write_cursor()
        elif input_char == 's':
            if xy[0] < self.maxY:
                self.window.move(xy[0] + 1, xy[1])
            self.write_cursor()
        elif input_char == 'd':
            if xy[1] < self.maxY:
                self.window.move(xy[0], xy[1] + 1)
            self.write_cursor()
        elif input_char == 'e':
            self.window.clear()
            self.array_setup()
        elif input_char == 'o':
            response = "Would you like to exit or change board size? y/n "
            if response == 'y':
                self.ended = True

        else:
            print("press w to move up, a to move left, s to move down, and d to move right.")
            print("e will shake and o will let you exit or change board size")

    def render(self):
        self.window.clear()
        print_string = ""
        for k in range(len(self.workingArray)):
            self.window.move(0, 0)
            self.window.move(k, 0)
            for j in range(len(self.workingArray[k])):
                print_string += self.workingArray[k][j]
                print_string += " "
            self.window.addstr(print_string)
            print_string = ""
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
        s = str(input("Would you like to change board size? y/n"))[0]
    curses.nocbreak()
    curses.echo()
    curses.endwin()


main()


curses.wrapper(main)
