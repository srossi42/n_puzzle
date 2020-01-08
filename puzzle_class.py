import numpy as np


class Puzzle:
    state = None
    g = 0
    h = 0
    parent = None
    size = 0
    zero_position = None
    zero_solution_position = None

    def __init__(self, parent=None):
        if parent:
            self.parent = parent
            self.g = parent.g + 1
            self.size = parent.size
            self.zero_solution_position = parent.zero_solution_position

    def __gt__(self, other):
        return (self.h + self.g) > (other.h + other.g)

    def __lt__(self, other):
        return (self.h + self.g) < (other.h + other.g)

    def print(self):
        space_max = len(str(self.size ** 2))
        i = 0
        for elem in self.state:
            for el in elem:
                if i % self.size == 0 and i != 0:
                    print("")
                print(" " * (space_max - len(str(el))) + str(el) + " ", end="")
                i += 1
        print("\n")

    def get_move_function(self, move):
        if move == "mv_left":
            return {'name': "mv_left", 'function': self.move_left}
        elif move == "mv_right":
            return {'name': "mv_right", 'function': self.move_right}
        elif move == "mv_up":
            return {'name': "mv_up", 'function': self.move_up}
        elif move == "mv_down":
            return {'name': "mv_down", 'function': self.move_down}

    def get_state(self):
        return self.state

    # movements functions => retourner un nouveau state et l'affecter dans le main a puzzle.state
    # plutot que de mov direct et sauver dans move_function
    # get children a modifier aussi ensuite, pas besoin de backup
    def move_right(self, opt=False):
        y = self.zero_position[0]
        x = self.zero_position[1]
        righter_value = self.state[y, x + 1]
        self.state[y, x + 1] = 0
        self.state[y, x] = righter_value
        if not opt:
            self.zero_position = (y, x + 1)

    def move_left(self, opt=False):
        y = self.zero_position[0]
        x = self.zero_position[1]
        lefter_value = self.state[y, x - 1]
        self.state[y, x - 1] = 0
        self.state[y, x] = lefter_value
        if not opt:
            self.zero_position = (y, x - 1)

    def move_up(self, opt=False):
        y = self.zero_position[0]
        x = self.zero_position[1]
        upper_value = self.state[y - 1, x]
        self.state[y - 1, x] = 0
        self.state[y, x] = upper_value
        if not opt:
            self.zero_position = (y - 1, x)

    def move_down(self, opt=False):
        y = self.zero_position[0]
        x = self.zero_position[1]
        lower_value = self.state[y + 1, x]
        self.state[y + 1, x] = 0
        self.state[y, x] = lower_value
        if not opt:
            self.zero_position = (y + 1, x)

    def get_position(self, value):
        position = np.where(self.state == value)
        return int(position[0]), int(position[1])

    def get_available_moves(self, value):
        available_moves = []
        value_position = self.get_position(value)
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
            raise Exception("Puzzle size is 0. No solution can be found")
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
            move['function'](True)
            # si pas de parent ou si le parent est different de l'etat courant on ajoute dans children list
            # if not self.parent or not np.array_equal(self.state, self.parent.state):
            if not self.parent or not (self.state == self.parent.state).all():
                children_list.append(self.state)
            self.state = backup_state.copy()
        return children_list
