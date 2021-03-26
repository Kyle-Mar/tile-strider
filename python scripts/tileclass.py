import pygame

# class for tiles
pit = pygame.image.load('../images/pit.png')
floor = pygame.image.load('../images/floor.png')
wall = pygame.image.load('../images/wall.png')
goal = pygame.image.load('../images/goal.png')
spawn = pygame.image.load('../images/player_spawn.png')
lever = pygame.image.load('../images/switch.png')
button = pygame.image.load('../images/button.png')
arrow = pygame.image.load('../images/right1.png')
rotator = pygame.image.load('../images/tile_clockwise.png')
tileset = [pit, floor, wall, lever, button, arrow, rotator, goal, spawn]
nameset = ["pit", "floor", "wall", "lever", "button", "arrow", "rotator", "goal", "spawn"]


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
        if variant == 3:
            self.__class__ = Lever
        if variant == 4:
            self.__class__ = Button
        if variant == 5:
            self.__class__ = Arrow
        if variant == 6:
            self.__class__ = Rotator
        if variant == 7:
            self.__class__ = Goal
        if variant == 8:
            self.__class__ = Spawn


class Pit(Tile):
    def __init__(self):
        # creates a pit subclass
        super().__init__()


class Floor(Tile):
    def __init__(self):
        # creates a floor subclass (includes spawn platform and red/blue blocks)
        super().__init__()


class Wall(Tile):
    def __init__(self):
        # creates a wall subclass
        super().__init__()


class Goal(Tile):
    def __init__(self):
        #creates an exit subclass
        super().__init__()


class Lever(Tile):
    def __init__(self):
        # creates a lever subclass (includes all variants)
        super().__init__()


class Button(Tile):
    def __init__(self):
        # creates a button subclass (includes all variants)
        super().__init__()


class Rotator(Tile):
    def __init__(self):
        # creates an arrow rotator subclass (includes all variants)
        super().__init__()


class Arrow(Tile):
    def __init__(self):
        # creates a pushing arrow subclass (includes all variants)
        super().__init__()


class Spawn(Tile):
    def __init__(self):
        # creates a designated spawn tile
        super().__init__()