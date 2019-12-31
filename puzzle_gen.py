from puzzle_class import Puzzle
from solver_class import Solver
import numpy as np
import random
from puzzle_class import Puzzle
#import os


class Generator:

    puzzle = None
    nb_moves = 0
    verbose = False
    debug = False
    last_move = None

    def __init__(self, size, nb_moves, verbose=False, debug=False):
        self.puzzle = Puzzle()
        self.puzzle.size = size
        self.nb_moves = nb_moves
        if verbose:
            self.verbose = verbose
        if debug:
            self.debug = debug

    def opposite_move(self, last_move):
        for key, value in last_move.items():
            field = key
        if field == 'mv_down':
            return "mv_up"
        if field == 'mv_up':
            return "mv_down"
        if field == 'mv_right':
            return "mv_left"
        if field == 'mv_left':
            return "mv_right"

    def shuffle(self):
        if self.debug == 1:
            print(self.puzzle.size)
        if self.debug == 1:
            print("shuffle")
        for i in range (0, self.nb_moves):
            availables_moves = self.puzzle.get_available_moves(0)
            if self.last_move is not None:
                opposite_move_key = self.opposite_move(self.last_move)
                opposite_move = self.puzzle.get_move_function(opposite_move_key)
                if opposite_move in availables_moves:
                    availables_moves.remove(opposite_move)
            if self.debug == 1:
                print("Available moves are : ", )
                for move in availables_moves:
                    print ("  Name : " + move['name'] + " - Function : " + str(move['function']))
                print ("")
            random_move = random.choice(availables_moves)
            if self.debug == 1:
                print("chosen move is : ", random_move['name'])
            random_move['function'](0)
            self.last_move = random_move
        return self.puzzle

    def generate_puzzle(self):
        solved_puzzle = self.puzzle.get_solution()
        print("solution of generator : ")
        self.puzzle.state = solved_puzzle
        shuffled_puzzle = self.shuffle()
        print("shuffle : ")
        print(shuffled_puzzle.state)
        return (shuffled_puzzle)