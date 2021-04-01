import pygame
import levels
import settings
import math

# initialize pygame window

pygame.init()
screen_size = settings.screen_size
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface(screen_size)

# create clock

clock = pygame.time.Clock()
FPS = settings.fps

# temporary. ideally here, we create a level manager
current_level = levels.level50

# create game loop

running = True
# variable to check if we should be in the menu or not
menu = True
while running:
    # check to see if the menu has been gotten through or not
    if menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        background.fill((current_level.bg()))
        background.convert()
        # get mouse information
        Mx,My = pygame.mouse.get_pos()
        L,R,C = pygame.mouse.get_pressed()
        # draws the menu image at the middle of the screen
        screen.blit('../images/Start 1.png', (settings.resolution_x/50 - 144, settings.resolution_y/50 - 144))
        # changes menu display if mouse is hovering the start text
        92 114 ul 195 158 br
        if 207 < Mx < 351 and 229 < My < 273:
            screen.blit('../images/Start 2.png', (settings.resolution_x/50 - 144, settings.resolution_y/50 - 144))
            # checks if the left mouse button has been pressed
            if L:
                menu = False
        clock.tick(FPS)
        pygame.display.flip()
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background.fill((current_level.bg()))
    background.convert()

    # note: these "code snippets" aren't really code, but rather what these blocks should end up doing in general

    # if current_level == none:
    #  display main menu
    # else:
    # load level

    # music stuff is going to go here
    # if current level == levels.levelX (where X is a level):
    #   play level song
    # else:
    #   play menu theme


    # move player

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            current_level.detection("up", 0, 0 - current_level.tile_size, screen_size)
        if event.key == pygame.K_DOWN:
            current_level.detection("down", 0, current_level.tile_size, screen_size)
        if event.key == pygame.K_LEFT:
            current_level.detection("left", 0 - current_level.tile_size, 0, screen_size)
        if event.key == pygame.K_RIGHT:
            current_level.detection("right", current_level.tile_size, 0, screen_size)
        if event.key == pygame.K_ESCAPE:
            running = False
        if event.key == pygame.K_1:
            current_level = levels.level51
        elif event.key == pygame.K_2:
            current_level = levels.level50
        elif event.key == pygame.K_3:
            current_level = levels.level52
        elif event.key == pygame.K_4:
            current_level = levels.menu1
        elif event.key == pygame.K_5:
            current_level = levels.menu2
        elif event.key == pygame.K_6:
            current_level = levels.menu3
        elif event.key == pygame.K_7:
            current_level = levels.menu4

    # draw new screen

    screen.blit(background, (0, 0))

    # update the level to the screen

    for i in range(len(current_level.tiles)):
        screen.blit(pygame.transform.scale(current_level.tiles[i].surface,
                                        (math.ceil(current_level.tile_size), math.ceil(current_level.tile_size))),
                (round(current_level.tiles[i].x), round(current_level.tiles[i].y)))
    for i in range(len(current_level.objects)):
        screen.blit(pygame.transform.scale(current_level.objects[i].surface,
                                        (math.ceil(current_level.tile_size), math.ceil(current_level.tile_size))),
                (round(current_level.objects[i].x), round(current_level.objects[i].y)))

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
