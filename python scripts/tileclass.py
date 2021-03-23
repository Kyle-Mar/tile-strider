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
        self.variant = tileset[variant]
        self.name = nameset[variant]

    def x(self):
        # returns the tile's x position
        return self.x

    def y(self):
        # returns the tile's y position
        return self.y

    def variant(self):
        # returns the tile's surface for blitting
        return self.variant

    def is_floor(self):
        # returns true if the tile can have objects on top of it, returns false otherwise
        if self.name == "pit" or self.name == "wall":
            return False
        else:
            return True
