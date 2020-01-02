

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
        exit()
    else:
        i = 0
        for line in file:
            # print("line : ")
            # print(line)
            x = 0
            split = line.split("#")
            if puzzle.size == 0 and len(split) == 1:
                puzzle.size = int(split[0])
                puzzle.solution = np.zeros((puzzle.size, puzzle.size), dtype=int)
            else:
                elems = split[0].split()
                if len(elems) != puzzle.size:
                    print("Error: your puzzle is not well formated (line " + str(i+1) + ")")
                    exit()
                # print(elems)
                # print(puzzle.state)
                elems_int = []
                for elem in elems:
                    elems_int.append(int(elem))
                row_to_be_added = np.array(elems_int)
                if len(puzzle.state) == 0:
                    puzzle.state = row_to_be_added
                else:
                    puzzle.state = np.vstack((puzzle.state, row_to_be_added))
                # print(puzzle.state)
                if len(elems) == puzzle.size and puzzle.size != 0:
                    y += 1
            i += 1
        print("puzzle.state parsé : ")
        print(puzzle.state)
        return puzzle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action="store_true", help='Verbose mode')
    parser.add_argument('-d', action="store_true", help='Debug mode')
    parser.add_argument("-f", type=str, help="Puzzle file (.txt)")
    parser.add_argument("-G",  action="store_true", help="GOD MODE")

    arg = parser.parse_args()

    #GENERATION PUZZLE
    # puzzle_gen = Generator(5, 1000)
    # new_puzzle = puzzle_gen.generate_puzzle()
    # print("new : ")
    # print (new_puzzle.state)

    answer = 0

    # Choix de la fonction heuristique
    # time.sleep(2)
    # available_answers =  ['1', '2', '3', '4']
    # while answer not in available_answers:
    #     # os.system("cls")
    #     os.system("clear")
    #     print("Which heuristic function do you want to use?")
    #     print("     1- Manhattan distance")
    #     print("     2- Euclidian distance")
    #     print("     3- Wrong values")
    #     print("     4- None")
    #     answer = input("Answer : ")
    #     if answer not in available_answers:
    #         print ("Wrong answer, please try again")
    #         time.sleep(2)
    # # os.system("cls")
    # os.system("clear")

    if arg.f:
        # Ouverture du fichier et creation du puzzle initial
        puzzle = create_from_file(arg.f, debug=arg.d, verbose=arg.v)
        print("")
        puzzle.print()
    else:
        #GENERATION PUZZLE
        size = None
        nb_moves = None
        # tant que valeurs size et nb_moves ne sont pas des nombres valides
        while size is None and nb_moves is None or (not size.isdigit() or not nb_moves.isdigit()) or int(size) == 0:
            # os.system("cls")
            os.system("clear")
            if size is not None and nb_moves is not None:
                print("Try again, you need to enter two positive numbers and size cannot be equal to 0")
            else:
                print("You are going to generate a puzzle.")
            size = input("Please chose your puzzle size: ")
            nb_moves = input("Please chose how many moves (from solution to your puzzle): ")
        puzzle_gen = Generator(int(size), int(nb_moves), debug=arg.d, verbose=arg.v)
        puzzle = puzzle_gen.generate_puzzle()
        print("You generated this puzzle: ")
        print(puzzle.state)
    print("Puzzle : ")
    puzzle.print()
    print("Calculating puzzle solution")
    puzzle_solution = puzzle.get_solution()

    if arg.G:
        print("GOD MOD ACTIVATED ! Solution: ")
        print(puzzle_solution)
        exit()

    print("[[1 2 3]" + "[8 4 0]" + "[7 6 5]]")
    solver = Solver(first_node=puzzle, debug=arg.d, verbose=arg.v)
    solution_moves = solver.find_path(answer)

if __name__ == '__main__':
    main()
