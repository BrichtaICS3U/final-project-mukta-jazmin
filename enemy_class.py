import pygame, random
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREENWIDTH = 1200
SCREENHEIGHT = 800

class enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()

        self.image=pygame.image.load('pixelMummy.png').convert()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(width,height))

        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image,BLACK, self.rect.center, self.radius)

        self.width = width
        self.height = height
        #self.color = color
        self.speed = 3
        self.steps = speed
        self.direction = 1

        #pygame.draw.rect(self.image, self.color, [0,0,self.width,self.height])

        self.rect = self.image.get_rect()

    def moveForward(self, speed):
        self.rect.y += self.speed*speed/40

    def moveBackward(self,speed):
        self.rect.y -= self.speed*speed/40

    def changeSpeed(self,speed):
        self.speed = speed


    def update(self, walls):
        """This method will choose a pseudo-random walk for the mummy."""
        if self.steps <=0:
            self.steps = random.randint(5,10)
            self.direction = random.randint(-2,2)
        else:
            if self.direction ==1:
                self.rect.x += 5
            elif self.direction == -1:
                self.rect.x -= 5
            elif self.direction == 0: # do nothing because mummies are dumb
                self.rect.x = self.rect.x
            elif self.direction == 2:
                self.rect.y +=5
            else:
                self.rect.y-= 5
            self.steps -= 1

        #prevent mummies from walking off screen
        if  self.rect.x < 0:
            self.rect.x=0
        elif self.rect.x > 990:
           self.rect.x=990
            
        if  self.rect.y < 0:
            self.rect.y=0
        elif self.rect.y > 790:
            self.rect.y=790

        #prevent enemies from moving through walls
        if pygame.sprite.spritecollide(self, walls, False):
            self.direction = -self.direction

    def chase(self, player, distance, walls):
        """This method allows the mummy to chase the player."""
        dx = (player.rect.x - self.rect.x)/distance
        dy = (player.rect.y - self.rect.y)/distance

        #prevent movement through walls
        
        if pygame.sprite.spritecollide(self, walls, False):
            self.rect.x -= dx*self.speed
            self.rect.y -= dy*self.speed

        else:
            
            self.rect.x += dx*self.speed
            self.rect.y += dy*self.speed

    

    
