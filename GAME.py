import pygame, random, math
from player_class import player
from treasure_class import Treasure
from enemy_class import enemy
from exitDoor_class import exitDoor
pygame.init()

PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

speed = 1
artifact_counter = 0

SCREENWIDTH = 1200
SCREENHEIGHT = 800

size = (SCREENWIDTH, SCREENHEIGHT)
screen= pygame.display.set_mode(size)
pygame.display.set_caption("...'")

all_sprites_list = pygame.sprite.Group()
                           
playerplayer = player(160,100,70)
playerplayer.rect.x = 0
playerplayer.rect.y = 0

treasure1 = Treasure(100,120)
treasure1.rect.x = 500
treasure1.rect.y = 500

enemy1 = enemy(80, 120, 40)
enemy1.rect.x = 500
enemy1.rect.y = 500

enemy2 = enemy(80, 120, 40)
enemy2.rect.x = 1000
enemy2.rect.y = 100

enemy3 = enemy(80, 120, 40)
enemy3.rect.x = 100
enemy3.rect.y = 700

exitDoor = exitDoor(100,120)
exitDoor.rect.x = 900
exitDoor.rect.y = 600

all_enemy_sprites = pygame.sprite.Group()
all_treasure_list = pygame.sprite.Group()
all_exitDoor_list = pygame.sprite.Group()
all_enemy_sprites.add(enemy1, enemy2, enemy3)


all_sprites_list.add(playerplayer)
#leave enemies in their own group
#all_sprites_list.add(enemy1,enemy2, enemy3)
all_treasure_list.add(treasure1)
all_exitDoor_list.add(exitDoor)

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
        #calculate distance between player and mummy and use for behaviour
        distance = math.hypot(enemy.rect.x-playerplayer.rect.x, enemy.rect.y-playerplayer.rect.y)
        #print("distance ", +distance)
        if distance < 300: #later mummies could detect player in larger distance
            enemy.chase(playerplayer, distance)
        else:
            enemy.update()

    point= pygame.sprite.spritecollide(playerplayer, all_treasure_list, True)
    if point:
        print ("You picked up the treasure!")
        artifact_counter += 1
    all_sprites_list.update()

    hit = pygame.sprite.spritecollide(playerplayer, all_enemy_sprites, True)
    if hit:
        print("game over")
        carryOn=False

    fontTitle = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceTitle = fontTitle.render('Score: ' + str(artifact_counter), True, BLACK) 
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (1100, 50) 

    pygame.display.update()

    escape = pygame.sprite.spritecollide(playerplayer, all_exitDoor_list, True)
    if escape:
        print('YOU HAVE ESCAPED')
        carryOn=False


#DRAWING ON SCREEN
    screen.fill(WHITE)
    all_enemy_sprites.draw(screen)
    all_sprites_list.draw(screen)
    all_treasure_list.draw(screen)
    screen.blit(textSurfaceTitle, textRectTitle)
    all_exitDoor_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
                           
#CITATIONS
#code for treasure collisions: https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
#code for enemy chase function: https://stackoverflow.com/questions/10971671/how-to-make-an-enemy-follow-a-player-in-pygame/10971710
