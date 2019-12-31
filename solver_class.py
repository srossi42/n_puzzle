import numpy as np
from puzzle_class import Puzzle


class Solver:

    solution = None
    size = 0
    opened = []
    closed = []
    nb_opened = 0
    nb_max_opened = 0
    verbose = False
    debug = False

    # First Node : objet puzzle à l'état initial
    def __init__(self, first_node=None, verbose=False, debug=False):
        if first_node is not None:
            self.size = first_node.size
            self.opened.append(first_node)
            self.solution = first_node.get_solution()
        else:
            print("Error: node was not provided to solver")
            exit()

    def is_final(self, state):
        if np.array_equal(state, self.solution):
            return True
        return False

    def add_closed(self, puzzle):
        self.closed = np.append(self.closed, puzzle)


    def add_opened(self, puzzle):
        self.opened = np.append(self.opened, puzzle)

    def delete_from_closed(self, puzzle):
        for node in self.closed:
            if np.array_equal(node.state, puzzle.state):
                self.closed = np.delete(self.closed, np.argwhere(self.closed == node))

    def delete_from_opened(self, puzzle):
        for node in self.opened:
            if np.array_equal(node.state, puzzle.state):
                self.opened = np.delete(self.closed, np.argwhere(self.opened == node))

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


        states_array = map(lambda x: x.state, array)
        for state in states_array:
            if node.state in states_array:
                return True
        return False

    def update_closed_puzzle(self, new_puzzle):
        index = self.get_index(self.closed, new_puzzle)
        self.closed[index].parent = new_puzzle.parent
        self.closed[index].g = new_puzzle.g

    def is_state_in(self, array, node):
        states_array = map(lambda x: x.state, array)
        for state in states_array:
            if node.state == state:
                return True
        return False

    # A* ALGO
    def find_path(self, heuristic=None):
        if heuristic is None:
            print("Error: heuristic function needs to be specify")
            exit()
        else:
            print("heuristic : ", heuristic)
        #     find heuristic
        success = False
        while len(self.opened) > 0 and not success:
            curr_node = self.get_best_opened()
            print("curr node : ")
            print(curr_node)
            if self.is_final(curr_node.state):
                print("curr_node is solution !")
                print(curr_node.state)
                success = True
            else:
                self.delete_from_opened(curr_node)
                self.add_closed(curr_node)
                children_states = curr_node.get_children()
                for child_state in children_states:
                    child = Puzzle()
                    child.state = child_state
                    is_opened = self.is_state_in(self.opened, child)
                    is_closed = self.is_state_in(self.closed, child)
                    if not is_opened and not is_closed:
                        print('Node is not closed nor open')
                        child.parent = curr_node
                        child.g = curr_node.g + 1
                        child.h = 1
                        # child.h = heuristic(child)
                        self.add_opened(child)
                        print(self.opened)
                    else:
                        print('Node is closed nor open')
                        if (child.g + child.h) > (curr_node.g + 1 + child.h):
                            child.g = curr_node.g + 1
                            child.parent = curr_node
                            if is_closed:
                                print('Node is closed')
                                self.delete_from_closed(child)
                                self.add_opened(child)
                                print(self.opened)
                print("opened : ")
                print(self.opened)
        if success:
            print("PATH FOUND !")
            print(self.closed)
            return 0
        else:
            print("ERROR: PATH NOT FOUND !")
        return -1
