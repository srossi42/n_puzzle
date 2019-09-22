

import os
import time
import argparse
import numpy as np
from puzzle_class import Puzzle
from solver_class import Solver
from test import test_movements
from puzzle_gen import Generator

def create_from_file(filename, debug=False, verbose=False):
    y = 0
    puzzle = Puzzle(debug=False, verbose=False)
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
    parser.add_argument('-v', action="store_true", help='Verbose mode')
    parser.add_argument('-d', action="store_true", help='Debug mode')
    parser.add_argument("file", help="Puzzle file (.txt)")
    arg = parser.parse_args()
    print(arg.file)
    answer = 0
    time.sleep(2)
    available_answers =  ['1', '2', '3', '4']
    while answer not in available_answers:
        os.system("cls")
        # os.system("clear")
        print("Which heuristic function do you want to use?")
        print("     1- Manhattan distance")
        print("     2- Euclidian distance")
        print("     3- Wrong values")
        print("     4- None")
        answer = input("Answer : ")
        if answer not in available_answers:
            print ("Wrong answer, please try again")
            time.sleep(2)
    os.system("cls")
    # os.system("clear")


    #Ouverture du fichier et creation du puzzle initiale
    puzzle = create_from_file(arg.file, debug=arg.d, verbose=arg.v)
    print("")
    puzzle.print()

 #GENERATION PUZZLE
    puzzle_gen = Generator(5, 1000, debug=arg.d, verbose=arg.v)
    new_puzzle = puzzle_gen.generate_puzzle()
    new_puzzle_solution = new_puzzle.get_solution()
    print("new : ")
    print (new_puzzle.state)

    solver = Solver(first_node=new_puzzle, debug=arg.d, verbose=arg.v)
    solution_moves = solver.find_path(answer)

if __name__ == '__main__':
    main()
