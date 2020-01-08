import numpy as np
from puzzle_class import Puzzle
import heuristics
from heapq import heappush, heappop
from heap_class import Heap

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple


class Solver:

    solution = None
    heuristic = None
    size = 0
    opened = Heap()
    closed = []
    closed_sets = set()
    count_open = 0
    nb_opened = 0
    states_max = 0
    verbose = False


    # First Node : objet puzzle à l'état initial
    def __init__(self, first_node):
        self.size = first_node.size
        self.opened.push(first_node)
        self.solution = first_node.get_solution()


    def add_closed(self, puzzle):
        if not self.closed:
            self.closed = [puzzle]
        else:
            self.closed.append(puzzle)
        self.closed_sets.add(tuple(map(tuple, puzzle.state)))

    def get_index(self, puzzles_list, puzzle):
        for i in range(0, puzzles_list.lenght()):
            if puzzles_list[i].state == puzzle.state:
                return i
        return -1

    def update_closed_puzzle(self, new_puzzle):
        index = self.get_index(self.closed, new_puzzle)
        self.closed[index].parent = new_puzzle.parent
        self.closed[index].g = new_puzzle.g

    def set_heuristic(self, heuristic_number):
        self.heuristic = heuristics.get_heuristic(heuristic_number)

    def set_time_complexity(self):
        nb_states = self.opened.len() + len(self.closed)
        if nb_states > self.states_max:
            self.states_max = nb_states

    def find_path(self, algo_number, heuristic_number):
        if algo_number == 1:
            return self.astar(heuristic_number)
        else:
            raise Exception("Error: algo needs to be ine the list")

    # A* ALGO
    def astar(self, heuristic_number=None):
        # print("test")
        # if heuristic_number is None:
        #     raise Exception("Error: heuristic function needs to be specify")
        self.set_heuristic(heuristic_number)
        success = False
        while not success and self.opened._heap:
            print("open : ", self.count_open)
            curr_node = self.opened.pop()
            self.count_open += 1
            if curr_node.h == 0 and curr_node.parent is not None:
                success = True
            else:
                self.add_closed(curr_node)
                if curr_node.parent is None:
                    curr_node.h = heuristics.calc_heuristic(self.heuristic, self.size, curr_node, self.solution)
                children_states = curr_node.get_children()
                for child_state in children_states:
                    child = Puzzle(parent=curr_node)
                    child.state = child_state
                    child.zero_position = child.get_position(0)
                    is_closed = tuple(map(tuple, child.state)) in self.closed_sets
                    if child not in self.opened._heap and not is_closed:
                        child.g = curr_node.g + 1
                        child.h = heuristics.calc_heuristic(self.heuristic, self.size, child, self.solution)
                        self.opened.push(child)
                    else:
                        if (child.g + child.h) > (curr_node.g + 1 + child.h):
                            child.g = curr_node.g + 1
                            child.parent = curr_node
                            if child.state in self.closed:
                                self.update_closed_puzzle(child)
            # print("test4")
            self.set_time_complexity()
        if success:
            print("--------------------------")
            print("PATH FOUND !")
            path = []
            while curr_node.parent:
                # print(curr_node.state)
                path.append(curr_node)
                curr_node = curr_node.parent
            # path.reverse()
            # print("--------------------------")
            # for i in (range(len(path))):
            #     # path[i].print()
            #     print(path[i].state)
            #     print()

            print("--------------------------")
            print("Number of moves:   ", len(path))
            print("Time complexity*:  ", self.count_open)
            print("Size complexity**: ", self.states_max)
            print("--------------------------")
            print("*Total number of states ever selected in the \"opened\" stack")
            print("**Maximum number of states ever represented in memory at the same time")
            print("--------------------------")
            print("         GAME OVER")
            print("--------------------------")
            return 0
        else:
            raise Exception("Error: not solvable")
