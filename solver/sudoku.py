# A class to represent a sudoku
# ------------------------------

import numpy as np

class Sudoku:

    # construct a Sudoku object
    def __init__(self, file_name):
        self.grid = self._read_sudoku(file_name)


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
