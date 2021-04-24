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
single_arrow_up = pygame.image.load('../images/up1.png')
rotator = pygame.image.load('../images/tile_clockwise.png')
void = pygame.image.load('../images/void.png')
red_block = pygame.image.load('../images/red_wall.png')
blue_block = pygame.image.load('../images/blue_wall.png')
red_block_on = pygame.image.load('../images/red_floor.png')
blue_block_on = pygame.image.load('../images/blue_floor.png')
red_lever = pygame.image.load('../images/red_switch.png')
blue_lever = pygame.image.load('../images/blue_switch.png')
red_button = pygame.image.load('../images/red_button.png')
blue_button = pygame.image.load('../images/blue_button.png')
double_arrow_up = pygame.image.load('../images/up2.png')
max_arrow_up = pygame.image.load('../images/upAll.png')
single_arrow_right = pygame.image.load('../images/right1.png')
single_arrow_down = pygame.image.load('../images/down1.png')
single_arrow_left = pygame.image.load('../images/left1.png')
double_arrow_right = pygame.image.load('../images/right2.png')
double_arrow_down = pygame.image.load('../images/down2.png')
double_arrow_left = pygame.image.load('../images/left2.png')
max_arrow_right = pygame.image.load('../images/rightAll.png')
max_arrow_down = pygame.image.load('../images/downAll.png')
max_arrow_left = pygame.image.load('../images/leftAll.png')
rotator_reverse = pygame.image.load('../images/tile_counter_clockwise.png')
rotator_flip = pygame.image.load('../images/tile_flip.png')
global_rotator = pygame.image.load('../images/tile_clockwise_global.png')
global_rotator_reverse = pygame.image.load('../images/tile_counter_clockwise_global.png')
global_rotator_flip = pygame.image.load('../images/tile_flip_global.png')

tileset = [pit, floor, wall, lever, button, single_arrow_up, rotator, goal, spawn, void,
           red_block, blue_block, red_lever, blue_lever, red_button, blue_button,
           double_arrow_up, max_arrow_up, rotator_reverse, rotator_flip]
nameset = ["pit", "floor", "wall", "lever", "button", "single_arrow", "rotator", "goal", "spawn", "void",
           "red_block", "blue_block", "red_lever", "blue_lever", "red_button", "blue_button",
           "double_arrow", "max_arrow", "rotator_reverse", "rotator_flip"]
arrowset = [single_arrow_up, single_arrow_right, single_arrow_down, single_arrow_left,
            double_arrow_up, double_arrow_right, double_arrow_down, double_arrow_left,
            max_arrow_up, max_arrow_right, max_arrow_down, max_arrow_left]

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
        if self.name == "wall":
            self.is_floor = False
        else:
            self.is_floor = True
        if variant == 0 or variant == 9:
            self.__class__ = Pit
        elif variant == 1 or variant == 8:
            self.__class__ = Floor
        elif variant == 2 or variant == 10 or variant == 11:
            self.__class__ = Wall
        elif variant == 3 or variant == 12 or variant == 13:
            self.__class__ = Lever
        elif variant == 4 or variant == 14 or variant == 15:
            self.__class__ = Button
        elif variant == 5 or variant == 16 or variant == 17:
            #updates the visuals for the arrows based on their type and state (faster solution than to make a seperate variant for all 12 of them)
            if self.name == "single_arrow":
                strength = 0
            elif self.name == "double_arrow":
                strength = 1
            elif self.name == "max_arrow":
                strength = 2
            self.surface = arrowset[self.state + (strength * 4)]
            self.__class__ = Arrow
        elif variant == 6 or variant == 18 or variant == 19:
            if self.state == 1:
                if self.name == "rotator":
                    self.surface = global_rotator
                elif self.name == "rotator_reverse":
                    self.surface = global_rotator_reverse
                elif self.name == "rotator_flip":
                    self.surface = global_rotator_flip
            self.__class__ = Rotator
        elif variant == 7:
            self.__class__ = Goal
    
    def back(self, back_num):
        #reverts the tile's state to a previous one in the state history
        if len(self.state_history) != 0:
            self.state = self.state_history[len(self.state_history) - back_num - 1]
            if back_num > len(self.state_history):
                print('hello')
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

    def fall_objects(self, objects):
        #makes any object on top of it fall into the pit
        #checks if there's an object on top
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y) and len(item.push_requests) == 0 and item.is_active:
                #sends falling push request
                item.push("fall", 1)

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
        # creates a floor subclass (includes spawn platform)
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

    def next_level(self, objects):
        """
        increments current_level
        :return:
        """
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y) and item.__class__ == objectclass.Player:
                pygame.mixer.music.fadeout(100)
                pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/exit.wav"))
                return True
        return False


class Lever(Tile):
    def __init__(self):
        # creates a lever subclass (includes all variants)
        super().__init__()

    def detect(self, objects):
        #detects if an object is on top of it (0 is no object, 1 is object, 2 is object but the color swap has already been triggered)
        #checks if an object is on top
        detector = 0
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y):
                pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/click.wav"))
                #if there's an object on top, make it so that a swap will be triggered with red_swap and/or blue_swap
                detector = 1
                if self.state == 0:
                    self.state = 1
        if detector == 0:
            self.state = 0

    def red_swap(self):
        #returns a boolean that will swap if red is on or off depending on if something triggered the lever
        if (self.name == "red_lever" or self.name == "lever") and self.state == 1:
            if self.name == "red_lever":
                self.state = 2
            return True
        else:
            return False

    def blue_swap(self):
        #returns a boolean that will swap if blue is on or off depending on if something triggered the lever
        if (self.name == "blue_lever" or self.name == "lever") and self.state == 1:
            self.state = 2
            return True
        else:
            return False


class Button(Tile):
    def __init__(self):
        # creates a button subclass (includes all variants)
        super().__init__()

    def detect(self, objects):
        #detects if an object is on top of it (0 is no object, 1 is object, 2 is object but the color swap has already been triggered,
        #3 is no object but color swap needs to be triggered)
        #checks if an object is on top
        detector = 0
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y):
                #if there's an object on top, make it so that a swap will be triggered with red_swap and/or blue_swap
                detector = 1
                if self.state == 0:
                    pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/click.wav"))
                    self.state = 1
        #swaps again if the object on top gets off
        if detector == 0 and self.state == 2:
            self.state = 3
        elif detector == 0:
            self.state = 0

    def red_swap(self):
        #returns a boolean that will swap if red is on or off depending on if something got on or off the button
        if (self.name == "red_button" or self.name == "button") and (self.state == 1 or self.state == 3):
            if self.name == "red_button":
                if self.state == 1:
                    self.state = 2
                else:
                    self.state = 0
            return True
        else:
            return False

    def blue_swap(self):
        #returns a boolean that will swap if blue is on or off depending on if something got on or off the button
        if (self.name == "blue_button" or self.name == "button") and (self.state == 1 or self.state == 3):
            if self.state == 1:
                self.state = 2
            else:
                self.state = 0
            return True
        else:
            return False
        

class Rotator(Tile):
    def __init__(self):
        # creates an arrow rotator subclass (includes all variants)
        super().__init__()

    def detect(self, objects, tiles, grid_size):
        #detects if an object is on top of it and changes the direction of surrounding arrows accordingly
        #checks for objects on top
        detector = 0
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y):
                detector = 1
        #changes directions of surrounding arrows
        if detector == 1 and self.state <= 1:
            if self.state == 0:
                self.state = 2
            elif self.state == 1:
                self.state = 3
            for item in tiles:
                if item.__class__ == Arrow and ((abs(tiles.index(item) - tiles.index(self)) == 1 or abs(tiles.index(item) - tiles.index(self)) == grid_size) or (self.state == 1 or self.state == 3)):
                    if self.name == "rotator":
                        pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/click.wav"))
                        item.update_direction(1)
                    elif self.name == "rotator_reverse":
                        pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/click.wav"))
                        item.update_direction(-1)
                    elif self.name == "rotator_flip":
                        pygame.mixer.Sound.play(pygame.mixer.Sound("../sounds/effects/click.wav"))
                        item.update_direction(2)
        elif detector == 0 and self.state >= 2:
            if self.state == 2:
                self.state = 0
            elif self.state == 3:
                self.state = 1
                
    def action(self):
        """
        :return:
        """
        return


class Arrow(Tile):
    def __init__(self):
        # creates a pushing arrow subclass (includes all variants)
        super().__init__()
        
    def update_direction(self, change):
        #updates the surface and direction of the arrow tile depending on the type and state
        self.state += change
        if self.state < 0:
            self.state += 4
        elif self.state > 3:
            self.state -= 4
        if self.name == "single_arrow":
            strength = 0
        elif self.name == "double_arrow":
            strength = 1
        elif self.name == "max_arrow":
            strength = 2
        self.surface = arrowset[self.state + (strength * 4)]

    def push_objects(self, objects):
        #sends a push request to any objects on top of it based on its type and state
        #changes direction of push request based on state
        direction = ""
        if self.state == 0:
            direction = "up"
        elif self.state == 1:
            direction = "right"
        elif self.state == 2:
            direction = "down"
        elif self.state == 3:
            direction = "left"
        #checks for objects on top
        for item in objects:
            if round(item.x) == round(self.x) and round(item.y) == round(self.y) and not item.is_anchored:
                #sends push request
                if self.name == "single_arrow":
                    item.push(direction, 1)
                if self.name == "double_arrow":
                    item.push(direction, 2)
                if self.name == "max_arrow":
                    item.push(direction, 20)

    def action(self):
        """
        :return:
        """
        return
