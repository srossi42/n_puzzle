from puzzle_class import Puzzle
from solver_class import Solver
import numpy as np
import random



def shuffle(puzzle, nb_moves):
    print(puzzle.size)
    print("shuffle")
    for i in range (0, nb_moves):
        availables_moves = puzzle.get_available_moves(0)
        print("Available moves are : ", )
        print ("  ", end = "")
        for i in range(0, len(availables_moves)):
            for move in availables_moves[i]:
                print (move, end=" ")
        print ("")
        random_move = random.choice (availables_moves)
        for name, function in random_move.items():
            print ("chosen move is : ", name)
            function(0)


        #print("chosen move is : ", random_move.key())

    return puzzle


def generate_puzzle(size, nb_moves):
    puzzle = Puzzle()
    puzzle.size = size
    solved_puzzle = puzzle.get_solution(size)
    puzzle.state = solved_puzzle
    print("solution of generator : ")
    puzzle.print()
    new_puzzle = shuffle(puzzle, nb_moves)
    return (solved_puzzle)