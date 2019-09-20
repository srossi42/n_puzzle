

import argparse
from puzzle_class import Puzzle
import numpy as np
from test import test_movements

def init(filename):
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
    puzzle = init(arg.file)
    print("")
    puzzle.print()
    # print(puzzle.size)
    puzzle.get_solution()
    #zero_position = puzzle.get_position('0')
    #print("zero position :", zero_position)
    #test_movements(puzzle)

    #parse file => objet puzzle

    #puzzle.solve
    #puzzle.print_solutions

if __name__ == '__main__':
    main()
