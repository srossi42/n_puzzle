import argparse
import numpy as np
from Class.puzzle_class import Puzzle
from Class.solver_class import Solver
from puzzle_gen import Generator
import time
import menu

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

    display_mode = 0
    heuristic_choice = 0
    weight = 1
    algo_choice = menu.chose_algo()
    greedy = (algo_choice == 2)



    if algo_choice and algo_choice != 3:
        heuristic_choice = menu.chose_heuristic()
        weight = menu.chose_weight()
    display_mode = menu.chose_display()
    if arg.filename:
        puzzle = create_from_file(arg.filename)
    else:
        nb_moves = None
        size = menu.chose_size()
        difficulty = menu.chose_difficulty(size)
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
