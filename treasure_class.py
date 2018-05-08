import pygame
WHITE = (255, 255, 255)

class Treasure(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        self.image = pygame.Surface([20, 20])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos
