import pygame, sys

class Visu:

    color_grey = (124, 126, 130)
    size_box = 100
    side_margin = 10
    header = 50
    footer = 25   
    puzzle_size = 0
    width_win = 0
    height_win = 0
    window_size = 0
    box_list = []
    new_box_list = []
    done = False

    def __init__(self, puzzle):
        self.puzzle = puzzle.state
        self.size = puzzle.size
        self.puzzle_size = self.size_box * self.size
        self.width_win = self.puzzle_size + self.side_margin
        self.height_win = self.puzzle_size + self.header + self.footer
        self.window_size = [self.width_win, self.height_win]

    def init_puzzle(self):
        self.create_screen()
        self.draw_header()
        self.draw_footer()
        self.box_list = self.calc_puzzle(self.puzzle)
        self.draw_puzzle()

    def create_screen(self):
        #windowSurface = pygame.display.set_mode((500, 400), 0, 32)
        pygame.init()
        pygame.display.set_mode((self.width_win,self.height_win))
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Npuzzle")
        self.screen.fill((255, 255, 255))
        clock = pygame.time.Clock()
        clock.tick(60)
    
    def draw_header(self):
        arialfont = pygame.font.Font(None, 18)
        text = arialfont.render('Algorithme: A* Star', True, (0, 0, 0))
        rect = text.get_rect(center=(self.width_win / 2, 10))

        self.screen.blit(text, rect)
        text = arialfont.render('Heuristic: Euclid', True, (0, 0, 0))
        rect = text.get_rect(center=(self.width_win / 2, 30))
        self.screen.blit(text, rect)

    def draw_footer(self):    
        arialfont = pygame.font.Font(None, 18)
        text = arialfont.render('Cpaquet & Srossi', True, (0, 0, 0))
        rect = text.get_rect(center=(self.width_win / 2, self.height_win - self.footer / 2))
        self.screen.blit(text, rect)


    def calc_puzzle(self, puzzle):
        box_list = []
        for line in range(self.size):
            x = (line * self.size_box) + self.header
            for column in range(self.size):
                y = (column * self.size_box) + self.side_margin / 2
                value = str(puzzle[line][column])
                if (value != '0'):
                    self.create_append_box(box_list, value, x, y)
        return box_list
            
    
    def create_append_box(self, box_list, value, x, y):
        box = pygame.Surface((self.size_box, self.size_box))
        box.fill(self.color_grey)
        box_rect = box.get_rect(topleft=(y, x))
        pygame.draw.rect(box, (255,255,255), box.get_rect(topleft=(0, 0)), 1)
        arialfont = pygame.font.Font(None, 40)
        text = arialfont.render(value, True, (255, 255, 255), self.color_grey)
        rect = text.get_rect(center=((self.size_box) / 2, (self.size_box) / 2))
        box.blit(text, rect)
        box_list.append((box, box_rect, value))

    def draw_puzzle(self):
        for box,box_rect,value in self.box_list:
            self.screen.blit(box, box_rect)
        pygame.display.update()

    def move_box(self, index):
        #old_box, new_box = self.find_move()
        actual_box = self.box_list.pop(index)
        old_rect = actual_box[1]
        new_rect = old_rect.move(0, 6)
        self.box_list.insert(index, (actual_box[0], new_rect, actual_box[2]))
        self.draw_puzzle()

    #def find_move(self):
    #    for new_box in self.new_box_list:
    #        for old_box in self.box_list:
    #            if (new_box[2] == old_box[2] and new_box[1] != old_box[1]):
    #                return old_box, new_box
    #    return False

    def display(self):
        self.init_puzzle()
        while not self.done:
            #for move in solution:
            #    self.new_box_list = self.calc_puzzle(move)
            #    self.find_move()
            #    self.move_box()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True 
            self.move_box(1)
        pygame.quit()
        quit()

npuzzle1 = [[1 8 2], [0 4 3], [7 6 5]]
npuzzle2 = [[8 1 2], [0 4 3], [7 6 5]]

if __name__ == "__main__":
    
    liste = []
    liste.append(npuzzle1)
    liste.append(npuzzle2)
    Visu(liste).display()
    # pour le mouvement, mettre la box du chiffre a zero pour l'effacer et commencer a la redessiner petit a petit pour la faire avancer
    # Attention il ne faut plus faire la margin