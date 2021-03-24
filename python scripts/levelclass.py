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

    def detection(self, direction, x_change, y_change):
        #triggers the player movement
        self.objects[0].movement(self.objects, 0, direction, x_change, y_change, self.tiles, self.tile_size, self.size)
