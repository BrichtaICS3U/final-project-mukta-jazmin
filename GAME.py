import pygame, random
from player_class import player
from treasure_class import Treasure
from enemy_class import enemy
pygame.init()

PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

speed = 1

font = pygame.font.SysFont("Courier", 25)

#def score (score):
    #text = font.render("Score: " + str(score), True black)
   # gameDisplay.blit


SCREENWIDTH = 1200
SCREENHEIGHT = 800

size = (SCREENWIDTH, SCREENHEIGHT)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("...'")

all_sprites_list = pygame.sprite.Group()
                           
playerplayer = player(120,100,70)

treasure1 = Treasure(100,120)
treasure1.rect.x = 500
treasure1.rect.y = 500

enemy1 = enemy(80, 120, 40)
enemy1.rect.x = 500
enemy1.rect.y = 500

all_enemy_sprites = pygame.sprite.Group()
all_treasure_list = pygame.sprite.Group()
all_enemy_sprites.add(enemy1)


all_sprites_list.add(playerplayer)
all_sprites_list.add(enemy1)
all_treasure_list.add(treasure1)


carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn= False

    keys = pygame.key.get_pressed()
    if  keys[pygame.K_a]:
        playerplayer.moveLeft (5)
    if keys[pygame.K_d]:
        playerplayer.moveRight (5)
    if keys[pygame.K_s]:
        playerplayer.moveForward (5)
    if keys [pygame.K_w]:
       playerplayer.moveBackward (5)

                                
#GAME LOGIC
    for enemy in all_enemy_sprites:
        enemy.moveForward(speed)

    all_sprites_list.update()
    
    point= pygame.sprite.spritecollide(playerplayer, all_treasure_list, True)
    if point:
        print ("sdfs")
    all_sprites_list.update()

    hit = pygame.sprite.spritecollide(playerplayer, all_enemy_sprites, True)
    if hit:
        print("game over")
        carryOn=False

#DRAWING ON SCREEN
    screen.fill(WHITE)

    all_sprites_list.draw(screen)
    all_treasure_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
                           
#CITATIONS
#code for treasure collisions : https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
