# A class to represent a sudoku
# ------------------------------

import numpy as np
import square
import minpq

class Sudoku:

    # CONSTRUCTOR --------------------------------------------------------------

    # construct a Sudoku object
    def __init__(self, file_name):
        self.grid = self._read_sudoku(file_name)

    # PUBLIC METHODS -----------------------------------------------------------

    # method to solve the sudoku
    def solve(self):
        self.pq = self._init_pq()
        while (self.pq.last > 0 and self.pq.peek().key() == 1):
            sqr = self.pq.pop()
            self._update(sqr.r, sqr.c, sqr.options[0])


    # method to report if the sudoku is in a bad state
    # will return true if it finds something wrong
    # and false otherwise
    def in_bad_state(self):
        for r in range(0, 9):                                                   # iterate over the rows of the grid
            if (self.bad_row(r)):                                               # test each row
                return True
        for c in range(0, 9):                                                   # iterate over the columns of the grid
            if (self.bad_col(c)):                                               # test each column
                return True
        for br in range(0, 3):                                                  # iterate over the boxes
            for bc in range(0, 3):
                if (self.bad_box(br, bc)):                                      # test each box
                    return True
        return False                                                            # all tests passed, return true

    # method to test whether the row r is in a bad state
    def bad_row(self, r):
        return self.bad(self.get_row(r))                                        # test the row

    # method to test whether the column c is in a bad state
    def bad_col(self, c):
        return self.bad(self.get_col(c))                                        # test the column

    # method to test whether the box (r,c) is in a bad state
    # the index (r,c) is on the big grid
    def bad_box(self, r, c):
        return self.bad(self.get_box(r, c))                                     # test the box

    # method to determine whether the array (length 9) is bad
    # other methods should construct an array corresponding to their
    # object (either row, column, or box) and use this to test its state
    def bad(self, arr):
        for val in range(1, 10):                                                # iterate over the values of the sudoku
            count = 0
            for i in range(0, len(arr)):                                        # count appearances of the value
                if (val == arr[i]):
                    count += 1
            if (count > 1):                                                     # test if there are more than one
                return True
        return False

    # method to return a boolean of whether the sudoku is solved
    def is_solved(self):
        for r in range(0, 9):                                                   # check if there are any zeros in the sudoku
            for c in range(0, 9):                                               # 0 => not solved
                if (self.grid[r][c] == 0):
                    return False
        return (not self.in_bad_state())                                        # check if the sudoku is in a bad state

    # GETTER METHODS -----------------------------------------------------------

    # getter method for a row (returns an array)
    def get_row(self, r):
        return list(self.grid[r])

    # getter method for a row (returns an array)
    def get_col(self, c):
        col = []
        for r in range(0, 9):
            col.append(self.grid[r][c])
        return col

    # getter method for a row (returns an array)
    # the index (r,c) is on the big grid
    def get_box(self, r, c):
        box = []
        for i in range(0, 3):
            for j in range(0, 3):
                box.append(self.grid[3*r+i][3*c+j])
        return box

    # PRIVATE METHODS ----------------------------------------------------------

    # method to update the value of an entry in the grid
    # the position (r,c) and the value to be set should be sent in
    def _update(self, r, c, val):
        self.grid[r][c] = val
        self.pq.update(self)

    # method to initialize the priority queue
    def _init_pq(self):
        pq = minpq.MinPriorityQueue()
        for r in range(0, 9):                                                   # initialize pq
            for c in range(0, 9):
                if (self.grid[r][c] == 0):                                      # test if value is blank
                    sqr = square.Square(r, c)
                    sqr.update(self)
                    pq.push(sqr.key(), sqr)
        return pq

    # private method to read in the sudoku
    def _read_sudoku(self, file_name):
        grid = np.zeros((9, 9), dtype=int)              # create a sudoku-sized 2-d array

        fin = open(file_name, "r")                      # open file
        r = 0                                           # set row index to 0
        while (r < 9):                                  # loop 9 times
            line = fin.readline()                       # read file line
            c = 0                                       # set column index to 0
            split = line.rstrip().split(" ")            # split line into list
            for s in split:                             # loop over list elements
                grid[r][c] = int(s)                     # save element to sudoku grid
                c += 1                                  # increment column counter
            r += 1                                      # increment row counter

        fin.close()                                     # close file
        return grid                                     # return the grid

    # string method
    def __str__(self):
        ret = ""                                        # return string
        null = "0"                                      # value of null character printed to the screen
        for r in range(0, 9):                           # iterate over rows
            for c in range(0, 9):                       # iterate over column
                val = self.grid[r][c]                   # get value
                if (val != 0):                          # check if value exists (0 => unkown)
                    ret += str(self.grid[r][c]) + " "   # if value exists, add it to the output
                else:                                   # otherwise, add the null character to the output
                    ret += null + " "
            ret += "\n"                                 # add new line character
        return ret                                      # return the output string
