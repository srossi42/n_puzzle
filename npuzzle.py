import os
import argparse
import numpy as np
from puzzle_class import Puzzle
from solver_class import Solver
from puzzle_gen import Generator
import time

def create_from_file(filename):
    y = 0
    puzzle = Puzzle()
    puzzle.state = np.array([], int)

    try:
        file = open(filename, "r")
    except FileNotFoundError as e:
        print(e)
        exit()
    else:
        i = 0
        for line in file:
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
                elems_int = []
                for elem in elems:
                    elems_int.append(int(elem))
                row_to_be_added = np.array(elems_int)
                if len(puzzle.state) == 0:
                    puzzle.state = row_to_be_added
                else:
                    puzzle.state = np.vstack((puzzle.state, row_to_be_added))
                if len(elems) == puzzle.size and puzzle.size != 0:
                    y += 1
            i += 1
        return puzzle


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help="Puzzle file (.txt)")
    parser.add_argument("-G",  action="store_true", help="GOD MODE")
    arg = parser.parse_args()

    algo_choice = 0

    # Choix de l'algo
    # time.sleep(2)
    available_answers = [1, 2, 3, 4]
    while algo_choice not in available_answers:
        # os.system("cls")
        os.system("clear")
        print("Which algorithm do you want to use?")
        print("     1- Astar")
        print("     2- Ida")
        print("     3- Greedy")
        print("     4- Uniform")
        algo_choice = int(input("Answer : "))
        if algo_choice not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
    # os.system("cls")
    os.system("clear")


    heuristic_choice = 0

    #Choix de la fonction heuristique
    if (algo_choice and algo_choice <= 2):
        available_answers = [1, 2, 3, 4]
        while heuristic_choice not in available_answers:
            # os.system("cls")
            os.system("clear")
            print("Which heuristic function do you want to use?")
            print("     1- Manhattan distance")
            print("     2- Euclidian distance")
            print("     3- Wrong values")
            heuristic_choice = int(input("Answer : "))
            if heuristic_choice not in available_answers:
                print ("Wrong answer, please try again")
                time.sleep(2)
        # os.system("cls")
        os.system("clear")




    if arg.filename:
        # Ouverture du fichier et creation du puzzle initial
        puzzle = create_from_file(arg.filename)
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
            nb_moves = input("Please chose difficulty (0-19 : Easy / 20-99 : Normal / 100-500 : Hard): ")
        puzzle_gen = Generator(int(size), int(nb_moves))
        puzzle = puzzle_gen.generate_puzzle()
    print("Puzzle:\n", puzzle.state)
    try:
        puzzle_solution = puzzle.get_solution()
        puzzle.zero_position = puzzle.get_position(0)
        puzzle.zero_solution_position = np.where(puzzle_solution == 0)
    except Exception as e:
        print(e)
        exit()
    if arg.G:
        print("GOD MOD ACTIVATED ! Solution: ")
        print(puzzle_solution)
        exit()


    solver = Solver(first_node=puzzle)
    try:
        start = time.time()
        solver.find_path(algo_choice, heuristic_choice)
        end = time.time()
        print('Solving time : {:.3f} s'.format(end-start))
        # print("Duree algo : ", end-start)
        # solver.astar(heuristic_choice)
    except Exception as e:
        print(e)
        exit()


if __name__ == '__main__':
    main()
