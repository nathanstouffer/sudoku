# main class for our sudoku solver

import sudoku
from sys import argv

# main method
def main(file_name):
    s = sudoku.Sudoku(file_name)
    print("initial state:\n" +str(s))
    s.solve()
    if (s.is_solved()):
        print("puzzle solved!\n" + str(s))
    elif (s.pq.last > 0):
        print("current algorithms cannot solve this puzzle\nfinal state:\n" + str(s))
    else:
        print("puzzle completed incorrectly:\n" + str(s))

script, name = argv
main(name)
