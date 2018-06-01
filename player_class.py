import pygame
WHITE = (255, 255, 255)
BLACK = (0,0,0)

SCREENWIDTH = 1200
SCREENHEIGHT = 800


class player(pygame.sprite.Sprite):

    def __init__(self, width, height, speed):
        super().__init__()

        #self.image = pygame.Surface([width, height])
        self.image=pygame.image.load('camelRobber.png').convert()
        self.image.set_colorkey(BLACK)
        self.image=pygame.transform.scale(self.image,(width,height))
        

        self.width = width
        self.height = height
        #self.color = color
        self.speed = speed

        #pygame.draw.rect(self.image, self.color, [0,0,self.width,self.height])

        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image,BLACK, self.rect.center, self.radius)

    def moveRight(self, pixels, walls):
        self.rect.x += pixels
        for wall in walls:
            if (pygame.sprite.collide_rect(self,wall)):
                self.rect.x -= pixels

    def moveLeft(self,pixels,walls):
        self.rect.x -= pixels
        for wall in walls:
            if (pygame.sprite.collide_rect(self,wall)):
                self.rect.x += pixels

    def moveForward(self, speed,walls):
        self.rect.y += self.speed*speed/40
        for wall in walls:
            if (pygame.sprite.collide_rect(self,wall)):
                self.rect.y -= self.speed*speed/40

    def moveBackward(self,speed,walls):
        self.rect.y -= self.speed*speed/40
        for wall in walls:
            if (pygame.sprite.collide_rect(self,wall)):
                self.rect.y += self.speed*speed/40


    def changeSpeed(self,speed):
        self.speed = speed

    def update(self):
        if  self.rect.x < 0 :
            self.rect.x= 0 
        elif self.rect.x >1200-self.width:
            self.rect.x=1200 - self.width
            
        if  self.rect.y < 0 :
            self.rect.y=0
        elif self.rect.y > 800-self.height :
            self.rect.y= 800-self.height

        #prevent player from moving through walls
##        if pygame.sprite.spritecollide(self, walls, False):
##            self.rect.x = self.rect.x- self.width
##            self.rect.y = self.rect.y- self.height
