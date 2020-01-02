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
        if verbose:
            self.verbose = verbose
        if debug:
            self.debug = debug
        self.sys = sys

    def print(self):
        space_max = len(str(self.size ** 2))
        i = 0
        for elem in self.state:
            if (i % self.size == 0 and i != 0):
                print("")
            print( " " * (space_max - len(str(elem))) + str(elem) + " ", end="")
            i += 1
        print("")

    def get_move_function(self, move):
        if move == "mv_left":
            return {"mv_left": self.move_left}
        if move == "mv_right":
            return {"mv_right": self.move_right}
        if move == "mv_up":
            return {"mv_up": self.move_up}
        if move == "mv_down":
            return {"mv_down": self.move_down}

    def get_state(self):
        return self.state

    # movements functions => retourner un nouveau state et l'affecter dans le main a puzzle.state
    # plutot que de mov direct et sauver dans move_function
    # get children a modifier aussi ensuite, pas besoin de backup
    def move_right(self, value):
        if self.debug == 1:
            print("move right ", value)
        position_value = self.get_position(value)
        y = position_value[0]
        x = position_value[1]
        if x >= (self.size - 1):
            if self.debug == 1:
                print("Error: can't move right: value position = [" + str(x) + ";" + str(y) + "]" )
                print(self.state)
            return -1
        righter_value = self.state[y, x + 1]
        self.state[y, x + 1] = value
        self.state[y, x] = righter_value
        if self.verbose == 1:
            time.sleep(self.tempo)
            if self.sys == 'unix':
                os.system("clear")
            else:
                os.system("cls")
            print(self.state)
        return 0

    def move_left(self, value):
        if self.debug == 1:
            print("move left ", value)
        position_value = self.get_position(value)
        y = position_value[0]
        x = position_value[1]
        if x <= 0:
            if self.debug == 1:
                print("Error: can't move left: value position = [" + str(x) + ";" + str(y) + "]" )
                print(self.state)
            return -1
        lefter_value = self.state[y, x - 1]
        self.state[y, x - 1] = value
        self.state[y, x] = lefter_value
        if self.verbose == 1:
            time.sleep(self.tempo)
            if self.os == 'unix':
                os.system("clear")
            else:
                os.system("cls")
            print(self.state)
        return 0

    def move_up(self, value):
        if self.debug == 1:
            print("move up ", value)
        position_value = self.get_position(value)
        y = position_value[0]
        x = position_value[1]
        if y <= 0:
            if self.debug == 1:
                print("Error: can't move up: value position = [" + str(x) + ";" + str(y) + "]" )
                print(self.state)
            return -1
        upper_value = self.state[y - 1, x]
        self.state[y - 1, x] = value
        self.state[y, x] = upper_value
        if self.verbose == 1:
            time.sleep(self.tempo)
            if self.os == 'unix':
                os.system("clear")
            else:
                os.system("cls")
            print(self.state)
        return 0

    def move_down(self, value):
        if self.debug == 1:
            print("move down ", value)
        position_value = self.get_position(value)
        y = position_value[0]
        x = position_value[1]
        if y >= (self.size - 1):
            if self.debug == 1:
                print("Error: can't move down: value position = [" + str(x) + ";" + str(y) + "]" )
                print(self.state)
            return -1
        lower_value = self.state[y + 1, x]
        self.state[y + 1, x] = value
        self.state[y, x] = lower_value
        if self.verbose == 1:
            time.sleep(self.tempo)
            if self.os == 'unix':
                os.system("clear")
            else:
                os.system("cls")
            print(self.state)
        return 0

    def get_position(self, value):
        if self.state is None:
            print("Error: puzzle state does not exist")
            return -1
        if self.debug == 1:
            print("value in get position : ", value)
            print("self.state :" , self.state)
        y = int(np.where(self.state == value)[0])
        x = int(np.where(self.state == value)[1])
        return y, x

    def get_available_moves(self, value):
        available_moves = []
        value_position = self.get_position(value)
        # print("value : ", value)
        # print("position : ", value_position)
        # print("self.size : ", self.size)
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
        # print("self size : ", self.size)
        if self.size == 0:
            print("Puzzle size is 0. No solution can be found")
            exit(-1)
        solution = np.zeros((self.size, self.size), dtype=int)
        #solution = [0] * (size*size)
        value_max = self.size ** 2
        value = 1
        x_max = y_max = self.size - 1
        x_min = y_min = 0
        #print("max value : ", value_max)
        while 1:
            x = x_min
            y = y_min
            while x < x_max:
                #print("value : ", value)
                #print(str(x) + ", " + str(y))
                solution[y, x] = value
                x += 1
                y = y_min
                #print("solution : ", solution)
                value += 1
            if value >= value_max:
                break
            while y < y_max:
                #print(value)
                #print(str(x) + ", " + str(y))
                solution[y, x] = value
                y += 1
               # print("solution : ", solution)
                value += 1
            if value >= value_max:
                break
            while x > x_min:
                #print(value)
                #print(str(x) + ", " + str(y))
                solution[y, x] = value
                x -= 1
                #print("solution : ", solution)
                value += 1
            if value >= value_max:
                break
            while y > y_min:
                #print(value)
                #print(str(x) + ", " + str(y))
                solution[y, x] = value
                y -= 1
                #print("solution : ", solution)
                value += 1
            x_min += 1
            y_min += 1
            y_max -= 1
            x_max -= 1
            if value >= value_max:
                break
        #print(str(x) + ", " + str(y))
        #print("----")
        #print(str(x_min) + ", " + str(y_min))
        #print(str(x_max) + ", " + str(y_max))
        #print("soution : ", solution)
        return solution

    def get_children(self):
        # print("get_children function")
        backup_state = self.state.copy()
        children_list = []
        availables_moves = self.get_available_moves(0)
        # print("availables_moves dans get children: ")
        # for move in availables_moves:
        #     print(move['name'])
        for move in availables_moves:
            # on deplace le 0 => self.state est affecte par le deplacement
            move['function'](0)
            # si pas de parent ou si le parent est different de l'etat courant on ajoute child
            if not self.parent or not np.array_equal(self.state, self.parent.state):
                # print("Adding child")
                children_list.append(self.state)
            self.state = backup_state.copy()
        return children_list