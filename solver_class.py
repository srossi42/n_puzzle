import numpy as np
from puzzle_class import Puzzle

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

class Solver:

    solution = None
    size = 0
    opened = []
    closed = []
    closed_sets = set()
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
            print(self.opened)
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
        # print("avant : ")
        # print(self.opened)
        if not self.opened:
            self.opened = [puzzle]
        else:
            self.opened.append(puzzle)
        # print("apres : ")
        # print(self.opened)

    def remove_opened(self, puzzle):
        for node in self.opened:
            if np.array_equal(node.state, puzzle.state):
                self.opened.remove(node)

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


    # def is_closed:
    #     states_array = map(lambda x: x.state, array)
    #     for state in states_array:
    #         if node.state in states_array:
    #             return True
    #     return False

    def update_closed_puzzle(self, new_puzzle):
        index = self.get_index(self.closed, new_puzzle)
        self.closed[index].parent = new_puzzle.parent
        self.closed[index].g = new_puzzle.g

    # a modifier avec les heap
    def is_opened(self, state):
        if self.opened:
            opened_states = map(lambda x: x, self.opened)
            for open_state in opened_states:
                if np.array_equal(open_state,  state):
                    return True
        return False

    def is_closed(self, state):
        state_set = tuple(map(tuple, state))
        return state_set in self.closed_sets


    # A* ALGO
    def find_path(self, heuristic=None):
        if heuristic is None:
            print("Error: heuristic function needs to be specify")
            exit()
        else:
            print("heuristic : ", heuristic)
        #     find heuristic
        success = False
        while self.opened is None or len(self.opened) > 0 and not success:
            curr_node = self.get_best_opened()
            # print(R+"current node : "+W)
            # print(curr_node.state)
            #  a changer par if node.h == 0 quand heuristics implementees
            if self.is_final(curr_node.state):
                print("curr_node is solution !")
                print(curr_node.state)
                success = True
            else:
                # print("node going from opened to closed")
                self.remove_opened(curr_node)
                self.add_closed(curr_node)
                children_states = curr_node.get_children()
                # print(G+'children_states : '+W)
                # print(children_states)
                for child_state in children_states:
                    # print("child : ")
                    # print(child_state)
                    is_opened = self.is_opened(child_state)
                    is_closed = self.is_closed(child_state)
                    child = Puzzle()
                    child.state = child_state
                    child.parent = curr_node
                    child.size = curr_node.size
                    if not is_opened and not is_closed:
                        # print('Node is not closed nor open')
                        child.parent = curr_node
                        child.g = curr_node.g + 1
                        child.h = 1
                        # child.h = heuristic(child)
                        # print("adding to opened list")
                        self.add_opened(child)
                        # print("added : ")
                        # print(self.opened)
                    else:
                        # print('Node is closed or open')
                        if (child.g + child.h) > (curr_node.g + 1 + child.h):
                            child.g = curr_node.g + 1
                            child.parent = curr_node
                            if child.state in self.closed:
                                # print('Node is closed')
                                self.update_closed_puzzle(child)
                # print("all opened node :")
                # for node in self.opened:
                #     print(node.state)
            # print("opened : ")
            # print(self.opened)
        if success:
            print("PATH FOUND !")
            # print(self.closed)
            print("nb closed : ", len(self.closed))
            print(curr_node.state)
            return 0
        else:
            print("ERROR: PATH NOT FOUND !")
        return -1
