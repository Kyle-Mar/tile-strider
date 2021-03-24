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
        if variant == 0:
            self.__class__ = Pit
        if variant == 1:
            self.__class__ = Floor
        if variant == 2:
            self.__class__ = Wall

class Pit(Tile):
    def __init__(self):
        #creates a pit subclass
        super().__init__()
        
class Floor(Tile):
    def __init__(self):
        #creates a floor subclass (includes spawn platform and red/blue blocks)
        super().__init__()

class Wall(Tile):
    def __init__(self):
        #creates a wall subclass
        super().__init__()

class Exit(Tile):
    def __init__(self):
        #creates an exit subclass
        super().__init__()

class Lever(Tile):
    def __init__(self):
        #creates a lever subclass (includes all variants)
        super().__init__()

class Button(Tile):
    def __init__(self):
        #creates a button subclass (includes all variants)
        super().__init__()

class Rotator(Tile):
    def __init__(self):
        #creates an arrow rotator subclass (includes all variants)
        super().__init__()

class Arrow(Tile):
    def __init__(self):
        #creates a pushing arrow subclass (includes all variants)
        super().__init__()
