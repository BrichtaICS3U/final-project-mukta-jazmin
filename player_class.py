import pygame
WHITE = (255, 255, 255)
BLACK = (0,0,0)

SCREENWIDTH = 0
SCREENHEIGHT = 0

class player(pygame.sprite.Sprite):

    def __init__(self, width, height, speed):
        super().__init__()

        #self.image = pygame.Surface([width, height])
        self.image=pygame.image.load('pixelRobber.png').convert()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(width,height))
        

        self.width = width
        self.height = height
        #self.color = color
        self.speed = speed

        #pygame.draw.rect(self.image, self.color, [0,0,self.width,self.height])

        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image,BLACK, self.rect.center, self.radius)

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self,pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed*speed/40

    def moveBackward(self,speed):
        self.rect.y -= self.speed*speed/40

    def changeSpeed(self,speed):
        self.speed = speed

    def update(self):
        if  self.rect.x < 600 - 625:
            self.rect.x= 600 - 625
        elif self.rect.x > 600 + 580:
            self.rect.x=600 + 580 
            
        if  self.rect.y < 400 - 410:
            self.rect.y=400 - 410
        elif self.rect.y > 400 + 325:
            self.rect.y= 400 + 325
