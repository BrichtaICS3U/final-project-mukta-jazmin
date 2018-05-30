# Menu template with button class and basic menu navigation
# Adapted from http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/

import pygame, sys
pygame.init()

# Define some colours
WHITE = (230, 230, 230)
YELLOW = (233, 215, 88)
BLACK = (57, 57, 58)
ORANGE = (255, 133, 82)
BLUE = (41, 115, 115)

SCREENWIDTH = 1200
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

background = pygame.image.load("menuBackground.jpg!d")
background=pygame.transform.scale(background,(SCREENWIDTH, SCREENHEIGHT))

fontTitle = pygame.font.Font('freesansbold.ttf', 55)
textSurfaceTitle = fontTitle.render('tbd', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (400, 100)   # place the centre of the text

fontSetting = pygame.font.Font('freesansbold.ttf', 55)
textSurfaceSetting = fontSetting.render('Settings', True, BLACK) 
textRectSetting = textSurfaceSetting.get_rect()
textRectSetting.center = (400, 100)   # place the centre of the text

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
    def __init__(self, txt, location, action, bg=WHITE, fg=BLACK, size=(175, 75), font_name="Gothic", font_size=35):
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

def my_setting_function():
    """A function that advances to the settings"""
    global level
    level += 2

def my_next_function():
    """A function that advances to the next level"""
    global level
    level += 1

def my_previous_function():
    """A function that retreats to the previous level"""
    global level
    level == 1

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

level = 1
carryOn = True
clock = pygame.time.Clock()

#create button objects and store in buttons list
button_play = Button("Play", (SCREENWIDTH/2, SCREENHEIGHT/3), my_play_function)
button_setting  = Button("Settings", (SCREENWIDTH/2, SCREENHEIGHT/3), my_setting_function)
button_quit = Button("Quit", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_quit_function, bg=(50, 200, 20))
button_back = Button("Back", (SCREENWIDTH/2, SCREENHEIGHT*2/3),my_previous_function, bg=(50, 200, 20))
button_soundon = Button("Sound On", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_soundon_function, bg=(50, 200, 20))
button_soundoff = Button("Sound Off", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_soundoff_function, bg=(50, 200, 20))
#button_restart = Button("Restart", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_quit_function, bg=(50, 200, 20))
#button_menu = Button("Menu", (SCREENWIDTH/2, SCREENHEIGHT*2/3), my_quit_function, bg=(50, 200, 20))



#arrange button groups depending on level
level1_buttons = [button_play, button_setting,button_quit]
level2_buttons = [button_back, button_soundon,button_soundoff ]

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
    elif level == 2:
        for button in level2_buttons:
            button.draw()

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
