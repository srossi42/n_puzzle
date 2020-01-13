import pygame, sys
import time
from os import path
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
    step_to_solution = []
    solution = 0
    box_bg_list = []
    box_coord_list = []
    prev_state = 0
    done = False
    img = 0
    flag = 0
    path_img = 0

    def __init__(self, step_to_solution, solution, flag, path_img):
        self.solution = solution
        self.step_to_solution = step_to_solution
        self.size = len(solution)
        self.box_bg_list = [0] * (self.size * self.size)
        self.box_coord_list = [0] * (self.size * self.size)
        self.puzzle_size = self.size_box * self.size
        self.width_win = self.puzzle_size + self.side_margin
        self.height_win = self.puzzle_size + self.header + self.footer
        self.window_size = [self.width_win, self.height_win]
        self.flag = flag
        self.path_img = path_img
        self.create_screen()
        self.load_img()

    def load_img(self):
        if path.exists(self.path_img):
            self.img = pygame.image.load(self.path_img)
            if self.img:
                self.img = pygame.transform.scale(self.img, (self.puzzle_size, self.puzzle_size))
        else:
            print("Oops!  nous n'avons pas pu ouvrir l'image choisie... :")

    def gen_img_bg(self):
        for line in range(self.size):
            x = line * self.size_box
            for column in range(self.size):
                y = column * self.size_box
                value = self.solution[line][column]
                bg = pygame.Surface((self.size_box, self.size_box))
                bg.blit(self.img , (0,0), (y,x,100,100))
                self.box_bg_list[value] = bg

    def gen_nbr_bg(self):
        for value in range(self.size * self.size):
            bg = pygame.Surface((self.size_box, self.size_box))
            bg.fill(self.grey)
            pygame.draw.rect(bg, (255,255,255), bg.get_rect(topleft=(0, 0)), 1)
            arialfont = pygame.font.Font(None, 40)
            text = arialfont.render(str(value), True, (255, 255, 255), self.grey)
            rect = text.get_rect(center=((self.size_box) / 2, (self.size_box) / 2))
            bg.blit(text, rect)
            self.box_bg_list[value] = bg

    def calc_coord(self, puzzle):
        for column in range(self.size):
            x = (column * self.size_box) + self.side_margin / 2
            for line in range(self.size):
                y = (line * self.size_box) + self.header
                value = puzzle[line][column]
                coord = pygame.Rect((x,y), (self.size_box, self.size_box))
                self.box_coord_list[value] = coord

    def draw_puzzle(self):
        self.screen.fill((255, 255, 255))
        for value in range(self.size * self.size):
            self.screen.blit(self.box_bg_list[value], self.box_coord_list[value])
        self.draw_header()
        self.draw_footer()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
    
    def find_change(self, new_state):
        value = 0
        for line in range(self.size):
            for column in range(self.size):
                prev_value = self.prev_state[line][column]
                new_value = new_state[line][column]
                if  new_value != 0 and prev_value != new_value:
                    new_line = line
                    new_col = column
                    value = new_value
                if new_value == 0:
                    old_line = line
                    old_col = column
        move_vert = new_line - old_line
        move_hor = new_col - old_col
        self.prev_state = new_state
        return value, move_vert, move_hor

    def move(self, value, move_vert, move_hor):
        speed = 4
        count = 0
        while count < self.size_box :
            self.box_coord_list[0] = self.box_coord_list[0].move(-move_hor * speed, -move_vert * speed)
            self.box_coord_list[value] = self.box_coord_list[value].move(move_hor * speed, move_vert * speed)
            count = count + speed 
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

    def display(self):
        if self.flag == 1 and self.img:
            self.gen_img_bg()
        else:
            self.gen_nbr_bg()
        while not self.done:
            for state in self.step_to_solution:
                if self.prev_state == 0:
                    self.calc_coord(state)
                    self.draw_puzzle()
                    self.prev_state = state
                else:
                    change, move_vert, move_hor = self.find_change(state)
                    self.move(change, move_vert, move_hor)
            self.step_to_solution = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
        pygame.quit()



npuzzle1 = [[0, 1, 2], [8, 4, 3], [7, 6, 5]]
npuzzle2 = [[1, 0, 2], [8, 4, 3], [7, 6, 5]]
npuzzle3 = [[1, 2, 0], [8, 4, 3], [7, 6, 5]]
npuzzle4 = [[1, 2, 3], [8, 4, 0], [7, 6, 5]]
npuzzle5 = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
solution = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
if __name__ == "__main__":
    
    liste = []
    liste.append(npuzzle1)
    liste.append(npuzzle2)
    liste.append(npuzzle3)
    liste.append(npuzzle4)
    liste.append(npuzzle5)
    #liste.append(solution)
    Visu(liste, solution, 0, "./meme.jpg").display()