# A class to represent a square in a sudoku game
# ----------------------------------------------

import numpy as np
import sudoku

class Square:

    # CONSTRUCTOR --------------------------------------------------------------

    def __init__(self, r, c):
        self.r       = r
        self.c       = c
        self.pos     = np.array([r, c])
        self.options = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # PUBLIC METHODS -----------------------------------------------------------

    # method to return the key of this item (for the priority queue)
    # the key is always the number of options remaining for this square
    def key(self):
        return len(self.options)

    # method to update the state of the options array
    def update(self, puzzle):
        row = puzzle.get_row(self.r)
        col = puzzle.get_col(self.c)
        box = puzzle.get_box(int(self.r/3), int(self.c/3))
        tmp = []
        for i in range(0, len(self.options)):
            num = self.options[i]
            if (num not in row and num not in col and num not in box):
                tmp.append(num)
        self.options = tmp

    # PRIVATE METHODS ----------------------------------------------------------

    def __str__(self):
        ret = ""
        ret += "pos: " + str(self.pos)
        ret += "\noptions: " + str(self.options)
        return ret
