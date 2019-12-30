import fileinput
import numpy as np
import math as math


#puzzle = np.array([13,2,10,3,1,12,8,4,5,0,9,6,15,14,11,7])
#zero_position = 10
#puzzle = np.array([6,13,7,10,8,9,11,0,15,2,12,5,14,3,1,4])
#zero_position = 8
#puzzle = np.array([3,9,1,15,14,11,4,6,13,0,10,12,2,7,8,5])
#zero_position = 10

class solvable:

    puzzle = 0
    size = 0
    zero_position = 0

    def __init__(self, puzzle):
        self.zero_position = puzzle.zero_position
        self.puzzle = puzzle.state
        self.size = puzzle.size

    # Compte le nombre d'inversions pour trier le tableau (eg. [2,3,1] = 2)
    def count_inversion(self):
        inversion = 0
        index = 0
        index_next = 0
        while index < len(self.puzzle) - 1:
            if self.puzzle[index + 1] == 0:
                index_next = index + 2
            else:
                index_next = index + 1
            if self.puzzle[index] > self.puzzle[index_next]:
                inversion += 1
                self.puzzle[index], self.puzzle[index_next] = self.puzzle [index_next], self.puzzle[index]
                index = 0
            else:
                index += 1
        return inversion % 2

    # Vérifie la position de X sur une ligne pair ou impair en partant de la dernière ligne
    def check_zero_position(self):
        #position = (self.size - self.zero_position + 1)
        #if position % math.sqrt(size) == 0 :
        #    line = position // math.sqrt(size)
        #else :
        #    line = position // math.sqrt(size) + 1
        #return line % 2
        return (self.zero_position[1] + 1 % 2)

    # Vérifie si le tableau est pair ou impair et les conditions associées (position de X et nbre d'inversions)
    def check_if_solvable(self):
        if (self.size % 2 == 1) and self.count_inversion() == 0 :
            return True
        elif (self.size % 2 == 0) and self.count_inversion() != self.check_zero_position() :
            return True
        return False