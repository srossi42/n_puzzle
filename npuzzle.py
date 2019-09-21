

import argparse
import numpy as np
from puzzle_class import Puzzle
from solver_class import Solver
from test import test_movements
from puzzle_gen import Generator

def create_from_file(filename):
    y = 0
    puzzle = Puzzle()
    puzzle.state = np.array([], int)

    try:
        file = open(filename, "r")
    except FileNotFoundError as e:
        print(e)
    else:
        for line in file:
            x = 0
            split = line.split("#")
            if puzzle.size == 0 and len(split) == 1:
                puzzle.size = int(split[0])
                puzzle.solution = np.zeros((puzzle.size, puzzle.size), dtype=int)
            else:
                elems = split[0].split()
                print(elems)
                puzzle.state = np.concatenate((puzzle.state, elems), axis=None)
                if len(elems) == puzzle.size and puzzle.size != 0:
                    y += 1
        return puzzle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Puzzle file (.txt)")
    arg = parser.parse_args()
    print(arg.file)
    #Ouverture du fichier et creation du puzzle initiale
    puzzle = create_from_file(arg.file)
    print("")
    puzzle.print()

    puzzle_gen = Generator(5, 1000)
    new_puzzle = puzzle_gen.generate_puzzle()
    print("new : ")
    print (new_puzzle.state)
    #puzzle_solved = generate_puzzle(5, 1000)

    # print(puzzle.size)
    #print(puzzle.get_solution())

    #test_sol = generate_puzzle(3, 10)
    #print(test_sol)
    #zero_position = puzzle.get_position('0')
    #print("zero position :", zero_position)
    #test_movements(puzzle)

    #parse file => objet puzzle

    #puzzle.solve
    #puzzle.print_solutions

if __name__ == '__main__':
    main()
