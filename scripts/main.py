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

# create clock

clock = pygame.time.Clock()
FPS = gamedata.fps

# temporary. ideally here, we create a level manager
lm = gamedata.levelmanager
current_level = 0
# create game loop

running = True
while running:
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
            if event.key == pygame.K_DOWN:
                lm.level_list[current_level].detection("down", 0, lm.level_list[current_level].tile_size, screen_size)
            if event.key == pygame.K_LEFT:
                lm.level_list[current_level].detection("left", 0 - lm.level_list[current_level].tile_size, 0, screen_size)
            if event.key == pygame.K_RIGHT:
                lm.level_list[current_level].detection("right", lm.level_list[current_level].tile_size, 0, screen_size)
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                current_level = lm.level_list[0]
            elif event.key == pygame.K_2:
                current_level = lm.level_list[1]
            elif event.key == pygame.K_3:
                current_level = lm.level_list[2]
            elif event.key == pygame.K_4:
                current_level = lm.level_list[3]
            elif event.key == pygame.K_5:
                current_level = lm.level_list[4]
            elif event.key == pygame.K_6:
                current_level = lm.level_list[5]
            elif event.key == pygame.K_7:
                current_level = lm.level_list[6]

        # draw new screen

        screen.blit(background, (0, 0))

        # update the level to the screen

        for i in range(len(lm.level_list[current_level].tiles)):
            screen.blit(pygame.transform.scale(lm.level_list[current_level].tiles[i].surface,
                                              (math.ceil(lm.level_list[current_level].tile_size), math.ceil(lm.level_list[current_level].tile_size))),
                       (round(lm.level_list[current_level].tiles[i].x), round(lm.level_list[current_level].tiles[i].y)))
        for i in range(len(lm.level_list[current_level].objects)):
            screen.blit(pygame.transform.scale(lm.level_list[current_level].objects[i].surface,
                                              (math.ceil(lm.level_list[current_level].tile_size), math.ceil(lm.level_list[current_level].tile_size))),
                       (round(lm.level_list[current_level].objects[i].x), round(lm.level_list[current_level].objects[i].y)))

        clock.tick(FPS)
        pygame.display.flip()

pygame.quit()
