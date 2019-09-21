import numpy as np
from puzzle_class import Puzzle

class Solver:

    solution = None
    size = 0
    opened = None
    closed = None
    nb_opened = 0
    nb_max_opened = 0

#    def __init__(self, size, first_node):
 #       self.size = size
  #      self.get_solution()
  #      self.opened.append(first_node)

    def __init__(self, size, first_node):
        self.size = size
        self.get_solution()
        self.opened.append(first_node)

    def get_solution(self):
        value_max = self.size ** 2
        value = 1
        x_max = y_max = self.size - 1
        x_min = y_min = 0
        print("SOLUTION ?")
        print(self.solution)
        print(value_max)
        while 1:
            x = x_min
            y = y_min
            while x < x_max:
                print("value : ", value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                x += 1
                y = y_min
                print("solution : ", self.solution)
                value += 1
            if value >= value_max:
                break
            while y < y_max:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                y += 1
                print(self.solution)
                value += 1
            if value >= value_max:
                break
            while x > x_min:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                x -= 1
                print(self.solution)
                value += 1
            if value >= value_max:
                break
            while y > y_min:
                print(value)
                print(str(x) + ", " + str(y))
                self.solution[y, x] = value
                y -= 1
                print(self.solution)
                value += 1
            x_min += 1
            y_min += 1
            y_max -= 1
            x_max -= 1
            if value >= value_max:
                break
        print(str(x) + ", " + str(y))
        print("----")
        print(str(x_min) + ", " + str(y_min))
        print(str(x_max) + ", " + str(y_max))
        print(self.solution)

# A STAR ALGO

    def get_solution(self):
        print("A star algo not done")
        return 1