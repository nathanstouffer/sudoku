# main class for our sudoku solver

import sudoku
from sys import argv
import glob

def single_puz(file_name):
    s = sudoku.Sudoku(file_name)
    print("initial state:\n" +str(s))
    s.solve()
    if (s.is_solved()):
        print("puzzle solved!\n" + str(s))
    elif (s.pq.last > 0):
        print("implemented algorithms cannot solve this puzzle\nfinal state:\n" + str(s))
    else:
        print("puzzle completed incorrectly:\n" + str(s))

def count_puz(dir_name):
    files = glob.glob(dir_name + "/*.txt")
    total = len(files)
    correct   = 0
    incorrect = 0
    unsolved  = 0
    for file_name in files:
        s = sudoku.Sudoku(file_name)
        s.solve()
        if (s.is_solved()):
            correct += 1
        elif (s.pq.last > 0):
            unsolved += 1
        else:
            incorrect += 1
    print("num puzzles:    " + str(total))
    print("num correct:    " + str(correct))
    print("num incorrect:  " + str(incorrect))
    print("num unsolved:   " + str(unsolved))

# main method
def main(input):
    if (input[-4:] == ".txt"):
        single_puz(input)
    else:
        count_puz(input)

script, name = argv
main(name)
