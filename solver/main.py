# main class for our sudoku solver

import sudoku

# main method
def main():
    s = sudoku.Sudoku("../puzzles/s01a.txt")
    print(s.in_bad_state())
    print(s.is_solved())

main()
