"""
Etch A Sketch.`

Authors Donald Hau.

"""
# !/usr/bin/env python3
chmod +x


def main():
    play()


class EtchASketch:
    def __init__(self):
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
        print("press w to move up, a to move left, s to move down, and d to move right.")
        print("e will shake and o will ask to exit")
        self.maxX = int(input("How wide should the grid be? "))
        self.maxY = int(input("How tall should the grid be? "))
        self.array_setup()

    def array_setup(self):
        self.printString = "  "
        for i in range(self.maxX):
            self.printString += str(i)
        self.workingArray.append(self.printString)
        for k in range(self.maxY):
            append_string = str(k) + " " * self.maxX
            self.workingArray.append(append_string)

    def write_cursor(self):
        # very long line to effectively just replace the character at the cursor x and y value with an X
        self.workingArray[self.y + 1] = self.workingArray[self.y + 1][0:self.x + 1] + "X" + self.workingArray[
                                                                                                self.y + 1][self.x + 2:]

    def get_input(self):
        input_str = str(input())[0]
        input_char = input_str.lower()
        if input_char == 'w':
            if self.y != 0:
                self.y -= 1
            self.write_cursor()
        elif input_char == 'a':
            if self.x != 0:
                self.x -= 1
            self.write_cursor()
        elif input_char == 's':
            if self.y != self.maxY:
                self.y += 1
            self.write_cursor()
        elif input_char == 'd':
            if self.x != self.maxX:
                self.x += 1
            self.write_cursor()
        elif input_char == 'e':
            self.workingArray.clear()
            self.array_setup()
        elif input_char == 'o':
            response = str(input("Would you like to exit or change board size? y/n "))[0]
            if response == 'y':
                self.ended = 1
        else:
            print("press w to move up, a to move left, s to move down, and d to move right.")
            print("e will shake and o will let you exit or change board size")

    def render(self):
        print_string = ""
        for k in range(len(self.workingArray)):
            for j in range(len(self.workingArray[k])):
                print_string += self.workingArray[k][j]
                print_string += " "
            print(print_string)
            print_string = ""

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
