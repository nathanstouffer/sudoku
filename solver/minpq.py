# A class to store a priority queue
# ---------------------------------

import numpy as np
import square

class MinPriorityQueue:

    # CONSTRUCTOR --------------------------------------------------------------

    # construct a Sudoku object
    def __init__(self):
        self.last = 0
        self.keys  = np.zeros(128, dtype=int)                                   # initialize keys and items
        for i in range(0, len(self.keys)):
            self.keys[i] = 10
        self.items = np.empty(128, dtype='O')

    # PUBLIC METHODS -----------------------------------------------------------

    # method to peek at the value with the lowest priority
    def peek(self):
        return self.items[1]

    # method to pop the value with the lowest priority
    def pop(self):
        lowest = self.items[1]                                                  # store the lowest priority item
        self.keys[1]  = self.keys[self.last]                                    # put the last item at the top
        self.items[1] = self.items[self.last]
        self.keys[self.last] = 10
        self.items[self.last] = None
        self.last -= 1                                                          # decrement last
        self._sink_down(1)                                                      # sink the item down to update the priority queue
        return lowest

    # method to push a value to the priority queue
    def push(self, key, item):
        self.last += 1                                                          # increment last
        self.keys[self.last]  = key                                             # insert the item at the end of the priority queue
        self.items[self.last] = item
        self._swim_up(self.last)                                                # swim the item up to update the priority queue

    # method to update the priority queue according to the new state of the grid
    def update(self, puzzle):
        for i in range(1, self.last+1):
            self.items[i].update(puzzle)
            self.keys[i] = self.items[i].key()
        self._fix()

    # PRIVATE METHODS ----------------------------------------------------------

    # method to swim an item up the priority queue
    def _swim_up(self, i):
        if (i == 1):
            return
        p = int(i/2)
        if (self.keys[i] <= self.keys[p]):
            self._swap(i, p)
            self._swim_up(p)

    # method to sink an item down the priority queue
    def _sink_down(self, i):
        lc = 2*i                                                             # set up relevant variables
        rc = 2*i+1
        lk = self.keys[lc]
        rk = self.keys[rc]
        ik = self.keys[i]
        if (ik <= lk and ik <= rk):                                             # done sinking
            return
        elif (lk < ik and lk <= rk):                                            # test if should sink left
            self._swap(i, lc)
            self._sink_down(lc)
        elif (rk < ik and rk <= lk):                                            # test if should sink right
            self._swap(i, rc)
            self._sink_down(rc)
        else:
            print("MUY BAD: this case should never be reached in swim down")

    # method to construct the priority queue in place
    def _fix(self):
        cur_last = 1
        while (cur_last <= self.last):
            cur_last += 1
            self._swim_up(cur_last)

    # method to swap the keys/items at indices i and j
    def _swap(self, i, j):
        tmp_key  = self.keys[i]
        tmp_item = self.items[i]
        self.keys[i]  = self.keys[j]
        self.items[i] = self.items[j]
        self.keys[j]  = tmp_key
        self.items[j] = tmp_item

    # string method
    def __str__(self):
        ret = ""                                        # return string
        if (self.last == 0):
            return "Priority Queue empty"
        for i in range(1, self.last+1):
            ret += "\npriority: " + str(self.keys[i])
            ret += "\nitem:\n" + str(self.items[i])
            ret += "\n"
        return ret                                      # return the output string
