import pygame
import levels
import settings
import levelclass
import math

# initialize pygame window

pygame.init()
screen_size = [settings.resolution_x, settings.resolution_y]
screen_offset = [(screen_size[0] - 500) / 2, (screen_size[1] - 500) / 2]
screen = pygame.display.set_mode(screen_size)
background = pygame.Surface(screen_size)
background.fill((0, 0, 0))
background.convert()

# create clock

clock = pygame.time.Clock()
FPS = 30

# temporary. ideally here, we create a level manager
#current_level = levelclass.Level(5, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                                [[1, 3, 0], [3, 4, 1], [3, 3, 1]], screen_offset)
current_level = levels.menu1

# create game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # move player

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                current_level.detection("up", 0, 0 - current_level.tile_size, screen_size)
            if event.key == pygame.K_DOWN:
                current_level.detection("down", 0, current_level.tile_size, screen_size)
            if event.key == pygame.K_LEFT:
                current_level.detection("left", 0 - current_level.tile_size, 0, screen_size)
            if event.key == pygame.K_RIGHT:
                current_level.detection("right", current_level.tile_size, 0, screen_size)

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
