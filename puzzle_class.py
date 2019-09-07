import numpy as np

class Puzzle:

    state = None
    g = 0
    h = 0
    parent = None
    size = 0

    def __init__(self, parent=None):
        if parent:
            self.parent = parent
            self.g = parent.g + 1

# A STAR ALGO

    def get_solution(self):
        return 1