import pygame
import tileclass

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
        # if an object is active, it is able to be interacted with
        # because we still need to undo the actions of the object
        # we cannot simply delete it we must keep it in the list
        self.active = True
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

    def movement(self, object_list, object_index, direction, x_change, y_change, tile_list, tile_size, grid_size,
                 offsets, screen_size):
        # handles movement of player in the desired direction if possible, as well as making sure crates are pushed
        # correctly by the player and other crates and act solid if pushed against a wall
        next_tile = None
        for item in object_list:
            if direction == "up":
                condition = item.y > offsets[1] and tile_list[
                    ((round((item.y - offsets[1]) / tile_size) - 1) * grid_size) + round(
                        (item.x - offsets[0]) / tile_size)].is_floor
                next_tile = item.desired_tile(direction, offsets, tile_list, tile_size, grid_size)
            elif direction == "down":
                condition = item.y < ((screen_size[1] - offsets[1]) - tile_size) and tile_list[
                    ((round((item.y - offsets[1]) / tile_size) + 1) * grid_size) + round(
                        (item.x - offsets[0]) / tile_size)].is_floor
                next_tile = item.desired_tile(direction, offsets, tile_list, tile_size, grid_size)
            elif direction == "left":
                condition = item.x > offsets[0] and tile_list[
                    (round((item.y - offsets[1]) / tile_size) * grid_size) + (
                                round((item.x - offsets[0]) / tile_size) - 1)].is_floor
                next_tile = item.desired_tile(direction, offsets, tile_list, tile_size, grid_size)
            elif direction == "right":
                condition = item.x < ((screen_size[0] - offsets[0]) - tile_size) and tile_list[
                    (round((item.y - offsets[1]) / tile_size) * grid_size) + (
                                round((item.x - offsets[0]) / tile_size) + 1)].is_floor
                next_tile = item.desired_tile(direction, offsets, tile_list, tile_size, grid_size)

            # do action of the desired tile for the object
            next_tile.action(item)

            if object_list.index(item) == object_index and condition:
                for item2 in object_list:
                    if item2.name == "crate" and round(item.x + x_change) == round(item2.x) and round(
                            item.y + y_change) == round(item2.y) and item2.active:
                        item2_next_tile = item2.desired_tile(direction, offsets, tile_list, tile_size, grid_size)
                        # check if its specifically a pit so it can fall in
                        if object_list[object_list.index(item2)].movement(object_list, object_list.index(item2),
                                                                          direction, x_change, y_change, tile_list,
                                                                          tile_size, grid_size, offsets,
                                                                          screen_size) or isinstance(item2_next_tile,
                                                                                                     tileclass.Pit):
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

    def back(self, back_num):
        # reverts the object's position to a previous state in the position history
        self.new_coords(self.position_history[len(self.position_history) - back_num - 1][0],
                        self.position_history[len(self.position_history) - back_num - 1][1])
        for i in range(back_num):
            self.position_history.pop(-1)

    def update(self):
        # adds an entry to the position history list after the player moves
        self.position_history.append([self.x, self.y])


class Player(Object):
    def __init__(self, x, y):
        # creates a player subclass
        super().__init__(x, y)


class Crate(Object):
    def __init__(self, x, y):
        # creates a crate subclass (includes red/blue crates)
        super().__init__(x, y)
