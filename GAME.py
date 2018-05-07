import pygame, random
from player_class import player
from enemy_class import enemy
pygame.init()

PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

speed = 1

SCREENWIDTH = 0
SCREENHEIGHT = 0

size = (SCREENWIDTH, SCREENHEIGHT)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("...'")

all_sprites_list = pygame.sprite.Group()
                           
playerplayer = player(PURPLE, 20, 30, 10)

enemy1 = enemy(BLACK, 20, 30, 10)
enemy1.rect.x = 500
enemy1.rect.y = 500

all_sprites_list.add(playerplayer)
all_sprites_list.add(enemy1)

all_enemy_sprites = pygame.sprite.Group()
all_enemy_sprites.add(enemy1)

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
    if keys[pygame.K_s]:
        playerplayer.moveForward(5)
    if keys [pygame.K_w]:
       playerplayer.moveBackward(5)
                                    

#GAME LOGIC
    for enemy in all_enemy_sprites:
        enemy.moveForward(speed)
        
    all_sprites_list.update()

#DRAWING ON SCREEN
    screen.fill(WHITE)

    all_sprites_list.draw(screen)

    #all_enemy_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
                           
