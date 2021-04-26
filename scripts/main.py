import pygame
pygame.init()
import gamedata
import levels
import math
# do not remove ^

# initialize pygame window

screen_size = gamedata.screen_size
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface(screen_size)
start1 = pygame.image.load("../images/Start 1.png")
start2 = pygame.image.load("../images/Start 2.png")
menu_background = pygame.image.load("../images/Menu.png")
# rectangle of image at position where the image will be placed
start1Rect = start1.get_rect(center=(gamedata.resolution_x/2, gamedata.resolution_y/2))

# create clock

clock = pygame.time.Clock()
FPS = gamedata.fps

# temporary. ideally here, we create a level manager
lm = gamedata.levelmanager
current_level = lm.current_level
red_on = False
blue_on = False
color_history = [[red_on, blue_on]]
lm.moving_state = 4
levelchange = 0
menu_change = 0
music_playing = True
timer = 0

# create game loop

running = True
# variable to check if we should be in the menu or not
menu = True
pygame.mixer.music.load("../music/menu.wav")
pygame.mixer.music.play(loops=-1)
while running:

    current_level = lm.current_level
    moves = lm.moves
    # check to see if the menu has been gotten through or not
    if menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        background.fill((lm.level_list[current_level].bg()))
        background.convert()
        # get mouse information
        mpos = pygame.mouse.get_pos()
        L, R, C = pygame.mouse.get_pressed()
        # draws the menu image at the middle of the screen
        screen.blit(pygame.transform.scale(menu_background, (gamedata.resolution_x, gamedata.resolution_y)), (0, 0))
        screen.blit(start1, (gamedata.resolution_x - gamedata.resolution_x / 3 - 144, gamedata.resolution_y/2 - 144))
        # changes menu display if mouse is hovering the start text
        if start1Rect.collidepoint(mpos):
            screen.blit(start2, (gamedata.resolution_x - gamedata.resolution_x / 3 - 144,
                                 gamedata.resolution_y/2 - 144))
            # checks if the left mouse button has been pressed
            if L:
                menu = False
                pygame.mixer.music.fadeout(100)
                pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/click.wav"))
                music_playing = False
        clock.tick(FPS)
        pygame.display.flip()
        continue

    move_requested = False

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
        
    if not music_playing:
        c_l = current_level
        for a in levels.difficultyA:
            if a == c_l:
                pygame.mixer.music.load('../music/tutorial.wav')
                pygame.mixer.music.play(loops=-1)
                music_playing = True
        for b in levels.difficultyB:
            if b == c_l:
                pygame.mixer.music.load('../music/easylevel.wav')
                pygame.mixer.music.play(loops=-1)
                music_playing = True
        for c in levels.difficultyC:
            if c == c_l:
                pygame.mixer.music.load('../music/mediumlevel.wav')
                pygame.mixer.music.play(loops=-1)
                music_playing = True
        for d in levels.difficultyD:
            if d == c_l:
                pygame.mixer.music.load('../music/hardlevel.wav')
                pygame.mixer.music.play(loops=-1)
                music_playing = True
        for e in levels.difficultyN:
            if e == c_l:
                pygame.mixer.music.load('../music/menu.wav')
                pygame.mixer.music.play(loops=-1)
                music_playing = True
        if not music_playing:
            pygame.mixer.music.load('../music/tutorial.wav')
            pygame.mixer.music.play(loops=-1)
            music_playing = True
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # move player

        if event.type == pygame.KEYDOWN and levelchange == 0:
            # exit game if esc is pressed
            if event.key == pygame.K_ESCAPE:
                running = False
                print(moves)
            # skip the level (debug feature commented out for potential gold release)
            # if event.key == pygame.K_s:
                # lm.level_list[current_level].restart(moves)
                # for i in range(len(color_history) - 1):
                    # color_history.pop(-1)
                # red_on = color_history[-1][0]
                # blue_on = color_history[-1][1]
                # lm.moving_state = 5
                # lm.moves = 0
                # gamedata.levelmanager.current_level += 1
            # restart the level if r is pressed
            if event.key == pygame.K_r:
                lm.level_list[current_level].restart(moves)
                for i in range(len(color_history) - 1):
                    color_history.pop(-1)
                red_on = color_history[-1][0]
                blue_on = color_history[-1][1]
                lm.moving_state = 4
                lm.moves = 0
            # undo 1 move if u is pressed and at least 1 move has been made
            if event.key == pygame.K_u and moves > 0:
                if lm.moving_state == 0:
                    lm.level_list[current_level].undo()
                    if len(color_history) > 1:
                        color_history.pop(-1)
                        red_on = color_history[-1][0]
                        blue_on = color_history[-1][1]
                else:
                    lm.level_list[current_level].go_back()
                    red_on = color_history[-1][0]
                    blue_on = color_history[-1][1]
                lm.moving_state = 4
                lm.moves -= 1
            # make sure the player isn't moving and isn't in a pit before moving them
            if lm.moving_state == 0 and lm.level_list[current_level].objects[0].is_active:
                # move the player up 1 tile if able
                if event.key == pygame.K_UP:
                    lm.level_list[current_level].objects[0].push("up", 1)
                    move_requested = True
                # move the player down 1 tile if able
                if event.key == pygame.K_DOWN:
                    lm.level_list[current_level].objects[0].push("down", 1)
                    move_requested = True
                # move the player left 1 tile if able
                if event.key == pygame.K_LEFT:
                    lm.level_list[current_level].objects[0].push("left", 1)
                    move_requested = True
                # move the player right 1 tile if able
                if event.key == pygame.K_RIGHT:
                    lm.level_list[current_level].objects[0].push("right", 1)
                    move_requested = True
            # if event.key == pygame.K_1 and lm.current_level != 0:
                # lm.current_level = 0
                # lm.moves = 0
            # elif event.key == pygame.K_2 and lm.current_level != 1:
                # lm.current_level = 1
                # lm.moves = 0
            # elif event.key == pygame.K_3 and lm.current_level != 2:
                # lm.current_level = 2
                # lm.moves = 0
            # elif event.key == pygame.K_4 and lm.current_level != 3:
                # lm.current_level = 3
                # lm.moves = 0
            # elif event.key == pygame.K_5 and lm.current_level != 4:
                # lm.current_level = 4
                # lm.moves = 0
            # elif event.key == pygame.K_6 and lm.current_level != 5:
                # lm.current_level = 5
                # lm.moves = 0
            # elif event.key == pygame.K_7 and lm.current_level != 6:
                # lm.current_level = 6
                # lm.moves = 0
        
    # address interactions
    
    if levelchange == 0:
        objects_moving = False
        # checks which movement state the game is in (0 = nothing moving, 1 = on tiles but stuff still needs to move,
        # 2 = currently moving, 3 = checking tiles after done moving, 4 = 3 but doesn't count as a move,
        # 5 = next level triggered (always goes to 4)) make sure an undo wasn't requested before setting the movement state
        if not lm.moving_state == 4:
            # sets up for a tile action check if objects are on tiles, otherwise continues moving them
            for item in lm.level_list[current_level].objects:
                if len(item.push_requests) > 0:
                    if item.push_requests[0][1] % 5 == 0:
                        lm.moving_state = 1
                    else:
                        lm.moving_state = 2
                    objects_moving = True
            # continues to the next step if nothing needs to move
            if not objects_moving:
                if lm.moving_state == 1:
                    lm.moving_state = 0
                elif lm.moving_state == 2:
                    lm.moving_state = 3
                elif lm.moving_state == 3:
                    # triggers the end of the turn (updates position/state histories)
                    for item in lm.level_list[current_level].tiles:
                        item.turn_end()
                    for item in lm.level_list[current_level].objects:
                        item.turn_end()
                    color_history.append([red_on, blue_on])
                    lm.moves += 1
                    lm.moving_state = 0
                elif lm.moving_state == 5:
                    lm.moving_state = 4
        
        # checks if tiles that perform functions have an object on them and preforms said function if so
        if lm.moving_state == 1 or lm.moving_state == 3 or lm.moving_state == 4:
            # activates levers, buttons, or rotators if something is on top of them
            for item in lm.level_list[current_level].tiles:
                if item.__class__ == levels.levelclass.tileclass.Lever or item.__class__ == levels.levelclass.tileclass.Button or item.__class__ == levels.levelclass.tileclass.Rotator:
                    if item.__class__ == levels.levelclass.tileclass.Rotator:
                        item.detect(lm.level_list[current_level].objects, lm.level_list[current_level].tiles, lm.level_list[current_level].size)
                    else:
                        item.detect(lm.level_list[current_level].objects)
            # swaps the red and/or blue state from any lever or button interactions
            for item in lm.level_list[current_level].tiles:
                if item.__class__ == levels.levelclass.tileclass.Lever or item.__class__ == levels.levelclass.tileclass.Button:
                    if item.red_swap():
                        if red_on:
                            red_on = False
                        else:
                            red_on = True
                    if item.blue_swap():
                        if blue_on:
                            blue_on = False
                        else:
                            blue_on = True
            # updates the crates and walls depending on which colors are on or off, tells objects to be pushed if
            # they're on an arrow, and tells objects to fall if they're on a pit
            for item in lm.level_list[current_level].objects:
                if item.__class__ == levels.levelclass.objectclass.Crate:
                    item.update_state(red_on, blue_on)
            for item in lm.level_list[current_level].tiles:
                if item.__class__ == levels.levelclass.tileclass.Wall:
                    item.update_state(red_on, blue_on)
                if item.__class__ == levels.levelclass.tileclass.Arrow:
                    item.update_direction(0)
                    item.push_objects(lm.level_list[current_level].objects, move_requested)
            # triggers movement detection specifically so that objects being pushed by arrows that get stopped
            # by a wall will still fall into pits
            lm.level_list[current_level].move_detection(screen_size)
            # continues with object updates
            for item in lm.level_list[current_level].tiles:
                if item.__class__ == levels.levelclass.tileclass.Pit:
                    item.fall_objects(lm.level_list[current_level].objects)
                if item.__class__ == levels.levelclass.tileclass.Goal:
                    if item.next_level(lm.level_list[current_level].objects):
                        lm.level_list[current_level].restart(moves)
                        for i in range(len(color_history) - 1):
                            color_history.pop(-1)
                        red_on = color_history[-1][0]
                        blue_on = color_history[-1][1]
                        gamedata.levelmanager.current_level += 1  
                        levelchange = 1
            if lm.moving_state == 1:
                # triggers movement detection and execution
                lm.level_list[current_level].move_detection(screen_size)
                lm.level_list[current_level].move_cycle()
            if lm.moving_state == 4:
                # ends the update chain if it was just for an undo
                lm.moving_state = 0
        elif lm.moving_state == 2:
            # moves objects if they're currently in between tiles
            lm.level_list[current_level].move_cycle()
    else:
        timer += 1
        if timer == 5:
            timer = 0
            lm.moving_state = 5
            lm.moves = 0
            levelchange = 0
            music_playing = False          

    # draw new screen

    screen.blit(background, (0, 0))

    # update the level to the screen

    for i in range(len(lm.level_list[current_level].tiles)):
        screen.blit(pygame.transform.scale(lm.level_list[current_level].tiles[i].surface,
                                          (math.ceil(lm.level_list[current_level].tile_size), math.ceil(lm.level_list[current_level].tile_size))),
                   (round(lm.level_list[current_level].tiles[i].x), round(lm.level_list[current_level].tiles[i].y)))
    for i in range(len(lm.level_list[current_level].objects)):
        # check if object is active otherwise don't render
        if lm.level_list[current_level].objects[i].is_active:
            screen.blit(pygame.transform.scale(lm.level_list[current_level].objects[i].surface,
                                              (math.ceil(lm.level_list[current_level].tile_size * lm.level_list[current_level].objects[i].size),
                                               math.ceil(lm.level_list[current_level].tile_size * lm.level_list[current_level].objects[i].size))),
                       (round(lm.level_list[current_level].objects[i].x), round(lm.level_list[current_level].objects[i].y)))
    screen.blit(lm.level_list[current_level].text, (gamedata.screen_offset[0] + 10, gamedata.screen_offset[1] - 40))

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
