import os
import argparse
import numpy as np
from puzzle_class import Puzzle
from solver_class import Solver
from puzzle_gen import Generator
import time
import random

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

def display(solution, display_mode):
    print("--------------------------")
    print("PATH FOUND !")
    path = []
    curr_node = solution.last_node
    while curr_node.parent:
        path.append(curr_node)
        curr_node = curr_node.parent
    path.reverse()
    print("--------------------------")
    for i in (range(len(path))):
        print(path[i].state)
        print()

    print("--------------------------")
    print("Number of moves:   ", len(path))
    print("Time complexity*:  ", solution.count_open)
    print("Size complexity**: ", solution.states_max)
    print("--------------------------")
    print("*Total number of states ever selected in the \"opened\" stack")
    print("**Maximum number of states ever represented in memory at the same time")
    print("--------------------------")
    print("         GAME OVER")
    print("--------------------------")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", type=str, help="Puzzle file (.txt)")
    parser.add_argument("-G",  action="store_true", help="GOD MODE")
    parser.add_argument("-d", "--default", type=str, help="Set default mode: A*/Manhattan/3*3/Normal")

    arg = parser.parse_args()

    algo_choice = 0
    heuristic_choice = 0
    weight = None
    display_mode = 0

    # Choix de l'algo

    available_answers = [1, 2, 3]
    while algo_choice not in available_answers:
        # os.system("cls")
        os.system("clear")
        print("Which algorithm do you want to use?")
        print("     1- Astar")
        print("     2- Greedy")
        print("     3- Uniform")
        algo_choice = int(input("Answer : "))
        if algo_choice not in available_answers:
            print("Wrong answer, please try again")
            time.sleep(2)
    # os.system("cls")
    os.system("clear")

    greedy = (algo_choice == 2)

    #Choix de la fonction heuristique
    if (algo_choice and algo_choice != 3):
        available_answers = [1, 2, 3, 4]
        while heuristic_choice not in available_answers:
            os.system("clear")
            print("Which heuristic function do you want to use?")
            print("     1- Manhattan distance")
            print("     2- Euclidian distance")
            print("     3- Misplaces tiles")
            print("     4- Chebyshev")
            heuristic_choice = int(input("Answer : "))
            if heuristic_choice not in available_answers:
                print("Wrong answer, please try again")
                time.sleep(2)
        os.system("clear")
        add_weight = 0
        available_answers = [1, 2]
        while add_weight not in available_answers:
            os.system("clear")
            print("Would you like to add some weight to your heuristic?")
            print("     1- Yes")
            print("     2- No")
            add_weight = int(input("Answer : "))
            if add_weight not in available_answers:
                print ("Wrong answer, please try again")
                time.sleep(2)
        os.system("clear")

        weight = (None, 1)[add_weight == 2]
        if weight is None:
            while weight is None or not weight.isdigit():
                # os.system("cls")
                os.system("clear")
                weight = input("Please enter weight:")
            os.system("clear")



    if arg.filename:
        # Ouverture du fichier et creation du puzzle initial
        puzzle = create_from_file(arg.filename)
    else:
        #GENERATION PUZZLE
        size = None
        nb_moves = None
        difficulty = 0
        available_answers = [1, 2, 3, 4]
        # tant que valeurs size et nb_moves ne sont pas des nombres valides
        while size is None and difficulty not in available_answers or (not size.isdigit() or int(size) == 0):
            # os.system("cls")
            os.system("clear")
            print("You are going to generate a puzzle.")
            size = input("Please chose your puzzle size: ")
            os.system("clear")
            print("Chose difficulty of the puzzle (" + str(size) + "*" + str(size) + "): ")
            print("     1- Easy")
            print("     2- Normal")
            print("     3- Hard")
            print("     4- Extreme")

            difficulty = int(input("Answer: "))

        if difficulty == 1:
           difficulty = random.randint(10, 49)
        elif difficulty == 2:
           difficulty = random.randint(50, 149)
        elif difficulty == 3:
           difficulty = random.randint(150, 499)
        elif difficulty == 4:
            difficulty = random.randint(500, 2000)

        puzzle_gen = Generator(int(size), difficulty)
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
        solution_path = solver.find_path(algo_choice, heuristic_choice, greedy, int(weight))
        display(solution_path, display_mode)
        end = time.time()
        print('Solving time : {:.3f} s'.format(end-start))
    except Exception as e:
        print(e)
        exit()


if __name__ == '__main__':
    main()
