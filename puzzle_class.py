import numpy as np
import os
import time

class Puzzle:

    state = None
    g = 0
    h = 0
    parent = None
    size = 0
    zero_position = None
    verbose = False
    debug = False
    tempo = 0
    sys = None

    def __init__(self, parent=None, verbose=False, debug=False, sys="unix"):
        if parent:
            self.parent = parent
            self.g = parent.g + 1
            self.size = parent.size
        if verbose:
            self.verbose = verbose
        if debug:
            self.debug = debug
        self.sys = sys

    def __gt__(self, other):
        return (self.h + self.g) > (other.h + other.g)

    def __lt__(self, other):
        return (self.h + self.g) < (other.h + other.g)

    # def __eq__(self, other):
    #     return np.array_equiv(self.state, other.state)

    def print(self):
        space_max = len(str(self.size ** 2))
        i = 0
        for elem in self.state:
            if i % self.size == 0 and i != 0:
                print("")
            print( " " * (space_max - len(str(elem))) + str(elem) + " ", end="")
            i += 1
        print("")

    def get_move_function(self, move):
        if move == "mv_left":
            return {"mv_left": self.move_left}
        elif move == "mv_right":
            return {"mv_right": self.move_right}
        elif move == "mv_up":
            return {"mv_up": self.move_up}
        elif move == "mv_down":
            return {"mv_down": self.move_down}

    def get_state(self):
        return self.state

    # movements functions => retourner un nouveau state et l'affecter dans le main a puzzle.state
    # plutot que de mov direct et sauver dans move_function
    # get children a modifier aussi ensuite, pas besoin de backup
    def move_right(self):
        y = self.zero_position[0]
        x = self.zero_position[1]
        righter_value = self.state[y, x + 1]
        self.state[y, x + 1] = 0
        self.state[y, x] = righter_value
        return 0

    def move_left(self):
        y = self.zero_position[0]
        x = self.zero_position[1]
        lefter_value = self.state[y, x - 1]
        self.state[y, x - 1] = 0
        self.state[y, x] = lefter_value
        return 0

    def move_up(self):
        y = self.zero_position[0]
        x = self.zero_position[1]
        upper_value = self.state[y - 1, x]
        self.state[y - 1, x] = 0
        self.state[y, x] = upper_value

        return 0

    def move_down(self):
        y = self.zero_position[0]
        x = self.zero_position[1]
        lower_value = self.state[y + 1, x]
        self.state[y + 1, x] = 0
        self.state[y, x] = lower_value
        return 0

    def get_position(self, value):
        return int(np.where(self.state == value)[0]), int(np.where(self.state == value)[1])

    def get_available_moves(self, value):
        available_moves = []
        value_position = self.get_position(value)
        if self.debug == 1:
            print("value position  : ", value_position)
        if value_position[1] > 0:
            available_moves.append({'name': "mv_left", 'function': self.move_left})
        if value_position[1] < (self.size - 1):
            available_moves.append({'name': "mv_right", 'function': self.move_right})
        if value_position[0] > 0:
            available_moves.append({'name': "mv_up", 'function': self.move_up})
        if value_position[0] < (self.size - 1):
            available_moves.append({'name': "mv_down", 'function': self.move_down})
        return available_moves

    def get_solution(self):
        if self.size == 0:
            print("Puzzle size is 0. No solution can be found")
            exit(-1)
        solution = np.zeros((self.size, self.size), dtype=int)
        value_max = self.size ** 2
        value = 1
        x_max = y_max = self.size - 1
        x_min = y_min = 0
        while 1:
            x = x_min
            y = y_min
            while x < x_max:
                solution[y, x] = value
                x += 1
                y = y_min
                value += 1
            if value >= value_max:
                break
            while y < y_max:
                solution[y, x] = value
                y += 1
                value += 1
            if value >= value_max:
                break
            while x > x_min:
                solution[y, x] = value
                x -= 1
                value += 1
            if value >= value_max:
                break
            while y > y_min:
                solution[y, x] = value
                y -= 1
                value += 1
            x_min += 1
            y_min += 1
            y_max -= 1
            x_max -= 1
            if value >= value_max:
                break
        return solution

    def get_children(self):
        backup_state = self.state.copy()
        children_list = []
        availables_moves = self.get_available_moves(0)
        for move in availables_moves:
            # on deplace le 0 => self.state est affecte par le deplacement
            move['function']()
            # si pas de parent ou si le parent est different de l'etat courant on ajoute dans children list
            # if not self.parent or not np.array_equal(self.state, self.parent.state):
            if not self.parent or not (self.state==self.parent.state).all():
                children_list.append(self.state)
            self.state = backup_state.copy()
        return children_list
