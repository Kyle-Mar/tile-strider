import pygame

# class for tiles
pit = pygame.image.load('../images/pit.png')
floor = pygame.image.load('../images/floor.png')
wall = pygame.image.load('../images/wall.png')
tileset = [pit, floor, wall]
nameset = ["pit", "floor", "wall"]


class Tile(object):
    def __init__(self, x, y, variant):
        # creates a tile (variant is what type of tile it is, see the tileset list for info)
        self.x = x
        self.y = y
        self.surface = tileset[variant]
        self.name = nameset[variant]
        self.is_floor = ""
        if self.name == "pit" or self.name == "wall":
            self.is_floor = False
        else:
            self.is_floor = True
