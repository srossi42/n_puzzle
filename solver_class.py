import numpy as np
from puzzle_class import Puzzle
import heuristics
from heapq import heappush, heappop
from heap_class import Heap
import time

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
    closed = {}
    count_open = 0
    nb_opened = 0
    states_max = 0


    # First Node : objet puzzle à l'état initial
    def __init__(self, first_node):
        self.size = first_node.size
        self.opened.push(first_node, (first_node.g + first_node.h))
        self.solution = first_node.get_solution()

    def add_closed(self, puzzle):
        self.closed[puzzle.__hash__()] = puzzle

    def set_heuristic(self, heuristic_number):
        self.heuristic = heuristics.get_heuristic(heuristic_number)

    def set_time_complexity(self):
        nb_states = self.opened.len() + len(self.closed)
        if nb_states > self.states_max:
            self.states_max = nb_states

    def find_path(self, algo_number, heuristic_number, greedy, weight):
        if algo_number <= 4:
            return self.astar(heuristic_number, greedy, weight)
        elif algo_number == 4:
            print("ida not ready")
            exit()
            return self.ida(heuristic_number)
        else:
            raise Exception("Error: algo needs to be ine the list")


# Greedy : on choisit une heuristique et osef du g => priority = h
# Uniform : heuristic == 0 => priority = g
#

    # A* ALGO
    def astar(self, heuristic_number=None, greedy=False, weight=1):
        print("Heuristic number : ", heuristic_number)
        print("greedy : ", greedy)
        self.set_heuristic(heuristic_number)
        success = False
        # prevTime = time.time()
        while not success and self.opened._heap:
            # if (self.count_open % 1000 == 0):
            #     print(time.time() - prevTime)
            #     prevTime = time.time()
            #     print("open : ", self.count_open)
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
                    hash_state = hash(tuple(map(tuple, child_state)))
                    if hash_state not in self.closed and hash_state not in self.opened._heap:
                        child = Puzzle()
                        child.parent = curr_node
                        child.size = curr_node.size
                        child.zero_solution_position = curr_node.zero_solution_position
                        child.state = child_state
                        child.g = curr_node.g + 1
                        # child.g = curr_node.g + 1
                        child.zero_position = child.get_position(0)
                        child.h = heuristics.calc_heuristic(self.heuristic, self.size, child, self.solution)
                        if heuristic_number == 0:
                            priority = child.g
                        else:
                            priority = ((child.g + child.h * weight), (child.h * weight))[greedy]
                        #  si greedy true : cost uniquement
                        self.opened.push(child, priority)
            self.set_time_complexity()
        if success:
            print("--------------------------")
            print("PATH FOUND !")
            path = []
            while curr_node.parent:
                # print(curr_node.state)
                path.append(curr_node)
                curr_node = curr_node.parent
            path.reverse()
            print("--------------------------")
            for i in (range(len(path))):
                # path[i].print()
                print(path[i].state)
                print()

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