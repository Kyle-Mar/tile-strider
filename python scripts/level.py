import objectclass
import tileclass


class Level(object):
    def __init__(self, size, tiles, objects):
        """
        :param int Level Size, ArrayList Level Tiles, ArrayList, Objects
        """
        self.size = size
        self.tiles = []
        self.objects = []
        self.tile_size = 500 / size

        # creates the grid and the lists containing the tiles and objects

        for y in range(size):
            for x in range(size):
                self.tiles.append(tileclass.Tile(round(x * self.tile_size) + 50, round(y * self.tile_size) + 50,
                                                 tiles[(y * size) + x]))
        for item in objects:
            self.objects.append(objectclass.Object(round((item[0] - 1) * self.tile_size) + 50,
                                                   round((item[1] - 1) * self.tile_size) + 50, item[2]))


def detection(object_list, object_index, direction, x_change, y_change, tile_list, tile_size, grid_size):
    # handles movement of player in the desired direction if possible, as well as making sure crates are pushed
    # correctly by the player and other crates and act solid if pushed against a wall
    for item in object_list:
        if direction == "up":
            condition = item.y > 50 and tile_list[
                ((round((item.y - 50) / tile_size) - 1) * grid_size) + round((item.x - 50) / tile_size)].is_floor()
        elif direction == "down":
            condition = item.y < (550 - tile_size) and tile_list[
                ((round((item.y - 50) / tile_size) + 1) * grid_size) + round((item.x - 50) / tile_size)].is_floor()
        elif direction == "left":
            condition = item.x > 50 and tile_list[
                (round((item.y - 50) / tile_size) * grid_size) + (round((item.x - 50) / tile_size) - 1)].is_floor()
        elif direction == "right":
            condition = item.x < (550 - tile_size) and tile_list[
                (round((item.y - 50) / tile_size) * grid_size) + (round((item.x - 50) / tile_size) + 1)].is_floor()
        if object_list.index(item) == object_index and condition:
            for item2 in object_list:
                if item2.name == "crate" and item.x + x_change == item2.x and item.y + y_change == item2.y:
                    if detection(object_list, object_list.index(item2), direction, x_change, y_change, tile_list,
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
