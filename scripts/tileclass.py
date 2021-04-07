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
void = pygame.image.load('../images/void.png')

tileset = [pit, floor, wall, lever, button, arrow, rotator, goal, spawn, void]
nameset = ["pit", "floor", "wall", "lever", "button", "arrow", "rotator", "goal", "spawn", "void"]

# variable to access player object


class Tile(object):
    def __init__(self, x, y, variant):
        # creates a tile (variant is what type of tile it is, see the tileset list for info)
        self.x = x
        self.y = y
        self.surface = tileset[variant]
        self.name = nameset[variant]
        self.state_history = []
        # the list above will be used for reverting changes to the states of tiles after an undo or
        # restart is triggered once tile functionality and different states are implemented

        self.is_floor = ""
        if self.name == "pit" or self.name == "wall" or self.name == "void":
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
        if variant == 9:
            self.__class__ = Void

    # create action funciton
    # will be overwritten in subclasses for those with actions
    # return TypeException if the superclass function runs instead of subclass function
    def action(self):
        return  # figure out how to return a type exception


class Pit(Tile):
    def __init__(self):
        # creates a pit subclass
        super().__init__()

    def action(self):
        """
        :return:
        """
        return


class Floor(Tile):
    def __init__(self):
        # creates a floor subclass (includes spawn platform and red/blue blocks)
        super().__init__()

    def action(self):
        """
        :return:
        """
        return


class Wall(Tile):
    def __init__(self):
        # creates a wall subclass
        super().__init__()
        # variable that tells whether this tile is red, blue, or no color (grey)
        self.type = "grey"
        # for colored tiles, tells if tile should be an active wall or not
        self.on = True

    def action(self):
        """
        :return:
        """
        return


class Goal(Tile):
    def __init__(self):
        #creates an exit subclass
        super().__init__()

    def action(self):
        """
        increments current_level
        :return:
        """
        main.current_level += 1

class Lever(Tile):
    def __init__(self):
        # creates a lever subclass (includes all variants)
        super().__init__()
        # variable that tells whether this tile is red, blue, or no color (grey)
        self.type = "grey"

    def action(self):
        """
        :return:
        """
        # change all if grey
        if self.type == "grey":
            Wall.on = not Wall.on
            # object.crate.on = not object.crate.on

        # change on Red tiles when switch is Red
        elif self.type == "red":
            if Wall.type == "red":
                Wall.on = not Wall.on   # swaps whatever state the wall is in
            # if object.crate.type == "red"
                # object.crate.on = not object.crate.on

        # change only blue tiles when switch is blue
        elif self.type == "blue":
            if Wall.type == "blue":
                Wall.on = not Wall.on   # swaps whatever state the wall is in
            # if object.crate.type == "blue"
                # object.crate.on = not object.crate.on


class Button(Tile):
    def __init__(self):
        # creates a button subclass (includes all variants)
        super().__init__()
        # variable that tells whether this tile is red, blue, or no color (grey)
        self.type = "grey"

    def action(self):
        """
        :return:
        """
        # change all if grey
        if self.type == "grey":
            Wall.on = not Wall.on
            # object.crate.on = not object.crate.on

        # change on Red tiles when switch is Red
        elif self.type == "red":
            if Wall.type == "red":
                Wall.on = not Wall.on  # swaps whatever state the wall is in
            # if object.crate.type == "red"
            # object.crate.on = not object.crate.on

        # change only blue tiles when switch is blue
        elif self.type == "blue":
            if Wall.type == "blue":
                Wall.on = not Wall.on  # swaps whatever state the wall is in
            # if object.crate.type == "blue"
            # object.crate.on = not object.crate.on


class Rotator(Tile):
    def __init__(self):
        # creates an arrow rotator subclass (includes all variants)
        super().__init__()

    def action(self):
        """
        :return:
        """
        return


class Arrow(Tile):
    def __init__(self):
        # creates a pushing arrow subclass (includes all variants)
        super().__init__()

    def action(self):
        """
        :return:
        """
        return


class Spawn(Tile):
    def __init__(self):
        # creates a designated spawn tile
        super().__init__()

    def action(self):
        """
        :return:
        """
        return

class Void(Tile):
    def __init__(self):
        # creates a void so that more unique shapes other than a square can be made
        super().__init__()

    def action(self):
        """
        :return:
        """
        return