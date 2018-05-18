import pygame, random
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREENWIDTH = 1200
SCREENHEIGHT = 800

class enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()

        self.image=pygame.image.load('flat,800x800,075,f.u1.jpg').convert()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(width,height))

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


    def chase(self):
        if self.steps <=0:
            self.steps = random.randint(5,10)
            self.direction = random.randint(1,4)
        else:
            if self.direction ==1:
                self.rect.x += 5
            elif self.direction == 2:
                self.rect.x -= 5
            elif self.direction == 3:
                self.rect.y +=5
            else:
                self.rect.y-= 5
            self.steps -= 1

        if  self.rect.x < 0:
            self.rect.x=1200
        elif self.rect.x > 1200:
           self.rect.x=1200
            
        self.rect.y = self.rect.y + random.randint(-5, 5)*self.speed/20
        if  self.rect.y < 0:
            self.rect.y=800
        elif self.rect.y > 800:
            self.rect.y=800

    def update(self, player):
        dx, dy = (player.rect.x - self.rect.x)/(math.sqrt((player.rect.x - self.rect.x) ** 2 + (player.rect.y - self.rect.y) ** 2)), (player.rect.y - self.rect.y)/math.sqrt((player.rect.x - self.rect.x)**2 +(player.rect.y - self.rect.y) ** 2)
        self.rect.x +=dx
        self.rect.y += dy

        #newCoord = (player.rect.x + dx * self.speed, player.rect.y + dy * self.speed)

    
