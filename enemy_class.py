import pygame, random
import math
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()

        self.image=pygame.image.load('Mummy_zombie_concept_art.jpg').convert()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(width,height))

        self.width = width
        self.height = height
        #self.color = color
        self.speed = 1
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


    def update(self):
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
                            
        if  self.rect.x < 500-200:
            self.rect.x=500-200
        elif self.rect.x > 500+200:
           self.rect.x=500+200
            
        self.rect.y = self.rect.y + random.randint(-5, 5)*self.speed/20
        if  self.rect.y < 500-100:
            self.rect.y=500-100
        elif self.rect.y > 500+100:
            self.rect.y=500+100

    
