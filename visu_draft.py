import pygame, sys

class display: 
    size = 6
    COLOR = (124, 126, 130)

    # A supprimer si utilisation image
    WIDTH_CASE = 50
    HEIGHT_CASE = 50

    HEADER = 50
    FOOTER = 50
    SIDE_MARGIN = 100
    PUZZLE_SIZE = 50 * size
    WIDTH_WIN = PUZZLE_SIZE + SIDE_MARGIN
    HEIGHT_WIN = PUZZLE_SIZE + HEADER + FOOTER
    WINDOW_SIZE = [WIDTH_WIN, HEIGHT_WIN]
    MARGIN = 1
    done = False
    # Used to manage how fast the screen updates


    def __init__(self, parent=None, verbose=False, debug=False, sys="unix"):
        

    # Create grid
    #grid = []
    #for row in range(10):
    #    grid.append([])
    #    for column in range(10):
    #        grid[row].append(0)

    def create_screen(self):
        pygame.display.set_mode((500, 400), 0, 32)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Npuzzle")
        self.screen.fill(self.COLOR)

    def draw_header(self):
        arialfont = pygame.font.Font(None, 18)
        text = arialfont.render('Algorithme: A* Star', True, (255, 255, 255))
        rect = text.get_rect(center=(self.WIDTH_WIN / 2, 10))
        self.screen.blit(text, rect)
        text = arialfont.render('Heuristic: Euclid', True, (255, 255, 255))
        rect = text.get_rect(center=(self.WIDTH_WIN / 2, 30))
        self.screen.blit(text, rect)

    def draw_footer(self):    
        arialfont = pygame.font.Font(None, 18)
        text = arialfont.render('Cpaquet & Srossi', True, (255, 255, 255))
        rect = text.get_rect(center=(self.WIDTH_WIN / 2, self.HEIGHT_WIN - self.FOOTER / 2))
        self.screen.blit(text, rect)
 
    def load_image(self):
        self.img = pygame.image.load("./img.png")
        pygame.transform.scale(self.img, (self.PUZZLE_SIZE, self.PUZZLE_SIZE))

    def draw_case(self):
        source_area = pygame.Rect((0,0), (self.PUZZLE_SIZE, self.PUZZLE_SIZE))
        self.screen.blit(self.img, (0,0), source_area)

    def loop(self):
        windowSurface = pygame.display.set_mode((500, 400), 0, 32)
        pygame.init()
        clock = pygame.time.Clock()
        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True 
        clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.time.wait(1000)
        pygame.display.flip()


    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            #elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                #pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                #column = pos[0] // (WIDTH_CASE + MARGIN)
                #row = pos[1] // (HEIGHT_CASE + MARGIN)
                # Set that location to one
                #grid[row][column] = 1
                #print("Click ", pos, "Grid coordinates: ", row, column)

        #Draw the grid
        #for row in range(size):
        #    for column in range(size):
        #        color = WHITE
        #        if grid[row][column] == 1:
        #            color = GREEN
        #        pygame.draw.rect(screen,
        #                         color,
        #                         [(MARGIN + WIDTH_CASE) * column + MARGIN + 50,
        #                          (MARGIN + HEIGHT_CASE) * row + MARGIN + HEADER,
        #                          WIDTH_CASE,
        #                          HEIGHT_CASE])
    
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.time.wait(1000)
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

    def main():
        draw_header()
        draw_footer()
        draw_case(screen, img)

    # pour le mouvement, mettre la case du chiffre a zero pour l'effacer et commencer a la redessiner petit a petit pour la faire avancer
    # Attention il ne faut plus faire la margin