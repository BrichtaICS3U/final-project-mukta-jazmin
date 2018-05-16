import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Treasure(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        
        self.image=pygame.image.load('images.png').convert()
        #self.image.set_colorkey(BLACK)
        self.image=pygame.transform.scale(self.image,(width,height))

        self.width = width
        self.height = height

        self.rect = self.image.get_rect()

      #  self.rect.center = pos
