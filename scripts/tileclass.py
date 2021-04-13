import pygame
import gamedata
import objectclass

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
red_block = pygame.image.load('../images/red_wall.png')
blue_block = pygame.image.load('../images/blue_wall.png')
red_block_on = pygame.image.load('../images/red_floor.png')
blue_block_on = pygame.image.load('../images/blue_floor.png')

tileset = [pit, floor, wall, lever, button, arrow, rotator, goal, spawn, void, red_block, blue_block]
nameset = ["pit", "floor", "wall", "lever", "button", "arrow", "rotator", "goal", "spawn", "void", "red_block", "blue_block"]

# variable to access player object


class Tile(object):
    def __init__(self, x, y, variant, state):
        # creates a tile (variant is what type of tile it is, see the tileset list for info)
        self.x = x
        self.y = y
        self.surface = tileset[variant]
        self.name = nameset[variant]
        self.state = state
        self.state_history = [state]
        # the list above will be used for reverting changes to the states of tiles after an undo or
        # restart is triggered once tile functionality and different states are implemented

        self.is_floor = ""
        if self.name == "pit" or self.name == "wall" or self.name == "void":
            self.is_floor = False
        else:
            self.is_floor = True
        if variant == 0:
            self.__class__ = Pit
        elif variant == 1:
            self.__class__ = Floor
        elif variant == 2 or variant == 10 or variant == 11:
            self.__class__ = Wall
        elif variant == 3:
            self.__class__ = Lever
        elif variant == 4:
            self.__class__ = Button
        elif variant == 5:
            self.__class__ = Arrow
        elif variant == 6:
            self.__class__ = Rotator
        elif variant == 7:
            self.__class__ = Goal
        elif variant == 8:
            self.__class__ = Spawn
        elif variant == 9:
            self.__class__ = Void
    
    def back(self, back_num):
        #reverts the tile's state to a previous one in the state history
        self.state = self.state_history[len(self.state_history) - back_num - 1]
        for i in range(back_num):
            self.state_history.pop(-1)
            
    def turn_end(self):
        self.state_history.append(self.state)
                
    # create action funciton
    # will be overwritten in subclasses for those with actions
    # return TypeException if the superclass function runs instead of subclass function
    def action(self):
        return  # figure out how to return a type exception

    # create action funciton
    # will be overwritten in subclasses for those with actions
    #takes object so we can determine what object is moving into the spot
    def action(self, object):
        return  # figure out how to return a type exception


class Pit(Tile):
    def __init__(self):
        # creates a pit subclass
        super().__init__()        

    def action(self, object):
        """
        :return:
        """
        lm = gamedata.levelmanager
        #if its the player restart
        if isinstance(object, objectclass.Player):
            lm.level_list[lm.current_level].restart(lm.level_list[lm.current_level].moves)
            lm.level_list[lm.current_level].moves = 0
        #set object inactive otherwise
        else:
            object.active = False
            return type(self)

class Floor(Tile):
    def __init__(self):
        # creates a floor subclass (includes spawn platform and red/blue blocks)
        super().__init__()

    def action(self, object):
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

    def action(self, object):
        """
        :return:
        """
        return

    def update_state(self, red_on, blue_on):
        #updates how the wall behaves depending on which colors are on or off
        if self.name == "red_block":
            if red_on:
                self.state = 1
                self.is_floor = True
                self.surface = red_block_on
            else:
                self.state = 0
                self.is_floor = False
                self.surface = red_block
        elif self.name == "blue_block":
            if blue_on:
                self.state = 1
                self.is_floor = True
                self.surface = blue_block_on
            else:
                self.state = 0
                self.is_floor = False
                self.surface = blue_block
            
    def action(self):
        """
        :return:
        """
        return


class Goal(Tile):
    def __init__(self):
        #creates an exit subclass
        super().__init__()

    def action(self, object):
        """
        increments current_level
        :return:
        """
        gamedata.levelmanager.current_level += 1

class Lever(Tile):
    def __init__(self):
        # creates a lever subclass (includes all variants)
        super().__init__()
        # variable that tells whether this tile is red, blue, or no color (grey)
        self.type = "grey"

<<<<<<< HEAD
    def action(self, object):
=======

    def detect(self, objects):
        #detects if an object is on top of it (0 is no object, 1 is object, 2 is object but the color swap has already been triggered)
        detector = 0
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y):
                detector = 1
                if self.state == 0:
                    self.state = 1
        if detector == 0:
            self.state = 0

    def red_swap(self):
        #returns a boolean that will swap if red is on or off depending on if something triggered the lever
        if (self.type == "red" or self.type == "grey") and self.state == 1:
            if self.type == "red":
                self.state = 2
            return True
        else:
            return False

    def blue_swap(self):
        #returns a boolean that will swap if blue is on or off depending on if something triggered the lever
        if (self.type == "blue" or self.type == "grey") and self.state == 1:
            self.state = 2
            return True
        else:
            return False

    def action(self):
>>>>>>> main
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

<<<<<<< HEAD
    def action(self, object):
=======
    def detect(self, objects):
        #detects if an object is on top of it (0 is no object, 1 is object, 2 is object but the color swap has already been triggered)
        detector = 0
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y):
                detector = 1
                if self.state == 0:
                    self.state = 1
        if detector == 0 and self.state == 2:
            self.state = 1
        elif detector == 0:
            self.state = 0

    def red_swap(self):
        #returns a boolean that will swap if red is on or off depending on if something got on or off the button
        if (self.type == "red" or self.type == "grey") and self.state == 1:
            if self.type == "red":
                self.state = 2
            return True
        else:
            return False

    def blue_swap(self):
        #returns a boolean that will swap if blue is on or off depending on if something got on or off the button
        if (self.type == "blue" or self.type == "grey") and self.state == 1:
            self.state = 2
            return True
        else:
            return False
        
    def action(self):
>>>>>>> main
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

<<<<<<< HEAD
    def action(self, object):
=======
    def detect(self, objects):
        detector = 0
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y):
                detector = 1
        if detector == 1 and self.state == 0:
            self.state = 1
            #put code that checks for adjacent arrows and changes their direction here
        elif detector == 0:
            self.state = 0
                
    def action(self):
>>>>>>> main
        """
        :return:
        """
        return


class Arrow(Tile):
    def __init__(self):
        # creates a pushing arrow subclass (includes all variants)
        super().__init__()

<<<<<<< HEAD
    def action(self, object):
=======
    def push_objects(self, objects):
        #put code that checks for objects on the arrow and gives them an appropriate push request here
        return

    def action(self):
>>>>>>> main
        """
        :return:
        """
        return


class Spawn(Tile):
    def __init__(self):
        # creates a designated spawn tile
        super().__init__()

    def action(self, object):
        """
        :return:
        """
        return

class Void(Tile):
    def __init__(self):
        # creates a void so that more unique shapes other than a square can be made
        super().__init__()

    def action(self, object):
        """
        :return:
        """
        return