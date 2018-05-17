import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class exitDoor(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.image=pygame.image.load('Trap_Door_open.png').convert()
        self.image=pygame.transform.scale(self.image,(width,height))
        self.image.set_colorkey(BLACK)

        self.width = width
        self.height = height

        self.rect = self.image.get_rect()

      
