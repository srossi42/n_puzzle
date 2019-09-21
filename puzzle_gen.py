from puzzle_class import Puzzle
from solver_class import Solver
import numpy as np
import random
from puzzle_class import Puzzle
#import os


class Generator:

    puzzle = None
    nb_moves = 0
    verbose = 0
    debug = 0

    def __init__(self, size, nb_moves, verbose = 0, debug = 0):
        self.puzzle = Puzzle()
        self.puzzle.size = size
        self.nb_moves = nb_moves
        if verbose:
            self.verbose = verbose
        if debug:
            self.debug = debug

    def shuffle(self):
        if self.debug == 1:
            print(self.puzzle.size)
        if self.verbose == 1:
            print("shuffle")
        for i in range (0, self.nb_moves):
            availables_moves = self.puzzle.get_available_moves(0)
            if self.verbose == 1:
                print("Available moves are : ", )
                print ("  ", end = "")
                for i in range(0, len(availables_moves)):
                    for move in availables_moves[i]:
                        print (move, end=" ")
                print ("")
            random_move = random.choice (availables_moves)
            for name, function in random_move.items():
                if self.verbose == 1:
                    print ("chosen move is : ", name)
                function(0)
        return self.puzzle

    def generate_puzzle(self):
        solved_puzzle = self.puzzle.get_solution(self.puzzle.size)
        print("solution of generator : ")
        print (solved_puzzle)
        self.puzzle.state = solved_puzzle
        shuffled_puzzle = self.shuffle()
        print("shuffle : ")
        print(shuffled_puzzle.state)
        return (shuffled_puzzle)