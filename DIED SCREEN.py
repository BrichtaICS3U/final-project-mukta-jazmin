import pygame, sys
pygame.init()

SCREENWIDTH = 1200
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

background = pygame.image.load("MUMMIFIED SCREEN copy.png")
background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))

pygame.display.flip()
