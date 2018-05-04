import pygame, random
from player_class import player
pygame.init()

PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

speed = 1

SCREENWIDTH = 0
SCREENHEIGHT = 0

size = (SCREENWIDTH, SCREENHEIGHT)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("...'")

all_sprites_list = pygame.sprite.Group()
                           
playerplayer = player(PURPLE, 20, 30)

all_sprites_list.add(playerplayer)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=FALSE

    keys = pygame.key.get_pressed()
    if  keys[pygame.K_a]:
        playerplayer.moveLeft(5)
    if keys[pygame.K_d]:
        playerplayer.moveRight(5)
    if keys[pygame.
                                    

#GAME LOGIC
    all_sprites_list.update()

#DRAWING ON SCREEN
    screen.fill(WHITE)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
                           
