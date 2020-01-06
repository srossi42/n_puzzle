import numpy as np
from puzzle_class import Puzzle
import heuristics
from heapq import heappush, heappop

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
    opened = []
    closed = []
    closed_sets = set()
    count_open = 0
    nb_opened = 0
    nb_max_opened = 0
    verbose = False
    debug = False

    # First Node : objet puzzle à l'état initial
    def __init__(self, first_node=None, verbose=False, debug=False):
        print("Solver init...")
        if first_node is not None:
            self.size = first_node.size
            self.opened.append(first_node)
            self.solution = first_node.get_solution()
        else:
            print("Error: node was not provided to solver")
            exit()

    # a suppriemr
    def is_final(self, state):
        if np.array_equal(state, self.solution):
            return True
        return False

    def add_closed(self, puzzle):
        if not self.closed:
            # self.closed_setstuple(map(tuple, puzzle.state))
            self.closed = [puzzle]
        else:
            self.closed.append(puzzle)
        self.closed_sets.add(tuple(map(tuple, puzzle.state)))

    def add_opened(self, puzzle):
        heappush(self.opened, puzzle)


    def remove_opened(self, puzzle):
        heappop(self.opened)
        self.count_open += 1

    def get_index(self, puzzles_list, puzzle):
        for i in range(0, puzzles_list.lenght()):
            if puzzles_list[i].state == puzzle.state:
                return i
        return -1

    def get_best_opened(self):
        best_puzzle = None
        lowest_value = 0
        for node in self.opened:
            if lowest_value == 0 or (node.h + node.g) < lowest_value:
                lowest_value = node.h + node.g
                best_puzzle = node
        return best_puzzle

    def update_closed_puzzle(self, new_puzzle):
        index = self.get_index(self.closed, new_puzzle)
        self.closed[index].parent = new_puzzle.parent
        self.closed[index].g = new_puzzle.g

    # a modifier avec les heap
    def is_opened(self, puzzle):
        return puzzle in self.opened

    def is_closed(self, state):
        state_set = tuple(map(tuple, state))
        return state_set in self.closed_sets

    def set_heuristic(self, heuristic_number):
        self.heuristic = heuristics.get_heuristic(heuristic_number)
        print("heuristic set : ", self.heuristic)


    # A* ALGO
    def find_path(self, heuristic_number=None):
        if heuristic_number is None:
            raise Exception("Error: heuristic function needs to be specify")
        self.set_heuristic(heuristic_number)
        success = False
        while self.opened is None or len(self.opened) > 0 and not success:
            curr_node = heappop(self.opened)
            self.count_open += 1
            if self.is_final(curr_node.state):
                success = True
            else:
                # self.remove_opened(curr_node)
                self.add_closed(curr_node)
                if curr_node.parent is None:
                    curr_node.h = heuristics.calc_heuristic(self.heuristic, self.size, curr_node, self.solution)
                    # print("H : ", curr_node.h)
                children_states = curr_node.get_children()
                for child_state in children_states:
                    child = Puzzle(parent=curr_node)
                    child.state = child_state
                    child.zero_position = child.get_position(0)
                    child.parent_zero_position = curr_node.get_position(0)
                    is_opened = self.is_opened(child)
                    is_closed = self.is_closed(child_state)
                    if not is_opened and not is_closed:
                        child.g = curr_node.g + 1
                        child.h = heuristics.calc_heuristic(self.heuristic, self.size, child, self.solution)
                        # print("H : ", curr_node.h)
                        self.add_opened(child)
                    else:
                        if (child.g + child.h) > (curr_node.g + 1 + child.h):
                            child.g = curr_node.g + 1
                            child.parent = curr_node
                            if child.state in self.closed:
                                self.update_closed_puzzle(child)
        if success:
            print("PATH FOUND !")
            path = []
            # while curr_node.parent:
            #     # print(curr_node.state)
            #     path.append(curr_node)
            #     curr_node = curr_node.parent
            # path.reverse()
            # for i in (range(len(path))):
            #     print(path[i].state)
            # print(curr_node.state)
            print("-----------------")
            print("Nombre de mouvements : ", len(path))
            # print("Nombre de closed : ", len(self.closed))
            print("Complexity in size : ", self.count_open)
            return 0
        else:
            print("ERROR: PATH NOT FOUND !")
        return -1
