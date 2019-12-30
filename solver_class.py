import numpy as np
from puzzle_class import Puzzle

class Solver:

    solution = None
    size = 0
    opened = []
    closed = None
    nb_opened = 0
    nb_max_opened = 0
    verbose = False
    debug = False

    def __init__(self, first_node=None, verbose=False, debug=False):
        if first_node is not None:
            self.size = first_node.size
            self.opened.append(first_node)
            self.solution = first_node.get_solution()
        else:
            print("Error: node was not provided to solver")
            exit()


# A STAR ALGO

    def find_path(self, heuristic=None):
        if heuristic is None:
            print("Error: heuristic function needs to be specify")
            exit()
        print("A star algo not done")
        return 1