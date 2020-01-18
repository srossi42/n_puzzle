import random
from Class.puzzle_class import Puzzle


class Generator:
    puzzle = None
    nb_moves = 0
    last_move = None

    def __init__(self, size, nb_moves):
        self.puzzle = Puzzle()
        self.puzzle.size = size
        self.nb_moves = nb_moves

    def opposite_move(self, last_move_name):
        if last_move_name == 'mv_down':
            return "mv_up"
        elif last_move_name == 'mv_up':
            return "mv_down"
        elif last_move_name == 'mv_right':
            return "mv_left"
        elif last_move_name == 'mv_left':
            return "mv_right"

    def shuffle(self):
        for i in range(0, self.nb_moves):
            availables_moves = self.puzzle.get_available_moves(0)
            if self.last_move is not None:
                opposite_move_name = self.opposite_move(self.last_move['name'])
                opposite_move = self.puzzle.get_move_function(opposite_move_name)
                if opposite_move in availables_moves:
                    availables_moves.remove(opposite_move)
            random_move = random.choice(availables_moves)
            random_move['function']()
            self.puzzle.zero_position = self.puzzle.get_position(0)
            self.last_move = random_move
        return self.puzzle

    def generate_puzzle(self):
        solved_puzzle = self.puzzle.get_solution()
        self.puzzle.state = solved_puzzle
        self.puzzle.zero_position = self.puzzle.get_position(0)
        shuffled_puzzle = self.shuffle()
        return (shuffled_puzzle)