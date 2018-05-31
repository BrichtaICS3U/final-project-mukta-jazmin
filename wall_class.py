import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREENWIDTH = 1200
SCREENHEIGHT = 800

class wall(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(WHITE)

        self.color = color
        self.width = width
        self.height = height

        pygame.draw.rect(self.image, color, [0,0, self.width,self.height])

        self.rect = self.image.get_rect()
