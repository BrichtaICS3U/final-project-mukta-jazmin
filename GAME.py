import pygame, random
from player_class import player
from treasure_class import Treasure
pygame.init()

PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

speed = 1

SCREENWIDTH = 0
SCREENHEIGHT = 0

size = (SCREENWIDTH, SCREENHEIGHT)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("...'")

all_sprites_list = pygame.sprite.Group()
all_treasure_list = pygame.sprite.Group()

playerplayer = player(PURPLE, 20, 30, 10)

treasure1 = Treasure([100, 60])

all_sprites_list.add(playerplayer)
all_treasure_list.add(treasure1)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn= False

    keys = pygame.key.get_pressed()
    if  keys[pygame.K_a]:
        playerplayer.moveLeft(5)
    if keys[pygame.K_d]:
        playerplayer.moveRight(5)
    if keys[pygame.K_s]:
        playerplayer.moveForward(5)
    if keys [pygame.K_w]:
       playerplayer.moveBackward(5)
                                    

#GAME LOGIC
    hit= pygame.sprite.spritecollide(playerplayer, all_treasure_list, True)

    if hit:
        print ("sdfs")
    all_sprites_list.update()

#DRAWING ON SCREEN
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [400, 400, 200, 200])

    all_sprites_list.draw(screen)
    all_treasure_list.draw(screen)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
                           
#CITATIONS
#code for treasure collisions : https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
