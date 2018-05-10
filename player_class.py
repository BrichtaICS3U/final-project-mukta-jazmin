import pygame
WHITE = (255, 255, 255)

class player(pygame.sprite.Sprite):

    def __init__(self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.rect(self.image, self.color, [0,0,self.width,self.height])

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self,pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed*speed/10

    def moveBackward(self,speed):
        self.rect.y -= self.speed*speed/10

    def changeSpeed(self,speed):
        self.speed = speed

    
