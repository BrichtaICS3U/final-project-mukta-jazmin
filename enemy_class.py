import pygame, random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class enemy(pygame.sprite.Sprite):
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

    def moveForward(self, speed):
        self.rect.y += self.speed*speed/20

    def moveBackward(self,speed):
        self.rect.y -= self.speed*speed/20

    def changeSpeed(self,speed):
        self.speed = speed

    def update(self):
        self.rect.x = self.rect.x + random.randint(-1, 1)*self.speed
        if  self.rect.x < 500-100:
            self.rect.x=500-100
        elif self.rect.x > 500+100:
            self.rect.x=500+100
            
        self.rect.y = self.rect.y + random.randint(-1, 1)*self.speed
        if  self.rect.y < 500-100:
            self.rect.y=500-100
        elif self.rect.y > 500+100:
            self.rect.y=500+100
        
