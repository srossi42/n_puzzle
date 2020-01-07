import fileinput
import numpy as np
import math as math

class Solvable:

    def __init__(self, puzzle):
        self.size = puzzle.size

        self.puzzle = np.reshape(puzzle.state, self.size * self.size)
        self.model = np.reshape(puzzle.get_solution(), self.size * self.size)

        self.zero_position = np.where(self.puzzle == 0)[0]
        self.size_parity = math.ceil(self.size / 2) % 2
        self.zero_parity = self.find_zero_parity()
        self.inversion_parity = self.find_inversion_parity()

        self.sovable = self.find_solvablility()
        print("size parity:", self.size_parity, "   zero parity:", self.zero_parity, "   inversion_parity", self.inversion_parity, "     Solvable:", self.sovable)

    # Compte le nombre d'inversions pour trier le tableau (eg. [2,3,1] = 2)
    def find_inversion_parity(self):
        puzzle = self.puzzle
        inversion = 0
        for index in range(len(self.model)):
            index_swap = np.where(puzzle == self.model[index])[0]
            while index_swap > index:
                puzzle[index_swap], puzzle[index_swap - 1] = puzzle[index_swap - 1], puzzle[index_swap]
                index_swap -= 1
                inversion += 1
        print("inversion", inversion)
        return inversion % 2

    # Vérifie la position de X sur une ligne pair ou impair en partant de la dernière ligne
    def find_zero_parity(self):
        print("milieu", math.ceil(self.size / 2))
        print ("zero position",  math.ceil((self.zero_position + 1) / self.size))
        return (math.ceil(self.size / 2) -  math.ceil((self.zero_position + 1) / self.size)) % 2

    # Vérifie si le tableau est pair ou impair et les conditions associées (position de X et nbre d'inversions)
    def find_solvablility(self):
        if self.size_parity == 1 and self.inversion_parity == 0 :
            return True
        elif self.size_parity == 0 and self.inversion_parity != self.zero_parity :
            return True
        return False