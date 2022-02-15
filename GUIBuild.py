# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Constants for H/W
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Grid(pygame.sprite.Sprite):
    def __init__(self):
        super(Grid, self).__init__()
        self.surf = pygame.Surface((400, 10))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(-30, 30)



# Initialize pygame
pygame.init()

line_color = (0, 0, 0)
def draw():
    pygame.draw.line(screen, line_color, (SCREEN_WIDTH / 3, 0), (SCREEN_WIDTH / 3, SCREEN_HEIGHT), 7)
    pygame.draw.line(screen, line_color, (SCREEN_WIDTH / 3 * 2, 0), (SCREEN_WIDTH / 3 * 2, SCREEN_HEIGHT), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, line_color, (0, SCREEN_HEIGHT / 3), (SCREEN_WIDTH, SCREEN_HEIGHT / 3), 7)
    pygame.draw.line(screen, line_color, (0, SCREEN_HEIGHT / 3 * 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 3 * 2), 7)

# myfont = pygame.font.SysFont('Comic Sans MS', 30)

# textsurface = myfont.render('Some Text', False, (0, 0, 0))


# Create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player
# grid = Grid()

# main
running = True
draw()
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    # fill BG w/ white
    screen.fill((255, 255, 255))

    # draw grid
    screen.blit(grid.surf, grid.rect)
    
    # screen.blit(textsurface, (0, 0))
    
    # update display
    pygame.display.flip()
    
