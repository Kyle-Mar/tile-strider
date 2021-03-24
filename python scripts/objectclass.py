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
        if variant == 0:
            self.__class__ = Player
        else:
            self.__class__ = Crate

    def new_coords(self, new_x, new_y):
        # changes the object's coords to the new ones specified
        self.x = new_x
        self.y = new_y

    def movement(self, object_list, object_index, direction, x_change, y_change, tile_list, tile_size, grid_size):
        # handles movement of player in the desired direction if possible, as well as making sure crates are pushed
        # correctly by the player and other crates and act solid if pushed against a wall
        for item in object_list:
            if direction == "up":
                condition = item.y > 50 and tile_list[
                    ((round((item.y - 50) / tile_size) - 1) * grid_size) + round((item.x - 50) / tile_size)].is_floor
            elif direction == "down":
                condition = item.y < (550 - tile_size) and tile_list[
                    ((round((item.y - 50) / tile_size) + 1) * grid_size) + round((item.x - 50) / tile_size)].is_floor
            elif direction == "left":
                condition = item.x > 50 and tile_list[
                    (round((item.y - 50) / tile_size) * grid_size) + (round((item.x - 50) / tile_size) - 1)].is_floor
            elif direction == "right":
                condition = item.x < (550 - tile_size) and tile_list[
                    (round((item.y - 50) / tile_size) * grid_size) + (round((item.x - 50) / tile_size) + 1)].is_floor
            if object_list.index(item) == object_index and condition:
                for item2 in object_list:
                    if item2.name == "crate" and item.x + x_change == item2.x and item.y + y_change == item2.y:
                        if object_list[object_list.index(item2)].movement(object_list, object_list.index(item2), direction, x_change, y_change, tile_list,
                                     tile_size, grid_size):
                            item.new_coords(item.x + x_change, item.y + y_change)
                            if item.name == "crate":
                                return True
                            else:
                                return
                        else:
                            return
                item.new_coords(item.x + x_change, item.y + y_change)
                return True
        if object_list[object_index].name == "crate":
            return False

class Player(Object):
    def __init__(self, x, y):
        #creates a player subclass
        super().__init__(x, y)

class Crate(Object):
    def __init__(self, x, y):
        #creates a crate subclass
        super().__init__(x, y)
