import pygame

# class for objects that sit on top of tiles like the player and crates
player = pygame.image.load('../images/player.png')
crate = pygame.image.load('../images/crate.png')
objectset = [player, crate]
nameset = ["player", "crate"]


class Object(object):
    def __init__(self, x, y, variant):
        # creates an object (variant is what type of object it is, see the objectset list for info)
        self.x = x
        self.y = y
        self.surface = objectset[variant]
        self.name = nameset[variant]
        self.position_history = [[x, y]]
        self.state = 0
        self.state_history = [0]
        self.push_requests = []
        self.can_move = False
        self.is_anchored = False
        self.displacement = []
        self.type = "normal"
        if variant == 0:
            self.__class__ = Player
        else:
            self.__class__ = Crate

    def new_coords(self, new_x, new_y):
        # changes the object's coords to the new ones specified
        self.x = new_x
        self.y = new_y

    def push(self, direction, tiles):
        #moves an object 1/5 of the way forward (executed 5 times for smooth moving)
        self.push_requests.append([direction, tiles * 5])

    def movement_detection(self, object_list, object_index, tile_list, tile_size, grid_size, offsets, screen_size):
        # handles movement of player in the desired direction if possible, as well as making sure crates are pushed
        # correctly by the player and other crates and act solid if pushed against a wall
        for item in object_list:
            if len(item.push_requests) != 0:
                x_change = 0
                y_change = 0
                if item.push_requests[0][0] == "up":
                    condition = item.y > offsets[1] and tile_list[
                        ((round((item.y - offsets[1]) / tile_size) - 1) * grid_size) + round((item.x - offsets[0]) / tile_size)].is_floor
                    y_change = 0 - tile_size
                elif item.push_requests[0][0] == "down":
                    condition = item.y < ((screen_size[1] - offsets[1]) - tile_size) and tile_list[
                        ((round((item.y - offsets[1]) / tile_size) + 1) * grid_size) + round((item.x - offsets[0]) / tile_size)].is_floor
                    y_change = tile_size
                elif item.push_requests[0][0] == "left":
                    condition = item.x > offsets[0] and tile_list[
                        (round((item.y - offsets[1]) / tile_size) * grid_size) + (round((item.x - offsets[0]) / tile_size) - 1)].is_floor
                    x_change = 0 - tile_size
                elif item.push_requests[0][0] == "right":
                    condition = item.x < ((screen_size[0] - offsets[0]) - tile_size) and tile_list[
                        (round((item.y - offsets[1]) / tile_size) * grid_size) + (round((item.x - offsets[0]) / tile_size) + 1)].is_floor
                    x_change = tile_size
                if object_list.index(item) == object_index and condition and not item.is_anchored:
                    for item2 in object_list:
                        if item2.name == "crate" and round(item.x + x_change) == round(item2.x) and round(item.y + y_change) == round(item2.y):
                            item2.push(item.push_requests[0][0], item.push_requests[0][1] / 5)
                            if object_list[object_list.index(item2)].movement_detection(object_list, object_list.index(item2), tile_list, tile_size, grid_size, offsets, screen_size):
                                item.can_move = True
                                item.displacement = [x_change, y_change]
                                if item.name == "crate":
                                    return True
                                else:
                                    return
                            else:
                                item.push_requests.pop(0)
                                return
                    item.can_move = True
                    item.displacement = [x_change, y_change]
                    return True
                elif object_list.index(item) == object_index and (not condition or item.is_anchored):
                    item.push_requests.pop(0)
                    return False

    def movement(self):
        #handles the movement of an object if said object is able to move
        if self.can_move:
            self.new_coords(self.x + (self.displacement[0] / 5), self.y + (self.displacement[1] / 5))
            self.push_requests[0][1] -= 1
            if self.push_requests[0][1] == 0:
                self.can_move = False
                self.displacement = []
                self.push_requests.pop(0)

    def back(self, back_num):
        #reverts the object's position to a previous state in the position history
        self.new_coords(self.position_history[len(self.position_history) - back_num - 1][0],self.position_history[len(self.position_history) - back_num - 1][1])
        self.state = self.state_history[len(self.state_history) - back_num - 1]
        for i in range(back_num):
            self.position_history.pop(-1)
            self.state_history.pop(-1)

    def turn_end(self):
        #adds an entry to the position history list after the player moves
        self.position_history.append([self.x, self.y])
        self.state_history.append(self.state)

class Player(Object):
    def __init__(self, x, y):
        # creates a player subclass
        super().__init__(x, y)

class Crate(Object):
    def __init__(self, x, y):
        # creates a crate subclass (includes red/blue crates)
        super().__init__(x, y)

    def update_state(self, red_on, blue_on):
        #updates how the crate behaves depending on which colors are on or off
        if self.type == "red":
            if red_on:
                self.state = 1
                self.is_anchored = False
            else:
                self.state = 0
                self.is_anchored = True
        elif self.type == "blue":
            if blue_on:
                self.state = 1
                self.is_anchored = False
            else:
                self.state = 0
                self.is_anchored = True
