import pygame
import level

# initialize pygame window

pygame.init()
screen = pygame.display.set_mode([600, 600])
background = pygame.Surface((600, 600))
background.fill((0, 0, 0))
background.convert()

# create clock

clock = pygame.time.Clock()
FPS = 30

# temporary. ideally here, we create a level manager
current_level = level.Level(5, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [[1, 3, 0], [3, 4, 1], [3, 3, 1]])

# create game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # move player

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level.detection(current_level.objects, 0, "up", 0, 0 - current_level.tile_size, current_level.tiles,
                                current_level.tile_size, current_level.size)
            if event.key == pygame.K_DOWN:
                level.detection(current_level.objects, 0, "down", 0, current_level.tile_size, current_level.tiles,
                                current_level.tile_size, current_level.size)
            if event.key == pygame.K_LEFT:
                level.detection(current_level.objects, 0, "left", 0 - current_level.tile_size, 0, current_level.tiles,
                                current_level.tile_size, current_level.size)
            if event.key == pygame.K_RIGHT:
                level.detection(current_level.objects, 0, "right", current_level.tile_size, 0, current_level.tiles,
                                current_level.tile_size, current_level.size)

        # draw new screen

        screen.blit(background, (0, 0))

        # update the level to the screen

        for i in range(len(current_level.tiles)):
            screen.blit(pygame.transform.scale(current_level.tiles[i].variant,
                                               (round(current_level.tile_size), round(current_level.tile_size))),
                        (current_level.tiles[i].x, current_level.tiles[i].y))
        for i in range(len(current_level.objects)):
            screen.blit(pygame.transform.scale(current_level.objects[i].variant,
                                               (round(current_level.tile_size), round(current_level.tile_size))),
                        (current_level.objects[i].x, current_level.objects[i].y))

        clock.tick(FPS)
        pygame.display.flip()

pygame.quit()
