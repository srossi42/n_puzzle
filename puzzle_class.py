import numpy as np

class Puzzle:

    state = None
    g = 0
    h = 0
    parent = None
    size = 0
 #   moves = ["move_up", "move_down", "move_left", "move_right"]

    def __init__(self, parent=None):
        if parent:
            self.parent = parent
            self.g = parent.g + 1
    def print (self):
        i = 0
        for elem in self.state:
            if (i % self.size == 0 and i != 0):
                print("")
            print(elem + " ", end="")
            i += 1
        print("")

    def move(self, value, direction):
        index_value = np.where(self.state == value)[0][0]
        position_value = self.get_position(value)
        x = position_value[0]
        y = position_value[1]
        if direction == "up":
            print(direction)
        elif direction == "down":
            print(direction)
        elif direction == "left":
            print(direction)
        elif direction == "right":
            print(direction)
        else:
            print("Error, wrong direction:", direction)
            return -1
        return 1

    def move_right(self, value):
        print("move right ", value)
        index_value = np.where(self.state == value)[0][0]
        position_value = self.get_position(value)
        x = position_value[0]
        y = position_value[1]
        if x >= (self.size - 1):
            print("Error: can't move right: value position = [" + str(x) + ";" + str(y) + "]" )
            return -1
        righter_value = self.state[index_value + 1]
        self.state[index_value + 1] = value
        self.state[index_value] = righter_value
        return 0

    def move_left(self, value):
        print("move left ", value)
        index_value = np.where(self.state == value)[0][0]
        position_value = self.get_position(value)
        x = position_value[0]
        y = position_value[1]
        if x <= 0:
            print("Error: can't move left: value position = [" + str(x) + ";" + str(y) + "]" )
            return -1
        lefter_value = self.state[index_value - 1]
        self.state[index_value - 1] = value
        self.state[index_value] = lefter_value
        return 0

    def move_up(self, value):
        print("move up ", value)
        index_value = np.where(self.state == value)[0][0]
        position_value = self.get_position(value)
        x = position_value[0]
        y = position_value[1]
        if y == 0:
            print("Error: can't move up: value position = [" + str(x) + ";" + str(y) + "]" )
            return -1
        upper_value = self.state[index_value - self.size]
        self.state[index_value - self.size] = value
        self.state[index_value] = upper_value
        return 0

    def move_down(self, value):
        print("move down ", value)
        index_value = np.where(self.state == value)[0][0]
        position_value = self.get_position(value)
        x = position_value[0]
        y = position_value[1]
        if y == (self.size - 1):
            print("Error: can't move down: value position = [" + str(x) + ";" + str(y) + "]" )
            return -1
        lower_value = self.state[index_value + self.size]
        self.state[index_value + self.size] = value
        self.state[index_value] = lower_value
        return 0

    def get_position(self, value):
        x = int(np.trunc(np.where(self.state == value)[0][0] % self.size))
        y = int(np.trunc(np.where(self.state == value)[0][0] / self.size))
        return x, y

    def get_available_moves(self):
        available_moves = []
        blank_position = self.get_position(0)
        if blank_position[0] > 0:
            available_moves.append({"mv_left": self.move_left})
        if blank_position[0] < (self.size - 1):
            available_moves.append({"mv_right": self.move_right})
        if blank_position[1] > 0:
            available_moves.append({"mv_up": self.move_up})
        if blank_position[1] < (self.size - 1):
            available_moves.append({"mv_down": self.move_down})
        return available_moves

# A STAR ALGO

    def get_solution(self):
        return 1