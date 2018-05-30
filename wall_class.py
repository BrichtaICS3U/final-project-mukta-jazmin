import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREENWIDTH = 1200
SCREENHEIGHT = 800

class wall(pygame.sprite.Sprite):
    def __init__(self, color, start_pos, end_pos, width):
        super().__init__()

        self.width = 1
        start_pos = (SCREENWIDTH/3, 0)
        end_pos = (SCREENWIDTH/3, SCREENHEIGHT/2)
        self.color = BLACK

        self.rect = self.image.get_rect()
