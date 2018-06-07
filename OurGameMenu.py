# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()

#print (pygame.font.get_fonts())

# Define some colours
WHITE = (230, 230, 230)
YELLOW = (233, 215, 88)
BLACK = (57, 57, 58)
ORANGE = (255, 133, 82)
BLUE = (41, 115, 115)
SANDORANGE = (196, 100, 40)
TRANSPARENT = (255, 255, 255, 100)

SCREENWIDTH = 1200
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

background = pygame.image.load("OurMenuBackground.png")
background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))

fontTitle = pygame.font.SysFont('Harrington', 75)
textSurfaceTitle = fontTitle.render('The Pink Sphinx', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (600, 150)   # place the centre of the text

fontSetting = pygame.font.SysFont('Harrington', 55)
textSurfaceSetting = fontSetting.render('SETTINGS', True, BLACK) 
textRectSetting = textSurfaceSetting.get_rect()
textRectSetting.center = (600, 125)   # place the centre of the text

fontSound = pygame.font.SysFont('Harrington', 40)
textSurfaceSound = fontSound.render('SOUND: ', True, BLACK) 
textRectSound = textSurfaceSound.get_rect()
textRectSound.center = (125, 245)   # place the centre of the text

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Ancient Egyptian Music - Hathor.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)

class Button():
    """This is a class for a generic button.
       txt = text on the button
       location = (x,y) coordinates of the button's centre
       action = name of function to run when button is pressed
       bg = background colour (default is white)
       fg = text colour (default is black)
       size = (width, height) of button
       font_name = name of font
       font_size = size of font
    """
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(175, 75), font_name="Myriad Web Pro", font_size=30):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        """Checks if mouse is over button using rect collision"""
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = BLACK  # mouseover color

    def call_back(self):
        """Runs a function when clicked"""
        self.call_back_()

def my_play_function():
    """A function that advances player to instruction screen"""
    global level
    level += 1
    print(level)


def my_setting_function():
    """A function that advances to the settings"""
    global level
    level += 3
    print(level)

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1
    print(level)

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level -= 3
    print(level)

def PlayTheGame():
    global level
    level += 2

def my_back_function():
    """A function that retreats to the previous level"""
    global level
    level -= 2
    
def my_soundon_function():
    """A function that turns sound on"""
    print('sound is ON')
    pygame.mixer.music.unpause()

def my_soundoff_function():
    """A function that turns sound off"""
    print('sound is OFF')
    pygame.mixer.music.pause()

def my_quit_function():
    """A function that will quit the game and close the pygame window"""
    pygame.quit()
    sys.exit()

def my_restart_function():
    """A function that will bring player back to start of game"""
    level == 3

def my_menu_function():
    """A function that brings player back to menu screen"""
    level == 1 

def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 2:
        for button in level2_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 3:
        for button in level3_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()
    elif level == 4:
        for button in level4_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects and store in buttons list
button_play = Button("PLAY", (SCREENWIDTH/3, SCREENHEIGHT/6*3.5), my_play_function, bg =  (196, 100, 40))
button_setting  = Button("SETTINGS", (SCREENWIDTH/3*2, SCREENHEIGHT/6*3.5), my_setting_function, bg= (196, 100, 40))
button_quit = Button("QUIT", (SCREENWIDTH/2, SCREENHEIGHT/4*3), my_quit_function, bg= (196, 100, 40))
button_next = Button("NEXT", (SCREENWIDTH*7/8 + 40, SCREENHEIGHT*7/8),my_next_function, bg=(196, 100, 40))
button_back = Button("BACK", (SCREENWIDTH/8 - 40, SCREENHEIGHT*7/8),my_previous_function, bg=(196, 100, 40))
button_back2 = Button("BACK", (SCREENWIDTH/8 - 40, SCREENHEIGHT*7/8),my_previous_function, bg=(196, 100, 40))
button_soundon = Button("ON", (SCREENWIDTH/3, SCREENHEIGHT/3 - 25), my_soundon_function, bg=(196, 100, 40))
button_soundoff = Button("OFF", (SCREENWIDTH/2 + 100, SCREENHEIGHT/3 - 25), my_soundoff_function, bg=(196, 100, 40))
button_restart = Button("RESTART", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_restart_function, bg=(196, 100, 40))
button_menu = Button("MENU", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_menu_function, bg=(196, 100, 40))
PlayTheGame = Button("PLAY", (SCREENWIDTH*7/8 + 40, SCREENHEIGHT*7/8), my_play_function, bg =  (196, 100, 40))

#arrange button groups depending on level
level1_buttons = [button_play, button_setting,button_quit]
level4_buttons = [button_back, button_soundon, button_soundoff]
level2_buttons = [button_back2, button_next]
level3_buttons = [button_back, PlayTheGame]


#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # Player clicked the mouse
            mousebuttondown(level)

    # --- Game logic goes here

    # --- Draw code goes here

    # Clear the screen to white
    screen.blit(background, (0, 0))

    # Draw buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()
        screen.blit(textSurfaceTitle, textRectTitle)
        background = pygame.image.load("OurMenuBackground.png")
        background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))
    elif level == 2:
        for button in level2_buttons:
            button.draw()
            background = pygame.image.load("Instruction Page 1.png")
            background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))
    elif level == 3:
        for button in level3_buttons:
            button.draw()
            background = pygame.image.load("unnamed.png")
            background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))
    elif level == 4:
        for button in level4_buttons:
            button.draw()
            screen.blit(textSurfaceSetting, textRectSetting)
            screen.blit(textSurfaceSound, textRectSound)
            background = pygame.image.load("OurMenuBackground.png")
            background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))
        

        

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
