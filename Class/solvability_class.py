import numpy as np
import math as math


class Solvability:
    def __init__(self, puzzle):
        backup_state = puzzle.state.copy()
        self.size = puzzle.size
        self.puzzle = np.reshape(puzzle.state, self.size * self.size)
        self.model = np.reshape(puzzle.get_solution(), self.size * self.size)
        if np.array_equal(self.puzzle, self.model):
            print("Puzzle:")
            puzzle.print()
            raise Exception("Puzzle already solved... Nice try!")
        self.zero_parity = self.find_zero_parity()
        self.inversion_parity = self.find_inversion_parity()
        self.solvable = self.zero_parity == self.inversion_parity
        if not self.solvable:
            raise Exception("Puzzle isn't solvable:   Zero parity: " + str(self.zero_parity) + "   Inversion parity: "
                            + str(self.inversion_parity))
        else:
            puzzle.state = backup_state.copy()

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
        return inversion % 2

    # Vérifie la position de X sur une ligne pair ou impair en partant de la dernière ligne
    def find_zero_parity(self):
        zero_current_position = np.where(self.puzzle == 0)[0] + 1
        zero_model_position = np.where(self.model == 0)[0] + 1
        zero_current_line = math.ceil(zero_current_position / self.size)
        zero_model_line = math.ceil(zero_model_position / self.size)
        if zero_current_position % self.size == 0:
            zero_current_col = self.size
        else :
            zero_current_col = zero_current_position % self.size
        zero_model_col = math.fabs(zero_model_position % self.size)
        move_column = math.fabs(zero_model_col - zero_current_col)
        move_line = math.fabs(zero_model_line - zero_current_line)
        return (move_column + move_line) % 2
