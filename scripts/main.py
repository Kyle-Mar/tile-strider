import pygame
import gamedata
import levels
# do not remove ^
import math

# initialize pygame window

pygame.init()
screen_size = gamedata.screen_size
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface(screen_size)
start1 = pygame.image.load("../images/Start 1.png")
start2 = pygame.image.load("../images/Start 2.png")
#rectangle of image at position where the image will be placed
start1Rect = start1.get_rect(center=((gamedata.resolution_x/2, gamedata.resolution_y/2)))
# create clock

clock = pygame.time.Clock()
FPS = gamedata.fps

# temporary. ideally here, we create a level manager
lm = gamedata.levelmanager
current_level = lm.current_level
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
        background.fill((lm.level_list[current_level].bg()))
        background.convert()
        # get mouse information
        mpos = pygame.mouse.get_pos()
        L,R,C = pygame.mouse.get_pressed()
        # draws the menu image at the middle of the screen
        screen.blit(start1, (gamedata.resolution_x/2 - 144, gamedata.resolution_y/2 - 144))
        # changes menu display if mouse is hovering the start text
        if start1Rect.collidepoint(mpos):
            screen.blit(start2, (gamedata.resolution_x/2 - 144, gamedata.resolution_y/2 - 144))
            # checks if the left mouse button has been pressed
            if L:
                menu = False
        clock.tick(FPS)
        pygame.display.flip()
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        background.fill((lm.level_list[current_level].bg()))
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
                lm.level_list[current_level].detection("up", 0, 0 - lm.level_list[current_level].tile_size, screen_size)
                lm.level_list[current_level].moves += 1
            if event.key == pygame.K_DOWN:
                lm.level_list[current_level].detection("down", 0, lm.level_list[current_level].tile_size, screen_size)
                lm.level_list[current_level].moves += 1
            if event.key == pygame.K_LEFT:
                lm.level_list[current_level].detection("left", 0 - lm.level_list[current_level].tile_size, 0, screen_size)
                lm.level_list[current_level].moves += 1
            if event.key == pygame.K_RIGHT:
                lm.level_list[current_level].detection("right", lm.level_list[current_level].tile_size, 0, screen_size)
                lm.level_list[current_level].moves += 1
            if event.key == pygame.K_u and lm.level_list[current_level].moves > 0:
                lm.level_list[current_level].undo()
                lm.level_list[current_level].moves -= 1
            if event.key == pygame.K_r:
                lm.level_list[current_level].restart(lm.level_list[current_level].moves)
                lm.level_list[current_level].moves = 0
            if event.key == pygame.K_d:
                print(lm.level_list[current_level].objects[1].position_history)
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                current_level = 0
            elif event.key == pygame.K_2:
                current_level = 1
            elif event.key == pygame.K_3:
                current_level = 2
            elif event.key == pygame.K_4:
                current_level = 3
            elif event.key == pygame.K_5:
                current_level = 4
            elif event.key == pygame.K_6:
                current_level = 5
            elif event.key == pygame.K_7:
                current_level = 6

        # draw new screen

        screen.blit(background, (0, 0))

        # update the level to the screen

        for i in range(len(lm.level_list[current_level].tiles)):
            screen.blit(pygame.transform.scale(lm.level_list[current_level].tiles[i].surface,
                                              (math.ceil(lm.level_list[current_level].tile_size), math.ceil(lm.level_list[current_level].tile_size))),
                       (round(lm.level_list[current_level].tiles[i].x), round(lm.level_list[current_level].tiles[i].y)))
        for i in range(len(lm.level_list[current_level].objects)):
            #check if object is active otherwise don't render
            if lm.level_list[current_level].objects[i].active:
                screen.blit(pygame.transform.scale(lm.level_list[current_level].objects[i].surface,
                                                  (math.ceil(lm.level_list[current_level].tile_size), math.ceil(lm.level_list[current_level].tile_size))),
                           (round(lm.level_list[current_level].objects[i].x), round(lm.level_list[current_level].objects[i].y)))

        clock.tick(FPS)
        pygame.display.flip()

pygame.quit()
