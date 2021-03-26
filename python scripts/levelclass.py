import objectclass
import tileclass
import settings


class Level(object):
    def __init__(self, size, tiles, objects):
        """
        :param size: a grid of A x A tiles that define the level. int.
        :param tiles: the tiles that comprise the level. Array, ints.
        :param objects: the objects, including the player, that populate the level. Array, ints. (X pos, Y pos, Obj.)
        """

        self.size = size
        self.tiles = []
        self.objects = []
        self.tile_size = 500 / size
        center_x = ((settings.resolution_x / 2) / size) + (round(self.tile_size) * (round(size) / 2)) + (round(self.tile_size / size))
        center_y = ((settings.resolution_y / 2) / size) + (round(self.tile_size) / (round(size) / 2)) + (round(self.tile_size / size))

        # creates the grid and the lists containing the tiles and objects

        for y in range(size):
            for x in range(size):
                self.tiles.append(tileclass.Tile(round(x * self.tile_size) + center_x, round(y * self.tile_size) +
                                                 center_y, tiles[(y * size) + x]))
        for item in objects:
            self.objects.append(objectclass.Object(round((item[0] - 1) * self.tile_size) + center_x,
                                                   round((item[1] - 1) * self.tile_size) + center_y, item[2]))

    def detection(self, direction, x_change, y_change):
        #triggers the player movement
        self.objects[0].movement(self.objects, 0, direction, x_change, y_change, self.tiles, self.tile_size, self.size)
