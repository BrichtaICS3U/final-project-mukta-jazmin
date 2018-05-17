import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class exitDoor(pygame.sprite.Sprite):
    def__init__(self,width,height):
        super().__init__()

        self.image=pygame.image.load('Trap_Door_open.png').convert()
