import pygame, sys
import time

class Visu:

    grey = (124, 126, 130)
    white = (255, 255, 255)
    size_box = 100
    side_margin = 10
    header = 50
    footer = 25   
    puzzle_size = 0
    width_win = 0
    height_win = 0
    window_size = 0
    solutions = []
    box_list = []
    prev_state = 0
    done = False

    def __init__(self, puzzle):
        self.solutions = puzzle
        self.size = len(puzzle[0])
        self.puzzle_size = self.size_box * self.size
        self.width_win = self.puzzle_size + self.side_margin
        self.height_win = self.puzzle_size + self.header + self.footer
        self.window_size = [self.width_win, self.height_win]
        self.create_screen()
        self.init_puzzle()

    def init_puzzle(self):
        self.prev_state = self.solutions.pop(0)
        self.calc_puzzle(self.prev_state)
        self.draw_puzzle()

    def create_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width_win,self.height_win))
        pygame.display.set_caption("Npuzzle")
        clock = pygame.time.Clock()
        clock.tick(60)
    
    def draw_header(self):
        arialfont = pygame.font.Font(None, 22)
        text = arialfont.render('Algorithme: A* Star', True, (0, 0, 0))
        rect = text.get_rect(center=(self.width_win / 2, 10))
        self.screen.blit(text, rect)
        text = arialfont.render('Heuristic: Euclid', True, (0, 0, 0))
        rect = text.get_rect(center=(self.width_win / 2, 35))
        self.screen.blit(text, rect)

    def draw_footer(self):    
        arialfont = pygame.font.Font(None, 22)
        text = arialfont.render('Cpaquet & Srossi', True, (0, 0, 0))
        rect = text.get_rect(center=(self.width_win / 2, self.height_win - self.footer / 2))
        self.screen.blit(text, rect)

    def calc_puzzle(self, puzzle):
        for line in range(self.size):
            x = (line * self.size_box) + self.header
            for column in range(self.size):
                y = (column * self.size_box) + self.side_margin / 2
                value = str(puzzle[line][column])
                if (value != '0'):
                    box, box_rect, value = self.create_box(value, x, y)
                    self.append_box(box, box_rect, value)
            
    def create_box(self, value, x, y):
        box = pygame.Surface((self.size_box, self.size_box))
        box.fill(self.grey)
        box_rect = box.get_rect(topleft=(y, x))
        pygame.draw.rect(box, (255,255,255), box.get_rect(topleft=(0, 0)), 1)
        arialfont = pygame.font.Font(None, 40)
        text = arialfont.render(value, True, (255, 255, 255), self.grey)
        rect = text.get_rect(center=((self.size_box) / 2, (self.size_box) / 2))
        box.blit(text, rect)
        return box, box_rect, value

    def append_box(self, box, box_rect, value):
        self.box_list.append((box, box_rect, value))

    def draw_puzzle(self):
        self.screen.fill((255, 255, 255))
        for box,box_rect,value in self.box_list:
            self.screen.blit(box, box_rect)
        self.draw_header()
        self.draw_footer()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
    
    def move_box(self, value, line, column):
        x = (line * self.size_box) + self.header
        y = (column * self.size_box) + self.side_margin / 2
        new_box = self.create_box(str(value), x, y)
        for old_index in range(len(self.box_list)):
            if self.box_list[old_index][2] == str(value):
                break
        dist_line = new_box[1][0] - self.box_list[old_index][1][0]
        dist_col = new_box[1][1] - self.box_list[old_index][1][1]
        while self.box_list[old_index][1][1] != new_box[1][1] or self.box_list[old_index][1][0] != new_box[1][0]:
            old_box = self.box_list.pop(old_index)
            old_rect = old_box[1]
            old_rect = old_rect.move(dist_line / 25, dist_col / 25) 
            self.box_list.insert(old_index, (old_box[0], old_rect, old_box[2]))
            self.draw_puzzle()
        self.box_list = []
        self.calc_puzzle(self.prev_state)

    def find_move(self, new_state):
        for line in range(self.size):
            for column in range(self.size):
                prev_value = self.prev_state[line][column]
                new_value = new_state[line][column]
                if  new_value != 0 and prev_value != new_value:
                    self.prev_state = new_state
                    return new_value, line, column
        return False    

    def display(self):
        while not self.done:
            for state in self.solutions:
                value, line, column = self.find_move(state)
                self.move_box(value, line, column)
            self.solutions = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
        pygame.quit()

npuzzle1 = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
npuzzle2 = [[0, 8, 2], [1, 4, 3], [7, 6, 5]]
npuzzle3 = [[8, 0, 2], [1, 4, 3], [7, 6, 5]]
npuzzle4 = [[8, 4, 2], [1, 0, 3], [7, 6, 5]]
if __name__ == "__main__":
    
    liste = []
    liste.append(npuzzle1)
    liste.append(npuzzle2)
    liste.append(npuzzle3)
    liste.append(npuzzle4)
    Visu(liste).display()
    # pour le mouvement, mettre la box du chiffre a zero pour l'effacer et commencer a la redessiner petit a petit pour la faire avancer
    # Attention il ne faut plus faire la margin