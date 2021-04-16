import pygame
import tileclass

# class for objects that sit on top of tiles like the player and crates
player = pygame.image.load('../images/player.png')
crate = pygame.image.load('../images/crate.png')
red_crate = pygame.image.load('../images/red_crate.png')
blue_crate = pygame.image.load('../images/blue_crate.png')
objectset = [player, crate, red_crate, blue_crate]
nameset = ["player", "crate", "red_crate", "blue_crate"]


class Object(object):
    def __init__(self, x, y, variant):
        # creates an object (variant is what type of object it is, see the objectset list for info)
        self.x = x
        self.y = y
        self.surface = objectset[variant]
        self.name = nameset[variant]
        self.position_history = [[x, y]]
        # if an object is active, it is able to be interacted with
        # because we still need to undo the actions of the object
        # we cannot simply delete it we must keep it in the list
        self.is_active = True
        self.state = 0
        self.state_history = [[self.state, self.is_active]]
        self.push_requests = []
        self.can_move = False
        self.is_anchored = False
        self.size = 1
        self.displacement = []
        if variant == 0:
            self.__class__ = Player
        else:
            self.__class__ = Crate

    def new_coords(self, new_x, new_y):
        # changes the object's coords to the new ones specified
        self.x = new_x
        self.y = new_y

    def desired_tile(self, direction, offsets, tile_list, tile_size, grid_size):
        """
        :return Tile given a desired direction
        """
        if direction == "up":
            return tile_list[
                ((round((self.y - offsets[1]) / tile_size) - 1) * grid_size) + round((self.x - offsets[0]) / tile_size)]
        elif direction == "down":
            return tile_list[
                ((round((self.y - offsets[1]) / tile_size) + 1) * grid_size) + round((self.x - offsets[0]) / tile_size)]
        elif direction == "left":
            return tile_list[
                (round((self.y - offsets[1]) / tile_size) * grid_size) + (round((self.x - offsets[0]) / tile_size) - 1)]
        elif direction == "right":
            return tile_list[
                (round((self.y - offsets[1]) / tile_size) * grid_size) + (round((self.x - offsets[0]) / tile_size) + 1)]
        else:
            return ValueError(f"Invalid direction: {direction}")

    def push(self, direction, tiles):
        #moves an object 1/5 of the way forward (executed 5 times for smooth moving)
        self.push_requests.append([direction, tiles * 5])

    def movement_detection(self, object_list, tile_list, tile_size, grid_size, offsets, screen_size, origin_index):
        # handles movement of objects in the desired direction if possible, as well as making sure other objects are pushed
        # correctly and act solid if pushed against a wall
        #makes sure the object has any push requests before doing detection
        if len(self.push_requests) > 0:
            #checks if the object is able to move to the next tile and sets where it needs to go
            x_change = 0
            y_change = 0
            if self.push_requests[0][0] == "up":
                condition = self.y > offsets[1] and tile_list[
                    ((round((self.y - offsets[1]) / tile_size) - 1) * grid_size) + round((self.x - offsets[0]) / tile_size)].is_floor
                y_change = 0 - tile_size
            elif self.push_requests[0][0] == "down":
                condition = self.y < ((screen_size[1] - offsets[1]) - tile_size) and tile_list[
                    ((round((self.y - offsets[1]) / tile_size) + 1) * grid_size) + round((self.x - offsets[0]) / tile_size)].is_floor
                y_change = tile_size
            elif self.push_requests[0][0] == "left":
                condition = self.x > offsets[0] and tile_list[
                    (round((self.y - offsets[1]) / tile_size) * grid_size) + (round((self.x - offsets[0]) / tile_size) - 1)].is_floor
                x_change = 0 - tile_size
            elif self.push_requests[0][0] == "right":
                condition = self.x < ((screen_size[0] - offsets[0]) - tile_size) and tile_list[
                    (round((self.y - offsets[1]) / tile_size) * grid_size) + (round((self.x - offsets[0]) / tile_size) + 1)].is_floor
                x_change = tile_size
            elif self.push_requests[0][0] == "fall":
                #ends detection if the object needs to fall into a pit since that doesn't require any detection
                self.can_move = True
                self.displacement = [tile_size / 4, tile_size / 4]
                if not origin_index == object_list.index(self):
                    return True
                else:
                    return
            #checks if the object can move to the next tile and that it can be moved (the latter is only for checking if red/blue crates are off or not)
            if condition and not self.is_anchored:
                #checks if there's any objects in the space that would be moved into and runs detection to see if they can move forward
                #(if not, prevents the initial object from moving forward as well)
                for item in object_list:
                    #checks if the new object is where the original object wants to go
                    if round(self.x + x_change) == round(item.x) and round(self.y + y_change) == round(item.y) and item.is_active == True:
                        #sends a push request to the new object
                        item.push(self.push_requests[0][0], 1)
                        #does a detection to see if the new object is able to move forward
                        if object_list[object_list.index(item)].movement_detection(object_list, tile_list, tile_size, grid_size, offsets, screen_size, origin_index):
                            #allows movement for the original object if the new object can move forward
                            self.can_move = True
                            self.displacement = [x_change, y_change]
                            #if the original object isn't the object that was initially moved, it automatically returns true for the detection to save time
                            #since it will be able to move no matter what if it made it to this point in the code (if it is the initially moved object, the function ends
                            if not origin_index == object_list.index(self):
                                return True
                            else:
                                return
                        else:
                            #prevents movement for the original object if the new object can't move forward and deletes its push request
                            self.can_move = False
                            self.push_requests.pop(0)
                            return False
                #allows movement for the object if there's a non-wall tile with no objects on it in front of it
                self.can_move = True
                self.displacement = [x_change, y_change]
                return True
            #prevents movement for the object if it either can't move to the next tile or can't be moved and deletes its push request
            else:
                self.can_move = False
                self.push_requests.pop(0)
                return False

    def movement(self):
        #handles the movement of an object if said object is able to move
        if self.can_move:
            if self.push_requests[0][0] == "fall":
                #handles the shrinking of objects if they fall into a pit
                self.new_coords(self.x + (self.displacement[0] / (2 ** (5 - self.push_requests[0][1]))),
                                self.y + (self.displacement[1] / (2 ** (5 - self.push_requests[0][1]))))
                self.size *= 0.5
                self.push_requests[0][1] -= 1
                if self.push_requests[0][1] == 0:
                    self.size = 1
                    self.is_active = False
                    self.can_move = False
                    self.displacement = []
                    self.push_requests.pop(0)
            else:
                #handles the movement of objects if they go to an adjacent tile
                self.new_coords(self.x + (self.displacement[0] / 5), self.y + (self.displacement[1] / 5))
                self.push_requests[0][1] -= 1
                if self.push_requests[0][1] == 0:
                    self.can_move = False
                    self.displacement = []
                    self.push_requests.pop(0)

    def back(self, back_num):
        #reverts the object's position to a previous state in the position history
        self.new_coords(self.position_history[len(self.position_history) - back_num - 1][0],
                        self.position_history[len(self.position_history) - back_num - 1][1])
        self.state = self.state_history[len(self.state_history) - back_num - 1][0]
        self.is_active = self.state_history[len(self.state_history) - back_num - 1][1]
        for i in range(back_num):
            self.position_history.pop(-1)
            self.state_history.pop(-1)

    def turn_end(self):
        #adds an entry to the position history list after the player moves
        self.position_history.append([self.x, self.y])
        self.state_history.append([self.state, self.is_active])


class Player(Object):
    def __init__(self, x, y):
        # creates a player subclass
        super().__init__(x, y)


class Crate(Object):
    def __init__(self, x, y):
        # creates a crate subclass (includes red/blue crates)
        super().__init__(x, y)

    def update_state(self, red_on, blue_on):
        #updates how the crate behaves depending on which colors are on or off (if its color is off it can't be moved)
        if self.name == "red_crate":
            if red_on:
                self.state = 1
                self.is_anchored = False
            else:
                self.state = 0
                self.is_anchored = True
        elif self.name == "blue_crate":
            if blue_on:
                self.state = 1
                self.is_anchored = False
            else:
                self.state = 0
                self.is_anchored = True
